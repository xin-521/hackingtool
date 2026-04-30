from core import HackingTool
from core import HackingToolsCollection


class Prowler(HackingTool):
    TITLE = "Prowler (云安全扫描器)"
    DESCRIPTION = "用于 AWS、Azure、GCP 和 Kubernetes 评估的开源安全工具。"
    INSTALL_COMMANDS = ["pip install --user prowler"]
    RUN_COMMANDS = ["prowler --help"]
    PROJECT_URL = "https://github.com/prowler-cloud/prowler"
    SUPPORTED_OS = ["linux", "macos"]


class ScoutSuite(HackingTool):
    TITLE = "ScoutSuite (多云审计)"
    DESCRIPTION = "多云安全审计工具，适用于 AWS、Azure、GCP、阿里云和甲骨文云。"
    INSTALL_COMMANDS = ["pip install --user scoutsuite"]
    RUN_COMMANDS = ["scout --help"]
    PROJECT_URL = "https://github.com/nccgroup/ScoutSuite"
    SUPPORTED_OS = ["linux", "macos"]


class Pacu(HackingTool):
    TITLE = "Pacu (AWS 利用框架)"
    DESCRIPTION = "用于 AWS 环境渗透测试的利用框架。"
    INSTALL_COMMANDS = ["pip install --user pacu"]
    RUN_COMMANDS = ["pacu --help"]
    PROJECT_URL = "https://github.com/RhinoSecurityLabs/pacu"
    SUPPORTED_OS = ["linux", "macos"]


class Trivy(HackingTool):
    TITLE = "Trivy (容器/K8s 扫描器)"
    DESCRIPTION = "全面的漏洞扫描器，适用于容器、Kubernetes、IaC 和代码。"
    INSTALL_COMMANDS = [
        "curl -sfL https://raw.githubusercontent.com/aquasecurity/trivy/main/contrib/install.sh | sudo sh -s -- -b /usr/local/bin",
    ]
    RUN_COMMANDS = ["trivy --help"]
    PROJECT_URL = "https://github.com/aquasecurity/trivy"
    SUPPORTED_OS = ["linux", "macos"]


class CloudSecurityTools(HackingToolsCollection):
    TITLE = "云安全工具"
    DESCRIPTION = "用于云基础设施安全评估和渗透的工具。"
    TOOLS = [
        Prowler(),
        ScoutSuite(),
        Pacu(),
        Trivy(),
    ]
