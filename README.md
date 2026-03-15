<div align="center">

# HackingTool

**All-in-One Hacking Tool for Security Researchers & Pentesters**

[![License](https://img.shields.io/github/license/Z4nzu/hackingtool?style=flat-square)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![Version](https://img.shields.io/badge/version-2.0.0-brightgreen?style=flat-square)](#)
[![Platform](https://img.shields.io/badge/platform-Linux%20%7C%20Kali%20%7C%20Parrot%20%7C%20macOS-informational?style=flat-square)](#)
[![Stars](https://img.shields.io/github/stars/Z4nzu/hackingtool?style=flat-square)](https://github.com/Z4nzu/hackingtool/stargazers)
[![Forks](https://img.shields.io/github/forks/Z4nzu/hackingtool?style=flat-square)](https://github.com/Z4nzu/hackingtool/network/members)
[![Issues](https://img.shields.io/github/issues/Z4nzu/hackingtool?style=flat-square)](https://github.com/Z4nzu/hackingtool/issues)
[![Last Commit](https://img.shields.io/github/last-commit/Z4nzu/hackingtool?style=flat-square)](https://github.com/Z4nzu/hackingtool/commits/master)

<br>

```
 17 categories  ·  150+ tools  ·  Linux & macOS  ·  Rich terminal UI
```

</div>

---

## What's New in v2.0.0

| | Change |
|---|---|
| **Python** | 3.10+ required — all Python 2 code removed |
| **OS-aware** | Linux-only tools hidden automatically on macOS |
| **Archived** | Unmaintained tools moved to a separate sub-menu |
| **Paths** | All `os.chdir()` bugs fixed — tools install to `~/.hackingtool/tools/` |
| **Root** | No more `sudo git clone` — installs to user home |
| **New tools** | 22 modern tools added across 6 categories |
| **UI** | Rich terminal UI with shared theme — single consistent console |
| **Menus** | Iterative navigation — no more recursion stack overflow |
| **Docker** | Builds locally — no unverified external images |
| **Deps** | `requirements.txt` cleaned — removed unused flask/boxes/lolcat/requests |

---

## Tool Categories

| # | Category | Tools |
|---|---|:---:|
| 1 | [Anonymously Hiding](#anonymously-hiding-tools) | 2 |
| 2 | [Information Gathering](#information-gathering-tools) | 22 |
| 3 | [Wordlist Generator](#wordlist-generator) | 7 |
| 4 | [Wireless Attack](#wireless-attack-tools) | 12 |
| 5 | [SQL Injection](#sql-injection-tools) | 7 |
| 6 | [Phishing Attack](#phishing-attack-tools) | 17 |
| 7 | [Web Attack](#web-attack-tools) | 13 |
| 8 | [Post Exploitation](#post-exploitation-tools) | 3 |
| 9 | [Forensics](#forensic-tools) | 7 |
| 10 | [Payload Creation](#payload-creation-tools) | 8 |
| 11 | [Exploit Framework](#exploit-framework) | 4 |
| 12 | [Reverse Engineering](#reverse-engineering-tools) | 3 |
| 13 | [DDOS Attack](#ddos-attack-tools) | 5 |
| 14 | [RAT](#remote-administrator-tools-rat) | 1 |
| 15 | [XSS Attack](#xss-attack-tools) | 9 |
| 16 | [Steganography](#steganography-tools) | 4 |
| 17 | [Other Tools](#other-tools) | 24 |

---

## Anonymously Hiding Tools
- [Anonymously Surf](https://github.com/Und3rf10w/kali-anonsurf)
- [Multitor](https://github.com/trimstray/multitor)

## Information Gathering Tools
- [Network Map (nmap)](https://github.com/nmap/nmap)
- [Dracnmap](https://github.com/Screetsec/Dracnmap)
- Port scanning
- Host to IP
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

## Wordlist Generator
- [Cupp](https://github.com/Mebus/cupp)
- [WordlistCreator](https://github.com/Z4nzu/wlcreator)
- [Goblin WordGenerator](https://github.com/UndeadSec/GoblinWordGenerator)
- [Password list (1.4B)](https://github.com/Viralmaniar/SMWYG-Show-Me-What-You-Got)
- [Hashcat](https://github.com/hashcat/hashcat) ★
- [John the Ripper](https://github.com/openwall/john) ★
- [haiti](https://github.com/noraj/haiti) ★

## Wireless Attack Tools
- [WiFi-Pumpkin](https://github.com/P0cL4bs/wifipumpkin3)
- [pixiewps](https://github.com/wiire/pixiewps)
- [Bluetooth Honeypot (bluepot)](https://github.com/andrewmichaelsmith/bluepot)
- [Fluxion](https://github.com/FluxionNetwork/fluxion)
- [Wifiphisher](https://github.com/wifiphisher/wifiphisher)
- [Wifite](https://github.com/derv82/wifite2)
- [EvilTwin](https://github.com/Z4nzu/fakeap)
- [Fastssh](https://github.com/Z4nzu/fastssh)
- Howmanypeople
- [Airgeddon](https://github.com/v1s1t0r1sh3r3/airgeddon) ★
- [hcxdumptool](https://github.com/ZerBea/hcxdumptool) ★
- [hcxtools](https://github.com/ZerBea/hcxtools) ★

## SQL Injection Tools
- [Sqlmap](https://github.com/sqlmapproject/sqlmap)
- [NoSqlMap](https://github.com/codingo/NoSQLMap)
- [DSSS](https://github.com/stamparm/DSSS)
- [Explo](https://github.com/dtag-dev-sec/explo)
- [Blisqy](https://github.com/JohnTroony/Blisqy)
- [Leviathan](https://github.com/leviathan-framework/leviathan)
- [SQLScan](https://github.com/Cvar1984/sqlscan)

## Phishing Attack Tools
- [Autophisher](https://github.com/CodingRanjith/autophisher)
- [PyPhisher](https://github.com/KasRoudra/PyPhisher)
- [AdvPhishing](https://github.com/Ignitetch/AdvPhishing)
- [Setoolkit](https://github.com/trustedsec/social-engineer-toolkit)
- [SocialFish](https://github.com/UndeadSec/SocialFish)
- [HiddenEye](https://github.com/Morsmalleo/HiddenEye)
- [Evilginx3](https://github.com/kgretzky/evilginx2)
- [I-See-You](https://github.com/Viralmaniar/I-See-You)
- [SayCheese](https://github.com/hangetzzu/saycheese)
- [QR Code Jacking](https://github.com/cryptedwolf/ohmyqr)
- [BlackEye](https://github.com/thelinuxchoice/blackeye)
- [ShellPhish](https://github.com/An0nUD4Y/shellphish)
- [Thanos](https://github.com/TridevReddy/Thanos)
- [QRLJacking](https://github.com/OWASP/QRLJacking)
- [Maskphish](https://github.com/jaykali/maskphish)
- [BlackPhish](https://github.com/iinc0gnit0/BlackPhish)
- [dnstwist](https://github.com/elceef/dnstwist)

## Web Attack Tools
- [Web2Attack](https://github.com/santatic/web2attack)
- Skipfish
- [Sublist3r](https://github.com/aboul3la/Sublist3r)
- [CheckURL](https://github.com/UndeadSec/checkURL)
- [Sub-Domain TakeOver](https://github.com/edoardottt/takeover)
- [Dirb](https://gitlab.com/kalilinux/packages/dirb)
- [Nuclei](https://github.com/projectdiscovery/nuclei) ★
- [ffuf](https://github.com/ffuf/ffuf) ★
- [Feroxbuster](https://github.com/epi052/feroxbuster) ★
- [Nikto](https://github.com/sullo/nikto) ★
- [wafw00f](https://github.com/EnableSecurity/wafw00f) ★
- [Katana](https://github.com/projectdiscovery/katana) ★

## Post Exploitation Tools
- [Vegile](https://github.com/Screetsec/Vegile)
- [Chrome Keylogger](https://github.com/UndeadSec/HeraKeylogger)
- [pwncat-cs](https://github.com/calebstewart/pwncat) ★

## Forensic Tools
- Autopsy
- Wireshark
- [Bulk extractor](https://github.com/simsong/bulk_extractor)
- [Guymager](https://guymager.sourceforge.io/)
- [Toolsley](https://www.toolsley.com/)
- [Volatility 3](https://github.com/volatilityfoundation/volatility3) ★
- [Binwalk](https://github.com/ReFirmLabs/binwalk) ★

## Payload Creation Tools
- [The FatRat](https://github.com/Screetsec/TheFatRat)
- [Brutal](https://github.com/Screetsec/Brutal)
- [Stitch](https://nathanlopez.github.io/Stitch)
- [MSFvenom Payload Creator](https://github.com/g0tmi1k/msfpc)
- [Venom](https://github.com/r00t-3xp10it/venom)
- [Spycam](https://github.com/indexnotfound404/spycam)
- [Mob-Droid](https://github.com/kinghacker0/Mob-Droid)
- [Enigma](https://github.com/UndeadSec/Enigma)

## Exploit Framework
- [RouterSploit](https://github.com/threat9/routersploit)
- [WebSploit](https://github.com/The404Hacking/websploit)
- [Commix](https://github.com/commixproject/commix)
- [Web2Attack](https://github.com/santatic/web2attack)

## Reverse Engineering Tools
- [Androguard](https://github.com/androguard/androguard)
- [Apk2Gold](https://github.com/lxdvs/apk2gold)
- [JadX](https://github.com/skylot/jadx)

## DDOS Attack Tools
- [DDoS Script](https://github.com/the-deepnet/ddos)
- [SlowLoris](https://github.com/gkbrk/slowloris)
- [Asyncrone](https://github.com/fatihsnsy/aSYNcrone)
- [UFOnet](https://github.com/epsylon/ufonet)
- [GoldenEye](https://github.com/jseidl/GoldenEye)

## Remote Administrator Tools (RAT)
- [Pyshell](https://github.com/knassar702/pyshell)

## XSS Attack Tools
- [DalFox](https://github.com/hahwul/dalfox)
- [XSS Payload Generator](https://github.com/capture0x/XSS-LOADER)
- [Extended XSS Searcher](https://github.com/Damian89/extended-xss-search)
- [XSS-Freak](https://github.com/PR0PH3CY33/XSS-Freak)
- [XSpear](https://github.com/hahwul/XSpear)
- [XSSCon](https://github.com/menkrep1337/XSSCon)
- [XanXSS](https://github.com/Ekultek/XanXSS)
- [XSStrike](https://github.com/UltimateHackers/XSStrike)
- [RVuln](https://github.com/iinc0gnit0/RVuln)

## Steganography Tools
- SteganoHide
- [StegoCracker](https://github.com/W1LDN16H7/StegoCracker)
- [Whitespace](https://github.com/beardog108/snow10)

## Other Tools

#### SocialMedia Bruteforce
- [AllinOne SocialMedia Attack](https://github.com/Matrix07ksa/Brute_Force)
- [Facebook Attack](https://github.com/Matrix07ksa/Brute_Force)
- [Application Checker](https://github.com/jakuta-tech/underhanded)

#### Android Hacking Tools
- [Keydroid](https://github.com/F4dl0/keydroid)
- [MySMS](https://github.com/papusingh2sms/mysms)
- [Lockphish](https://github.com/JasonJerry/lockphish)
- [DroidCam / WishFish](https://github.com/kinghacker0/WishFish)
- [EvilApp](https://github.com/crypticterminal/EvilApp)

#### IDN Homograph Attack
- [EvilURL](https://github.com/UndeadSec/EvilURL)

#### Email Verify Tools
- [Knockmail](https://github.com/4w4k3/KnockMail)

#### Hash Cracking Tools
- [Hash Buster](https://github.com/s0md3v/Hash-Buster)

#### Wifi Deauthenticate
- [WifiJammer-NG](https://github.com/MisterBianco/wifijammer-ng)
- [KawaiiDeauther](https://github.com/aryanrtm/KawaiiDeauther)

#### SocialMedia Finder
- [Find SocialMedia By Facial Recognition](https://github.com/Greenwolf/social_mapper)
- [Find SocialMedia By UserName](https://github.com/xHak9x/finduser)
- [Sherlock](https://github.com/sherlock-project/sherlock)
- [SocialScan](https://github.com/iojw/socialscan)

#### Payload Injector
- [Debinject](https://github.com/UndeadSec/Debinject)
- [Pixload](https://github.com/chinarulezzz/pixload)

#### Web Crawling
- [Gospider](https://github.com/jaeles-project/gospider)

#### Mix Tools
- Terminal Multiplexer (tilix)
- [Crivo](https://github.com/GMDSantana/crivo)

---

## Contributing — Add a New Tool

### Open an Issue

> **Title format:** `[Tool Request] ToolName — Category`
> Example: `[Tool Request] Subfinder — Information Gathering`

Use the [Tool Request](.github/ISSUE_TEMPLATE/tool_request.md) issue template.
Required fields: tool name, GitHub URL, category, supported OS, install command, reason for inclusion.

### Open a Pull Request

> **Title format:** `[New Tool] ToolName — Category`
> Example: `[New Tool] Subfinder — Information Gathering`

Use the [PR template](.github/PULL_REQUEST_TEMPLATE.md) checklist. Key requirements:

1. Add your class to the right `tools/*.py` file
2. Set `TITLE`, `DESCRIPTION`, `INSTALL_COMMANDS`, `RUN_COMMANDS`, `PROJECT_URL`
3. Set `SUPPORTED_OS` — `["linux"]` or `["linux", "macos"]`
4. Append the instance to `TOOLS` list in the collection at the bottom of the file
5. Test install + run locally before submitting

Issues or PRs that **don't follow the title format** will be closed without review.

---

## Installation

**Requires Python 3.10+**

```bash
git clone https://github.com/Z4nzu/hackingtool.git
cd hackingtool
chmod -R 755 .
sudo python3 install.py
```

Then run:
```bash
sudo hackingtool
```

## Docker

```bash
# Build image
docker build -t hackingtool .

# Run
docker-compose up -d

# Interact
docker exec -it hackingtool bash
```

## Requirements

- Python 3.10+
- Linux (Kali, Parrot, Ubuntu) or macOS
- Go 1.21+ *(for nuclei, ffuf, amass, httpx, katana, dalfox)*
- Ruby *(for haiti)*

```bash
pip install -r requirements.txt
```

---

## Star History

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=Z4nzu/hackingtool&type=Date&theme=dark" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=Z4nzu/hackingtool&type=Date" />
  <img alt="HackingTool Star History Chart" src="https://api.star-history.com/svg?repos=Z4nzu/hackingtool&type=Date" />
</picture>

---

## Social

[![Twitter](https://img.shields.io/twitter/url?color=%231DA1F2&label=follow&logo=twitter&logoColor=%231DA1F2&style=flat-square&url=https%3A%2F%2Ftwitter.com%2F_Zinzu07)](https://twitter.com/_Zinzu07)
[![GitHub](https://img.shields.io/badge/-GitHub-181717?style=flat-square&logo=github&link=https://github.com/Z4nzu/)](https://github.com/Z4nzu/)

> **Please don't use for illegal activity.**
> Thanks to all original authors of the tools included in hackingtool.

Your favourite tool is not listed? [Suggest it here](https://github.com/Z4nzu/hackingtool/issues/new?template=tool_request.md)
