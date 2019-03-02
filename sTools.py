class tools:
    ipNumber = ""

    def __init__(self, name):
        self.name = name

    def setIpNumber(self, ipNumber):
        self.ipNumber = ipNumber

    def getIpNumber(self):
        return self.ipNumber

    def decToBin(self):
        table = [128, 64, 32, 16, 8, 4, 2, 1]
        ipSplit = self.ipNumber.split(".")
        binar = []
        for i in ipSplit:
            ipart = int(i)
            for t in table:
                if ipart >= t:
                    ipart = ipart - t
                    binar.append(1)
                else:
                    binar.append(0)

        n = 0
        n2 = 7
        bin = ""
        for b in binar:
            bin += str(b)
            if n == n2 and not n == 31:
                bin += "."
                n2 += 8
            n += 1
        return bin

    def maskSuffix(self, mask):
        num = 0
        for m in mask:
            if m == "1" or m == "0":
                num += int(m)
        return num

    def networkNumber(self, ip, mask):
        net = ""
        n = 0
        while n < len(ip):
            if ip[n] == "1" and mask[n] == "1":
                net += "1"
            elif (ip[n] == "1" and mask[n] == "0") or (ip[n] == "0" and mask[n] == "1") or (
                    ip[n] == "0" and mask[n] == "0"):
                net += "0"
            if ip[n] == ".":
                net += "."
            n += 1
        return net  # string

    def binToDec(self, net):
        table = [128, 64, 32, 16, 8, 4, 2, 1]
        bitable = net.split(".")
        dec = []
        dec2 = ""
        for i in bitable:
            num = 0
            sum = 0
            for j in i:
                if j == "1":
                    sum += table[num]
                num += 1
            dec.append(sum)
        n = 0
        dec2 = ""
        for b in dec:
            dec2 += str(b)
            if n < 3:
                dec2 += "."
            n += 1

        return dec2
