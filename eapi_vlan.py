import json
from jsonrpclib import Server

switches = ["192.168.0.14", "192.168.0.15", "192.168.0.16","192.168.0.17"]
username = "arista"
password = "arista"

# Going through all the switch IP addresses listed above
for switch in switches:
    urlString = "https://{}:{}@{}/command-api".format(username, password, switch)
    switchReq = Server( urlString )

    # Display the current vlan list
    response = switchReq.runCmds( 1, ["show vlan"] )
    print "Switch : " + switch + " VLANs: "
    print response[0]["vlans"].keys()

    # Add vlan 100 to the switch
    print "Adding vlan 100"
    response = switchReq.runCmds( 1, ["enable", "configure", "vlan 100"] )

    # List the vlans again to show vlan 100 configured
    response = switchReq.runCmds( 1, ["show vlan"] )
    print "Switch : " + switch + " VLANs: "
    print response[0]["vlans"].keys()
    print

print "\n*** Done adding vlan to switches ***\n"

print "\n*** Script done ***"
