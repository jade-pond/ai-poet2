from langchain_community.chat_models import ChatOllama
llm = ChatOllama(model="EEVE-Korean-10.8B:latest")


import streamlit as st

st.title("인공지능 제이드")
st.title("만나서 반가워요. 제이드에요. :sunglasses:")

content = st.text_input("여기에 주제를 입력해주세요:")

if st.button('시 작성 요청하기'):
    with st.spinner('제이드 생각 중...'):
        result = llm.invoke(f"{content}에 대한 시를 써줘") 
        st.write(result)


