import os
import subprocess

from core import HackingTool, HackingToolsCollection, console

from rich.panel import Panel
from rich.prompt import Prompt
from rich import box


class FacialFind(HackingTool):
    TITLE = "通过人脸识别系统查找社交媒体"
    DESCRIPTION = "一种社交媒体映射工具，通过人脸识别在不同平台之间关联个人资料。"
    INSTALL_COMMANDS = [
        "sudo apt install -y software-properties-common",
        "sudo add-apt-repository ppa:mozillateam/firefox-next && sudo apt update && sudo apt upgrade",
        "git clone https://github.com/Greenwolf/social_mapper.git",
        "sudo apt install -y build-essential cmake libgtk-3-dev libboost-all-dev",
        "cd social_mapper/setup",
        "sudo python3 -m pip install --no-cache-dir -r requirements.txt",
        '[!]现在你需要手动完成一些设置\n'
        '[!]为你的操作系统安装 Geckodriver\n'
        '[!]复制并粘贴以下链接下载文件作为系统配置\n'
        '[#] https://github.com/mozilla/geckodriver/releases\n'
        '[!!]在 Linux 上你可以将其放在 /usr/bin'
    ]
    PROJECT_URL = "https://github.com/Greenwolf/social_mapper"

    def run(self):
        from config import get_tools_dir
        import subprocess
        setup_dir = get_tools_dir() / "social_mapper" / "setup"
        subprocess.run(["python3", "social_mapper.py", "-h"], cwd=str(setup_dir))
        console.print(
            "[bold magenta]运行前请在 social_mapper.py 中设置用户名和密码。[/]\n"
            "[magenta]用法: python social_mapper.py -f <文件夹> -i <路径> -m fast <账户名称> -fb -tw[/]"
        )


class FindUser(HackingTool):
    TITLE = "通过用户名查找社交媒体"
    DESCRIPTION = "在超过 75 个社交网络中查找用户名"
    INSTALL_COMMANDS = [
        "git clone https://github.com/xHak9x/finduser.git",
        "cd finduser && sudo chmod +x finduser.sh"
    ]
    RUN_COMMANDS = ["cd finduser && sudo bash finduser.sh"]
    PROJECT_URL = "https://github.com/xHak9x/finduser"


class Sherlock(HackingTool):
    TITLE = "Sherlock"
    DESCRIPTION = "通过用户名在社交网络中追踪社交媒体账户\n" \
                  "更多用法:\n" \
                  "\t >>python3 sherlock --help"
    INSTALL_COMMANDS = [
        "git clone https://github.com/sherlock-project/sherlock.git",
        "cd sherlock;sudo python3 -m pip install -r requirements.txt"
    ]
    PROJECT_URL = "https://github.com/sherlock-project/sherlock"

    def run(self):
        from config import get_tools_dir
        from rich.prompt import Prompt
        name = Prompt.ask("输入用户名")
        # Bug 3 修复: os.chdir() 替换为 cwd= 参数
        subprocess.run(
            ["python3", "sherlock", name],
            cwd=str(get_tools_dir() / "sherlock"),
        )


class SocialScan(HackingTool):
    TITLE = "SocialScan | 用户名或邮箱"
    DESCRIPTION = "以 100% 准确率检查在线平台上邮箱地址和用户名的可用性"
    INSTALL_COMMANDS = ["pip install --user socialscan"]
    PROJECT_URL = "https://github.com/iojw/socialscan"

    def run(self):
        name = input(
            "输入用户名或邮箱 (如果两者都有请用空格分隔) >> ")
        subprocess.run(["sudo", "socialscan", f"{name}"])


class SocialMediaFinderTools(HackingToolsCollection):
    TITLE = "社交媒体查找器"
    TOOLS = [
        FacialFind(),
        FindUser(),
        Sherlock(),
        SocialScan()
    ]

if __name__ == "__main__":
    tools = SocialMediaFinderTools()
    tools.show_options()
