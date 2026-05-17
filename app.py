import streamlit as st
from data_loader import load_csv, get_summary
from agent import ask_agent
from visualizer import plot_bar, plot_line, plot_pie, plot_scatter, plot_histogram

st.set_page_config(page_title="StatBot Pro", page_icon="📊")


st.title("📊 StatBot Pro — AI CSV Analyst")

if "history" not in st.session_state:
    st.session_state.history = []
if "chart_history" not in st.session_state:
    st.session_state.chart_history = []
if "input_key" not in st.session_state:
    st.session_state.input_key = 0

uploaded_file = st.file_uploader("Upload CSV or Excel file",
                  type=["csv", "xlsx"])

if uploaded_file:
    df = load_csv(uploaded_file)
    st.success("✅ File Loaded Successfully!")
    st.dataframe(df)

    summary = get_summary(df)

    st.markdown("### 💬 Ask StatBot Anything")
    question = st.text_input("Type your question here...",
                 key=f"q_{st.session_state.input_key}")
    ask_button = st.button("🔍 Ask StatBot")

    if ask_button and question:
        with st.spinner("StatBot is thinking..."):
            answer = ask_agent(question, summary)

        st.session_state.history.append({
            "q": question,
            "a": answer
        })
        st.session_state.input_key += 1
        st.rerun()

    if st.session_state.history:
        st.markdown("### 🕓 Chat History")
        for chat in reversed(st.session_state.history):
            st.markdown(f"**🧑 You:** {chat['q']}")
            st.markdown(f"**🤖 StatBot:** {chat['a']}")
            st.download_button(
                label="📥 Download Answer",
                data=chat['a'],
                file_name="statbot_answer.txt",
                key=f"dl_{chat['q']}"
            )
            st.markdown("---")

    st.markdown("### 📈 Visualize Your Data")
    cols = list(df.columns)
    num_cols = list(df.select_dtypes(include='number').columns)

    chart_type = st.radio("Chart Type", [
        "Bar Chart",
        "Line Chart",
        "Pie Chart",
        "Scatter Plot",
        "Histogram"
    ])

    if chart_type in ["Bar Chart", "Line Chart", "Scatter Plot"]:
        x_col = st.selectbox("Select X-axis column", cols)
        y_col = st.selectbox("Select Y-axis column", num_cols)
    elif chart_type == "Pie Chart":
        x_col = st.selectbox("Select Category column", cols)
        y_col = None
    elif chart_type == "Histogram":
        x_col = st.selectbox("Select column", num_cols)
        y_col = None

    if st.button("Generate Chart"):
        st.session_state.chart_history.append({
            "x": x_col,
            "y": y_col,
            "type": chart_type
        })
        st.rerun()

    if st.session_state.chart_history:
        st.markdown("### 🕓 Chart History")
        for i, chart in enumerate(reversed(st.session_state.chart_history)):
            st.markdown(f"**📊 {chart['type']}** — `{chart['x']}`")
            try:
                if chart["type"] == "Bar Chart":
                    fig = plot_bar(df, chart["x"], chart["y"])
                elif chart["type"] == "Line Chart":
                    fig = plot_line(df, chart["x"], chart["y"])
                elif chart["type"] == "Pie Chart":
                    fig = plot_pie(df, chart["x"])
                elif chart["type"] == "Scatter Plot":
                    fig = plot_scatter(df, chart["x"], chart["y"])
                elif chart["type"] == "Histogram":
                    fig = plot_histogram(df, chart["x"])
                st.pyplot(fig)
            except:
                st.warning("⚠️ Could not generate this chart.")
            st.markdown("---")