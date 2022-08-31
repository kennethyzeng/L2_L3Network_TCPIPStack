#Name: Kenneth Zeng 
#crated by 8/20/2022 
#This file for Layer3 or multilayer switch and how to configure them. 
#Inter-VLAN routing via SVI   

###########################1 pointer to point confgiraution between Router and L3 switch, Then SVI configuration on L3 switch###########
#remove Router's stick configuation and configure that new IP address as default interface 
#@Router config
#check status of current running config and interface status
#en
#sh runnning-config brief 
#show ip interface brief 
config t
no interface g0/0.10
no interface g0/0.20
no interface g0/0.30
default interface g0/0 

do sh run 
do show ip interface brief   #do sh ip int br


interface g0/0 
ip address 192.168.1.194 255.255.255.252    #/30 subnet mask
do show ip interface brief


#@switch side config 
#eheck status 
#en 
#show run 
conf t
default interface g0/1 
ip routing               #this command enable layer 3 routing on the switch. @config level. If forget, inter-VLAN routing won't work 
interface g0/1 
no switchport      #This configure the interface as a 'routed port' (layer 3 port, not a layer 2/switchport )
#It changes the interface from a layer 2 switchporot to a layer 3 routed port 
ip address 192.168.1.193 255.255.255.252
do show ip interface brief 


exit 

##default route pointing to Router; still at swtich 
#check the current routing table if need
#do sh ip route 
ip route 0.0.0.0 0.0.0.0 192.168.1.194  #next hop's interface
do show ip route 

show interface status   ##check if the interface is routed or not  (VLAN part)

#SVI configuration; Still at switch 
#do sh vlan brief
interface vlan 10 
ip address 192.168.1.62 255.255.255.192
no shutdown 

interface vlan 20
ip address 192.168.1.126 255.255.255.192
no shutdown 

interface vlan 30 
ip address 192.168.1.190 255.255.255.192
no shutdown 




###########################2 SVI troubleshooting###########
#the conditions requried for an SVI to be UP/UP
-The VLAN must exist on the switch 

-The switch must have at least one access port in the VLAN in an up/up state, and/or one trunk port 
that allows the VLAN that is in an up/up state 

-The VLAN must not be shutdown(you can use the shutdown command to disable a VLAN)

-The SVI must not be shutdown(SVIs are disabled by defualt )
