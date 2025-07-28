"""
@ Name: KomFetch
@ Author: ElofHew
@ Version: 1.2
@ Description: A tool to display system information on Quarter OS.
@ Date: 2025-07-17
@ Last Modified: 2025-07-28
@ License: GNU General Public License v3.0
@ Repository: https://github.com/ElofHew/komfetch
@ Class: Shizuku Application Package
"""

try:
    # 导入所需模块
    import os
    import sys
    import json
    import shutil
    import time as tm
    import platform
    from colorama import Fore, Back, Style, init
except ImportError as e:
    print(f"Error: {e}")
    exit()
except Exception as e:
    print(f"Error: {e}")
    exit()

# 初始化颜色模块
init(autoreset=True)

def get_package_value():
    """获取PY OS Improved中，Shizuku的软件包数量"""
    # 定义全局变量：biscuit_value和shizuku_value
    global shizuku_value
    # 获取Shizuku软件包数量
    try:
        with open(os.path.join("..", "apps.json"), "r") as shizuku_file:
            shizuku_data = json.load(shizuku_file)
        shizuku_value = len(shizuku_data)
    except (FileNotFoundError, json.JSONDecodeError, TypeError, KeyError, IndexError, AttributeError, ValueError, OSError, IOError):
        # 若文件不存在或格式错误，则置0
        shizuku_value = 0
    except Exception as e:
        # 其他错误，打印错误信息并退出程序
        print(f"{Fore.RED}Error: {e}{Style.RESET_ALL}")
        sys.exit(1)

def get_cut_length(i, infos_num, terminal_width, infos, double):
    """获取info的一行文字截断处理后的文字"""
    if i <= infos_num:
        used_space = infos[i][2] + 1  # 最后留一个空字符
        free_space = terminal_width - used_space  # 供info[i][1]使用的剩余空间
        dynamical_space = len(infos[i][1])  # 计算当前值需要占用的空间
        combined_space = dynamical_space - free_space  # 计算需要截断的字符长度(后面的部分)
        if combined_space > 0:  # 计算结果大于0，说明需要截断
            dyna_words = infos[i][1][0:dynamical_space - combined_space]  # 截断后的字符串
        else:  # 计算结果小于等于0，说明不需要截断
            dyna_words = infos[i][1]  # 直接输出原字符串
        info_text = infos[i][0] + dyna_words # 键 + 值
    else:
        info_text = " " * (terminal_width - 1)  # 若info_num大于实际数量，则填充空白
    return info_text

