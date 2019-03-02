from sTools import tools

t = tools("IP")
t2 = tools("Mask")
print("Ip Conversion Decimal to Binary")
while True:
    ipN = input("Type an IP: ")
    t.setIpNumber(ipN)
    mask = input("Type an Mask: ")
    t2.setIpNumber(mask)
    print("Binary IP:   " + t.decToBin())
    print("Binary Mask: " + t2.decToBin() + "/" + str(t2.maskSuffix(t2.decToBin())))
    print("Network:     " + t2.networkNumber(t.decToBin(), t2.decToBin()))
    print("Network Dec: " + t2.binToDec(t2.networkNumber(t.decToBin(), t2.decToBin())))
