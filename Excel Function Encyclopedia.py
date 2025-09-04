import streamlit as st
import pandas as pd

# ============================
# CONFIG (harus paling atas)
# ============================
st.set_page_config(
    page_title="Excel Function Encyclopedia",
    page_icon="📘",
    layout="wide"
)

# ============================
# LOGIN SYSTEM
# ============================

@st.cache_data
def load_users():
    try:
        df = pd.read_csv("data/assets/idpass.csv", encoding="utf-8-sig")
    except UnicodeDecodeError:
        df = pd.read_csv("data/assets/idpass.csv", encoding="latin1")

    # Bersihkan spasi & pastikan string
    df["Username"] = df["Username"].astype(str).str.strip()
    df["Password"] = df["Password"].astype(str).str.strip()
    return df

users_df = load_users()

# Init session state
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.username = None

# Jika belum login
if not st.session_state.logged_in:
    st.title("🔑 Login")

    username = st.text_input("Username").strip()
    password = st.text_input("Password", type="password").strip()

    if st.button("Login"):
        # Normalisasi input
        username_check = users_df[users_df["Username"].str.lower() == username.lower()]

        if username_check.empty:
            st.error("❌ Username tidak ditemukan.")
        else:
            if username_check["Password"].values[0] == password:
                st.session_state.logged_in = True
                st.session_state.username = username_check["Username"].values[0]
                st.success(f"✅ Selamat datang, {st.session_state.username}!")
                st.rerun()
            else:
                st.error("❌ Password salah.")
else:
    # Kalau sudah login
    st.sidebar.success(f"👋 Hi, {st.session_state.username}")

    if st.sidebar.button("Logout"):
        st.session_state.logged_in = False
        st.session_state.username = None
        st.rerun()

# ============================
# CUSTOM CSS (Tema Modern)
# ============================
    st.markdown("""
        <style>
            .stApp {
                background-color: #222831;
                color: #EEEEEE;
                font-family: 'Segoe UI', sans-serif;
            }
            [data-testid="stSidebar"] {
                background-color: #393E46;
            }
            header[data-testid="stHeader"] {
                background-color: #222831 !important;
            }
            header[data-testid="stHeader"]::before {
                background: none !important;
            }
            header[data-testid="stHeader"] > div:first-child svg {
                display: none !important;
            }
            h1, h2, h3, h4 {
                color: #00ADB5 !important;
            }

            /* Sidebar Success Box Override */
            section[data-testid="stSidebar"] div.stAlert {
                background-color: #1b4332 !important;   /* Hijau tua */
                border-left: 5px solid #4CAF50 !important;
                color: #FFFFFF !important;
            }
            section[data-testid="stSidebar"] div.stAlert p {
                color: #FFFFFF !important;              /* Putih */
                font-weight: 600 !important;
            }

            /* Style khusus semua tombol */
            div.stButton > button {
                background-color: #00ADB5 !important;   /* teal */
                color: #FFFFFF !important;              /* teks putih */
                border: none !important;
                border-radius: 8px !important;
                font-weight: 600 !important;
                transition: all 0.3s ease-in-out;
            }
            div.stButton > button:hover {
                background-color: #00FFF5 !important;   /* hover jadi biru terang */
                color: #222831 !important;              /* teks hitam */
                box-shadow: 0 0 10px #00FFF5 !important;
            }

            label, .st-emotion-cache-1wbqy5l, .st-emotion-cache-16idsys p {
                color: #CCCCCC !important;
                font-weight: 500;
            }
            code {
                font-size: 18px !important;
                font-weight: 600 !important;
                color: #00FFF5 !important;
                background-color: #1a1f25 !important;
                padding: 4px 8px;
                border-radius: 8px;
            }
            input[type="text"], div[data-baseweb="select"] > div {
                background-color: #222831 !important;
                color: #EEEEEE !important;
                border: 1px solid #00ADB5 !important;
                border-radius: 6px;
                transition: all 0.3s ease-in-out;
            }
            input[type="text"]::placeholder,
            div[data-baseweb="select"] span {
                color: #AAAAAA !important;
            }
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
            .streamlit-expanderHeader {
                background-color: #393E46 !important;
                color: #EEEEEE !important;
                border-radius: 6px;
                transition: all 0.3s ease-in-out;
            }
            .streamlit-expanderHeader:hover {
                box-shadow: 0 0 12px #00ADB5;
            }
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
            div.stAlert[data-baseweb="notification"][class*="success"] {
                background-color: #1e3d32 !important;
                border-left: 5px solid #4CAF50 !important;
                color: #FFFFFF !important;
            }
            div.stAlert[data-baseweb="notification"][class*="warning"] {
                background-color: #3d3622 !important;
                border-left: 5px solid #FFC107 !important;
                color: #FFFFFF !important;
            }
            div.stAlert[data-baseweb="notification"][class*="error"] {
                background-color: #3d2222 !important;
                border-left: 5px solid #F44336 !important;
                color: #FFFFFF !important;
            }
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
if st.session_state.logged_in:
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

    # Footer
    st.sidebar.markdown("<div class='footer'>Created by <span>Almadha Rafif</span></div>", unsafe_allow_html=True)

    st.sidebar.markdown(
        """
        <div style='margin-top:20px; margin-bottom:8px; font-weight:bold; color:#00ADB5; font-size:16px;'>
            Support Kak Madha dengan traktir Nasi Goreng dan Kopi lewat link ini
        </div>
        """,
        unsafe_allow_html=True
    )
    st.sidebar.markdown("<a href='https://lynk.id/almadharp' target='_blank'>", unsafe_allow_html=True)
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