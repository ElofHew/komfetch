<div align="center">

# KomFetch

一款适用于Quarter OS的快速查看系统信息的第三方应用程序。

![GitHub Repo Size](https://img.shields.io/github/repo-size/ElofHew/komfetch)
![GitHub Repo Stars](https://img.shields.io/github/stars/ElofHew/komfetch?style=flat)
![Github License](https://img.shields.io/github/license/ElofHew/komfetch?style=flat)
![GitHub Commit activity](https://img.shields.io/github/commit-activity/t/ElofHew/komfetch)
![GitHub Last Commit](https://img.shields.io/github/last-commit/ElofHew/komfetch)
![GitHub Created At](https://img.shields.io/github/created-at/ElofHew/komfetch)
![GitHub Issues](https://img.shields.io/github/issues/ElofHew/komfetch)
![GitHub Release](https://img.shields.io/github/v/release/ElofHew/komfetch)

</div>

## 介绍

KomFetch是一款适用于**Quarter OS**的快速查看系统信息的第三方应用程序。

它的功能类似于Linux上的 `neofetch` 应用程序：

![neofetch截图](img/neofetch.png)

## 截图

![KomFetch截图](img/komfetch.png)

## 用处

### Quarter OS 系统信息

- `OS`: 系统名称 (名称+版本号/版本代码)
- `Path` : 系统路径 (当前系统的工作目录)
- `Login` : 当前登录的用户 (用户名-主机名)
- `Shell` : 当前使用的Shell (目前只能是KomShell)
- `Packages` : 已安装的软件包数量 (Biscuit & Shizuku)
- `Edition` : 系统激活版本 (如果未激活则为空)

### 宿主机系统信息

- `Platform` : 宿主机系统平台 (Windows|Linux|MacOS+系统版本)
- `Version` : 宿主机系统版本 (具体的发行版本号)
- `Node` : 设备名称 (如：DESKTOP-D6A6N6)
- `Arch` : 系统架构 (如：AMD64/aarch64)
- `CPU` : 设备处理器 (可能不是具体名称)

### Python 环境信息

- `Python` : Python 版本 (如：3.12.10)
- `Exec` : 当前运行的Python 路径 (如：C:\User\Evan\venv\Scripts\python.exe)

## 使用方法

### Quarter OS

在 Quarter OS 终端中，使用 `Biscuit` 软件包管理器获取 `komfetch` 软件包：

```bash
biscuit get komfetch
```

安装完成后，在终端中输入 `komfetch` 即可运行该程序。

```bash
komfetch
```

### PY OS Improved

首先获取到 `komfetch` 软件包

(minqwq未来可能会搭建一个下载站，目前还是得找他或者找我获取……)

然后在终端中输入 `shizuku install /path/to/komfetch.sap` 安装 `komfetch` 软件包。

```bash
shizuku install /path/to/komfetch.sap
```

安装完成后，在终端中输入 `szk komfetch` 即可运行该程序。

```bash
szk komfetch
```

> [!TIP]
> PY OS Improved 由于没有图标，所以是纯文本版本。

> [!WARNING]
> 即使**Quarter OS**兼容**PY OS Improved**的 `shizuku` 软件包管理器，但请不要在Quarter OS上直接安装使用Shizuku版本，请使用Biscuit版本。

## 启动模式

KomFetch 程序可以以两种模式启动：

- `--default` : 默认模式，拥有大图标、16位颜色显示。
- `--stdout` : 标准输出模式，仅输出系统信息，不显示图标。

默认模式：

```bash
komfetch --default
```

标准输出模式：

```bash
komfetch --stdout
```

查询参数帮助：

```bash
komfetch -h
```

## 注意事项

- 目前仅支持 `Quarter OS` (Biscuit/.qap) 和 `PY OS Improved` (Shizuku/.sap) 这两个Python伪系统。

---

<div align="center">

Written by [ElofHew](https://github.com/ElofHew)

&copy; 2025 [Oak Studio](https://os.drevan.xyz/). All rights reserved.

</div>