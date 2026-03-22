#import streamlit as st

#st.title("Hello Streamlit 👋")
#st.write("Streamlit 앱이 정상적으로 실행되고 있습니다. TEST")

##st.number_input() 
#age = st.number_input("나이", 0, 120)



import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_classic.memory import ConversationSummaryMemory
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

from dotenv import load_dotenv

load_dotenv()


# ---------------------------
# 1. 기본 설정
# ---------------------------
st.set_page_config(page_title="제조 컨설턴트", layout="wide")
st.title("🔧 제조분야 전문 기술 컨설턴트")

# ---------------------------
# 2. 세션 초기화 (중요)
# ---------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

if "memory" not in st.session_state:
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.7)

    st.session_state.llm = llm
    st.session_state.memory = ConversationSummaryMemory(
        llm=llm,
        return_messages=True
    )

# ---------------------------
# 3. 프롬프트
# ---------------------------
prompt = ChatPromptTemplate.from_messages([
    ("system",
     "너는 제조분야 전문 기술 컨설턴트야. "
     "제품설계, 3D 설계, 설계자동화 중심으로 답변해라. "
     "반드시 '문의주셔서 감사합니다. 해당문의에 답변을 드립니다.' 문구를 포함해라. "
     "www.j-cns.com 참고를 안내해라."
    ),
    MessagesPlaceholder(variable_name="history"),
    ("human", "{input}")
])

chain = prompt | st.session_state.llm

# ---------------------------
# 4. 기존 대화 출력
# ---------------------------
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# ---------------------------
# 5. 입력창 (핵심!)
# ---------------------------
user_input = st.chat_input("질문을 입력하세요")

# ⚠️ 이 부분이 없으면 제목만 뜸
if user_input is not None and user_input.strip() != "":

    # 사용자 메시지
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    with st.chat_message("user"):
        st.write(user_input)

    # 메모리 불러오기
    history = st.session_state.memory.load_memory_variables({})["history"]

    # LLM 실행
    result = chain.invoke({
        "history": history,
        "input": user_input
    })

    # AI 응답 저장
    st.session_state.messages.append({
        "role": "assistant",
        "content": result.content
    })

    with st.chat_message("assistant"):
        st.write(result.content)

    # 메모리 저장
    st.session_state.memory.save_context(
        {"input": user_input},
        {"output": result.content}
    )

# ---------------------------
# 6. 디버그
# ---------------------------
with st.expander("메모리 확인"):
    st.write(st.session_state.memory.buffer)