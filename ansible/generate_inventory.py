import os

bastion_ip = os.getenv('BASTION_IP')

inventory_content = f"""
[bastion]
{bastion_ip} ansible_user=debian ansible_ssh_private_key_file=~/.ssh/id_rsa
"""

with open('ansible/inventory.ini', 'w') as file:
    file.write(inventory_content)
