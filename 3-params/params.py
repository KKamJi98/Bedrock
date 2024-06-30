'''
param's

# Temperature 
- 생성 모델의 출력의 무작위성 제어. 모델이 다음 단어를 선택할 때의 확률 분포의 평탄도 조정 
- 값이 0에 가까울수록 더 결정론적으로 작동하며, 가장 높은 확률을 가진 단어 선택

# Token
- 텍스트를 구성하는 기본 단위로, 단어 또는 부분 단어로 간주될 수 있음
- 입력 토큰: 모델에 제공되는 텍스트 입력을 토큰 단위로 나누어 처리
    ex) "Hello, world!" => ["Hello", ",", "world"]
- 출력 토큰 제한: 출력 텍스트의 길이 제어(모델이 너무 길거나 짧은 텍스트를 생성하지 않도록 하는 데 유용)

# Stop Sequences
- 모델이 텍스트 생성을 중지해야 하는 특정 문자열 또는 토큰 시퀀스를 정의
- 해당 매개변수를 사용하면 출력 텍스트의 특정 지점에서 생성을 중지할 수 있음 (특정 패턴이나 문구 이후에 불필요한 텍스트 생성 방지)
'''

import sys
from langchain_aws import BedrockLLM


def get_inference_parameters(model):  # 모델의 공급자에 따라 기본 매개변수 집합 반환
    bedrock_model_provider = model.split(
        '.')[0]  # 모델 ID의 첫 번째 부분에서 모델 공급자 가져오기

    if (bedrock_model_provider == 'anthropic'):  # Anthropic 모델
        return {  # anthropic
            "max_tokens_to_sample": 512,
            "temperature": 0
        }

    elif (bedrock_model_provider == 'ai21'):  # AI21 모델
        return {  # AI21
            "maxTokens": 512,
            "temperature": 0,
            "topP": 0.5,
            "stopSequences": [],
            "countPenalty": {"scale": 0},
            "presencePenalty": {"scale": 0},
            "frequencyPenalty": {"scale": 0}
        }

    elif (bedrock_model_provider == 'cohere'):  # COHERE 모델
        return {
            "max_tokens": 512,
            "temperature": 0,
            "p": 0.01,
            "k": 0,
            "stop_sequences": [],
            "return_likelihoods": "NONE"
        }

    else:  # Amazon
        # LangChain Bedrock 구현의 경우, 이러한 매개변수는 LangChain이 생성하는 textGenerationConfig 구성항목에 추가됩니다.
        return {
            "maxTokenCount": 512,
            "stopSequences": [],
            "temperature": 0,
            "topP": 0.9
        }

def get_text_response(model, input_content): #text-to-text 클라이언트 함수
    
    model_kwargs = get_inference_parameters(model) #선택한 모델에 따른 기본 매개변수 할당
    
    llm = BedrockLLM( #Bedrock llm 클라이언트 생성
        model_id=model,
        model_kwargs = model_kwargs
    )
    
    return llm.invoke(input_content) #프롬프트에 대한 응답 반환

response = get_text_response(sys.argv[1], sys.argv[2])

print(response)