"""
Streamlit interface for Market Research Bot
"""
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


import os
import sys
import streamlit as st
import pandas as pd
from src.summarizer import summarize_text

# Add project root to Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, ".."))
if project_root not in sys.path:
    sys.path.append(project_root)

st.set_page_config(page_title="📊 Market Research Bot", layout="wide")
st.title("📊 Autonomous Market Research Bot")

uploaded_file = st.file_uploader("Upload a CSV with competitor text data", type=["csv"])

if uploaded_file:
    try:
        df = pd.read_csv(uploaded_file)
        st.success("✅ File uploaded successfully!")

        if "description" not in df.columns or "company" not in df.columns:
            st.error("❌ CSV must contain 'company' and 'description' columns.")
        else:
            st.dataframe(df)

            st.subheader("📌 Summaries")
            with st.spinner("Generating summaries..."):
                df["summary"] = df["description"].apply(summarize_text)
                st.success("✅ Summaries generated.")

            st.write(df[["company", "summary"]])

            st.download_button(
                "📥 Download Summaries",
                df.to_csv(index=False),
                file_name="summarized_competitors.csv",
                mime="text/csv"
            )

    except Exception as e:
        st.error(f"❌ Error processing file: {e}")
else:
    st.info("📤 Please upload a CSV file to begin.")
