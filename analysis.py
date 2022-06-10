import numpy as np
import pandas as pd
import textblob as tb

kot_df = pd.read_csv('kotkin_comments.csv')
sto_df = pd.read_csv('stone_comments.csv')

print(len(kot_df))
print(len(sto_df))