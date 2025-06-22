from openai import OpenAI
import streamlit as st
user_db={"mahes":{"password":"mahes1302"}}
def login_page():
    with st.form("Login"):
        st.title(" Login to your account")
        username=st.text_input("Username",placeholder="Enter username/email id")
        password=st.text_input("Password",placeholder="Enter Password",type="password")
        if st.form_submit_button("Login"):
            if username in user_db and user_db[username]["password"]==password:
                st.success("Login successful!")
                st.session_state["authenticated"]=True
                st.session_state["username"]=username
                st.session_state["page"]="chatbot"
                st.rerun()

            else:
                st.error("Invalid username or password")
def gemini_bot(place_name):
    
    clien = OpenAI(api_key="AIzaSyBebu9JXr_Ek0uruCAuFXWs-v5dbDKmNao")

    response = clien.chat.completions.create(model="gpt-4",messages=[{"role": "user", "content": f"Act as a tourist guide for TamilNadu southern districts. Respond to: {place_name}"}])

    st.markdown(response.choices.message.content)

    

   

def chatbot():
    st.title("Alaiva Chatbot")
    if st.button("Sign-of"):
            st.session_state["authenticated"]=False
            st.session_state["page"]="Login"
            st.rerun()
    st.write(f"Hello,Welcome to Alaiva touist Guide chatbot,{st.session_state['username']}")
    place_name = st.chat_input("Ask about tourist places in Tamil Nadu south districts")
    if place_name:
        gemini_bot(place_name)

          
#main app

if "authenticated" not in st.session_state:
    st.session_state["authenticated"]=False
if "page" not in st.session_state:
    st.session_state["page"]="Login"


if st.session_state["page"]=="Login":
    login_page()
elif st.session_state["page"]=="chatbot":
    chatbot()