# HackITBA — Ideas Pool

> Documento vivo. No se borra nada, solo se agrega. Las ideas validadas serán las que lleven a la implementación.

---

## 🤖 Automatización & IA

### IDEAS PROPIAS (descritas por Juan)

#### A1. OutlookAgent — Agente de control de mails corporativos
Un agente que controle los mails principalmente con Outlook, ya que es el principal cliente de correo corporativo. El agente debe poder leer, clasificar, responder y ejecutar acciones sobre los correos de forma autónoma o semi-autónoma.

**Pain points que resuelve:**
- Los profesionales reciben 100+ mails diarios y pierden horas respondiendo
- Outlook es el cliente dominante en empresas y tiene API robusta (Microsoft Graph)
- La IA generativa puede leer contexto, priorizar y redactar respuestas coherentes
- Integración natural con Teams, Calendar y Tasks del ecosistema Microsoft

**Tech stack sugerido (48hs):**
- Microsoft Graph API para leer/enviar mails desde Outlook
- Agente LLM (Claude / GPT-4o) para clasificación y redacción
- Next.js + Supabase para dashboard
- OAuth 2.0 con Microsoft para autenticación empresarial

**Features posibles:**
- Clasificación automática por urgencia y tipo
- Borrador automático de respuestas para aprobación humana
- Reglas personalizadas ("si el asunto tiene URGENTE, notificar por SMS")
- Resumen diario de inbox a las 8am
- Detección de threads sin respuesta hace más de X días

---

#### A2. FileWatcher — Sistema de analíticas de contribuciones a base de documentos
Sistema para evaluar las contribuciones de cada persona a una base de documentos. Principalmente un servidor corriendo en Windows Server. Interesa ver quién cambió cada archivo (nombre de PC), horario, y hacer analíticas de quién modifica más archivos y qué tipo de archivos modifican.

**Pain points que resuelve:**
- En empresas con servidores de archivos compartidos no hay visibilidad de actividad
- Imposible saber quién editó un archivo sin auditoría manual
- No existe forma simple de ver patrones de trabajo por equipo
- Útil para RRHH, gerencia y auditorías internas

**Tech stack sugerido (48hs):**
- Windows Event Log / File System Watcher (ReadDirectoryChangesW) para capturar eventos
- Agente Python en Windows Server que pushea eventos a una API
- Backend Node.js/FastAPI + PostgreSQL para almacenar eventos
- Dashboard con gráficos de actividad (React + Recharts)

**Features posibles:**
- Timeline de modificaciones por archivo
- Ranking de usuarios más activos por tipo de archivo
- Alertas cuando se modifican archivos sensibles fuera de horario laboral
- Heatmap de actividad por hora/día/usuario
- Exportación de reportes para auditoría
- Detección de eliminación masiva de archivos (alerta de posible incidente)

---

#### A3. ReplyFast — Sistema de respuestas rápidas para ventas minoristas
Sistema para ventas minoristas que permita contestar mensajes rápido de Mercado Libre y Facebook Marketplace. El objetivo es reducir el tiempo de respuesta y aumentar la tasa de conversión de consultas a ventas.

**Pain points que resuelve:**
- Vendedores minoristas manejan múltiples plataformas desde el celular
- Responder tarde = perder la venta (ML penaliza respuestas lentas)
- Respuestas repetitivas que se podrían automatizar parcialmente
- No hay una bandeja unificada para ML + Facebook Marketplace

**Tech stack sugerido (48hs):**
- MercadoLibre API (Mensajes de preguntas y chats de ventas)
- Facebook Graph API (Messenger para Marketplace)
- Agente LLM para sugerir respuestas basadas en el catálogo del vendedor
- React Native / PWA para mobile-first

**Features posibles:**
- Bandeja unificada ML + Facebook Marketplace
- Respuestas sugeridas con un tap para aprobar y enviar
- Templates personalizables por tipo de consulta (precio, disponibilidad, envío)
- Alertas de consultas sin responder
- Score de tiempo de respuesta (como lo mide ML)
- Historial del comprador para dar seguimiento personalizado
- Generación automática de respuesta basada en descripción del producto

---

### IDEAS ADICIONALES (generadas)

#### A4. ContractAI — Revisor de contratos para PYMEs
Subís un PDF de contrato y un agente LLM te explica los riesgos, cláusulas abusivas y qué negociar. Para PYMEs que no pueden pagar un abogado por cada contrato.

