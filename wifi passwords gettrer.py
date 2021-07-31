#importing module
import subprocess # pip install subprocess

# getting wifi profiles from cmd
data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')

# storing profiles in a list
profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]

# getting password from cmd
for i in profiles:
    results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i,
                        'key=clear']).decode('utf-8').split('\n')
    # storing passwords in a list
    results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
    # printing wifi results
    try:
        print ("{:<30}|  {:<}".format(i, results[0]))
    except IndexError:
        print ("{:<30}|  {:<}".format(i, ""))