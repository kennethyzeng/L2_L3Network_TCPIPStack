#Created by kenenth zeng 
#08/22/2022
##Blow Command are operated with Cisco Switch or Router

####################1 ECMP(Equal cost multiple path) with static routing ##########################
####configure two static route to dst IP for load balance purpose 
ip route 192.168.4.0 2555.255.255.0 10.0.12.2
ip route 192.168.4.0 2555.255.255.0 10.0.13.2

####################2 to assign metric ##########################
ip route 192.168.4.0 2555.255.255.0 10.0.12.2 ? 



####################3 floating static Routing################
#by Changing AD higher to make it less preferred than dynamic route
ip route 192.168.4.0 2555.255.255.0 10.0.12.2 110
sh ip route 




####################4 example of floating static routing ###########
#1  check the routing tables of R1 and R2 
en
sh ip route 

#2 configure floaing static routes on R1 and R2 that stilll have 
connection if the link between R1 and R2 failed 
#@R2 
conf t
ip route 10.0.1.0 255.255.255.0 203.0.113.5 111
do sh ip route 
#Note: do the same to another routes, 

#3 shut down the G2/0 interface of R1 or R2. ping dst IP from your PC