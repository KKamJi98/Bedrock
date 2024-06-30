# LangChain 라이브러리를 사용하여 Amazon Bedrock을 호출하고 벡터를 비교하는 데 필요한 계산을 수행
#from langchain.embeddings import BedrockEmbeddings
from langchain_community.embeddings import BedrockEmbeddings
from numpy import dot
from numpy.linalg import norm

# Bedrock Embeddings LangChain 클라이언트 생성
belc = BedrockEmbeddings()


class EmbedItem:
    def __init__(self, text):
        self.text = text
        self.embedding = belc.embed_query(text)


class ComparisonResult:
    def __init__(self, text, similarity):
        self.text = text
        self.similarity = similarity


# 코사인 유사도를 확인: https://en.wikipedia.org/wiki/Cosine_similarity
def calculate_similarity(a, b):
    return dot(a, b) / (norm(a) * norm(b))


# 비교할 임베딩 목록을 작성
items = []

with open("items.txt", "r") as f:
    text_items = f.read().splitlines()

for text in text_items:
    items.append(EmbedItem(text))

'''
임베딩을 비교 후 목록을 표시 => 다양한 텍스트가 얼마나 유사한지 또는 다른지 확인

유사도 값이 1이면 완전히 동일함을 의미
유사도가 작을수록 임베딩이 덜 유사하다는 의미
'''
for e1 in items:
    print(f"Closest matches for '{e1.text}'")
    print("----------------")
    cosine_comparisons = []

    for e2 in items:
        similarity_score = calculate_similarity(e1.embedding, e2.embedding)

        # 비교 내용을 목록에 저장
        cosine_comparisons.append(ComparisonResult(e2.text, similarity_score))

    # 가장 가까운 일치 항목을 먼저 나열
    cosine_comparisons.sort(key=lambda x: x.similarity, reverse=True)

    for c in cosine_comparisons:
        print("%.6f" % c.similarity, "\t", c.text)

    print()
