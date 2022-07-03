import serial

class MyUart:
# 串口打开函数
    def open_ser(self):
        port = 'com3'  # 串口号
        baudrate = 115200  # 波特率
        try:
            global ser
            ser = serial.Serial(port,baudrate,timeout=0.5)
            if(ser.isOpen()==True):
                print("串口打开成功")
        except Exception as exc:
            print("串口打开异常",exc)
            
    # 数据发送
    def send_msg( self, x):
        try:
            if   x == 1:
                send_datas = bytes.fromhex('0001')
            elif x == 0:
                 send_datas = bytes.fromhex('0000')
            else: print('参数输入0或1')

            ser.write(send_datas)
            print("已发送数据:",send_datas)
        except Exception as exc:
            print("发送异常", exc)
            
    # 接收数据
    def read_msg(self):
        try:
            print("等待接收数据")
            while True:
                data = ser.read(ser.in_waiting).decode('gbk')
                if data != '':
                    break
            print("已接受到数据:",data)
        except Exception as exc:
            print("读取异常",exc)
            
    # 关闭串口
    def close_ser(self):
            try:
                ser.close()
                if ser.isOpen():
                    print("串口未关闭")
                else:
                    print("串口已关闭")
            except Exception as exc:
                print("串口关闭异常", exc)
                
ser = MyUart()
ser.open_ser()   # 打开串口
ser.send_msg(1)   # 写数据
#read_msg()   # 读数据
ser.close_ser()  # 关闭串口
