#%%
import pandas as pd
#%%
data_raw = pd.read_csv('train.csv')

# %%
data_raw.describe()


# %%
data_raw.info()


# %%
for col in data_raw:
    print(data_raw[col].name,data_raw[col].nunique())

# %%
y = data_raw.Survived
data_raw.drop('Survived',axis= 1)

# %%
y


# %%
import seaborn as sns

# %%
sns.
# %%


# %%
