import whisper

def main():
    print("正在加载模型...")
    # 加载模型（可改为 base, small, medium, large）
    model = whisper.load_model("tiny")
    
    print("正在识别音频...")
    # 识别音频文件
    result = model.transcribe("voice.mp3", language="zh")
    
    print("\n===== 识别结果 =====")
    print(result["text"])
    print("===================\n")
    
    # 保存结果到文件
    with open("result.txt", "w", encoding="utf-8") as f:
        f.write(result["text"])
    
    print("结果已保存到 result.txt")

if __name__ == "__main__":
    main()
