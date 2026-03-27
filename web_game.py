import streamlit as st
import random
import base64

def get_base64_image(image_path):
    with open(image_path, "rb") as f:
        return base64.b64encode(f.read()).decode()

img = get_base64_image("ww_icon.png")
st.markdown(f"""
    <style>
    .stApp {{
        background: linear-gradient(135deg, #1a1a2e, #1f5c99);
        color: #eaeaea;
    }}
    .stApp::before {{
        content: "";
        position: fixed;
        top: 50%;
        left: 25%;
        transform: translate(-50%, -50%) rotate(-15deg);
        width: 80%;
        height: 80%;
        background-image: url("data:image/png;base64,{img}");
        background-repeat: no-repeat;
        background-size: contain;
        background-position: center;
        opacity: 0.08;
        z-index: 0;
        pointer-events: none;
    }}
    .stButton>button {{
        background-color: #1f5c99;
        color: white;
        border: none;
        border-radius: 8px;
        padding: 8px 20px;
        font-weight: bold;
    }}
    .stButton>button:hover {{
        background-color: #4fc3f7;
        color: #1a1a2e;
    }}
    </style>
""", unsafe_allow_html=True)

st.title("Wizardwerks Guessing Game")
st.write("I'm thinking of a number between 1 and 10. Can you guess it?")
if "secret_number" not in st.session_state:
    st.session_state.secret_number = random.randint(1, 10)
    st.session_state.attempts = 0
    st.session_state.won = False
if not st.session_state.won:
    guess = st.number_input("Your guess:", min_value=1, max_value=10, step=1)
    
    if st.button("Guess!"):
        st.session_state.attempts += 1
        
        if guess == st.session_state.secret_number:
            st.session_state.won = True
        elif guess < st.session_state.secret_number:
            st.write("Too low! Try again.")
        else:
            st.write("Too high! Try again.")
if st.session_state.won:
    st.success(f"You got it! It took you {st.session_state.attempts} attempts.")
    
    if st.button("Play Again"):
        st.session_state.secret_number = random.randint(1, 10)
        st.session_state.attempts = 0
        st.session_state.won = False