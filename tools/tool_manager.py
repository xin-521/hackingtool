import os
import sys
import subprocess
from time import sleep

from rich.prompt import Confirm

from core import HackingTool, HackingToolsCollection, console
from constants import APP_INSTALL_DIR, APP_BIN_PATH, USER_CONFIG_DIR, REPO_URL


class UpdateTool(HackingTool):
    TITLE = "更新工具或系统"
    DESCRIPTION = "更新系统包或拉取最新的 hackingtool 代码"

    def __init__(self):
        super().__init__([
            ("更新系统", self.update_sys),
            ("更新 Hackingtool", self.update_ht),
        ], installable=False, runnable=False)

    def update_sys(self):
        from os_detect import CURRENT_OS, PACKAGE_UPDATE_CMDS
        mgr = CURRENT_OS.pkg_manager
        cmd = PACKAGE_UPDATE_CMDS.get(mgr)
        if cmd:
            priv = "" if (CURRENT_OS.system == "macos" or os.geteuid() == 0) else "sudo "
            # shell=True 需要 - cmd 包含 && 链；字符串是硬编码的，非用户输入
            subprocess.run(f"{priv}{cmd}", shell=True, check=False)
        else:
            console.print("[warning]未知的包管理器 - 请手动更新。[/warning]")

    def update_ht(self):
        if not APP_INSTALL_DIR.exists():
            console.print(f"[error]未找到安装目录: {APP_INSTALL_DIR}[/error]")
            console.print("[dim]请先运行 install.py。[/dim]")
            return
        console.print(f"[bold cyan]正在从 {REPO_URL} 拉取最新代码...[/bold cyan]")
        result = subprocess.run(
            ["git", "pull", "--rebase"],
            cwd=str(APP_INSTALL_DIR),
            capture_output=True, text=True,
        )
        if result.returncode != 0:
            console.print(f"[error]git pull 失败:\n{result.stderr}[/error]")
            return
        pip = str(APP_INSTALL_DIR / "venv" / "bin" / "pip")
        if (APP_INSTALL_DIR / "venv" / "bin" / "pip").exists():
            subprocess.run([pip, "install", "-q", "-r",
                            str(APP_INSTALL_DIR / "requirements.txt")])
        console.print("[success]✔ Hackingtool 已更新。[/success]")


class UninstallTool(HackingTool):
    TITLE = "卸载 HackingTool"
    DESCRIPTION = "从系统中删除 hackingtool"

    def __init__(self):
        super().__init__([
            ("卸载", self.uninstall),
        ], installable=False, runnable=False)

    def uninstall(self):
        import shutil
        console.print("[warning]这将从您的系统中删除 hackingtool。[/warning]")
        if not Confirm.ask("继续？", default=False):
            return

        if APP_INSTALL_DIR.exists():
            shutil.rmtree(str(APP_INSTALL_DIR))
            console.print(f"[success]✔ 已删除 {APP_INSTALL_DIR}[/success]")
        else:
            console.print(f"[dim]{APP_INSTALL_DIR} 不存在 - 已被删除？[/dim]")

        if APP_BIN_PATH.exists():
            APP_BIN_PATH.unlink()
            console.print(f"[success]✔ 已删除启动器 {APP_BIN_PATH}[/success]")

        if Confirm.ask(f"同时删除用户数据 {USER_CONFIG_DIR}？", default=False):
            shutil.rmtree(str(USER_CONFIG_DIR), ignore_errors=True)
            console.print(f"[success]✔ 已删除 {USER_CONFIG_DIR}[/success]")

        console.print("[bold green]Hackingtool 已卸载。再见。[/bold green]")
        sleep(1)
        sys.exit(0)


class ToolManager(HackingToolsCollection):
    TITLE = "更新或卸载 | Hackingtool"
    TOOLS = [
        UpdateTool(),
        UninstallTool(),
    ]


if __name__ == "__main__":
    manager = ToolManager()
    manager.show_options()
