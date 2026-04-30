import contextlib
import os
import subprocess

from core import HackingTool, HackingToolsCollection, console

from rich.panel import Panel
from rich.prompt import Prompt
from rich import box


class InstaBrute(HackingTool):
    TITLE = "Instagram 攻击"
    DESCRIPTION = "针对 Instagram 的暴力破解攻击"
    PROJECT_URL = "https://github.com/chinoogawa/instaBrute"
    # Py3-7: Python 2 only (pip2.7); also violates Instagram ToS
    ARCHIVED = True
    ARCHIVED_REASON = "仅支持 Python 2 - 已于 2020 年 1 月停止维护。仓库自 2017 年以来未更新。"
    INSTALL_COMMANDS = []
    RUN_COMMANDS = []

    def __init__(self):
        super().__init__(installable=False, runnable=False)


class BruteForce(HackingTool):
    TITLE = "社交媒体综合攻击"
    DESCRIPTION = "暴力破解攻击 Gmail、Hotmail、Twitter、Facebook、Netflix\n" \
                  "[!] python3 Brute_Force.py -g <Account@gmail.com> -l <File_list>"
    INSTALL_COMMANDS = [
        "git clone https://github.com/Matrix07ksa/Brute_Force.git",
        "cd Brute_Force;sudo pip3 install proxylist;pip3 install mechanize"
    ]
    RUN_COMMANDS = ["cd Brute_Force;python3 Brute_Force.py -h"]
    PROJECT_URL = "https://github.com/Matrix07ksa/Brute_Force"


class Faceshell(HackingTool):
    TITLE = "Facebook 攻击"
    DESCRIPTION = "Facebook 暴力破解工具"
    INSTALL_COMMANDS = [
        "git clone https://github.com/Matrix07ksa/Brute_Force.git",
        "cd Brute_Force;sudo pip3 install proxylist;pip3 install mechanize"
    ]
    PROJECT_URL = "https://github.com/Matrix07ksa/Brute_Force"

    def run(self):
        from config import get_tools_dir
        name = Prompt.ask("输入用户名")
        wordlist = Prompt.ask("输入字典文件路径")
        # Bug 3 修复: os.chdir() 替换为 cwd= 参数
        subprocess.run(
            ["python3", "Brute_Force.py", "-f", name, "-l", wordlist],
            cwd=str(get_tools_dir() / "Brute_Force"),
        )


class AppCheck(HackingTool):
    TITLE = "应用程序检查器"
    DESCRIPTION = "通过链接检查目标设备上是否安装了某个应用程序的工具。"
    INSTALL_COMMANDS = [
        "git clone https://github.com/jakuta-tech/underhanded.git",
        "cd underhanded && sudo chmod +x underhanded.sh"
    ]
    RUN_COMMANDS = ["cd underhanded;sudo bash underhanded.sh"]
    PROJECT_URL = "https://github.com/jakuta-tech/underhanded"


class SocialMediaBruteforceTools(HackingToolsCollection):
    TITLE = "社交媒体暴力破解"
    TOOLS = [
        InstaBrute(),
        BruteForce(),
        Faceshell(),
        AppCheck()
    ]

if __name__ == "__main__":
    tools = SocialMediaBruteforceTools()
    tools.show_options()
