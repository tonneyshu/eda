## Overview

![image](https://github.com/user-attachments/assets/f93d8b19-d050-4830-b4cd-af2c9ba4f2d5)


**Exploratory Data Analysis** is a Streamlit application that allows users to perform exploratory data analysis (EDA) on CSV files. It leverages the ydata_profiling library to generate comprehensive reports that summarize the data characteristics.

## Features

- **CSV File Upload**: Users can upload multiple CSV files for analysis.
- **Automated EDA Reports**: For each uploaded file, an EDA report is generated, providing insights into the dataset.
- **Metrics Calculation**: The app calculates key metrics such as total rows, total columns, completeness percentage, and uniqueness percentage.

## Requirements

Ensure you have Python 3.10 or higher installed. All required packages are listed in the `requirements.txt` file. You can install them using pip:

```bash
pip install -r requirements.txt
```

## Setup

1. **Clone the Repository**: 
   ```bash
   git clone https://github.com/tonneyshu/eda.git
   ```

2. **Run the Application**:
   Start the Streamlit application by running:
   ```bash
   streamlit run app.py
   ```

## Usage

1. Upload CSV Files: Once the app is running, open it in your web browser. Use the file uploader to select and upload your CSV files.
2. View EDA Reports: The application will process each file and generate an EDA report. You can view the report paths displayed in the text area.

## Code Explanation

### Key Functions

- **load_data()**: Reads CSV files into a Pandas DataFrame.
- **calculate_metrics()**: Computes essential metrics about the dataset, including:
   - Total number of rows and columns
   - Total missing values
   - Completeness percentage
   - Uniqueness percentage

## Acknowledgments

- [YData Profiling](https://github.com/ydataai/ydata-profiling)
