import time

#start=time.time()
# total1= total2= total3=0

# for i in range(0,100000000):
#     total1+=i
# print(total1)


# for i in range(10000001,200000000):
#     total2+=i
# print(total2)

# for i in range(20000001,300000000):
#     total3+=i
# print(total3)

# end= time.time()

# print(f"실행시간:{end-start:.6f}초")

from multiprocessing import Process

def start_get(start,end):
    total = 0
    for i in range(start, end):
        total+=i
    print(total)

if __name__== '__main__':
    
    start=time.time()

    #Process를 생성
    p0=Process(target=start_get,args=(0,100000000))
    p1=Process(target=start_get,args=(10000001,200000000))
    p2=Process(target=start_get,args=(20000001,300000000))

    #각 프로세스를 실행
    p0.start()
    p1.start()
    p2.start()

    #프로세스가 종료되길 기다린다
    p0.join()
    p1.join()
    p2.join()

    end= time.time()
    print(f"실행시간:{end-start:.6f}초")
