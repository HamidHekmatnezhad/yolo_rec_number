import numpy as np
import matplotlib.pyplot as plt
import os

#################################  setting  #################################
# True if you want to save train images
bool_train = True 
bool_test = False

# True if you want classes.txt and directory to save images and label
bool_classes = True

# index of witch image to start
start_train = 0
start_test = 0

# -1 if you want to save all images. or set number of images
end_trian = 300 # -1 
end_test = -1

# location of mnist data
# download data from https://pjreddie.com/projects/mnist-in-csv/
loc_data_mnist_train = 'data_mnist/data/mnist_train.csv'
loc_data_mnist_test  = 'data_mnist/data/mnist_test.csv'
#################################    end    #################################

# import data 
train_file = open(loc_data_mnist_train, 'r')
train_list = train_file.readlines()
train_file.close()

test_file = open(loc_data_mnist_test, 'r')
test_list = test_file.readlines()
test_file.close()

if end_trian == -1:
    end_trian = len(train_list)
if end_test == -1:
    end_test = len(test_list)

print('number of image test = ', len(test_list))
print('number od image train= ', len(train_list))

if bool_classes:
    os.makedirs('data_mnist/train', exist_ok=True)
    os.makedirs('data_mnist/test', exist_ok=True)
    with open('data_mnist/train/classes.txt', 'w') as f:
            f.write('0\n1\n2\n3\n4\n5\n6\n7\n8\n9')
    with open('data_mnist/test/classes.txt', 'w') as f:
            f.write('0\n1\n2\n3\n4\n5\n6\n7\n8\n9')

if bool_train:
    # save images and write labels
    for i in range(start_train, end_trian):
        # read row data
        temp_d = train_list[i].split(',')
        print(str(i) + '. number: ', temp_d[0])

        # set image shape in np
        image_data = np.array(temp_d[1:]).astype('int').reshape((28,28))

        # remove ticks
        plt.xticks([])
        plt.yticks([])
        plt.grid(False)

        # save images and write labels
        plt.imshow(image_data, cmap='Greys')
        plt.savefig('data_mnist/train/' + str(i) + '_num' + str(temp_d[0]) + '.png')
        with open('data_mnist/train/' + str(i) + '_num' + str(temp_d[0]) + '.txt', 'w') as f:
            f.write(str(temp_d[0])  + ' 0.511719 0.506250 0.579688 0.770833')

if bool_test:
    # save images and write labels
    for i in range(start_test, end_test):
        # read row data
        temp_d = test_list[i].split(',')
        print(str(i) + '. number: ', temp_d[0])

        # set image shape in np
        image_data = np.array(temp_d[1:]).astype('int').reshape((28,28))

        # remove ticks
        plt.xticks([])
        plt.yticks([])
        plt.grid(False)

        # save images and write labels
        image = plt.imshow(image_data, cmap='Greys')
        plt.savefig('data_mnist/test/' + str(i) + '_num' + str(temp_d[0]) + '.png')
        with open('data_mnist/test/' + str(i) + '_num' + str(temp_d[0]) + '.txt', 'w') as f:
            f.write(str(temp_d[0])  + ' 0.511719 0.504167 0.570312 0.758333')

print('done')