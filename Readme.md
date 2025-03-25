### 🤖 Assistant


# SCUNET 校园网自动登录脚本

这是一个基于 Selenium 的自动登录脚本，用于自动登录 SCUNET 校园网。通过输入用户名、密码以及选择服务类型，脚本可以自动化完成登录过程，适合需要频繁登录校园网的用户。

## 功能特性

- **自动输入用户名和密码**：无需手动输入用户名和密码。
- **选择服务类型**：支持选择校园网、联通、电信、移动等不同服务类型。
- **兼容性强**：使用 Selenium 作为核心工具，支持主流浏览器（如 Edge、Chrome、Firefox 等）。
- **简化操作**：一键运行，快速登录。

## 环境要求

- Python 3.x
- Selenium 库
- Edge 浏览器（或其他支持的浏览器）
- Edge WebDriver（与浏览器版本匹配）

## 安装步骤

1. **克隆项目**：
   ```bash
   git clone https://github.com/Eli-Zxh/SCUNET_login_in.git
   ```

2. **安装依赖**：
   ```bash
   pip install requests
   ```

3.**修改脚本**：
   打开 `request_way.py` 文件，填写你的校园网用户名和密码：
   ```python
   user_name = '你的用户名'
   user_pwd = '你的密码'
   target_service_value = '校园网'  # 选择你使用的服务类型
   ```

4.**运行脚本**：
   ```bash
   python request_way.py
   ```

5.**设置自动运行脚本**：
   以linux为例：
   ```bash
   crontab -e
   */5 * * * * /usr/bin/python3 /path/to/your/SCUNET_requests.py # 在文件末尾添加以下内容，设置每五分钟自动执行
   #保存并退出
   ```
   Windows系统可以自行设置计划任务程序

## 如果你需要用到selenium控制浏览器

（不太建议，奇怪的bug，配置复杂）

1. **克隆项目**：
   ```bash
   git clone https://github.com/Eli-Zxh/SCUNET_login_in.git
   ```

2. **安装依赖**：
   ```bash
   pip install requests
   ```

3. **配置 WebDriver**：
   - 下载与 Edge 浏览器版本匹配的 [Edge WebDriver](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/)。
   - 将 WebDriver 可执行文件路径添加到系统环境变量中。

4. **修改脚本**：
   打开 `SCUNET.py` 文件，填写你的校园网用户名和密码：
   ```python
   user_name = '你的用户名'
   user_pwd = '你的密码'
   target_service_value = '校园网'  # 选择你使用的服务类型
   ```

5. **运行脚本**：
   ```bash
   python SCUNET.py
   ```

## 使用说明

1. 确保浏览器和 WebDriver 已正确配置。
2. 运行脚本后，浏览器会自动打开校园网登录页面，并自动填写用户名、密码，选择服务类型，最后点击登录按钮。
3. 登录成功后，浏览器会自动关闭。

## 项目结构

```
SCUNET_login_in/
├── SCUNET.py           # 使用selenium的备份
├── request_way.py      # 主脚本文件
├── README.md           # 项目介绍
├── LICENSE             # MIT证书
```

## 注意事项

- 确保用户名和密码正确。
- 如果使用了浏览器登录：
   - WebDriver 版本必须与浏览器版本匹配。
   - 如果登录页面结构发生变化，可能需要调整脚本中的元素定位方式。
   - 目前没完成图形验证码功能。

## 贡献

欢迎提交 Issue 或 PR 来改进此项目。如果你有任何问题或建议，请通过 1796313642@qq.com 联系我。

## 许可证

本项目基于 [MIT License](LICENSE) 开源。
```
