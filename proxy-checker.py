import time
import os
import requests
from colorama import Fore, init

init(autoreset=True)

def print_logo():
    logo = """
    ██████╗ ██████╗  ██████╗ ██╗  ██╗██╗   ██╗     ██████╗██╗  ██╗███████╗ ██████╗██╗  ██╗
    ██╔══██╗██╔══██╗██╔═══██╗╚██╗██╔╝╚██╗ ██╔╝    ██╔════╝██║  ██║██╔════╝██╔════╝██║ ██╔╝
    ██████╔╝██████╔╝██║   ██║ ╚███╔╝  ╚████╔╝     ██║     ███████║█████╗  ██║     █████╔╝ 
    ██╔═══╝ ██╔══██╗██║   ██║ ██╔██╗   ╚██╔╝      ██║     ██╔══██║██╔══╝  ██║     ██╔═██╗ 
    ██║     ██║  ██║╚██████╔╝██╔╝ ██╗   ██║       ╚██████╗██║  ██║███████╗╚██████╗██║  ██╗
    ╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝   ╚═╝        ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝ 
    """

    print(Fore.GREEN + logo)

def loading_screen():
    columns, lines = os.get_terminal_size()
    logo = """
    ██████╗ ██████╗  ██████╗ ██╗  ██╗██╗   ██╗     ██████╗██╗  ██╗███████╗ ██████╗██╗  ██╗
    ██╔══██╗██╔══██╗██╔═══██╗╚██╗██╔╝╚██╗ ██╔╝    ██╔════╝██║  ██║██╔════╝██╔════╝██║ ██╔╝
    ██████╔╝██████╔╝██║   ██║ ╚███╔╝  ╚████╔╝     ██║     ███████║█████╗  ██║     █████╔╝ 
    ██╔═══╝ ██╔══██╗██║   ██║ ██╔██╗   ╚██╔╝      ██║     ██╔══██║██╔══╝  ██║     ██╔═██╗ 
    ██║     ██║  ██║╚██████╔╝██╔╝ ██╗   ██║       ╚██████╗██║  ██║███████╗╚██████╗██║  ██╗
     ╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝   ╚═╝        ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝ 
    """

    message = "Загрузка скрипта..."

    logo_lines = logo.splitlines()
    top_space = (lines - len(logo_lines) - 2) // 2
    print("\n" * top_space)
    
    for line in logo_lines:
        print(line.center(columns))

    print("\n" * 2)  
    print(message.center(columns))
    
    time.sleep(3)

    os.system('cls' if os.name == 'nt' else 'clear')

def main_menu():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        loading_screen()
        print_logo()
        print("1. Начать проверку")
        print("2. Закрыть окно")
        choice = input("Выберите вариант (1/2): ").strip()

        if choice == '1':
            os.system('cls' if os.name == 'nt' else 'clear')
            proxy_check()
        elif choice == '2':
            print("Закрытие программы...")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")
            time.sleep(2)

def check_proxy(proxy):
    url = "http://httpbin.org/ip" 
    proxies = {"http": f"http://{proxy}", "https": f"http://{proxy}"}
    try:
        response = requests.get(url, proxies=proxies, timeout=5)
        if response.status_code == 200:
            return True
    except requests.RequestException:
        return False
    return False

def proxy_check():
    print("\nЗапуск проверки прокси...\n")
    with open("proxy.txt", "r") as file:
        proxies = file.readlines()

    working_proxies = []

    for proxy in proxies:
        proxy = proxy.strip()
        if check_proxy(proxy):
            print(f"{proxy} — " + Fore.GREEN + "Работает")
            working_proxies.append(proxy)
        else:
            print(f"{proxy} — " + Fore.RED + "Не работает")

    with open("working.txt", "w") as file:
        file.write("\n".join(working_proxies))

    print("\nПроверка завершена.")
    print(f"Рабочие прокси сохранены в 'working.txt'.")
    input("Нажмите Enter, чтобы вернуться в главное меню...")
    os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
    main_menu()
