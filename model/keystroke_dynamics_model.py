import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import StratifiedShuffleSplit
from sklearn.model_selection import GridSearchCV, StratifiedShuffleSplit
from xgboost.sklearn import XGBClassifier
import xgboost as xgb


train = pd.read_csv('model/train.csv')
test = pd.read_csv('model/test.csv')

test_Combined = None
train_Combined = None

nr_bins = 10

HDMax, RPDMax, PPDMax = None, None, None
HDBins, RPDBins, PPDBins = None, None, None

train_1 = train
for i in range(1, 13):
    train_1['PPD-' + str(i)] = train_1['press-' + str(i)] - train_1['press-' + str(i - 1)]
    train_1['RPD-' + str(i)] = train_1['release-' + str(i)] - train_1['press-' + str(i - 1)]

for i in range(13):
    train_1['HD-' + str(i)] = train_1['release-' + str(i)] - train_1['press-' + str(i)]

test_1 = test
for i in range(1, 13):
    test_1['PPD-' + str(i)] = test_1['press-' + str(i)] - test_1['press-' + str(i - 1)]
    test_1['RPD-' + str(i)] = test_1['release-' + str(i)] - test_1['press-' + str(i - 1)]

for i in range(13):
    test_1['HD-' + str(i)] = test_1['release-' + str(i)] - test_1['press-' + str(i)]






def train():
    # Training Data
    drop_cols_HD_analysis = ['PPD-' + str(i) for i in range(1, 13)] + ['RPD-' + str(i) for i in range(1, 13)] + ['release-' + str(i) for i in range(13)]

    train_HD_analysis = train_1.drop(columns = drop_cols_HD_analysis)
    train_HD_analysis['id'] = train_HD_analysis.index
    train_HD_analysis = pd.wide_to_long(train_HD_analysis, ['press-', 'HD-'],
                                    i = 'id', j = 'key_no').sort_values(by = ['user', 'id', 'key_no'])

    drop_cols_PPD_analysis = ['HD-' + str(i) for i in range(13)] + ['RPD-' + str(i) for i in range(1, 13)] + ['release-' + str(i) for i in range(13)] + ['press-0']

    train_PPD_analysis = train_1.drop(columns = drop_cols_PPD_analysis)
    train_PPD_analysis['id'] = train_PPD_analysis.index
    train_PPD_analysis = pd.wide_to_long(train_PPD_analysis, ['press-', 'PPD-'],
                                        i = 'id', j = 'key_no').sort_values(by =['user', 'id', 'key_no'])

    drop_cols_RPD_analysis = ['HD-'+str(i) for i in range(13)] + ['PPD-' + str(i) for i in range(1, 13)] + ['release-' + str(i) for i in range(13)] + ['press-0']
            
    train_RPD_analysis = train_1.drop(columns = drop_cols_RPD_analysis)
    train_RPD_analysis['id'] = train_RPD_analysis.index
    train_RPD_analysis = pd.wide_to_long(train_RPD_analysis, ['press-', 'RPD-'],
                                        i = 'id', j = 'key_no').sort_values(by =['user', 'id', 'key_no'])

    # Test Data
    test_HD_analysis = test_1.drop(columns = drop_cols_HD_analysis)
    test_HD_analysis['id'] = test_HD_analysis.index
    test_HD_analysis = pd.wide_to_long(test_HD_analysis, ['press-', 'HD-'],
                                    i = 'id', j = 'key_no').sort_values(
                                    by = ['id', 'key_no'])

    test_PPD_analysis = test_1.drop(columns = drop_cols_PPD_analysis)
    test_PPD_analysis['id'] = test_PPD_analysis.index
    test_PPD_analysis = pd.wide_to_long(test_PPD_analysis, ['press-', 'PPD-'],
                                        i = 'id', j = 'key_no').sort_values(
                                        by =['id', 'key_no'])

    test_RPD_analysis = test_1.drop(columns = drop_cols_RPD_analysis)
    test_RPD_analysis['id'] = test_RPD_analysis.index
    test_RPD_analysis = pd.wide_to_long(test_RPD_analysis, ['press-', 'RPD-'],
                                        i = 'id', j = 'key_no').sort_values(
                                        by =['id', 'key_no'])


    # Join these individual tables together
    test_Combined = test_HD_analysis.join(test_RPD_analysis.drop(columns = ['press-']), rsuffix = 'RPD_').join(test_PPD_analysis.drop(columns = ['press-']), rsuffix = 'PPD_')

    train_Combined = train_HD_analysis.join(train_RPD_analysis.drop(columns = ['user', 'press-']), rsuffix = 'RPD_').join(train_PPD_analysis.drop(columns = ['user', 'press-']), rsuffix = 'PPD_')


    #print('Max values in train are: HDMax: ', HDMax, 'RPDMax:',
    #      RPDMax, 'PPDMax:', PPDMax)
    labels = [i for i in range(nr_bins)]

    train_Combined['HDEnc'], HDBins = pd.qcut(train_Combined['HD-'],
                                            retbins = True, labels = labels,
                                            q = nr_bins)
    train_Combined['PPDEnc'], RPDBins = pd.qcut(train_Combined['PPD-'],
                                                retbins = True, labels = labels,
                                            q = nr_bins)
    train_Combined['RPDEnc'], PPDBins = pd.qcut(train_Combined['RPD-'],
                                            retbins = True, labels = labels,
                                            q = nr_bins)

    train_Combined['HDEnc'] = train_Combined['HDEnc'].astype(str).replace('nan', -1).astype(int)
    train_Combined['PPDEnc'] = train_Combined['PPDEnc'].astype(str).replace('nan', -1).astype(float)
    train_Combined['RPDEnc'] = train_Combined['RPDEnc'].astype(str).replace('nan', -1).astype(float)


