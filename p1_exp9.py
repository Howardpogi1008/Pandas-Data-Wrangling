import pandas as pd


a = {'Student': ['Ice Bear','Panda','Grizzly'],
     'Math':[80,95,79]}
A = pd.DataFrame(a, columns = ['Student','Math'])


b = {'Student': ['Ice Bear','Panda','Grizzly'],
     'Electronics':[85,81,83]}
B = pd.DataFrame(b, columns = ['Student','Electronics'])


c = {'Student': ['Ice Bear','Panda','Grizzly'],
     'GEAS':[90,79,94]}
C = pd.DataFrame(c, columns = ['Student','GEAS'])


d = {'Student': ['Ice Bear','Panda','Grizzly'],
     'ESAT':[93,89,88]}
D = pd.DataFrame(d, columns = ['Student','ESAT'])


x = pd.merge(A,B, how='left', on = 'Student')
y = pd.merge(x,C, how='left', on = 'Student')
z = pd.merge(y,D, how='left', on = 'Student')

prob1 = pd.melt(z, id_vars = ['Student'], var_name = 'Subject', value_name = 'Grades')

print(prob1)