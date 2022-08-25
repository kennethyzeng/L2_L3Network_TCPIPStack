##################################
#Kennethyzeng
#created by 05/2022
##################################
'''
Those CLI are operated at Cisco's Switch environment. It is not a python file, just use python file to store command lines
'''
#################STP######################
####1 PortFast####
inferface g0/2
spanning-tree portfast
Note: portfase is enabled at the interface level with CLI spanning-tree portfast

#at config level (global)
spanning-tree portfast default


####2  BPDU Guard###
inferface g0/2
spanning-tree bpdugard enable

#@config level 
spanning-tree portfast bpdugard default 
#Note: This enable BPDU Gard on all portfast-enable interfaces
