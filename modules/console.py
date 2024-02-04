from colorama import Fore
from threading import Lock
from datetime import datetime
from ctypes import windll
from pystyle import Center,Colors,Colorate


lock = Lock()

class Console:
    
    @staticmethod
    def printsc(content: str):
        lock.acquire()
        print(f"{Fore.LIGHTBLACK_EX}[{Fore.LIGHTBLUE_EX}Hesap Oluşturuldu{Fore.LIGHTBLACK_EX}]{Fore.LIGHTWHITE_EX} >{Fore.LIGHTGREEN_EX} {content}")
        lock.release()

    @staticmethod
    def printe(content: str):
        lock.acquire()

        lock.release()
        
    @staticmethod
    def printi(content: str):
        lock.acquire()
        print(f"{Fore.LIGHTBLACK_EX}[{Fore.LIGHTYELLOW_EX}Takip{Fore.LIGHTBLACK_EX}]{Fore.LIGHTWHITE_EX} >{Fore.LIGHTYELLOW_EX} {content}")
        lock.release()
        
    @staticmethod
    def printm(content: str):
        lock.acquire()
        print(f"{Fore.LIGHTBLACK_EX}[{Fore.LIGHTBLUE_EX}Mail Doğrulandı{Fore.LIGHTBLACK_EX}]{Fore.LIGHTWHITE_EX} >{Fore.LIGHTMAGENTA_EX} {content}")
        lock.release()
        
    @staticmethod
    def printhc(content: str):
        lock.acquire()
        print(f"{Fore.LIGHTBLACK_EX}[{Fore.LIGHTMAGENTA_EX}İnsanlaştırma Tamamlandı{Fore.LIGHTBLACK_EX}]{Fore.LIGHTWHITE_EX} >{Fore.LIGHTCYAN_EX} {content}")
        lock.release()


class Tools:

    @staticmethod
    def setTitle(threads: int, proxies: int, created: int, follow: int, pfp:int):

        windll.kernel32.SetConsoleTitleW(
            f"|  Yüklenen Proxy: {proxies}  |  Hız: {threads}  |  Oluşturulan: {created} | Takip Edilen: {follow} | PFP Değişen {pfp} ")