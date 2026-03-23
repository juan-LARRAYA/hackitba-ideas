## 💳 Fintech & Finanzas Inteligentes

## consultar

#### colateral para compra de acciones con activos

#### Apalancamiento del 100% como hacen empresas de afuera .

### IDEAS VALIDADAS

| califi(0-5)      | F1-splitar | F2-sn inv | F3-CashFlowSME | F4-InversorSimple | F5-Scrapper |
| ---------------- | ---------- | --------- | -------------- | ----------------- | ----------- |
| juan             | 3          | 5         | 3              | 4                 | 5           |
| yerson           | 0          | 3         | 2              | 3                 | 5           |
| marcos           | 3          | 3         | 1              | 3                 | 5           |
| **_puntuacion_** | 2          | 3.7       | 2              | 3.3               | 5           |

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

#### F2. Red social de inverion — compartir carteras de inversión

Lugar donde las personas comparten sus carteras de inversión en porcentajes. Se puede crear manualmente o conectar con brokers/plataformas locales como iiol, Cocos Capital, Bull Market, PPI, etc.

> _Nota de Juan: Puede ser un producto separado de SplitAR pero ambas ideas son muy valiosas._

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

#### F4. InversorSimple — Recomendador de inversiones

Explicás en lenguaje natural cuánto tenés y qué querés ("quiero preservar capital en dólares") y te recomienda instrumentos financieros argentinos (cedears, FCIs, crypto) con comparativa de rendimiento.

**Pain points:**

- Los inversores minoristas no entienden los instrumentos financieros disponibles
- Las plataformas de brokerage muestran listas de instrumentos sin contexto
- El asesoramiento financiero personal es caro
- El contexto argentino (inflación, cepo, brecha cambiaria) hace la decisión mucho más compleja que en otros países

### F5 Aplicacion de compras con ai scrapeando todos los medio de compra.

APP para recopilar precios de cosa y comprar el mas barato.
