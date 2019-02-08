
#%%
import pandas as pd   # every changed line must be interpreted in sequence again


#%%
user_cols = ['Subject code' , 'col0' , 'col1' , 'col2' , 'InSem', 'col4' , 'Theory', 'col6' , 'Total', 'col8' , 'TermWork', 'col10' , 'PR', 'col12' , 'OR', 'col14' , 'col15', 'col16' ]

dfd = pd.read_csv('TGUIOP.csv' , sep=r'\s*( */*,*,,*,,,*)*\s', header =None, names=user_cols,engine="python") 


#%%
dfd.to_csv('goodOP.csv')


#%%
# sep=r'\s*( */*,*,,*,,,*)*\s'    engine="python" sep=r'\s*( )*(,,,)*(,,)*(,)*\s'  sep=r"\s"  #sep=r'\ *(:|\,,,|\,,|\,)\s*'   sep= " |,|,,|,,,|:"  " |:|,,,"


