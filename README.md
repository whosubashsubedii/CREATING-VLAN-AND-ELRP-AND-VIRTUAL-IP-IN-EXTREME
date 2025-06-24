


# Extreme VLAN Configuration Script

This Python script helps network engineers quickly generate CLI configuration commands for VLAN creation on Extreme Networks switches.

---

## 💡 Features

- Create a VLAN with a custom VLAN number.
- Assign tagged ports to the VLAN.
- Optionally configure an IP address and subnet mask for the VLAN.

---

## 🛠️ Requirements

- Python 3.x
- Works in any environment with Python installed (no third-party libraries needed).

---

## 🚀 How to Use

1. **Run the script** using Python:

   ```bash
   python vlan_config.py
````

2. **Follow the prompts**:

   * Enter the VLAN number.
   * Enter the port/interface to be tagged.
   * Choose whether to assign an IP address.
   * If yes, enter the IP address and subnet mask.

3. **Result**:

   * The script will display CLI commands you can paste into an Extreme switch CLI.

---

## 🧾 Example Output

```
Enter the VLAN number: 100
Enter the interface to tag VLAN: 1:1
Do you have IP on VLAN? (yes/no): yes
Enter your IP & Subnet mask for VLAN: 192.168.100.1
Enter your Subnet mask for VLAN: 255.255.255.0

# Command to add VLAN in Extreme switch #

create vlan vlan_100

configure vlan vlan_100 tag 100

configure vlan vlan_100 add port 20 tagged

configure vlan_100 ip address 192.168.100.1 255.255.255.0
```

---

## 📌 Notes

* This script only prints the configuration—it does **not** apply it to any device.
* You can copy the output and paste it into your Extreme Networks CLI manually or build automation using tools like Netmiko later.

---

## 📄 License

This project is free to use and modify for internal or educational purposes.

