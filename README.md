<div align="center">

<img src="images/logo.svg" alt="HackingTool" width="600">

<p><b>安全研究人员和渗透测试人员的一站式黑客工具</b></p>

[![License](https://img.shields.io/github/license/Z4nzu/hackingtool)](LICENSE)&nbsp;
[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)&nbsp;
[![Version](https://img.shields.io/badge/v2.0.0-00FF88?style=flat-square)](#)&nbsp;
[![Stars](https://img.shields.io/github/stars/Z4nzu/hackingtool?style=flat-square&color=yellow)](https://github.com/Z4nzu/hackingtool/stargazers)&nbsp;
[![Forks](https://img.shields.io/github/forks/Z4nzu/hackingtool?style=flat-square&color=blue)](https://github.com/Z4nzu/hackingtool/network/members)&nbsp;
[![Issues](https://img.shields.io/github/issues/Z4nzu/hackingtool?style=flat-square&color=red)](https://github.com/Z4nzu/hackingtool/issues)&nbsp;
[![Last Commit](https://img.shields.io/github/last-commit/Z4nzu/hackingtool?style=flat-square&color=00FF88)](https://github.com/Z4nzu/hackingtool/commits/master)

![](https://img.shields.io/badge/20_Categories-7B61FF?style=for-the-badge)
![](https://img.shields.io/badge/185+_Tools-00FF88?style=for-the-badge)
![](https://img.shields.io/badge/19_Tags-FF61DC?style=for-the-badge)
![](https://img.shields.io/badge/Linux_%7C_Kali_%7C_Parrot_%7C_macOS-FFA116?style=for-the-badge&logo=linux&logoColor=white)

<a href="#installation"><img src="https://img.shields.io/badge/Install_Now-00FF88?style=for-the-badge&logo=rocket&logoColor=black" alt="立即安装"></a>&nbsp;
<a href="#quick-commands"><img src="https://img.shields.io/badge/Quick_Commands-7B61FF?style=for-the-badge&logo=terminal&logoColor=white" alt="快速命令"></a>&nbsp;
<a href="https://github.com/Z4nzu/hackingtool/issues/new?template=tool_request.md"><img src="https://img.shields.io/badge/Suggest_a_Tool-FF61DC?style=for-the-badge&logo=plus&logoColor=white" alt="推荐工具"></a>

</div>

---


## v2.0.0 新功能

<table>
<tr><td>

| | 功能 | 描述 |
|:---:|---|---|
| **🐍** | **Python 3.10+** | 移除所有 Python 2 代码，全面使用现代语法 |
| **🖥** | **操作系统感知菜单** | 在 macOS 上自动隐藏仅 Linux 工具 |
| **📦** | **185+ 工具** | 在 6 个类别中新增 35 个现代工具 |
| **🔍** | **搜索** | 输入 `/` 按名称、描述或关键词搜索所有工具 |
| **🏷** | **标签过滤** | 输入 `t` 按 19 个标签过滤 — osint、web、c2、cloud、mobile... |
| **💡** | **推荐** | 输入 `r` — "我想扫描网络" → 显示相关工具 |
| **✅** | **安装状态** | 每个工具旁显示 ✔/✘ — 了解已准备就绪的工具 |
| **⚡** | **一键安装** | 在任何类别中选择 `97` — 批量安装所有工具 |
| **🔄** | **智能更新** | 每个工具都有更新选项 — 自动检测 git pull / pip upgrade / go install |
| **📂** | **打开文件夹** | 进入任何工具的目录进行手动检查 |
| **🐳** | **Docker** | 本地构建 — 无需未经验证的外部镜像 |
| **🚀** | **一行命令安装** | `curl -sSL .../install.sh | sudo bash` — 零手动步骤 |
| **🏢** | **3 个新类别** | 活动目录、云安全、移动安全 |

</td></tr>
</table>



---

## 快速命令

<div align="center">

| 命令 | 功能 | 适用位置 |
|:---:|---|:---:|
| `/query` | **搜索** — 按关键词即时查找工具 | 主菜单 |
| `t` | **标签** — 按 osint、scanner、c2、cloud、mobile 等过滤 | 主菜单 |
| `r` | **推荐** — "我想做 X" → 匹配的工具 | 主菜单 |
| `?` | **帮助** — 快速参考卡片 | 任何位置 |
| `q` | **退出** — 从任何深度退出 | 任何位置 |
| `97` | **全部安装** — 批量安装类别中的所有工具 | 类别 |
| `99` | **返回** — 返回上一级菜单 | 任何位置 |

</div>

---

## 工具分类

<div align="center">

| # | 类别 | 工具数 | | # | 类别 | 工具数 |
|:---:|---|:---:|---|:---:|---|:---:|
| 1 | 🛡 [匿名隐藏](#匿名隐藏工具) | 2 | | 11 | 🧰 [漏洞利用框架](#漏洞利用框架) | 4 |
| 2 | 🔍 [信息收集](#信息收集工具) | 26 | | 12 | 🔁 [逆向工程](#逆向工程工具) | 5 |
| 3 | 📚 [字典生成器](#字典生成器) | 7 | | 13 | ⚡ [DDOS 攻击](#ddos-攻击工具) | 5 |
| 4 | 📶 [无线攻击](#无线攻击工具) | 13 | | 14 | 🖥 [远程管理工具](#远程管理工具-rat) | 1 |
| 5 | 🧩 [SQL 注入](#sql-注入工具) | 7 | | 15 | 💥 [XSS 攻击](#xss-攻击工具) | 9 |
| 6 | 🎣 [钓鱼攻击](#钓鱼攻击工具) | 17 | | 16 | 🖼 [隐写术](#隐写术工具) | 4 |
| 7 | 🌐 [Web 攻击](#web-攻击工具) | 20 | | 17 | 🏢 [活动目录](#活动目录工具) | 6 |
| 8 | 🔧 [后渗透攻击](#后渗透攻击工具) | 10 | | 18 | ☁ [云安全](#云安全工具) | 4 |
| 9 | 🕵 [数字取证](#数字取证工具) | 8 | | 19 | 📱 [移动安全](#移动安全工具) | 3 |
| 10 | 📦 [负载创建](#负载创建工具) | 8 | | 20 | ✨ [其他工具](#其他工具) | 24 |

</div>



---

## 🛡 匿名隐藏工具

- [Anonymously Surf](https://github.com/Und3rf10w/kali-anonsurf)
- [Multitor](https://github.com/trimstray/multitor)



## 🔍 信息收集工具

- [Network Map (nmap)](https://github.com/nmap/nmap)
- [Dracnmap](https://github.com/Screetsec/Dracnmap)
- 端口扫描
- 主机转 IP
- [Xerosploit](https://github.com/LionSec/xerosploit)
- [RED HAWK](https://github.com/Tuhinshubhra/RED_HAWK)
- [ReconSpider](https://github.com/bhavsec/reconspider)
- IsItDown
- [Infoga](https://github.com/m4ll0k/Infoga)
- [ReconDog](https://github.com/s0md3v/ReconDog)
- [Striker](https://github.com/s0md3v/Striker)
- [SecretFinder](https://github.com/m4ll0k/SecretFinder)
- [Shodanfy](https://github.com/m4ll0k/Shodanfy.py)
- [rang3r](https://github.com/floriankunushevci/rang3r)
- [Breacher](https://github.com/s0md3v/Breacher)
- [theHarvester](https://github.com/laramies/theHarvester) ★
- [Amass](https://github.com/owasp-amass/amass) ★
- [Masscan](https://github.com/robertdavidgraham/masscan) ★
- [RustScan](https://github.com/RustScan/RustScan) ★
- [Holehe](https://github.com/megadose/holehe) ★
- [Maigret](https://github.com/soxoj/maigret) ★
- [httpx](https://github.com/projectdiscovery/httpx) ★
- [SpiderFoot](https://github.com/smicallef/spiderfoot) ★
- [Subfinder](https://github.com/projectdiscovery/subfinder) ★
- [TruffleHog](https://github.com/trufflesecurity/trufflehog) ★
- [Gitleaks](https://github.com/gitleaks/gitleaks) ★



## 📚 字典生成器

- [Cupp](https://github.com/Mebus/cupp)
- [WordlistCreator](https://github.com/Z4nzu/wlcreator)
- [Goblin WordGenerator](https://github.com/UndeadSec/GoblinWordGenerator)
- [密码字典 (14亿)](https://github.com/Viralmaniar/SMWYG-Show-Me-What-You-Got)
- [Hashcat](https://github.com/hashcat/hashcat) ★
- [John the Ripper](https://github.com/openwall/john) ★
- [haiti](https://github.com/noraj/haiti) ★



## 📶 无线攻击工具

- [WiFi-Pumpkin](https://github.com/P0cL4bs/wifipumpkin3)
- [pixiewps](https://github.com/wiire/pixiewps)
- [蓝牙蜜罐 (bluepot)](https://github.com/andrewmichaelsmith/bluepot)
- [Fluxion](https://github.com/FluxionNetwork/fluxion)
- [Wifiphisher](https://github.com/wifiphisher/wifiphisher)
- [Wifite](https://github.com/derv82/wifite2)
- [EvilTwin](https://github.com/Z4nzu/fakeap)
- [Fastssh](https://github.com/Z4nzu/fastssh)
- Howmanypeople
- [Airgeddon](https://github.com/v1s1t0r1sh3r3/airgeddon) ★
- [hcxdumptool](https://github.com/ZerBea/hcxdumptool) ★
- [hcxtools](https://github.com/ZerBea/hcxtools) ★
- [Bettercap](https://github.com/bettercap/bettercap) ★



## 🧩 SQL 注入工具

- [Sqlmap](https://github.com/sqlmapproject/sqlmap)
- [NoSqlMap](https://github.com/codingo/NoSQLMap)
- [DSSS](https://github.com/stamparm/DSSS)
- [Explo](https://github.com/dtag-dev-sec/explo)
- [Blisqy](https://github.com/JohnTroony/Blisqy)
- [Leviathan](https://github.com/leviathan-framework/leviathan)
- [SQLScan](https://github.com/Cvar1984/sqlscan)



## 🎣 钓鱼攻击工具

- [Autophisher](https://github.com/CodingRanjith/autophisher)
- [PyPhisher](https://github.com/KasRoudra/PyPhisher)
- [AdvPhishing](https://github.com/Ignitetch/AdvPhishing)
- [Setoolkit](https://github.com/trustedsec/social-engineer-toolkit)
- [SocialFish](https://github.com/UndeadSec/SocialFish)
- [HiddenEye](https://github.com/Morsmalleo/HiddenEye)
- [Evilginx3](https://github.com/kgretzky/evilginx2)
- [I-See-You](https://github.com/Viralmaniar/I-See-You)
- [SayCheese](https://github.com/hangetzzu/saycheese)
- [二维码劫持](https://github.com/cryptedwolf/ohmyqr)
- [BlackEye](https://github.com/thelinuxchoice/blackeye)
- [ShellPhish](https://github.com/An0nUD4Y/shellphish)
- [Thanos](https://github.com/TridevReddy/Thanos)
- [QRLJacking](https://github.com/OWASP/QRLJacking)
- [Maskphish](https://github.com/jaykali/maskphish)
- [BlackPhish](https://github.com/iinc0gnit0/BlackPhish)
- [dnstwist](https://github.com/elceef/dnstwist)



## 🌐 Web 攻击工具

- [Web2Attack](https://github.com/santatic/web2attack)
- Skipfish
- [Sublist3r](https://github.com/aboul3la/Sublist3r)
- [CheckURL](https://github.com/UndeadSec/checkURL)
- [子域名接管](https://github.com/edoardottt/takeover)
- [Dirb](https://gitlab.com/kalilinux/packages/dirb)
- [Nuclei](https://github.com/projectdiscovery/nuclei) ★
- [ffuf](https://github.com/ffuf/ffuf) ★
- [Feroxbuster](https://github.com/epi052/feroxbuster) ★
- [Nikto](https://github.com/sullo/nikto) ★
- [wafw00f](https://github.com/EnableSecurity/wafw00f) ★
- [Katana](https://github.com/projectdiscovery/katana) ★
- [Gobuster](https://github.com/OJ/gobuster) ★
- [Dirsearch](https://github.com/maurosoria/dirsearch) ★
- [OWASP ZAP](https://github.com/zaproxy/zaproxy) ★
- [testssl.sh](https://github.com/drwetter/testssl.sh) ★
- [Arjun](https://github.com/s0md3v/Arjun) ★
- [Caido](https://github.com/caido/caido) ★
- [mitmproxy](https://github.com/mitmproxy/mitmproxy) ★



## 🔧 后渗透攻击工具

- [Vegile](https://github.com/Screetsec/Vegile)
- [Chrome 键盘记录器](https://github.com/UndeadSec/HeraKeylogger)
- [pwncat-cs](https://github.com/calebstewart/pwncat) ★
- [Sliver](https://github.com/BishopFox/sliver) ★
- [Havoc](https://github.com/HavocFramework/Havoc) ★
- [PEASS-ng (LinPEAS/WinPEAS)](https://github.com/peass-ng/PEASS-ng) ★
- [Ligolo-ng](https://github.com/nicocha30/ligolo-ng) ★
- [Chisel](https://github.com/jpillora/chisel) ★
- [Evil-WinRM](https://github.com/Hackplayers/evil-winrm) ★
- [Mythic](https://github.com/its-a-feature/Mythic) ★



## 🕵 数字取证工具

- Autopsy
- Wireshark
- [Bulk extractor](https://github.com/simsong/bulk_extractor)
- [Guymager](https://guymager.sourceforge.io/)
- [Toolsley](https://www.toolsley.com/)
- [Volatility 3](https://github.com/volatilityfoundation/volatility3) ★
- [Binwalk](https://github.com/ReFirmLabs/binwalk) ★
- [pspy](https://github.com/DominicBreuker/pspy) ★



## 📦 负载创建工具

- [The FatRat](https://github.com/Screetsec/TheFatRat)
- [Brutal](https://github.com/Screetsec/Brutal)
- [Stitch](https://nathanlopez.github.io/Stitch)
- [MSFvenom 负载创建器](https://github.com/g0tmi1k/msfpc)
- [Venom](https://github.com/r00t-3xp10it/venom)
- [Spycam](https://github.com/indexnotfound404/spycam)
- [Mob-Droid](https://github.com/kinghacker0/Mob-Droid)
- [Enigma](https://github.com/UndeadSec/Enigma)



## 🧰 漏洞利用框架

- [RouterSploit](https://github.com/threat9/routersploit)
- [WebSploit](https://github.com/The404Hacking/websploit)
- [Commix](https://github.com/commixproject/commix)
- [Web2Attack](https://github.com/santatic/web2attack)



## 🔁 逆向工程工具

- [Androguard](https://github.com/androguard/androguard)
- [Apk2Gold](https://github.com/lxdvs/apk2gold)
- [JadX](https://github.com/skylot/jadx)
- [Ghidra](https://github.com/NationalSecurityAgency/ghidra) ★
- [Radare2](https://github.com/radareorg/radare2) ★



## ⚡ DDOS 攻击工具

- [DDoS 脚本](https://github.com/the-deepnet/ddos)
- [SlowLoris](https://github.com/gkbrk/slowloris)
- [Asyncrone](https://github.com/fatihsnsy/aSYNcrone)
- [UFOnet](https://github.com/epsylon/ufonet)
- [GoldenEye](https://github.com/jseidl/GoldenEye)



## 🖥 远程管理工具 (RAT)

- [Pyshell](https://github.com/knassar702/pyshell)



## 💥 XSS 攻击工具

- [DalFox](https://github.com/hahwul/dalfox)
- [XSS 负载生成器](https://github.com/capture0x/XSS-LOADER)
- [扩展型 XSS 搜索器](https://github.com/Damian89/extended-xss-search)
- [XSS-Freak](https://github.com/PR0PH3CY33/XSS-Freak)
- [XSpear](https://github.com/hahwul/XSpear)
- [XSSCon](https://github.com/menkrep1337/XSSCon)
- [XanXSS](https://github.com/Ekultek/XanXSS)
- [XSStrike](https://github.com/UltimateHackers/XSStrike)
- [RVuln](https://github.com/iinc0gnit0/RVuln)



## 🖼 隐写术工具

- SteganoHide
- [StegoCracker](https://github.com/W1LDN16H7/StegoCracker)
- [Whitespace](https://github.com/beardog108/snow10)



## 🏢 活动目录工具

- [BloodHound](https://github.com/BloodHoundAD/BloodHound) ★
- [NetExec (nxc)](https://github.com/Pennyw0rth/NetExec) ★
- [Impacket](https://github.com/fortra/impacket) ★
- [Responder](https://github.com/lgandx/Responder) ★
- [Certipy](https://github.com/ly4k/Certipy) ★
- [Kerbrute](https://github.com/ropnop/kerbrute) ★



## ☁ 云安全工具

- [Prowler](https://github.com/prowler-cloud/prowler) ★
- [ScoutSuite](https://github.com/nccgroup/ScoutSuite) ★
- [Pacu](https://github.com/RhinoSecurityLabs/pacu) ★
- [Trivy](https://github.com/aquasecurity/trivy) ★



## 📱 移动安全工具

- [MobSF](https://github.com/MobSF/Mobile-Security-Framework-MobSF) ★
- [Frida](https://github.com/frida/frida) ★
- [Objection](https://github.com/sensepost/objection) ★



## ✨ 其他工具

#### 社交媒体暴力破解
- [社交媒体攻击一体化工具](https://github.com/Matrix07ksa/Brute_Force)
- [Facebook 攻击](https://github.com/Matrix07ksa/Brute_Force)
- [应用程序检查器](https://github.com/jakuta-tech/underhanded)

#### Android 黑客工具
- [Keydroid](https://github.com/F4dl0/keydroid)
- [MySMS](https://github.com/papusingh2sms/mysms)
- [Lockphish](https://github.com/JasonJerry/lockphish)
- [DroidCam / WishFish](https://github.com/kinghacker0/WishFish)
- [EvilApp](https://github.com/crypticterminal/EvilApp)

#### IDN 同形异义攻击
- [EvilURL](https://github.com/UndeadSec/EvilURL)

#### 邮箱验证工具
- [Knockmail](https://github.com/4w4k3/KnockMail)

#### 哈希破解工具
- [Hash Buster](https://github.com/s0md3v/Hash-Buster)

#### WiFi 解除认证
- [WifiJammer-NG](https://github.com/MisterBianco/wifijammer-ng)
- [KawaiiDeauther](https://github.com/aryanrtm/KawaiiDeauther)

#### 社交媒体查找器
- [通过面部识别查找社交媒体](https://github.com/Greenwolf/social_mapper)
- [通过用户名查找社交媒体](https://github.com/xHak9x/finduser)
- [Sherlock](https://github.com/sherlock-project/sherlock)
- [SocialScan](https://github.com/iojw/socialscan)

#### 负载注入器
- [Debinject](https://github.com/UndeadSec/Debinject)
- [Pixload](https://github.com/chinarulezzz/pixload)

#### Web 爬虫
- [Gospider](https://github.com/jaeles-project/gospider)

#### 混合工具
- 终端多路复用器 (tilix)
- [Crivo](https://github.com/GMDSantana/crivo)


---

## 贡献指南 — 添加新工具

<table>
<tr>
<td width="50%">

### 提交 Issue

> **标题:** `[工具请求] 工具名称 — 类别`

使用 [工具请求模板](.github/ISSUE_TEMPLATE/tool_request.md)。

必需：工具名称、GitHub URL、类别、操作系统、安装命令、原因。

</td>
<td width="50%">

### 提交 Pull Request

> **标题:** `[新工具] 工具名称 — 类别`

使用 [PR 模板](.github/PULL_REQUEST_TEMPLATE.md) 清单。

必需：`tools/*.py` 中的类、TITLE、DESCRIPTION、INSTALL/RUN 命令、SUPPORTED_OS、本地测试。

</td>
</tr>
</table>

> 不遵循标题格式的 Issue 或 PR 将被关闭而不进行审查。

---

## 安装

<table>
<tr>
<td>

### 一行命令安装（推荐）

```bash
curl -sSL https://raw.githubusercontent.com/Z4nzu/hackingtool/master/install.sh | sudo bash
```

自动处理所有内容 — 先决条件、克隆、venv、启动器。

</td>
<td>

### 手动安装

```bash
git clone https://github.com/Z4nzu/hackingtool.git
cd hackingtool
sudo python3 install.py
```

然后运行: `hackingtool`

</td>
</tr>
</table>


### Docker

```bash
# 构建
docker build -t hackingtool .

# 运行（直接）
docker run -it --rm hackingtool

# 运行（Compose — 推荐）
docker compose up -d
docker exec -it hackingtool bash

# 开发模式（实时源码挂载）
docker compose --profile dev up
docker exec -it hackingtool-dev bash

# 停止
docker compose down        # 停止容器
docker compose down -v     # 同时删除数据卷
```



### 系统要求

| 依赖项 | 版本 | 用途 |
|---|---|---|
| Python | 3.10+ | 核心 |
| Go | 1.21+ | nuclei, ffuf, amass, httpx, katana, dalfox, gobuster, subfinder |
| Ruby | 任意 | haiti, evil-winrm |
| Docker | 任意 | Mythic, MobSF（可选） |

```bash
pip install -r requirements.txt
```

---

## Star 历史

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=Z4nzu/hackingtool&type=Date&theme=dark" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=Z4nzu/hackingtool&type=Date" />
  <img alt="HackingTool Star 历史图表" src="https://api.star-history.com/svg?repos=Z4nzu/hackingtool&type=Date" />
</picture>

---

## 支持

如果这个项目对您有帮助，可以请我喝杯咖啡：

<a href="https://buymeacoffee.com/hardikzinzu" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="请我喝杯咖啡" height="50"></a>

## 社交媒体

[![Twitter](https://img.shields.io/badge/Twitter-Follow-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/_Zinzu07)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Z4nzu/)

> **仅用于授权的安全测试。**
> 感谢所有包含在 hackingtool 中的工具的原作者。

您喜欢的工具没有列出？[在这里推荐](https://github.com/Z4nzu/hackingtool/issues/new?template=tool_request.md)
