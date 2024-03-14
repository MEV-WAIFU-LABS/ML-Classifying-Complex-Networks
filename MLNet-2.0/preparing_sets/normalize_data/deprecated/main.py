#!/usr/bin/env python
 
 
__author__ = "Mia Stein"
__copyright__ = "Copyright 2014, The Cogent Project"
__credits__ = ["Mia Stein"]
__license__ = "GPL"
__version__ = "2.0"
__maintainer__ = "Mia Stein"
__email__ = ""


import  os
import numpy as np
from sklearn import preprocessing


# CONSTANTS 

INPUT_FOLDER     = '../../data/divide_train_test/'
OUTPUT_FOLDER  = "../../data/processed_normalized-train-test/"

OUTPUT_TRAIN_G    = OUTPUT_FOLDER + "train_" + str(PERCENTAGE) + "_gauss.data" 
OUTPUT_TEST_G     = OUTPUT_FOLDER + "test_" + str(PERCENTAGE) + "_gauss.data" 
OUTPUT_TRAIN_M    = OUTPUT_FOLDER + "train_" + str(PERCENTAGE) + "_xmin.data" 
OUTPUT_TEST_M     = OUTPUT_FOLDER + "test_" + str(PERCENTAGE) + "_xmin.data" 
OUTPUT_TRAIN_N    = OUTPUT_FOLDER + "train_" + str(PERCENTAGE) + "_none.data" 
OUTPUT_TEST_N     = OUTPUT_FOLDER + "test_" + str(PERCENTAGE) + "_none.data" 


IN_FILE_TRAIN = INPUT_FOLDER + "train_" + str(PERCENTAGE) + ".data" 
IN_FILE_TEST  = INPUT_FOLDER + "test_" + str(PERCENTAGE) + ".data" 



def save_results(X, Y, output_file):
    ''' Save in a file the results of spliting'''

    with open(output_file , "w") as f:
        for i in range(len(X)):
            for j in range(len(X[i])):
                f.write(str(X[i][j]) + ',')
            f.write(str(Y[i])  + "\n")




def load_data(datafile_name):
     ''' Load the data and separate it by feature
         and labels '''
     data = np.loadtxt(datafile_name, delimiter = ',')

     # features
     X = data[:,:-1] 

     # label
     Y = data[:,-1]
     return X, Y




def main():

    # get paths and create output folder
    input_train = IN_FILE_TRAIN
    input_test = IN_FILE_TEST
    output_folder = OUTPUT_FOLDER

    if not os.path.exists(output_folder):
        os.makedirs(output_folder) 
           
    output_train_g = OUTPUT_TRAIN_G
    output_test_g = OUTPUT_TEST_G
    output_train_m = OUTPUT_TRAIN_M
    output_test_m = OUTPUT_TEST_M
    output_train_n = OUTPUT_TRAIN_N
    output_test_n = OUTPUT_TEST_N


    # open files
    learn_data_X, learn_data_Y = load_data(input_train)
    predict_data_X, predict_data_Y = load_data(input_test)


    '''
       No normlization
    '''
    # save results
    save_results(learn_data_X, learn_data_Y, output_train_n)
    save_results(predict_data_X, predict_data_Y, output_test_n)


    '''
       Run normalizer xmin, xmax
    '''
    # run normalizer gaussian
    scaler = preprocessing.StandardScaler().fit(learn_data_X)
    learn_data_X_1 = scaler.transform(learn_data_X)
    predict_data_X_1 = scaler.transform(predict_data_X) 

    # save results
    save_results(learn_data_X_1, learn_data_Y, output_train_g)
    save_results(predict_data_X_1, predict_data_Y, output_test_g)


    '''
       Run normalizer xmin, xmax
    '''
    min_max_scaler = preprocessing.MinMaxScaler()
    learn_data_X_2 = min_max_scaler.fit_transform(learn_data_X) 
    predict_data_X_2 = min_max_scaler.transform(predict_data_X)
 
    # save results
    save_results(learn_data_X_2, learn_data_Y, output_train_m)
    save_results(predict_data_X_2, predict_data_Y, output_test_m)

    print 'Results saved at ' + output_folder

    print 'Done!'


   


if __name__ == '__main__':
    main()
