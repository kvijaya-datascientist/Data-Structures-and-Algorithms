

class ReverseString:

    def reverse(self,str):
        if(len(str) < 2 ):
         return "Hmmm..., This is not good"
        temp_str = []
        for i in range(len(str)-1 , -1 , -1):
         temp_str.append(str[i])
        return ''.join(temp_str)

if __name__ == "__main__":
    ins1 = ReverseString()
    input_str = input("Enter the statment/wor for reversing -->  ")
    rev_str  = ins1.reverse(input_str)
    print(rev_str)

# using built-in methods
#input_str = 'He is good boy'
print(input_str[-1::-1])
print(''.join(reversed(input_str)))

list1 = list(input_str)
list1.reverse()
print(''.join(list1))


