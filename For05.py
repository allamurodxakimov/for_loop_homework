def main(A,B):
    """
    Return the numbers from B to A in the form of a list.
    Args:
        A: int
        B: int
    Returns:
        list: return  answer
    """
    ls=[]
    for i in range(B,A-1,-1):
        ls.append(i)
    return ls
print(main(4,9))