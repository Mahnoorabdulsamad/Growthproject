#streamlit
import streamlit as st

st.set_page_config(page_title="Streamlit App", page_icon=":shark:")
st.title("Growth Mindset Challenge: Web App with Streamlit")

st.header("Welcome to the Growth Mindset Challenge!")
st.write("Embrace challenges,learn from mistakes, and unlock your full potential. This AI powered web app will help you to develop a growth mindset.")

#quote section
st.header("Today's Growth Mindset Quote")
st.write("“Success is not about being the best. It’s about always getting better.” – Behance")

st.header("What's Your Growth Mindset Today Challenge?")
user_input = st.text_input("Describe a challenge you are facing today:")
#conditional statement
if user_input:
    st.success(f"you are facing: {user_input}.Keep going!")
else:
    st.warning("What challenge are you facing today?")    

    #reflexing
st.header("Daily Reflexion")
reflexion = st.text_area("How did you overcome the challenge?")
if reflexion:
    st.success(f"Great job! Keep going!{reflexion}")
else:
    st.info("Reflecting on past challenges can help you to grow.share your difficulties and how you overcame them.")
    #cheivements
st.header("Celebrate Your Achievements")
achievement = st.text_input("What did you achieve today?")
if achievement:
    st.success(f"Congratulations! You achieved: {achievement}.Keep it up!")
else:
    st.info("Big or small, every achievement counts. Share your achievements with us!🥰")

    #footer
    st.write("_ _ _")
    st.write("Never give up, because great things take time and perseverance.🚀")
    st.write("**©️ Developed with ❤️ by Mahnoor**")
 


