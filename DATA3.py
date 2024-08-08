import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


header = ['preg', 'b', 'c', 'd', 'e', 'for', 'g', 'h', 'i']
data = pd.read_csv('./data/pima-indians-diabetes.data.csv', names=header)



corr=data.corr(method='pearson')


fig = plt.figure()
ax=fig.add_subplot(111)
cax=ax.matshow(corr, cmap='coolwarm', vmin=-1, vmax=1)
fig.colorbar(cax)
ticks=np.arange(0, 9, 1)
ax.set_xticks(ticks)
ax.set_yticks(ticks)
ax.set_xticklabels(header)
ax.set_yticklabels(header)

plt.show()
plt.savefig('./result/Data1result.png')