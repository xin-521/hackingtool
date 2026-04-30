from core import HackingTool
from core import HackingToolsCollection


class BloodHound(HackingTool):
    TITLE = "BloodHound (AD 攻击路径)"
    DESCRIPTION = "使用图论揭示 Active Directory/Azure 环境中隐藏的攻击路径。"
    INSTALL_COMMANDS = [
        "pip install --user bloodhound",
        "sudo apt-get install -y neo4j",
    ]
    RUN_COMMANDS = ["bloodhound-python --help"]
    PROJECT_URL = "https://github.com/BloodHoundAD/BloodHound"
    SUPPORTED_OS = ["linux", "macos"]


class NetExec(HackingTool):
    TITLE = "NetExec — nxc (网络渗透测试)"
    DESCRIPTION = "Windows/AD 网络渗透测试的瑞士军刀。CrackMapExec 的继任者。"
    INSTALL_COMMANDS = ["pip install --user netexec"]
    RUN_COMMANDS = ["nxc --help"]
    PROJECT_URL = "https://github.com/Pennyw0rth/NetExec"
    SUPPORTED_OS = ["linux", "macos"]


class Impacket(HackingTool):
    TITLE = "Impacket (网络协议工具)"
    DESCRIPTION = "用于 SMB、MSRPC、Kerberos、LDAP 等协议的 Python 类库。"
    INSTALL_COMMANDS = ["pip install --user impacket"]
    RUN_COMMANDS = ["impacket-smbclient --help"]
    PROJECT_URL = "https://github.com/fortra/impacket"
    SUPPORTED_OS = ["linux", "macos"]


class Responder(HackingTool):
    TITLE = "Responder (LLMNR/NBT-NS 投毒)"
    DESCRIPTION = "LLMNR/NBT-NS/MDNS 投毒器，带有用于凭据捕获的恶意认证服务器。"
    INSTALL_COMMANDS = ["git clone https://github.com/lgandx/Responder.git"]
    RUN_COMMANDS = ["cd Responder && sudo python3 Responder.py --help"]
    PROJECT_URL = "https://github.com/lgandx/Responder"
    SUPPORTED_OS = ["linux"]


class Certipy(HackingTool):
    TITLE = "Certipy (AD 证书滥用)"
    DESCRIPTION = "Active Directory 证书服务枚举和滥用工具。"
    INSTALL_COMMANDS = ["pip install --user certipy-ad"]
    RUN_COMMANDS = ["certipy --help"]
    PROJECT_URL = "https://github.com/ly4k/Certipy"
    SUPPORTED_OS = ["linux", "macos"]


class Kerbrute(HackingTool):
    TITLE = "Kerbrute (Kerberos 暴力破解)"
    DESCRIPTION = "Kerberos 预认证暴力破解器，用于用户名枚举和密码喷洒。"
    REQUIRES_GO = True
    INSTALL_COMMANDS = [
        "go install github.com/ropnop/kerbrute@latest",
    ]
    RUN_COMMANDS = ["kerbrute --help"]
    PROJECT_URL = "https://github.com/ropnop/kerbrute"
    SUPPORTED_OS = ["linux", "macos"]


class ActiveDirectoryTools(HackingToolsCollection):
    TITLE = "Active Directory 工具"
    DESCRIPTION = "用于 AD 枚举、攻击路径发现和凭据攻击的工具。"
    TOOLS = [
        BloodHound(),
        NetExec(),
        Impacket(),
        Responder(),
        Certipy(),
        Kerbrute(),
    ]