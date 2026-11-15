# Referencias del proyecto

Enunciados oficiales de la asignatura Aprendizaje Automático (CUN, Especialización en
Inteligencia Artificial · Dr. Hamilton Rivera Flor):

- `ACA_2_Aprendizaje_Automatico_CUN.pdf` — **enunciado y rúbrica del ACA N.º 2**, el que
  desarrolla este repositorio: *Modelado con Redes Neuronales Artificiales (CNN, RNN,
  Transformers) y Despliegue Interactivo en Streamlit*.
- `ACA_1_Aprendizaje_Automatico_CUN.pdf` — enunciado del ACA N.º 1 (modelos clásicos), que
  se conserva como referencia porque el ACA 2 reutiliza su dataset, su limpieza y su
  partición 80/20 para comparar las redes contra los modelos de árboles.

Pilar elegido en ambos: **Proyecto 2 — Educación**.

## Por qué un MLP y un FT-Transformer, y no una CNN o una RNN

El título del enunciado nombra «CNN, RNN, Transformers», pero el catálogo de la Sección 2
autoriza explícitamente el perceptrón multicapa para este pilar:

> «Redes Neuronales Recurrentes (LSTM/GRU) o **Perceptrones Multicapa (MLP) profundos**
> para predicción temporal de deserción académica.»
> — ACA N.º 2, Sección 2, Proyecto 2: Educación

El dataset es una tabla: no hay imágenes, señales ni texto libre. Las CNN, las RNN y los
modelos de Hugging Face (BERT, ViT…) están diseñados para esas modalidades. Para datos
tabulares las arquitecturas idóneas son el MLP con *embeddings* y el **FT-Transformer**
(Gorishniy et al., 2021), que es la adaptación tabular de la arquitectura Transformer: cada
variable se trata como un *token* y se procesa con auto-atención. Las dos están
implementadas y se comparan por validación cruzada.

## Correspondencia con el enunciado del ACA 2

| Requisito del ACA 2 | Dónde se cumple |
|---|---|
| Paso 1 · Exploración y gestión SQL | Notebook, Parte 1 · `src/db.py` · `data/estudiantes.db` (SQLite) |
| Paso 2 · Preparación y pipeline | Notebook, Parte 2 · `src/nn/data.py` (`TabularEncoder`) |
| Paso 3 · Modelado neuronal | Notebook, Partes 3–5 · `src/nn/models.py` · `src/nn/training.py` |
| Paso 4 · Evaluación y métricas | Notebook, Partes 6–7 · `src/evaluate.py` · `models/metricas_nn*.json` |
| Paso 5 · Despliegue Streamlit | `app.py` · `src/predict.py` · `requirements.txt` |
| Entregable 1 · Notebook reproducible y modular | `notebooks/ACA2_Student_Dropout_NN.ipynb` |
| Entregable 2 · Póster infografía (APA 7) | `scripts/build_poster.py` → `docs/poster/` |
| Entregable 3 · App Streamlit + dependencias | `app.py`, `src/`, `requirements.txt` |
| Entregable 4 · Video de 3 a 5 min | guion en `docs/video/guion_sustentacion.md` |

Los enlaces públicos de la app y del video se centralizan en
`src/project_info.py` (`ENLACE_APP`, `ENLACE_VIDEO`, `ENLACE_REPO`); de allí los leen la app
y el póster.

## Referencia del ACA 1 (entrega anterior, ya calificable)

Repositorio: https://github.com/DanielSQN/edupredict-ml-streamlit ·
video de sustentación del **ACA 1**: https://www.youtube.com/watch?v=BEmN8dqMv-o

## Nota sobre la cita del dataset

El enunciado cita el dataset como *Martins, M. V., Real, M. B., Machado, J., & Becker, A. (2021)*. La cita
oficial que publica el UCI Machine Learning Repository es:

Realinho, V., Vieira Martins, M., Machado, J., & Baptista, L. (2021). *Predict Students' Dropout and Academic
Success* [Dataset]. UCI Machine Learning Repository. https://doi.org/10.24432/C5MC89

El proyecto usa la cita oficial de UCI. Si el docente exige la forma del enunciado, conviene confirmarlo con él.
