# pan-automator-cli
A script to generate a Panorama ( PaloAltoNetworks ) network template via a YAML file.
The script will generate PAN/OS command line that you can then copy paste in the Panorama terminal

## Explanation & Motivation
I originaly plan to use Ansible to generate hundred of Panorama template for a customer but failed at it.
I then found out that Python + YAML + Jinja2 could do what I needed quick & clean.
It is also a great example if you want to give a try to YAML template for your network & Security deployment.

## How does it work
The script will read your YAML file, get the variables, fill the Jinja2 and generate cli ready to be pushed in Panorama.
You can add extra interfaces & routes in the YAML file if needed

## How to Run it
```
 python pan-automator-cli.py
 
set template akira_template config deviceconfig system login-banner akira
set template akira_template config network interface ethernet ethernet1/1 layer3 ip 192.168.1.254/24
set template akira_template config network interface ethernet ethernet1/1 comment Untrust_Zone
set template akira_template config vsys vsys1 import network interface ethernet1/1
set template akira_template config vsys vsys1 zone default network layer3 ethernet1/1
set template akira_template config network virtual-router default interface ethernet1/1
set template akira_template config network interface ethernet ethernet1/2 layer3 units ethernet1/2.123 tag 123
....
```

