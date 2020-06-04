# DataFrameの作成

import numpy as np, pandas as pd
df = pd.DataFrame(np.arange(2,14,2).reshape(2,3),
    columns=['A','B','C'])
df