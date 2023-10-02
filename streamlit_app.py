import streamlit as st
import lgcn_cd as lch

#App tille 
st.title("Pets Name Generator")
st.subheader('This app super is :blue[cool] :100:')
# A selectbox for selecting the animals types
animal_type = st.sidebar.selectbox("What is your pet?", ("Dog", "Cat", "Hamster", "Snake", "Lizard"))

#With if statement, define the the label en the max character according to the type of animal
if animal_type == "Dog":
  pet_color = st.sidebar.text_area(label="What color is your dog?", max_chars=15)

if animal_type == "Cat":
  pet_color = st.sidebar.text_area(label="What color is your cat?", max_chars=15)

if animal_type == "Hamster":
  pet_color = st.sidebar.text_area(label="What color is your hamster?", max_chars = 15)

if animal_type == "Snake":
  pet_color = st.sidebar.text_area(label="What color is your snake?", max_chars = 25)

if animal_type == "Lizard":
  pet_color = st.sidebar.text_area(label="What color is your lizard?", max_chars = 25)


#Define the input text in witch the user set his openia key
with st.sidebar:
    openai_api_key = st.text_input("OpenAI API Key", key="langchain_search_api_key_openai", type="password")
    "[Get an OpenAI API key](https://platform.openai.com/account/api-keys)"
    
if pet_color:
    if not openai_api_key:
      st.info("Please add your OpenAI API key to continue.")
      st.stop()
    if len(openai_api_key) != 51:
       st.info("Check your OpenAI API key: it may be too short or too long.")
       st.stop()

    response = lch.generate_pet_name(animal_type, pet_color, openai_api_key)
    st.text(response['pet_name'])
                     
