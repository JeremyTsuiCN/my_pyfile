import csv,re


class CreateList():
    n = 0
    def __init__(self,date):
        self.date = date
        
    
    def read_stu_data(self):  #用于读取两个csv的数据，并把结果封装在两个字典里
        CreateList.n+=1     #通过n的值判断放进哪个字典中
        old_data = {}
        new_data = {}
        
        with open('./original_data/{}.csv'.format(self.date),encoding = 'utf-8',errors="ignore") as file:
            reader = csv.reader(file)
            for data in reader:
                wx_name = re.findall(r'(.*?)\nwxid',data[0])  #获取微信名
                level = data[1] #获取当前关卡
                #此处之后需要再添加一个备注功能，用于判断是否在加班，生病，
                #或备注第几关奖励已经发放情况
                try:
                    if CreateList.n == 1:
                        old_data[wx_name[0]]=level
                    else: 
                        new_data[wx_name[0]]=level
                except:
                    continue
            return old_data,new_data

        
def parse(*args):    #两个文件名作为参数传入，并解析
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


old_date = input('please input the old document'\s name: \n')
today =  input('what\'s the date today??')
my_parse = parse(old_date,today)       #调用这个函数

def moveSit(stu_list):    #学习动态情况分析，分三个类别。有进度的，无进度的，新进班的。
    with open('output.csv','w') as file:
        writer = csv.writer(file)
        writer.writerow(['学员情况说明'])
        stu_list[0].insert(0,'没有学习：')
        stu_list[1].insert(0,'勤奋学习：')
        stu_list[2].insert(0,'新增学员：')
        writer.writerow(stu_list[0])
        writer.writerow(stu_list[1])
        writer.writerow(stu_list[2])

def levelParse():
    pass
                 
             

