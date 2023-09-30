from dotenv import load_dotenv
import streamlit as st
from dsaprompt import DsaPromptChain

def display_article(article_data):
    for each_heading in article_data:
        st.subheader(clean_heading(each_heading))
        if each_heading == 'code':
            st.code(article_data[each_heading], language=language, line_numbers=True)
        else:
            st.write(article_data[each_heading])

def input_problem_statement():
    input_text = st.text_input("Problem Statement: ", key="input")
    return input_text

def language_drop_down():
    option = st.selectbox(
    'Language',
    ('Python', 'Java', 'C', 'C++'))
    return option

def clean_heading(heading):
    head_list = heading.split("_")
    return " ".join(head_list).capitalize()

# # # App Init # # #
global language
load_dotenv()
st.title("DSA Notes App")
st.caption("Build for geeks not for typewriters !")
user_input = input_problem_statement()
language = language_drop_down()
submit = st.button('Generate')    

if submit: 
    init_chain = DsaPromptChain()
    init_chain.init_all_prompts()
    input_request = {}
    input_request["problem_statement"] = user_input
    input_request["language"] = language
    response = init_chain.execute_chain(input_request)
    display_article(response)