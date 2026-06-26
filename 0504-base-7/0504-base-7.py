class Solution:
    def convertToBase7(self, num: int) -> str:
        if num==0:
            return "0"
        neg=num<0
        num=abs(num)
        a=[]
        while num:

            a.append(str(num%7))
            num=num//7

        if neg:
            a.append("-")
        return "".join(reversed(a))
    