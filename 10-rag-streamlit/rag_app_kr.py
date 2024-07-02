import streamlit as st
import rag_lib_kr as glib #로컬 라이브러리 스크립트에 대한 참조

st.set_page_config(page_title="Retrieval-Augmented Generation") #HTML 제목
st.title("Retrieval-Augmented Generation") #페이지 제목

# 세션 캐시에 벡터 인덱스 추가
if 'vector_index' not in st.session_state: #벡터 인덱스가 아직 생성되지 않았는지 확인
    with st.spinner("Indexing document..."): #이 with 블록의 코드가 실행되는 동안 스피너를 표시
        st.session_state.vector_index = glib.get_index() #지원 라이브러리를 통해 색인을 검색하고 앱의 세션 캐시에 저장합니다
        
# 입력 요소 추가
input_text = st.text_area("Input text", label_visibility="collapsed") #레이블이 없는 여러 줄 텍스트 상자 표시
go_button = st.button("Go", type="primary") #기본 버튼 표시

# 출력 요소 추가
if go_button: #버튼을 클릭하면 이 if 블록의 코드가 실행
    with st.spinner("Working..."): #이 with 블록의 코드가 실행되는 동안 스피너를 표시합니다
        response_content = glib.get_rag_response(index=st.session_state.vector_index, question=input_text) #지원 라이브러리를 통해 모델을 호출합니다.
        st.write(response_content) #응답 콘텐츠 표시

