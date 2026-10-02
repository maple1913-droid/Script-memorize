import streamlit as st
import pandas as pd

st.set_page_config(page_title="지해 대사 연습 프로그램", page_icon="🎭", layout="centered")

st.title("🎭 지해 대사 암기 & 연습 프로그램")
st.markdown("상대방의 이전 대사(또는 노래)를 보고 나의 대사를 떠올려보세요!")

@st.cache_data
def load_data():
    return pd.read_csv("jihae_extracted_dialogues.csv")

try:
    df = load_data()
except Exception as e:
    st.error(f"데이터 파일을 불러오는 중 오류가 발생했습니다: {e}")
    st.stop()

# 세션 상태 초기화
if "index" not in st.session_state:
    st.session_state.index = 0
if "show_answer" not in st.session_state:
    st.session_state.show_answer = False

# 인덱스가 바뀔 때 정답 숨기기 초기화 함수
def reset_answer():
    st.session_state.show_answer = False

col1, col2, col3 = st.columns([1, 2, 1])
with col1:
    if st.button("⬅️ 이전 대사", use_container_width=True):
        if st.session_state.index > 0:
            st.session_state.index -= 1
            reset_answer()
with col3:
    if st.button("다음 대사 ➡️", use_container_width=True):
        if st.session_state.index < len(df) - 1:
            st.session_state.index += 1
            reset_answer()

current_row = df.iloc[st.session_state.index]

st.markdown("---")

# 진행 상황 및 씬 위치 정보 표시
st.caption(f"📍 전체 진행 상황: {st.session_state.index + 1} / {len(df)} (원래 시트 행 번호: {int(current_row['index'])})")

# 이전 대사 (상대방 대사 또는 노래)
st.subheader("💬 상대방 이전 대사 / 노래")
prev_line = str(current_row['이전대사'])
prev_speaker = str(current_row['이전화자'])

if pd.isna(prev_line) or prev_line.strip() == "":
    st.info("(이전 대사 없음 / 해당 씬의 첫 대사입니다)")
else:
    if prev_speaker == '노래':
        st.warning(f"🎵 노래/넘버: {prev_line}")
    else:
        st.markdown(f"> **[{prev_speaker}]**\n> {prev_line}")

st.markdown("---")

# 내 대사 (클릭해서 확인)
st.subheader("🎯 나의 대사 (지해)")

if st.button("🔍 정답 확인 / 숨기기", type="primary", use_container_width=True):
    st.session_state.show_answer = not st.session_state.show_answer

if st.session_state.show_answer:
    st.success(current_row['지해대사'])
else:
    st.info("💡 버튼을 눌러 내 대사를 확인해 보세요.")

st.markdown("---")

# 빠른 이동 슬라이더
selected_idx = st.slider("빠른 이동 (대사 번호 선택)", 1, len(df), st.session_state.index + 1)
if selected_idx - 1 != st.session_state.index:
    st.session_state.index = selected_idx - 1
    reset_answer()
    st.rerun()
