# Quarter OS - System Information Fetcher

try:
    import os
    import sys
    import json
    import shutil
    import time as tm
    import platform
    from colorama import Fore, Back, Style, init
except ImportError as e:
    print(f"{Fore.RED}Error: {e}{Style.RESET_ALL}")
    print(f"{Fore.LIGHTGREEN_EX}This tool only works on Quarter OS version Alpha 0.2.2 or later.{Style.RESET_ALL}")
    exit()
except Exception as e:
    print(f"{Fore.RED}Error: {e}{Style.RESET_ALL}")
    exit()

init(autoreset=True)

qos_big_logo = """                                              
                  %%%%%%%%%%                  
             %%%%%%%%%%%%%%%%%%%%             
          %%%%%%%%%%%%%%%%%%%%%%%%%%          
        %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%        
      %%%%%%%%%%%%          %%%%%%%%%%%%      
     %%%%%%%%%%                %%%%%%%%%%     
    %%%%%%%%%                    %%%%%%%%%    
   %%%%%%%%%                      %%%%%%%%%   
   %%%%%%%%          %%%%          %%%%%%%%   
   %%%%%%%%        %%%%%%%%        %%%%%%%%   
   %%%%%%%%        %%%%%%%%        %%%%%%%%   
   %%%%%%%%          %%%%%         %%%%%%%%   
   %%%%%%%%%                  %%% %%%%%%%%%   
    %%%%%%%%%               %%%%%%%%%%%%%%    
     %%%%%%%%%%             %%%%%%%%%%%%%     
      %%%%%%%%%%%%          %%%%%%%%%%%%      
        %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%    
          %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%   
             %%%%%%%%%%%%%%%%%%%%  %%%%%%%%   
                  %%%%%%%%%%         %%%%     
                                              """

def get_package_value():
    """获取Quarter OS中，Biscuit和Shizuku的软件包数量"""
    # 定义全局变量：biscuit_value和shizuku_value
    global biscuit_value, shizuku_value
    # 获取Biscuit软件包数量
    try:
        with open(os.path.join("..", "..", "..", "system", "shell", "apps.json"), "r") as biscuit_sys_file:
            biscuit_sys_data = json.load(biscuit_sys_file)
        biscuit_value_sys = len(biscuit_sys_data)
        with open(os.path.join("..", "..", "shell", "apps.json"), "r") as biscuit_3rd_file:
            biscuit_3rd_data = json.load(biscuit_3rd_file)
        biscuit_value_3rd = len(biscuit_3rd_data)
        biscuit_value = biscuit_value_sys + biscuit_value_3rd
    except (FileNotFoundError, json.JSONDecodeError, TypeError, KeyError, IndexError, AttributeError, ValueError, OSError, IOError):
        # 若文件不存在或格式错误，则置0
        biscuit_value = 0
    except Exception as e:
        print(f"{Fore.RED}Error: {e}{Style.RESET_ALL}")
        sys.exit(1)
    # 获取Shizuku软件包数量
    try:
        with open(os.path.join("..", "..", "shizuku", "apps.json"), "r") as shizuku_file:
            shizuku_data = json.load(shizuku_file)
        shizuku_value = len(shizuku_data)
    except (FileNotFoundError, json.JSONDecodeError, TypeError, KeyError, IndexError, AttributeError, ValueError, OSError, IOError):
        # 若文件不存在或格式错误，则置0
        shizuku_value = 0
    except Exception as e:
        print(f"{Fore.RED}Error: {e}{Style.RESET_ALL}")
        sys.exit(1)

