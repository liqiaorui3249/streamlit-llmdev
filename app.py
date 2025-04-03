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
st.divider()
st.write("侧边栏")
st.sidebar.button("click me!")

