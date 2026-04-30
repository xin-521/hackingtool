import subprocess

from core import HackingTool, HackingToolsCollection, console

from rich.panel import Panel
from rich.prompt import Prompt


class AndroGuard(HackingTool):
    TITLE = "Androguard"
    DESCRIPTION = "Androguard 是一个逆向工程、恶意软件和良性应用\n" \
                  "分析工具，用于分析 Android 应用程序等"
    INSTALL_COMMANDS = ["sudo pip3 install -U androguard"]
    PROJECT_URL = "https://github.com/androguard/androguard "

    def __init__(self):
        super().__init__(runnable=False)


class Apk2Gold(HackingTool):
    TITLE = "Apk2Gold"
    SUPPORTED_OS = ["linux"]
    DESCRIPTION = "Apk2Gold 是一个用于将 Android 应用反编译为 Java 的命令行工具"
    INSTALL_COMMANDS = [
        "git clone https://github.com/lxdvs/apk2gold.git",
        "cd apk2gold;sudo bash make.sh"
    ]
    PROJECT_URL = "https://github.com/lxdvs/apk2gold "

    def run(self):
        uinput = input("输入 (.apk) 文件 >> ")
        subprocess.run(["sudo", "apk2gold", uinput])


class Jadx(HackingTool):
    TITLE = "JadX"
    DESCRIPTION = "Jadx 是 Dex 到 Java 的反编译器。\n" \
                  "[*] 将 APK、dex、aar 和 zip 文件中的 Dalvik 字节码反编译为 Java 类\n" \
                  "[*] 从 resources.arsc 解码 AndroidManifest.xml 和其他资源"
    INSTALL_COMMANDS = [
        "git clone https://github.com/skylot/jadx.git",
        # Bug 30 修复: gradlew dist 需要 Java - 先检查
        "java -version 2>&1 | grep -q 'version' && cd jadx && ./gradlew dist || echo '[错误] 未找到 Java。安装: sudo apt install default-jdk'",
    ]
    PROJECT_URL = "https://github.com/skylot/jadx"
    REQUIRES_JAVA = True

    def __init__(self):
        # Py3-4 修复: super(Jadx, self) → super()
        super().__init__(runnable=False)


class Ghidra(HackingTool):
    TITLE = "Ghidra (NSA 逆向工程)"
    DESCRIPTION = "NSA 的软件逆向工程框架 - 反汇编、反编译、脚本编写。"
    REQUIRES_JAVA = True
    INSTALL_COMMANDS = [
        "sudo apt-get install -y ghidra || echo '从 https://ghidra-sre.org/ 下载'",
    ]
    RUN_COMMANDS = ["ghidra --help || echo '运行: ghidraRun'"]
    PROJECT_URL = "https://github.com/NationalSecurityAgency/ghidra"
    SUPPORTED_OS = ["linux", "macos"]


class Radare2(HackingTool):
    TITLE = "Radare2 (逆向工程框架)"
    DESCRIPTION = "便携式 UNIX 类逆向工程框架和命令行工具集。"
    INSTALL_COMMANDS = [
        "git clone https://github.com/radareorg/radare2.git",
        "cd radare2 && sys/install.sh",
    ]
    RUN_COMMANDS = ["r2 -h"]
    PROJECT_URL = "https://github.com/radareorg/radare2"
    SUPPORTED_OS = ["linux", "macos"]


class ReverseEngineeringTools(HackingToolsCollection):
    TITLE = "逆向工程工具"
    TOOLS = [
        AndroGuard(),
        Apk2Gold(),
        Jadx(),
        Ghidra(),
        Radare2(),
    ]

if __name__ == "__main__":
    tools = ReverseEngineeringTools()
    tools.show_options()
