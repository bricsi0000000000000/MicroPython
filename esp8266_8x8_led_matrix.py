from machine import Pin

DIN = Pin(4, Pin.OUT)
CLK = Pin(2, Pin.OUT)
CS = Pin(0, Pin.OUT)

szivecske = bytes([0x0c, 0x1e, 0x3e, 0x7c, 0x7c, 0x3e, 0x1e, 0x0c])
mosolygos_fej = bytes([0x00, 0x20, 0x44, 0x40, 0x40, 0x44, 0x20, 0x00])
szomoru_fej = bytes([0x00, 0x40, 0x24, 0x20, 0x20, 0x24, 0x40, 0x00])

def writeByte(DATA):
    i = 0
    CS.value(0)
    for i in range(8, 0, -1):
        CLK.value(0)
        DIN.value(DATA&0x80)
        DATA = DATA << 1
        CLK.value(1)
        
def write(address, dat):
    CS.value(0)
    writeByte(address)
    writeByte(dat)
    CS.value(1)
    
def init():
    write(0x09,0x00)
    write(0x0a,0x03)
    write(0x0b,0x07)
    write(0x0c,0x01)
    write(0x0f,0x00)

def mosolyog():
    for i in range(1, 9):
        write(i, mosolygos_fej[i - 1])
        
def szomoru():
    for i in range(1, 9):
        write(i, szomoru_fej[i - 1])
        
def sziv():
    for i in range(1, 9):
        write(i, szivecske[i - 1])

init()

mosolyog()
