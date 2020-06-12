import numpy as np

def udp_checksum(source_string):
    #校验和字段设为0
    sum = 0
    for bit in source_string:
        # 检查位数是否为16
        if len(bit) != 16:
            return
        #依次求和    
        sum += int(bit, 2)
        # 回卷
        sum = (sum & 0xffff)+((sum >> 16) & 0x1)
    # 取反
    sum = sum ^ 0xffff
    return sum

if __name__=='__main__':
    list=["0110011001100000",
          "0101010101010101",
          "1000111100001100"]
    for i in range(len(list)):
        print("checknum{0}：{1}".format(i+1,list[i]))
    print("checksum：{0}".format(np.binary_repr(udp_checksum(list),16)))
