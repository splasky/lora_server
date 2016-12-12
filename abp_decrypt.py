from Crypto.Cipher import AES
import binascii

class decodePHYpayload:
    def __init__(self, PHYpayload, key):
        """
        name       type    
        PHYpayload str 
        key        str   
        """
        print PHYpayload
        self.addr = PHYpayload[2:10]
        self.FCnt = PHYpayload[12:16]
        self.data = PHYpayload[18:-8]
        self.MIC = PHYpayload[-8:]
        self.appkey = binascii.unhexlify(key)
        
        Ablock = "0100000000" + "00" + self.addr + self.FCnt + "0000" + "0001"
        self.Ablock = Ablock
    
    def getdata(self):
        """
        get_data return data(type str)
        """
        en = AES.new(self.appkey, AES.MODE_ECB)
        Ablock = self.Ablock
        print Ablock
        hex_Ablock = binascii.unhexlify(Ablock)
        enA = en.encrypt(hex_Ablock)
        hex_data = binascii.unhexlify(self.data)
        b_data = bytearray(hex_data)
        print enA.encode("hex")
        b_enA = bytearray(enA)
        s = ""
        for i in range(len(b_data)):
            s += hex(b_data[i] ^ b_enA[i])[2:]

        return s




