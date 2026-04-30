#!/usr/bin/env python3
import os
import sys
import shutil
import subprocess
from pathlib import Path

# ── Python version check (must be before any other local import) ──────────────
if sys.version_info < (3, 10):
    print(
        f"[错误] 需要 Python 3.10 或更高版本。\n"
        f"您当前运行的是 Python {sys.version_info.major}.{sys.version_info.minor}。\n"
        f"请使用以下命令安装: sudo apt install python3.10"
    )
    sys.exit(1)

from rich.console import Console
from rich.panel import Panel
from rich.prompt import Confirm
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.text import Text
from rich import box

from constants import (
    REPO_URL, APP_INSTALL_DIR, APP_BIN_PATH,
    VERSION, VERSION_DISPLAY,
    USER_CONFIG_DIR, USER_TOOLS_DIR, USER_CONFIG_FILE,
    DEFAULT_CONFIG,
)
from os_detect import CURRENT_OS, REQUIRED_PACKAGES, PACKAGE_UPDATE_CMDS, PACKAGE_INSTALL_CMDS

console = Console()

VENV_DIR_NAME = "venv"
REQUIREMENTS   = "requirements.txt"


# ── Privilege check ────────────────────────────────────────────────────────────

def check_root():
    if os.geteuid() != 0:
        console.print(Panel(
            "[error]此安装程序必须以 root 权限运行。\n"
            "请使用: [bold]sudo python3 install.py[/bold][/error]",
            border_style="red",
        ))
        sys.exit(1)


# ── OS compatibility check ─────────────────────────────────────────────────────

def check_os_compatibility():
    """打印检测到的操作系统信息，并在不支持的系统上退出。"""
    info = CURRENT_OS
    console.print(
        f"[dim]检测到: 操作系统={info.system} | 发行版={info.distro_id or '无'} | "
        f"包管理器={info.pkg_manager or '无'} | 架构={info.arch}[/dim]"
    )

    if info.system == "windows":
        console.print(Panel(
            "[error]不支持原生 Windows。[/error]\n"
            "请使用 WSL2 并搭配 Kali 或 Ubuntu 镜像。",
            border_style="red",
        ))
        sys.exit(1)

    if info.is_wsl:
        console.print("[warning]检测到 WSL。无线工具在 WSL 中无法工作。[/warning]")

    if info.system == "macos":
        console.print(Panel(
            "[warning]macOS 支持有限。[/warning]\n"
            "网络/无线工具需要 Linux。OSINT 和 Web 工具可以工作。",
            border_style="yellow",
        ))
        if not shutil.which("brew"):
            console.print("[error]未找到 Homebrew。请先安装: https://brew.sh[/error]")
            sys.exit(1)

    if not info.pkg_manager:
        console.print("[warning]未找到支持的包管理器。[/warning]")
        console.print("[dim]支持的包管理器: apt-get, pacman, dnf, zypper, apk, brew[/dim]")


# ── Internet check ─────────────────────────────────────────────────────────────

def check_internet() -> bool:
    console.print("[dim]检查网络连接...[/dim]")
    for host in ("https://github.com", "https://www.google.com"):
        r = subprocess.run(
            ["curl", "-sSf", "--max-time", "8", host],
            capture_output=True,
        )
        if r.returncode == 0:
            console.print("[success]✔ 网络连接正常[/success]")
            return True
    console.print("[error]✘ 无网络连接[/error]")
    return False


# ── System packages ────────────────────────────────────────────────────────────

def install_system_packages():
    mgr = CURRENT_OS.pkg_manager
    if not mgr:
        console.print("[warning]跳过系统包安装 - 未找到包管理器。[/warning]")
        return

    # 仅在未以 root 运行时使用 sudo (uid != 0)。
    # 在 Docker 中我们以 root 运行，且未安装 sudo。
    priv = "" if os.geteuid() == 0 else "sudo "

    # 首先更新索引 (brew 不需要)
    if mgr != "brew":
        update_cmd = PACKAGE_UPDATE_CMDS.get(mgr, "")
        if update_cmd:
            console.print(f"[dim]正在更新包索引 ({mgr})...[/dim]")
            subprocess.run(f"{priv}{update_cmd}", shell=True, check=False)

    packages = REQUIRED_PACKAGES.get(mgr, [])
    if not packages:
        return

    install_tpl = PACKAGE_INSTALL_CMDS[mgr]
    cmd = install_tpl.format(packages=" ".join(packages))
    console.print(f"[dim]正在安装系统依赖 ({mgr})...[/dim]")
    result = subprocess.run(f"{priv}{cmd}", shell=True, check=False)
    if result.returncode != 0:
        console.print("[warning]部分包安装失败 - 您可能需要手动安装。[/warning]")


# ── App directory ──────────────────────────────────────────────────────────────

def _is_source_dir() -> bool:
    """检查 install.py 是否从本地 clone 运行 (hackingtool.py 存在于同目录)。"""
    return (Path(__file__).resolve().parent / "hackingtool.py").exists()


def prepare_install_dir():
    if APP_INSTALL_DIR.exists():
        console.print(f"[warning]{APP_INSTALL_DIR} 已存在。[/warning]")
        if not Confirm.ask("替换它？这将删除现有安装。", default=False):
            console.print("[error]安装已中止。[/error]")
            sys.exit(1)
        subprocess.run(["rm", "-rf", str(APP_INSTALL_DIR)], check=True)
    APP_INSTALL_DIR.mkdir(parents=True, exist_ok=True)


