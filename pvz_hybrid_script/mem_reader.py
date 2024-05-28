import psutil
from psutil import Process

# TODO:change this
nameprocess = "QQ.exe"


def getpid():
    for proc in psutil.process_iter():
        if proc.name() == nameprocess:
            return proc.pid
    return -1


class MemReader:
    def __init__(self, pid, base_addr):
        self.pid = pid
        self.base_addr = base_addr
        self.process = Process(pid)
        self.__open_process()
        self.mem = self.process.memory_info()

    def __open_process(self):
        self.process = Process(self.pid)

    '''
    读取内存
    :param addr: 偏移量
    :param size: 读取的字节数
    :return: 读取的内容
    '''

    def read(self, addr, size):
        return self.mem.read(self.base_addr + addr, size)

    def __read_int(self, addr):
        return self.mem.read_int(self.base_addr + addr)

    def __read_float(self, addr):
        return self.mem.read_float(self.base_addr + addr)

    def __read_double(self, addr):
        return self.mem.read_double(self.base_addr + addr)

    def __read_string(self, addr):
        return self.mem.read_string(self.base_addr + addr)

    def __read_bytes(self, addr, size):
        return self.mem.read_bytes(self.base_addr + addr, size)

    def __read_int_array(self, addr, size):
        return self.mem.read_int_array(self.base_addr + addr, size)

    def __read_float_array(self, addr, size):
        return self.mem.read_float_array(self.base_addr + addr, size)

    def __read_double_array(self, addr, size):
        return self.mem.read_double_array(self.base_addr + addr, size)

    def __read_string_array(self, addr, size):
        return self.mem.read_string_array(self.base_addr + addr, size)

    def __read_bytes_array(self, addr, size, element_size):
        return self.mem.read_bytes_array(self.base_addr + addr, size, element_size)

    def close(self):
        self.process.kill()


if __name__ == "__main__":
    # mem_reader = MemReader(pid=23712, base_addr=0x7ff7b5e00000)
    # print(mem_reader.read(0x1000, 4))
    print(getpid())