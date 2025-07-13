##### 기본 정보 불러오기 ####
import streamlit as st
import openai

##### 기능 구현 함수 #####
def askGpt(text, apikey):
    system_prompt = '''
    You are an expert assistant that summarizes text into **Korean language**.
    Your summaries should include the following:
    - Omit duplicate content, but increase the summary weight of duplicate content.
    - Summarize by emphasizing concepts and arguments rather than case evidence.
    - Summarize in 3 lines.
    - Use the format of a bullet point.
    '''

    client = openai.OpenAI(api_key=apikey)
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": text}
        ]
    )
    return response.choices[0].message.content

##### 메인 함수 #####
def main():
    st.set_page_config(page_title="요약 프로그램")

    if "OPENAI_API" not in st.session_state:
        st.session_state["OPENAI_API"] = ""

    # 사이드바
    with st.sidebar:
        open_apikey = st.text_input(
            label='OPENAI API 키', 
            placeholder='Enter Your API Key', 
            value='', type='password',
        )
        if open_apikey:
            st.session_state["OPENAI_API"] = open_apikey
        st.markdown('---')

    st.header("📃요약 프로그램")
    st.markdown('---')

    text = st.text_area("요약 할 글을 입력하세요")
    if st.button("요약") and text.strip():
        st.info(askGpt(text, st.session_state["OPENAI_API"]))

if __name__ == "__main__":
    main()
