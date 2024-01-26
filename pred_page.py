import streamlit as st
import pickle
import pandas as pd

def load_data():
    with open("iris.pkl", "rb") as file:
        data = pickle.load(file)
    return data

data = load_data()
model = data["model"]


def show_page():
    st.title(":blue[Iris Dataset Insights: Decision Tree Classification]")
    st.write("Select the values for prediction")
    sepal_length = st.slider("Sepal Length", 0.0, 10.0, 5.0)
    sepal_width = st.slider("Sepal Width", 0.0, 5.0, 3.0)
    petal_length = st.slider("Petal Length", 0.0, 10.0, 4.5)
    petal_width = st.slider("Petal Width", 0.0, 5.0, 3.0)
    btn_act = st.button("Predict")

    if btn_act:
        predictors = pd.DataFrame({"sepal_length": [sepal_length], "sepal_width": [sepal_width],  
                      "petal_length": [petal_length], "petal_width": [petal_width]})
        
        
        # st.dataframe(predictors)

        result = model.predict(predictors)

        def result_condition():
            if result == 0:
                return ":red[Setosa]"
            elif result == 1:
                return ":blue[Versicolor]"
            else:
                return ":green[Virginica]"

        st.write(f"The flower is likely to be of  {result_condition()} species" )