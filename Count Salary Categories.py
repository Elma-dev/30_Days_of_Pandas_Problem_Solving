import pandas as pd

def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    d={"category":["Low Salary","Average Salary","High Salary"],"accounts_count":[]}
    d["accounts_count"].append(len(accounts[accounts.income<20000]))
    d["accounts_count"].append(len(accounts[(accounts.income>=20000) & (accounts.income<=50000)]))
    d["accounts_count"].append(len(accounts[accounts.income>50000]))
    return pd.DataFrame(d)


    
