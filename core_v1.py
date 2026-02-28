import os

def create_code():
    os.system('clear')
    print("--- [ AssmM4 - مـصـنـع الأكـواد ] ---")
    print("1. إنشاء سكربت بايثون (Python)")
    print("2. إنشاء سكربت أوامر (Bash)")
    
    choice = input("\nاختر نوع الكود الذي تريد صنعه: ")
    name = input("اختر اسماً للملف الجديد (مثلاً test): ")
    msg = input("اكتب الرسالة التي سيطبعها الكود: ")

    if choice == "1":
        with open(f"{name}.py", "w") as f:
            f.write(f"print('{msg}')\nprint('تمت البرمجة بواسطة AssmM4')")
        print(f"\n[+] تم إنشاء {name}.py بنجاح!")
    
    elif choice == "2":
        with open(f"{name}.sh", "w") as f:
            f.write(f"#!/bin/bash\necho '{msg}'\necho 'AssmM4 Shield Active'")
        os.system(f"chmod +x {name}.sh")
        print(f"\n[+] تم إنشاء {name}.sh بنجاح!")

if __name__ == "__main__":
    create_code()
