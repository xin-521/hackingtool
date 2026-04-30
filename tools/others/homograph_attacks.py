from core import HackingTool, HackingToolsCollection, console

from rich.panel import Panel
from rich.prompt import Prompt
from rich import box


class EvilURL(HackingTool):
    TITLE = "EvilURL"
    DESCRIPTION = "生成 unicode 恶意域名用于 IDN 同形攻击\n" \
                  "并检测它们。"
    INSTALL_COMMANDS = ["git clone https://github.com/UndeadSec/EvilURL.git"]
    RUN_COMMANDS = ["cd EvilURL;python3 evilurl.py"]
    PROJECT_URL = "https://github.com/UndeadSec/EvilURL"


class IDNHomographAttackTools(HackingToolsCollection):
    TITLE = "IDN 同形攻击"
    TOOLS = [EvilURL()]

if __name__ == "__main__":
    tools = IDNHomographAttackTools()
    tools.show_options()
