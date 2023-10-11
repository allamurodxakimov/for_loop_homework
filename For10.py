def main(ls1):
    """
    Returns a list where only the first letter of each name is capitalized.
    Args:
        list1: list
    Returns:
        list: return  answer
    """
    ls=[]
    for i in range(0,len(ls1)):
        ls.append(ls1[i].capitalize())
    return ls
print(main(['rustam', 'diyor', 'alisher', 'bektosh']))