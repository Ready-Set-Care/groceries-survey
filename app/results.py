import pandas as pd
import streamlit as st

import questionClass

def prepare_data(path: str) -> pd.DataFrame:
    """
    Load and prepare the data 

    Parameters:
    -----------

    link : str
        Link to respondent dataset in .csv format
    """
    df = pd.read_csv(path, index_col=0)
    df['Variable: External: Q2: Age (write-in)'] = pd.to_numeric(df['Variable: External: Q2: Age (write-in)'])

    return df

def combine_data(gen_pop, caregivers) -> pd.DataFrame:
    # Add a column with Boolean values to distinguish between general population and caregivers. 
    zeroes = gen_pop.shape[0] * [0]
    gen_pop['Caregiver Status'] = zeroes

    ones = caregivers.shape[0] * [1]
    caregivers['Caregiver Status'] = ones

    df = pd.concat([gen_pop, caregivers])

    return df

def select_data(df):
    display_data = st.radio(
        "Select the data:",
        ("All", 'General Population', 'Caregivers')
    )
    
    if display_data == 'General Population':
        data = df.loc[df['Caregiver Status'] == 0]
    elif display_data == 'Caregivers':
        data = df.loc[df['Caregiver Status'] == 1]
    else:
        data = df
    
    return data


def get_response_data(responses_df, question_df, segmentation=None, skip_q=None):

    for index, row in question_df.iterrows():
        question_name = row['Name']
        question_col = row['Columns']
        type = row['Type']

        if question_name != skip_q:
            
            # Check if question type is in "question_mapping" and loop through for each question
            if questionClass.question_mapping.get(type):
                st.markdown(f'#### {question_name}')

                # If data is being segmented, loop through each segment for each question 
                if segmentation is not None:
                    for key, value in segmentation.items():
                        st.markdown(f'##### {key}')
                        instance = questionClass.question_mapping[type](question_col, value)
                        instance.display_data()
                else:
                    instance = questionClass.question_mapping[type](question_col, responses_df)
                    instance.display_data()
            st.markdown('---')
        else:
            continue
