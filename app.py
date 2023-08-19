import pandas as pd
import openpyxl
import plotly.express as px
import streamlit as st
import plotly.graph_objects as go

# Set page configuration
st.set_page_config(
    page_title="Bouncing Ball tracker",
    page_icon="🎱",
    layout="wide"
)

# Read data from CSV
df = pd.read_csv(
    filepath_or_buffer='ballpositions.csv',
    usecols=["X", "Y", "Gravity", "yv", "xv"],
    nrows=1000
)

# Extract columns from DataFrame
x_column = df["X"]
y_column = df["Y"]
gravity = df["Gravity"]
yv = df["yv"]
xv = df["xv"]

# Display title and subheaders
st.title("🎱 Bouncing Ball 🎱")
st.markdown("##")
st.markdown("##")

# Create left and right columns for layout
left_column, right_column = st.columns([3, 7])

with left_column:
    # Display ball path details
    st.subheader(f"Ball path with:")
    st.subheader(f"Gravity: :blue[{gravity[0]}]")
    st.subheader(f"X velocity: :blue[{xv[0]}]")
    st.subheader(f"Y velocity: :blue[{yv[0]}]")
    st.subheader("______________________________")
    st.subheader(f"Highest point: :blue[({max(x_column)} , {max(y_column)})]")

# Create graph of ball path
graph = go.Scatter(x=x_column, y=y_column, mode='lines', name="<b>Ball path</b>")
x_column = x_column.tolist()
y_column = y_column.tolist()
fig = go.Figure()
fig.add_trace(graph)
fig.add_trace(go.Scatter(x=[x_column[0]], y=[y_column[0]], mode='markers+text', marker=dict(size=25, color='green'), name='Starting Point'))
fig.add_trace(go.Scatter(x=[x_column[-1]], y=[y_column[-1]], mode='markers', marker=dict(size=25, color='red'), name='End Point'))

# Configure layout of the graph
fig.update_layout(width=1000, height=600, margin=dict(t=0, l=0, r=100, b=0))

with right_column:
    # Display the graph
    st.plotly_chart(fig)

contact_form = """
<form action="https://formsubmit.co/awhismail@gmail.com" method="POST">
     <input type="text" name="name" required>
     <input type="email" name="email" required>
     <button type="submit">Send</button>
</form>
"""
st.markdown(contact_form, unsafe_allow_html=True)
