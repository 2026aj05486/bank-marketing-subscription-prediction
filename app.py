from pathlib import Path
import runpy
import zipfile
import streamlit as st

ROOT = Path(__file__).resolve().parent
BUNDLE = ROOT / "project_bundle.zip"
PROJECT_DIR = ROOT / "Bank_Marketing_Subscription_Prediction"

if not BUNDLE.exists():
    st.error("The model bundle project_bundle.zip is missing. Please add it to the repository root.")
    st.stop()

if not (PROJECT_DIR / "preprocessor.joblib").exists():
    try:
        with zipfile.ZipFile(BUNDLE, "r") as archive:
            archive.extractall(ROOT)
    except Exception as exc:
        st.error(f"Could not extract the saved model bundle: {exc}")
        st.stop()

APP_FILE = PROJECT_DIR / "app.py"
if not APP_FILE.exists():
    st.error("The application source app.py is missing from the model bundle.")
    st.stop()

runpy.run_path(str(APP_FILE), run_name="__main__")