**Pain points:**
- Contratos de proveedores, alquileres comerciales y servicios son largos y en lenguaje legal
- Un error en un contrato puede costar miles de pesos
- Acceso a abogados es caro para PYMEs

**Tech stack:** PDF parsing (PyMuPDF) + LLM con función de análisis estructurado + UI simple

---

#### A5. SupportPilot — Agente de soporte que aprende de tickets
Agente que aprende de tickets históricos de Zendesk/Intercom y responde el 80% automáticamente. Se escala solo cuando no tiene confianza suficiente.

**Pain points:**
- Equipos de soporte repiten las mismas respuestas decenas de veces por día
- El onboarding de agentes nuevos es lento
- Los tickets urgentes se mezclan con consultas básicas

**Tech stack:** RAG sobre tickets históricos + LLM + API de Zendesk/Intercom

---

#### A6. DataJanitor — Limpiador inteligente de bases de datos
Conectás tu DB o Google Sheets y un agente detecta inconsistencias, duplicados y datos faltantes. Genera reporte + script SQL para limpiarla.

**Pain points:**
- Bases de datos sucias generan errores de negocio
- Limpiar datos es tedioso y requiere conocimiento técnico
- No existe una herramienta simple para no-técnicos que identifique problemas

**Tech stack:** Conectores DB + LLM para análisis semántico + generación de SQL

---

#### A7. HireBot — Screening de CVs con agente IA
Agente que procesa CVs, hace primer filtro con criterios del recruiter y agenda entrevistas automáticamente por email. Sin ATS caro.

**Pain points:**
- Leer 200 CVs por posición consume días
- Las plataformas de ATS cuestan miles de dólares al mes
- El filtrado manual introduce sesgos inconsistentes

**Tech stack:** Parsing de PDFs + LLM para scoring + envío de emails via SMTP/SendGrid

---

#### A8. MeetingMind — Resumen automático de reuniones
Agente que se une a reuniones de Zoom/Meet, transcribe, extrae action items y los manda automáticamente a Notion/Slack/email. Cero fricción post-reunión.

**Pain points:**
- El 40% del tiempo en reuniones se pierde sin acuerdos documentados
- Los action items no siempre se registran ni se les da seguimiento
- Zoom/Meet tienen transcripción pero no post-procesamiento útil

**Tech stack:** Recall.ai o Whisper para transcripción + LLM para extracción de tareas + webhooks a Notion/Slack

---

---

## 📈 Marketing & Growth

> **Premisa central validada por Juan:** El marketing hecho por personas tiene más efectividad que el hecho por IA. Las herramientas deben *amplificar* al humano, no reemplazarlo. Las ideas nuevas nacen de investigar los pain points reales de profesionales de marketing.

### IDEAS VALIDADAS

#### M1. CohortLens — Analytics de retención sin data analyst
Conectás tu base de datos de usuarios (Postgres/BigQuery) y te muestra retención por cohortes, LTV y churn automáticamente. Sin necesitar un data analyst.

**Pain points:**
- Las empresas saben que el churn es un problema pero no tienen visibilidad en tiempo real
- Contratar un data analyst es caro para una startup o PYME
- GA4 y Mixpanel son complejos de configurar correctamente
- Los fundadores quieren saber "cuántos de los usuarios de enero siguen activos hoy"

**Tech stack sugerido:** Conectores a Postgres/BigQuery/Supabase + motor de cohortes propio + React con gráficos de retención + exportación a CSV

---

#### M2. LocalBoost — Marketing automático para negocios físicos
Para negocios físicos: genera contenido de redes sociales localizado (barrio, ciudad), sugiere horarios y publica automáticamente. Pensado para el dueño que no sabe de marketing.

**Pain points:**
- El dueño de una panadería, peluquería o ferretería no tiene tiempo ni conocimiento de redes
- Las agencias cobran caro para contenido básico
- El contenido genérico no conecta con la audiencia local
- Sin presencia online pierden clientes frente a competidores que sí postean

**Tech stack sugerido:** LLM para generación de texto localizado + conexión a Instagram/Facebook API + geolocalización para adaptar vocabulario y referencias locales

---

### IDEAS NUEVAS (basadas en investigación de herramientas profesionales)

> Herramientas que los profesionales de marketing ya usan y sus limitaciones conocidas:
> - **Hootsuite / Buffer / Sprout Social**: Gestión de redes, pero caros, interfaces viejas, sin soporte para plataformas emergentes
> - **SEMrush / Ahrefs**: SEO, pero complejos para no-técnicos y costosos por usuario adicional
> - **GA4 / Looker Studio**: Analytics, pero curva de aprendizaje enorme; crear el primer reporte toma 40+ horas
> - **Mailchimp / ActiveCampaign**: Email marketing, pero precios escalan agresivamente y cobran por desuscriptos
> - **Jasper / ChatGPT para contenido**: Buenos para velocidad, pero el contenido pierde la voz auténtica del profesional

