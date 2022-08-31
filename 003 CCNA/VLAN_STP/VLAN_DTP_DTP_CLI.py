#Created by Kenneth zeng 
#8/22/2022
#VTP and DTP CLI 
"""
DTP negotiation
desirable  forms trunk with trunk, dynmaic desirable, auto, but not accces(acess ports in the Default VLAN)
disireable with auto  => i will form a trunk, but i am not actively try to form a trunk with you

auto form trunk with trunk and dynamic disirable only
     

"""


############################1 DTP ###############################
swithport mode ?     #dynamic for DTP; also have otheroption: trunk, access, dot1q-tunnel, private-vlan

swithchport mode dynamic ?     ##auto , desirable 

show interface g0/0 switchport   #do show interface g0/0 switchport 



#switchport mode trunk 
#switchport mode dynamic desirable 
#switchport mode dynmaic auto 

#disable DTP negotiation 
switchport nonegotiate 
#configure an access port  also diable DTP negotiabtion on interface 
switchport mode access 


#The negotiaton is enable by default ,as the default trunk encapsulation mode is 
switchport trunk encapsulation negotiate 


############################2 VTP ###############################
#@server switch 
show vtp status 


#add VTP domain name
config t 
vtp domain cisco 

#create vlan and add vlan name 
vlan 10 
name enginneering 
exit 

show vlan brief


#@client switch 
vtp mode client 
vlan 20    #now allowed because sw2 is now in client mode 

#at another switch  transparent mode 
vtp mode transparent 
vtp domain juniper   #changing VTP domain name from cisco to juniper 

#to change VTP version 
#2 server switch config 
vtp version 2 


##VTP password 
vtp password cisco 






