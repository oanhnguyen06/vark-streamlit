
import streamlit as st

st.set_page_config(page_title="VARK Learning Style", layout="centered")

st.title("Ứng dụng xác định phong cách học tập VARK cho sinh viên")
st.markdown("#### Chào mừng bạn đến với công cụ xác định phong cách học tập VARK!")
st.write(
    """
    Mô hình VARK phân loại người học theo 4 kiểu:
    - **V (Visual)**: Học qua hình ảnh, biểu đồ.
    - **A (Aural)**: Học qua âm thanh, thảo luận.
    - **R (Read/Write)**: Học qua chữ viết, tài liệu.
    - **K (Kinesthetic)**: Học qua trải nghiệm, vận động.

    👉 Ứng dụng này sẽ giúp bạn hiểu rõ hơn về kiểu học của bản thân và cách phát triển tối đa năng lực học tập.
    """
)

st.markdown("### 🔍 Chức năng chính (sẽ cập nhật thêm):")
st.write("- Hiển thị kết quả khảo sát VARK")
st.write("- Gợi ý chiến lược học tập theo kiểu V, A, R, K")
st.write("- Phân tích kết quả theo giới tính, ngành học (khi kết nối dữ liệu)")

st.success("👉 Bạn có thể mở rộng thêm nhiều tính năng như biểu đồ, nhập liệu, và tải kết quả!")

