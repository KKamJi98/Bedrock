import json
import boto3 # pip install -U boto3

session = boto3.Session()
bedrock = session.client(service_name='bedrock-runtime') #Bedrock client 생성

bedrock_model_id = "anthropic.claude-3-sonnet-20240229-v1:0" #파운데이션 모델 설정

prompt = "Hybrid 클라우드 구성에 가장 중요한 요소는 뭐야?" #모델에 보낼 프롬프트 설정

body = json.dumps({
    "anthropic_version": "bedrock-2023-05-31",
    "max_tokens": 1024, 
    "temperature": 0,
    "messages": [
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": prompt 
                        }
                    ]
                }
            ],
}) #요청 payload 설정

response = bedrock.invoke_model(body=body, modelId=bedrock_model_id) #payload를 Bedrock으로 전송

response_body = json.loads(response.get('body').read()) # response 읽기
results = response_body.get("content")[0].get("text")

print(results)