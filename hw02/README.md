# 实验二：论文导读 + DeepSeek Chatbot
## 运行Chatbot示例

### 方法一：使用火山引擎
1. 注册火山引擎并创建DeepSeek模型接入点
2. 复制.env.example为.env
3. 在.env中填写你的ARK_API_KEY、BOT_ID和ENDPOINT_ID
4. 安装依赖：`pip install -r requirements.txt`
5. 运行：`python chatbot_deepseek.py`

### 方法二：使用DeepSeek官方API
1. 获取DeepSeek API Key
2. 在.env中设置DEEPSEEK_API_KEY和API_PLATFORM=deepseek
3. 安装依赖并运行

### 示例输入/输出
👤 你: 介绍一下皮肤癌分割任务
🤖 Bot: 皮肤癌分割是医学图像处理中的重要任务...
