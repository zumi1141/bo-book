####################
# Study of Optimizaiton of Hyper Param. 
# @author W.Sumihira
#
####################

import optuna

from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score
from sklearn.svm import SVC

def objective(trial):
  iris = load_iris()
  x, y = iris.data, iris.target
  

## push test ##