#编译语言为python
b=[0]
a=[-1,0,-3,1,5,6,-11,5]
global count,bi,bj
count=0
#三次循环方法
def MaxSum3(n,a,besti,bestj):
    sum=0
    global count
    for i in range(0,n):
        for j in range (i,n):
            thissum=0
            for k in range(i,j+1):
                thissum+=a[k]
                if(thissum>sum) :
                    sum=thissum
                    besti=i
                    bestj=j
                count+=1
    return sum,besti,bestj
#分治法
#从中间向两边寻找最大连续子数组
def findmid(a,left,right):
    global count
    count+=1
    #左右下标相等时，数组只有一个数，直接输出
    if(right==left):
        besti=left
        bestj=right
        sum=a[left]
        return sum,besti,bestj
    #参数定义
    center=int((left+right)/2)
    s1=0
    lefts=0
    s2=0
    rights=0
    cibest=0
    cjbest=0
    i=center
    j=center+1
    #从数组中间位置向左循环累加，找到从数组中间向左边数的最长连续子数组
    #更新s1的值，这一步是为了防止累加结果一直是负数，s1始终是0，不能正确更新
    if(a[i]<0):
        s1=a[i]
    while(i>=left):
        lefts+=a[i]  
        if(lefts>s1):
            s1=lefts
            cibest=i
        i-=1
    if(i==left-1)and(lefts>a[center]):
        cibest=left
    #从中间位置向数组右边累加，操作过程与前面类似
    j=center+1
    if(a[j]<0):
        s2=a[j]
    while(j<=right):
        rights+=a[j]
        if(rights>s2):
            s2=rights
            cjbest=j
        j+=1
    if(j==right+1)and(rights>a[center+1]):
        cjbest=right
    #两个结果相加，即可计算出从中间向两边寻找的最长连续子数组的值和下标
    crosssum=s1+s2
    return crosssum,cibest,cjbest
def Maxsubsum(a,left,right):
    sum=0
    global count
    #左右下标相等时，数组只有一个数，直接输出
    if(right==left):
        sum=a[left]
        return sum,left,right
    else:
        center=int((left+right)/2)
        #从中间向右边递归计算最大的连续子数组
        (rightsum,ribest,rjbest)=Maxsubsum(a,center+1,right)
        #从左边向中间递归计算最长连续子数组
        (leftsum,libest,ljbest)=Maxsubsum(a,left,center)
        #从中间向两边递归计算最长连续子数组
        (crosssum,cibest,cjbest)=findmid(a,left,right)
        count+=1
        #比较三个值，求解
        if(crosssum<rightsum):
            sum=rightsum
            return sum,ribest,rjbest
        elif(crosssum<leftsum):
            sum=leftsum
            return sum,libest,ljbest 
        else:
            sum=crosssum
            return sum,cibest,cjbest
#二次循环法求解
def MaxSum2(n,a,besti,bestj):
    sum=0
    global count
    for i in range(0,n):
        thissum=0
        for j in range(i,n):
            thissum+=a[j]
            if(thissum>sum):
                sum=thissum
                besti=i
                bestj=j
            count+=1
    return sum,besti,bestj
print("测试数组为",a)
print("三次循环法",MaxSum3(8,a,0,0))
print("运行次数为",count)
count=0
print("二次循环法",MaxSum2(8,a,0,0))
print("运行次数为",count)
count=0
print("分治法",Maxsubsum(a,0,7))
print("运行次数为",count)
