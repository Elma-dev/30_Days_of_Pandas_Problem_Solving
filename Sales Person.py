import pandas as pd

def sales_person(sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    df=sales_person.merge(orders).merge(company,on="com_id")
    red_sales=df[df.name_y=="RED"].sales_id.values
    return (sales_person[~sales_person.sales_id.isin(red_sales)][["name"]])
    
