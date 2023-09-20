import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    df=views[views.author_id==views.viewer_id][["author_id"]]
    return df.drop_duplicates().sort_values(by="author_id").rename(columns={"author_id":"id"})
    
