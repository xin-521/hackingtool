import os
import socket
import subprocess
import webbrowser
import sys

from core import HackingTool, HackingToolsCollection, console
from core import clear_screen

from rich.panel import Panel
from rich.text import Text
from rich.prompt import Prompt


class NMAP(HackingTool):
    TITLE = "网络映射器 (nmap)"
    DESCRIPTION = "免费开源的网络发现和安全审计工具"
    INSTALL_COMMANDS = [
        "git clone https://github.com/nmap/nmap.git",
        "sudo chmod -R 755 nmap && cd nmap && sudo ./configure && make && sudo make install"
    ]
    PROJECT_URL = "https://github.com/nmap/nmap"

    def __init__(self):
        super().__init__(runnable=False)


class Dracnmap(HackingTool):
    TITLE = "Dracnmap"
    DESCRIPTION = "Dracnmap 是一个开源程序，用于\n利用网络并借助 nmap 收集信息。"
    INSTALL_COMMANDS = [
        "git clone https://github.com/Screetsec/Dracnmap.git",
        "cd Dracnmap && chmod +x dracnmap-v2.2-dracOs.sh  dracnmap-v2.2.sh"
    ]
    RUN_COMMANDS = ["cd Dracnmap;sudo ./dracnmap-v2.2.sh"]
    PROJECT_URL = "https://github.com/Screetsec/Dracnmap"


class PortScan(HackingTool):
    TITLE = "端口扫描"

    def __init__(self):
        super().__init__(installable=False)

    def run(self):
        clear_screen()
        console.print(Panel(Text(self.TITLE, justify="center"), style="bold magenta"))
        target = Prompt.ask("[bold]选择目标 IP[/bold magenta]", default="", show_default=False)
        subprocess.run(["sudo", "nmap", "-O", "-Pn", target])


class Host2IP(HackingTool):
    TITLE = "主机名转 IP"

    def __init__(self):
        super().__init__(installable=False)

    def run(self):
        clear_screen()
        console.print(Panel(Text(self.TITLE, justify="center"), style="bold magenta"))
        host = Prompt.ask("输入主机名 (例如 www.google.com):-  ")
        ips = socket.gethostbyname(host)
        console.print(f"[bold magenta]{host} -> {ips}[/bold magenta]")


class XeroSploit(HackingTool):
    TITLE = "Xerosploit"
    DESCRIPTION = "Xerosploit 是一个渗透测试工具包，目标是执行\n中间人攻击进行测试"
    INSTALL_COMMANDS = [
        "git clone https://github.com/LionSec/xerosploit.git",
        "cd xerosploit && sudo python install.py"
    ]
    RUN_COMMANDS = ["sudo xerosploit"]
    PROJECT_URL = "https://github.com/LionSec/xerosploit"


class RedHawk(HackingTool):
    TITLE = "RED HAWK (一体化扫描)"
    DESCRIPTION = "用于信息收集和漏洞扫描的一体化工具。"
    INSTALL_COMMANDS = [
        "git clone https://github.com/Tuhinshubhra/RED_HAWK.git"]
    RUN_COMMANDS = ["cd RED_HAWK;php rhawk.php"]
    PROJECT_URL = "https://github.com/Tuhinshubhra/RED_HAWK"


class ReconSpider(HackingTool):
    TITLE = "ReconSpider (全面扫描)"
    DESCRIPTION = "ReconSpider 是最先进的开源情报 (OSINT)" \
                  "框架，用于扫描 IP 地址、电子邮件、\n" \
                  "网站、组织并从不同来源查找信息。\n"
    INSTALL_COMMANDS = [
        "git clone https://github.com/bhavsec/reconspider.git",
        "sudo apt install -y python3 python3-pip && cd reconspider && pip install --user ."
    ]
    RUN_COMMANDS = ["cd reconspider;python3 reconspider.py"]
    PROJECT_URL = "https://github.com/bhavsec/reconspider"


class IsItDown(HackingTool):
    TITLE = "IsItDown (检查网站在线/离线)"
    DESCRIPTION = "检查网站是否在线"

    def __init__(self):
        super().__init__(
            [('打开', self.open)], installable=False, runnable=False)

    def open(self):
        console.print(Panel("正在打开 isitdownrightnow.com", style="bold magenta"))
        webbrowser.open_new_tab("https://www.isitdownrightnow.com/")


class Infoga(HackingTool):
    TITLE = "Infoga - 电子邮件 OSINT"
    DESCRIPTION = "Infoga 是一个从不同公开来源收集电子邮件账户信息\n" \
                  "(IP、主机名、国家等) 的工具"
    INSTALL_COMMANDS = [
        "git clone https://github.com/m4ll0k/Infoga.git",
        "cd Infoga && pip install --user ."
    ]
    RUN_COMMANDS = ["cd Infoga;python3 infoga.py"]
    PROJECT_URL = "https://github.com/m4ll0k/Infoga"


