from langchain.memory import ConversationSummaryBufferMemory
from langchain_community.chat_models import BedrockChat
from langchain.chains import ConversationChain

# Bedrock LangChain 클라이언트 생성 함수
def get_llm():

    model_kwargs = {  # anthropic
        "max_tokens": 1024,
        "temperature": 0
    }

    llm = BedrockChat(
        model_id="anthropic.claude-3-sonnet-20240229-v1:0",  # 파운데이션 모델 설정
        model_kwargs=model_kwargs)  # Claude에 대한 속성 구성

    return llm

# LangChain 메모리 객체 초기화 함수 추가
def get_memory(): #이 채팅 세션에 대한 메모리 생성
    
    # ConversationSummaryBufferMemory에는 이전 메시지를 요약하기 위한 LLM이 필요
    # 이를 통해 이어지는 대화의 '맥락'을 유지할 수 있음
    llm = get_llm()
    
    memory = ConversationSummaryBufferMemory(llm=llm, max_token_limit=1024) #이전 메시지의 요약을 유지합니다.
    
    return memory

# get_memory함수를 추가하여 Bedrock 호출
def get_chat_response(input_text, memory): #채팅 클라이언트 함수
    
    llm = get_llm()
    
    conversation_with_summary = ConversationChain( #채팅 클라이언트 생성
        llm = llm, #Bedrock LLM 사용
        memory = memory, #summarization memory 사용
        verbose = True #실행 중 체인의 내부 상태 중 일부를 출력합니다.
    )
    
    chat_response = conversation_with_summary.invoke(input_text) #사용자 메시지와 요약을 모델에 전달합니다.
    
    return chat_response['response']
