# 从零开始构建 ReAct Agent

## 这个项目是关于什么的？
本项目基于ReAct思想实现了一个 AI Agent 自主代理，主要用于电商客服的智能接待问答。

## 架构
![架构图](https://muyu001.oss-cn-beijing.aliyuncs.com/img/2024-09-19-1024.png)


## 先决条件
- Python >= 3.10
- 掌握 OpenAI API 调用在线 GPT 模型 或者 Ollama 本地部署并使用开源大模型

## 步骤

1. **虚拟环境设置：**
   - 创建一个专用的虚拟环境：
   
     ```bash
     conda create --name react_ai_agent python==3.11
     ```
   - 激活环境：
     ```bash
     conda activate --name react_ai_agent
     ```

2. **安装项目依赖：**

   - 导航到项目目录，并使用 `pip` 安装所需的包：
   
     ```bash
     pip install -r requirements.txt
     ```

3. **修改配置文件：**

   - 如果使用 OpenAI API，新建 .env 文件，内容如下
        ```bash
     API_KEY="xxxxx"
     ```
   - 如果使用Ollama托管的开源模型，请确保可以正常访问 Ollama RestFul API 接口，并将 config.json配置文件中的 `use_model` 设置为 true

4. **运行 ReAct Agent 代理**

   ```bash 
   # 运行 Re-Act AI 代理进行财务分析
   python main.py   
   ```