
import subprocess
import re

esxi_name = ['jasmine', 'lotus', 'mint', 'violet', 'rose']
get_vm_list = 'vim-cmd vmsvc/getallvms'

for esxi in esxi_name:
    print(esxi)
    ssh_command = f"ssh {esxi} {get_vm_list}"

    result = subprocess.run(ssh_command, shell=True, capture_output=True, text=True)

    vm_list = result.stdout.strip().split('\n')
    list = []
    for i in vm_list:
        i = i.split(' ')
        a = []
        for j in i:
            if j == '':
                continue
            else:
                a.append(j)
        list.append(a)

    list_dic = []
    for j in range(1, len(list)):
        dic = {}
        for k in range(len(list[0])):
            try:
                dic[list[0][k]] = list[j][k]
            except:
                dic[list[0][k]] = ''
        list_dic.append(dic)

    for i in list_dic:
        print(i["Vmid"])
        getvm = f"ssh jasmine vim-cmd vmsvc/get.guest {i["Vmid"]}"
        vm = subprocess.run(getvm, shell=True, capture_output=True, text=True)
        vm = vm.stdout.replace(' ', '')
        vm = vm.split("\n")
        for j in vm:
            if "hostName" in j and "<unset>" not in j:
                print(j)
            if 'ipAddress="192.168.' in j and "<unset>" not in j:
                print(j)

