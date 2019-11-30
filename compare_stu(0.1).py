import csv,re


class CreateList():
    n = 0
    def __init__(self,date):
        self.date = date
        self.n = 0
        
    
    def read_stu_data(self):
        CreateList.n+=1
        old_data = {}
        new_data = {}
        with open('./original_data/{}.csv'.format(self.date),encoding = 'utf-8',errors="ignore") as file:
            reader = csv.reader(file)
            
            for data in reader:
                
                wx_name = re.findall(r'(.*?)\nwxid',data[0])
                level = data[1]
                try:
                    if CreateList.n == 1:
                        old_data[wx_name[0]]=level
                    else: 
                        new_data[wx_name[0]]=level
                except:
                    continue
            return old_data,new_data

        
def parse(*args):
    old_data = CreateList(args[0]).read_stu_data()[0]
    new_data = CreateList(args[1]).read_stu_data()[1]
    lazy_stu = []
    good_stu = []
    new_stu = []
    
    oldname_list = []
    
    for name1 in old_data:
        oldname_list.append(name1)
        
    for name2 in new_data:
        if name2 in oldname_list:
            if new_data[name2]==old_data[name2]:
                lazy_stu.append(name2)
            else:
                good_stu.append(name2)
        else:
            new_stu.append(name2)
        
    return lazy_stu,good_stu,new_stu


old_date = input('please input a date before today: ')
today =  input('what\'s the date today??')
my_parse = parse(old_date,today)       

def outPut(all_list):
    with open('output.csv','w') as file:
        writer = csv.writer(file)
        writer.writerow(['学员情况说明'])
        all_list[0].insert(0,'没有学习：')
        all_list[1].insert(0,'勤奋学习：')
        all_list[2].insert(0,'新增学员：')
        writer.writerow(all_list[0])
        writer.writerow(all_list[1])
        writer.writerow(all_list[2])

outPut(my_parse)

