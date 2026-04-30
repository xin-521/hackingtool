from core import HackingTool, HackingToolsCollection, console

from rich.panel import Panel
from rich.prompt import Prompt
from rich import box


class WifiJammerNG(HackingTool):
    TITLE = "WifiJammer-NG"
    DESCRIPTION = "持续干扰范围内所有 WiFi 客户端和接入点。"
    SUPPORTED_OS = ["linux"]
    REQUIRES_WIFI = True
    INSTALL_COMMANDS = [
        "git clone https://github.com/MisterBianco/wifijammer-ng.git",
        "cd wifijammer-ng;pip install --user -r requirements.txt"
    ]
    RUN_COMMANDS = [
        "cd wifijammer-ng && sudo python3 wifijammer.py --help",
    ]
    PROJECT_URL = "https://github.com/MisterBianco/wifijammer-ng"


class KawaiiDeauther(HackingTool):
    TITLE = "KawaiiDeauther"
    DESCRIPTION = "Kawaii Deauther 是一个渗透测试工具包，用于干扰 WiFi 客户端/路由器\n" \
                  "并生成大量虚假 AP 进行测试。"
    SUPPORTED_OS = ["linux"]
    REQUIRES_WIFI = True
    INSTALL_COMMANDS = [
        "git clone https://github.com/aryanrtm/KawaiiDeauther.git",
        "cd KawaiiDeauther;sudo bash install.sh"
    ]
    RUN_COMMANDS = ["cd KawaiiDeauther;sudo bash KawaiiDeauther.sh"]
    PROJECT_URL = "https://github.com/aryanrtm/KawaiiDeauther"


class WifiJammingTools(HackingToolsCollection):
    TITLE = "WiFi 取消认证攻击"
    TOOLS = [
        WifiJammerNG(),
        KawaiiDeauther()
    ]

if __name__ == "__main__":
    tools = WifiJammingTools()
    tools.show_options()
