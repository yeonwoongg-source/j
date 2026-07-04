import streamlit as st
import random

# 페이지 설정
st.set_page_config(page_title="가위바위보 게임", layout="centered")

# 배경색과 글씨색
st.markdown("""
<style>
body {
    background-color: white;
    color: black;
}
.stApp {
    background-color: white;
}
h1, h2, h3, p {
    color: black;
    text-align: center;
}
div.stButton > button {
    display: block;
    margin: auto;
    font-size: 24px;
    padding: 10px 25px;
}
</style>
""", unsafe_allow_html=True)

# 세션 상태 초기화
if "screen" not in st.session_state:
    st.session_state.screen = "start"

if "player" not in st.session_state:
    st.session_state.player = ""

if "computer" not in st.session_state:
    st.session_state.computer = ""

if "result" not in st.session_state:
    st.session_state.result = ""

emoji = {
    "가위": "✌️",
    "바위": "✊",
    "보": "✋"
}

# 승패 판정 함수
def judge(player, computer):
    if player == computer:
        return "무승부"

    if player == "가위":
        if computer == "바위":
            return "패배"
        else:
            return "승리"

    if player == "바위":
        if computer == "가위":
            return "승리"
        else:
            return "패배"

    if player == "보":
        if computer == "가위":
            return "패배"
        else:
            return "승리"

# ---------------- 시작 화면 ----------------
if st.session_state.screen == "start":

    st.markdown("<h1>가위바위보 게임</h1>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns([2,1,2])

    with col2:
        if st.button("시작하기"):
            st.session_state.screen = "select"
            st.rerun()

# ---------------- 선택 화면 ----------------
elif st.session_state.screen == "select":

    st.markdown("<h2>무엇을 낼까요?</h2>", unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)

    with c1:
        if st.button("✌️", use_container_width=True):
            st.session_state.player = "가위"

    with c2:
        if st.button("✊", use_container_width=True):
            st.session_state.player = "바위"

    with c3:
        if st.button("✋", use_container_width=True):
            st.session_state.player = "보"

    if st.session_state.player != "":
        st.session_state.computer = random.choice(["가위", "바위", "보"])
        st.session_state.result = judge(
            st.session_state.player,
            st.session_state.computer
        )
        st.session_state.screen = "result"
        st.rerun()

# ---------------- 결과 화면 ----------------
elif st.session_state.screen == "result":

    st.markdown("<h2>컴퓨터</h2>", unsafe_allow_html=True)
    st.markdown(
        f"<h1 style='text-align:center'>{emoji[st.session_state.computer]}</h1>",
        unsafe_allow_html=True
    )

    st.markdown(
        f"<h2 style='text-align:center'>{st.session_state.result}</h2>",
        unsafe_allow_html=True
    )

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("<h2>나</h2>", unsafe_allow_html=True)
    st.markdown(
        f"<h1 style='text-align:center'>{emoji[st.session_state.player]}</h1>",
        unsafe_allow_html=True
    )

    st.markdown("<br>", unsafe_allow_html=True)

    if st.button("돌아가기"):
        st.session_state.screen = "start"
        st.session_state.player = ""
        st.session_state.computer = ""
        st.session_state.result = ""
        st.rerun()
