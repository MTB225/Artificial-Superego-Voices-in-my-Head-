from groq import Groq
import streamlit as st


client = Groq(api_key=st.secrets["GROQ_API_KEY"])
model_name ="llama3-8b-8192"
if model_name not in st.session_state:
    st.session_state.model_name = model_name
SYSTEM_PROMPT = "Make five different personalities in which each personality has an extremely high value for one of each of the traits and an extremely low value for all the other traits (The traits as outlined in the Big Five personality traits, those being Openness, Conscientiousness, Extraversion, Agreeableness and Neuroticism) and refrain from naming them. Make the first personality high on openness and low on all others, then the second one high on conscientiousness and low on all others, then the third one high on extraversion and low on all others, then the fourth one high on agreeableness and low on all others and then the fith one high on neuroticism and low on all others. Then, make a sixth neutral personality that will find consensus amongst the five of them. You will generally be provided ethical dilemmas and you should consider them very carefully. As such, do not present silly/humorous responses. Present the scenario of the prompt in a detailed and clear paragraph. Now, for a given prompt, have the first five provide answers as well as detailed and at least 100 words long paragraphs as reasons for the answer, making 'decision' and 'reason' seperate headings. Then, have the sixth one find common ground among them."
Question=st.text_input("Enter your dilemma: ")
completion = client.chat.completions.create(
    model=model_name,
    messages=[
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        },
        {
            "role": "user",
            "content": Question
        }
    ],
    temperature=0.5,
    max_tokens=8192,
    top_p=1,
    stream=False,
    stop=None,
)

st.markdown(completion.choices[0].message.content)