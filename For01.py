def main(n):
    """
    Return numbers from zero to n in a list view.
    Args:
        n: int
    Returns:
        list: return  answer
    """
    ls=[]
    for i in range(n):
        ls.append(i)
    return ls
print(main(5))