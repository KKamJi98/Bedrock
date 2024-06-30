"""
# 스트리밍 응답

- 최종 사용자에게 콘텐츠를 즉시 반환하고 싶을 때 유용
- 전체 응답이 생성될 때까지 기다리지 않고 한 번에 몇 단어씩 출력을 표시할 수 있음
"""

import json
import boto3

session = boto3.Session()
# creates a Bedrock client
bedrock = session.client(service_name='bedrock-runtime')


def chunk_handler(chunk):
    print(chunk, end='')

# 스트리밍 API 엔드포인트를 호출하기 위해 Bedrock의 invoke_model_with_response_stream 함수를 사용
# 응답 청크가 반환되면, 반환된 JSON에서 청크의 텍스트를 추출하여 제공된 콜백 메서드에 전달


def get_streaming_response(prompt, streaming_callback):

    bedrock_model_id = "anthropic.claude-3-sonnet-20240229-v1:0"
    body = json.dumps({
        "anthropic_version": "bedrock-2023-05-31",
        "max_tokens": 2000,
        "temperature": 0,
        "system": "You are a helpful assistant.",
        "messages": [
            {
                "role": "user",
                "content": [{"type": "text", "text": prompt}]
            }
        ],
    })

    response = bedrock.invoke_model_with_response_stream(
        modelId=bedrock_model_id, body=body)  # 스트리밍 메소드를 호출합니다.

    for event in response.get('body'):
        chunk = json.loads(event['chunk']['bytes'])

        if chunk['type'] == 'content_block_delta':
            if chunk['delta']['type'] == 'text_delta':
                streaming_callback(chunk['delta']['text'])


prompt = "가장 친한 친구가 된 강아지 두 마리와 새끼 고양이 두 마리에 대한 이야기를 들려주세요."

get_streaming_response(prompt, chunk_handler)