def install_source() -> bool:
    """从 GitHub clone 或从本地源复制 (如果已在 clone 中)。"""
    source_dir = Path(__file__).resolve().parent

    if _is_source_dir() and source_dir != APP_INSTALL_DIR:
        # 已在本地 clone 中 - 复制而不是重新 clone
        console.print(f"[dim]正在从 {source_dir} 复制源...[/dim]")
        # 首先删除以确保干净复制 (prepare_install_dir 可能已创建它)
        if APP_INSTALL_DIR.exists():
            subprocess.run(["rm", "-rf", str(APP_INSTALL_DIR)], check=True)
        subprocess.run(["cp", "-a", str(source_dir), str(APP_INSTALL_DIR)], check=True)
        # 修复所有权以避免 git 报"dubious ownership"错误
        subprocess.run(["chown", "-R", "root:root", str(APP_INSTALL_DIR)], check=False)
        console.print("[success]✔ 源已复制 (无需重新 clone)[/success]")
        return True

    # 不是从源运行 - 从 GitHub clone
    console.print(f"[dim]正在 clone {REPO_URL}...[/dim]")
    r = subprocess.run(["git", "clone", "--depth", "1", REPO_URL, str(APP_INSTALL_DIR)], check=False)
    if r.returncode == 0:
        console.print("[success]✔ 仓库已 clone[/success]")
        return True
    console.print("[error]✘ 仓库 clone 失败[/error]")
    return False


# ── Python venv ────────────────────────────────────────────────────────────────

def create_venv_and_install():
    venv_path = APP_INSTALL_DIR / VENV_DIR_NAME
    console.print("[dim]正在创建虚拟环境...[/dim]")
    subprocess.run([sys.executable, "-m", "venv", str(venv_path)], check=True)

    pip = str(venv_path / "bin" / "pip")
    req = APP_INSTALL_DIR / REQUIREMENTS
    if req.exists():
        console.print("[dim]正在安装 Python 依赖...[/dim]")
        subprocess.run([pip, "install", "--quiet", "-r", str(req)], check=False)
    else:
        console.print("[warning]未找到 requirements.txt - 跳过 pip 安装。[/warning]")


# ── Launcher script ────────────────────────────────────────────────────────────

def create_launcher():
    launcher = APP_INSTALL_DIR / "hackingtool.sh"
    launcher.write_text(
        "#!/bin/bash\n"
        f'source "{APP_INSTALL_DIR / VENV_DIR_NAME}/bin/activate"\n'
        f'python3 "{APP_INSTALL_DIR / "hackingtool.py"}" "$@"\n'
    )
    launcher.chmod(0o755)
    if APP_BIN_PATH.exists():
        APP_BIN_PATH.unlink()
    shutil.move(str(launcher), str(APP_BIN_PATH))
    console.print(f"[success]✔ 启动器已安装在 {APP_BIN_PATH}[/success]")


# ── User directories ───────────────────────────────────────────────────────────

def create_user_directories():
    """
    创建 ~/.hackingtool/ 并写入初始 config.json。
    使用 Path.home() - 无论用户名或操作系统如何，始终正确。
    以 root 或普通用户运行都安全。
    """
    import json
    USER_CONFIG_DIR.mkdir(parents=True, exist_ok=True)
    USER_TOOLS_DIR.mkdir(parents=True, exist_ok=True)
    if not USER_CONFIG_FILE.exists():
        USER_CONFIG_FILE.write_text(json.dumps(DEFAULT_CONFIG, indent=2, sort_keys=True))
        console.print(f"[success]✔ 配置已创建于 {USER_CONFIG_FILE}[/success]")
    console.print(f"[success]✔ 工具目录: {USER_TOOLS_DIR}[/success]")


# ── 入口点 ────────────────────────────────────────────────────────────────

def main():
    check_root()
    console.clear()

    console.print(Panel(
        Text(f"HackingTool 安装程序  {VERSION_DISPLAY}", style="bold magenta"),
        box=box.DOUBLE, border_style="bright_magenta",
    ))

    check_os_compatibility()

    if not check_internet():
        sys.exit(1)

    with Progress(SpinnerColumn(), TextColumn("[progress.description]{task.description}")) as p:
        p.add_task("正在安装系统包...", total=None)
        install_system_packages()

    prepare_install_dir()

    if not install_source():
        sys.exit(1)

    with Progress(SpinnerColumn(), TextColumn("[progress.description]{task.description}")) as p:
        p.add_task("正在设置虚拟环境和依赖...", total=None)
        create_venv_and_install()

    create_launcher()
    create_user_directories()

    console.print(Panel(
        "[bold magenta]安装完成！[/bold magenta]\n\n"
        "在终端中输入 [bold cyan]hackingtool[/bold cyan] 启动。",
        border_style="magenta",
    ))


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        console.print("\n[error]安装已中断。[/error]")
        sys.exit(1)
    except subprocess.CalledProcessError as e:
        console.print(f"[error]命令失败: {e}[/error]")
        sys.exit(1)
