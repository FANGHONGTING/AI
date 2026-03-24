# 📷 简单面部识别应用

## 项目结构
- src/app.py : 主程序代码
- requirements.txt : 依赖包列表
- README.md : 说明文档

## 功能说明
本项目是一个基于 Streamlit 和 face_recognition 的简单人脸检测应用。
1. 用户上传图片。
2. 系统自动检测图中的人脸。
3. 在原图上用红色方框标出人脸位置，并显示坐标。

## 运行方式
1. 安装依赖：pip install -r requirements.txt
2. 运行程序：streamlit run src/app.py
3. 在浏览器打开 http://localhost:8501