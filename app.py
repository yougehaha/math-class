import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt

st.set_page_config(page_title="计数原理教学助手", layout="wide")

st.title("🍎 计数原理交互演示器")
st.sidebar.header("教学设置")

# 模式选择
mode = st.sidebar.radio("选择计数原理：", ["乘法原理 (分步)", "加法原理 (分类)"])

if mode == "乘法原理 (分步)":
    m = st.sidebar.slider("第一步选项数", 1, 4, 2)
    n = st.sidebar.slider("第二步选项数", 1, 4, 3)
    st.subheader("乘法原理：分步计数")
    st.latex(f"N = {m} \\times {n} = {m*n}")
    
    G = nx.Graph()
    G.add_node("开始")
    for i in range(m):
        node_a = f"A{i+1}"
        G.add_edge("开始", node_a)
        for j in range(n):
            G.add_edge(node_a, f"B{i+1}_{j+1}")
else:
    m = st.sidebar.slider("第一类选项数", 1, 6, 3)
    n = st.sidebar.slider("第二类选项数", 1, 6, 2)
    st.subheader("加法原理：分类计数")
    st.latex(f"N = {m} + {n} = {m+n}")
    
    G = nx.Graph()
    G.add_node("分类点")
    for i in range(m): G.add_edge("分类点", f"A{i+1}")
    for j in range(n): G.add_edge("分类点", f"B{j+1}")

# 绘图
fig, ax = plt.subplots(figsize=(8, 5))
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color='orange' if mode=="加法原理 (分类)" else 'skyblue', 
        node_size=1000, font_size=10, ax=ax)
st.pyplot(fig)

st.success("AI 提示：分步相乘，分类相加。当分支结构复杂时，计算机会自动为您生成决策树。")
