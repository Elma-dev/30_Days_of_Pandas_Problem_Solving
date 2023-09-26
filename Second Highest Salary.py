import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    salaries=employee.salary.drop_duplicates().to_frame()
    secondLargest=salaries.salary.nlargest(2).iloc[-1] if salaries.shape[0]>=2 else None
    return pd.DataFrame({"SecondHighestSalary":[secondLargest]})
    
