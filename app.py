import streamlit as st
import base64
from supabase import create_client, Client

st.set_page_config(page_title="Bản tin Chi bộ - Tuyên Quang", page_icon="📖", layout="wide")

# ==========================================
# CẤU HÌNH SUPABASE
# ==========================================
SUPABASE_URL = "https://qqzsdxhqrdfvxnlurnyb.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InFxenNkeGhxcmRmdnhubHVybnliIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzU2MjY0NjAsImV4cCI6MjA5MTIwMjQ2MH0.H62F5zYEZ5l47fS4IdAE2JdRdI7inXQqWG0nvXhn2P8"

# ⚠️ Đổi mật khẩu quản trị tại đây
ADMIN_PASSWORD = "Admin@2026"

try:
    supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
except Exception:
    supabase = None

# Hàm đếm lượt truy cập thông minh
def log_access(app_name):
    key_name = f"da_dem_truy_cap_{app_name}"
    if key_name not in st.session_state:
        try:
            supabase.table("thong_ke_truy_cap").insert({"ten_app": app_name}).execute()
            st.session_state[key_name] = True
        except Exception:
            pass

log_access("Bản tin Sinh hoạt")

# ==========================================
# HÀM LẤY / GHI DỮ LIỆU BẢN TIN TỪ SUPABASE
# ==========================================
@st.cache_data(ttl=60)
def lay_danh_sach_ban_tin():
    try:
        res = (
            supabase.table("ban_tin_sinh_hoat")
            .select("*")
            .order("thu_tu", desc=True)
            .execute()
        )
        return res.data or []
    except Exception as e:
        st.error(f"Không tải được danh sách bản tin: {e}")
        return []

def them_ban_tin(ky, link, thu_tu):
    supabase.table("ban_tin_sinh_hoat").insert(
        {"ky_xuat_ban": ky, "link": link, "thu_tu": thu_tu}
    ).execute()
    st.cache_data.clear()

def sua_ban_tin(id_bantin, ky, link, thu_tu):
    supabase.table("ban_tin_sinh_hoat").update(
        {"ky_xuat_ban": ky, "link": link, "thu_tu": thu_tu}
    ).eq("id", id_bantin).execute()
    st.cache_data.clear()

def xoa_ban_tin(id_bantin):
    supabase.table("ban_tin_sinh_hoat").delete().eq("id", id_bantin).execute()
    st.cache_data.clear()

# ==========================================
# GIAO DIỆN CHUNG
# ==========================================
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

logo_html = ""
try:
    with open("Logo TGDV.png", "rb") as f:
        data = base64.b64encode(f.read()).decode("utf-8")
        logo_html = f'<img src="data:image/png;base64,{data}" style="height: 85px;">'
except Exception:
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

tab_xem, tab_quantri = st.tabs(["📖 Xem bản tin", "🔐 Quản trị"])

# ==========================================
# TAB 1: XEM BẢN TIN (CÔNG KHAI)
# ==========================================
with tab_xem:
    danh_sach = lay_danh_sach_ban_tin()

    if not danh_sach:
        st.warning("Chưa có bản tin nào được đăng. Vui lòng vào tab Quản trị để thêm mới.")
    else:
        ten_ky_list = [item["ky_xuat_ban"] for item in danh_sach]
        col_chon, col_trong = st.columns([1, 3])
        with col_chon:
            thang_chon = st.selectbox("📌 Chọn kỳ xuất bản:", ten_ky_list)

        link_hien_tai = next(item["link"] for item in danh_sach if item["ky_xuat_ban"] == thang_chon)

        st.markdown(f"""
            <iframe src="{link_hien_tai}" width="100%" height="750px" frameborder="0" allowfullscreen seamless style="border-radius: 10px; box-shadow: 0px 4px 10px rgba(0,0,0,0.1);"></iframe>
        """, unsafe_allow_html=True)

        st.info("💡 Hướng dẫn: Vuốt từ phải sang trái hoặc bấm vào mép trang sách để lật trang. Bấm biểu tượng ⛶ ở góc để xem toàn màn hình.")

