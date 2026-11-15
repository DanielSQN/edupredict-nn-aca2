# Guion del video de sustentación (3 minutos)

> **Enunciado (entregable 4):** exposición sintética del equipo con *problema, arquitectura de red
> seleccionada, métricas obtenidas y demostración en vivo de la app en Streamlit y del póster*.
> Cumplir el tiempo (3–5 min) vale el 15 % de la rúbrica.
>
> **Recomendaciones del docente para este video:**
> - **Enfoque divulgativo.** Se le explica el proyecto a un público general, destacando el impacto
>   y la importancia de la solución. **Nada de detalles técnicos profundos de código.**
> - **Voz real** de uno o varios integrantes. No se admite locución sintética.
> - **Cronometrar**: estrictamente entre 3:00 y 5:00.
> - **Público**: cualquiera debe poder abrirlo y reproducirlo sin pedir permisos.
> - Mostrar **tanto el póster como la interfaz gráfica en funcionamiento**.
>
> **Duración prevista: 3:10 a 3:25.** El texto tiene 440 palabras (unos 3:00 de voz a ritmo
> normal) más los cambios de pantalla de la demostración y del póster. El límite inferior es
> estricto: **si un ensayo baja de 3:05, no se recorta nada; se habla más despacio.**
>
> Las cifras salen de `models/metricas_nn.json` y `models/metricas_nn_temprano.json`, medidas sobre
> el conjunto de prueba: 885 estudiantes que las redes nunca vieron. Si se vuelve a entrenar, hay
> que actualizarlas aquí, en la presentación y en el póster.
> El reparto es una propuesta: intercámbienlo como les sirva.

El guion sigue la [presentación de nueve diapositivas](presentacion_EduPredictAI_ACA2.pdf) (el texto de cada una está también en sus
notas del orador). Los bloques 7 y 9 se graban **fuera de la presentación**: en el navegador con
la app y con el póster en PDF.

