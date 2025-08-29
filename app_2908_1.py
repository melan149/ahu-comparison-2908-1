import streamlit as st
import pandas as pd
from PIL import Image
import plotly.express as px
import numpy as np


# -----------------------------
# Load data
# -----------------------------
@st.cache_data
def load_data():
return pd.read_excel("Data_2025_2.xlsx", sheet_name="data", engine="openpyxl")


df = load_data()


# -----------------------------
# Helpers
# -----------------------------
def get_column_safe(df, name_options):
for name in name_options:
if name in df.columns:
return name
return None


unit_name_col = get_column_safe(df, ["Unit name", "Unit Name"])
region_col = get_column_safe(df, ["Region"])
year_col = get_column_safe(df, ["Year"])
quarter_col = get_column_safe(df, ["Quarter"])
recovery_col = get_column_safe(df, ["Recovery type", "Recovery Type"])
size_col = get_column_safe(df, ["Unit size", "Unit Size"])
brand_col = get_column_safe(df, ["Brand name", "Brand"])
logo_col = get_column_safe(df, ["Brand logo", "Brand Logo"])
unit_photo_col = get_column_safe(df, ["Unit photo", "Unit Photo"])
type_col = get_column_safe(df, ["Type"])
material_col = get_column_safe(df, ["Material"])


# Updated columns
impeller_size_col = get_column_safe(df, ["Impeller size (available optins)", "Impeller size"])
impeller_efficiency_col = get_column_safe(df, ["Impeller efficiency at optimal airflow [%]", "Impeller efficiency at nominal airflow [%]"])
capacity_note_col = get_column_safe(df, ["Capacity Note"])
base_frame_height_col = get_column_safe(df, ["Base frame/Feets height [mm]"])
cabling_col = get_column_safe(df, ["Cabling"])


# -----------------------------
# Sidebar filter block per unit
# -----------------------------
def unit_filter_block(unit_idx, df):
st.markdown(f"### Select Unit {unit_idx}")


year = st.selectbox(f"Year (Unit {unit_idx})", sorted(df[year_col].dropna().unique()), key=f"year_{unit_idx}")
df_tmp = df[df[year_col] == year]


quarter = st.selectbox(f"Quarter (Unit {unit_idx})", sorted(df_tmp[quarter_col].dropna().unique()), key=f"quarter_{unit_idx}")
df_tmp = df_tmp[df_tmp[quarter_col] == quarter]


region = st.selectbox(f"Region (Unit {unit_idx})", sorted(df_tmp[region_col].dropna().unique()), key=f"region_{unit_idx}")
df_tmp = df_tmp[df_tmp[region_col] == region]


brand = st.selectbox(f"Brand (Unit {unit_idx})", sorted(df_tmp[brand_col].dropna().unique()), key=f"brand_{unit_idx}")
df_tmp = df_tmp[df_tmp[brand_col] == brand]


unit = st.selectbox(f"Unit name (Unit {unit_idx})", sorted(df_tmp[unit_name_col].dropna().unique()), key=f"unit_{unit_idx}")
df_tmp = df_tmp[df_tmp[unit_name_col] == unit]


recovery = st.selectbox(f"Recovery type (Unit {unit_idx})", sorted(df_tmp[recovery_col].dropna().unique()), key=f"recovery_{unit_idx}")
df_tmp = df_tmp[df_tmp[recovery_col] == recovery]


size = st.selectbox(f"Unit size (Unit {unit_idx})", sorted(df_tmp[size_col].dropna().unique()), key=f"size_{unit_idx}")
df_tmp = df_tmp[df_tmp[size_col] == size]

