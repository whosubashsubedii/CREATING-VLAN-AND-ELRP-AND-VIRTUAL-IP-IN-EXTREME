
vlan = input ("Enter the vlan Number: ")
tag_port = input ("Enter the interface to tag vlan: ")


vlan_ip_cmd = ""
vlan_ip = input ("Do you have ip on vlan?(yes/no)").strip().lower()


if  vlan_ip == "yes":
    while True:
     vlan_ip = input("Enter your ip for vlan: ") 
     vlan_subnet = input ("Enter your Subnet mask for vlan: ")  
     vlan_ip_cmd += f"configure vlan_{vlan} ipaddress {vlan_ip} {vlan_subnet}"
     break


print (f"""

        #Command to add vlan in extreme switch#


create vlan vlan_{vlan}

configure vlan vlan_{vlan} tag {vlan}

configure vlan vlan_{vlan} add port {tag_port} tagged



{vlan_ip_cmd}



""")

input ("Enter to Exit....")