"""Export the Breast Cancer Wisconsin (Diagnostic) data to CSV and ARFF.

The data comes with scikit-learn, so nothing is downloaded from the internet.
The ARFF file is for Weka. Note: the "breast-cancer.arff" file that ships with
Weka is a different dataset (Ljubljana) and must not be used for this project.

Run from the repository root:  python data/make_data.py
"""
from pathlib import Path

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split

OUT = Path(__file__).resolve().parent

bunch = load_breast_cancer(as_frame=True)
df = bunch.frame.copy()

# In scikit-learn 0 = malignant and 1 = benign. We store readable labels
# instead, so that the CSV and Weka show "malignant" / "benign".
df["diagnosis"] = df["target"].map({0: "malignant", 1: "benign"})
df = df.drop(columns="target")

# Column names without spaces are easier to use in Weka and pandas.
df.columns = [c.replace(" ", "_") for c in df.columns]

df.to_csv(OUT / "wdbc.csv", index=False)

features = [c for c in df.columns if c != "diagnosis"]


def write_arff(frame, path, relation):
    with open(path, "w", encoding="utf-8") as f:
        f.write("% Breast Cancer Wisconsin (Diagnostic), exported from scikit-learn\n")
        f.write("% Source: https://archive.ics.uci.edu/dataset/17/breast+cancer+wisconsin+diagnostic\n")
        f.write(f"@relation {relation}\n\n")
        for c in features:
            f.write(f"@attribute {c} numeric\n")
        # malignant is listed first so that Weka treats it as the first class.
        f.write("@attribute diagnosis {malignant,benign}\n\n@data\n")
        for row in frame.itertuples(index=False):
            f.write(",".join(repr(float(v)) for v in row[:-1]) + f",{row[-1]}\n")


write_arff(df, OUT / "wdbc.arff", "wdbc")

print(f"Saved {len(df)} rows x {len(features)} features to {OUT}")
print(df["diagnosis"].value_counts().to_string())

# Same split as the notebook (Section 5), so that Weka and Python are tested
# on exactly the same samples.
y = (df["diagnosis"] == "malignant").astype(int)
train, test = train_test_split(df, test_size=0.25, stratify=y, random_state=42)
for name, part in [("wdbc_train", train), ("wdbc_test", test)]:
    write_arff(part, OUT / f"{name}.arff", name)
print(f"Saved Weka split: {len(train)} training and {len(test)} test samples")
