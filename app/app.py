import streamlit as st

# Custom Functions
import questions
import results
import homepage
import segmentation


def main():
    st.title('Groceries Survey Analysis')
    page = st.sidebar.selectbox("Please select a page:", ["Homepage", "Results"])
    responses_df, questions_df = load_data()

    if page == "Homepage":
        homepage.load_homepage()
    #elif page == "Questions":
     #   load_question_page(question_df)
    elif page == "Results":
        load_results_page(responses_df, questions_df)


@st.cache_data # Caches the data and only run it if it has not been seen before
def load_data(): 
    #DATA_PATH = os.path.join(pathlib.Path(__file__).parent.resolve(), "data")
    DATA_URL = "https://raw.githubusercontent.com/Ready-Set-Care/groceries-survey/main/Data/"

    GEN_POP_PATH = DATA_URL + "raw_gen_pop.csv"
    CAREGIVERS_PATH = DATA_URL + 'raw_caregivers.csv'

    gen_pop_df = results.prepare_data(GEN_POP_PATH)
    caregiver_responses_df = results.prepare_data(CAREGIVERS_PATH, caregivers=True)
    questions_df = questions.create_question_df()

    responses_df = results.combine_data(gen_pop_df, caregiver_responses_df)
    
    return responses_df, questions_df

def load_results_page(df, questions):
    
    col1, col2 = st.columns(2)
    with col1:
        selection = st.selectbox(
            "Segmentation:",
            ('Not Segmented', 'Caregiver Status', 'Gender', 'Annual Household Income', "Community Classification"))
    with col2:
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

    count = data.shape[0]
    st.markdown(f"**Total Number of participants:** {count}")    

    
    st.markdown(f'## Survey Results for {selection}')
    
    if selection == "Caregiver Status":
        segments = segmentation.get_segmentation("Caregiver Status", data)
        results.get_response_data(data, questions, segments)
    elif selection == 'Gender':
        segments = segmentation.get_segmentation("Gender", data)
        results.get_response_data(data, questions, segments, 'Variable: External: Q1: Gender')
    elif selection == "Community Classification":
        segments = segmentation.get_segmentation("Community Classification", data)
        results.get_response_data(data, questions, segments, "Variable: External: Q3: _ Urban/Rural (self-report)")
    elif selection == 'Annual Household Income':
        segments = segmentation.get_segmentation("Annual Household Income", data)
        results.get_response_data(data, questions, segments, "External Variable: Annual Household Income (US)")
    else:
        results.get_response_data(data, questions)

if __name__ == "__main__":
    main()