| # | Tiempo | Diapositiva | Quién | Texto para decir | Qué se muestra |
|---|---|---|---|---|---|
| 1 | 0:00–0:12 | Portada | Paula Calvo | Hola. Somos el equipo de EduPredict AI, de la Especialización en Inteligencia Artificial de la CUN. En tres minutos les contamos cómo una red neuronal puede ayudar a anticipar la deserción universitaria. | Título, integrantes y logo de la CUN. |
| 2 | 0:12–0:34 | El problema | Paula Calvo | En los datos que usamos, casi uno de cada tres estudiantes abandonó la carrera: mil cuatrocientos veintiuno de cuatro mil cuatrocientos veinticuatro. Cuando la universidad se da cuenta, casi siempre ya es tarde. Nuestra pregunta: ¿se puede anticipar ese riesgo con los datos que la institución ya tiene? | «1 de cada 3» y el dashboard de la app. |
| 3 | 0:34–0:54 | Los datos y el método | Juan Caviedes | Trabajamos con datos públicos de una universidad portuguesa: treinta y seis datos de cada estudiante, como materias aprobadas, notas, beca o matrícula al día. Los guardamos en una base de datos, los preparamos y entrenamos las redes. Hay tres resultados posibles: desertó, sigue matriculado o se graduó. | Las tres cifras del conjunto de datos y los cinco pasos del método. |
| 4 | 0:54–1:20 | Dos redes, dos momentos | Jonathan Flórez | En lugar de darle reglas al computador, le mostramos miles de historias académicas y la red aprende sola qué combinaciones anticipan el abandono. Probamos dos redes en dos momentos. Con la historia completa ganó la más sencilla, una red de capas en cadena llamada MLP. Con solo el primer semestre ganó el FT-Transformer, que relaciona todos los datos entre sí. | Diagrama de la arquitectura y las dos redes ganadoras. |
| 5 | 1:20–1:34 | El entrenamiento | Jonathan Flórez | Estas curvas muestran el aprendizaje. La red mejora hasta la vuelta once; después empieza a memorizar en lugar de aprender. Por eso nos quedamos con el modelo de ese punto. | Curvas de pérdida y F1 macro tomadas de la app. |
| 6 | 1:34–2:04 | Qué tan bien funciona | Daniel Quintero | ¿Qué tan bien funciona? Con estudiantes que nunca había visto, la red acierta la situación de setenta y tres de cada cien, y detecta a siete de cada diez de los que desertaron. Con solo el primer semestre acierta setenta y dos de cada cien: casi lo mismo, un semestre antes. Con honestidad: le cuesta distinguir al que sigue matriculado, y frente a los modelos clásicos el resultado es comparable, no superior. | Las tres cifras y la matriz de confusión. |
| 7 | 2:04–2:40 | La aplicación, en vivo | Daniel Quintero | Veámosla en vivo. Este es el panorama de los cuatro mil cuatrocientos estudiantes. En Predicción individual llenamos los datos de un estudiante que casi no aprobó materias y pulsamos Analizar: la red estima deserción con ochenta y siete por ciento de probabilidad. Y en Comparación de modelos están las tablas, la matriz de confusión y las curvas que acabamos de mostrar. | **Cambiar al navegador**, con la app ya abierta: Dashboard → Predicción individual → Comparación de modelos. |
| 8 | 2:40–3:02 | Para qué sirve y para qué no | Juan Caviedes | ¿Para qué sirve? Para que un coordinador llame al estudiante en riesgo antes de que abandone. Lo que más pesa son las materias aprobadas y tener la matrícula al día. Pero la herramienta señala coincidencias, no causas; los datos son de Portugal, y es un apoyo a la decisión humana, nunca una decisión automática. | Usos, límites y la gráfica de variables que más pesan. |
| 9 | 3:02–3:18 | Póster, aplicación y código | Todos | Este es nuestro póster, con los códigos para abrir la aplicación y el repositorio. Somos Paula Calvo, Juan Caviedes, Jonathan Flórez y Daniel Quintero, de la asignatura Aprendizaje Automático, con el docente Hamilton Rivera Flor. Gracias. | **Abrir el póster en PDF** a pantalla completa y volver a la diapositiva de cierre. |

## El caso de la demostración

Para que la app muestre una alerta clara, dejar el formulario de **Predicción individual** con
*Información académica completa* y cambiar solo estos campos antes de pulsar **Analizar estudiante**:

| Pestaña | Campo | Valor |
|---|---|---|
| 1.er semestre | Unidades aprobadas | 1 |
| 1.er semestre | Promedio de notas | 9,5 |
| 2.º semestre | Unidades aprobadas | 0 |
| 2.º semestre | Promedio de notas | 0 |
| 2.º semestre | Evaluaciones presentadas | 2 |

Resultado comprobado en la app desplegada: **Deserción, 87,3 %** (Matriculado 12,4 %, Graduado
0,2 %). Conviene dejar el caso ya lleno antes de grabar y solo pulsar el botón en cámara.

En la demostración no se cambia a *Alerta temprana*: con este mismo caso ese modelo queda casi
empatado entre Matriculado (50,0 %) y Deserción (48,4 %), y explicarlo no cabe en tres minutos.
La alerta temprana se cuenta con su cifra en el bloque 6.

## Cifras de respaldo

Para tenerlas a mano al grabar. En voz se dicen redondeadas («73 de cada 100»); el valor exacto está
en el póster.