class ReconDog(HackingTool):
    TITLE = "ReconDog"
    DESCRIPTION = "ReconDog 信息收集套件"
    INSTALL_COMMANDS = ["git clone https://github.com/s0md3v/ReconDog.git"]
    RUN_COMMANDS = ["cd ReconDog;sudo python dog"]
    PROJECT_URL = "https://github.com/s0md3v/ReconDog"


class Striker(HackingTool):
    TITLE = "Striker"
    DESCRIPTION = "侦察和漏洞扫描套件"
    INSTALL_COMMANDS = [
        "git clone https://github.com/s0md3v/Striker.git",
        "cd Striker && pip3 install -r requirements.txt"
    ]
    PROJECT_URL = "https://github.com/s0md3v/Striker"

    def run(self):
        from config import get_tools_dir
        site = Prompt.ask("输入网站名称 (example.com)")
        # Bug 3 修复: os.chdir() 会永久破坏进程 CWD - 改用 cwd=
        subprocess.run(
            ["sudo", "python3", "striker.py", site],
            cwd=str(get_tools_dir() / "Striker"),
        )


class SecretFinder(HackingTool):
    TITLE = "SecretFinder (API 等)"
    DESCRIPTION = "SecretFinder - 一个用于查找敏感数据的 Python 脚本\n" \
                  "如 apikeys、accesstoken、authorizations、jwt 等\n" \
                  "并在 JavaScript 文件中搜索任何内容\n\n" \
                  "用法: python SecretFinder.py -h"
    INSTALL_COMMANDS = [
        "git clone https://github.com/m4ll0k/SecretFinder.git secretfinder",
        "cd secretfinder; sudo pip3 install -r requirements.txt"
    ]
    PROJECT_URL = "https://github.com/m4ll0k/SecretFinder"

    def __init__(self):
        super().__init__(runnable=False)


class Shodan(HackingTool):
    TITLE = "使用 Shodan 查找信息"
    DESCRIPTION = "使用 Shodan 获取任何 IP 的端口、漏洞、信息、横幅等\n" \
                  "(无需 API 密钥！无速率限制！)\n" \
                  "[X] 不要使用此工具，因为您的 IP 将被 Shodan 封禁！"
    INSTALL_COMMANDS = ["git clone https://github.com/m4ll0k/Shodanfy.py.git"]
    PROJECT_URL = "https://github.com/m4ll0k/Shodanfy.py"

    def __init__(self):
        super().__init__(runnable=False)


class PortScannerRanger(HackingTool):
    TITLE = "端口扫描器 - rang3r"
    DESCRIPTION = "rang3r 是一个 Python 脚本，以多线程方式扫描\n" \
                  "您指定范围内的所有存活主机。"
    INSTALL_COMMANDS = [
        "git clone https://github.com/floriankunushevci/rang3r.git;"
        "pip install --user termcolor"]
    PROJECT_URL = "https://github.com/floriankunushevci/rang3r"

    def run(self):
        from config import get_tools_dir
        ip = Prompt.ask("输入 IP")
        # Bug 3 修复: os.chdir() 替换为 cwd= 参数
        subprocess.run(
            ["sudo", "python3", "rang3r.py", "--ip", ip],
            cwd=str(get_tools_dir() / "rang3r"),
        )


class Breacher(HackingTool):
    TITLE = "Breacher"
    DESCRIPTION = "高级多线程管理面板查找器，用 Python 编写。"
    INSTALL_COMMANDS = ["git clone https://github.com/s0md3v/Breacher.git"]
    PROJECT_URL = "https://github.com/s0md3v/Breacher"

    def run(self):
        from config import get_tools_dir
        domain = Prompt.ask("输入域名 (example.com)")
        # Bug 3 修复: os.chdir() 替换为 cwd= 参数
        subprocess.run(
            ["python3", "breacher.py", "-u", domain],
            cwd=str(get_tools_dir() / "Breacher"),
        )


class TheHarvester(HackingTool):
    TITLE = "theHarvester (OSINT)"
    DESCRIPTION = (
        "从公开来源收集电子邮件、名称、子域名、IP 和 URL。\n"
        "用法: theHarvester -d example.com -b all"
    )
    INSTALL_COMMANDS = [
        "git clone https://github.com/laramies/theHarvester.git",
        "cd theHarvester && pip install --user -r requirements/base.txt",
    ]
    RUN_COMMANDS = ["cd theHarvester && python3 theHarvester.py -h"]
    PROJECT_URL = "https://github.com/laramies/theHarvester"


class Amass(HackingTool):
    TITLE = "Amass (攻击面映射)"
    DESCRIPTION = (
        "深入的子域名枚举和攻击面映射。\n"
        "用法: amass enum -d example.com"
    )
    SUPPORTED_OS = ["linux"]
    REQUIRES_GO = True
    INSTALL_COMMANDS = [
        "go install -v github.com/owasp-amass/amass/v4/...@master",
    ]
    RUN_COMMANDS = ["amass -h"]
    PROJECT_URL = "https://github.com/owasp-amass/amass"


