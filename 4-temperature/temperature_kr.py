import sys
from langchain_aws import ChatBedrock # pip install -U langchain-aws

def get_text_response(input_content, temperature): #text-to-text 클라이언트 함수

    llm = ChatBedrock( #BedrockChat llm 클라이언트 생성
        model_id="anthropic.claude-3-sonnet-20240229-v1:0", # Claude 3 Sonnet 모델 선택
        model_kwargs={
            "max_tokens": 512,
            "temperature": temperature
        }
    )
    
    return llm.invoke(input_content).content #프롬프트에 응답을 반환

for i in range(1):
    response = get_text_response(sys.argv[1], float(sys.argv[2]))
    print(response)
