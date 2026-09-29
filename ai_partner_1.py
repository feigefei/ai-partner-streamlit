import streamlit as st
import os
from openai import OpenAI


#设置页面配置项
st.set_page_config(
    page_title="AI智能伴侣",
    page_icon="🤖",
    layout="wide",
    #侧边栏状态
    initial_sidebar_state="expanded",

    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)
#大标题
st.title("AI智能伴侣")

#logo
st.logo(os.path.join(os.path.dirname(os.path.abspath(__file__)), "resources", "logo.png"))
#系统提示词
system_prompt = "You are a helpful assistant"
#初始化聊天信息
if 'message' not in st.session_state:
    st.session_state['message'] = []

#展示聊天信息
for message in st.session_state.message:
    st.chat_message(message["role"]).write(message["content"])
    # if message["role"] == "user":
    #     st.chat_message("user").write(message["content"])
    # else:
    #     st.chat_message("assistant").write(message["content"])
#创建与AI大模型交互的客户端对象
client = OpenAI(
    api_key=os.environ.get('DEEPSEEK_API_KEY'),
    base_url="https://api.deepseek.com")

#消息输入框
prompt = st.chat_input("请输入您要问的问题")
if prompt:    #如果字符串不为空，则为True，为空则为False
    st.chat_message("user").write(prompt)
    print("------------>调用AI大模型，提示词",prompt)
    #保存用户输入的提示词
    st.session_state.message.append({"role":"user","content":prompt})
    # 与AI大模型进行交互
    response = client.chat.completions.create(
        model="deepseek-v4-pro",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt},
        ],
        stream=False,
        reasoning_effort="high",
        extra_body={"thinking": {"type": "enabled"}}
    )

    #输出大模型返回的结果
    print("<----------大模型返回的结果:",response.choices[0].message.content)
    st.chat_message("assistant").write(response.choices[0].message.content)
    #保存大模型返回的结果
    st.session_state.message.append({"role": "assistant","content":response.choices[0].message.content})