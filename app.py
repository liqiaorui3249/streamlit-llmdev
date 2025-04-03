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
