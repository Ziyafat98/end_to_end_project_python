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


import streamlit as st
import pandas as pd
from joblib import load
import calendar

# Model yükləmə
@st.cache_resource(show_spinner="Loading model...")
def load_model():
    model = load("model_new.saleslib")
    return model

def make_prediction(model):
    year = st.session_state["year"]
    month = st.session_state["month"]
    temp = st.session_state["temp"]
    store = st.session_state["store"]
    days_option = st.session_state["days_option"]

    if days_option == "Specific day":
        day = st.session_state["day"]
        X_pred = pd.DataFrame({
            "year": [year],
            "month_num": [month],
            "day_num": [day],
            "temperature_2m_mean": [temp],
            "store_id": [store]
        })
        pred = model.predict(X_pred)
        st.session_state["pred"] = round(float(pred[0]), 2)
    else:  # Whole month
        days_in_month = calendar.monthrange(year, month)[1]
        X_pred = pd.DataFrame({
            "year": [year]*days_in_month,
            "month_num": [month]*days_in_month,
            "day_num": list(range(1, days_in_month+1)),
            "temperature_2m_mean": [temp]*days_in_month,
            "store_id": [store]*days_in_month
        })
        preds = model.predict(X_pred)
        total_sales = preds.sum()
        st.session_state["pred"] = round(float(total_sales), 2)

if __name__ == "__main__":
    st.title("Store Sales Prediction")

    model = load_model()

    if "pred" not in st.session_state:
        st.session_state["pred"] = None

    with st.form("form"):
        col1, col2, col3 = st.columns(3)

        # Sol sütun: Year + Month
        with col1:
            st.number_input("Year", min_value=2023, max_value=2030, value=2024, key="year")
            st.number_input("Month", min_value=1, max_value=12, value=1, key="month")

        # Orta sütun: Day + Days Option + Temperature
        with col2:
            st.selectbox(
                "Days Option",
                options=["Specific day", "Whole month"],
                key="days_option"
            )
            if st.session_state["days_option"] == "Specific day":
                st.number_input("Select Day", min_value=1, max_value=31, value=1, key="day")
            st.number_input("Temperature (°C)", value=20.0, key="temp")

        # Sağ sütun: Store
        with col3:
            st.selectbox(
                "Store ID",
                options=[3, 5, 8],
                key="store"
            )

        st.form_submit_button(
            "Calculate",
            type="primary",
            on_click=make_prediction,
            kwargs=dict(model=model)
        )

    # Nəticəni göstər
    if st.session_state["pred"] is not None:
        if st.session_state["days_option"] == "Specific day":
            st.subheader(f"Predicted Sales for {st.session_state['month']}/{st.session_state['day']}: {st.session_state['pred']}")
        else:
            st.subheader(f"Total Predicted Sales for Month {st.session_state['month']}: {st.session_state['pred']}")
