from langchain_community.embeddings import BedrockEmbeddings
from langchain.indexes import VectorstoreIndexCreator
from langchain_community.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.chat_models import BedrockChat

def get_llm():
    
    model_kwargs = { #Anthropic Cloude v3
        "max_tokens": 1024, 
        "temperature": 0
    }
    
    llm = BedrockChat(
        model_id="anthropic.claude-3-sonnet-20240229-v1:0", #파운데이션 모델 설정
        model_kwargs=model_kwargs) #Claude에 대한 속성
    
    return llm

def get_index(): #애플리케이션에서 사용할 인메모리 벡터 저장소를 생성하고 반환합니다
    
    embeddings = BedrockEmbeddings() #Titan Embeddings 클라이언트 생성
    
    pdf_path = "2022-Shareholder-Letter-ko.pdf" #로컬 PDF 파일 (2022년 주주 서한)

    loader = PyPDFLoader(file_path=pdf_path) #pdf 파일을 로드합니다
    
    text_splitter = RecursiveCharacterTextSplitter( #텍스트 분할기를 만듭니다
        chunk_size=1000, #구분 기호를 사용하여 1000자 청크로 분할
        chunk_overlap=100 #이전 청크와 겹칠 수 있는 문자 수
    )
    
    index_creator = VectorstoreIndexCreator( #벡터 스토어 팩토리 생성
        vectorstore_cls=FAISS, #데모 목적으로 인메모리 벡터 스토어 사용
        embedding=embeddings, #Titan Embeddings 사용
        text_splitter=text_splitter, #재귀적 텍스트 분할기 사용
    )
    
    index_from_loader = index_creator.from_loaders([loader]) #로드된 PDF에서 벡터 스토어 인덱스 생성
    
    return index_from_loader #클라이언트 앱에서 캐시할 인덱스 반환

def get_rag_response(index, question): #rag client 함수
    
    llm = get_llm()
    
    response_text = index.query(question=question, llm=llm) #인메모리 인덱스에 대해 검색하고 결과를 프롬프트에 채워서 llm으로 전송
    
    return response_text
