import streamlit as st

# Custom Functions
import preprocessing
import homepage

def main():
    st.title('Groceries Survey Analysis')
    page = st.sidebar.selectbox("Please select a page:", ["Homepage", "Results"])
    respondent_df = load_data()

    if page == "Homepage":
        homepage.load_homepage()
    #elif page == "Questions":
     #   load_question_page(question_df)
    elif page == "Results":
        load_results_page(respondent_df)


@st.cache # Caches the data and only run it if it has not been seen before
def load_data(): 
    #DATA_PATH = os.path.join(pathlib.Path(__file__).parent.resolve(), "data")
    DATA_URL = "https://raw.githubusercontent.com/Ready-Set-Care/groceries-survey/main/Data/"

    GEN_POP_PATH = DATA_URL + "raw_gen_pop.csv"
    CAREGIVERS_PATH = DATA_URL + 'raw_caregivers.csv'
    
    #question_df = preprocessing.prepare_questions(QUESTION_PATH)
    respondent_df = preprocessing.prepare_respondent_data(GEN_POP_PATH)
    
    return respondent_df

def load_results_page():
    st.markdown('# WIP')

if __name__ == "__main__":
    main()