import random
import sys
import matplotlib.pyplot as plt
import time

def partition(low,high):
	global pivotpoint,sum
	pivotitem=S[low];j=low			#取第一個數值，比較其他所有值，確定自己在第幾個list的位子
	for i in range(low+1,high+1):
		if S[i]<pivotitem:
			j+=1
			k=S[i]
			S[i]=S[j]
			S[j]=k
			sum+=1
	pivotpoint=j
	g=S[low]
	S[low]=S[pivotpoint]
	S[pivotpoint]=g	
			
def quicksort(low,high):			#從左邊第一個，不斷找出自己在整個list的位子	，並分割		
	global pivotpoint,sum
	if low<high:
		partition(low,high)
		quicksort(low,pivotpoint-1)
		quicksort(pivotpoint+1,high)
		map()
		
def map():
	plt.ion()												#使matplotlib的顯示模式轉換為互動（interactive）模式
	plt.clf()												#清除前面所畫的圖
	plt.plot(range(1,1001),S,'.')							#畫點圖
	#plt.bar(range(1,1001),S,)								#畫長條圖
	plt.pause(0.00000000000000000000000000000000000001)		#暫時暫停，否則看不到圖
	#plt.ioff()												#最後動態跑完後仍然會留下圖
	
starttime = time.process_time()
sys.setrecursionlimit(900000)		#用來設定遞迴最多能到幾層
sum=0								#計算運算次數
pivotpoint=0
S=[i for i in range(1,1001)]		#一個數值1~1000的list
S=random.sample(S, len(S))			#將list不重複地打亂順序
map()
time.sleep(2)
quicksort(0,999)					#開始快速排序法
endtime = time.process_time()

print("快速排序法共花"+str(endtime-starttime)+"秒，共執行"+str(sum)+"次運算。")




	