# ==========================================
# TAB 2: QUẢN TRỊ (CÓ MẬT KHẨU)
# ==========================================
with tab_quantri:
    if "da_dang_nhap_admin" not in st.session_state:
        st.session_state.da_dang_nhap_admin = False

    if not st.session_state.da_dang_nhap_admin:
        st.subheader("🔐 Đăng nhập quản trị")
        mat_khau_nhap = st.text_input("Nhập mật khẩu quản trị:", type="password")
        if st.button("Đăng nhập"):
            if mat_khau_nhap == ADMIN_PASSWORD:
                st.session_state.da_dang_nhap_admin = True
                st.rerun()
            else:
                st.error("Sai mật khẩu, vui lòng thử lại.")
    else:
        col_title, col_logout = st.columns([4, 1])
        with col_title:
            st.subheader("⚙️ Quản lý các kỳ bản tin")
        with col_logout:
            if st.button("Đăng xuất"):
                st.session_state.da_dang_nhap_admin = False
                st.rerun()

        st.write("---")

        # --- THÊM MỚI ---
        st.markdown("### ➕ Thêm bản tin mới")
        danh_sach_hientai = lay_danh_sach_ban_tin()
        thu_tu_max = max([item["thu_tu"] for item in danh_sach_hientai], default=0)

        with st.form("form_them_moi", clear_on_submit=True):
            c1, c2 = st.columns([1, 2])
            with c1:
                ky_moi = st.text_input("Tên kỳ xuất bản (VD: Bản tin Tháng 8/2026)")
            with c2:
                link_moi = st.text_input("Link Flipbook từ Fliphtml5")
            thu_tu_moi = st.number_input(
                "Thứ tự hiển thị (số lớn hơn sẽ hiện lên đầu danh sách)",
                value=thu_tu_max + 1, step=1
            )
            gui = st.form_submit_button("Thêm bản tin")
            if gui:
                if not ky_moi.strip() or not link_moi.strip():
                    st.warning("Vui lòng nhập đầy đủ tên kỳ xuất bản và link.")
                else:
                    try:
                        them_ban_tin(ky_moi.strip(), link_moi.strip(), int(thu_tu_moi))
                        st.success(f"Đã thêm '{ky_moi}' thành công!")
                        st.rerun()
                    except Exception as e:
                        st.error(f"Lỗi khi thêm (có thể tên kỳ đã tồn tại): {e}")

        st.write("---")

        # --- DANH SÁCH / SỬA / XOÁ ---
        st.markdown("### 📋 Danh sách bản tin hiện có")
        danh_sach_hientai = lay_danh_sach_ban_tin()

        if not danh_sach_hientai:
            st.info("Chưa có bản tin nào.")
        else:
            for item in danh_sach_hientai:
                with st.expander(f"📖 {item['ky_xuat_ban']}  (thứ tự: {item['thu_tu']})"):
                    with st.form(f"form_sua_{item['id']}"):
                        ky_sua = st.text_input("Tên kỳ xuất bản", value=item["ky_xuat_ban"], key=f"ky_{item['id']}")
                        link_sua = st.text_input("Link Flipbook", value=item["link"], key=f"link_{item['id']}")
                        thutu_sua = st.number_input(
                            "Thứ tự hiển thị", value=item["thu_tu"], step=1, key=f"thutu_{item['id']}"
                        )
                        c_luu, c_xoa = st.columns(2)
                        with c_luu:
                            luu = st.form_submit_button("💾 Lưu thay đổi")
                        with c_xoa:
                            xoa = st.form_submit_button("🗑️ Xoá bản tin")

                        if luu:
                            try:
                                sua_ban_tin(item["id"], ky_sua.strip(), link_sua.strip(), int(thutu_sua))
                                st.success("Đã cập nhật!")
                                st.rerun()
                            except Exception as e:
                                st.error(f"Lỗi khi cập nhật: {e}")

                        if xoa:
                            try:
                                xoa_ban_tin(item["id"])
                                st.success("Đã xoá!")
                                st.rerun()
                            except Exception as e:
                                st.error(f"Lỗi khi xoá: {e}")
