import streamlit as st
import streamlit.components.v1 as components

# ... (Giữ nguyên các phần cấu hình trang, Header, Logo của bạn) ...

# ==========================================
# 1. KHO DỮ LIỆU TÀI LIỆU SỐ (CẤU TRÚC TỪ ĐIỂN 2 LỚP)
# ==========================================
# Thay các link "https://fliphtml5.com/..." bằng link iframe thật của bạn
KHO_SACH = {
    "📰 Bản tin Sinh hoạt Chi bộ": {
        "Bản tin Tháng 5/2026": "https://fliphtml5.com/bookcase/xxxx",
        "Bản tin Tháng 4/2026": "https://fliphtml5.com/bookcase/yyyy"
    },
    "📚 Lịch sử Đảng bộ tỉnh": {
        "Lịch sử Đảng bộ tỉnh (Tập 1)": "https://fliphtml5.com/bookcase/aaaa",
        "Lịch sử Đảng bộ tỉnh (Tập 2)": "https://fliphtml5.com/bookcase/bbbb",
        "Lịch sử truyền thống Ngành Tuyên giáo": "https://fliphtml5.com/bookcase/cccc"
    },
    "🎯 Văn kiện - Nghị quyết": {
        "Văn kiện Đại hội đại biểu Đảng bộ tỉnh lần thứ XVII": "https://fliphtml5.com/bookcase/dddd",
        "Nghị quyết Hội nghị Trung ương 8 khóa XIII": "https://fliphtml5.com/bookcase/eeee"
    },
    "🌿 Mô hình Dân vận khéo": {
        "Sổ tay xây dựng mô hình Dân vận khéo": "https://fliphtml5.com/bookcase/ffff"
    }
}

# ==========================================
# 2. GIAO DIỆN CHỌN SÁCH THÔNG MINH
# ==========================================
st.markdown("### 📖 THƯ VIỆN TÀI LIỆU SỐ")

# Tạo 2 cột để chọn Thể loại và Tên sách cho gọn gàng
col1, col2 = st.columns([1, 2])

with col1:
    # Lớp 1: Chọn nhóm tài liệu (Lấy các key chính của KHO_SACH)
    nhom_tai_lieu = st.selectbox("📌 Chọn Nhóm tài liệu:", list(KHO_SACH.keys()))

with col2:
    # Lớp 2: Chọn cuốn sách cụ thể (Dựa vào nhóm đã chọn ở Lớp 1)
    danh_sach_cuon = list(KHO_SACH[nhom_tai_lieu].keys())
    cuon_sach = st.selectbox("📕 Chọn Cuốn sách / Kỳ xuất bản:", danh_sach_cuon)

# Lấy ra link FlipHTML5 tương ứng với lựa chọn
link_hien_thi = KHO_SACH[nhom_tai_lieu][cuon_sach]

st.markdown("---")

# ==========================================
# 3. NHÚNG KHUNG HIỂN THỊ SÁCH (FLIPHTML5)
# ==========================================
with st.spinner("Đang tải dữ liệu sách số..."):
    components.html(
        f"""
        <div style="display: flex; justify-content: center; background-color: #555555; border-radius: 8px; padding: 10px;">
            <iframe style="width:100%; height:750px; border:none; border-radius: 5px;"
                    src="{link_hien_thi}"
                    seamless="seamless" scrolling="no" frameborder="0"
                    allowtransparency="true" allowfullscreen="true">
            </iframe>
        </div>
        """,
        height=770
    )