def main():
    """主函数"""
    # 获取参数
    args = sys.argv[1:] if len(sys.argv) > 1 else []
    mode = args[0] if args else "--default"

    # 避免Quarter OS用户安装SAP包使用
    try:
        with open(os.path.join("..", "..", "config", "config.json"), "r") as qos_config_file:
            qos_config_data = json.load(qos_config_file)
        qos_name = qos_config_data.get("name", "other")
        qos_ename = qos_config_data.get("ename", "other")
        if qos_name.lower().replace(" ", "") == "quarteros" and qos_ename.lower().replace(" ", "") == "qos":
            print(f"{Fore.RED}Error: This tool only works on PY OS Improved. Quarter OS User please use QAP edition.{Style.RESET_ALL}")
            print(f"{Fore.LIGHTGREEN_EX}`biscuit get komfetch`{Style.RESET_ALL}\n")
            sys.exit(1)
    except (FileNotFoundError, json.JSONDecodeError, TypeError, KeyError, IndexError, AttributeError, ValueError, OSError, IOError):
        pass
    except Exception as e:
        print(f"{Fore.RED}Error: {e}{Style.RESET_ALL}")
        sys.exit(1)

    # 获取Quarter OS的配置文件数据
    try:
        config_path = os.path.join("..", "..", "..", "config")
        with open(os.path.join(config_path, "config.json"), "r") as pyosi_config_file:
            config_data = json.load(pyosi_config_file)
        with open(os.path.join(config_path, ".devconfig", "confdev.json"), "r") as pyosi_dev_file:
            dev_data = json.load(pyosi_dev_file)
        pyosi_name = "PY OS Improved"
        pyosi_version = dev_data.get("system_version", "?")
        pyosi_vercode = dev_data.get("system_build", "Build ?").split()[1]
        pyosi_node = config_data.get("default_hostname", "pyosi")
        pyosi_path = os.path.abspath(os.path.join(os.getcwd(), "..", "..", ".."))
        last_login = config_data.get("last_login", "user")
    except ValueError:
        # 提示信息
        print(f"{Fore.LIGHTGREEN_EX}This tool only works on Quarter OS version Alpha 0.2.2 or later.{Style.RESET_ALL}")
        sys.exit(1)
    except FileNotFoundError:
        print(f"{Fore.RED}Error: Config file not found.{Style.RESET_ALL}")
        sys.exit(1)
    except json.JSONDecodeError:
        print(f"{Fore.RED}Error: Config file is not a valid JSON file.{Style.RESET_ALL}")
        sys.exit(1)
    except Exception as e:
        print(f"{Fore.RED}Error: {e}{Style.RESET_ALL}")
        sys.exit(1)

    get_package_value() # 获取Shizuku的软件包数量

    # 从动态数据中获取信息转换为实打实的字符串
    item_OS_name = str(f"{pyosi_name} {pyosi_version} ({pyosi_vercode})")
    item_pyosi_path = str(pyosi_path)
    item_pyosi_login = str(f"{last_login}@{pyosi_node}")
    item_pyosi_shell = str("Flandre Shell")
    item_pyosi_pks = str(f"Shizuku({shizuku_value})")
    item_sys_platform = str(f"{platform.system()} {platform.release()}")
    item_sys_version = str(platform.version())
    item_sys_name = str(platform.node())
    item_sys_arch = str(platform.machine())
    item_sys_cpu = str(platform.processor())
    item_py_ver = str(platform.python_version())
    item_py_exec = str(sys.executable)

    # 准备输出信息的一些数据变量
    terminal_width = shutil.get_terminal_size().columns  # 获取终端宽度(单位：字符)
    
    # 输出信息的键(以列表形式存储)
    infos = [
        [" ", "", 1],
        [f"{Fore.LIGHTMAGENTA_EX}KomFetch System Fetcher{Fore.RESET}", "", 23],
        ["-" * 23, "", 23],
        [f"{Fore.YELLOW}OS: {Style.RESET_ALL}", item_OS_name, 4],
        [f"{Fore.YELLOW}Path: {Style.RESET_ALL}", item_pyosi_path, 6],
        [f"{Fore.YELLOW}Login: {Style.RESET_ALL}", item_pyosi_login, 7],
        [f"{Fore.YELLOW}Shell: {Style.RESET_ALL}", item_pyosi_shell, 7],
        [f"{Fore.YELLOW}Packages: {Style.RESET_ALL}", item_pyosi_pks, 10],
        [f"{Fore.CYAN}Platform: {Style.RESET_ALL}", item_sys_platform, 10],
        [f"{Fore.CYAN}Version: {Style.RESET_ALL}", item_sys_version, 9],
        [f"{Fore.CYAN}Node: {Style.RESET_ALL}", item_sys_name, 6],
        [f"{Fore.CYAN}Arch: {Style.RESET_ALL}", item_sys_arch, 6],
        [f"{Fore.CYAN}CPU: {Style.RESET_ALL}", item_sys_cpu, 5],
        [f"{Fore.LIGHTRED_EX}Python: {Style.RESET_ALL}", item_py_ver, 8],
        [f"{Fore.LIGHTRED_EX}Exec: {Style.RESET_ALL}", item_py_exec, 6],
        [" ", "", 1],
        [f"{Fore.LIGHTGREEN_EX}Fetched at {tm.strftime('%Y-%m-%d %H:%M:%S', tm.localtime())}{Style.RESET_ALL}", "", 30],
        [" ", "", 1],
        [f"{Back.BLACK}   {Back.RED}   {Back.GREEN}   {Back.YELLOW}   {Back.BLUE}   {Back.MAGENTA}   {Back.CYAN}   {Back.WHITE}   {Style.RESET_ALL}", "", 24],
        [f"{Back.LIGHTBLACK_EX}   {Back.LIGHTRED_EX}   {Back.LIGHTGREEN_EX}   {Back.LIGHTYELLOW_EX}   {Back.LIGHTBLUE_EX}   {Back.LIGHTMAGENTA_EX}   {Back.LIGHTCYAN_EX}   {Back.LIGHTWHITE_EX}   {Style.RESET_ALL}", "", 24],
        [" ", "", 1]
    ]
    # 其中，0为info的键，1为info的值，2为键的长度

    # Logo和info的行数
    infos_num = len(infos)

    def stdout_mode(color_mode):
        """标准输出模式：没有颜色块，若color_mode为True则打印颜色块。"""
        # 循环打印一行info
        for i in range(infos_num - 3 if not color_mode else infos_num): # -3是为了去掉最后的颜色块
            info_text = get_cut_length(i, infos_num, terminal_width, infos, False)
            print(info_text.ljust(terminal_width))  # 左对齐，右边用空格填充，打印出来

    if mode == "-h":  # 打印帮助信息
        print(f"{Fore.LIGHTGREEN_EX}Usage: komfetch [mode]{Style.RESET_ALL}")
        print(f"{Fore.CYAN}Mode:{Style.RESET_ALL}")
        print(f"{Fore.CYAN}  (No Argument): Default mode.{Style.RESET_ALL}")
        print(f"{Fore.CYAN}  --default: Default mode, print two columns.{Style.RESET_ALL}")
        print(f"{Fore.CYAN}  --stdout: Standard output mode, print one column.{Style.RESET_ALL}")
        print(f"{Fore.CYAN}  -h: Print help information.{Style.RESET_ALL}")
        print()
        sys.exit(0)
    elif mode == "--default":  # 默认模式
        stdout_mode(True)
    elif mode == "--stdout":  # 标准输出模式
        stdout_mode(False)
    else:  # 其他参数，打印错误信息
        print(f"{Fore.RED}Error: Invalid argument.{Style.RESET_ALL}")
        sys.exit(1)

if __name__ == "__main__":
    main()