---

#### M3. VoiceGuard — Guardián de voz de marca para equipos
Cuando múltiples personas del equipo crean contenido (social, email, blog), mantener coherencia de voz de marca es casi imposible. VoiceGuard es una capa que se integra a Notion, Google Docs y el editor de Hootsuite/Buffer para analizar en tiempo real si el contenido que está escribiendo el equipo es consistente con el tono y estilo de la marca.

**Pain points reales:**
- Equipos de 3+ personas publicando sin guía de estilo consistente → marca fragmentada
- Las guías de estilo se escriben y nadie las lee
- Las agencias y freelancers externos se alejan aún más del tono real
- El feedback de "esto no suena a nosotros" es subjetivo y genera fricción

**Diferenciador respecto a AI genérica:** No genera el contenido, *evalúa* lo que el humano escribió. Mantiene al humano como autor, usa IA como editor.

**Tech stack:** LLM fine-tuned o few-shot con ejemplos de contenido aprobado + extensión de Chrome + API para integraciones + dashboard de métricas de consistencia

---

#### M4. CreatorBridge — Plataforma de colaboración con micro-creadores locales
Las herramientas de influencer marketing (GRIN, HypeAuditor, Upfluence) están pensadas para grandes marcas con presupuesto de USD 5K+/mes. CreatorBridge conecta PYMEs y marcas medianas con micro-creadores (1K-50K seguidores) de su ciudad/nicho, facilitando colaboraciones de canje o micropago.

**Pain points reales:**
- Las marcas chicas quieren trabajar con creadores pero no tienen herramienta ni contacto
- Los micro-creadores no tienen representación y cobrar es complicado
- El tracking de resultados de una colaboración de canje no existe
- El mercado argentino no tiene plataforma local (todas las herramientas son en USD)

**Diferenciador:** Enfocado en Argentina, soporta pago en pesos/ML, integración con Instagram para métricas reales de la colaboración.

**Tech stack:** Marketplace con perfiles de creadores + Instagram Graph API para validar métricas reales + sistema de briefing y aprobación de contenido + pago vía MercadoPago

---

#### M5. RepurposeAI — Motor de repurposing de contenido humano
El problema no es crear contenido desde cero con IA (eso ya existe y el resultado es genérico). El problema es tomar *lo que un humano ya creó* — una charla, un podcast, una entrevista, un hilo de Twitter — y convertirlo automáticamente en 10 formatos distintos manteniendo la voz original.

**Pain points reales (investigados):**
- Los profesionales de marketing producen contenido valioso (charlas, reportes, entrevistas) pero solo en un formato
- Repurposear manualmente toma horas y el resultado pierde la esencia
- Las herramientas actuales (Lumen5, Descript) son buenas para video pero no tienen el enfoque "voz auténtica"
- El 80% del valor de una conferencia se pierde porque el video no se convierte en posts, newsletter, etc.

**Flujo:** Subís audio/video/texto → extrae las mejores citas y momentos → genera versiones para LinkedIn, Twitter/X, newsletter, blog, Reels (con script), Stories. El humano aprueba y ajusta cada pieza.

**Tech stack:** Whisper para transcripción + LLM para extracción de ideas clave + templates por formato + conexión a Buffer/Hootsuite para schedulear directo

---

#### M6. BrandAudit — Auditoría de presencia de marca para freelancers y consultores
Un profesional independiente (consultor, coach, abogado, arquitecto) no sabe cómo se percibe su marca online. BrandAudit analiza su LinkedIn, Instagram, sitio web y reseñas de Google My Business, y devuelve un reporte con: coherencia visual, tono de comunicación, keywords por las que aparece, gaps vs. su competencia directa, y 10 acciones concretas para mejorar.

**Pain points reales:**
- Las agencias cobran USD 500+ por una auditoría de marca básica
- Los profesionales independientes no saben por dónde empezar
- No existe herramienta self-service que unifique todas las fuentes
- Saben que tienen que mejorar su presencia pero no tienen el diagnóstico

**Diferenciador:** Output accionable, no solo métricas. Priorizado por impacto. Sin necesidad de conocimiento de marketing.

**Tech stack:** Scraping de LinkedIn/IG (con restricciones) + Google My Business API + análisis LLM + generación de reporte en PDF

