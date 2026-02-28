import os

def build_advanced_tool():
    os.system('clear')
    print("--- [ AssmM4 - THE MASTER GENERATOR V3 ] ---")
    print("1. إنشاء (IP & Info Grabber) - أداة سحب معلومات الجهاز")
    print("2. إنشاء (File Encryptor) - أداة تشفير الملفات بكلمة سر")
    print("3. إنشاء (Auto-Update Bot) - بوت تحديث النظام تلقائياً")
    
    choice = input("\n[AssmM4] اختر نوع السلاح البرمجي: ")
    
    if choice == "1":
        with open("grabber.py", "w") as f:
            f.write("import socket\nimport platform\nimport requests\n")
            f.write("ip = requests.get('https://api.ipify.org').text\n")
            f.write("print(f'IP Address: {ip}')\n")
            f.write("print(f'System: {platform.system()}')\n")
        print("\n[+] تم إنشاء وحش سحب المعلومات: grabber.py")

    elif choice == "2":
        with open("vault.py", "w") as f:
            f.write("import hashlib\n")
            f.write("password = input('Enter Secret Password: ')\n")
            f.write("if hashlib.sha256(password.encode()).hexdigest() == '5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8':\n")
            f.write("    print('Vault Access Granted!')\n")
            f.write("else: print('Access Denied!')\n")
        print("\n[+] تم إنشاء حصن التشفير: vault.py")

if __name__ == "__main__":
    build_advanced_tool()
