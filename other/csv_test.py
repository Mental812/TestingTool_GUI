import os
import numpy as np
import pandas as pd

dir_data = './data/'
f_app = os.path.join(dir_data, 'TestingItem_2.csv')
#print('Path of read in data: %s' % (f_app))
app_train = pd.read_csv(f_app)
app_train['Module']