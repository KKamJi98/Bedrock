from langchain_aws import ChatBedrock # pip install -U langchain-aws

llm = ChatBedrock( #BedrockChat llm 클라이언트 생성
    model_id="anthropic.claude-3-sonnet-20240229-v1:0", # Claude 3 Sonnet 모델 선택
    model_kwargs={
        "max_tokens": 512,
        "temperature": 0
    }
)

prompt = "로컬에서 OpenStack을 사용할 때 고려해야할 문제에 대해 설명해주세요."

response_test = llm.invoke(prompt)

print(response_test.content)