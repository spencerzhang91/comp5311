#!/usr/bin/python
# Create a ring topology network

from mininet.net import Mininet
from mininet.node import Controller, RemoteController, OVSController
from mininet.node import CPULimitedHost, Host, Node
from mininet.node import OVSKernelSwitch, UserSwitch
from mininet.node import IVSSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.link import TCLink, Intf
from subprocess import call
import sys


def myNetwork(num):

    net = Mininet( topo=None,
                   build=False,
                   ipBase='10.0.0.0/8')

    info( '*** Adding controller\n' )
    c0=net.addController(name='c0',
                      controller=Controller,
                      protocol='tcp',
                      port=6633)

    info( '*** Add switches\n')
    s=[]
    for i in range(0,num):

        s.append( net.addSwitch('s'+str(i), cls=OVSKernelSwitch,
                                            failMode='standalone',
                                            stp=1))

        # s.append( net.addSwitch('s'+str(i), cls=OVSKernelSwitch))


    info( '*** Add hosts\n')
    h=[]
    for i in range(0,num):
        tmp=i+1
        h.append(net.addHost('h'+str(i), cls=Host, ip='10.0.0.'+str(tmp), defaultRoute=None))
    h.append(net.addHost('h'+str(num+1), cls=Host, ip='10.0.0.'+str(num+1), defaultRoute=None))

    info( '*** Add links\n')
    print(h)
    print(s)
    # wire up hosts and switches:
    for i in range(0,num):
        net.addLink(h[i],s[i])
    net.addLink(s[num-1], h[num])

    # wire up switches:
    for  i in range(1,num):
        net.addLink(s[i-1],s[i])
    # create a loop:
    net.addLink(s[num-1], s[0])

    info( '*** Starting network\n')
    net.build()
    info( '*** Starting controllers\n')
    for controller in net.controllers:
        controller.start()

    info( '*** Starting switches\n')
    for i in range(0,num):
        net.get('s'+str(i)).start([c0])

    info( '*** Post configure switches and hosts\n')

    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    number=int(sys.argv[1])
    print(number)
    myNetwork(number)
