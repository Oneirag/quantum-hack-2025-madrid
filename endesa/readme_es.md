
# Optimización conjunta de un sistema de batería y parque eólico

## Contexto

La integración de fuentes de energía renovable en los sistemas eléctricos, como la eólica, plantea retos y oportunidades. El principal desafío es la variabilidad de la producción, que puede no coincidir con los momentos de mayor demanda o precio en el mercado eléctrico. Para gestionar esta variabilidad y maximizar los ingresos, es habitual complementar los parques eólicos con sistemas de almacenamiento energético, como baterías. Estos sistemas permiten almacenar energía cuando la producción eólica es alta y los precios son bajos, y liberarla cuando los precios son más elevados.

## Descripción del problema

El objetivo es maximizar el ingreso conjunto de un parque eólico y una batería a lo largo de un horizonte de un día (24 horas). Se debe determinar la estrategia óptima de operación de la batería (cuándo cargar y descargar), considerando la producción eólica y los precios horarios del mercado eléctrico.

La estrategia de operación de la batería se determina el día anterior, basándose en la previsión de producción eólica. Dado que la producción varía y no se puede predecir con exactitud, se facilitan 13 escenarios de previsión de producción del parque eólico (equiprobables). La estrategia óptima no debe basarse en un solo escenario, sino que debe maximizar el ingreso esperado en todos ellos.

La batería puede alimentarse tanto de la generación del parque eólico como de la red eléctrica. Ambas instalaciones se consideran como un portfolio, sumando ingresos y costes para obtener un margen conjunto.

## Datos disponibles

**Fichero:** `input_data.csv`

Estructura del fichero:

- **hour:** Hora del día (1 a 24).
- **scenario_1 a scenario_13:** Predicciones de producción eólica (MWh) para los 13 escenarios equiprobables.
- **price:** Precio del mercado eléctrico (€/MWh), único para todos los escenarios.

Este formato permite modelar la incertidumbre en la producción eólica y facilita la toma de decisiones óptimas considerando la variabilidad de la generación renovable y la evolución de los precios eléctricos.

## Características físicas de la batería

- Capacidad máxima de almacenamiento: **16 MWh**
- Potencia máxima de carga: **5,0 MW**
- Potencia máxima de descarga: **4,0 MW**
- Eficiencia de carga: **80%** (por cada 5 MW consumidos de la red en carga, solo 4 MW se almacenan)
- Eficiencia de descarga: **100%**
- Número máximo de ciclos completos de carga-descarga por día: **2**
- La batería comienza descargada y debe terminar descargada al final del día.
- No se consideran costes adicionales a la compra de energía de la red.

## Requisitos del ejercicio

- Plantear el modelo de optimización para decidir, hora a hora, cuánta energía debe almacenar la batería y cuánta se descarga para su venta.
- Considerar la incertidumbre en la producción eólica utilizando los 13 escenarios equiprobables. El objetivo es maximizar el ingreso esperado.
- Incluir todas las restricciones físicas de la batería y la condición de estado inicial y final (batería descargada al principio y al final del día).
- En cada hora, la batería solo puede estar cargando o descargando, no ambas cosas a la vez.
- La batería compra y vende toda su energía de la red al precio del mercado, sin neteos con el parque eólico.
- Presentar y justificar las decisiones de modelado (variables, función objetivo, restricciones, etc.).
- Resolver el problema con la herramienta que se considere adecuada e interpretar los resultados. Documentar y justificar cualquier simplificación realizada.

## Entregables

- Documento explicativo del modelo, variables y restricciones.
- Código empleado para resolver el problema.
- Resultados obtenidos e interpretación.
- Opcional: análisis de sensibilidad ante cambios en los parámetros de la batería o precios del mercado.

## Notas adicionales

- Se asume que la batería y el parque eólico están conectados al mismo punto de conexión a red y pueden operar de forma coordinada.
- No existen pérdidas de energía adicionales más allá de la eficiencia de carga especificada.
- Justificar cualquier supuesto adicional necesario para la resolución del problema.

---

¡Buena suerte! Si tienes dudas sobre los datos o el planteamiento, no dudes en consultarlas.
