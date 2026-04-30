import os
import shutil
import sys
import webbrowser
from collections.abc import Callable
from platform import system

from rich import box
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.table import Table
from rich.text import Text
from rich.theme import Theme
from rich.traceback import install

from constants import (
    THEME_PRIMARY, THEME_BORDER, THEME_ACCENT,
    THEME_SUCCESS, THEME_ERROR, THEME_WARNING,
    THEME_DIM, THEME_ARCHIVED, THEME_URL,
)

# Enable rich tracebacks globally
install()

_theme = Theme({
    "purple":   "#7B61FF",
    "success":  THEME_SUCCESS,
    "error":    THEME_ERROR,
    "warning":  THEME_WARNING,
    "archived": THEME_ARCHIVED,
    "url":      THEME_URL,
    "dim":      THEME_DIM,
})

# Single shared console — all tool files do: from core import console
console = Console(theme=_theme)


def clear_screen():
    os.system("cls" if system() == "Windows" else "clear")


def validate_input(ip, val_range: list) -> int | None:
    """Return the integer if it is in val_range, else None."""
    if not val_range:
        return None
    try:
        ip = int(ip)
        if ip in val_range:
            return ip
    except (TypeError, ValueError):
        pass
    return None


def _show_inline_help():
    """快速帮助，可在任何菜单级别使用。"""
    console.print(Panel(
        Text.assemble(
            ("  导航\n", "bold white"),
            ("  ─────────────────────────────────\n", "dim"),
            ("  1–N    ", "bold cyan"), ("选择项目\n", "white"),
            ("  97     ", "bold cyan"), ("安装全部 (在分类中)\n", "white"),
            ("\n  工具菜单: 安装、运行、更新、打开文件夹\n", "dim"),
            ("  99     ", "bold cyan"), ("返回\n", "white"),
            ("  98     ", "bold cyan"), ("打开项目页面 / 已归档\n", "white"),
            ("  ?      ", "bold cyan"), ("显示此帮助\n", "white"),
            ("  q      ", "bold cyan"), ("退出 hackingtool\n", "white"),
        ),
        title="[bold magenta] ? 快速帮助 [/bold magenta]",
        border_style="magenta",
        box=box.ROUNDED,
        padding=(0, 2),
    ))
    Prompt.ask("[dim]按回车键返回[/dim]", default="")


