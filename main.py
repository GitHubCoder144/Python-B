print("Hello, Fedora Bug Tester!")

package_name = "firefox"
print("Package to test:", package_name)

def greet():
    print("Hello, Fedora Bug Tester!")

greet()

package_name = input("Enter package name to test: ")
print("You want to test:", package_name)

package_name = input("Enter package name to test: ")
if package_name == "firefox":
    print("Testing Firefox!")
else:
    print("Testing Another Package!")

packages = ["firefox", "gimp", "vlc"]
for package in packages:
    print("Testing", package)

import subprocess

def run_command(command):
    result = subprocess.run(command, capture_output=True, text=True)
    print(result.stdout)

run_command(["dnf", "list", "updates"])

