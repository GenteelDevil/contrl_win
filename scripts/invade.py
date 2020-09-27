'''
Author: your name
Date: 2020-09-24 16:11:15
LastEditTime: 2020-09-27 15:23:33
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
        self.ipsegs = ['192.168.0.0/16', '172.16.0.0/16', '10.0.0.0/16']
        # 需要进行感染的IP
        self.ipsegs_to_infect = ['192.168.0.0/16',
                                 '172.16.0.0/16', '10.0.0.0/24']

    def random_ipseg(self, num):
        # 获得随机的一些内网IP段
        ip1_c = [10, 172, 192]
        ipsegs_set = []
        while num != 0:
            ip1 = ip1_c[random.randint(0, 2)]
            if ip1 == 10:
                ip2 = random.randint(0, 255)
            elif ip1 == 172:
                ip2 = random.randint(16, 31)
            else:
                ip2 = 168
            ip3 = random.randint(1, 24)
            ip4 = 0

            ipseg = str(ip1) + '.' + str(ip2) + '.' + \
                str(ip3) + '.' + str(ip4) + '/24'
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

        while num != 0:
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
        for i in range(1, 7):
            RANDSTR = "".join(random.sample("0123456789abcdef", 2))
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
        arch = ['win7/32', 'win7/64', 'win8/32', 'win8/64', 'winserver2008/32', 'winserver2008/64',
                'winserver2012/32', 'winserver2012/64', 'winserver2016/32', 'winserver2016/64']
        # 指定数量的IP段
        for ipseg in self.ipsegs:
            # 从IP段中获得IP
            num = random.randint(min_num_ips, max_num_ips)
            ips = self.random_ips(ipseg, num=num)
            for ip in ips:
                tmp_host = {}
                tmp_host['mac'] = self.random_mac()
                tmp_host['ip_seg'] = ipseg
                tmp_host['ip'] = ip
                tmp_host['server'] = False
                tmp_host['status'] = True
                if tmp_host['server']:
                    tmp_host['antimal'] = anti_mal[random.randint(0, 2) % 3]
                else:
                    tmp_host['antimal'] = None
                tmp_host['arch'] = arch[random.randint(0, 3)]
                self.hosts.append(tmp_host)
        for each in self.hosts:
            print(str(each) + ', ')

    def init_hosts_final(self):
        self.hosts = [{'mac': 'cd:08:b8:8b:02:7b', 'ip_seg': '192.168.0.0/16', 'ip': '192.168.91.120', 
                          'server': False, 'status': True, 'antimal': None, 'arch': 'win8/64'},
                      {'mac': '4d:b3:20:60:b5:51', 'ip_seg': '192.168.0.0/16', 'ip': '192.168.207.245',
                          'server': False, 'status': True, 'antimal': None, 'arch': 'win8/64'},
                      {'mac': 'ec:b0:2b:59:cb:9f', 'ip_seg': '192.168.0.0/16', 'ip': '192.168.160.227',
                          'server': False, 'status': True, 'antimal': None, 'arch': 'win8/64'},
                      {'mac': '2e:e7:de:91:b7:bd', 'ip_seg': '192.168.0.0/16', 'ip': '192.168.133.151',
                       'server': False, 'status': True, 'antimal': None, 'arch': 'win8/32'},
                      {'mac': '9c:23:87:89:94:69', 'ip_seg': '192.168.0.0/16', 'ip': '192.168.149.5',
                       'server': False, 'status': True, 'antimal': None, 'arch': 'win7/32'},
                      {'mac': '6e:32:5c:9f:f7:ec', 'ip_seg': '192.168.0.0/16', 'ip': '192.168.207.190',
                       'server': False, 'status': True, 'antimal': None, 'arch': 'win8/64'},
                      {'mac': 'c6:7d:39:13:e8:b6', 'ip_seg': '192.168.0.0/16', 'ip': '192.168.170.52',
                       'server': False, 'status': True, 'antimal': None, 'arch': 'win7/64'},
                      {'mac': 'b7:1c:fd:34:b6:78', 'ip_seg': '192.168.0.0/16', 'ip': '192.168.12.201',
                       'server': False, 'status': True, 'antimal': None, 'arch': 'win8/64'},
                      {'mac': 'fa:85:53:5a:87:5f', 'ip_seg': '192.168.0.0/16', 'ip': '192.168.22.0',
                       'server': False, 'status': True, 'antimal': None, 'arch': 'win8/32'},
                      {'mac': '94:f8:04:01:73:4f', 'ip_seg': '192.168.0.0/16', 'ip': '192.168.224.85',
                       'server': False, 'status': True, 'antimal': None, 'arch': 'win8/64'},
                      {'mac': 'c1:cd:53:50:e4:bd', 'ip_seg': '192.168.0.0/16', 'ip': '192.168.100.1',
                       'server': True, 'status': True, 'antimal': 'Kaspersky', 'arch': 'winserver2000/64'},
                      {'mac': 'f5:c7:21:36:a8:1e', 'ip_seg': '192.168.0.0/16', 'ip': '192.168.9.17',
                       'server': False, 'status': True, 'antimal': None, 'arch': 'win7/32'},
                      {'mac': '53:2f:ea:c8:57:82', 'ip_seg': '192.168.0.0/16', 'ip': '192.168.36.195',
                       'server': False, 'status': True, 'antimal': None, 'arch': 'win7/32'},
                      {'mac': 'c8:2f:c7:a7:04:03', 'ip_seg': '192.168.0.0/16', 'ip': '192.168.61.5',
                       'server': False, 'status': True, 'antimal': None, 'arch': 'win7/64'},
                      {'mac': '3d:82:3e:e9:a9:5e', 'ip_seg': '192.168.0.0/16', 'ip': '192.168.45.230',
                       'server': False, 'status': True, 'antimal': None, 'arch': 'win8/64'},
                      {'mac': 'd9:19:cb:98:d3:07', 'ip_seg': '192.168.0.0/16', 'ip': '192.168.190.240',
                       'server': False, 'status': True, 'antimal': None, 'arch': 'win8/32'},
                      {'mac': '87:7b:bf:a4:d8:de', 'ip_seg': '192.168.0.0/16', 'ip': '192.168.200.164',
                       'server': False, 'status': True, 'antimal': None, 'arch': 'win8/64'},
                      {'mac': 'a1:f0:5d:74:b8:15', 'ip_seg': '192.168.0.0/16', 'ip': '192.168.199.172',
                       'server': False, 'status': True, 'antimal': None, 'arch': 'win8/32'},
                      {'mac': '81:1b:2e:18:12:9e', 'ip_seg': '192.168.0.0/16', 'ip': '192.168.106.239',
                       'server': False, 'status': True, 'antimal': None, 'arch': 'win7/64'},
                      {'mac': 'c9:02:a2:0e:a8:91', 'ip_seg': '192.168.0.0/16', 'ip': '192.168.146.22',
                       'server': False, 'status': True, 'antimal': None, 'arch': 'win8/64'},
                      {'mac': '4a:82:68:8c:d1:29', 'ip_seg': '192.168.0.0/16', 'ip': '192.168.37.181',
                       'server': False, 'status': True, 'antimal': None, 'arch': 'win8/64'},
                      {'mac': '71:f5:3c:72:18:c8', 'ip_seg': '172.16.0.0/16', 'ip': '172.16.194.1',
                       'server': False, 'status': True, 'antimal': None, 'arch': 'win7/32'},
                      {'mac': '6e:76:9c:f5:31:7e', 'ip_seg': '172.16.0.0/16', 'ip': '172.16.6.108',
                       'server': False, 'status': True, 'antimal': None, 'arch': 'win8/64'},
                      {'mac': '50:7a:6a:e8:8f:4f', 'ip_seg': '172.16.0.0/16', 'ip': '172.16.234.29',
                       'server': False, 'status': True, 'antimal': None, 'arch': 'win7/64'},
                      {'mac': 'b1:26:3c:6e:82:c1', 'ip_seg': '172.16.0.0/16', 'ip': '172.16.142.235',
                       'server': False, 'status': True, 'antimal': None, 'arch': 'win7/32'},
                      {'mac': '8d:d7:8a:cf:38:9c', 'ip_seg': '172.16.0.0/16', 'ip': '172.16.144.238',
                       'server': False, 'status': True, 'antimal': None, 'arch': 'win8/32'},
                      {'mac': '9f:6b:a4:0f:92:19', 'ip_seg': '172.16.0.0/16', 'ip': '172.16.160.226',
                       'server': False, 'status': True, 'antimal': None, 'arch': 'win8/64'},
                      {'mac': '19:19:f0:e2:46:c2', 'ip_seg': '172.16.0.0/16', 'ip': '172.16.224.91',
                       'server': False, 'status': True, 'antimal': None, 'arch': 'win7/32'},
                      {'mac': 'b1:60:e4:97:c2:cb', 'ip_seg': '172.16.0.0/16', 'ip': '172.16.52.123',
                       'server': False, 'status': True, 'antimal': None, 'arch': 'win8/32'},
                      {'mac': '57:ae:73:1d:90:ca', 'ip_seg': '172.16.0.0/16', 'ip': '172.16.5.2',
                       'server': False, 'status': True, 'antimal': None, 'arch': 'win8/64'},
                      {'mac': 'e9:be:b8:c4:0e:3f', 'ip_seg': '172.16.0.0/16', 'ip': '172.16.100.1',
                       'server': True, 'status': True, 'antimal': 'Norton', 'arch': 'winserver2012'},
                      {'mac': '5e:eb:53:7f:1d:1a', 'ip_seg': '172.16.0.0/16', 'ip': '172.16.63.184',
                       'server': False, 'status': True, 'antimal': None, 'arch': 'win7/32'},
                      {'mac': 'a6:30:a4:4b:32:7a', 'ip_seg': '172.16.0.0/16', 'ip': '172.16.42.37',
                       'server': False, 'status': True, 'antimal': None, 'arch': 'win8/32'},
                      {'mac': 'cf:82:17:b9:ea:4d', 'ip_seg': '172.16.0.0/16', 'ip': '172.16.190.35',
                       'server': False, 'status': True, 'antimal': None, 'arch': 'win7/64'},
                      {'mac': '53:52:04:c1:82:38', 'ip_seg': '172.16.0.0/16', 'ip': '172.16.169.184',
                       'server': False, 'status': True, 'antimal': None, 'arch': 'win8/64'},
                      {'mac': '13:85:54:6f:c5:b2', 'ip_seg': '172.16.0.0/16', 'ip': '172.16.171.76',
                       'server': False, 'status': True, 'antimal': None, 'arch': 'win7/64'},
                      {'mac': '0e:d9:30:e7:2f:13', 'ip_seg': '172.16.0.0/16', 'ip': '172.16.184.161',
                       'server': False, 'status': True, 'antimal': None, 'arch': 'win7/32'},
                      {'mac': 'b4:72:38:14:52:5a', 'ip_seg': '172.16.0.0/16', 'ip': '172.16.252.180',
                       'server': False, 'status': True, 'antimal': None, 'arch': 'win7/64'},
                      {'mac': '43:fb:21:56:39:15', 'ip_seg': '172.16.0.0/16', 'ip': '172.16.33.14',
                       'server': False, 'status': True, 'antimal': None, 'arch': 'win8/32'},
                      {'mac': '5a:fa:b0:8a:f8:2c', 'ip_seg': '172.16.0.0/16', 'ip': '172.16.159.87',
                       'server': False, 'status': True, 'antimal': None, 'arch': 'win7/64'},
                      {'mac': 'f8:45:35:46:e6:9e', 'ip_seg': '172.16.0.0/16', 'ip': '172.16.30.166',
                       'server': False, 'status': True, 'antimal': None, 'arch': 'win7/64'},
                      {'mac': 'b2:76:4f:ae:12:4b', 'ip_seg': '172.16.0.0/16', 'ip': '172.16.23.70',
                       'server': False, 'status': True, 'antimal': None, 'arch': 'win8/32'},
                      {'mac': '98:7e:a9:07:fc:6e', 'ip_seg': '172.16.0.0/16', 'ip': '172.16.70.241',
                       'server': False, 'status': True, 'antimal': None, 'arch': 'win7/32'},
                      {'mac': '95:49:81:6d:a2:a2', 'ip_seg': '172.16.0.0/16', 'ip': '172.16.190.213',
                       'server': False, 'status': True, 'antimal': None, 'arch': 'win8/64'},
                      {'mac': '46:d6:7a:59:df:24', 'ip_seg': '172.16.0.0/16', 'ip': '172.16.191.23',
                       'server': False, 'status': True, 'antimal': None, 'arch': 'win7/64'},
                      {'mac': 'a8:6a:4f:ea:84:b8', 'ip_seg': '172.16.0.0/16', 'ip': '172.16.52.110',
                       'server': False, 'status': True, 'antimal': None, 'arch': 'win8/64'},
                      {'mac': 'b8:13:e4:1a:75:f7', 'ip_seg': '10.0.0.0/16', 'ip': '10.0.207.189',
                       'server': False, 'status': True, 'antimal': None, 'arch': 'win8/64'},
                      {'mac': '75:84:b7:be:ac:d2', 'ip_seg': '10.0.0.0/16', 'ip': '10.0.26.42',
                       'server': False, 'status': True, 'antimal': None, 'arch': 'win8/64'},
                      {'mac': '6f:f2:3d:ce:db:6a', 'ip_seg': '10.0.0.0/16', 'ip': '10.0.14.163',
                       'server': False, 'status': True, 'antimal': None, 'arch': 'win7/32'},
                      {'mac': 'f5:c5:91:86:53:5a', 'ip_seg': '10.0.0.0/16', 'ip': '10.0.34.240',
                       'server': False, 'status': True, 'antimal': None, 'arch': 'win7/32'},
                      {'mac': 'df:1b:1c:cd:ae:39', 'ip_seg': '10.0.0.0/16', 'ip': '10.0.91.26',
                       'server': False, 'status': True, 'antimal': None, 'arch': 'win8/32'},
                      {'mac': 'd4:e2:09:f6:7a:4e', 'ip_seg': '10.0.0.0/16', 'ip': '10.0.49.9',
                       'server': False, 'status': True, 'antimal': None, 'arch': 'win8/64'},
                      {'mac': 'b7:a6:0f:4b:90:fb', 'ip_seg': '10.0.0.0/16', 'ip': '10.0.29.30',
                       'server': False, 'status': True, 'antimal': None, 'arch': 'win8/32'},
                      {'mac': '9e:c0:64:93:47:b1', 'ip_seg': '10.0.0.0/16', 'ip': '10.0.177.80',
                       'server': False, 'status': True, 'antimal': None, 'arch': 'win7/64'},
                      {'mac': 'd1:de:7e:67:e0:90', 'ip_seg': '10.0.0.0/16', 'ip': '10.0.144.116',
                       'server': False, 'status': True, 'antimal': None, 'arch': 'win8/64'},
                      {'mac': 'c0:04:3a:47:8a:18', 'ip_seg': '10.0.0.0/16', 'ip': '10.0.206.10',
                       'server': False, 'status': True, 'antimal': None, 'arch': 'win8/32'},
                      {'mac': '35:8a:f5:05:32:87', 'ip_seg': '10.0.0.0/16', 'ip': '10.0.94.152',
                       'server': False, 'status': True, 'antimal': None, 'arch': 'win8/32'},
                      {'mac': '6e:a9:a8:be:86:e0', 'ip_seg': '10.0.0.0/16', 'ip': '10.0.196.144',
                       'server': False, 'status': True, 'antimal': None, 'arch': 'win8/32'},
                      {'mac': '6e:45:5a:21:b2:e6', 'ip_seg': '10.0.0.0/16', 'ip': '10.0.100.1',
                       'server': True, 'status': True, 'antimal': '360', 'arch': 'win8/64'},
                      {'mac': '85:8c:58:d1:71:6f', 'ip_seg': '10.0.0.0/16', 'ip': '10.0.88.58',
                       'server': False, 'status': True, 'antimal': None, 'arch': 'win8/32'},
                      {'mac': 'ea:7a:e6:37:95:ab', 'ip_seg': '10.0.0.0/16', 'ip': '10.0.165.134',
                       'server': False, 'status': True, 'antimal': None, 'arch': 'win8/32'},
                      {'mac': '82:5d:da:27:51:b2', 'ip_seg': '10.0.0.0/16', 'ip': '10.0.113.188',
                       'server': False, 'status': True, 'antimal': None, 'arch': 'win8/32'},
                      {'mac': 'f6:78:60:9c:e3:81', 'ip_seg': '10.0.0.0/16', 'ip': '10.0.205.250',
                       'server': False, 'status': True, 'antimal': None, 'arch': 'win7/32'},
                      {'mac': 'f3:e2:51:39:f2:a9', 'ip_seg': '10.0.0.0/16', 'ip': '10.0.29.168',
                       'server': False, 'status': True, 'antimal': None, 'arch': 'win7/64'},
                      {'mac': '67:1b:6e:5a:91:31', 'ip_seg': '10.0.0.0/16', 'ip': '10.0.138.169',
                       'server': False, 'status': True, 'antimal': None, 'arch': 'win8/32'},
                      {'mac': '82:47:75:24:be:20', 'ip_seg': '10.0.0.0/16', 'ip': '10.0.89.151', 
                       'server': False, 'status': True, 'antimal': None, 'arch': 'win8/32'}]
    # 正式的step文件

    def parse_config(self):
        print("\n####################################################################")
        print("Stage 1: parse configure files")
        print("[+] Reading configurations from files...")

    def output_config(self):
        print("\n####################################################################")
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
        print("\n####################################################################")
        print("Stage 3: scan hosts")
        print("[+] Scanning hosts in IP ranges")
        print("      IP                    MAC           Server      Status")
        for host in self.hosts:
            if host['server']:
                server_flag = "yes"
            else:
                server_flag = "   "
            if host['status']:
                server_status = "oneline"
            else:
                server_status = "offline"
            print("  " + '%-15s' % host['ip'] + "    " + host['mac'] +
                  "     " + server_flag + "       " + server_status)

    def show_server(self):
        # 输出扫描到主机的相关情况
        # IP、MAC、Status、是否server
        print("\n####################################################################")
        print("Stage 4: show servers")
        print("[+] Calculating servers")
        print("  [-] servers info:")
        print("         IP                MAC           Anti-Mal       Arch")
        for host in self.hosts:
            if host['server']:
                print("    " + '%-13s' %
                      host['ip'] + "   " + host['mac'] + "   " + '%-10s' % host['antimal'] + "   " + host['arch'])

    def check_available(self):
        print("\n####################################################################")
        print("Stage 5 check servers' availability")
        print("[+] Tring to connect servers")
        for each in self.hosts:
            if each['server'] == True:
                print("  [-] Target IP : " + each['ip'])
                print("    [*] Connecting...")
                print("    [*] Connect Success!")
                print("    [*] Loading control module...")
                print("    [*] Load Success!")
        print("\n####################################################################")
        print("Final Step")
        print("[+] All Steps finished!")

if __name__ == "__main__":
    test = show()
    test.init_hosts_final()
    test.parse_config()
    test.output_config()
    test.scan_hosts()
    test.show_server()
    test.check_available()
