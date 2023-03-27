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


@st.cache # Caches the data and only run it if it has not been seen before
def load_data(): 
    #DATA_PATH = os.path.join(pathlib.Path(__file__).parent.resolve(), "data")
    DATA_URL = "https://raw.githubusercontent.com/Ready-Set-Care/groceries-survey/main/Data/"

    GEN_POP_PATH = DATA_URL + "raw_gen_pop.csv"
    CAREGIVERS_PATH = DATA_URL + 'raw_caregivers.csv'

    gen_pop_df = results.prepare_data(GEN_POP_PATH)
    caregiver_responses_df = results.prepare_data(CAREGIVERS_PATH)
    questions_df = questions.get_question_df()

    responses_df = results.combine_data(gen_pop_df, caregiver_responses_df)
    
    return responses_df, questions_df

def load_results_page(df, questions):

    data = results.select_data(df)

    selection = st.selectbox(
        "Select the one of the segmentations:",
        ('All Data', 'Caregivers v. General Pop', "Community Classification")
        )

    st.markdown(f'## Survey Results for {selection}')

    if selection == "Caregivers v. General Pop":
        segments = segmentation.get_segmentation()
        results.get_response_data(data, segments, "Q18")
    elif selection == "Community Classification":
        segments = segmentation.get_segmentation("Community Classification", df)
        results.get_response_data(data, segments, "Variable: External: Q3: _ Urban/Rural (self-report)")
    else:
        results.get_response_data(data, questions)

if __name__ == "__main__":
    main()