class HackingTool:
    TITLE: str              = ""
    DESCRIPTION: str        = ""
    INSTALL_COMMANDS: list[str]  = []
    UNINSTALL_COMMANDS: list[str] = []
    RUN_COMMANDS: list[str]      = []
    OPTIONS: list[tuple[str, Callable]] = []
    PROJECT_URL: str        = ""

    # OS / capability metadata
    SUPPORTED_OS: list[str] = ["linux", "macos"]
    REQUIRES_ROOT: bool     = False
    REQUIRES_WIFI: bool     = False
    REQUIRES_GO: bool       = False
    REQUIRES_RUBY: bool     = False
    REQUIRES_JAVA: bool     = False
    REQUIRES_DOCKER: bool   = False

    # Tags for search/filter (e.g. ["osint", "web", "recon", "scanner"])
    TAGS: list[str]         = []

    # Archived tool flags
    ARCHIVED: bool          = False
    ARCHIVED_REASON: str    = ""

    def __init__(self, options=None, installable=True, runnable=True):
        options = options or []
        if not isinstance(options, list):
            raise TypeError("options 必须是 (option_name, option_fn) 元组的列表")
        self.OPTIONS = []
        if installable:
            self.OPTIONS.append(("安装", self.install))
        if runnable:
            self.OPTIONS.append(("运行", self.run))
        self.OPTIONS.append(("更新", self.update))
        self.OPTIONS.append(("打开文件夹", self.open_folder))
        self.OPTIONS.extend(options)

    @property
    def is_installed(self) -> bool:
        """Check if the tool's binary is on PATH or its clone dir exists."""
        if self.RUN_COMMANDS:
            cmd = self.RUN_COMMANDS[0]
            # Handle "cd foo && binary --help" pattern
            if "&&" in cmd:
                cmd = cmd.split("&&")[-1].strip()
            if cmd.startswith("sudo "):
                cmd = cmd[5:].strip()
            binary = cmd.split()[0] if cmd else ""
            if binary and binary not in (".", "echo", "cd"):
                if shutil.which(binary):
                    return True
        # Check if git clone target dir exists
        if self.INSTALL_COMMANDS:
            for ic in self.INSTALL_COMMANDS:
                if "git clone" in ic:
                    parts = ic.split()
                    repo_url = [p for p in parts if p.startswith("http")]
                    if repo_url:
                        dirname = repo_url[0].rstrip("/").rsplit("/", 1)[-1].replace(".git", "")
                        if os.path.isdir(dirname):
                            return True
        return False

    def show_info(self):
        desc = f"[cyan]{self.DESCRIPTION}[/cyan]"
        if self.PROJECT_URL:
            desc += f"\n[url]🔗 {self.PROJECT_URL}[/url]"
        if self.ARCHIVED:
            desc += f"\n[archived]⚠ 已归档: {self.ARCHIVED_REASON}[/archived]"
        console.print(Panel(
            desc,
            title=f"[{THEME_PRIMARY}]{self.TITLE}[/{THEME_PRIMARY}]",
            border_style="purple",
            box=box.DOUBLE,
        ))

    def show_options(self, parent=None):
        """迭代菜单循环 - 无递归，无堆栈增长。"""
        while True:
            clear_screen()
            self.show_info()

            table = Table(title="选项", box=box.SIMPLE_HEAVY)
            table.add_column("序号", style="bold cyan", justify="center")
            table.add_column("操作", style="bold yellow")

            for index, option in enumerate(self.OPTIONS):
                table.add_row(str(index + 1), option[0])

            if self.PROJECT_URL:
                table.add_row("98", "打开项目页面")
            table.add_row("99", f"返回 {parent.TITLE if parent else '主菜单'}")
            console.print(table)
            console.print(
                "  [dim cyan]?[/dim cyan][dim]帮助  "
                "[/dim][dim cyan]q[/dim cyan][dim]退出  "
                "[/dim][dim cyan]99[/dim cyan][dim] 返回[/dim]"
            )

            raw = Prompt.ask("[bold cyan]╰─>[/bold cyan]", default="").strip().lower()
            if not raw:
                continue
            if raw in ("?", "help"):
                _show_inline_help()
                continue
            if raw in ("q", "quit", "exit"):
                raise SystemExit(0)

            try:
                choice = int(raw)
            except ValueError:
                console.print("[error]⚠ 请输入数字、? 获取帮助或 q 退出。[/error]")
                Prompt.ask("[dim]按回车键继续[/dim]", default="")
                continue

            if choice == 99:
                return
            elif choice == 98 and self.PROJECT_URL:
                self.show_project_page()
            elif 1 <= choice <= len(self.OPTIONS):
                try:
                    self.OPTIONS[choice - 1][1]()
                except Exception:
                    console.print_exception(show_locals=True)
                Prompt.ask("[dim]按回车键继续[/dim]", default="")
            else:
                console.print("[error]⚠ 无效选项。[/error]")

    def before_install(self): pass

    def install(self):
        self.before_install()
        if isinstance(self.INSTALL_COMMANDS, (list, tuple)):
            for cmd in self.INSTALL_COMMANDS:
                console.print(f"[warning]→ {cmd}[/warning]")
                os.system(cmd)
        self.after_install()

    def after_install(self):
        console.print("[success]✔ 安装成功！[/success]")

    def before_uninstall(self) -> bool:
        return True

    def uninstall(self):
        if self.before_uninstall():
            if isinstance(self.UNINSTALL_COMMANDS, (list, tuple)):
                for cmd in self.UNINSTALL_COMMANDS:
                    console.print(f"[error]→ {cmd}[/error]")
                    os.system(cmd)
        self.after_uninstall()

    def after_uninstall(self): pass

    def update(self):
        """智能更新 - 检测安装方式并运行正确的更新命令。"""
        if not self.is_installed:
            console.print("[warning]工具尚未安装。请先安装。[/warning]")
            return

        updated = False
        for ic in (self.INSTALL_COMMANDS or []):
            if "git clone" in ic:
                # 从 clone 命令中提取仓库目录名
                parts = ic.split()
                repo_urls = [p for p in parts if p.startswith("http")]
                if repo_urls:
                    dirname = repo_urls[0].rstrip("/").rsplit("/", 1)[-1].replace(".git", "")
                    if os.path.isdir(dirname):
                        console.print(f"[cyan]→ git -C {dirname} pull[/cyan]")
                        os.system(f"git -C {dirname} pull")
                        updated = True
            elif "pip install" in ic:
                # 重新运行 pip install (--upgrade)
                upgrade_cmd = ic.replace("pip install", "pip install --upgrade")
                console.print(f"[cyan]→ {upgrade_cmd}[/cyan]")
                os.system(upgrade_cmd)
                updated = True
            elif "go install" in ic:
                # 重新运行 go install (获取最新版本)
                console.print(f"[cyan]→ {ic}[/cyan]")
                os.system(ic)
                updated = True
            elif "gem install" in ic:
                upgrade_cmd = ic.replace("gem install", "gem update")
                console.print(f"[cyan]→ {upgrade_cmd}[/cyan]")
                os.system(upgrade_cmd)
                updated = True

        if updated:
            console.print("[success]✔ 更新完成！[/success]")
        else:
            console.print("[dim]此工具没有自动更新方法。[/dim]")

    def _get_tool_dir(self) -> str | None:
        """查找工具的本地目录 - clone 目标、pip 位置或二进制路径。"""
        # 1. 检查 git clone 目标目录
        for ic in (self.INSTALL_COMMANDS or []):
            if "git clone" in ic:
                parts = ic.split()
                # 如果最后一个参数不是 URL，则是自定义目录名
                repo_urls = [p for p in parts if p.startswith("http")]
                if repo_urls:
                    dirname = repo_urls[0].rstrip("/").rsplit("/", 1)[-1].replace(".git", "")
                    # 检查自定义目标目录 (URL 后的参数)
                    url_idx = parts.index(repo_urls[0])
                    if url_idx + 1 < len(parts):
                        dirname = parts[url_idx + 1]
                    if os.path.isdir(dirname):
                        return os.path.abspath(dirname)

        # 2. 通过 which 检查二进制位置
        if self.RUN_COMMANDS:
            cmd = self.RUN_COMMANDS[0]
            if "&&" in cmd:
                # "cd foo && bar" → 检查 "foo"
                cd_part = cmd.split("&&")[0].strip()
                if cd_part.startswith("cd "):
                    d = cd_part[3:].strip()
                    if os.path.isdir(d):
                        return os.path.abspath(d)
            binary = cmd.split()[0] if cmd else ""
            if binary.startswith("sudo"):
                binary = cmd.split()[1] if len(cmd.split()) > 1 else ""
            path = shutil.which(binary) if binary else None
            if path:
                return os.path.dirname(os.path.realpath(path))

        return None

    def open_folder(self):
        """在新 shell 中打开工具的目录，以便用户手动操作。"""
        tool_dir = self._get_tool_dir()
        if tool_dir:
            console.print(f"[success]正在打开文件夹: {tool_dir}[/success]")
            console.print("[dim]输入 'exit' 返回 hackingtool。[/dim]")
            os.system(f'cd "{tool_dir}" && $SHELL')
        else:
            console.print("[warning]未找到工具目录。[/warning]")
            if self.PROJECT_URL:
                console.print(f"[dim]您可以手动 clone:[/dim]")
                console.print(f"[cyan]  git clone {self.PROJECT_URL}.git[/cyan]")

    def before_run(self): pass

    def run(self):
        self.before_run()
        if isinstance(self.RUN_COMMANDS, (list, tuple)):
            for cmd in self.RUN_COMMANDS:
                console.print(f"[cyan]⚙ 正在运行:[/cyan] [bold]{cmd}[/bold]")
                os.system(cmd)
        self.after_run()

    def after_run(self): pass

    def show_project_page(self):
        console.print(f"[url]🌐 正在打开: {self.PROJECT_URL}[/url]")
        webbrowser.open_new_tab(self.PROJECT_URL)


