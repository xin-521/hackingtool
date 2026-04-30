import subprocess
from core import HackingTool, HackingToolsCollection, console

from rich.panel import Panel
from rich.prompt import Prompt


class Web2Attack(HackingTool):
    TITLE = "Web2Attack"
    DESCRIPTION = "Web 黑客框架，包含 Python 编写的工具和漏洞利用"
    INSTALL_COMMANDS = [
        "git clone https://github.com/santatic/web2attack.git"
    ]
    RUN_COMMANDS = ["cd web2attack && sudo python3 w2aconsole"]
    PROJECT_URL = "https://github.com/santatic/web2attack"


class Skipfish(HackingTool):
    TITLE = "Skipfish"
    DESCRIPTION = (
        "Skipfish – 全自动主动 Web 应用程序\n"
        "安全侦察工具\n"
        "用法: skipfish -o [文件夹名] 目标IP/网站"
    )
    RUN_COMMANDS = [
        "sudo skipfish -h",
        'echo "skipfish -o [FolderName] targetip/site"|boxes -d headline | lolcat'
    ]

    def __init__(self):
        super().__init__(installable=False)


class SubDomainFinder(HackingTool):
    TITLE = "子域名查找器"
    DESCRIPTION = (
        "Sublist3r 是一个 Python 工具，旨在通过 OSINT 枚举\n"
        "网站的子域名\n"
        "用法:\n\t[1] python3 sublist3r.py -d example.com \n"
        "[2] python3 sublist3r.py -d example.com -p 80,443"
    )
    INSTALL_COMMANDS = [
        "sudo pip3 install requests argparse dnspython",
        "git clone https://github.com/aboul3la/Sublist3r.git",
        "cd Sublist3r && sudo pip3 install -r requirements.txt"
    ]
    RUN_COMMANDS = ["cd Sublist3r && python3 sublist3r.py -h"]
    PROJECT_URL = "https://github.com/aboul3la/Sublist3r"


class CheckURL(HackingTool):
    TITLE = "URL 检查器"
    DESCRIPTION = (
        "检测使用 IDN 同形异义字攻击的恶意 URL\n\t"
        "[!] python3 checkURL.py --url google.com"
    )
    INSTALL_COMMANDS = ["git clone https://github.com/UndeadSec/checkURL.git"]
    RUN_COMMANDS = ["cd checkURL && python3 checkURL.py --help"]
    PROJECT_URL = "https://github.com/UndeadSec/checkURL"


class Blazy(HackingTool):
    TITLE = "Blazy (含点击劫持检测)"
    DESCRIPTION = "Blazy 是一个现代化的登录页面暴力破解工具"
    INSTALL_COMMANDS = []
    RUN_COMMANDS = []
    PROJECT_URL = "https://github.com/UltimateHackers/Blazy"
    ARCHIVED = True
    ARCHIVED_REASON = "仅支持 Python 2。仓库已归档/无人维护。"

    def __init__(self):
        super().__init__(installable=False, runnable=False)


class SubDomainTakeOver(HackingTool):
    TITLE = "子域名劫持"
    DESCRIPTION = (
        "当子域名指向已删除或删除的服务\n"
        "(例如: GitHub, AWS/S3 等) 时，\n"
        "会发生子域名劫持漏洞。\n"
        "用法:python3 takeover.py -d www.domain.com -v"
    )
    INSTALL_COMMANDS = [
        "git clone https://github.com/edoardottt/takeover.git",
        "cd takeover && pip install --user ."
    ]
    PROJECT_URL = "https://github.com/edoardottt/takeover"

    def __init__(self):
        super().__init__(runnable=False)


