import subprocess

v_hash = str(input("Vendor Hash: ")).strip().upper()
hash_type = str(input("Hash Type: ")).strip()
file_path = str(input("File path: ")).strip()

ps_invoker = f"Get-FileHash -Path {file_path} -Algorithm {hash_type} | Select-Object -ExpandProperty Hash"

ps_hash = subprocess.run(["powershell", "-Command", ps_invoker], capture_output=True, text=True)

output = ps_hash.stdout.strip().upper()

condition = v_hash==output

if condition is True:
    print("The Hashes Match!")
else:
    print("The Hashes Don't Match!")

input("press enter to exit")