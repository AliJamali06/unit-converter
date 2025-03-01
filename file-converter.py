import streamlit as st 
import pandas as pd
from io import BytesIO

st.set_page_config(page_title="file Converter", layout="wide")
st.title("File Conerter & Cleaner")
st.write("upload csv or excel files data ,and convert formats.")

files =st.file_uploader("Upload CSV Excel Files." , type=["csv", "xlsx"], accept_multiple_files=True)

if files :
    for file in files:
        ext = file.name.split(".")[-1]
        df = pd.read_csv(file) if ext == "csv" else pd.read_excel(file)
        st.subheader(f"{file.name} - preview")
        st.dataframe(df.head())

        if st.checkbox(f"Remove Duplicate - {file.name}"):
            df= df.drop_dublicate()
            st.success("Duplicates Removed")
            st.dataframe(df.head())

            if st.checkbox(f"Fill Missing Values- {file.name}"):
                df.fillna(df.select_dtypes (include=["number"]).mean(), inplace=True)
                # df.fillna(df.select_dtypes(include=["number"]).mean(), inplace=True)

                st.success("Missing Values Filled")
                st.dataframe(df.head()) 
                selected_colums = st.multiselect(f"Select Colums - {file.name}", df.colums, default=df.colums)
                df = df[selected_colums]
                st.dataframe(df.head())

                if st.checkbox(f"Show Chart - (file.name)") and not df.select_dtypes(include="number").empty:
                    format_choise = st.radio(f"Convert {file.name} to:",["csv", "Excel"], key=file.name)

                    if st.button(f"Download {file.name} as {format_choise}"):
                        output = BytesIO()
                        if format_choise == "csv":
                            df.to_csv(output, index=False)
                            mine = "text/csv"
                            new_name = file.name.replace(ext,"csv")
                        else :
                            df.to_excel(output,index=False, engine="openpyxl")
                            mine= "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                            new_name = file.name.replace(ext, "xlsx")

                            output.seek(a)
                            st.download_button("download file",file_name=new_name, data=output, mine=mine)

                            st.success("processing complete!")

                              


                

