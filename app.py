import streamlit as st
import streamlit.components.v1 as components

# BẬT CHẾ ĐỘ TRÀN VIỀN (FULL MÀN HÌNH) - LỆNH NÀY PHẢI ĐẶT TRÊN CÙNG
st.set_page_config(page_title="Thư viện số TGDV", page_icon="📚", layout="wide")

# --- Tiêu đề trang ---
st.markdown("### 📚 THƯ VIỆN SỐ SINH HOẠT CHI BỘ")
st.info("💡 Mẹo: Bạn có thể bấm trực tiếp vào từng cuốn sách trên kệ để mở ra đọc toàn màn hình.")

# --- Link bookcase của sếp ---
link_bookcase = "https://fliphtml5.com/bookcase/yeprz/?v=1"

# ==========================================
# 1. NÚT MỞ TOÀN MÀN HÌNH (CỨU TINH CHO ĐIỆN THOẠI)
# ==========================================
st.markdown(f"""
    <div style="text-align: right; margin-bottom: 15px;">
        <a href="{link_bookcase}" target="_blank" style="background-color: #004B87; color: white; padding: 10px 18px; text-decoration: none; border-radius: 8px; font-weight: bold; font-size: 14px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); transition: 0.3s;">
            ⛶ MỞ ĐỌC TOÀN MÀN HÌNH
        </a>
    </div>
""", unsafe_allow_html=True)

# ==========================================
# 2. KHUNG ĐỌC TRỰC TIẾP (TỐI ƯU PC VÀ MOBILE)
# ==========================================
st.markdown(f"""
    <style>
        .responsive-iframe {{
            width: 100%;
            height: 850px;
            border: none;
            border-radius: 8px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.05);
        }}
        /* Tự động co bóp thông minh khi xem trên điện thoại */
        @media (max-width: 768px) {{
            .responsive-iframe {{
                height: 600px; /* Chiều cao vừa vặn để vuốt */
                border-radius: 0px; /* Bỏ bo góc để ép sát lề */
            }}
        }}
    </style>
    <iframe class="responsive-iframe" 
            src="{link_bookcase}" 
            allowfullscreen="true" 
            webkitallowfullscreen="true" 
            mozallowfullscreen="true">
    </iframe>
""", unsafe_allow_html=True)

st.markdown("---")
st.markdown("<p style='text-align:center; color:#888; font-size: 13px;'>Hệ thống tài liệu số - Ban Tuyên giáo và Dân vận Tỉnh ủy Tuyên Quang</p>", unsafe_allow_html=True)
