# VM-manager

## はじめに
複数のESXiを使用している環境で，仮想マシンの情報をまとめて管理しておこうという目的のプログラムです．

## get_vm.py
`vim-cmd vmsvc/getallvms`でESXiから仮想マシンのリストを取得

`vim-cmd vmsvc/get.guest {"Vmid"}`で仮想マシンの詳細情報を取得

ubuntu24.04上で，`python3 get_vm.py`で実行

実行結果↓
```
jasmine
132
138
169
200
203
hostName="c0a21030-monitoring-mj",
ipAddress="192.168.100.185",
ipAddress="192.168.100.185",
hostName="c0a21030-monitoring-mj",
204
205
206
208
209
21
210
hostName="c0a21030-monitoring-wj1",
ipAddress="192.168.100.187",
ipAddress="192.168.100.187",
hostName="c0a21030-monitoring-wj1",
```
ESXiの名前，Vmid，起動中の仮想マシンのhostNameとipAddressを出力

## table.sql
mariadbのテーブルスキーマ
- id    　　　　レコードのID
- uuid    　　　仮想マシンに与える固有のID
- vmname  　　　仮想マシンの名前
- hostname　　　仮想マシンのホスト名
- ipaddress　　 仮想マシンのIPv4アドレス
- created_by　　仮想マシンの作成者
- esxi　　　　　仮想マシンが登録されているESXiの名前
