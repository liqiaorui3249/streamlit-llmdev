import datetime
import streamlit as st
st.title("hello llm dev")
st.divider()
st.write("I am fine")
st.divider()
st.info("Hello lqr")
st.divider()
st.header("Hello everyone")
st.divider()
st.markdown("Hello **world**!")
st.divider()
st.subheader("This is a subheader")
st.badge("New")
st.caption("This is written small caption text")
st.divider()
st.code("a = 1234")
st.latex("\int a x^2 \,dx")
st.divider()
st.html("<p>Foo bar.</p>")
st.button("Reset", type="primary")
st.divider()
if st.button("Say hello"):
    st.write("Why hello there")
else:
    st.write("Goodbye")
st.divider()
st.write("图片控制")
enable = st.checkbox("Enable camera")
picture = st.camera_input("Take a picture", disabled=not enable)

if picture:
    st.image(picture)


st.html("<p><a href="streamlit.py" target="_blank">Streamlit 是一个开源的python库</a></p>")



These are featured components create

st.divider()
st.write("时间控件")

today = datetime.datetime.now()
next_year = today.year + 1
jan_1 = datetime.date(next_year, 1, 1)
dec_31 = datetime.date(next_year, 12, 31)

d = st.date_input(
    "Select your vacation for next year",
    (jan_1, datetime.date(next_year, 1, 7)),
    jan_1,
    dec_31,
    format="MM.DD.YYYY",
)
d
st.divider()
st.write("输入框")
name=st.text_input("First name")
st.write(f"Hello{name}")

st.divider()
st.write("选择框")
choice=st.number_input("pick a number,0,10")

st.divider()
st.write("多行框")
text=st.text_area("text to translate")

st.divider()
st.write("上传")
data=st.file_uploader("Upload a csv")


st.sidebar.write("This lives in the sidebar")
st.sidebar.divider()
st.sidebar.button("click me!")

st.divider()
st.write("扩展器")
with st.expander("open to see more"):
     st.write("this is more content")
     st.write("this is another content")
     st.image("https://static.streamlit.io/examples/dice.jpg")

st.divider()
st.write("标签页")
tab1,tab2=st.tabs(["tab1","tab2"])
tab1.write("this is tab1")
tab2.write("this is tab2")

st.divider()
st.write("聊天输入")
myname=st.text_input("First_name")
if name:
    st.write(f"Hello {myname}")
prompt=st.chat_input("say something")
if prompt:
    st.write(f"the user has sent:{prompt}")

st.divider()
st.write("聊天消息")
import numpy as np
with st.chat_message("user"):
     st.write("hello")
     st.line_chart(np.random.randn(30,3))
with st.chat_message("ai"):
     st.write("I am an AI assistant")
