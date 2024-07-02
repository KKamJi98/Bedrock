import streamlit as st # pip install -U streamlit

# 실제 페이지의 페이지 제목과 브라우저 탭에 표시되는 제목 설정
st.set_page_config(page_title="Streamlit Demo") #HTML 제목
st.title("Streamlit Demo") #page 제목

# 입력 요소 추가
# 사용자로부터 색상을 가져오는 입력 텍스트 상자와 버튼을 생성
color_text = st.text_input("가장 좋아하는 색깔이 뭔가요?") #텍스트 상자 표시
go_button = st.button("Go", type="primary") #기본 버튼 표시

# 출력 요소 추가
if go_button: #버튼이 클릭될 때 이 if 블록의 코드가 실행됩니다.
    st.write(f"저도 {color_text} 좋아해요!") #응답 콘텐츠 표시
