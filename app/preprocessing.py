import pandas as pd

def prepare_respondent_data(respondents_path: str) -> pd.DataFrame:
    """
    Load and prepare the data 

    Parameters:
    -----------

    link : str
        Link to respondent dataset in .csv format
    """
    responses = pd.read_csv(respondents_path, index_col=0)
    #responses["Q2"] = responses["Q2"].fillna('other')

    return responses