import os
import time
import pandas as pd
import streamlit as st
from ydata_profiling import ProfileReport

def print_time_taken(seconds):
    m = int(seconds // 60)
    s = int(seconds % 60)
    st.write(f"Took: {m}m{s}s" if seconds >= 60 else f"Took: {int(seconds)}s")

def load_data(uploaded_file):
    return pd.read_csv(uploaded_file, low_memory=False)

def calculate_metrics(df):
    total_rows = df.shape[0]
    total_columns = df.shape[1]
    total_missing = df.isnull().sum().sum()
    unique_count = df.nunique().sum()
    completeness_percentage = ((total_rows * total_columns - total_missing) / (total_rows * total_columns) * 100) if total_rows > 0 else 0
    uniqueness_percentage = (unique_count / (total_rows * total_columns) * 100) if total_rows > 0 else 0
    return total_rows, total_columns, completeness_percentage, uniqueness_percentage

st.title("Exploratory Data Analysis")
uploaded_files = st.file_uploader("Upload your CSV files", type=["csv"], accept_multiple_files=True)

if uploaded_files:
    start_time = time.time()
    success_messages = ""
    success_placeholder = st.empty()
    success_placeholder.text_area("EDA Report:", value=success_messages, height=350)
    for index, uploaded_file in enumerate(reversed(uploaded_files)):
        with st.spinner(f"Processing {uploaded_file.name}..."):
            df = load_data(uploaded_file)
            profile = ProfileReport(
                df,
                title=f"EDA Report for {uploaded_file.name}",
                explorative=True,
                sensitive=True,
                correlations=None,
                interactions={"continuous": False}
            )
            total_rows, total_columns, completeness_percentage, uniqueness_percentage = calculate_metrics(df)
            report_filename = (
                f"{os.path.splitext(uploaded_file.name)[0]}_"
                f"(row{total_rows}_col{total_columns}_"
                f"c{int(completeness_percentage):02}_u{int(uniqueness_percentage):02}).html"
            )
            report_path = os.path.join(os.getcwd(), "reports", report_filename)
            profile.to_file(report_path)
            success_message = f"{index + 1}. {uploaded_file.name}\n{report_path}\n\n"
            success_messages += success_message
            success_placeholder.text_area("EDA Report:", value=success_messages, height=350)
    end_time = time.time()
    print_time_taken(time.time() - start_time)