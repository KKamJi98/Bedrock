import streamlit as st 
import chatbot_lib_kr as glib

st.set_page_config(page_title="Chatbot") #HTML 제목
st.title("Chatbot") #페이지 제목

# 세션 캐시에 LangChain 메모리를 추가
# 사용자 세션당 고유한 채팅 메모리 유지
# 그렇지 않으면 챗봇이 사용자와의 과거 메시지를 기억할 수 없음
# Streamlit에서는 세션 상태가 서버 측에서 추적됨
# 브라우저 탭이 닫히거나 애플리케이션이 중지되면 세션과 해당 채팅 기록이 손실됨
# 실제 애플리케이션에서는 Amazon DynamoDB 와 같은 데이터베이스에서 채팅 기록을 추적 가능
if 'memory' not in st.session_state: #메모리가 아직 생성되지 않았는지 확인합니다.
    st.session_state.memory = glib.get_memory() #메모리 초기화
        
# UI 채팅 기록을 세션 캐시에 추가
if 'chat_history' not in st.session_state: #채팅 내역이 아직 생성되지 않았는지 확인합니다.
    st.session_state.chat_history = [] #채팅 내역 초기화

#채팅 기록 다시 렌더링(Streamlit은 이 스크립트를 다시 실행하므로 이전 채팅 메시지를 보존하려면 이 기능이 필요합니다.)
for message in st.session_state.chat_history: #채팅 기록 루프
    with st.chat_message(message["role"]): #지정된 역할에 대한 챗 라인을 렌더링하며, with 블록의 모든 내용을 포함
        st.markdown(message["text"]) #챗 컨텐츠 출력
        
# 입력 요소 추가
input_text = st.chat_input("Chat with your bot here") #채팅 입력 상자 표시

if input_text: #사용자가 채팅 메시지를 제출한 후 이 if 블록의 코드를 실행합니다.
    
    with st.chat_message("user"): #사용자 채팅 메시지 표시
        st.markdown(input_text) #사용자의 최신 메시지를 렌더링합니다.
    
    st.session_state.chat_history.append({"role":"user", "text":input_text}) #사용자의 최신 메시지를 채팅 기록에 추가합니다.
    
    chat_response = glib.get_chat_response(input_text=input_text, memory=st.session_state.memory) #지원 라이브러리를 통해 모델을 호출합니다.
    
    with st.chat_message("assistant"): #봇 채팅 메시지 표시
        st.markdown(chat_response) #봇의 최신 응답 표시
    
    st.session_state.chat_history.append({"role":"assistant", "text":chat_response}) #봇의 최신 메시지를 채팅 기록에 추가합니다.
