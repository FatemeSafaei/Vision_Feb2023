class utils():
    
    
    
    def clct_average_from_list(a):
        '''
        input: list
        elemets: int or float
        output: average of the elemetas (float)
        '''
        sum = 0
        for i in a:
            sum += i
        ave = sum / len(a)
        return ave
            