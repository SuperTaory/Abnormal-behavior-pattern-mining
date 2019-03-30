# 极值点判断函数
def JEP(S, m, v):
    if (v + m) > len(S)-1:
        if S[v] >= S[v - m]:
            flag = 1
        else:
            flag = -1
    elif v - m < 0:
        if S[v] >= S[v + m]:
            flag = 1
        else:
            flag = -1
    elif v - m >= 0 and v + m <= len(S) - 1:
        if S[v] >= S[v + m] and S[v] >= S[v - m]:
            flag = 1
        elif S[v] <= S[v + m] and S[v] <= S[v - m]:
            flag = -1
        else:
            flag = 0
    else:
        flag = 0
    return flag


def EIIR(S):
    tag = [0] * len(S)
    # 设置遍历邻域范围cyc
    cyc = 10
    # tag[0] = tag[len(S)-1] = cyc + 1
    for i in range(1, cyc + 1):
        for j in range(0, len(S)):
            if tag[j] == i - 1 and JEP(S, i, j) == 1:
                tag[j] += 1
            elif tag[j] == -(i - 1) and JEP(S, i, j) == -1:
                tag[j] -= 1
            else:
                pass
    return tag


# 保存重要极值点作为切割点
def MSR(tag, c):
    cp = []
    if tag[0] <= c:
        cp.append(0)
    for i in range(1, len(tag)):
        if tag[i] <= c:
            flag = -1
            for k in range(1, 10):
                if tag[i - k] == tag[i]:
                    flag = 1
                    break
            if flag == -1:
                cp.append(i)
    return cp

