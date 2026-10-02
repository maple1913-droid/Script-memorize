import streamlit as st
import pandas as pd
import os

# 페이지 설정 (모바일 최적화)
st.set_page_config(page_title="뮤지컬 <썸데이> 지해 대사 암기 연습", page_icon="🎭", layout="centered")

@st.cache_data
def load_script_data():
    # 업로드된 엑셀 파일 찾기
    excel_files = [f for f in os.listdir('.') if f.endswith('.xlsx')]
    if not excel_files:
        return None, "엑셀 파일(.xlsx)을 찾을 수 없습니다."
    
    filename = excel_files[0]
    df = pd.read_excel(filename, sheet_name=0)
    
    # 엑셀 데이터에서 '지해' 대사 추출 및 직전 대사를 CUE로 매핑
    pairs = []
    jihae_indices = df[df['화자'] == '지해'].index.tolist()
    
    for idx in jihae_indices:
        if idx > 0:
            cue_row = df.loc[idx - 1]
            jihae_row = df.loc[idx]
            
            cue_speaker = str(cue_row['화자']).strip()
            cue_line = str(cue_row['대사']).strip()
            my_line = str(jihae_row['대사']).strip()
            
            pairs.append({
                "cue_speaker": cue_speaker,
                "cue_line": cue_line,
                "my_line": my_line
            })
            
    return pairs, filename

script_pairs, file_source = load_script_data()

st.title("🎭 뮤지컬 <썸데이> 지해 대사 암기 연습")

if script_pairs is None:
    st.error(file_source)
    st.stop()

# 전체 대사를 하나의 연습 세트로 구성 (또는 필요시 구간별 슬라이싱 가능)
total_lines = len(script_pairs)

# 세션 상태 초기화
if "line_index" not in st.session_state:
    st.session_state.line_index = 0

# 상단 진행 상황 표시
st.progress((st.session_state.line_index + 1) / total_lines)
st.caption(f"전체 진행 상황: {st.session_state.line_index + 1} / {total_lines} 대사 (출처: {file_source})")

st.markdown("---")

current_data = script_pairs[st.session_state.line_index]
cue_speaker = current_data['cue_speaker']
cue_line = current_data['cue_line']
my_line = current_data['my_line']

# 화면 상단: 상대방의 직전 대사 (CUE)
st.markdown(f"### 💬 상대방 직전 대사 CUE **[{cue_speaker}]**")
st.warning(f"\"{cue_line}\"")

st.markdown("---")

# 네비게이션 버튼 (이전 / 다음)
col1, col2 = st.columns(2)

with col1:
    if st.button("⬅️ 이전 대사", use_container_width=True):
        if st.session_state.line_index > 0:
            st.session_state.line_index -= 1
            st.rerun()

with col2:
    if st.button("➡️ 다음 대사", use_container_width=True):
        if st.session_state.line_index < total_lines - 1:
            st.session_state.line_index += 1
            st.rerun()

# 하단 체크박스: 내가 쳐야 할 정답(지해 대사) 확인
show_answer = st.checkbox("🔑 내가 쳐야 할 대사 (정답 보기)", value=False)

if show_answer:
    st.success(f"**[내 대사 - 지해]**\n\n🗣️ {my_line}")

st.markdown("---")

if st.button("🔄 처음부터 다시 연습", use_container_width=True):
    st.session_state.line_index = 0
    st.rerun()
