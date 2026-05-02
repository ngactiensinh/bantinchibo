import streamlit as st

# 1. KHAI BÁO KHO SÁCH (Sếp dán link trực tiếp của từng cuốn vào đây)
# Link lấy từ mục "Share" của từng cuốn sách trên FlipHTML5
KHO_BAN_TIN = {
    "Bản tin Tháng 5/2026": {
        "link": "https://online.fliphtml5.com/yeprz/abdc/", 
        "cover": "https://pub-static.fleepit.com/dev/logos/fliphtml5-logo.png" # Có thể thay bằng link ảnh bìa nếu có
    },
    "Bản tin Tháng 4/2026": {
        "link": "https://online.fliphtml5.com/yeprz/xyza/",
        "cover": "https://pub-static.fleepit.com/dev/logos/fliphtml5-logo.png"
    }
}

# 2. CSS LÀM ĐẸP THẺ SÁCH
st.markdown("""
<style>
    .book-container {
        display: flex;
        flex-wrap: wrap;
        gap: 20px;
        justify-content: center;
    }
    .book-card {
        width: 160px;
        background: white;
        padding: 10px;
        border-radius: 10px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.1);
        text-align: center;
        transition: 0.3s;
    }
    .book-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 6px 15px rgba(0,75,135,0.2);
    }
    .book-cover {
        width: 100%;
        height: 220px;
        background-color: #004B87; /* Màu nền nếu chưa có ảnh bìa */
        border-radius: 5px;
        margin-bottom: 10px;
        display: flex;
        align-items: center;
        justify-content: center;
        color: white;
        font-weight: bold;
        font-size: 40px;
    }
    .book-title {
        font-size: 14px;
        font-weight: bold;
        color: #333;
        text-decoration: none;
        display: block;
        margin-top: 5px;
    }
    .btn-read {
        display: inline-block;
        margin-top: 10px;
        padding: 5px 15px;
        background-color: #C8102E;
        color: white !important;
        text-decoration: none;
        border-radius: 5px;
        font-size: 12px;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# 3. GIAO DIỆN CHÍNH
st.markdown("### 📚 THƯ VIỆN SỐ SINH HOẠT CHI BỘ")
st.info("💡 Các đồng chí chạm vào bìa sách hoặc nút 'ĐỌC NGAY' để mở bản tin toàn màn hình.")

# Tạo hàng cột để hiển thị các thẻ sách
cols = st.columns(4) # Trên PC hiện 4 cột, Mobile tự nhảy thành 1-2 cột

# Duyệt qua kho sách để hiển thị
for idx, (ten_sach, data) in enumerate(KHO_BAN_TIN.items()):
    with cols[idx % 4]:
        st.markdown(f"""
            <div class="book-card">
                <div class="book-cover">📖</div>
                <div class="book-title">{ten_sach}</div>
                <a href="{data['link']}" target="_top" class="btn-read">📖 ĐỌC NGAY</a>
            </div>
        """, unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# 4. NÚT PHỤ: XEM CẢ TỦ SÁCH (Dành cho ai thích xem kệ gỗ)
with st.expander("📂 Xem toàn bộ kệ sách (Giao diện cũ)"):
    st.markdown(f"""
        <iframe style="width:100%; height:600px; border:none;" 
                src="https://fliphtml5.com/bookcase/yeprz/?v=1" 
                allowfullscreen="true">
        </iframe>
    """, unsafe_allow_html=True)
