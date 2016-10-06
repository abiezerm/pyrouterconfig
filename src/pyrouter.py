import paramiko
import cmd

ssh = paramiko.SSHClient()

ssh.set_missing_host_key_policy(
    paramiko.AutoAddPolicy()
)

ssh.connect("172.16.200.8", username="test", password="cisco")

stdin, stdout stderr = ssh.exec_command("show run")

stdin.write("lol\n")
stdin.flush()
data = stdout.readlines()

for line in data:
    print(line)
