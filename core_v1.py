import os
import platform
import datetime

class AssmM4_Agent:
    def __init__(self):
        self.sovereign = "Assm Mssto"
        self.start_time = datetime.datetime.now()

    def system_check(self):
        print(f"\n[+] فحص الأنظمة السيادية لـ {self.sovereign}...")
        print(f"[-] نظام التشغيل: {platform.system()}")
        print(f"[-] مسار العمل: {os.getcwd()}")
        print(f"[-] وقت التشغيل: {self.start_time.strftime('%Y-%m-%d %H:%M:%S')}")

    def tool_box(self):
        print("\n--- قائمة العمليات المتاحة ---")
        print("1. إنشاء ملف مشفر")
        print("2. فحص الاتصال بالشبكة")
        print("3. خروج")
        
        choice = input("\nاختر أمرك يا سلطان: ")
        if choice == "1":
            filename = input("اسم الملف: ")
            with open(filename, "w") as f:
                f.write(f"CONFIDENTIAL - Property of {self.sovereign}")
            print(f"تم إنشاء الحصن الرقمي: {filename}")
        elif choice == "2":
            os.system("ping -c 2 google.com")
        else:
            print("إغلاق النظام.. وداعاً أيها السيادي.")

if __name__ == "__main__":
    agent = AssmM4_Agent()
    print("--- [ AssmM4 - ACTIVE AGENT ] ---")
    agent.system_check()
    agent.tool_box()
