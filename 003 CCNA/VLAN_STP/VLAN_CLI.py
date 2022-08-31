#Created by Kenneth zeng
#08/22/2022
#CLI realted VLAN

####################1 VLAN configuration####################
show vlan brief 

interface range g1/0 -3 
switchport mode access 
switchport access vlan 10 

interface range g2/0 - 3 
switchport mode access 
swithcport access vlan 20 

interface range g3/0 -3 
switchport mode access 
switchport access vlan 30

do sh vlan brief 




####################2 change VLAN name ####################
@swich config 
vlan 10 
name ENGINEERING 

vlan 20 
name  HR 

vlan 30 
name SALES 

do show vlan brief 


####################3 Example  ####################
#1 configure theh correct IP address /subnet mask on each PC. Set the gateway address as the last usable address of the subnet 
ipconfig /ip 10.0.0.1 255.255.255.192    #@PC1
ipconfig /ip 10.0.0.2 255.255.255.192     #@PC2
#gateway 10.0.0.62

ipconfig /ip 10.0.0.65 255.255.255.192   #@PC3
ipconfig /ip 10.0.0.66 255.255.255.192     #@PC4
#gateway 10.0.0.126

ipconfig /ip 10.0.0.129 255.255.255.192   #@PC3
ipconfig /ip 10.0.0.130 255.255.255.192     #@PC4
#gateway 10.0.0.190


#2 make three connection between R1 and Sw1. configure one interface on R1 for each VLAN. Make sure the IP address are the gateway address you configured on the pc 
@R1 router
en 
enable 
config t 
sh interface brief 
interface g0/0 
ip address 10.0.0.62 255.255.255.192   #for LAN10
no shutdoown

interface g0/1 
ip address 10.0.0.126 255.255.255.192   #for LAN20
no shutdoown

interface g0/2 
ip address 10.0.0.190 255.255.255.192   #for LAN30
no shutdoown

do sh ip interface brief

#3 configure SW1's interface in the proper VLANs. name The VLAN(Engineering, HR, Sales )
@switch SW1
en 
enable 
config t

interface range g0/0, f3/1, f4/1
sw 
switchport 
switchport mode ac
switchport mode access 
sw 
switchport ac 
swithcport access v
switchport access vlan 10 

interface range g1/1, f5/1, f6/1
sw mode ac
sw ac vlan 20


interface range g2/1, f7/1, f8/1
sw mode ac
sw ac vlan 30

do show vl br 

vlan 10 
name ENGINNERING 

vlan 20 
name HR

vlan 30 
name SALES

do sh vlan br 


#4 ping between the PCs to check connectivity. send a braodcast ping from a pC(ping the subnet broadcast address) and see which PCs device receive the broadcast
#use the packet Tracer'ssimulation Mode 
ping 10.0.0.65    #why ping-able ?  inter-VLAN routing 

ping 10.0.0.129  #?

ping 10.0.0.63  #broadcast; only the Devices at the same VLAN