import os

from core import HackingTool, HackingToolsCollection, console

from rich.panel import Panel
from rich.text import Text
from rich.prompt import Prompt


class Autopsy(HackingTool):
    TITLE = "Autopsy"
    DESCRIPTION = "Autopsy 是一个网络调查人员使用的平台。\n" \
                  "[!] 适用于任何操作系统\n" \
                  "[!] 从任何操作系统和媒体恢复已删除的文件\n" \
                  "[!] 提取图像元数据"
    RUN_COMMANDS = ["sudo autopsy"]

    def __init__(self):
        super().__init__(installable=False)


class Wireshark(HackingTool):
    TITLE = "Wireshark"
    DESCRIPTION = "Wireshark 是一个网络捕获和分析\n" \
                  "工具，可查看网络中发生的情况。\n" \
                  "并调查网络相关事件"
    RUN_COMMANDS = ["sudo wireshark"]

    def __init__(self):
        super().__init__(installable=False)


class BulkExtractor(HackingTool):
    TITLE = "Bulk extractor"
    DESCRIPTION = "无需解析文件系统即可提取有用信息"
    PROJECT_URL = "https://github.com/simsong/bulk_extractor"
    SUPPORTED_OS = ["linux"]

    def __init__(self):
        super().__init__([
            ('GUI 模式 (需要下载)', self.gui_mode),
            ('命令行模式', self.cli_mode)
        ], installable=False, runnable=False)

    def gui_mode(self):
        import subprocess
        from config import get_tools_dir
        console.print(Panel(Text(self.TITLE, justify="center"), style="bold magenta"))
        console.print("[bold magenta]正在克隆仓库并尝试运行 GUI...[/]")
        tools_dir = get_tools_dir()
        subprocess.run(["git", "clone", "https://github.com/simsong/bulk_extractor.git"],
                       cwd=str(tools_dir))
        be_dir = tools_dir / "bulk_extractor"
        subprocess.run(["./BEViewer"], cwd=str(be_dir / "java_gui"))
        console.print(
            "[magenta]如果克隆后出现错误，请转到 /java_gui/src/ 并编译 .jar 文件 && 运行 ./BEViewer[/]")
        console.print(
            "[magenta]请访问获取有关安装的详细信息: https://github.com/simsong/bulk_extractor[/]")

    def cli_mode(self):
        import subprocess
        console.print(Panel(Text(self.TITLE + " - 命令行模式", justify="center"), style="bold magenta"))
        subprocess.run(["sudo", "apt", "install", "-y", "bulk-extractor"])
        console.print("[magenta]bulk_extractor [选项] imagefile[/]")
        subprocess.run(["bulk_extractor", "-h"])


class Guymager(HackingTool):
    TITLE = "磁盘克隆和 ISO 镜像获取"
    DESCRIPTION = "Guymager 是一个免费的媒体取证映像器。"
    SUPPORTED_OS = ["linux"]
    INSTALL_COMMANDS = ["sudo apt install guymager"]
    RUN_COMMANDS = ["sudo guymager"]
    PROJECT_URL = "https://guymager.sourceforge.io/"



class Toolsley(HackingTool):
    TITLE = "Toolsley"
    DESCRIPTION = "Toolsley 提供十多个有用的调查工具。\n" \
                  "[+] 文件签名验证器\n" \
                  "[+] 文件识别器\n" \
                  "[+] 哈希和验证\n" \
                  "[+] 二进制检查器\n" \
                  "[+] 文本编码\n" \
                  "[+] 数据 URI 生成器\n" \
                  "[+] 密码生成器"
    PROJECT_URL = "https://www.toolsley.com/"

    def __init__(self):
        super().__init__(installable=False, runnable=False)


class Volatility3(HackingTool):
    TITLE = "Volatility 3 (内存取证)"
    DESCRIPTION = (
        "世界上最常用的内存取证框架。\n"
        "用法: python3 vol.py -f memory.dmp windows.pslist"
    )
    INSTALL_COMMANDS = [
        "git clone https://github.com/volatilityfoundation/volatility3.git",
        "cd volatility3 && pip install --user -r requirements.txt",
    ]
    PROJECT_URL = "https://github.com/volatilityfoundation/volatility3"

    def run(self):
        from config import get_tools_dir
        import subprocess
        from rich.prompt import Prompt
        dump = Prompt.ask("输入内存转储路径")
        plugin = Prompt.ask("输入插件", default="windows.pslist")
        subprocess.run(
            ["python3", "vol.py", "-f", dump, plugin],
            cwd=str(get_tools_dir() / "volatility3"),
        )


class Binwalk(HackingTool):
    TITLE = "Binwalk (固件分析)"
    DESCRIPTION = (
        "分析、逆向工程和提取固件镜像。\n"
        "用法: binwalk -e firmware.bin"
    )
    INSTALL_COMMANDS = ["pip install --user binwalk"]
    RUN_COMMANDS = ["binwalk --help"]
    PROJECT_URL = "https://github.com/ReFirmLabs/binwalk"


class Pspy(HackingTool):
    TITLE = "pspy (进程监控器 - 无需 Root)"
    DESCRIPTION = "无需 root 即可监控 Linux 进程 - 检测 cron 作业、计划任务、其他用户的命令。"
    INSTALL_COMMANDS = [
        "curl -sSL https://github.com/DominicBreuker/pspy/releases/latest/download/pspy64 -o pspy",
        "chmod +x pspy",
    ]
    RUN_COMMANDS = ["./pspy --help"]
    PROJECT_URL = "https://github.com/DominicBreuker/pspy"
    SUPPORTED_OS = ["linux"]


class ForensicTools(HackingToolsCollection):
    TITLE = "取证工具"
    TOOLS = [
        Autopsy(),
        Wireshark(),
        BulkExtractor(),
        Guymager(),
        Toolsley(),
        Volatility3(),
        Binwalk(),
        Pspy(),
    ]

if __name__ == "__main__":
    tools = ForensicTools()
    tools.show_options()