---

#### M7. PitchDeck Validator — Validador de narrativa de marketing para founders
Antes de lanzar una campaña o mandar un deck a un inversor, los founders y marketers necesitan saber si su narrativa de propuesta de valor realmente conecta. PitchDeck Validator muestra el deck o la landing page a un panel de "usuarios simulados" con perfiles distintos y analiza dónde se pierde la atención, qué es confuso y qué genera conversión.

**Pain points reales:**
- Los founders tienen sesgos enormes sobre su propio producto → no pueden evaluar si la narrativa funciona
- Los focus groups son caros y lentos
- Las herramientas de A/B testing requieren tráfico previo
- El feedback de inversores llega tarde y sin detalle

**Diferenciador:** Feedback inmediato antes de lanzar, no después. Múltiples perfiles de usuario simulados (inversor, cliente B2B, cliente B2C).

**Tech stack:** LLM con personas definidas evaluando el contenido + parsing de PDFs/URLs + reporte estructurado con scoring por sección

---

---

## 💳 Fintech & Finanzas Inteligentes

### IDEAS VALIDADAS

#### F1. SplitAR — App argentina para dividir gastos
App para dividir gastos entre amigos adaptada a Argentina: maneja pesos, dólares y crypto. Reconcilia con Mercado Pago/Uala. Sin depender de Splitwise en USD.

**Pain points:**
- Splitwise no tiene integración con el ecosistema argentino de pagos
- Las deudas en pesos se deprecian rápido → necesitás saber si la deuda era en pesos o en dólares al momento de generarse
- Pagar la deuda debería ser un tap desde la misma app

**Features clave mencionados por Juan:**
- Conexión con MercadoPago y Uala de cada persona del grupo → las deudas se saldan directamente desde la app
- Soporte nativo para múltiples monedas: ARS, USD, USDT
- Historial de deudas con fecha y cotización del día

---

#### F2. CarperaShare — Plataforma para compartir carteras de inversión
Lugar donde las personas comparten sus carteras de inversión en porcentajes. Se puede crear manualmente o conectar con brokers/plataformas locales como iiol, Cocos Capital, Bull Market, PPI, etc.

> *Nota de Juan: Puede ser un producto separado de SplitAR pero ambas ideas son muy valiosas.*

**Pain points:**
- En Argentina no hay una plataforma pública donde los inversores minoristas comparten sus carteras (como lo hace la comunidad en Reddit/r/investing o en Etoro)
- Los influencers financieros muestran sus picks pero no sus carteras reales
- No existe forma de validar socialmente si una estrategia funciona
- Los brokers locales no tienen feature de "seguir cartera"

**Features clave:**
- Conectar cuenta de iiol / Cocos / PPI via API o CSV de exportación
- Vista pública de cartera en % (sin montos absolutos para privacidad)
- Seguir carteras de otros usuarios
- Feed de cambios: "Juan agregó 5% de CEDEAR de Apple"
- Benchmark vs. inflación, dólar y S&P500

**Tech stack:** Integraciones via CSV/API con brokers locales + React + Supabase + gráficos de cartera en tiempo real

---

#### F3. CashFlowSME — Dashboard de flujo de caja para PYMEs argentinas
Dashboard que conecta con AFIP y el banco y predice liquidez a 30/60/90 días. Alerta antes de quedarte sin caja.

**Pain points reales de una PYME en flujo de pagos:**

1. **Cobranzas impredecibles**: Los clientes pagan a 30/60/90 días pero los proveedores exigen pago inmediato. Sin visibilidad del flujo futuro, la empresa vive en emergencia financiera constante.

2. **Cheques diferidos**: Muchas PYMEs operan con cheques propios y de terceros. Llevar el control de qué cheques vencen cuándo, si hay fondos para cubrirlos, y qué cheques de terceros pueden descontarse → se hace en Excel o "de memoria".

3. **Retenciones de AFIP**: Los clientes grandes retienen entre 1% y 11% de cada factura (IVA, Ganancias, IIBB). Eso genera saldo a favor en AFIP que tarda meses en recuperarse y destruye el flujo de caja.

4. **IVA como trampa de liquidez**: El IVA se paga el día 20 del mes siguiente aunque el cliente no haya pagado todavía. Una PYME puede tener ganancias en papel y estar quebrada en caja por el IVA.

5. **Falta de proyección**: El contador hace el balance anual, no el flujo semanal. El dueño de la PYME no tiene visibilidad de "¿tengo plata para pagar los sueldos el 10?".

