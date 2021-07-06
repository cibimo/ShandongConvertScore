rule = {
    'rank':['A', 'B+', 'B', 'C+', 'C', 'D+', 'D', 'E'],
    'precent':[3, 10, 26, 50, 74, 90, 97, 100],
    'high':[100, 90, 80, 70, 60, 50, 40, 30],
    'low':[91, 81, 71, 61, 51, 41, 31, 21]
}

def convertScore(scorelist): # 格式为 [(标识, 原始分), (标识, 原始分), (标识, 原始分), (标识, 原始分), ...]
    scorelist = sorted(scorelist,key=lambda x:x[1],reverse=True) # 分数由高到低排序，很关键
    lastrank = 0
    partscorelistList = []
    for i in range(len(rule['rank'])):
        rank = int(len(scorelist) * rule['precent'][i]/100)
        partscorelist = scorelist[lastrank:rank]
        partscorelistList.append(partscorelist)
        lastrank = rank
        
    for i in range(len(partscorelistList)):
        if i != 0: # 让本区间最高分与上区间最低分相同的人挪到上一区间
            for p in partscorelistList[i]:
                if p[1] == partscorelistList[i-1][-1][1]:
                    partscorelistList[i-1].append(p)
                    partscorelistList[i] = partscorelistList[i][1:]

    convertList = []
    for i,partscorelist in enumerate(partscorelistList):
        partmax,partmin = partscorelist[0][1],partscorelist[-1][1] # 获取区间内最高分，最低分
        for p in partscorelist:
            if partmax == partmin:
                convertScore = rule['low'][i] + (0.5 * (rule['high'][i]-rule['low'][i])) # 计算
            else:
                convertScore = rule['low'][i] + ((p[1]-partmin)/(partmax-partmin) * (rule['high'][i]-rule['low'][i])) # 计算
            convertScore = int(convertScore+0.5) # 分数取整
            convertList.append((p[0],p[1],convertScore))
        
    return convertList # 返回 [(标识, 原始分, 转换分), (标识, 原始分, 转换分), (标识, 原始分, 转换分), (标识, 原始分, 转换分), ...]

  
# convertScore(scorelist)
