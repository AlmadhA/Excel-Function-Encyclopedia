import streamlit as st
import pandas as pd

# ============================
# CONFIG
# ============================
st.set_page_config(
    page_title="Excel Function Encyclopedia",
    page_icon="📘",
    layout="wide"
)

# ============================
# BACKEND: Load Database
# ============================
@st.cache_data
def load_data():
    df = pd.read_csv("data/db_function.csv")  # database utama function
    return df

df = load_data()

# ============================
# FRONTEND: UI
# ============================
# Judul
st.title("📘 Excel Function Encyclopedia")
st.markdown("""
Selamat datang di **Excel Function Encyclopedia**!  

Di sini kamu bisa **mencari, mempelajari, dan memahami semua function Excel** 
lengkap dengan kategori, sintaks, deskripsi, contoh kasus, serta tingkat kesulitan.  

👉 Untuk praktek langsung, buka halaman **Excel Function Trial** di sidebar.
""")

# ============================
# SIDEBAR FILTER
# ============================
st.sidebar.header("🔎 Filter Function")

search_query = st.sidebar.text_input("Cari function berdasarkan nama:")
selected_category = st.sidebar.multiselect(
    "Kategori:",
    options=sorted(df["Kategori"].dropna().unique())
)
selected_level = st.sidebar.multiselect(
    "Tingkat:",
    options=sorted(df["Tingkat"].dropna().unique())
)

# ============================
# BACKEND: Filtering
# ============================
filtered_df = df.copy()

# Filter by search
if search_query:
    filtered_df = filtered_df[
        filtered_df["Nama Function"].str.contains(search_query, case=False, na=False)
    ]

# Filter by category
if selected_category:
    filtered_df = filtered_df[filtered_df["Kategori"].isin(selected_category)]

# Filter by level
if selected_level:
    filtered_df = filtered_df[filtered_df["Tingkat"].isin(selected_level)]

# ============================
# FRONTEND: Display Function List
# ============================
st.subheader("📂 Daftar Function")

if filtered_df.empty:
    st.warning("⚠️ Tidak ada function yang cocok dengan filter.")
else:
    for _, row in filtered_df.iterrows():
        with st.expander(f"🔹 {row['No']}. {row['Nama Function']}"):
            st.markdown(f"**Kategori:** {row['Kategori']}")
            st.markdown(f"**Sintaks:** `{row['Sintaks']}`")
            st.markdown(f"**Deskripsi:** {row['Deskripsi']}")
            st.markdown(f"**Contoh Kasus:** {row['Contoh Kasus']}")
            st.markdown(f"**Tingkat:** {row['Tingkat']}")
            
            if pd.notna(row['Catatan']):
                st.info(f"💡 {row['Catatan']}")