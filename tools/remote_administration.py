from core import HackingTool, HackingToolsCollection, console

from rich.panel import Panel
from rich.prompt import Prompt


# Bug 17 修复: Stitch 在 payload_creator.py 和 remote_administration.py 中都有定义。
# 保留在 payload_creator.py (其正确类别) 并从此处删除。


class Pyshell(HackingTool):
    TITLE = "Pyshell"
    DESCRIPTION = "Pyshell 是一个 RAT 工具，能够下载和上传\n" \
                  "文件、执行操作系统命令等.."
    INSTALL_COMMANDS = [
        "git clone https://github.com/knassar702/Pyshell.git;"
        "pip install --user pyscreenshot python-nmap requests"
    ]
    RUN_COMMANDS = ["cd Pyshell;./Pyshell"]
    PROJECT_URL = "https://github.com/knassar702/pyshell"


class RemoteAdministrationTools(HackingToolsCollection):
    TITLE = "远程管理工具 (RAT)"
    TOOLS = [
        Pyshell()
    ]

if __name__ == "__main__":
    tools = RemoteAdministrationTools()
    tools.show_options()