class HackingToolsCollection:
    TITLE: str       = ""
    DESCRIPTION: str = ""
    TOOLS: list      = []

    def __init__(self):
        pass

    def show_info(self):
        console.rule(f"[{THEME_PRIMARY}]{self.TITLE}[/{THEME_PRIMARY}]", style="purple")
        if self.DESCRIPTION:
            console.print(f"[italic cyan]{self.DESCRIPTION}[/italic cyan]\n")

    def _active_tools(self) -> list:
        """返回未归档且与操作系统兼容的工具。"""
        from os_detect import CURRENT_OS
        return [
            t for t in self.TOOLS
            if not getattr(t, "ARCHIVED", False)
            and CURRENT_OS.system in getattr(t, "SUPPORTED_OS", ["linux", "macos"])
        ]

    def _archived_tools(self) -> list:
        return [t for t in self.TOOLS if getattr(t, "ARCHIVED", False)]

    def _incompatible_tools(self) -> list:
        from os_detect import CURRENT_OS
        return [
            t for t in self.TOOLS
            if not getattr(t, "ARCHIVED", False)
            and CURRENT_OS.system not in getattr(t, "SUPPORTED_OS", ["linux", "macos"])
        ]

    def _show_archived_tools(self):
        """显示已归档工具子菜单 (选项 98)。"""
        archived = self._archived_tools()
        if not archived:
            console.print("[dim]此分类中没有已归档的工具。[/dim]")
            Prompt.ask("[dim]按回车键返回[/dim]", default="")
            return

        while True:
            clear_screen()
            console.rule(f"[archived]已归档工具 — {self.TITLE}[/archived]", style="yellow")

            table = Table(box=box.MINIMAL_DOUBLE_HEAD, show_lines=True)
            table.add_column("序号", justify="center", style="bold yellow")
            table.add_column("工具", style="dim yellow")
            table.add_column("原因", style="dim white")

            for i, tool in enumerate(archived):
                reason = getattr(tool, "ARCHIVED_REASON", "未说明原因")
                table.add_row(str(i + 1), tool.TITLE, reason)

            table.add_row("99", "返回", "")
            console.print(table)

            raw = Prompt.ask("[bold yellow][?] 选择[/bold yellow]", default="99")
            try:
                choice = int(raw)
            except ValueError:
                continue

            if choice == 99:
                return
            elif 1 <= choice <= len(archived):
                archived[choice - 1].show_options(parent=self)

    def show_options(self, parent=None):
        """迭代菜单循环 - 无递归，无堆栈增长。"""
        while True:
            clear_screen()
            self.show_info()

            active = self._active_tools()
            incompatible = self._incompatible_tools()
            archived = self._archived_tools()

            table = Table(title="可用工具", box=box.SIMPLE_HEAD, show_lines=True)
            table.add_column("序号", justify="center", style="bold cyan", width=6)
            table.add_column("", width=2)  # 已安装指示器
            table.add_column("工具", style="bold yellow", min_width=24)
            table.add_column("描述", style="white", overflow="fold")

            for index, tool in enumerate(active, start=1):
                desc = getattr(tool, "DESCRIPTION", "") or "—"
                desc = desc.splitlines()[0] if desc != "—" else "—"
                has_status = hasattr(tool, "is_installed")
                status = ("[green]✔[/green]" if tool.is_installed else "[dim]✘[/dim]") if has_status else ""
                table.add_row(str(index), status, tool.TITLE, desc)

            # 统计未安装的工具数量以显示"全部安装"标签 (跳过子集合)
            not_installed = [t for t in active if hasattr(t, "is_installed") and not t.is_installed]
            if not_installed:
                table.add_row(
                    "[bold green]97[/bold green]", "",
                    f"[bold green]全部安装 ({len(not_installed)} 个未安装)[/bold green]", "",
                )
            if archived:
                table.add_row("[dim]98[/dim]", "", f"[archived]已归档工具 ({len(archived)})[/archived]", "")
            if incompatible:
                console.print(f"[dim]({len(incompatible)} 个工具已隐藏 - 当前操作系统不支持)[/dim]")

            table.add_row("99", "", f"返回 {parent.TITLE if parent else '主菜单'}", "")
            console.print(table)
            console.print(
                "  [dim cyan]?[/dim cyan][dim]帮助  "
                "[/dim][dim cyan]q[/dim cyan][dim]退出  "
                "[/dim][dim cyan]99[/dim cyan][dim] 返回[/dim]"
            )

            raw = Prompt.ask("[bold cyan]╰─>[/bold cyan]", default="").strip().lower()
            if not raw:
                continue
            if raw in ("?", "help"):
                _show_inline_help()
                continue
            if raw in ("q", "quit", "exit"):
                raise SystemExit(0)

            try:
                choice = int(raw)
            except ValueError:
                console.print("[error]⚠ 请输入数字、? 获取帮助或 q 退出。[/error]")
                continue

            if choice == 99:
                return
            elif choice == 97 and not_installed:
                console.print(Panel(
                    f"[bold]正在安装 {len(not_installed)} 个工具...[/bold]",
                    border_style="green", box=box.ROUNDED,
                ))
                for i, tool in enumerate(not_installed, start=1):
                    console.print(f"\n[bold cyan]({i}/{len(not_installed)})[/bold cyan] {tool.TITLE}")
                    try:
                        tool.install()
                    except Exception:
                        console.print(f"[error]✘ 失败: {tool.TITLE}[/error]")
                Prompt.ask("\n[dim]按回车键继续[/dim]", default="")
            elif choice == 98 and archived:
                self._show_archived_tools()
            elif 1 <= choice <= len(active):
                try:
                    active[choice - 1].show_options(parent=self)
                except Exception:
                    console.print_exception(show_locals=True)
                    Prompt.ask("[dim]按回车键继续[/dim]", default="")
            else:
                console.print("[error]⚠ 无效选项。[/error]")
