def get_segmentation(segment_name, df):
    """
    Parameters
    ----------
        segment_name: the name of segment
        df: the entire dataframe
    Output
    ------
    Python dict:
        Keys -> name of each segment within the segmentation
        Values -> the code that goes inside df.loc[____] to access
    """

    SEGMENTATIONS = {
        "Community Classification": {
            "Urban": df.loc[df["Variable: External: Q3: _ Urban/Rural (self-report)"] == "Urban (metropolis or a city)"],
            "Suburban": df.loc[df["Variable: External: Q3: _ Urban/Rural (self-report)"] == "Suburban/semiurban (residential area on outskirts of a city)"],
            "Rural": df.loc[df["Variable: External: Q3: _ Urban/Rural (self-report)"] == "Rural (settled place outside a town or city)"]
        },
        "Income": {
            "Not fair at all": df.loc[df["Q9"] == 1],
            "Somewhat unfair":  df.loc[df["Q9"] == 2],
            "Neutral":  df.loc[df["Q9"] == 3],
            "Somewhat fair":  df.loc[df["Q9"] == 4],
            "Very fair":  df.loc[df["Q9"] == 5]
        }
    }

    return SEGMENTATIONS.get(segment_name, 'Not Found') # if not presemt, return 'Not found'