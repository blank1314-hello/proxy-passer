#proxy
import winreg as reg
import time

def on_press():
    try:
        registry_path = r"Software\Microsoft\Windows\CurrentVersion\Internet Settings"
        
        key = reg.OpenKey(reg.HKEY_CURRENT_USER, registry_path, 0, reg.KEY_SET_VALUE)
        
        reg.SetValueEx(key, "ProxyEnable", 0, reg.REG_DWORD, 0)
        reg.SetValueEx(key, "ProxyServer", 0, reg.REG_SZ, "")
        
        reg.CloseKey(key)
    except Exception as e:
        print(f"오류 발생: {e}")

if __name__ == "__main__":
    print("프록시 서버가 비활성화되었습니다.")
    while True:
        on_press()