def main():
    # 获取Quarter OS的配置文件数据
    try:
        with open(os.path.join("..", "..", "config", "config.json")) as qos_config_file:
            config_data = json.load(qos_config_file)
            qos_version = config_data.get("version", "?")
            qos_vercode = config_data.get("vercode", "?")
            qos_name = config_data.get("system_name", "qos")
            qos_path = config_data.get("qos_path", "unknown path")
            qos_activate = config_data.get("activate_statue", False)
            qos_edition = config_data.get("qos_edition", "unknown edition")
            last_login = config_data.get("last_login", "user")
    except FileNotFoundError:
        print(f"{Fore.RED}Error: Config file not found.{Style.RESET_ALL}")
        sys.exit(1)
    except json.JSONDecodeError:
        print(f"{Fore.RED}Error: Config file is not a valid JSON file.{Style.RESET_ALL}")
        sys.exit(1)
    except Exception as e:
        print(f"{Fore.RED}Error: {e}{Style.RESET_ALL}")
        print(f"{Fore.LIGHTGREEN_EX}This tool only works on Quarter OS version Alpha 0.2.2 or later.{Style.RESET_ALL}")
        sys.exit(1)

    get_package_value() # 获取Biscuit和Shizuku的软件包数量

    # 从动态数据中获取信息
    item_qos_login = str(f"{last_login}@{qos_name}")
    item_qos_version = str(f"{qos_version} ({qos_vercode})")
    item_qos_path = str(qos_path)
    item_qos_shell = str(f"KomShell - {qos_version}")
    item_qos_pks = str(f"Biscuit ({biscuit_value}) | Shizuku ({shizuku_value})")
    item_qos_edition = str(qos_edition)
    item_sys_platform = str(f"{platform.system()} {platform.release()}")
    item_sys_version = str(platform.version())
    item_dev_name = str(platform.node())
    item_sys_arch = str(platform.machine())
    item_dev_cpu = str(platform.processor())
    item_py_ver = str(platform.python_version())
    item_py_exec = str(sys.executable)

    # 准备输出信息的一些数据变量
    qos_logo_lines = qos_big_logo.split('\n') # 将logo分割成行(应该是22行)
    qos_logo_line_width = len(qos_logo_lines[0]) # logo每一行的长度(单位：字符)
    terminal_width = shutil.get_terminal_size().columns  # 获取终端宽度(单位：字符)
    div_line_width = terminal_width - len(qos_logo_lines[0]) - 2 # 分割线的长度(单位：字符)
    
    # 输出信息的键(以列表形式存储)
    infos = [
        [" ", "", 1],
        [f"{Fore.LIGHTMAGENTA_EX}Quarter OS System Information Fetcher{Fore.RESET}", "", 37],
        ["-" * div_line_width, "", div_line_width],
        [f"{Fore.YELLOW}Quarter OS Login: {Style.RESET_ALL}", item_qos_login, 18],
        [f"{Fore.YELLOW}Quarter OS Version: {Style.RESET_ALL}", item_qos_version, 20],
        [f"{Fore.YELLOW}Quarter OS Path: {Style.RESET_ALL}", item_qos_path, 17],
        [f"{Fore.YELLOW}Quarter OS Shell: {Style.RESET_ALL}", item_qos_shell, 18],
        [f"{Fore.YELLOW}Quarter OS Packages: {Style.RESET_ALL}", item_qos_pks, 21],
        [f"{Fore.YELLOW}Quarter OS Edition: {Style.RESET_ALL}", item_qos_edition if qos_activate else "", 20],
        [f"{Fore.CYAN}System Platform: {Style.RESET_ALL}", item_sys_platform, 17],
        [f"{Fore.CYAN}System Version: {Style.RESET_ALL}", item_sys_version, 16],
        [f"{Fore.CYAN}Device Name: {Style.RESET_ALL}", item_dev_name, 13],
        [f"{Fore.CYAN}System Architecture: {Style.RESET_ALL}", item_sys_arch, 21],
        [f"{Fore.CYAN}Device Processor: {Style.RESET_ALL}", item_dev_cpu, 18],
        [f"{Fore.CYAN}Python Version: {Style.RESET_ALL}", item_py_ver, 16],
        [f"{Fore.CYAN}Python Executable: {Style.RESET_ALL}", item_py_exec, 19],
        [" ", "", 1],
        [f"{Fore.LIGHTGREEN_EX}Fetched at {tm.strftime('%Y-%m-%d %H:%M:%S', tm.localtime())}{Style.RESET_ALL}", "", 30],
        [" ", "", 1],
        [f"{Back.BLACK}   {Back.RED}   {Back.GREEN}   {Back.YELLOW}   {Back.BLUE}   {Back.MAGENTA}   {Back.CYAN}   {Back.WHITE}   {Style.RESET_ALL}", "", 24],
        [f"{Back.LIGHTBLACK_EX}   {Back.LIGHTRED_EX}   {Back.LIGHTGREEN_EX}   {Back.LIGHTYELLOW_EX}   {Back.LIGHTBLUE_EX}   {Back.LIGHTMAGENTA_EX}   {Back.LIGHTCYAN_EX}   {Back.LIGHTWHITE_EX}   {Style.RESET_ALL}", "", 24],
        [" ", "", 1]
    ]
    # 其中，0为info的键，1为info的值，2为键的长度

    # Logo和info的行数
    logo_lines_num = len(qos_logo_lines)
    infos_num = len(infos)
    if logo_lines_num > infos_num: # logo行数大于info行数，则需要补充空行
        need_lines_num = logo_lines_num
    else: # logo行数小于等于info行数，则直接输出
        need_lines_num = infos_num

    # 循环打印一行logo和一条info
    for i in range(need_lines_num):
        if i < logo_lines_num:
            logo_text = f"{Fore.BLUE}{qos_logo_lines[i]}{Style.RESET_ALL}"
        else:
            logo_text = " " * qos_logo_line_width
        if i < infos_num:
            used_space = qos_logo_line_width + 1 + infos[i][2] + 1  # 最后留一个空字符
            free_space = terminal_width - used_space  # 供info[i][1]使用的剩余空间
            dynamical_space = len(infos[i][1])  # 计算当前值需要占用的空间
            combined_space = dynamical_space - free_space  # 计算需要截断的字符长度(后面的部分)
            if combined_space > 0:  # 计算结果大于0，说明需要截断
                dyna_words = infos[i][1][0:dynamical_space - combined_space]  # 截断后的字符串
            else:  # 计算结果小于等于0，说明不需要截断
                dyna_words = infos[i][1]  # 直接输出原字符串
            info_text = infos[i][0] + dyna_words
        else:
            info_text = " " * (terminal_width - qos_logo_line_width - 1)
        line_text = logo_text + " " + info_text
        print(line_text.ljust(terminal_width))  # 左对齐，右边用空格填充，打印出来

if __name__ == "__main__":
    main()