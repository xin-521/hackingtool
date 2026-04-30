from core import HackingTool
from core import HackingToolsCollection


class MobSF(HackingTool):
    TITLE = "MobSF (移动安全框架)"
    DESCRIPTION = "一站式移动应用渗透测试、恶意分析和安全评估工具。"
    INSTALL_COMMANDS = [
        "git clone https://github.com/MobSF/Mobile-Security-Framework-MobSF.git",
        "cd Mobile-Security-Framework-MobSF && ./setup.sh",
    ]
    RUN_COMMANDS = ["cd Mobile-Security-Framework-MobSF && ./run.sh"]
    PROJECT_URL = "https://github.com/MobSF/Mobile-Security-Framework-MobSF"
    SUPPORTED_OS = ["linux", "macos"]


class Frida(HackingTool):
    TITLE = "Frida (动态插桩)"
    DESCRIPTION = "动态插桩工具包，用于在 Android、iOS、Windows、macOS、Linux 上进行运行时 hook。"
    INSTALL_COMMANDS = ["pip install --user frida-tools"]
    RUN_COMMANDS = ["frida --help"]
    PROJECT_URL = "https://github.com/frida/frida"
    SUPPORTED_OS = ["linux", "macos"]


class Objection(HackingTool):
    TITLE = "Objection (移动运行时探索)"
    DESCRIPTION = "基于 Frida 的运行时移动探索工具包 - 无需越狱/root。"
    INSTALL_COMMANDS = ["pip install --user objection"]
    RUN_COMMANDS = ["objection --help"]
    PROJECT_URL = "https://github.com/sensepost/objection"
    SUPPORTED_OS = ["linux", "macos"]


class MobileSecurityTools(HackingToolsCollection):
    TITLE = "移动安全工具"
    DESCRIPTION = "用于 Android/iOS 应用程序安全测试和分析的工具。"
    TOOLS = [
        MobSF(),
        Frida(),
        Objection(),
    ]