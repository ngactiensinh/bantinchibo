import streamlit as st
import base64
from supabase import create_client, Client # Thêm dòng này

st.set_page_config(page_title="Bản tin Chi bộ - Tuyên Quang", page_icon="📖", layout="wide")
# ==========================================
# CẤU HÌNH SUPABASE (DÙNG ĐỂ ĐẾM TRUY CẬP)
# ==========================================
SUPABASE_URL = "https://qqzsdxhqrdfvxnlurnyb.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InFxenNkeGhxcmRmdnhubHVybnliIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzU2MjY0NjAsImV4cCI6MjA5MTIwMjQ2MH0.H62F5zYEZ5l47fS4IdAE2JdRdI7inXQqWG0nvXhn2P8"

try:
    supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
except:
    pass

# Hàm đếm lượt truy cập thông minh
def log_access(app_name):
    key_name = f"da_dem_truy_cap_{app_name}"
    if key_name not in st.session_state:
        try:
            supabase.table("thong_ke_truy_cap").insert({"ten_app": app_name}).execute()
            st.session_state[key_name] = True
        except:
            pass

# Kích hoạt bộ đếm cho trang này
log_access("Bản tin Sinh hoạt")

st.markdown("""
<style>
    .header-oval {
        background-color: #ffffff;
        border: 4px solid #C8102E;
        border-radius: 60px;
        padding: 15px 30px;
        margin-bottom: 30px;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.1);
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 25px;
        flex-wrap: wrap;
    }
    .main-title { font-size: 32px; font-weight: 900; color: #C8102E; text-transform: uppercase; margin: 0; line-height: 1.2; text-align: center;}
    .sub-title { font-size: 18px; font-weight: bold; color: #004B87; margin-top: 5px; text-align: center;}
</style>
""", unsafe_allow_html=True)

# Lấy Logo từ kho (nếu có)
logo_html = ""
try:
    with open("Logo TGDV.png", "rb") as f:
        data = base64.b64encode(f.read()).decode("utf-8")
        logo_html = f'<img src="data:image/png;base64,{data}" style="height: 85px;">'
except:
    logo_html = '<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Qu%E1%BB%91c_huy_Vi%E1%BB%87t_Nam.svg/250px-Qu%E1%BB%91c_huy_Vi%E1%BB%87t_Nam.svg.png" style="height: 85px;">'

st.markdown(f"""
<div class="header-oval">
    <div>{logo_html}</div>
    <div>
        <div class="main-title">BẢN TIN SINH HOẠT CHI BỘ</div>
        <div class="sub-title">BAN TUYÊN GIÁO VÀ DÂN VẬN TỈNH ỦY TUYÊN QUANG</div>
    </div>
</div>
""", unsafe_allow_html=True)

st.write("---")

# Bộ lọc chọn tháng/quý
col_chon, col_trong = st.columns([1, 3])
with col_chon:
    thang_chon = st.selectbox("📌 Chọn kỳ xuất bản:", [
        "Bản tin Tháng 4/2026", 
        "Bản tin Quý I/2026",
        "Bản tin Tháng 3/2026", 
        "Bản tin Tháng 2/2026", 
        "Bản tin Tháng 1/2026"
    ])

# DANH SÁCH LINK FLIPBOOK TỪNG THÁNG/QUÝ
thu_vien_link = {
    "Bản tin Tháng 4/2026": "https://online.fliphtml5.com/zwykz/BAN-TIN-SINH-HOAT-THUONG-KY-THANG-4-2026/",
    "Bản tin Quý I/2026": "https://online.fliphtml5.com/zwykz/BAN-TIN-QUY-I-2026/",
    "Bản tin Tháng 3/2026": "https://online.fliphtml5.com/zwykz/BAN-TIN-SINH-HOAT-CHI-BO-THANG-3-2026/",
    "Bản tin Tháng 2/2026": "https://online.fliphtml5.com/zwykz/okrm/",
    "Bản tin Tháng 1/2026": "https://online.fliphtml5.com/zwykz/aozs/"
}

link_hien_tai = thu_vien_link[thang_chon]

# Nhúng Flipbook vào khung
st.markdown(f"""
    <iframe src="{link_hien_tai}" width="100%" height="750px" frameborder="0" allowfullscreen seamless style="border-radius: 10px; box-shadow: 0px 4px 10px rgba(0,0,0,0.1);"></iframe>
""", unsafe_allow_html=True)

st.info("💡 Hướng dẫn: Vuốt từ phải sang trái hoặc bấm vào mép trang sách để lật trang. Bấm biểu tượng ⛶ ở góc để xem toàn màn hình.")
