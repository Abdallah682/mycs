class Solution(object):
    def busyStudent(self, startTime, endTime, queryTime):
        num_s = 0
        print(len(startTime))
        for i in range(len(startTime)):
            if endTime[i]>=queryTime :
                print("end")
                if startTime[i]<=queryTime:
                    print("st")
                    num_s +=1
        return num_s
                