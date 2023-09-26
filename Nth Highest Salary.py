import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    employee=employee.sort_values(by="salary",ascending=False)
    employee=employee.salary.drop_duplicates().to_frame()
    if employee.shape[0]<N:
        return pd.DataFrame({f"getNthHighestSalary({N})":[None]})
    return pd.DataFrame({f"getNthHighestSalary({N})":[employee.salary.iloc[N-1]]}) 
