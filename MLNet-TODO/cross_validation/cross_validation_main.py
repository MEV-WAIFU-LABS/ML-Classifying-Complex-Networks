#!/usr/bin/python
# marina von steinkirch @2014
# steinkirch at gmail

''' This program divide the sets for cross validation '''

import random
import numpy as np

INPUT_FILE = ["./all_nets.data", "./all_nets_entire.data"]
OUTPUT_FILE = ["./output_sampled/", "./output_entire_net/"]
SAMPLINGS_SETS = [300, 200, 100, 50]
PERCENTAGE = 0.9 # percentage for training and test sets



def save_result_split(final, name):
    ''' Save in a file the results of spliting'''

    with open(name , "w") as f:
        for i in range(len(final)):
            f.write(str(final[i]) + "\n")




def split_data(percentage, num_sets, input_file, output_file):
    ''' split data for training and test sets '''

    with open(input_file, "rb") as f:
        data = f.read().split('\n')

    border = int(percentage*len(data))
    for i in range(num_sets):   

        random.shuffle(data)

        train_data = data[:border][:]
        test_data = data[border:][:]

        OUTPUT_FILE_TRAIN = output_file + "train_" + str(i) + '_.data' 
        OUTPUT_FILE_TEST = output_file + "test_" + str(i) + '_.data' 

        save_result_split(train_data, OUTPUT_FILE_TRAIN)
        save_result_split(test_data, OUTPUT_FILE_TEST)




def main():
    ''' Load and split data'''

    for i, data in enumerate(INPUT_FILE):
        for sam in SAMPLINGS_SETS:
                
            output_file = OUTPUT_FILE[i] + str(sam) + '/'

            # split data in the # of datasets
            split_data(PERCENTAGE, sam, data, output_file)

    print 'Done!'

   
if __name__ == '__main__':
    main()
