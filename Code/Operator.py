  
def NOT(posting_list):
    universal_list = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55]
    return list(set(universal_list)-set(posting_list))

def AND(posting_list_1 , posting_list_2 ):
    return list(set(posting_list_1)&set(posting_list_2))

def OR(posting_list_1 , posting_list_2 ):
    return list(set(posting_list_1+posting_list_2))

def GetPostingList(posting_list):
    postinglist = []
    for key in posting_list:
        postinglist.append(list(key.keys())[0])
    return postinglist

def GetPostfix(query):
    operator = ['NOT','OR','AND','(',')']
    pre_operator = ['NOT','OR','AND']

    stack = []
    postfix_query = []
    index = 0 

    while len(query) is not index:
        if query[index].upper() not in operator:
            postfix_query.append(query[index])
        elif query[index] is '(':
            stack.append(query[index])
        elif query[index] is ')':
            while len(stack) is not 0 and stack[len(stack) - 1] is not '(':
                postfix_query.append(stack.pop())
            stack.pop()
        else:
            try: 
                while len(stack) is not 0 and pre_operator.index(query[index].upper())<=pre_operator.index(stack[len(stack) -1].upper()):
                    postfix_query.append(stack.pop())
            except ValueError:
                pass
            stack.append(query[index])
        index += 1

    while len(stack) is not 0:
        postfix_query.append(stack.pop())

    return postfix_query


if __name__ == "__main__":
    print(GetPostingList([1,2,3,4]))
    print('o')