class Masscan(HackingTool):
    TITLE = "Masscan (快速端口扫描器)"
    DESCRIPTION = (
        "最快的互联网端口扫描器 - 每秒 1000 万个数据包。\n"
        "用法: masscan -p1-65535 <IP> --rate=1000"
    )
    SUPPORTED_OS = ["linux"]
    INSTALL_COMMANDS = ["sudo apt-get install -y masscan"]
    RUN_COMMANDS = ["masscan --help"]
    PROJECT_URL = "https://github.com/robertdavidgraham/masscan"


class RustScan(HackingTool):
    TITLE = "RustScan (现代化端口扫描器)"
    DESCRIPTION = (
        "3 秒内扫描全部 65k 端口，自动将结果传递给 nmap。\n"
        "用法: rustscan -a <IP> -- -sV"
    )
    SUPPORTED_OS = ["linux"]
    INSTALL_COMMANDS = [
        "curl -sLO https://github.com/RustScan/RustScan/releases/latest/download/rustscan_2.3.0_amd64.deb",
        "sudo dpkg -i rustscan_2.3.0_amd64.deb",
    ]
    RUN_COMMANDS = ["rustscan --help"]
    PROJECT_URL = "https://github.com/RustScan/RustScan"


class Holehe(HackingTool):
    TITLE = "Holehe (邮箱 → 社交账户)"
    DESCRIPTION = (
        "检查电子邮件地址是否在 120+ 网站上注册。\n"
        "用法: holehe user@example.com"
    )
    INSTALL_COMMANDS = ["pip install --user holehe"]
    RUN_COMMANDS = ["holehe --help"]
    PROJECT_URL = "https://github.com/megadose/holehe"


class Maigret(HackingTool):
    TITLE = "Maigret (用户名 OSINT)"
    DESCRIPTION = (
        "通过用户名在 3000+ 站点收集个人信息。\n"
        "用法: maigret <username>"
    )
    INSTALL_COMMANDS = ["pip install --user maigret"]
    RUN_COMMANDS = ["maigret --help"]
    PROJECT_URL = "https://github.com/soxoj/maigret"


class Httpx(HackingTool):
    TITLE = "httpx (HTTP 工具包)"
    DESCRIPTION = (
        "快速多用途 HTTP 探测工具。\n"
        "用法: httpx -l urls.txt -status-code -title -tech-detect"
    )
    REQUIRES_GO = True
    INSTALL_COMMANDS = [
        "go install -v github.com/projectdiscovery/httpx/cmd/httpx@latest",
    ]
    RUN_COMMANDS = ["httpx -h"]
    PROJECT_URL = "https://github.com/projectdiscovery/httpx"


class SpiderFoot(HackingTool):
    TITLE = "SpiderFoot (OSINT 自动化)"
    DESCRIPTION = "自动化 OSINT 收集，用于威胁情报和攻击面映射。"
    INSTALL_COMMANDS = ["pip install --user spiderfoot"]
    RUN_COMMANDS = ["spiderfoot -h"]
    PROJECT_URL = "https://github.com/smicallef/spiderfoot"


class Subfinder(HackingTool):
    TITLE = "Subfinder (子域名枚举)"
    DESCRIPTION = "使用多种来源的快速被动子域名枚举。"
    REQUIRES_GO = True
    INSTALL_COMMANDS = [
        "go install -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest",
    ]
    RUN_COMMANDS = ["subfinder -h"]
    PROJECT_URL = "https://github.com/projectdiscovery/subfinder"


class TruffleHog(HackingTool):
    TITLE = "TruffleHog (密钥扫描器)"
    DESCRIPTION = "在 git 仓库、S3 存储桶、文件系统中查找、验证和分析泄露的凭证。"
    INSTALL_COMMANDS = ["pip install --user trufflehog"]
    RUN_COMMANDS = ["trufflehog --help"]
    PROJECT_URL = "https://github.com/trufflesecurity/trufflehog"


class Gitleaks(HackingTool):
    TITLE = "Gitleaks (Git 密钥扫描器)"
    DESCRIPTION = "快速的 git 仓库密钥扫描器 - 检测硬编码密码、API 密钥、令牌。"
    REQUIRES_GO = True
    INSTALL_COMMANDS = [
        "go install github.com/gitleaks/gitleaks/v8@latest",
    ]
    RUN_COMMANDS = ["gitleaks --help"]
    PROJECT_URL = "https://github.com/gitleaks/gitleaks"


class InformationGatheringTools(HackingToolsCollection):
    TITLE = "信息收集工具"
    TOOLS = [
        NMAP(),
        Dracnmap(),
        PortScan(),
        Host2IP(),
        XeroSploit(),
        RedHawk(),
        ReconSpider(),
        IsItDown(),
        Infoga(),
        ReconDog(),
        Striker(),
        SecretFinder(),
        Shodan(),
        PortScannerRanger(),
        Breacher(),
        TheHarvester(),
        Amass(),
        Masscan(),
        RustScan(),
        Holehe(),
        Maigret(),
        Httpx(),
        SpiderFoot(),
        Subfinder(),
        TruffleHog(),
        Gitleaks(),
    ]

if __name__ == "__main__":
    tools = InformationGatheringTools()
    tools.show_options()