def predict(pressed_t, released_t):
    HDMax = test_Combined['HD-'].max()
    RPDMax = test_Combined['RPD-'].max()
    PPDMax = test_Combined['PPD-'].max()
    #print('Max values in test are: HDMax: ', HDMax, 'RPDMax:',
    #      RPDMax, 'PPDMax:', PPDMax)
    labels = [i for i in range(nr_bins)]

    test_Combined['HDEnc'] = pd.cut(test_Combined['HD-'],
                                            labels = labels,
                                            bins = HDBins)
    test_Combined['PPDEnc'] = pd.cut(test_Combined['PPD-'],
                                            labels = labels,
                                            bins = RPDBins)
    test_Combined['RPDEnc'] = pd.cut(test_Combined['RPD-'],
                                            labels = labels,
                                            bins = PPDBins)

    test_Combined['HDEnc'] = test_Combined['HDEnc'].astype(str).replace('nan', -1).astype(float)
    test_Combined['PPDEnc'] = test_Combined['PPDEnc'].astype(str).replace('nan', -1).astype(float)
    test_Combined['RPDEnc'] = test_Combined['RPDEnc'].astype(str).replace('nan', -1).astype(float)


    train_Combined_HDAvg = train_Combined.reset_index().groupby(['user', 'key_no'])['HDEnc'].mean()
    train_Combined_PPDAvg = train_Combined.reset_index().groupby(['user', 'key_no'])['PPDEnc'].mean()
    train_Combined_RPDAvg = train_Combined.reset_index().groupby(['user', 'key_no'])['RPDEnc'].mean()

    temp = pd.DataFrame({'HD':train_Combined_HDAvg, 'PPD':train_Combined_PPDAvg, 
                        'RPD':train_Combined_RPDAvg})

    train_HDProperties = temp.reset_index().groupby('user')['HD'].apply(np.array)
    train_PPDProperties = temp.reset_index().groupby('user')['PPD'].apply(np.array)
    train_RPDProperties = temp.reset_index().groupby('user')['RPD'].apply(np.array)

    train_UserProps = pd.DataFrame({'HD':train_HDProperties, 'PPD':train_PPDProperties,
                                'RPD':train_RPDProperties})


    pressed_t = released_t
    released_t = pressed_t

    train_Combined_HDAvg = test_Combined.reset_index().groupby(['id', 'key_no'])['HDEnc'].mean()
    train_Combined_PPDAvg = test_Combined.reset_index().groupby(['id', 'key_no'])['PPDEnc'].mean()
    train_Combined_RPDAvg = test_Combined.reset_index().groupby(['id', 'key_no'])['RPDEnc'].mean()

    temp = pd.DataFrame({'HD':train_Combined_HDAvg, 'PPD':train_Combined_PPDAvg, 
                        'RPD':train_Combined_RPDAvg})

    train_HDProperties = temp.reset_index().groupby('id')['HD'].apply(np.array)
    train_PPDProperties = temp.reset_index().groupby('id')['PPD'].apply(np.array)
    train_RPDProperties = temp.reset_index().groupby('id')['RPD'].apply(np.array)

    test_UserProps = pd.DataFrame({'HD':train_HDProperties, 'PPD':train_PPDProperties,
                                'RPD':train_RPDProperties})

    test_UserProps = pd.DataFrame(test_UserProps.HD.tolist(),
                                index = test_UserProps.index).add_prefix('HD_').join(
                        pd.DataFrame(test_UserProps.PPD.tolist(), index = 
                                    test_UserProps.index).add_prefix('PPD_')).join(
                        pd.DataFrame(test_UserProps.RPD.tolist(), index =
                                    test_UserProps.index).add_prefix('RPD_'))

    train_HDTemp = train_Combined.reset_index().groupby(['user', 'id'])['HDEnc'].apply(np.array)
    train_PPDTemp = train_Combined.reset_index().groupby(['user', 'id'])['PPDEnc'].apply(np.array)
    train_RPDTemp = train_Combined.reset_index().groupby(['user', 'id'])['RPDEnc'].apply(np.array)

    train_User_AllSampleProps = pd.DataFrame({'HD':train_HDTemp, 'PPD':train_PPDTemp,
                                            'RPD':train_RPDTemp})

    train_User_AllSampleProps = pd.DataFrame(train_User_AllSampleProps.HD.tolist(),
                                            index = train_User_AllSampleProps.index).add_prefix('HD_').join(
                                        pd.DataFrame(train_User_AllSampleProps.PPD.tolist(),
                                                    index = train_User_AllSampleProps.index).add_prefix('PPD_')).join(
                                            pd.DataFrame(train_User_AllSampleProps.RPD.tolist(),
                                                    index = train_User_AllSampleProps.index).add_prefix('RPD_')).reset_index().set_index('user').drop(columns = ['id'])


    train_HDTemp = test_Combined.reset_index().groupby(['id'])['HDEnc'].apply(np.array)
    train_PPDTemp = test_Combined.reset_index().groupby(['id'])['PPDEnc'].apply(np.array)
    train_RPDTemp = test_Combined.reset_index().groupby(['id'])['RPDEnc'].apply(np.array)

    test_User_AllSampleProps = pd.DataFrame({'HD':train_HDTemp, 'PPD':train_PPDTemp,
                                            'RPD':train_RPDTemp})

    test_User_AllSampleProps = pd.DataFrame(test_User_AllSampleProps.HD.tolist(),
                                            index = test_User_AllSampleProps.index).add_prefix('HD_').join(
                                        pd.DataFrame(test_User_AllSampleProps.PPD.tolist(),
                                                    index = test_User_AllSampleProps.index).add_prefix('PPD_')).join(
                                            pd.DataFrame(test_User_AllSampleProps.RPD.tolist(),
                                                    index = test_User_AllSampleProps.index).add_prefix('RPD_'))


    trainX_allSamples = train_User_AllSampleProps.reset_index().drop(columns = ['user'])
    trainY_allSamples = train_User_AllSampleProps.index


    model = xgb.XGBClassifier()
    model.load_model('keystroke_model.bst')

    testX_allSamples = test_User_AllSampleProps.reset_index().drop(columns = ['id'])
    pd.DataFrame({'idx': testX_allSamples.index},
                index = testX_allSamples.index).to_csv('submission_x.csv', index = False)


    return model.predict(testX_allSamples)