class Dirb(HackingTool):
    TITLE = "Dirb"
    DESCRIPTION = (
        "DIRB 是一个 Web 内容扫描器。它查找现有的\n"
        "(和/或隐藏的) Web 对象。\n"
        "它基本上通过对 Web 服务器发起基于字典的攻击\n"
        "并分析响应来工作。"
    )
    INSTALL_COMMANDS = [
        "git clone https://gitlab.com/kalilinux/packages/dirb.git",
        "cd dirb;sudo bash configure;make"
    ]
    PROJECT_URL = "https://gitlab.com/kalilinux/packages/dirb"

    def run(self):
        uinput = input("输入 URL >> ")
        subprocess.run(["sudo", "dirb", uinput])


class Nuclei(HackingTool):
    TITLE = "Nuclei (漏洞扫描器)"
    DESCRIPTION = (
        "快速基于模板的漏洞扫描器，被 5 万+安全团队使用。\n"
        "用法: nuclei -u https://example.com"
    )
    REQUIRES_GO = True
    INSTALL_COMMANDS = [
        "go install -v github.com/projectdiscovery/nuclei/v3/cmd/nuclei@latest",
        "nuclei -update-templates",
    ]
    RUN_COMMANDS = ["nuclei -h"]
    PROJECT_URL = "https://github.com/projectdiscovery/nuclei"


class Ffuf(HackingTool):
    TITLE = "ffuf (Web 模糊测试器)"
    DESCRIPTION = (
        "快速 Web 模糊测试器 - 内容发现、参数模糊测试、虚拟主机发现。\n"
        "用法: ffuf -w wordlist.txt -u https://example.com/FUZZ"
    )
    REQUIRES_GO = True
    INSTALL_COMMANDS = [
        "go install -v github.com/ffuf/ffuf/v2@latest",
    ]
    RUN_COMMANDS = ["ffuf -h"]
    PROJECT_URL = "https://github.com/ffuf/ffuf"


class Feroxbuster(HackingTool):
    TITLE = "Feroxbuster (目录暴力破解)"
    DESCRIPTION = (
        "用 Rust 编写的快速递归内容发现工具。\n"
        "用法: feroxbuster -u https://example.com -w wordlist.txt"
    )
    SUPPORTED_OS = ["linux"]
    INSTALL_COMMANDS = [
        "curl -sL https://raw.githubusercontent.com/epi052/feroxbuster/main/install-nix.sh "
        "| sudo bash -s /usr/local/bin",
    ]
    RUN_COMMANDS = ["feroxbuster -h"]
    PROJECT_URL = "https://github.com/epi052/feroxbuster"


class Nikto(HackingTool):
    TITLE = "Nikto (Web 服务器扫描器)"
    DESCRIPTION = (
        "扫描 Web 服务器中的危险文件、过时软件、错误配置。\n"
        "用法: nikto -h https://example.com"
    )
    SUPPORTED_OS = ["linux"]
    INSTALL_COMMANDS = ["sudo apt-get install -y nikto"]
    RUN_COMMANDS = ["nikto -Help"]
    PROJECT_URL = "https://github.com/sullo/nikto"


class Wafw00f(HackingTool):
    TITLE = "wafw00f (WAF 检测器)"
    DESCRIPTION = (
        "指纹识别和检测 Web 应用程序防火墙 (WAF)。\n"
        "用法: wafw00f https://example.com"
    )
    INSTALL_COMMANDS = [
        "git clone https://github.com/EnableSecurity/wafw00f.git",
        "cd wafw00f && pip install --user .",
    ]
    RUN_COMMANDS = ["wafw00f --help"]
    PROJECT_URL = "https://github.com/EnableSecurity/wafw00f"


class Katana(HackingTool):
    TITLE = "Katana (Web 爬虫)"
    DESCRIPTION = (
        "ProjectDiscovery 的新一代爬取和蜘蛛框架。\n"
        "用法: katana -u https://example.com"
    )
    REQUIRES_GO = True
    INSTALL_COMMANDS = [
        "go install -v github.com/projectdiscovery/katana/cmd/katana@latest",
    ]
    RUN_COMMANDS = ["katana -h"]
    PROJECT_URL = "https://github.com/projectdiscovery/katana"


