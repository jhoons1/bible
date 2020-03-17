import pandas as pd

x = pd.read_pickle('./FinalBibleNIV.pkl')

x['index'] = x['index'].astype(int);
x['chapter'] = x['chapter'].astype(int);
x['verse'] = x['verse'].astype(int);

y = x.sort_values(['index','chapter','verse'],ascending=[True, True, True])

y['index'] = y['index'].astype(str);
y['chapter'] = y['chapter'].astype(str);
y['verse'] = y['verse'].astype(str);

y.to_pickle('./FinalBibleNIVSorted.pkl')
