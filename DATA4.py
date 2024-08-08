import matplotlib.pyplot as plt
import pandas as pd
import scipy as sp

header = ['preg', 'plas', 'pres', 'd', 'e', 'for', 'g', 'h', 'i']
data = pd.read_csv('./data/pima-indians-diabetes.data.csv', names=header)

plt.clf()
pd.plotting.scatter_matrix(data)
plt.savefig('./DATA4result.png')







#
# data.plot(kind='density', figsize=(12, 10), subplots=True, layout=(3, 3), sharex=False, sharey=False)
# data.plot(kind='box', subplots=True, figsize=(12, 10), layout=(3, 3), sharex=False, sharey=False)
# # data.hist(figsize=(12, 10), bins=5)
# plt.tight_layout()