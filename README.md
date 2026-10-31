# Breast Cancer Diagnosis (Wisconsin)

**Course:** SE309 AI and Data Science for Innovation in Health Science · Fall 2026–27
**Topic code:** SE309-03   ·   **Working as:** Individual

> **Educational project only.** The models in this repository are not a diagnostic tool and must not be used to make decisions about real patients.

## Members

| Name | Student no. | GitHub username |
|---|---|---|
| Talha Tufan | 220201035 | @TalhaTufanN |

## What the project does

The project classifies breast tumours as benign or malignant from 30 cell-nucleus measurements taken from fine needle aspirate (FNA) images, using the public Breast Cancer Wisconsin (Diagnostic) data. It explores the strongly correlated features, compares at least two models with a majority-class baseline in Weka and Python, and reports confusion matrices with sensitivity and specificity. Special attention is given to false negatives — malignant tumours predicted as benign — because they are the most costly error. As an extension it tests feature selection and compares the models with a single-feature baseline.

## How to install and run

### Weka
1. Open Weka → Explorer → **Open file…** → `data/wdbc.arff`.
   (Do **not** use the `breast-cancer.arff` file that ships with Weka — it is a different dataset.)
2. Load the saved model: Classify tab → right-click the result list → **Load model** → `weka/<model>.model`.
3. Settings used: <!-- classifier, filters, test option — added when the Weka part is done -->

### Python / Colab
1. Open `notebooks/project.ipynb` in Google Colab (**File → Open notebook → GitHub**, paste this repository's URL).
2. **Runtime → Run all.** The notebook loads the data from scikit-learn itself; no other step is needed.

To run locally instead: `pip install -r requirements.txt`, then open the notebook in Jupyter.
To recreate the CSV and ARFF files: `python data/make_data.py`.

## Example output

<!-- Added when the first results are ready: ![Main result](images/result.png) -->

## Data

| Dataset | Source (link) | Size | Licence / terms of use |
|---|---|---|---|
| Breast Cancer Wisconsin (Diagnostic) | [UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/17/breast+cancer+wisconsin+diagnostic), also in scikit-learn | 569 × 30 features + label (357 benign, 212 malignant) | CC BY 4.0 |

> Only public or properly released data is used. No real patient records, and no identifiable health data uploaded to online tools.

A short **data note** (who, why, when/where, label, missingness, impossible values, timing, consent) is in the report and in Section 2 of the notebook.

## Folder structure

```
├── README.md
├── requirements.txt
├── data/
│   ├── make_data.py      # exports the scikit-learn data to CSV and ARFF
│   ├── wdbc.csv          # the data as CSV
│   └── wdbc.arff         # the data for Weka
├── weka/                 # saved models (.model) and result buffers (.txt)
├── notebooks/
│   └── project.ipynb     # main notebook (from the course template)
├── images/               # figures used in the README and reports
├── reports/
│   ├── interim_report.pdf
│   └── final_report.pdf
└── video.md              # link to the presentation video
```

## Who did what

| Member | Main responsibilities | Main files / parts |
|---|---|---|
| @TalhaTufanN | All parts (individual project) | All files |

## External code, libraries and AI tools

| What | Used for | Where |
|---|---|---|
| scikit-learn | loading the data, models, evaluation | `data/make_data.py`, notebook |
| pandas, NumPy, Matplotlib | data handling and plots | notebook |
| Weka | models and evaluation without code | `weka/` |
| Claude (AI assistant) | help with setting up the repository, drafting code and text, explaining methods | <!-- list the files / sections --> |

## Reports and video

- Interim report (Week 10): [`reports/interim_report.pdf`](reports/interim_report.pdf)
- Final report: [`reports/final_report.pdf`](reports/final_report.pdf)
- Presentation video: <link — added at the final>
