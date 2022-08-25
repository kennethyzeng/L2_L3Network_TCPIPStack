##Created by Kenneth Zeng
## 08/25/2022
##purpose: quickly review Static routing and catch up 
##Blow Command are operated with Cisco Switch or Router

###################1 Trouble shooting Static Routing##################
#1 ping the dst IP address 
#2 check your PC configuratoin (ip address, subnet, and gateway info)
ipconfig   
ipconfig /all 

#2check interface info of default router
en 
show ip interface br 

#3 check the routing table info of default router 
sh ip route 

#4 checking it in running-config
show running-config 
show running-config |inclue ip route 

#5 ping the default router
#6 repeate steps 2-4 for each router in routing path and make sure information are correct  
#7 check the dst PC's info
ipconfig 
ipconfig /all 
#8 ping the dst PC again 

#note: make sure it is  two-way reachability  (example: send and reply path for ping. broadcast and unitcast)






###################2 Configure default Route##################
###ip route dst_add mask next-hop 
###ip route dst_add mask interface-port

#1 configure the default gateway on your PC 
ip route 0.0.0.0 0.0.0.0 192.168.1.254     #route's port interface address


#2 manually configure the routing path for each router
ip route dst_add mask next-hop   #by next hop interface's ip address
ip route dst_add mask interface-port   #by self router's exit infterce port 

sh ip route  #do show ip route 


##############3 Manually configure the whole static routing###################
#1 configure your PC(gateway, ip address, and subnet)
#2 configure your defualt router's interface
#hostname, Interface port and its address and subnet, and description, 
en 
enable 
conf t
host 
hostname R1 
int
interface g0/0
ip add 
ip address 192.168.1.254 255.255.255.0 
desc 
description ##to SW1 ##
no shut 
do sh ip int brief 
exit 

#3 configure router's routing
ip route 192.168.1.0 255.255.255.0 g0/0
ip route 192.168.3.0 255.255.255.0 192.168.13.3
do sh ip ro
ping the route's address   #for ARP

#4 repeat step 2-3 or similar step for each router, and step 1 for dst PC

