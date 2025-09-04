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
# CUSTOM CSS (Tema Modern)
# ============================
st.markdown("""
    <style>
        /* ==============================
           BASE STYLE
        ============================== */
        .stApp {
            background-color: #222831;
            color: #EEEEEE;
            font-family: 'Segoe UI', sans-serif;
        }

        /* Sidebar */
        [data-testid="stSidebar"] {
            background-color: #393E46;
        }

        /* Header */
        header[data-testid="stHeader"] {
            background-color: #222831 !important;
        }
        header[data-testid="stHeader"]::before {
            background: none !important;
        }

        /* Hilangkan hanya logo Streamlit, bukan toggle */
        header[data-testid="stHeader"] > div:first-child svg {
            display: none !important;
        }

        /* Title */
        h1, h2, h3, h4 {
            color: #00ADB5 !important;
        }

        /* Label */
        label, .st-emotion-cache-1wbqy5l, .st-emotion-cache-16idsys p {
            color: #CCCCCC !important;
            font-weight: 500;
        }
            
        /* ==============================
           CUSTOM CODE BLOCK (Sintaks)
        ============================== */
        code {
            font-size: 18px !important;   /* lebih besar */
            font-weight: 600 !important;
            color: #00FFF5 !important;    /* biru neon */
            background-color: #1a1f25 !important;
            padding: 4px 8px;
            border-radius: 8px;
        }
            
        /* ==============================
           INPUT & DROPDOWN
        ============================== */
        input[type="text"], div[data-baseweb="select"] > div {
            background-color: #222831 !important;
            color: #EEEEEE !important;
            border: 1px solid #00ADB5 !important;
            border-radius: 6px;
            transition: all 0.3s ease-in-out;
        }

        /* Placeholder */
        input[type="text"]::placeholder,
        div[data-baseweb="select"] span {
            color: #AAAAAA !important;
        }

        /* Hover Glow */
        input[type="text"]:hover,
        div[data-baseweb="select"] > div:hover {
            box-shadow: 0 0 10px #00ADB5;
            border: 1px solid #00FFF5 !important;
        }
        input[type="text"]:focus,
        div[data-baseweb="select"] > div:focus-within {
            box-shadow: 0 0 15px #00FFF5;
            border: 1px solid #00FFF5 !important;
        }

        /* ==============================
           EXPANDER
        ============================== */
        .streamlit-expanderHeader {
            background-color: #393E46 !important;
            color: #EEEEEE !important;
            border-radius: 6px;
            transition: all 0.3s ease-in-out;
        }
        .streamlit-expanderHeader:hover {
            box-shadow: 0 0 12px #00ADB5;
        }

        /* ==============================
           FOOTER
        ============================== */
        .footer {
            text-align: left;
            padding-top: 30px;
            font-size: 14px;
            color: #EEEEEE;
        }
        .footer span {
            color: #00ADB5;
            font-weight: bold;
        }
            
        /* ==============================
           CUSTOM ALERT BOXES
        ============================== */

        /* Info Box */
        div.stAlert[data-baseweb="notification"] {
            background-color: #393E46 !important;
            color: #FFFFFF !important;
            border-left: 5px solid #00ADB5 !important;
            border-radius: 6px !important;
            padding: 10px 15px !important;
            transition: all 0.3s ease-in-out;
        }
        div.stAlert[data-baseweb="notification"]:hover {
            box-shadow: 0 0 12px #00ADB5;
        }

        /* Success Box */
        div.stAlert[data-baseweb="notification"][class*="success"] {
            background-color: #1e3d32 !important;
            border-left: 5px solid #4CAF50 !important;
            color: #FFFFFF !important;
        }
        div.stAlert[data-baseweb="notification"][class*="success"]:hover {
            box-shadow: 0 0 12px #4CAF50;
        }

        /* Warning Box */
        div.stAlert[data-baseweb="notification"][class*="warning"] {
            background-color: #3d3622 !important;
            border-left: 5px solid #FFC107 !important;
            color: #FFFFFF !important;
        }
        div.stAlert[data-baseweb="notification"][class*="warning"]:hover {
            box-shadow: 0 0 12px #FFC107;
        }

        /* Error Box */
        div.stAlert[data-baseweb="notification"][class*="error"] {
            background-color: #3d2222 !important;
            border-left: 5px solid #F44336 !important;
            color: #FFFFFF !important;
        }
        div.stAlert[data-baseweb="notification"][class*="error"]:hover {
            box-shadow: 0 0 12px #F44336;
        }

        /* Pastikan teks di dalam box putih */
        div.stAlert[data-baseweb="notification"] p,
        div.stAlert[data-baseweb="notification"] li,
        div.stAlert[data-baseweb="notification"] span {
            color: #FFFFFF !important;
        }
    </style>
""", unsafe_allow_html=True)

# ============================
# BACKEND: Load Database
# ============================
@st.cache_data
def load_data():
    try:
        df = pd.read_csv("data/db_function.csv", encoding="utf-8-sig")
    except UnicodeDecodeError:
        df = pd.read_csv("data/db_function.csv", encoding="latin1")
    return df

df = load_data()

# ============================
# FRONTEND: UI
# ============================
st.title("📘 Excel Function Encyclopedia")
st.markdown("""
Selamat datang di **Excel Function Encyclopedia**!  

Di sini kamu bisa **Mempelajari, dan memahami semua function Excel** 
lengkap dengan kategori, sintaks, dan contoh kasus.  
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

order_level = ["Basic", "Beginner", "Intermediate", "Advance"]
selected_level = st.sidebar.multiselect(
    "Tingkat:",
    options=order_level
)

# Tambah footer di sidebar
st.sidebar.markdown(
    "<div class='footer'>Created by <span>Almadha Rafif</span></div>",
    unsafe_allow_html=True
)

# Tambah tulisan dan gambar support
st.sidebar.markdown(
    """
    <div style='margin-top:20px; margin-bottom:8px; font-weight:bold; color:#00ADB5; font-size:16px;'>
        Support Kak Madha dengan traktir Nasi Goreng dan Kopi lewat link ini
    </div>
    """,
    unsafe_allow_html=True
)
st.sidebar.markdown(
    "<a href='https://lynk.id/almadharp' target='_blank'>",
    unsafe_allow_html=True
)
st.sidebar.image("data/assets/lynkid.png", width=250)
st.sidebar.markdown("</a>", unsafe_allow_html=True)

# ============================
# BACKEND: Filtering
# ============================
filtered_df = df.copy()

if search_query:
    filtered_df = filtered_df[
        filtered_df["Nama Function"].str.contains(search_query, case=False, na=False)
    ]

if selected_category:
    filtered_df = filtered_df[filtered_df["Kategori"].isin(selected_category)]

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

            # if pd.notna(row['Catatan']):
            #     st.info(f"💡 {row['Catatan']}")