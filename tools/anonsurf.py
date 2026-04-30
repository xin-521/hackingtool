import os

from core import HackingTool, HackingToolsCollection, console


class AnonymouslySurf(HackingTool):
    TITLE = "匿名冲浪"
    DESCRIPTION = (
        "系统关闭时自动覆盖 RAM 内容\n"
        "并更改您的 IP 地址。"
    )
    # Bug 28 修复: 原来是 "cd kali-anonsurf && ./installer.sh && cd .. && sudo rm -r kali-anonsurf"
    # 安装时删除源意味着如果安装失败无法重试。
    # 现在保留在单独的步骤中，失败不会破坏源。
    INSTALL_COMMANDS = [
        "git clone https://github.com/Und3rf10w/kali-anonsurf.git",
        "cd kali-anonsurf && sudo ./installer.sh",
    ]
    RUN_COMMANDS = ["sudo anonsurf start"]
    PROJECT_URL = "https://github.com/Und3rf10w/kali-anonsurf"
    SUPPORTED_OS = ["linux"]

    def __init__(self):
        super().__init__([("停止", self.stop)])

    def stop(self):
        import subprocess
        console.print("[bold magenta]正在停止匿名冲浪...[/bold magenta]")
        subprocess.run(["sudo", "anonsurf", "stop"])


class Multitor(HackingTool):
    TITLE = "多 Tor"
    DESCRIPTION = "如何同时存在于多个地方。"
    INSTALL_COMMANDS = [
        "git clone https://github.com/trimstray/multitor.git",
        "cd multitor && sudo bash setup.sh install",
    ]
    RUN_COMMANDS = [
        "multitor --init 2 --user debian-tor --socks-port 9000 --control-port 9900 --proxy privoxy --haproxy"
    ]
    PROJECT_URL = "https://github.com/trimstray/multitor"
    SUPPORTED_OS = ["linux"]

    def __init__(self):
        super().__init__(runnable=False)


class AnonSurfTools(HackingToolsCollection):
    TITLE = "匿名隐藏工具"
    TOOLS = [
        AnonymouslySurf(),
        Multitor(),
    ]


if __name__ == "__main__":
    tools = AnonSurfTools()
    tools.show_options()
