import boto3  # AWS SDK 및 지원 라이브러리 가져오기
import json
import base64
from io import BytesIO

session = boto3.Session()

bedrock = session.client(service_name='bedrock-runtime')  # 베드락 클라이언트를 생성

bedrock_model_id = "stability.stable-diffusion-xl-v1"  # Stable Diffusion 모델 사용


def get_response_image_from_payload(response):  # 모델 응답 페이로드에서 이미지 바이트를 반환합니다

    payload = json.loads(response.get('body').read())  # 응답 본문을 json 객체에 로드합니다
    images = payload.get('artifacts')  # 이미지 아티팩트 추출
    image_data = base64.b64decode(images[0].get('base64'))  # 이미지 디코딩

    return BytesIO(image_data)  # 클라이언트 앱 소비를 위한 BytesIO 객체 반환


def get_image_response(prompt_content):  # text-to-text 클라이언트 함수
    
    request_body = json.dumps({"text_prompts":
                                [{"text": prompt_content}],  # 사용할 프롬프트
                                "cfg_scale": 9,  # 모델이 프롬프트와 얼마나 가깝게 일치하려고 하는지
                                "steps": 50, })  # 수행할 Diffusion steps의 수

    response = bedrock.invoke_model(
        body=request_body, modelId=bedrock_model_id)  # 베드락 엔드포인트를 호출

    # 응답 페이로드를 클라이언트가 소비할 수 있도록 BytesIO 객체로 변환
    output = get_response_image_from_payload(response)

    return output
