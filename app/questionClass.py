import pandas as pd
import plotly.express as px
import streamlit as st

def get_value_pcts(df_question):
    vc = df_question.value_counts()
    vc = vc.apply(lambda x: round((x / vc.sum())*100))
    return vc

def get_vc(df_question):
    vc = df_question.value_counts().reset_index()
    vc.columns.values[0] = 'Answer'
    vc.columns.values[1] = 'Counts'
    vc["Percent"] = vc['Counts'].apply(lambda x: round((x / vc['Counts'].sum())*100))
    return vc


class Question:
    """
    Base class for all question types.

    Input: question columns and respondent dataframe. 
    """

    def __init__(self, question, response_df) -> None:
        self.question = question
        self.response_df = response_df
        

    def display_count(self):
        count = self.response_df[self.question].count()
        st.markdown(f'{count} participants answered this question.')

        

class NumericQuestion(Question):
    def __init__(self, question, response_df) -> None:
        super().__init__(question, response_df)
        self.mean = round(self.response_df[self.question].mean())
        self.median = round(self.response_df[self.question].median())
        self.min = round(self.response_df[self.question].min())
        self.max = round(self.response_df[self.question].max())
    
    def display_data(self) -> None:
        self.display_count()
        data =  [self.mean, self.median, self.min, self.max]
        col1, col2, col3 = st.columns(3)
        col1.metric("Mean", f'{data[0]}')
        col2.metric("Median", f'{data[1]}')
        col3.metric("Range", f'{data[2]} - {data[3]}')


class LikertQuestion(Question):
    def __init__(self, question, response_df) -> None:
        super().__init__(question, response_df)
        self.mean = round(self.response_df[self.question].mean())
        self.median = round(self.response_df[self.question].median())
        self.vpct = get_value_pcts(self.response_df[self.question])
        self.vc = get_vc(self.response_df[self.question])


    def display_data(self) -> None:
        self.display_count()
        st.markdown(f'**Mean:** {self.mean}')
        st.markdown(f'**Median:** {self.median}')
        st.markdown("##### Likert Breakdown")
        col1, col2, col3, col4, col5 = st.columns(5)
        with col1:
            try:
                col1.metric("1", f'{self.vpct[1]}%')
            except KeyError: 
                col1.metric("1", f'0%')
        with col2:
            try:
                col2.metric("2", f'{self.vpct[2]}%')
            except KeyError: 
                col2.metric("2", f'0%')
        col3.metric("3", f'{self.vpct[3]}%')
        col4.metric("4", f'{self.vpct[4]}%')
        with col5:
            col5.metric("5", f'{self.vpct[5]}%')

        # Display Graph
        fig = px.bar(self.vc, x='Answer', y='Counts', hover_data=['Percent'])
        st.plotly_chart(fig, theme='streamlit')
            


class ShortQuestion(Question):
    def __init__(self, question, response_df) -> None:
        super().__init__(question, response_df)
        self.answers = self.response_df.loc[self.response_df[self.question].notnull() == True][self.question]

    def display_data(self) -> None:
        self.display_count()
        st.dataframe(self.answers)

class MultipleQuestion(Question):
    def __init__(self, question, response_df) -> None:
        super().__init__(question, response_df)
        self.vc = get_vc(self.response_df[self.question])

    def display_data(self) -> None:
        self.display_count()
        fig = px.bar(self.vc, x='Answer', y='Counts', hover_data=['Percent'])
        st.plotly_chart(fig, theme='streamlit')

class MultipleAnswerQuestion(Question):
    def __init__(self, question, response_df) -> None:
        super().__init__(question, response_df)

    def display_data(self) -> None:
        #questions = self.question.split(',')
        
        answer_names = []
        answer_counts = []
        for column in self.question:
            count = self.response_df[self.response_df[column] == 1].shape[0]
            column_name = column.split(':')[-1]
            answer_names.append(column_name)
            answer_counts.append(count)
        data = pd.DataFrame(list(zip(answer_names, answer_counts)), columns =['Answer', 'Counts'])     
        
    

        #st.markdown(f'{count} participants answered this question.')
        fig = px.bar(data, x='Answer', y='Counts')
        st.plotly_chart(fig, theme='streamlit')
        
        

question_mapping = {
    "Number": NumericQuestion,
    "Likert": LikertQuestion,
    "Multiple Choice": MultipleQuestion,
    "Multiple Answer": MultipleAnswerQuestion,
    "Likert - Multiple Answer": MultipleAnswerQuestion,
    "Open Ended": ShortQuestion,
}