| | Información completa | Alerta temprana |
|---|---|---|
| Red desplegada | MLP con embeddings (17.323 parámetros) | FT-Transformer (22.083 parámetros) |
| Cómo se eligió (F1 macro en validación cruzada) | MLP 0,715 frente a FT-Transformer 0,702 | FT-Transformer 0,691 frente a MLP 0,677 |
| Exactitud en prueba | 0,733 (649 de 885) | 0,720 (637 de 885) |
| F1 macro en prueba | 0,693 | 0,682 |
| Exactitud balanceada | 0,701 | 0,690 |
| ROC-AUC | 0,878 | 0,868 |
| Desertores detectados (recall) | 196 de 284 (69 %) | 184 de 284 (65 %) |
| Aciertos al señalar deserción (precisión) | 84 % | 86 % |
| F1 por clase: deserción / matriculado / graduado | 0,758 / 0,494 / 0,826 | 0,739 / 0,490 / 0,816 |
| Mejor clásico del ACA 1 (F1 macro en validación) | Gradient Boosting 0,730, frente a 0,715 de la red | Gradient Boosting 0,699, frente a 0,691 de la red |
| Época elegida | 11 de 26 | 37 de 52 |

**Si preguntan por qué en el escenario completo no se desplegó el FT-Transformer**, que en prueba
obtuvo un F1 macro algo mayor (0,711 frente a 0,693): la red se eligió por validación cruzada,
antes de mirar el conjunto de prueba. Elegir con la prueba sería escoger la respuesta después de
ver el examen, y la cifra reportada dejaría de ser honesta.

## Cómo decir la parte técnica sin perder al público

| En vez de… | Decir… |
|---|---|
| «MLP con capas ocultas de 128 y 64 neuronas» | «una red de capas en cadena: cada capa resume lo que entendió la anterior» |
| «FT-Transformer con token [CLS] y auto-atención» | «una red que mira todos los datos del estudiante a la vez y aprende sola cuáles se relacionan entre sí» |
| «*embeddings* para las variables nominales» | «el modelo aprende a representar cada programa académico según cómo se comportan sus estudiantes» |
| «*early stopping* sobre el macro-F1 de validación» | «paramos el entrenamiento en el punto en que deja de aprender y empieza a memorizar» |
| «pérdida de entropía cruzada ponderada por clase» | «le damos más peso a los casos poco frecuentes para que no los ignore» |
| «validación cruzada estratificada de 5 pliegues» | «comparamos las dos redes cinco veces con particiones distintas, para no quedarnos con un resultado de suerte» |
| «F1 macro de 0,693» | «una nota de 0 a 1 que promedia qué tan bien le va en cada una de las tres situaciones, sin dejar que la más frecuente tape a las demás» |
| «recall de 0,69 en la clase Deserción» | «de cada diez estudiantes que desertaron, la red identificó a siete» |

El detalle técnico completo (AdamW, dropout, hiperparámetros, importancia por permutación) va en el
**notebook y en el póster**, que es donde la rúbrica lo evalúa. En el video resta puntos.

## Checklist antes de grabar

- [x] Modelos entrenados en `models/` (los dos `.pt` con sus metadatos y métricas).
- [x] App **desplegada y probada** fuera de `localhost`: <https://edupredict-nn-aca2.streamlit.app/>.
- [x] `ENLACE_APP` y `ENLACE_REPO` completados en `src/project_info.py`, con sus QR en el póster.
- [x] Presentación de nueve diapositivas con gráficas y pantallas de la app.
- [ ] Notebook **con las salidas de la ejecución** subido al repositorio.
- [ ] Abrir la app unos minutos antes de grabar: si lleva días sin visitas, Streamlit la suspende y
      tarda cerca de un minuto en volver.
- [ ] Dejar lleno el caso de la demostración y el póster en PDF abierto en otra ventana.
- [ ] Ensayo **cronometrado**: entre 3:05 y 3:30. Si pasa de 3:30, se acorta la demostración, no
      los resultados; si baja de 3:05, se habla más despacio.
- [ ] Grabado con **voz real** de los integrantes.
- [ ] Video **público**: probar el enlace en una ventana de incógnito, como pidió el docente.
- [ ] Después de publicar: completar `ENLACE_VIDEO`, ejecutar `python scripts/build_qr.py` y
      `python scripts/build_poster.py`, y exportar de nuevo el PDF para que lleve el tercer QR.
