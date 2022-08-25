###Created by Kenneth 
###7/28/2022
####example of setup configuration for static routing 
##Blow Command are operated with Cisco Switch or Router


#1 configure Router 1 with a host name of Route 1. configre the apporiate Ip address on the interface; DCE cable is serial link(need rate speed)
en 
enable 
conf t 
hostname R1
int f0/0
ip address  192.168.101.1 255.255.255.0 
no shut
do sh ip int

int s0/0
ip address 192.168.1.1 255.255.255.0 
clock rate 64000
exit 

#2 on route 1, congigure a static route so that all devices can ping any other device 
#ip route 192.168.191.2 255.255.255.0 f0/0   (may not need?)
ip route 192.168.100.0 255.255.255.0 192.168.1.2 
do sh ip route

#3 configure Router 2 with a host name of Route 2. configre the apporiate Ip address on the interface, refer to the IP address table. enable the interface 
en 
conf t 
host
hostname R2
int 
interface f0/0
ip address  192.168.101.0 255.255.255.0 
no shut
do sh ip int

int s0/0
ip address 192.168.1.2 255.255.255.0 
no shut 

#4 on route 2, configate a static route so that all devices can ping any other device 
#ip route 192.168.191.2 255.255.255.0 f0/0
ip route 192.168.101.0 255.255.255.0 192.168.1.1
do sh ip route

#5 on Host A and Host B, configure the apporiate IP address and default gateway, refer to IP address table 
@host A
ipconfig /all
ipconfig /ip 192.168.101.2 255.255.255.0
ipconfig /dg 192.168.101.1 
#ipconfig /ip 0.0.0.0 0.0.0.0 192.168.101.1
ipconfig /all 

#6 on Host A and Host B, configure the apporiate IP address and default gateway, refer to IP address table 
ipconfig /ip 192.168.100.2 255.255.255.0
ipconfig /dg 192.168.100.1 

#7 on route 1 and route 2, dispaly the routle table. you should see the static routes you added 
sh ip route 

#8 verify your configuation by ping from hostA to hostB(192.168.100.2)
ping 192.168.100.2
