def solve(a, b):
    c, x = len(b)-len(a), a.find('*')
    if len(b) + 1 < len(a):
        return False
    if a[:x] == b[:x] and a[x+1:] == b[x+1+c:]:
        return True
    else:
        return False


print(solve("code*warrior", "codewars"))
