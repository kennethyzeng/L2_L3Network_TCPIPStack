#Created by Kenneth Zeng 
#08/22/2022

###############################Layer 2 EtherChannel ###############################
#1  check and Configure load-balancing method  

#@Access Switch 
show etherchannel load-balance

#Change the load-balancing method, Enter globla config mode 
conf t 
port-channel load-balance src-dst-mac 
do show etherchannel load-balance

port-channel load-balance ?  //show all the options for load balance 



#2   Create Etherchannel between two switches 
####PAgP configuration
@Access switch(config)
interface range g0/0 -3 
channel-group 1 mode ? 
#two options for PagP, two for LACP, one for static etherchannel
channel-group 1 mode desirable 
#Creating a port channel interface port-channel 1

#similar to LACP but choose differnt mode name 
#similar to static etherchannel


#3 Manually Configure the Negotiation protocol that the member interfaces should use channel-protocol command 
interface range f0/0 - 3
channel-protocol  ?       //LACP or pagp 
channel-protocol lacp 
channel-group 1 mode desirable 


#4 confige the port-channel interface itself 
#@Access switch => config 
Interface port-channel 1 
switchport trunk encapsulation dot1q 
switchport mode trunk 
do show interfaces trunk 


#5

#Verify the status of an therchannel 
show etherchannel summary

##command to shut down port channel 1 interface 
interface po1
shutdown 

#change one of the member interface to access mode 
interface g0/0
swithport mode access 
do show etherchannel summary 

#see the numbers of ports in the port-channel, 
which protocol is being used , port status
@ASW
show etherchannel port-channel 

#see how etherchannel affect STP
show spanning-tree 


###############################Layer 3 EtherChannel ###############################
#configure Layer 3 etherchannel
#start from a clean configaution , no port-channel have been configuared yet 
@#ASW
int range g0/0 -3 
no switchport   //use the no switchport command to make them layer 3 routed swtich 
channel-group 1 mode activate 

//we need ip address for layer 3
#int po1      //configure on port channel interface 
#ip address 10.0.0.1 255.255.255.252 

#do sh etherch sum 


#@ASW 
show ip interface brief     //see port-channel 