import streamlit as st
st.set_page_config(layout="wide")
from streamlit_option_menu import option_menu


# Custom CSS for styling
st.markdown(
"""
<style>
.header {
background-color: #a70529;
color: white;
padding: 10px;
display: flex;
justify-content: space-between;
align-items: center;
border-radius: 10px;
}
.header img {
max-height: 60px;
}
.header h4 {
margin: 0;
padding: 0;
color: white;
}
.header .right-section {
display: flex;
align-items: center;
}
.header .right-section h4 {
margin-left: 10px;
font-size: 24px;
}
.disclaimer {
background-color: #FFFFE0;
color: black;
padding: 10px;
border-radius: 10px;
margin-top: 10px;
}
.disclaimer strong{
color:red;
}
.general {
background-color:lavender;
}
#opt{
width:30%;
hight:20%;
padding:10px;
margin:15px;

}
.row {
display: flex;
background-color:lavender;
}

.column {
flex: 50%;
border:solid;

}
</style>
""",
unsafe_allow_html=True
)

# Custom HTML for the header
st.markdown(
"""
<div class="header">
<img src="https://results.eci.gov.in/PcResultGenJune2024/img/eci-logo.png" alt="ECI Logo">
<h4>Home</h4>
<div class="right-section">
<img src="https://results.eci.gov.in/PcResultGenJune2024/img/deshgarv-logo.png" alt="Desh Ka Garv Logo">
</div>
</div>
""",
unsafe_allow_html=True
)


st.markdown(
"""
<div class="disclaimer">
<strong>Disclaimer:</strong> ECI is displaying the information as being filled in the system by the Returning Officers from their respective Counting Centres. The final data for each AC/PC will be shared in Form-20.
</div>
""",
unsafe_allow_html=True
)
def call():
a = option_menu(
menu_title='',
options = ["Parliamentary Constituency General","Assembly Constituency General","Assembly Constituency Bye"],
orientation="horizontal",
styles={
"nav-link": {"--hover-color": "#dc3545",       
"font-size":"15px",
"color":"#dc3545",
"background-color": "#f0f0f0",
"border":"solid"
}   ,
"nav-link-selected": {"background-color": "#dc3545",
"color": "white"},

}
)
call()

st.markdown("""

<div class="general">
<h3> General Election to Parliamentary Constituencies: Trends & Results June-2024</h3>
<select name="cars" id="opt">
<option value="volvo">Select State Wise</option>
<option value="saab">Saab</option>
<option value="mercedes">Mercedes</option>
<option value="audi">Audi</option>
</select>
</div>
""",
unsafe_allow_html=True
)
st.write("")

st.markdown("""

<div class="row">
<div class="column">
<h3>Party Wise Vote Share</h3>
</div>
<div class="column">
<h3>Party Wise Results Status</h3>
</div>
</div>

""",
unsafe_allow_html=True)

import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv('file.csv')
x = df['Won']
y = df['Party']
# plt.figure(figsize=(8, 8)) 
# plt.pie(x,labels=y, autopct='%1.1f%%', startangle=140)
# plt.legend(title="Legend", loc="best")

# Create a pie chart
fig, ax = plt.subplots(figsize=(8, 8)) 
ax.pie(x, labels=y, autopct='%1.1f%%', startangle=140)

# Place the legend in the bottom right corner
ax.legend(title="Legend", loc="right")

# Display the chart in Streamlit
st.pyplot(fig)