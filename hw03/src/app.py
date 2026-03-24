import streamlit as st
import face_recognition
import numpy as np
from PIL import Image, ImageDraw

# 设置页面标题和图标
st.set_page_config(page_title="面部识别应用", page_icon="📷")

st.title("📷 简单面部识别应用")
st.write("请选择一张图片")

# 文件上传器
uploaded_file = st.file_uploader("Drag and drop file here", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # 加载图片
    image = Image.open(uploaded_file)
    st.image(image, caption='上传的图片', use_column_width=True)
    
    # 转换为 numpy 数组供 face_recognition 使用
    image_array = np.array(image)
    
    # 检测人脸位置
    face_locations = face_recognition.face_locations(image_array)
    
    if len(face_locations) == 0:
        st.warning("未检测到人脸 😢")
    else:
        st.success(f"✅ 检测到 {len(face_locations)} 张人脸！")
        
        # 创建绘图对象
        draw = ImageDraw.Draw(image)
        
        # 遍历每个人脸，画红框
        for (top, right, bottom, left) in face_locations:
            # 画红色矩形框 (宽度=4像素)
            draw.rectangle([left, top, right, bottom], outline="red", width=4)
            # 可选：标注坐标
            draw.text((left, top - 10), f"({left},{top})", fill="red")
        
        # 显示带红框的图片
        st.image(image, caption='检测结果（红框标示）', use_column_width=True)
        
        # 显示坐标信息
        st.write("📍 人脸坐标位置：")
        for i, (top, right, bottom, left) in enumerate(face_locations):
            st.write(f"人脸 {i+1}: 上={top}, 右={right}, 下={bottom}, 左={left}")