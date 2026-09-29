import streamlit as st

#设置页面配置项
st.set_page_config(
    page_title="Streamlit入门演示",
    page_icon="🧊",
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
st.title("🐱 布偶猫介绍")
st.header("优雅的仙女猫")
st.subheader("Ragdoll")

#段落文字
st.write( "布偶猫（Ragdoll）是一种体型较大、性格温顺的猫咪品种，"
    "因其被抱起时会像布偶一样全身放松而得名。"
    "它们拥有湛蓝的眼睛和柔软蓬松的长毛，被称为'仙女猫'。"
          "布偶猫是一种非常受欢迎的猫咪品种，因其温顺的性格和美丽的外观而受到人们的喜爱。")


#表格
student_dict = {"姓名": ["张三", "李四", "王五"], "年龄": [18, 19, 20]}
st.table(student_dict)

#普通输入框
name = st.text_input("请输入姓名：")
st.write(f"您输入的姓名为：{name}")

#密码输入框
password = st.text_input("请输入密码",type = "password")
st.write(f"您输入的密码为：{password}")

#单选按钮
gender = st.radio("请选择性别：", ("男", "女"))
st.write(f"您选择的性别为：{gender}")
