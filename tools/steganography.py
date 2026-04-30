import subprocess

from core import HackingTool, HackingToolsCollection, console
from core import validate_input

from rich.panel import Panel
from rich.prompt import Prompt


class SteganoHide(HackingTool):
    TITLE = "SteganoHide"
    INSTALL_COMMANDS = ["sudo apt-get install steghide -y"]

    def run(self):
        choice_run = input(
            "[1] 隐藏\n"
            "[2] 提取\n"
            "[99] 取消\n"
            ">> "
        )
        choice_run = validate_input(choice_run, [1, 2, 99])
        if choice_run is None:
            console.print("[bold red]请输入有效选项[/bold red]")
            return self.run()

        if choice_run == 99:
            return

        if choice_run == 1:
            file_hide = input("输入要嵌入的文件名 (1.txt) >> ")
            file_to_be_hide = input("输入封面文件名 (test.jpeg) >> ")
            subprocess.run(["steghide", "embed", "-cf", file_to_be_hide, "-ef", file_hide])

        elif choice_run == 2:
            from_file = input("输入要提取数据的文件名 >> ")
            subprocess.run(["steghide", "extract", "-sf", from_file])


class StegnoCracker(HackingTool):
    TITLE = "StegnoCracker"
    DESCRIPTION = "SteganoCracker 使用暴力破解实用程序揭示文件中隐藏的数据"
    INSTALL_COMMANDS = ["pip3 install stegcracker && pip3 install stegcracker -U --force-reinstall"]

    def run(self):
        filename = input("输入文件名 >> ")
        passfile = input("输入密码字典文件名 >> ")
        subprocess.run(["stegcracker", filename, passfile])


class StegoCracker(HackingTool):
    TITLE = "StegoCracker"
    DESCRIPTION = "StegoCracker 允许您在图像或音频文件中隐藏和检索数据"
    INSTALL_COMMANDS = [
        "git clone https://github.com/W1LDN16H7/StegoCracker.git",
        "sudo chmod -R 755 StegoCracker"
    ]
    RUN_COMMANDS = [
        "cd StegoCracker && python3 -m pip install -r requirements.txt",
        "./install.sh"
    ]
    PROJECT_URL = "https://github.com/W1LDN16H7/StegoCracker"


class Whitespace(HackingTool):
    TITLE = "Whitespace"
    DESCRIPTION = "使用空白字符和 Unicode 字符进行隐写术"
    INSTALL_COMMANDS = [
        "git clone https://github.com/beardog108/snow10.git",
        "sudo chmod -R 755 snow10"
    ]
    RUN_COMMANDS = ["cd snow10 && ./install.sh"]
    PROJECT_URL = "https://github.com/beardog108/snow10"


class SteganographyTools(HackingToolsCollection):
    TITLE = "隐写术工具"
    TOOLS = [SteganoHide(), StegnoCracker(), StegoCracker(), Whitespace()]

if __name__ == "__main__":
    tools = SteganographyTools()
    tools.show_options()
