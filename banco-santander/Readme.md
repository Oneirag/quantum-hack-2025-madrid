# **Challenge name**

**Quantum Credit – Exploring the Frontier Between Classical and Quantum ML**

---

## **1. Motivation**

Credit risk assessment is a core function in modern finance, determining who gets access to capital and under what conditions. Classical machine learning models, such as **XGBoost**, already provide robust predictive capabilities—but the rise of **quantum computing** promises to reshape how complex, high-dimensional data can be processed and optimized.

This challenge invites participants to test that promise: can quantum machine learning methods match or outperform classical algorithms in predicting credit risk? You’ll explore this frontier by implementing both approaches and comparing their results.

---

## **2. The Challenge: Predicting Credit Risk**

### **2.1 Problem Description**

Your task is to predict credit default risk for individual borrowers using financial and personal indicators.
You will:

* Analyze a classical **XGBoost** model provided as a reference implementation (you are free to build your own if you prefer).
* Reformulate and solve the same problem using quantum and hybrid quantum-classical approaches.
* Compare the results in terms of accuracy, interpretability, and efficiency.

**Dataset:** A reduced credit risk dataset (`credit_risk_dataset_red.csv`) containing **3,000 samples** with financial and personal features. The accompanying Jupyter notebook provides detailed information about each variable and feature engineering examples.

**Note:** This proposal is especially focused on scenarios with limited samples and features, making it ideal for testing quantum advantage in small-data regimes.

---

## **3. Resources**

The following tools and data will be available to all teams:

**Quantum SDKs:** Access to the **IQM Resonance** environment and compatible SDKs such as **PennyLane**, **Qiskit**, or **Cirq**.

**Dataset:**
The provided CSV file (`credit_risk_dataset_red.csv`) contains **3,000 samples** with personal and loan-related features, including:

* Personal information (age, income, employment length, home ownership status).
* Loan characteristics (amount, interest rate, loan grade, loan intent).
* Financial ratios and creditworthiness indicators.
* Target label: binary classification for credit default risk.

Detailed variable descriptions and exploratory data analysis are available in the accompanying Jupyter notebook (`Reduced-credit-risk-prediction.ipynb`).

**Computing Resources:**
Participants will have access to the **IQM Quantum Computer** for validation and testing of their quantum circuits.

---

## **4. Suggested Approaches and Starting Points**

Teams are encouraged to explore and compare both paradigms creatively. Some possible directions include:

**Step 1 – Understand the Classical Baseline:**

* Review the provided XGBoost implementation in the reference notebook.
* Analyze the data preprocessing, feature selection, and model evaluation approach.
* **Split the dataset into training and test sets** (a 70/30 split is recommended). **All reported results must be evaluated on the test set, which must NOT be used for training the model.**
* Optionally, build your own classical model for comparison.

**Step 2 – Quantum and Hybrid Approaches:**

* Reformulate the problem using one or more quantum algorithms, such as:

  * **QSVC (Quantum Support Vector Classifier)**
  * **QNN (Quantum Neural Network)**
  * **PQC / VQC (Parameterized / Variational Quantum Circuits)**
* Design an appropriate feature encoding strategy for the quantum domain.
* Train your quantum circuits using a hybrid optimization loop.
* Validate the circuits on IQM hardware.

**Step 3 – Comparative Analysis:**

* Evaluate both classical and quantum models using metrics like accuracy, AUC-ROC, Gini coefficient, and F1-score **on the test set only**.
* Discuss trade-offs in terms of complexity, interpretability, training time, and computational cost.
* Analyze performance in the small-data regime (3,000 samples).

**Bonus Ideas:**

* Develop a novel *feature encoding* strategy optimized for small datasets.
* Visualize quantum embeddings or decision boundaries.
* Explore *hybrid quantum–classical* architectures that leverage the strengths of both approaches.
* Investigate quantum advantage in specific subsets or edge cases of the data.

---

## **5. Submission Requirements**

* **Git Repository** containing:

  * Source code and reproducible notebooks.
  * A clear README.md explaining data preprocessing, feature selection, and model design.
  * Quantum circuit details and parameterization.
  * A short comparative summary of classical vs. quantum results.
  * Analysis of model performance in the small-data regime.
* **Presentation (max 3 minutes)** highlighting your methodology, insights, and results.

---

## **6. Evaluation Criteria**

| Category                   | Description                                                        | Weight |
| -------------------------- | ------------------------------------------------------------------ | ------ |
| **Technical Quality**      | Soundness of the approach, reproducibility, and correctness        | 30%    |
| **Innovation**             | Creativity in reformulation, encoding, or circuit design           | 25%    |
| **Performance**            | Quality of results and insights compared to the classical baseline | 25%    |
| **Presentation & Clarity** | Clarity of explanation and overall communication                   | 20%    |

---

---

# **Nombre del Desafío**

**Quantum Credit – Explorando la Frontera Entre ML Clásico y Cuántico**

---

## **1. Motivación**

La evaluación del riesgo crediticio es una función central en las finanzas modernas, determinando quién tiene acceso al capital y bajo qué condiciones. Los modelos clásicos de machine learning, como **XGBoost**, ya proporcionan capacidades predictivas robustas, pero el auge de la **computación cuántica** promete remodelar cómo se procesan y optimizan los datos complejos de alta dimensionalidad.

Este desafío invita a los participantes a poner a prueba esa promesa: ¿pueden los métodos de machine learning cuántico igualar o superar a los algoritmos clásicos en la predicción del riesgo crediticio? Explorarás esta frontera implementando ambos enfoques y comparando sus resultados.

