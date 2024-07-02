from langchain_aws import ChatBedrock
# pip install -U langchain-aws

def get_text_response(input_content): #text-to-text 클라이언트 함수

    llm = ChatBedrock( #ChatBedrock llm 클라이언트 생성
        model_id="anthropic.claude-3-sonnet-20240229-v1:0", # Claude 3 Sonnet 모델 선택
        model_kwargs={
            "max_tokens": 1024,
            "temperature": 0
        }
    )
    
    response = llm.invoke(input_content) #프롬프트에 응답을 반환
    return(response.content)