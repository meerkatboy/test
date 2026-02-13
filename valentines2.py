import streamlit as st

# --- Page Config ---
st.set_page_config(page_title="for my bibble! ❤️", page_icon="💌")

# --- Style ---
st.markdown("""
<style>
    .stButton>button { width: 100%; border-radius: 20px; height: 3em; background-color: #ff4b4b; color: white; }
    .stProgress > div > div > div > div { background-color: #ff4b4b; }
</style>
""", unsafe_allow_html=True)

# --- Initialize State ---
if 'page' not in st.session_state:
    st.session_state.page = 0
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'total_questions' not in st.session_state:
    st.session_state.total_questions = 5 # Change this if you add more!
if 'no_clicks' not in st.session_state:
    st.session_state['no_clicks'] = 0

# --- Helper Functions ---
def answer_question(is_correct):
    if is_correct:
        st.session_state.score += 1
    next_page()

def next_page():
    st.session_state['page'] += 1
    st.rerun()

def restart():
    st.session_state.page = 0
    st.session_state.score = 0

# --- Progress Bar ---
progress = st.session_state.page / (st.session_state.total_questions + 4) # +3 for Intro and Result pages and gift
st.progress(min(progress, 1.0))

# --- PAGE 0: Introduction ---
if st.session_state['page'] == 0:
    st.title("hi my bibble!")
    st.write("here's a small website for you to play around with! it's my first time making a website so I hope it's cute enough hehe ❤️")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image("https://i.makeagif.com/media/3-15-2017/oh40yM.gif", width=300) # bibble
    with col2:
        st.image("https://media.tenor.com/gjTjxUCoP3sAAAAj/jumping-gatito.gif", width=300) # cat
    with col3:
        st.image("https://i.pinimg.com/originals/78/29/e3/7829e339feb4aa89a7d2f72e4f8cc96a.gif", width=300) # gumball

    st.button("click to progress", on_click=next_page)

# --- PAGE 0: Intro ---
elif st.session_state.page == 1:
    st.title("how well do you know us? 🧐")
    st.write("let's see how good your memory is hehehe")
    col1, col2 = st.columns(2)
    with col1:
        st.image("https://64.media.tumblr.com/fb2c63f2895fc75d4be3a71789ac35f5/a0c78971185bcc6a-bd/s400x600/032b53660ab82065537bf87a3687291f99077a2e.gif")
    with col2:
        st.image("https://i.makeagif.com/media/8-19-2013/rtcTRs.gif")
    st.write("get all correct to win TOP PRIZE 🎁")
    if st.button("START QUIZ 🚀"):
        next_page()

# --- PAGE 1: Question 1 ---
elif st.session_state.page == 2:
    st.subheader("question 1: when did we first meet 1 on 1?")
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("otw home after ocip"): answer_question(False)
    with col2:
        if st.button("studying at msl"): answer_question(True)
    with col3:
        if st.button("dinner in sengkang"): answer_question(False)

# --- PAGE 2: Question 2 ---
elif st.session_state.page == 3:
    st.subheader("question 2: what is the first show/movie we (tried to) watch tgt? 🎬")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image("https://m.media-amazon.com/images/M/MV5BNDAwMjFhYTEtNzYyMS00YmY2LTg3MGEtZTRkNWNiMDI4MDRkXkEyXkFqcGc@._V1_FMjpg_UX1000_.jpg")
        if st.button("how the grinch stole christmas"): answer_question(False)
    with col2:
        st.image("https://ghsgrowl.com/wp-content/uploads/2025/10/When-I-Fly-Towards-You-1.png")
        if st.button("when i fly towards you"): answer_question(False)
    with col3:
        st.image("https://m.media-amazon.com/images/M/MV5BMTM1MTIwNTMxOF5BMl5BanBnXkFtZTcwNjIxMjQyMw@@._V1_.jpg")
        if st.button("the terminal"): answer_question(True)

# --- PAGE 3: Question 3 ---
elif st.session_state.page == 4:
    st.subheader("question 3: when did we first hold hands HEHEHEHE")
    st.subheader("dates are too difficult so will just give you easier options")
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("septmber 18, after going to haidilao"): answer_question(False)
    with col2:
        if st.button("october 11, after going to chinatown"): answer_question(True)
    with col3:
        if st.button("september 6, after dinnering in sengkang"): answer_question(False)

elif st.session_state.page == 5:
    st.subheader("question 4: who is the cuter one among us? (be honest)")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("me (tommy)"): answer_question(False)
    with col2:
        if st.button("you (bibble)"): answer_question(True)

elif st.session_state.page == 6:
    st.subheader("question 5: will you be my valentine's?")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("YEP 😆😆😆😆😆😆😆"):
            st.balloons()
            answer_question(True)
    with col2:
        # The Tricky No Button Logic
        no_texts = ["NOPE 😢😢😢😢😢😢😢", "please try again", "you picked the wrong answer", "👈 try this one"]
        text_index = (st.session_state['no_clicks']) % len(no_texts)
        
        # If No is clicked, just rerun to update text, don't change page
        if st.button(no_texts[text_index]):
            st.session_state['no_clicks'] += 1
            st.rerun()

elif st.session_state.page == 7:
    st.title("Quiz Complete! ✅")
    score = st.session_state.score
    total = st.session_state.total_questions
    
    st.write(f"### Your Score: {score} / {total}")
    
    if score == total:
        st.write("you got FULL MARKS HEHEHE 😍")
    else:
        st.write("close but not close enough HAHAHA but I'll give you a free pass n you still get to redeem the prize because you're rly cute hehe")
        
    if st.button("click here to redeem your prize 🏆"):
        next_page()
    
elif st.session_state.page == 8:
    score = st.session_state.score
    total = st.session_state.total_questions
    if score == total:
        st.write("since you got full marks, you are entitled to:")
    else:
        st.write("although you didn't get full marks, you are still entitled to:")
    
    st.write("🎁 1 redeemable dinner date night at any restaurant of your choice in italy 🇮🇹🍝🍕🍨 ")
    st.write("🎁 1 gift of your choosing that we can pick tgt when we're exploring italy")
    st.write("🎁 1 big, giant hug redeemable at Milan Malpensa Airport on 21st Mar 2026")

    if st.button("Start Over"):
        restart()
        st.rerun()