import pandas as pd
import numpy as np

mat = np.arange(0,50).reshape(5,10)

df = pd.DataFrame(mat)

print(df)
