from sys import argv

script, filename = argv

txt = open(filename)

lines = txt.readlines()
txt.close()

devices = {}

for line in lines:
    tokens = line.split(' ')
    if tokens[1] == 'C':
        if tokens[2] in devices.keys():
            devices[tokens[2]]["Created"] = devices[tokens[2]]["Created"] + 1
        else:
            device = {}
            device["Created"] = 0
            #device["Received"] = 0
            device["Sent"] = 0
            device["Delivered"] = 0
            device["Aborted"] = 0
            device["Dropped"] = 0
            device["Removed"] = 0
            devices[tokens[2]] = device
    elif tokens[1] == 'S':
        if tokens[2] in devices.keys():
            devices[tokens[2]]["Sent"] = devices[tokens[2]]["Sent"] + 1
        else:
            device = {}
            device["Created"] = 0
            #device["Received"] = 0
            device["Sent"] = 0
            device["Delivered"] = 0
            device["Aborted"] = 0
            device["Dropped"] = 0
            device["Removed"] = 0
            devices[tokens[2]] = device
    elif tokens[1] == 'DE':
        if tokens[2] in devices.keys():
            devices[tokens[2]]["Delivered"] = devices[tokens[2]]["Delivered"] + 1
        else:
            device = {}
            device["Created"] = 0
            #device["Received"] = 0
            device["Sent"] = 0
            device["Delivered"] = 0
            device["Aborted"] = 0
            device["Dropped"] = 0
            device["Removed"] = 0
            devices[tokens[2]] = device
        if tokens[5] == 'A\n':
            devices[tokens[2]]["Aborted"] = devices[tokens[2]]["Aborted"] + 1
        elif tokens[5] == 'R\n':
            devices[tokens[2]]["Removed"] = devices[tokens[2]]["Removed"] + 1
    elif tokens[1] == 'DR':
        if tokens[2] in devices.keys():
            devices[tokens[2]]["Dropped"] = devices[tokens[2]]["Dropped"] + 1
        else:
            device = {}
            device["Created"] = 0
            #device["Received"] = 0
            device["Sent"] = 0
            device["Delivered"] = 0
            device["Aborted"] = 0
            device["Dropped"] = 0
            device["Removed"] = 0
            devices[tokens[2]] = device
for key in devices.keys():
    print key
    print devices[key]
    print '--------------------------------------------'
