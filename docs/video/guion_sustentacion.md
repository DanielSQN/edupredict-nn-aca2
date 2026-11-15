# Guion del video de sustentación (3 a 5 minutos)

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
> Las cifras salen de `models/metricas_nn.json` y `models/metricas_nn_temprano.json`, medidas sobre
> el conjunto de prueba: 885 estudiantes que las redes nunca vieron. Si se vuelve a entrenar, hay
> que actualizarlas aquí y regenerar el póster.
> El reparto de abajo es una propuesta: intercámbienlo como les sirva.

| Tiempo | Bloque | Quién | Qué decir / mostrar |
|---|---|---|---|
| 0:00–0:30 | **El problema** | Paula Calvo | En los datos de este proyecto, casi uno de cada tres estudiantes abandonó la carrera: 1.421 de 4.424. Cuando la institución se da cuenta, casi siempre ya es tarde para ayudarlo. La pregunta del proyecto: ¿se puede anticipar ese riesgo con los datos que la universidad ya tiene, y ponerlo en una herramienta que un coordinador pueda usar? Datos reales: 4.424 estudiantes, 36 datos de cada uno. |
| 0:30–1:10 | **Los datos** | Juan Caviedes | De dónde salen (repositorio público UCI, una universidad portuguesa) y qué sabemos de cada estudiante: notas del semestre, materias aprobadas, beca, deuda de matrícula, edad al ingresar. Están guardados en una base de datos y la aplicación los consulta de ahí. Tres resultados posibles: desertó (32 %), sigue matriculado (18 %) o se graduó (50 %). |
| 1:10–2:05 | **Las redes neuronales, en palabras sencillas** | Jonathan Flórez | Mostrar el **diagrama del póster** (Figura 1). Idea central: en vez de darle reglas al computador, le mostramos miles de historias académicas y él aprende solo qué combinaciones anticipan el abandono. Probamos **dos redes** en **dos momentos**: con la historia académica completa y con solo el primer semestre, que es la alerta temprana. **No ganó la misma en los dos**: con la información completa quedó la red más sencilla, de capas en cadena (MLP); en la alerta temprana quedó la que relaciona todos los datos entre sí (FT-Transformer). Las comparamos cinco veces con particiones distintas para no elegir por suerte. Mostrar las **curvas de aprendizaje** (Figura 2): la red mejora hasta la vuelta 11; después empieza a memorizar en lugar de aprender, y nos quedamos con la de ese punto. |
| 2:05–2:55 | **Qué tan bien funciona** | Daniel Quintero | Tablas del póster. **Con la información completa** (red MLP): acierta la situación de **73 de cada 100** estudiantes que nunca había visto (exactitud 0,733; F1 macro 0,693). De los que de verdad desertaron, **detecta a 7 de cada 10**, y cuando señala a alguien como posible desertor acierta en 84 de cada 100. Dos mensajes honestos: (1) **el punto débil es el estudiante que *sigue matriculado***: es el grupo más pequeño y el que más se confunde con los otros dos (F1 de 0,49, frente a 0,76 en deserción y 0,83 en graduado); (2) **frente a los modelos clásicos del ACA 1 el desempeño es comparable, no superior**: el mejor clásico obtiene 0,730 y la red 0,715 — con 4.400 filas de tabla las redes no dan un salto, y decirlo es parte del rigor. Y la **alerta temprana** (red FT-Transformer): con solo el primer semestre acierta **72 de cada 100** (F1 macro 0,682) y detecta a casi dos de cada tres desertores. Se pierde muy poco por avisar un semestre antes. |
| 2:55–4:10 | **Demostración en vivo** | Paula Calvo o Juan Caviedes | Abrir la app desplegada: <https://edupredict-nn-aca2.streamlit.app/>. **Dashboard** (panorama del grupo) → **Predicción individual**: llenar el formulario de un estudiante con *Información académica completa* y mostrar las probabilidades de cada situación (aquí responde la red MLP); cambiar a *Alerta temprana* para ver que funciona con menos datos (aquí responde la otra red, el FT-Transformer) → **Comparación de modelos** (tabla, matriz de confusión y curvas, con una pestaña por escenario). Cerrar mostrando el **póster en PDF** completo, con sus QR de app, repositorio y video. |
| 4:10–4:40 | **Para qué sirve y para qué no** | Jonathan Flórez | Impacto: permite que un coordinador llame al estudiante en riesgo **antes** de que abandone. Lo que más pesa en la predicción son las materias aprobadas y tener la matrícula al día (Figura 3). Límites, dichos sin tecnicismos: la herramienta señala coincidencias, no causas; los datos son de una universidad portuguesa y pueden no trasladarse al caso colombiano; variables como el sexo o la nacionalidad podrían introducir sesgos. Es **apoyo a la decisión humana, nunca una decisión automática** sobre un estudiante. |
| 4:40–5:00 | **Cierre** | Todos | Nombres completos de los cuatro integrantes, la asignatura y el docente. |

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
- [ ] Notebook **con las salidas de la ejecución** subido al repositorio.
- [ ] Abrir la app unos minutos antes de grabar: si lleva días sin visitas, Streamlit la suspende y
      tarda cerca de un minuto en volver.
- [ ] Ensayar en la app el caso que se va a mostrar, en los dos escenarios.
- [ ] Póster en PDF abierto y a mano para mostrarlo.
- [ ] Ensayo **cronometrado**: si pasa de 5:00, se recorta el bloque de la demostración, no el de resultados.
- [ ] Grabado con **voz real** de los integrantes.
- [ ] Video **público**: probar el enlace en una ventana de incógnito, como pidió el docente.
- [ ] Después de publicar: completar `ENLACE_VIDEO`, ejecutar `python scripts/build_qr.py` y
      `python scripts/build_poster.py`, y exportar de nuevo el PDF para que lleve el tercer QR.
