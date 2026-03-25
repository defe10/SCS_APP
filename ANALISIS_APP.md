# Análisis técnico y propuestas de mejora — SCS_APP

Fecha: 2026-03-25

## 1) Resumen ejecutivo

La app tiene una base sólida para un evento: estructura modular por apps (`trivia`, `votacion`, `encuesta`, `inicio`, `usuario`), UI clara para móvil y un flujo de uso simple. Sin embargo, hoy presenta riesgos críticos de seguridad y de operación (secretos en repositorio, falta de `settings_local.py`, configuración de host permisiva y ausencia de pruebas automáticas), que pueden afectar la confiabilidad y la seguridad en producción.

## 2) Hallazgos principales

### Fortalezas
- Arquitectura separada por dominios funcionales (`trivia`, `votacion`, `encuesta`) que facilita iteración por módulo.
- Restricción de voto único por usuario vía `unique_together` en modelos de votación/encuesta.
- Uso de `login_required` en pantallas principales de interacción.
- Flujo de trivia con feedback inmediato y sesión de puntaje.

### Riesgos críticos
1. **Secretos expuestos en código**:
   - `SECRET_KEY` hardcodeada.
   - Credenciales de base de datos y `INSTANCE_CONNECTION_NAME` en `app.yaml`.
2. **Entorno local roto por defecto**:
   - `settings/__init__.py` intenta importar `settings_local.py`, pero ese archivo no existe.
3. **Configuración insegura para producción**:
   - `ALLOWED_HOSTS = ['*']`.
   - Sin validadores de contraseña (`AUTH_PASSWORD_VALIDATORS = []`).
   - `ACCOUNT_EMAIL_VERIFICATION = 'none'`.
4. **Calidad y mantenibilidad**:
   - Sin tests reales (todos los `tests.py` vacíos).
   - Lógica repetida entre `votacion` y `encuesta`.
   - Falta de validación explícita del valor recibido en POST para votos.
5. **Inconsistencias operativas/documentación**:
   - README menciona SQLite, pero settings de producción usan PostgreSQL Cloud SQL.
   - Diferencia entre dependencias raíz y subproyecto (`psycopg2-binary` sólo en una).

## 3) Priorización recomendada (plan 30 días)

### Semana 1 — Seguridad y estabilidad (alto impacto)
- Rotar **inmediatamente** todos los secretos expuestos (DB, secret key).
- Mover secretos a Secret Manager / variables de entorno de despliegue.
- Crear `settings_local.py` y `settings_base.py` para separar local/prod.
- Restringir `ALLOWED_HOSTS`, activar `SECURE_*` y `CSRF_TRUSTED_ORIGINS`.
- Rehabilitar validadores de contraseña y rate limiting para login.

### Semana 2 — Confiabilidad y DX
- Agregar suite inicial de tests:
  - Modelos: restricción de voto único.
  - Vistas: acceso autenticado, votación única, manejo de inputs inválidos.
  - Trivia: progresión y cálculo de puntaje.
- Configurar CI (GitHub Actions) para `python manage.py check` + `pytest/manage.py test` + lint.

### Semana 3 — Modelo de datos y analítica
- Añadir timestamps (`created_at`) a votos y respuestas.
- Estandarizar catálogos de escala de valoración.
- Crear panel admin/consultas para exportar resultados por película, sección y día.

### Semana 4 — UX y producto
- Mejorar accesibilidad móvil (botones, contraste, labels, estados vacíos).
- Agregar mensajes de confirmación de voto y posibilidad de revisar respuesta antes de enviar.
- Implementar tracking básico de eventos (sin PII) para medir embudo de participación.

## 4) Propuestas concretas de refactor

1. **Consolidar lógica de votación**
   - Extraer patrón común `lista + votar` de `votacion` y `encuesta` en mixins o servicio de aplicación.
2. **Endurecer validación de POST**
   - Verificar que `valor` esté dentro de opciones permitidas antes de crear el voto.
3. **Mejorar robustez de trivia**
   - Evitar hardcode de “de 12” en template y calcular total dinámicamente.
4. **Internacionalización/localización**
   - Cambiar `LANGUAGE_CODE` y `TIME_ZONE` a configuración real del evento o parametrizable por entorno.
5. **Static files y despliegue**
   - Revisar `STATIC_ROOT` y carpeta servida por App Engine para evitar conflictos (`static/` vs `staticfiles/`).

## 5) KPI sugeridos para medir mejora

- % de usuarios autenticados que completan al menos una acción (trivia/voto/encuesta).
- Tasa de finalización de trivia.
- Tiempo medio de votación por ítem.
- Errores 4xx/5xx por día.
- Cobertura de tests y tiempo de pipeline CI.

## 6) Riesgos de no actuar

- Compromiso de base de datos por secretos expuestos.
- Caídas o imposibilidad de ejecutar en local por settings incompletos.
- Dificultad para evolucionar rápido sin romper funcionalidades por falta de tests.

## 7) Próximos pasos inmediatos (48 horas)

1. Rotar secretos y limpiar historial si fue público.
2. Crear configuración local funcional.
3. Añadir 5–8 tests críticos de voto único y auth.
4. Activar pipeline CI mínimo.

