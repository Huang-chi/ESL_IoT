import datetime
i = datetime.datetime.now()

LIMIT_SZIE = 200
time_block = 5

class design_buff():
    def __init__(self):
        # self.buff_array = [[{'id':1,'power':123},{'id':2,'power':321}],[{'id':1,'power':123},{'id':1,'power':123}]]
        self.buff_array = []

    def push(self,values):
        temp = []
        result = self.check_array(values['id'])

        if result == None:
            temp.append(values)
            self.buff_array.append(temp)
        elif type(result) is int:
            self.buff_array[result].append(values)

    def pop(self):
        if self.check_buffer_size:
            temp = self.buff_array[0]
            del self.buff_array[0]
            return temp
        else:
            print("The datas don't perpare not yet.")
            return 0

    def check_buffer_size(self):
        legth = len(self.buff_array[0])
        if legth == LIMIT_SZIE:
            return True
        else:
            return False

    # def get_request_enter_container(self):


    def check_array(self,value):
        get_array_layer = len(self.buff_array)
        # print('Array size :'+str(get_array_layer))
        
        if get_array_layer == 0:
            # print("\nThe array is Null.")
            return None
        
        for index in range(get_array_layer-1):
            element_size = len(self.buff_array[index])
            count = 0
            for element in range(0,element_size):
                
                if value == self.buff_array[index][element]['id']:
                    print('Find same id, and go to next array')
                    break
                
                elif count == element_size-1:
                    return index

                count +=1
            print("****************************")

    def show_buff(self):
        # print(self.buff_array)
        return self.buff_array
    
    def lack_time_block(self):
        print(type(i.minute), i.minute)
        time = i.minute
        if (time > time_block and time < 30-time_block):
            return True
        elif (time > 30 + time_block and time < 60-time_block):
            return True
        else :
            return False

    def run_buff(self,values):
        print(self.show_buff())
        open_buff = self.lack_time_block()
        if open_buff:
            self.push(values)
        else :
            print("Now, Don't receive any data.")

values = {'id': 3, 'power': 333}
values1 = {'id': 5, 'power': 333}
a = design_buff()
a.run_buff(values)
a.run_buff(values1)
a.run_buff(values)
result_array = a.show_buff()
print(result_array)