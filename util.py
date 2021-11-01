class MyUtil:
    def left_shift(self, mas, count):
        ret = mas[:]
        for i in range(count):
            temp = ret[1:]
            temp.append(ret[0])
            ret[:] = temp[:]
        return ret

    def right_shift(self, mas, count):
        ret = mas[:]
        for i in range(count):
            tmp = ret[:-1]
            tmp.insert(0, ret[-1])
            ret[:] = tmp[:]
        return ret

    def mul_by_02(self, num):
        if num < 0x80:
            res = (num << 1)
        else:
            res = (num << 1) ^ 0x1b

        return res % 0x100

    def mul_by_03(self, num):
        return self.mul_by_02(num) ^ num

    def mul_by_09(self, num):
        return self.mul_by_02(self.mul_by_02(self.mul_by_02(num))) ^ num

    def mul_by_0b(self, num):
        return self.mul_by_02(self.mul_by_02(self.mul_by_02(num))) ^ self.mul_by_02(num) ^ num

    def mul_by_0d(self, num):
        return self.mul_by_02(self.mul_by_02(self.mul_by_02(num))) ^ self.mul_by_02(self.mul_by_02(num)) ^ num

    def mul_by_0e(self, num):
        return self.mul_by_02(self.mul_by_02(self.mul_by_02(num))) ^ self.mul_by_02(
            self.mul_by_02(num)) ^ self.mul_by_02(num)
