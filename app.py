import streamlit as st
import os
import openai

openai.api_key = ""     


engine_dis={'danici':'''Davinci is the most capable engine and can perform any task the other models can perform and often with less instruction. For applications requiring a lot of understanding of the content, like summarization for a specific audience and content creative generation, Davinci is going to produce the best results. The trade-off with Davinci is that it costs more to use per API call and other engines are faster.\nAnother area where Davinci shines is in understanding the intent of text. Davinci is quite good at solving many kinds of logic problems and explaining the motives of characters. Davinci has been able to solve some of the most challenging AI problems involving cause and effect.''',
            'curie':'''Curie is extremely powerful, yet very fast. While Davinci is stronger when it comes to analyzing complicated text, Curie is quite capable for many nuanced tasks like sentiment classification and summarization. Curie is also quite good at answering questions and performing Q&A and as a general service chatbot.''',
            'babbage':'''Babbage can perform straightforward tasks like simple classification. It’s also quite capable when it comes to Semantic Search ranking how well documents match up with search queries.''',
            'ada':'''Ada is usually the fastest model and can perform tasks like parsing text, address correction and certain kinds of classification tasks that don’t require too much nuance. Ada’s performance can often be improved by providing more context.'''}
st.header("AskMeAnything")

prompt_input=st.text_input("") 
if st.checkbox("Show Advance Options:"):
    engine_input=st.selectbox("Engine",['ada','babbage','curie','davinci'])




response = openai.Completion.create(
  engine="curie",
  prompt=prompt_input,
  temperature=0,
  max_tokens=200,
  top_p=1,
  frequency_penalty=0.0,
  presence_penalty=0.0
)
st.write(response.choices[0].text)
st.write(response)