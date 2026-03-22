# Langchain---260322
Langchain 챗봇만들기 > 웹 Streamlit 으로 기술지원 상담봇으로 서비스 하기

LangChain ?
LangChain은 **대규모 언어모델(LLM)** 을 더 쉽게 활용할 수 있도록 도와주는 **프레임워크**입니다.  

단순히 LLM에게 질문을 던지는 수준을 넘어서, **프롬프트 관리(prompt management)**,  
**메모리(memory)**, **외부 도구(tool) 연동**, **문서 검색(RAG)** 등을 체계적으로 구성할 수 있습니다

예를 들어, 우리가 ChatGPT 같은 LLM을 사용할 때  
단순히 모델 하나만으로 뛰어난 답변이 만들어지는 것은 아닙니다.  

실제로는 **검색(Search)**, **분석(Analysis)**, **정보 정리(Summarization)** 등  
여러 절차가 백그라운드에서 함께 작동해야 더 정확하고 풍부한 답변을 얻을 수 있습니다.  

LangChain은 이러한 여러 단계를 **하나의 체계적인 구조로 묶어주는 프레임워크**입니다.  
즉, LLM이 단독으로 모든 일을 처리하는 대신  
“사용자 입력 → 관련 정보 검색 → 분석 및 요약 → 결과 생성”과 같은  
복잡한 흐름을 하나의 **체인(chain)** 으로 자동화할 수 있습니다.  

<img src="image/chatgpt.jpg" width="600">

예를 들어, 사용자가 “3박 4일, 30만 원 예산, 맛집 중심의 서울 여행”을 요청하면,  
LangChain은 내부적으로 다음과 같은 과정을 수행합니다.  

> 입력 분석 → 예산과 일정 파악 → 추천 장소 검색 → 일정표 생성 → 자연스러운 문장으로 요약  

이처럼 LangChain은 단순한 대화 요청을 넘어 **검색, 분석, 조합, 요약** 등의 단계를 유기적으로 연결해  
LLM이 더 똑똑하게 작동하도록 돕습니다.  

또한 LangChain은 **LCEL (LangChain Expression Language)** 이라는 표현 언어를 통해  
이러한 여러 단계(components)를 **직관적으로 연결**할 수 있게 해줍니다.  
즉, “LLM → 요약기 → 출력 포맷터”처럼 **함수형 파이프라인**을 선언적으로 작성할 수 있어  
확장성과 유지보수성이 뛰어납니다.

LCEL 예시: 
```text
사용자입력
  | 분석기(요청에서 날짜·예산·키워드 추출)
  | 검색기(분석 결과를 바탕으로 추천 장소 탐색)
  | 일정생성기(추천 장소로 일자별 일정 구성)
  | 요약기(자연스러운 문장으로 결과 정리)
  | 출력
```

이처럼 LCEL은 각 단계를 함수처럼 “연결(pipe)”하여 데이터가 흘러가는 경로를 선언적으로 표현합니다.  
복잡한 제어문 없이 “입력 → 처리 → 출력” 구조를 직관적으로 구성할 수 있어,
체인 전체의 논리 흐름을 한눈에 파악할 수 있습니다.


# LangChain으로 만드는 웹 기반 챗봇 실습  

##  1. 과정 소개 및 개요
- **학습 목표**
  - AI 챗봇의 기본 개념과 발전 과정을 이해한다.
  - 규칙 기반 챗봇과 LLM 기반 챗봇을 비교할 수 있다.
  - LangChain, Streamlit, FAISS 등 주요 기술의 역할과 장점을 이해한다.
  - LCEL을 사용하여 확장성 있는 체인을 직접 설계할 수 있다.
  - **웹 기반으로 자신이 커스텀한 챗봇을 배포할 수 있는 역량을 갖춘다.**

- **핵심 키워드**
  - LLM Chatbot, LangChain, LCEL, Prompt, Streamlit, FAISS, RAG
 
  - 
시스템 구조
<img width="1410" height="1866" alt="image" src="https://github.com/user-attachments/assets/eab99ac2-fec7-465f-bd7f-f643f0c8c0a9" />


결과물
<img width="1757" height="796" alt="image" src="https://github.com/user-attachments/assets/23ed3b2b-10dd-4983-9c65-c8eee51a3355" />

