import streamlit as st
import base64

st.set_page_config(page_title="Bản tin Chi bộ - Tuyên Quang", page_icon="📖", layout="wide")

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

# Bộ lọc chọn tháng
col_chon, col_trong = st.columns([1, 3])
with col_chon:
    thang_chon = st.selectbox("📌 Chọn kỳ xuất bản:", ["Bản tin Tháng 3/2026", "Bản tin Tháng 2/2026", "Bản tin Tháng 1/2026"])

# DANH SÁCH LINK FLIPBOOK TỪNG THÁNG
thu_vien_link = {
    "Bản tin Tháng 3/2026": "https://heyzine.com/flip-book/701fc3e590.html",
    "Bản tin Tháng 2/2026": "https://heyzine.com/flip-book/5a1b559093.html",
    "Bản tin Tháng 1/2026": "https://heyzine.com/flip-book/b8e0a13ea1.html"
}

link_hien_tai = thu_vien_link[thang_chon]

# Nhúng Flipbook vào khung
st.markdown(f"""
    <iframe src="{link_hien_tai}" width="100%" height="750px" frameborder="0" allowfullscreen seamless style="border-radius: 10px; box-shadow: 0px 4px 10px rgba(0,0,0,0.1);"></iframe>
""", unsafe_allow_html=True)

st.info("💡 Hướng dẫn: Vuốt từ phải sang trái hoặc bấm vào mép trang sách để lật trang. Bấm biểu tượng ⛶ ở góc để xem toàn màn hình.")
