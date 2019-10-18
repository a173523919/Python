#编译语言为python
a=[12,2,1,7,5,8,1,12,9]
b=[12,2,1,7,5,8,1,12,9]
def jieshu(a,k):
    c=[]
    #申请0到k，k+1个空间
    for i in range(0,k+1):
        c.append(0)
    #将a数组各个数的出现次数记录在c
    for i in range(0,len(a)):
        c[a[i]]=1+c[a[i]]
    #修改c数组，为该数在有序序列中的结束位置
    for i in range(1,len(c)):
        c[i]=c[i-1]+c[i]
    #print(c)
    #调整 
    for i in range(0,len(c)):
        c[i]=c[i]-1
    j=len(a)-1
    #初始化一个新序列b
    b=[]
    for i in range(0,len(a)):
        b.append(0)
    for i in range(0,len(b)):
        b[i]=0
    while(j>=0):
        u=a[j]
        d=c[u]
        b[d]=u
        #print("u=",u,"d=",d)
        c[u]=d-1
        j-=1
    print("b=",b)
    return b

def kaishi(a,k):
    c=[]
    #申请0到k，k+1个空间
    for i in range(0,k+1):
        c.append(0)
    #将a数组各个数的出现次数记录在c
    for i in range(0,len(a)):
        c[a[i]]=1+c[a[i]]
    #print("c1=",c)
    #修改c数组的数值，为该数在有序序列中的开始位置
    s=0
    t=0
    #先设置好c[0]和c[1]的值
    if(c[0]==0):
        t=c[1]
        c[1]=1
    else:        
        t=c[1]
        c[1]=1+c[0]
        c[0]=1
    #修改数组c，循环确定各个数字的位置
    for i in range(2,len(c)):
        s=c[i]
        c[i]=c[i-1]+t
        t=s
    #print("c2=",c)
    #调整C为数组表示法
    for i in range(0,len(c)):
        c[i]=c[i]-1
    #初始化一个新序列b
    b=[]
    for i in range(0,len(a)):
        b.append(0)
    for i in range(0,len(b)):
        b[i]=0
    #循环输出
    j=0
    while(j<len(a)):
        u=a[j]
        d=c[u]
        b[d]=u
        #print("u=",u,"d=",d)
        c[u]=d+1
        j+=1
    print("b=",b)
    return b
print("测试数组",a)
jieshu(a,12)
kaishi(b,12)
