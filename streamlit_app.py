import streamlit as st
# Main page title
st.title("My app")
st.header("My Header")

st.markdown("## Header 1 ")
# # Display code snippet
st.code("""import pandas as pd 
         pd.read_txt(my_text_file)""")

# # Another plain text
st.text("Some Text")

# Render LaTeX formula
st.latex(r"x = 210 * 10")

# Generic write output
st.write("My text")

# Slider to pick age
age = st.slider("Select your age", 0, 100, 25)

# Echo chosen age
st.write(f"You picked: {age}")

# # Open sidebar context


with st.sidebar:
    # Sidebar label
    st.write(" **Sidebar** — extra space")
    # Simple sidebar button
    st.button("Click me!")

# Main‑area button with balloons
if st.button("Celebrate"):
    st.balloons()


import streamlit as st
import pandas as pd 


df=pd.read_excel('/workspaces/end_to_end_project_python/datasets/Coffee Shop Sales.xlsx')
# As  data frame  you can order  ects cick on the column in dataframe
st.dataframe(df.head())

# st.write(df) ( This is works  also )


# # Do not use t this if you need it . beacuse it looaded allo fthe data to memeroty 
# st.table(df)

st.metric(label="Survive rate", value=150 , delta= 20 , delta_color="normal")
st.metric(label="Death rate in titainica", value=100 , delta= - 20 , delta_color="normal" ) # user inverse if teh red colour is positive)


## Visualtion 
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
    'Product A': [100, 120, 150, 170, 160, 180],
    'Product B': [90, 110, 130, 160, 155, 170]
}
df = pd.DataFrame(data)

st.line_chart(df, x="Month", y=["Product A", "Product B"], y_label="Product names", x_label="Months")


### Second modethid

# Set Month as index (optional, for better x-axis labeling)
df_visual=df.set_index('Month')

st.title(" Monthly Sales Line Chart")

# Plot using matplotlib
st.subheader("Sales Over Time")
fig, ax = plt.subplots()
df_visual.plot(kind='line', ax=ax, marker='o')
ax.set_ylabel("Units Sold")
ax.set_xlabel("Month")
ax.set_title("Monthly Sales of Product A and B")
st.pyplot(fig)



## Streamlit_area chart

st.area_chart(df, x="Month", y="Product A")


## Streamlit bar chart 

st.bar_chart(df, x="Month", y=["Product A", "Product B"])