6. **Múltiples cuentas bancarias**: Cuenta corriente, caja de ahorro, cuenta comitente, billetera virtual → la plata está en varios lados y no hay vista unificada.

7. **Financiamiento reactivo**: Se pide el préstamo cuando ya no hay caja, no preventivamente cuando el banco da mejores condiciones.

**Features del producto:**
- Sincronización bancaria (via Home Banking scraping o PSD2-like)
- Carga manual de facturas a cobrar y a pagar con fecha estimada
- Proyección de flujo de caja en gráfico de 90 días
- Alerta "te quedás sin fondos en 15 días si no cobrás X"
- Dashboard de retenciones acumuladas en AFIP recuperables
- Agenda de vencimientos impositivos (IVA, IIBB, Ganancias)

---

#### F4. MonoFlow — CashFlow para monotributistas y freelancers

> *Variante de CashFlow pensada para el segmento monotributista, que tiene pain points distintos a la PYME.*

**Pain points específicos del monotributista:**

1. **Riesgo de recategorización**: El monotributista tiene que facturar dentro de un rango anual. Si factura de más, sube de categoría (cuota más cara). Si factura de menos, puede ser excluido. Hoy no existe alerta que diga "vas a superar tu categoría en 2 meses si seguís a este ritmo".

2. **Guardar para el impuesto**: El pago mensual de monotributo es fijo, pero también hay que pagar Ganancias anual (si se pasa a autónomos o si tiene otros ingresos). Muchos freelancers gastan todo lo que entra y después no tienen para pagar.

3. **Facturación en pesos vs. dólar**: Un freelancer cobra en USD (transferencia, USDT, Payoneer) y factura en pesos al tipo de cambio del día. El seguimiento de cuánto cobraste en dólares, cuánto convertiste, a qué tipo de cambio → se hace en Excel o no se hace.

4. **Proyección de ingreso anual**: A mitad de año no saben si van a superar el tope de su categoría de monotributo. Tampoco saben si conviene pasarse a responsable inscripto.

5. **Sin herramientas de ahorro sistematizado**: Un empleado tiene el sueldo neto directo. Un freelancer recibe el bruto y tiene que separar manualmente lo que es "del fisco".

**Features del producto:**
- Tracker de facturación acumulada en el año fiscal vs. tope de categoría actual
- Alerta cuando estás al 80% del tope (con proyección de cuándo lo alcanzás)
- Separación automática del cobro: "de este pago, X% es para monotributo y Y% para ahorro"
- Calculadora de conveniencia: ¿me conviene pasar a RI?
- Tracker de ingresos en USD con historial de tipo de cambio utilizado
- Recordatorio de vencimientos (monotributo se paga los últimos días de cada mes)

**Tech stack:** Next.js + Supabase + integración con AFIP Facturación Electrónica + alertas por WhatsApp (Twilio)

---

#### F5. InversorSimple — Recomendador de inversiones en lenguaje natural
Explicás en lenguaje natural cuánto tenés y qué querés ("quiero preservar capital en dólares") y te recomienda instrumentos financieros argentinos (cedears, FCIs, crypto) con comparativa de rendimiento.

**Pain points:**
- Los inversores minoristas no entienden los instrumentos financieros disponibles
- Las plataformas de brokerage muestran listas de instrumentos sin contexto
- El asesoramiento financiero personal es caro
- El contexto argentino (inflación, cepo, brecha cambiaria) hace la decisión mucho más compleja que en otros países

**Tech stack:** LLM con contexto de instrumentos financieros ARG actualizados (Cedears, FCI, ONs, Cauciones) + API de precios en tiempo real (BYMA/IOL) + interfaz conversacional

---

#### F6. FreelanceWallet — Optimizador de conversión para freelancers con ingresos en USD
Para freelancers que cobran en USD: optimiza la conversión (MEP, CCL, cripto), trackea ingresos en ambas monedas y genera resumen para declarar.

**Pain points:**
- La diferencia entre convertir por MEP, CCL, crypto o dólar cable puede ser del 5-10%
- Los freelancers hacen la conversión "cuando pueden" sin estrategia
- Declarar ingresos en USD requiere saber el tipo de cambio oficial del día de cobro
- No hay herramienta que unifique los distintos métodos de conversión argentinos

**Tech stack:** Scraping de tipos de cambio en tiempo real (MEP, CCL, blue, cripto) + calculadora de resultado neto por método + exportación de informe para el contador

---

*Última actualización: sesión de brainstorm HackITBA 2026*
