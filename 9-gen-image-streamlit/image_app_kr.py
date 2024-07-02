import streamlit as st #모든 streamlit 명령은 "st" 별칭을 통해 사용할 수 있습니다
import image_lib_kr as glib #로컬 라이브러리 스크립트 참조

st.set_page_config(layout="wide", page_title="Image Generation") #컬럼을 위해 페이지 너비를 더 넓게 설정

st.title("Image Generation") #페이지 제목

col1, col2 = st.columns(2) #2개 컬럼 생성

with col1: #이 with 블록의 모든 내용이 컬럼 1에 배치됨
    st.subheader("Image generation prompt") #이 컬럼의 서브헤드
    
    prompt_text = st.text_area("Prompt text", height=200, label_visibility="collapsed") #레이블이 없는 여러 줄 텍스트 상자 표시
    
    process_button = st.button("Run", type="primary") #기본 버튼 표시
    
with col2: #이 with 블록의 모든 내용은 컬럼 2에 배치됩니다
    st.subheader("Result") #이 컬럼의 서브헤드
    
    if process_button: #버튼을 클릭하면 이 if 블록의 코드가 실행됩니다
        with st.spinner("Drawing..."): #이 with 블록의 코드가 실행되는 동안 스피너를 표시합니다
            generated_image = glib.get_image_response(prompt_content=prompt_text) #지원 라이브러리를 통해 모델을 호출합니다
        
        st.image(generated_image) #생성된 이미지를 표시합니다
