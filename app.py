import streamlit as st
import pandas as pd
import re

st.set_page_config(page_title="썸데이 지해 대사 & 넘버 연습", page_icon="🎭", layout="centered")

# 사용자가 업로드한 원본 파일명 반영
@st.cache_data
def load_data():
    return pd.read_csv("썸데이_지해_큐_대사_정리 - 지해대사+Cue.csv", encoding="utf-8")

try:
    df = load_data()
except Exception as e:
    st.error(f"데이터 파일을 불러오는 중 오류가 발생했습니다: {e}")
    st.stop()

# 사이드바 메뉴 네비게이션
st.sidebar.title("📌 연습 메뉴 선택")
menu = st.sidebar.radio("이동할 페이지", ["🎭 지해 대사 연습", "🎵 넘버(노래) 연습"])

# 구글 드라이브 링크 변환 함수
def convert_gdrive_link(url):
    if not url or pd.isna(url):
        return "", ""
    match = re.search(r'/file/d/([a-zA-Z0-9_-]+)', str(url))
    if match:
        file_id = match.group(1)
        preview_url = f"https://drive.google.com/file/d/{file_id}/preview"
        return preview_url, str(url)
    return "", str(url)

if menu == "🎭 지해 대사 연습":
    st.title("🎭 지해 대사 암기 & 연습 프로그램")
    st.markdown("상대방의 이전 대사(또는 노래/상황)를 보고 나의 지해 대사를 떠올려보세요!")

    # 세션 상태 초기화
    if "dialogue_index" not in st.session_state:
        st.session_state.dialogue_index = 0
    if "show_answer" not in st.session_state:
        st.session_state.show_answer = False

    def reset_answer():
        st.session_state.show_answer = False

    col1, col2, col3 = st.columns([1, 2, 1])
    with col1:
        if st.button("⬅️ 이전 대사", use_container_width=True):
            if st.session_state.dialogue_index > 0:
                st.session_state.dialogue_index -= 1
                reset_answer()
    with col3:
        if st.button("다음 대사 ➡️", use_container_width=True):
            if st.session_state.dialogue_index < len(df) - 1:
                st.session_state.dialogue_index += 1
                reset_answer()

    current_row = df.iloc[st.session_state.dialogue_index]

    st.markdown("---")
    st.caption(f"📍 전체 진행 상황: {st.session_state.dialogue_index + 1} / {len(df)} (원래 시트 행 번호: {int(current_row['index'])})")

    # 이전 대사 (상대방 대사, 노래 또는 상황)
    st.subheader("💬 상대방 이전 대사 / 노래 / 큐")
    prev_line = str(current_row['이전대사'])
    prev_speaker = str(current_row['이전화자'])

    if pd.isna(prev_line) or prev_line.strip() == "":
        st.info("(이전 대사 없음 / 해당 씬의 첫 대사입니다)")
    else:
        if prev_speaker == '노래':
            lines = prev_line.split('\n')
            song_title = lines[0]
            link_url = ""
            for l in lines:
                if "http" in l:
                    link_url = l.strip()
            
            st.warning(f"🎵 노래/넘버: **{song_title}**")
            if link_url:
                preview_url, original_url = convert_gdrive_link(link_url)
                if preview_url:
                    st.markdown(f"🎧 [구글 드라이브 MR 플레이어 창에서 열기]({original_url})")
                    st.components.v1.iframe(f"https://drive.google.com/file/d/{re.search(r'/file/d/([a-zA-Z0-9_-]+)', original_url).group(1)}/preview", height=100)
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
    selected_idx = st.slider("빠른 이동 (대사 번호 선택)", 1, len(df), st.session_state.dialogue_index + 1)
    if selected_idx - 1 != st.session_state.dialogue_index:
        st.session_state.dialogue_index = selected_idx - 1
        reset_answer()
        st.rerun()

elif menu == "🎵 넘버(노래) 연습":
    st.title("🎵 넘버(노래) 가사 & MR 연습")
    st.markdown("작품 속 노래(넘버)들의 가사를 확인하고 구글 드라이브 MR을 바로 재생하거나 링크로 열어 연습하세요!")

    song_df = df[df['이전화자'] == '노래'].copy()
    
    song_options = []
    song_map = {}
    for idx, row in song_df.iterrows():
        text = str(row['이전대사'])
        title = text.split('\n')[0].strip()
        if title not in song_map:
            song_map[title] = {
                'full_text': text,
                'lyric': str(row['지해대사'])
            }
            song_options.append(title)

    if song_options:
        selected_song = st.selectbox("🎵 연습할 넘버 선택하기", song_options)
        
        if selected_song:
            song_info = song_map[selected_song]
            full_text = song_info['full_text']
            
            link_url = ""
            for l in full_text.split('\n'):
                if "http" in l:
                    link_url = l.strip()
            
            st.markdown(f"### 🎶 {selected_song}")
            
            if link_url:
                preview_url, original_url = convert_gdrive_link(link_url)
                st.success("✨ 구글 드라이브 MR 링크가 등록되어 있습니다.")
                st.markdown(f"🔗 [구글 드라이브 새창에서 열기]({original_url})")
                
                if preview_url:
                    match_id = re.search(r'/file/d/([a-zA-Z0-9_-]+)', original_url)
                    if match_id:
                        file_id = match_id.group(1)
                        st.markdown("#### 🎧 MR 재생 플레이어")
                        st.components.v1.iframe(f"https://drive.google.com/file/d/{file_id}/preview", height=150)
            else:
                st.info("ℹ️️ 이 넘버에는 등록된 MR 링크가 없습니다.")
            
            st.markdown("---")
            st.subheader("📝 해당 넘버 / 가사 및 대사 내용")
            st.info(song_info['lyric'])
    else:
        st.warning("등록된 넘버 데이터가 없습니다.")