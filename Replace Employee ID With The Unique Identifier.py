import pandas as pd

def replace_employee_id(employees: pd.DataFrame, employee_uni: pd.DataFrame) -> pd.DataFrame:
    results=pd.merge(employees,employee_uni,on="id",how="left")[["unique_id","name"]]
    return results
    
