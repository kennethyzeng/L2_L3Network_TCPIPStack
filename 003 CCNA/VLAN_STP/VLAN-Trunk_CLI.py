#Created By kenenth zeng 
#8/22/2022
#Trunk configuration and router configuration (ROAS)


######################1 Trunk configuration #################
interface g0/0
switchport mode trunk      #will be command reject. trunk encapsulation is 'auto' can not be configured to truck mode 
switchport trunk encapsulation ? 
switchport trunk encapsulation dot1q 
switchport mode trunk 

show interface trunk 
#shoow vlan brief 

######################2 command to configure the VLAN allowed on the trucnk ###############
int g0/0 
switchport trunk allowed vlan ?    #(WORD, add, all, except, non, remove)
switchport trunk allowed vlan 10, 30
#switchport trunk alllwed vlan add 20
#switchport trunk allowed vlan remove 20
#switchport trunk allowed vlan all
#switchport trunk allowed vlan except 1-5, 10
#switchport trunk allowed vlan none 

do show interfaces trunk 

######################3 change native vlan (between switches p2p) ###############
switchport trunk native vlan 1001
show vlan brief 



######################4 router configuration    ROAS(Router on a stick) ###############
interface g0/0 
no shutdown           ##make sure the interface is enable with 'no shutdown'

interface g0/0.10 
encapsulation dot1q 10 
ip address 192.168.1.62 255.255.255.192 

interface g0/0.20 
encapsulation dot1q 20
ip address 192.168.1.126 255.255.255.192 

interface g0/0.30
encapsulation dot1q 30 
ip address 192.168.1.190 255.255.255.192

show ip interface brief 
shwo ip route 




#######################5 two method to configure the native VLAN on aourter in a ROAS configuration###############
#1 @Router's config-subif
encapsulation dot1q 112 native 
ip address 192.168.1.1 255.255.255.0 


#2 @router's config-f
ip address 192.168.1.1. 255.255.255.0