class Gobuster(HackingTool):
    TITLE = "Gobuster (目录/DNS/虚拟主机暴力破解)"
    DESCRIPTION = "用 Go 编写的目录/文件、DNS 和虚拟主机暴力破解工具。"
    REQUIRES_GO = True
    INSTALL_COMMANDS = ["go install github.com/OJ/gobuster/v3@latest"]
    RUN_COMMANDS = ["gobuster --help"]
    PROJECT_URL = "https://github.com/OJ/gobuster"


class Dirsearch(HackingTool):
    TITLE = "Dirsearch (Web 路径发现)"
    DESCRIPTION = "用于发现 Web 服务器上目录和文件的 Web 路径暴力破解工具。"
    INSTALL_COMMANDS = ["pip install --user dirsearch"]
    RUN_COMMANDS = ["dirsearch --help"]
    PROJECT_URL = "https://github.com/maurosoria/dirsearch"


class OwaspZap(HackingTool):
    TITLE = "OWASP ZAP (Web 应用扫描器)"
    DESCRIPTION = "功能齐全的 Web 应用程序安全扫描器 - 代理、爬虫、模糊测试器、扫描器。"
    SUPPORTED_OS = ["linux"]
    INSTALL_COMMANDS = ["sudo apt-get install -y zaproxy"]
    RUN_COMMANDS = ["zaproxy --help"]
    PROJECT_URL = "https://github.com/zaproxy/zaproxy"


class TestSSL(HackingTool):
    TITLE = "testssl.sh (TLS/SSL 检查器)"
    DESCRIPTION = "检查任何端口上的 TLS/SSL 密码、协议和加密缺陷。"
    INSTALL_COMMANDS = ["git clone https://github.com/drwetter/testssl.sh.git"]
    RUN_COMMANDS = ["cd testssl.sh && ./testssl.sh --help"]
    PROJECT_URL = "https://github.com/drwetter/testssl.sh"


class Arjun(HackingTool):
    TITLE = "Arjun (HTTP 参数发现)"
    DESCRIPTION = "HTTP 参数发现套件，用于查找隐藏的 GET/POST 参数。"
    INSTALL_COMMANDS = ["pip install --user arjun"]
    RUN_COMMANDS = ["arjun --help"]
    PROJECT_URL = "https://github.com/s0md3v/Arjun"


class Caido(HackingTool):
    TITLE = "Caido (Web 安全审计)"
    DESCRIPTION = "轻量级现代化 Web 安全审计工具 - Burp Suite 的 Rust 替代品。"
    INSTALL_COMMANDS = [
        "curl -sSL https://caido.download/releases/latest/caido-cli-linux-x86_64.tar.gz | sudo tar xz -C /usr/local/bin",
    ]
    RUN_COMMANDS = ["caido --help"]
    PROJECT_URL = "https://github.com/caido/caido"
    SUPPORTED_OS = ["linux", "macos"]


class Mitmproxy(HackingTool):
    TITLE = "mitmproxy (拦截代理)"
    DESCRIPTION = "交互式支持 TLS 的拦截 HTTP 代理，适用于渗透测试人员和开发人员。"
    INSTALL_COMMANDS = ["pip install --user mitmproxy"]
    RUN_COMMANDS = ["mitmproxy --version"]
    PROJECT_URL = "https://github.com/mitmproxy/mitmproxy"


class WebAttackTools(HackingToolsCollection):
    TITLE = "Web 攻击工具"
    DESCRIPTION = ""
    TOOLS = [
        Web2Attack(),
        Skipfish(),
        SubDomainFinder(),
        CheckURL(),
        Blazy(),
        SubDomainTakeOver(),
        Dirb(),
        Nuclei(),
        Ffuf(),
        Feroxbuster(),
        Nikto(),
        Wafw00f(),
        Katana(),
        Gobuster(),
        Dirsearch(),
        OwaspZap(),
        TestSSL(),
        Arjun(),
        Caido(),
        Mitmproxy(),
    ]

if __name__ == "__main__":
    tools = WebAttackTools()
    tools.show_options()
