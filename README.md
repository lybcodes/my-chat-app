# My Chat App

My Chat App 是一个基于通义千问（Qwen）的开源聊天机器人应用。它支持通过页面或 REST API 与通义千问大模型交互，并且可以轻松部署在本地环境中。

## 功能特性

- **基于通义千问**：使用阿里巴巴集团的超大规模语言模型（Qwen）。
- **多交互方式**：
  - 页面访问：启动后在web页面中与机器人对话。
  - REST API 接口：支持与其他系统集成。
- **易于部署**：支持 pip 安装和本地运行。
- **可扩展性**：可以根据需求替换模型或添加更多功能。

---

## 快速开始

### **1. 环境准备**

确保你的开发环境满足以下条件：
- **Python 版本**：Python 3.7 或更高版本。
- **操作系统**：支持 Windows、macOS 和 Linux。
- **网络连接**：需要访问阿里云的服务以调用通义千问 API。

---

### **2. 安装依赖**

#### **克隆项目**
如果你是从源码安装，请先克隆项目：
```bash
git clone https://github.com/lybcodes/my-chat-app.git
cd my-chat-app
```
#### **安装依赖**
在项目根目录下运行以下命令，安装所需的 Python 包：
```bash
pip install -r requirements.txt
```

### **3. 配置 API 密钥**

通义千问需要一个有效的 API 密钥才能工作。你需要从阿里云获取 API 密钥，并将其设置为环境变量。

获取 API 密钥:

1. 登录 阿里云控制台
2. 进入 [百炼平台](https://bailian.console.aliyun.com)，找到你的 API 密钥。
3. 复制 API 密钥（例如：sk-xxx）替换代码modle.py中的api_key。（或者将api_key设置为环境变量，每次只需更改环境变量即可）

### **4. 启动服务**

运行以下命令启动应用：
```bash
 export DASHSCOPE_API_KEY=sk-xxx # 替换自己的API_KEY
 uvicorn my_chat_app.app:app --reload
```
如果一切正常，你会看到类似以下的日志输出：
```text
INFO:     Will watch for changes in these directories: ['/Users/lyb/projects/my-test/my-chat-app']
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [95693] using StatReload
INFO:     Started server process [95695]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     127.0.0.1:55672 - "GET / HTTP/1.1" 200 OK
INFO:     127.0.0.1:55672 - "GET /static/script.js HTTP/1.1" 200 OK
INFO:     127.0.0.1:55709 - "POST /chat HTTP/1.1" 200 OK

```
此时，服务已经启动，监听在 http://127.0.0.1:8080。

### **5. 使用方法**

#### **页面交互**
本地访问 http://127.0.0.1:8080，开始与通义千问交互：

![本地图片](my_chat_app/static/img.png)

#### **REST API 测试**
如果你希望通过 REST API 测试聊天功能，可以使用 curl 或 Postman 发送请求。

- 发送请求

运行以下命令：
```bash
curl -X POST http://127.0.0.1:8000/chat \
     -H "Content-Type: application/json" \
     -d '{"message": "你好"}'

```
- 响应

你会收到类似以下的 JSON 响应：
```json
{
  "response": "你好！我是通义千问，阿里巴巴集团旗下的超大规模语言模型。有什么可以帮你的吗？"
}
```
### **6. 常见问题排查**
问题 1：服务无法启动
- 原因：端口被占用或其他依赖未安装。
- 解决方法： 
    - 检查端口占用情况：
  ```bash
  lsof -i :8080
  ```
  - 杀死占用端口的进程：
  ```bash
  kill <PID>
  ```
  - 确保所有依赖已正确安装。

问题 2：响应时间过长

- 原因：网络延迟或通义千问服务繁忙。
- 解决方法：
    - 检查网络连接是否正常。
    - 如果问题持续，请稍后再试。

### **7. 贡献与反馈**
如果你对项目有任何改进建议或发现 Bug，请随时提交 Issue 或 Pull Request：

GitHub 地址：https://github.com/lybcodes/my-chat-app.git

### **8. 许可证**
本项目采用 MIT 许可证。详情请参阅 LICENSE 文件。


希望这份文档能够帮助你快速上手自己的 AI 聊天应用！如果有任何其他需求或需要进一步优化文档，请随时告诉我！