---

## **2. El Desafío: Predicción del Riesgo Crediticio**

### **2.1 Descripción del Problema**

Tu tarea es predecir el riesgo de impago crediticio de prestatarios individuales utilizando indicadores financieros y personales.
Deberás:

* Analizar un modelo **XGBoost** clásico proporcionado como implementación de referencia (eres libre de construir el tuyo propio si lo prefieres).
* Reformular y resolver el mismo problema utilizando enfoques cuánticos e híbridos cuántico-clásicos.
* Comparar los resultados en términos de precisión, interpretabilidad y eficiencia.

**Dataset:** Un conjunto de datos reducido de riesgo crediticio (`credit_risk_dataset_red.csv`) que contiene **3,000 muestras** con características financieras y personales. El notebook de Jupyter adjunto proporciona información detallada sobre cada variable y ejemplos de ingeniería de características.

**Nota:** Esta propuesta está especialmente enfocada en escenarios con muestras y características limitadas, haciéndola ideal para probar la ventaja cuántica en regímenes de datos pequeños.

---

## **3. Recursos**

Las siguientes herramientas y datos estarán disponibles para todos los equipos:

**SDKs Cuánticos:** Acceso al entorno **IQM Resonance** y SDKs compatibles como **PennyLane**, **Qiskit**, o **Cirq**.

**Dataset:**
El archivo CSV proporcionado (`credit_risk_dataset_red.csv`) contiene **3,000 muestras** con características personales y relacionadas con préstamos, incluyendo:

* Información personal (edad, ingresos, historial de empleo, estado de propiedad de vivienda).
* Características del préstamo (monto, tasa de interés, grado del préstamo, intención del préstamo).
* Ratios financieros e indicadores de solvencia crediticia.
* Etiqueta objetivo: clasificación binaria para riesgo de impago crediticio.

Las descripciones detalladas de las variables y el análisis exploratorio de datos están disponibles en el notebook de Jupyter adjunto (`Reduced-credit-risk-prediction.ipynb`).

**Recursos Computacionales:**
Los participantes tendrán acceso al **Computador Cuántico de IQM** para validación y pruebas de sus circuitos cuánticos.

---

## **4. Enfoques Sugeridos y Puntos de Partida**

Se alienta a los equipos a explorar y comparar ambos paradigmas de manera creativa. Algunas posibles direcciones incluyen:

**Paso 1 – Comprender la Línea Base Clásica:**

* Revisar la implementación de XGBoost proporcionada en el notebook de referencia.
* Analizar el preprocesamiento de datos, la selección de características y el enfoque de evaluación del modelo.
* **Dividir el dataset en conjuntos de entrenamiento y testeo** (se recomienda una división 70/30). **Todos los resultados reportados deben ser evaluados en el conjunto de testeo, el cual NO debe ser utilizado para entrenar el modelo.**
* Opcionalmente, construir tu propio modelo clásico para comparación.

**Paso 2 – Enfoques Cuánticos e Híbridos:**

* Reformular el problema utilizando uno o más algoritmos cuánticos, tales como:

  * **QSVC (Quantum Support Vector Classifier)**
  * **QNN (Quantum Neural Network)**
  * **PQC / VQC (Parameterized / Variational Quantum Circuits)**
* Diseñar una estrategia apropiada de codificación de características para el dominio cuántico.
* Entrenar tus circuitos cuánticos utilizando un bucle de optimización híbrido.

**Paso 3 – Análisis Comparativo:**

* Evaluar ambos modelos clásicos y cuánticos utilizando métricas como precisión, AUC-ROC, coeficiente de Gini y F1-score **únicamente en el conjunto de testeo**.
* Discutir compensaciones en términos de complejidad, interpretabilidad, tiempo de entrenamiento y costo computacional.
* Analizar el rendimiento en el régimen de datos pequeños (3,000 muestras).

**Ideas Bonus:**

* Desarrollar una estrategia de *codificación de características* novedosa optimizada para conjuntos de datos pequeños.
* Visualizar embeddings cuánticos o fronteras de decisión.
* Explorar arquitecturas *híbridas cuántico-clásicas* que aprovechen las fortalezas de ambos enfoques.
* Investigar la ventaja cuántica en subconjuntos específicos o casos límite de los datos.

---

## **5. Requisitos de Entrega**

* **Repositorio Git** que contenga:

  * Código fuente y notebooks reproducibles.
  * Un README.md claro explicando el preprocesamiento de datos, la selección de características y el diseño del modelo.
  * Detalles del circuito cuántico y parametrización.
  * Un breve resumen comparativo de los resultados clásicos vs. cuánticos.
  * Análisis del rendimiento del modelo en el régimen de datos pequeños.
* **Presentación (máx. 3 minutos)** destacando tu metodología, insights y resultados.

---

## **6. Criterios de Evaluación**

| Categoría                       | Descripción                                                                 | Peso |
| ------------------------------- | --------------------------------------------------------------------------- | ---- |
| **Calidad Técnica**             | Solidez del enfoque, reproducibilidad y corrección                          | 30%  |
| **Innovación**                  | Creatividad en la reformulación, codificación o diseño de circuitos         | 25%  |
| **Rendimiento**                 | Calidad de los resultados e insights comparados con la línea base clásica   | 25%  |
| **Presentación y Claridad**     | Claridad de la explicación y comunicación general                           | 20%  |

---
