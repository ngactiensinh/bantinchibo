import streamlit as st
import streamlit.components.v1 as components

# BẬT CHẾ ĐỘ TRÀN VIỀN (FULL MÀN HÌNH) - LỆNH NÀY PHẢI ĐẶT TRÊN CÙNG
st.set_page_config(page_title="Thư viện số TGDV", page_icon="📚", layout="wide")

# --- Tiêu đề trang ---
st.markdown("### 📚 THƯ VIỆN SỐ SINH HOẠT CHI BỘ")
st.info("💡 Mẹo: Bạn có thể bấm trực tiếp vào từng cuốn sách trên kệ để mở ra đọc toàn màn hình.")

# --- Link bookcase của sếp (Đã có đuôi phá cache) ---
link_bookcase = "https://fliphtml5.com/bookcase/yeprz/?v=1"

# --- Nhúng kệ sách vào App ---
with st.spinner("Đang kết nối tới tủ sách điện tử..."):
    components.html(
        f"""
        <div style="display: flex; justify-content: center; background-color: #f4f6f9; border-radius: 12px; padding: 10px; box-shadow: inset 0 0 10px rgba(0,0,0,0.1);">
            <iframe style="width:100%; height:850px; border:none; border-radius: 8px;"
                    src="{link_bookcase}"
                    seamless="seamless" scrolling="no" frameborder="0"
                    allowtransparency="true" allowfullscreen="true">
            </iframe>
        </div>
        """,
        height=880
    )

st.markdown("---")
st.markdown("<p style='text-align:center; color:#888; font-size: 13px;'>Hệ thống tài liệu số - Ban Tuyên giáo và Dân vận Tỉnh ủy Tuyên Quang</p>", unsafe_allow_html=True)
