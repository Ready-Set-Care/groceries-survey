import streamlit as st

def main():
    st.title('Groceries Survey Analysis')
    page = st.sidebar.selectbox("Please select a page:", ["Homepage", "Questions", "Results"])
    question_df, respondent_df = load_data()

    if page == "Homepage":
        homepage.load_homepage()
    elif page == "Questions":
        load_question_page(question_df)
    elif page == "Results":
        load_results_page(respondent_df)


@st.cache # Caches the data and only run it if it has not been seen before
def load_data(): 
    #DATA_PATH = os.path.join(pathlib.Path(__file__).parent.resolve(), "data")
    DATA_URL = ""

    #Change back to data URL
    RESPONDENTS_PATH = ""
    QUESTION_PATH = ''
    
    question_df = preprocessing.prepare_questions(QUESTION_PATH)
    respondent_df = preprocessing.prepare_respondent_data(RESPONDENTS_PATH, OTHER_PATH)
    
    return question_df, respondent_df