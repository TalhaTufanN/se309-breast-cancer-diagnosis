#!/bin/bash
# Reproduces the Weka results in this folder. Run from the repository root:
#   WEKA_JAR=/path/to/weka.jar bash weka/run_weka.sh
# First create the data files with:  python data/make_data.py
#
# Each classifier gets 10-fold cross-validation on the training set, and is then
# trained on the training set and evaluated on the shared test set.
W="${WEKA_JAR:-$HOME/weka-3-8-7/weka.jar}"
TR=data/wdbc_train.arff
TE=data/wdbc_test.arff

run() {
  name=$1; shift
  java -cp "$W" "$@" -t "$TR" -x 10 -s 42 > "weka/${name}_cv.txt"
  java -cp "$W" "$@" -t "$TR" -T "$TE" -d "weka/${name}.model" > "weka/${name}_test.txt"
}

run zeror weka.classifiers.rules.ZeroR
run logistic_default weka.classifiers.functions.Logistic
run logistic_ridge05 weka.classifiers.functions.Logistic -R 0.5
run random_forest weka.classifiers.trees.RandomForest -I 300 -S 42
