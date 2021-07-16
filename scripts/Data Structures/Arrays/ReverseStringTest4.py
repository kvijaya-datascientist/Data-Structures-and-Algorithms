"""
class ReverseString:

    def reverse(self,str):
        temp_str = []
        for i in range(len(str)-1 , -1 , -1):
            temp_str.append(str[i])
        return ''.join(temp_str)

if __name__ == "__main__":
    ins1 = ReverseString()
    input = input("Enter the statement -->  ")
    reverse_str = ins1.reverse(input)
    print(reverse_str)  """

"""from py.builtin import reversed
name = "hello"
a = reversed(name)
print(''.join(a))  """
