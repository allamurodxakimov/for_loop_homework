def main(k,n):
    """
    Repeat the number k n times and return to the list view.
    Args:
        k: int
        n: int
    Returns:
        list: return  answer
    """
    ls=[]
    for i in range(n):
        ls.append(k)
    return ls
print(main(5,3))