import os
import subprocess

from core import HackingTool, HackingToolsCollection, console
from tools.others.android_attack import AndroidAttackTools
from tools.others.email_verifier import EmailVerifyTools
from tools.others.hash_crack import HashCrackingTools
from tools.others.homograph_attacks import IDNHomographAttackTools
from tools.others.mix_tools import MixTools
from tools.others.payload_injection import PayloadInjectorTools
from tools.others.socialmedia import SocialMediaBruteforceTools
from tools.others.socialmedia_finder import SocialMediaFinderTools
from tools.others.web_crawling import WebCrawlingTools
from tools.others.wifi_jamming import WifiJammingTools

from rich.panel import Panel
from rich.prompt import Prompt


class HatCloud(HackingTool):
    TITLE = "HatCloud (绕过 CloudFlare 获取 IP)"
    DESCRIPTION = "HatCloud 使用 Ruby 构建。它可以绕过 CloudFlare 发现真实 IP。"
    INSTALL_COMMANDS = ["git clone https://github.com/HatBashBR/HatCloud.git"]
    PROJECT_URL = "https://github.com/HatBashBR/HatCloud"

    def run(self):
        from config import get_tools_dir
        from rich.prompt import Prompt
        site = Prompt.ask("输入网站")
        # Bug 3 修复: os.chdir() 替换为 cwd= 参数
        subprocess.run(
            ["sudo", "ruby", "hatcloud.rb", "-b", site],
            cwd=str(get_tools_dir() / "HatCloud"),
        )


class OtherTools(HackingToolsCollection):
    TITLE = "其他工具"
    TOOLS = [
        SocialMediaBruteforceTools(),
        AndroidAttackTools(),
        HatCloud(),
        IDNHomographAttackTools(),
        EmailVerifyTools(),
        HashCrackingTools(),
        WifiJammingTools(),
        SocialMediaFinderTools(),
        PayloadInjectorTools(),
        WebCrawlingTools(),
        MixTools()
    ]

if __name__ == "__main__":
    tools = OtherTools()
    tools.show_options()
