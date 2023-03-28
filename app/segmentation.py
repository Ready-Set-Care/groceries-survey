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
        "Caregiver Status": {
            "General Population": df.loc[df['Caregiver Status'] == 0],
            "Caregiver": df.loc[df['Caregiver Status'] == 1]
        },
        "Annual Household Income": {
            'Less than $24,999': df.loc[df['Annual Household Income'] == 'Less than $24,999'],
            '\$25,000 - $49,999': df.loc[df['Annual Household Income'] == '$25,000 - $49,999'],
            '\$50,000 - $99,999': df.loc[df['Annual Household Income'] == '$50,000 - $99,999'],
            '\$100,000 - $199,999': df.loc[df['Annual Household Income'] == '$100,000 - $199,999'],
            'More than $200,000': df.loc[df['Annual Household Income'] == 'More than $200,000'],
        }
    }

    return SEGMENTATIONS.get(segment_name, 'Not Found') # if not presemt, return 'Not found'