import streamlit as st
from io import StringIO
from langchain_core.messages import HumanMessage,SystemMessage
from langchain_openai import AzureChatOpenAI
st.title("Let's to code review for your python file")
st.header("Please upload your .py file")
data=st.file_uploader("Upload python file",type=".py")
if data:
    stringio=StringIO(data.getvalue().decode('utf-8'))
    fetched_data=stringio.read()
    st.write(fetched_data)
    
    
    llm = AzureChatOpenAI(
            azure_endpoint=st.secrets["AZURE_OPENAI_ENDPOINT"],       
            openai_api_key=st.secrets["AZURE_OPENAI_API_KEY"],
            openai_api_version="2024-06-01",
            deployment_name=st.secrets["AZURE_OPENAI_DEPLOYMENT"], 
            temperature=0.7
        )

    systemMessage=SystemMessage(content="You are a code review assistent.Provide detailed suggestions to improve the given python code" )
    humanMessage=HumanMessage(content=fetched_data)
    response=llm.invoke([systemMessage,humanMessage])
    st.markdown(response.content)
    
