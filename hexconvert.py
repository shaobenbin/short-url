# -*- coding: utf-8 -*-

class HexConvert:

    # a = [  '0', '1', '2', '3', '4', '5', '6', '7', '8', '9','a', 'b',
    #           'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
    #           'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    #           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
    #           'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
    #           'Y', 'Z'  ]

    a = ['a', '1', '2', '3', '4', 'Q', 'u', '7', '8', '9', '0', 'b',
         'c', 'd', 'e', 'f', 'g', 'h', 'G', 'j', 'k', 'l', 'm', 'n',
         'o', 'Z', 'q', 'r', 's', 'H', '6', 'v', 'w', 'x', 'y', 'z',
         'A', 'B', 'C', 'D', 'E', 'F', 'i', 't', 'I', 'J', 'K', 'L',
         'M', 'N', 'O', 'P', '5', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
         'Y', 'p']


    @classmethod
    def convert10_64(cls, num10):
        """
        十进制转换成64进制
        :param num10:
        :return:
        """

        rest = num10
        elements = []
        while rest:
            elements.insert(0, cls.a[(rest-int(rest/62) * 62)])
            rest = int(rest/62)

        return "".join(elements)

    @classmethod
    def convert64_10(cls, str64):
        """
        64进制转换成十进制
        :param str64:
        :return:
        """

        multiple = len(str64)-1
        result = 0
        for c in str64:
            v = cls.value_of_62(c)
            result += 62**multiple*int(v)
            multiple-=1

        return result

    @classmethod
    def value_of_62(cls, character):
        """
        给定一个字符码，返回下标
        :param character:
        :return:
        """
        return cls.a.index(character)


if __name__ == "__main__":
    num = 113131123
    _str64 = HexConvert.convert10_64(num)
    print("原始数据: ", num)
    print("64位进制: " + _str64)
    print("恢复后数据: ", HexConvert.convert64_10(_str64))
    pass

