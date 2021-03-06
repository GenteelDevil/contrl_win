'''
Author: your name
Date: 2020-09-24 16:11:15
LastEditTime: 2020-09-27 13:13:03
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /control_win/scripts/invade.py
'''
import time
import random
from IPy import IP

class show():
    def __init__(self):
        self.hosts = []
        self.ipsegs = []
        # 需要进行感染的IP
        self.ipsegs_to_infect = ['192.168.0.0/24', '192.168.1.1', '10.59.12.0/24']
    
    def random_ipseg(self, num):
        # 获得随机的一些内网IP段
        ip1_c = [10, 172, 192]
        ipsegs_set = []
        while num != 0:
            ip1 = ip1_c[random.randint(0, 2)]
            if ip1 == 10:
                ip2 = random.randint(0, 255)
            elif ip1 == 172 :
                ip2 = random.randint(16, 31)
            else:
                ip2 = 168
            ip3 = random.randint(1, 24)
            ip4 = 0

            ipseg = str(ip1) + '.' + str(ip2) + '.' + str(ip3) + '.' + str(ip4) + '/24'
            if ipseg in ipsegs_set:
                continue
            else:
                ipsegs_set.append(ipseg)
                num -= 1 
        for each in self.ipsegs_to_infect:
            if '/' in each:
                ipsegs_set.append(each)
            else:
                tmp_host = {}
                anti_mal = ['Kaspersky', 'Norton', '360']
                tmp_host['mac'] = self.random_mac()
                tmp_host['ip_seg'] = each
                tmp_host['ip'] = each
                tmp_host['server'] = not bool(random.randint(1, 5) % 5)
                tmp_host['status'] = bool(random.randint(1, 5) % 5)
                if tmp_host['server']:
                    tmp_host['antimal'] = anti_mal[random.randint(0, 2) % 3]
                else:
                    tmp_host['antimal'] = None
                self.hosts.append(tmp_host)
        return ipsegs_set
    
    def random_ips(self, ips, num):
        # 从给定的IP段中获得随机的IP
        # TODO 这个地方最好不要用IP这个库，使用计算的方式比较好
        ip_set = []
        ip_raw = IP(ips)
        if num > len(ip_raw):
            return None
        
        while num!= 0:
            random_index = random.randint(0, len(ip_raw))
            random_ip = str(ip_raw[random_index])
            if random_ip in ip_set:
                num += 1
                continue
            else:
                ip_set.append(random_ip)
                num -= 1
        return ip_set
    
    def random_mac(self):
        Maclist = []
        for i in range(1,7):
            RANDSTR = "".join(random.sample("0123456789abcdef",2))
            Maclist.append(RANDSTR)
        RANDMAC = ":".join(Maclist)
        return RANDMAC
    
    # 从以下是正式的功能

    def init_hosts(self, num_ipsegs, min_num_ips, max_num_ips):
        # 加载config文件
        # 重要的一些config字段
        # - IP字段
        # 存储已有的主机
        anti_mal = ['Kaspersky', 'Norton', '360']
        # 指定数量的IP段
        self.ipsegs = self.random_ipseg(num_ipsegs)
        for ipseg in self.ipsegs:
            # 从IP段中获得IP
            num = random.randint(min_num_ips, max_num_ips)
            ips = self.random_ips(ipseg, num=num)
            for ip in ips:
                tmp_host = {}
                tmp_host['mac'] = self.random_mac()
                tmp_host['ip_seg'] = ipseg
                tmp_host['ip'] = ip
                tmp_host['server'] = not bool(random.randint(1, 5) % 5)
                tmp_host['status'] = bool(random.randint(1, 5) % 5)
                if tmp_host['server']:
                    tmp_host['antimal'] = anti_mal[random.randint(0, 2) % 3]
                else:
                    tmp_host['antimal'] = None
                self.hosts.append(tmp_host)
    
    def init_test_hosts(self, num_ipsegs, min_num_ips, max_num_ips):
    # 加载config文件
    # 重要的一些config字段
    # - IP字段
    # 存储已有的主机
        anti_mal = ['Kaspersky', 'Norton', '360']
        arch = ['win7/32', 'win7/64', 'win8/32', 'win8/64', 'winserver2008/32', 'winserver2008/64', 'winserver2012/32', 'winserver2012/64', 'winserver2016/32', 'winserver2016/64']
        # 指定数量的IP段
        self.ipsegs = self.random_ipseg(num_ipsegs)
        for ipseg in self.ipsegs:
            # 从IP段中获得IP
            num = random.randint(min_num_ips, max_num_ips)
            ips = self.random_ips(ipseg, num=num)
            for ip in ips:
                tmp_host = {}
                tmp_host['mac'] = self.random_mac()
                tmp_host['ip_seg'] = ipseg
                tmp_host['ip'] = ip
                tmp_host['server'] = not bool(random.randint(1, 5) % 5)
                tmp_host['status'] = bool(random.randint(1, 5) % 5)
                if tmp_host['server']:
                    tmp_host['antimal'] = anti_mal[random.randint(0, 2) % 3]
                else:
                    tmp_host['antimal'] = None
                self.hosts.append(tmp_host)
                
    # 正式的step文件
    def parse_config(self):
        print("\n###############################################")
        print("Stage 1: parse configure files")
        print("[+] Reading configurations from files...")

    def output_config(self):
        print("\n###############################################")
        print("Stage 2: show configurations")
        print("[+] " + str(len(self.ipsegs)) + " IP ranges loaded")
        for each in self.ipsegs:
            print("  [-] " + each)
        print("[+] Operation mode : Semi-automatic")
        print("  [*] hosts to be infected in IP range")
        # TODO 这个地方添加扩散范围
        for each in self.ipsegs_to_infect:
            print("    [-] " + each)
        print("  [*] data destroy function activate")
        print("  [*] system paralyze function deactivate")


    def scan_hosts(self):
        # 对整体的主机进行扫描
        print("\n###############################################")
        print("Stage 3: scan hosts")
        print("[+] Scanning hosts in IP ranges")
        print("      IP                MAC         Server   Status")
        for host in self.hosts:
            if host['server']:
                server_flag = "yes"
            else:
                server_flag = "   "
            if host['status']:
                server_status = "oneline"
            else:
                server_status = "offline"
            print("  " + '%-13s' % host['ip'] + "   " + host['mac'] + "   " + server_flag + "   " + server_status)


    def show_server(self):
        # 输出扫描到主机的相关情况
        # IP、MAC、Status、是否server
        print("\n###############################################")
        print("Stage 4: show servers")
        print("[+] Calculating servers")
        print("  [-] servers info:")
        print("         IP                MAC          Anti-Mal") 
        for host in self.hosts:
            if host['server']:
                print("    " + '%-13s' % host['ip'] + "   " + host['mac']  + "   " + host['antimal'])

    def check_available(self):
        print("\n###############################################")
        print("Stage 5 check servers' availability")
        
        
        
    


if __name__ == "__main__":
    test = show()
    test.init_hosts(10, 4, 8)
    test.parse_config()
    test.output_config()
    test.scan_hosts()
    test.show_server()
    test.check_available()