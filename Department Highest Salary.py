import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    df=(employee.merge(department,left_on="departmentId",right_on="id"))
    df2=df.groupby("name_y").max().reset_index()[["salary","name_y"]]
    return (df.merge(df2)[["name_y","name_x","salary"]].rename(columns={"name_y":"Department","salary":"Salary","name_x":"Employee"}))
