import time
import serial
import sys

dev=serial.Serial('/dev/ttyTHS1',9600,timeout=0.5)

if __name__ =='__main__':
    while 1:
            try:
                time.sleep(0.3)
                data = dev.read(10)     #读取串口
                if dev:
                    print("数据已经读取:", data.decode("GB2312"))
                else:
                    print('等待数据发送')
            except KeyboardInterrupt:
                print('外部中断')
                sys.exit()