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
> Las cifras entre `[ ]` se toman del notebook ejecutado / `models/metricas_nn.json`.
> El reparto de abajo es una propuesta: intercámbienlo como les sirva.

| Tiempo | Bloque | Quién | Qué decir / mostrar |
|---|---|---|---|
| 0:00–0:30 | **El problema** | Paula Calvo | Uno de cada tres estudiantes que entra a la universidad no termina. Cuando la institución se da cuenta, casi siempre ya es tarde para ayudarlo. La pregunta del proyecto: ¿se puede anticipar ese riesgo con los datos que la universidad ya tiene, y ponerlo en una herramienta que un coordinador pueda usar? Datos reales: 4.424 estudiantes, 36 datos de cada uno. |
| 0:30–1:10 | **Los datos** | Juan Caviedes | De dónde salen (repositorio público UCI, una universidad portuguesa) y qué sabemos de cada estudiante: notas del semestre, materias aprobadas, beca, deuda de matrícula, edad al ingresar. Están guardados en una base de datos y la aplicación los consulta de ahí. Tres resultados posibles: desertó, sigue matriculado o se graduó. |
| 1:10–2:05 | **La red neuronal, en palabras sencillas** | Jonathan Flórez | Mostrar el **diagrama del póster**. Idea central: en vez de darle reglas al computador, le mostramos miles de historias académicas y él aprende solo qué combinaciones anticipan el abandono. Probamos **dos redes** y nos quedamos con la que acertó más. Mostrar las **curvas de aprendizaje**: la red va mejorando hasta que empieza a memorizar en lugar de aprender, y ahí la detenemos. |
| 2:05–2:55 | **Qué tan bien funciona** | Daniel Quintero | Tabla del póster: red elegida `[nombre]`, acierto global `[x.xxx]`, F1 macro `[x.xxx]`. Dos mensajes honestos: (1) **acierta de forma pareja en las tres situaciones, no solo en la mayoritaria**; (2) **frente a los modelos clásicos del ACA 1 el desempeño es comparable, no superior** — con 4.400 filas de tabla las redes no dan un salto, y decirlo es parte del rigor. Caso más difícil: distinguir al que *sigue matriculado*. Y el escenario de **alerta temprana**: con solo el primer semestre ya se puede avisar, `[x.xxx]`. |
| 2:55–4:10 | **Demostración en vivo** | Paula Calvo o Juan Caviedes | Abrir la app desplegada. **Dashboard** (panorama del grupo) → **Predicción individual**: llenar el formulario de un estudiante y mostrar las probabilidades de cada situación; cambiar a *Alerta temprana* para ver que funciona con menos datos → **Comparación de modelos** (tabla, matriz de confusión y curvas). Cerrar mostrando el **póster en PDF** completo, con sus QR de app, repositorio y video. |
| 4:10–4:40 | **Para qué sirve y para qué no** | Jonathan Flórez | Impacto: permite que un coordinador llame al estudiante en riesgo **antes** de que abandone. Límites, dichos sin tecnicismos: la herramienta señala coincidencias, no causas; los datos son de una universidad portuguesa y pueden no trasladarse al caso colombiano; variables como el sexo o la nacionalidad podrían introducir sesgos. Es **apoyo a la decisión humana, nunca una decisión automática** sobre un estudiante. |
| 4:40–5:00 | **Cierre** | Todos | Nombres completos de los cuatro integrantes, la asignatura y el docente. |

## Cómo decir la parte técnica sin perder al público

| En vez de… | Decir… |
|---|---|
| «FT-Transformer con token [CLS] y auto-atención» | «una red que mira todos los datos del estudiante a la vez y aprende solos cuáles se relacionan entre sí» |
| «*embeddings* para las variables nominales» | «el modelo aprende a representar cada programa académico según cómo se comportan sus estudiantes» |
| «*early stopping* sobre el macro-F1 de validación» | «paramos el entrenamiento en el punto en que deja de aprender y empieza a memorizar» |
| «pérdida de entropía cruzada ponderada por clase» | «le damos más peso a los casos poco frecuentes para que no los ignore» |
| «validación cruzada estratificada de 5 pliegues» | «comparamos las dos redes cinco veces con particiones distintas, para no quedarnos con un resultado de suerte» |

El detalle técnico completo (AdamW, dropout, hiperparámetros, importancia por permutación) va en el
**notebook y en el póster**, que es donde la rúbrica lo evalúa. En el video resta puntos.

## Checklist antes de grabar

- [ ] Notebook ejecutado y `models/*.pt` en su sitio: sin eso la app no abre.
- [ ] App **desplegada y probada** en otro navegador, no solo en `localhost`.
- [ ] `ENLACE_APP` y `ENLACE_VIDEO` completados en `src/project_info.py`, y el póster regenerado
      con los QR ya apuntando a las URL reales.
- [ ] Póster en PDF abierto y a mano para mostrarlo.
- [ ] Ensayo **cronometrado**: si pasa de 5:00, se recorta el bloque de la demostración, no el de resultados.
- [ ] Grabado con **voz real** de los integrantes.
- [ ] Video **público**: probar el enlace en una ventana de incógnito, como pidió el docente.
