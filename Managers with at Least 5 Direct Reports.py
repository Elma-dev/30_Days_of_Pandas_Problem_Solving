import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    res=employee[["id","name"]].merge(employee[["managerId"]],left_on="id",right_on="managerId")
    res=res.groupby(["id","name"]).count().reset_index()
    return (res[res.managerId>=5][["name"]])
    
