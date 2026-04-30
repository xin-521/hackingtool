import os
import subprocess

from core import HackingTool, HackingToolsCollection, console


class TheFatRat(HackingTool):
    TITLE = "The FatRat"
    SUPPORTED_OS = ["linux"]
    DESCRIPTION = (
        "TheFatRat 提供了一种简单的方法来创建后门和 payload，\n"
        "可以绕过大多数防病毒软件。"
    )
    INSTALL_COMMANDS = [
        "git clone https://github.com/Screetsec/TheFatRat.git",
        "cd TheFatRat && chmod +x setup.sh",
    ]
    RUN_COMMANDS = ["cd TheFatRat && sudo bash setup.sh"]
    PROJECT_URL = "https://github.com/Screetsec/TheFatRat"

    def __init__(self):
        super().__init__([
            ("更新", self.update),
            ("故障排除", self.troubleshoot),
        ])

    def update(self):
        from config import get_tools_dir
        cwd = str(get_tools_dir() / "TheFatRat")
        subprocess.run(["bash", "update"], cwd=cwd)
        subprocess.run(["chmod", "+x", "setup.sh"], cwd=cwd)
        subprocess.run(["bash", "setup.sh"], cwd=cwd)

    def troubleshoot(self):
        from config import get_tools_dir
        cwd = str(get_tools_dir() / "TheFatRat")
        subprocess.run(["chmod", "+x", "chk_tools"], cwd=cwd)
        subprocess.run(["./chk_tools"], cwd=cwd)


class Brutal(HackingTool):
    TITLE = "Brutal"
    SUPPORTED_OS = ["linux"]
    DESCRIPTION = (
        "Brutal 是一个工具包，可快速创建各种 payload、powershell 攻击、\n"
        "病毒攻击并为人类接口设备启动监听器。"
    )
    INSTALL_COMMANDS = [
        "git clone https://github.com/Screetsec/Brutal.git",
        "cd Brutal && chmod +x Brutal.sh",
    ]
    RUN_COMMANDS = ["cd Brutal && sudo bash Brutal.sh"]
    PROJECT_URL = "https://github.com/Screetsec/Brutal"

    def show_info(self):
        super().show_info()
        console.print(
            "[bold cyan]要求:[/bold cyan]\n"
            "  - Arduino 软件 (v1.6.7+)\n"
            "  - TeensyDuino\n"
            "  - Linux udev 规则\n"
            "  参见: https://github.com/Screetsec/Brutal/wiki/Install-Requirements"
        )


class Stitch(HackingTool):
    TITLE = "Stitch"
    SUPPORTED_OS = ["linux"]
    DESCRIPTION = (
        "Stitch 是一个跨平台 Python 远程管理工具。\n"
        "[!] 有关 Windows 和 macOS 支持，请参阅项目链接。"
    )
    INSTALL_COMMANDS = [
        "git clone https://github.com/nathanlopez/Stitch.git",
        "cd Stitch && pip install --user -r lnx_requirements.txt",
    ]
    RUN_COMMANDS = ["cd Stitch && sudo python3 main.py"]
    PROJECT_URL = "https://nathanlopez.github.io/Stitch"


class MSFVenom(HackingTool):
    TITLE = "MSFvenom Payload 创建器"
    SUPPORTED_OS = ["linux"]
    DESCRIPTION = (
        "MSFvenom Payload Creator (MSFPC) 是一个包装器，\n"
        "根据用户选择生成多种类型的 payload。"
    )
    INSTALL_COMMANDS = [
        "git clone https://github.com/g0tmi1k/msfpc.git",
        "cd msfpc && chmod +x msfpc.sh",
    ]
    RUN_COMMANDS = ["cd msfpc && sudo bash msfpc.sh -h -v"]
    PROJECT_URL = "https://github.com/g0tmi1k/msfpc"


class Venom(HackingTool):
    TITLE = "Venom Shellcode 生成器"
    SUPPORTED_OS = ["linux"]
    DESCRIPTION = "Venom 利用 apache2 web 服务器通过虚假网页传递 LAN payload。"
    INSTALL_COMMANDS = [
        "git clone https://github.com/r00t-3xp10it/venom.git",
        # 删除了 "sudo ./venom.sh -u" - 交互式，在安装过程中运行工具
        "sudo chmod -R 775 venom*/ && cd venom*/ && cd aux && sudo bash setup.sh",
    ]
    RUN_COMMANDS = ["cd venom && sudo ./venom.sh"]
    PROJECT_URL = "https://github.com/r00t-3xp10it/venom"


class Spycam(HackingTool):
    TITLE = "Spycam"
    DESCRIPTION = "生成 Win32 payload，每 1 分钟捕获一次网络摄像头图像。"
    INSTALL_COMMANDS = [
        "git clone https://github.com/indexnotfound404/spycam.git",
        "cd spycam && bash install.sh && chmod +x spycam",
    ]
    RUN_COMMANDS = ["cd spycam && ./spycam"]
    PROJECT_URL = "https://github.com/indexnotfound404/spycam"


class MobDroid(HackingTool):
    TITLE = "Mob-Droid"
    SUPPORTED_OS = ["linux"]
    DESCRIPTION = "轻松生成 metasploit payload，无需输入长命令。"
    INSTALL_COMMANDS = ["git clone https://github.com/kinghacker0/mob-droid.git"]
    RUN_COMMANDS = ["cd mob-droid && sudo python3 mob-droid.py"]
    PROJECT_URL = "https://github.com/kinghacker0/Mob-Droid"


class Enigma(HackingTool):
    TITLE = "Enigma"
    SUPPORTED_OS = ["linux"]
    DESCRIPTION = "Enigma 是一个多平台 payload 投放器。"
    INSTALL_COMMANDS = ["git clone https://github.com/UndeadSec/Enigma.git"]
    RUN_COMMANDS = ["cd Enigma && sudo python3 enigma.py"]
    PROJECT_URL = "https://github.com/UndeadSec/Enigma"


class PayloadCreatorTools(HackingToolsCollection):
    TITLE = "Payload 创建工具"
    # Bug 11 修复: show_options() 覆盖缺少 `parent` 参数 -
    # 整个覆盖现在已删除，改用基类方法。
    TOOLS = [
        TheFatRat(),
        Brutal(),
        Stitch(),
        MSFVenom(),
        Venom(),
        Spycam(),
        MobDroid(),
        Enigma(),
    ]


if __name__ == "__main__":
    tools = PayloadCreatorTools()
    tools.show_options()
