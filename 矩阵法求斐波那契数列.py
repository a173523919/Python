#该程序运行语言为python
#用四个变量模拟计算矩阵，这个矩阵的值固定不变，一直累乘结果矩阵
A11=1
A12=1
A21=1
A22=0
#定义函数
def fib(n):
    if(n==1):
        print(1)
        return 1
    if(n==2):
        print(1)
        return 1
	#用四个变量模拟矩阵a，作为结果矩阵
    a11=1
    a12=1
    a21=1
    a22=0
n=n-1
#用以存储计算的值
    z=0
    x=0
    c=0
    v=0
    while(n>=2):
        z=a11*A11+a12*A21
        x=a11*A12+a12*A22
        c=a21*A11+a22*A21
        v=a21*A12+a22*A22
        a11=z
        a12=x
        a21=c
        a22=v
        n-=1
    print(a11,a12)
    print(a21,a22)
    print(a11)
return a11
