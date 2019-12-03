import pandas as pd

data = {'Box': ['Box1','Box1','Box1','Box2','Box2','Box2'], 'Dimension': ['Length','Width','Height','Length','Width','Height'], 'Value': [6,4,2,5,3,4]}

x = pd.DataFrame (data, columns=['Box','Dimension','Value'])

tidy = x.pivot_table (index = ['Box'], columns = 'Dimension', values = 'Value')

tidy['Volume'] = tidy.Width*tidy.Height*tidy.Length

print(tidy)
