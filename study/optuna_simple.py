####################
# study of simple optimization using optuna
# @author W.Sumihira
#
####################

import optuna

def objective(trial):
  x = trial.suggest_float("x", -5, 5)
  y = trial.suggest_float("y", -5, 5)
  return  2 * x ** 2 - 1.05 * x ** 4 + x ** 6 / 6 + x * y + y ** 2

if __name__ == "__main__":
  study = optuna.create_study()
  study.optimize(objective, n_trials=5000)
  print(f"Best Value: {study.best_value}" f"params: {study.best_params}")

################
#メモ：トライ数を5000にしても、最適解は701試行目あたり、
#最適化手法は確認するけど、ある程度凸部に落ちるようにはできているのかも。
################