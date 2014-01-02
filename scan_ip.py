import threading
import datetime
import socket
ports = [22,19381,3389,8888,80]
ipseg = "119.147.208.%s"


def scan_ip(addr_list,port):
    reachable_ips = {}

class ThreadClass(threading.Thread):
    def __init__(self, addr_list,port):
      threading.Thread.__init__(self)
      self.addr_list = addr_list
      self.port = port
      self.reachable_ips = []

    def run(self):
        for addr in self.addr_list:
            try:
                conn = socket.create_connection((addr,self.port),2)
                conn.close
                self.reachable_ips[addr] = [self.port]
            except Exception,ex:
                print ex
def split_list(alist, wanted_parts=1):
    length = len(alist)
    return [ alist[i*length // wanted_parts: (i+1)*length // wanted_parts]
             for i in range(wanted_parts) ]
addr_list  = [ "ipseg %s " % i for i xrange(1,255) ]
split_list(
for i in range(2):
  t = ThreadClass()
  t.start()

print reachable_ips
