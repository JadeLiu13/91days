###
K取余作为相加的位数，K取整作为进一位的相加结果
###
class Solution:
    def addToArrayForm(self, A: list[int], K: int) -> list[int]:
        n = len(A)
        ans = []

        for i in range(n-1, -1, -1):
            total = A[i] + K % 10

            K //= 10
            
            if total >= 10:
                #当前位相加结果大于 10 时，进位 1 加入下一位计算
                K += 1

            ans.append(total % 10)
            
        # 这里考虑数组 A 的长度小于整数 K 位数个数的情况
        while K > 0:
            ans.append(K % 10)
            K //= 10
        # 因为添加进来是由低位往高位，输出时进行逆序输出
        return ans[::-1]
ans = Solution().addToArrayForm([1,2,0,0],44)
print(ans)
