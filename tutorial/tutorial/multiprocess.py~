import multiprocessing as mp
import os

filenames=os.listdir('/data4/jiali/scrapy_imdb/tutorial/cut/')
num=len(filenames)


def job(file):
	command='scrapy crawl imdb -a file=%s' %file
	print(command)
	os.system(command)



if __name__=='__main__':
	num_loops=1;
	for loop in range(num_loops):
		i=0
		for file in filenames[loop*10:1]:
			print ('begin process %s' %file)
			p=mp.Process(target=job,args=(file,))
			p.start()
			i+=1
			print('process %d is running' % i)



