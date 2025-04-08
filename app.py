import streamlit as st

#聊天机器人页面，可视化展示内容和大模型的聊天记录

#构建和大模型的聊天chain

#页面的左半部分展示聊天内容，右半部分展示聊天记录

from pydantic import BaseModel

#通义大模型
from langchain_community.chat_models.tongyi import ChatTongyi 
#提示词模型
from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder
#输出的解析器
from langchain_core.output_parsers import StrOutputParser
#定义大模型
from langchain.schema import AIMessage,HumanMessage

model=ChatTongyi(model_name='qwen-max',streaming=True)
mermory_key='history'
prompt=ChatPromptTemplate.from_messages(
	[
		MessagesPlaceholder(variable_name=mermory_key),
		('human','{input}')
	]
)

class Message(BaseModel):	
	content:str
	role:str

if "messages" not in st.session_state:
	st.session_state.messages = []
	
def to_message_place_holder(messages):
	return [
		Message(content=message['content']) if message['role']=="ai" else HumanMessage(content=message['content']) 
		for message in messages
	]
	
chain = {
	'input':lambda x: x['input'],
	'history':lambda x:to_message_place_holder(x['messages'])
} | prompt | model | StrOutputParser()

#构建页面
st.columns([0.7,0.3])
left,right = st.columns([0.7,0.3])

with left:
    #聊天内容展示
	container=st.container()
	with container:
		for message in st.session_state.messages:
			with st.chat_message(message['role']):
			     st.write(message['content'])
	
	#接收用户的输入，存放在sessin_state中
	prompt = st.chat_input("您好，请问有什么可以帮助到您的吗？")
	if prompt:
		st.session_state.messages.append(Message(content=prompt,role="human").model_dump())
		with container:
			with st.chat_message("human"):
			     st.write(prompt)
	#获取大模型的返回，并展示
	with container:
		response = st.write_stream(chain.stream({"input":prompt,'messages':st.session_state.messages}))
		st.session_state.messages.append(Message(content=response,role="ai").model_dump())
		
	

with right:
	#聊天记录	
	st.json(st.session_state.messages)
