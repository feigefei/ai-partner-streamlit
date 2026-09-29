# AI 智能伴侣

这是学习黑马程序员课程过程中完成的 Python 项目，使用 Streamlit 构建界面，通过 OpenAI Python SDK 调用 DeepSeek API。

## 功能

- 聊天界面与流式回复。
- 自定义 AI 伴侣的昵称和性格。
- 多轮对话上下文。
- 创建、保存、加载和删除本地历史会话。

## 运行

以下命令在项目根目录执行。原开发环境使用 Python 3.13，依赖版本记录在 `requirements.txt` 中。

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
$env:DEEPSEEK_API_KEY = "替换为你自己的 DeepSeek API Key"
.\.venv\Scripts\python.exe -m streamlit run ai_partner_3.py
```

macOS / Linux：

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
export DEEPSEEK_API_KEY="替换为你自己的 DeepSeek API Key"
.venv/bin/python -m streamlit run ai_partner_3.py
```

浏览器打开终端中显示的本地地址即可使用。API Key 必须在启动前配置到环境变量；代码没有自动加载 `.env` 的逻辑。调用模型需要网络和可用的 DeepSeek API 账户。

当前代码使用 `deepseek-v4-pro`，并配置了思考模式相关参数；是否可用取决于服务端及账户支持情况，可根据实际使用的 API 修改调用参数。

## 文件说明

| 文件 | 说明 |
| --- | --- |
| `ai_partner_3.py` | 完整版入口，包含历史会话管理 |
| `ai_partner_2.py` | 中间版本，包含角色设置、多轮对话和流式输出 |
| `ai_partner_1.py` | 最初版本，展示基本聊天界面和单次模型调用 |
| `deepseek调用.py` | DeepSeek API 调用练习 |
| `resources/` | 界面图片 |

历史会话由程序保存到运行目录下的 `sessions/`，其中包含聊天内容。

这是个人课程学习项目,完整应用请从 `ai_partner_3.py` 启动。会话使用本地文件保存，没有多用户隔离或登录功能。

