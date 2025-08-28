import streamlit as st
import pandas as pd
import os

# ============================
# CONFIG
# ============================
st.set_page_config(page_title="Excel Function Trial", layout="wide")

# ============================
# BACKEND: Load Database
# ============================
@st.cache_data
def load_function_db():
    return pd.read_csv("data/db_function.csv")

@st.cache_data
def load_practice_db():
    return pd.read_csv("data/practice_db/practice_db.csv")

def load_dataset(file_name):
    file_path = os.path.join("data/datasets", file_name)
    if file_path.endswith(".csv"):
        return pd.read_csv(file_path)
    elif file_path.endswith(".xlsx"):
        return pd.read_excel(file_path)
    else:
        st.error("❌ Format dataset tidak didukung.")
        return pd.DataFrame()

# ============================
# DATA
# ============================
function_db = load_function_db()
practice_db = load_practice_db()

# ============================
# FRONTEND: UI
# ============================
st.title("🧪 Excel Function Trial")
st.markdown("Pilih sebuah function dari daftar untuk melihat contoh dataset dan mencoba penerapannya.")

# Dropdown Function (mengacu ke db_function)
selected_func = st.sidebar.selectbox(
    "🔎 Pilih Function:",
    options=sorted(function_db["Nama Function"].dropna().unique())
)

if selected_func:
    # =======================
    # INFO DARI db_function
    # =======================
    func_info = function_db[function_db["Nama Function"] == selected_func].iloc[0]

    st.subheader(f"📘 {func_info['Nama Function']}")
    st.markdown(f"**Kategori:** {func_info['Kategori']}")
    st.markdown(f"**Sintaks:** `{func_info['Sintaks']}`")
    st.markdown(f"**Deskripsi:** {func_info['Deskripsi']}")
    st.markdown(f"**Contoh Kasus:** {func_info['Contoh Kasus']}")

    # =======================
    # DATASET DARI practice_db
    # =======================
    dataset_info = practice_db[practice_db["Nama Function"] == selected_func]

    if not dataset_info.empty:
        dataset_info = dataset_info.iloc[0]
        dataset_file = dataset_info["Dataset"]

        st.markdown("### 📊 Dataset Contoh")
        df_example = load_dataset(dataset_file)
        st.dataframe(df_example, use_container_width=True)

        # Tampilkan Catatan / Hint
        if "Catatan" in dataset_info and pd.notna(dataset_info["Catatan"]):
            st.info(f"💡 {dataset_info['Catatan']}")

        st.success("Silakan gunakan dataset ini di Excel dan coba aplikasikan formula di atas!")
    else:
        st.warning("⚠️ Belum ada dataset practice untuk function ini.")