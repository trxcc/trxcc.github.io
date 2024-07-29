# -*- coding: utf-8 -*-
"""

Get some chips

"""
from xgboost import XGBRegressor
import pandas as pd

from sklearn.metrics import r2_score as R2
from sklearn.metrics import mean_squared_error as MSE
from sklearn.metrics import explained_variance_score as EVS
from sklearn.metrics import mean_absolute_error as MAE

from sklearn.model_selection import cross_val_score as CVS
from matplotlib import pyplot as plt
import optuna
from sklearn.model_selection import train_test_split as TTS
import numpy as np
#%%
plt.rc('font', family='Times New Roman', size=20)

targetName = 'k'
modelName = 'XGBoost'


#加载数据
trainPath = r'数据删除.xlsx'
dataBase = pd.read_excel(trainPath)
dataBase.dropna(inplace=True)
dataBaseCopy = dataBase.copy()

#%%======================================================
#取出特征和标签
X = dataBase.drop(['ID', targetName, 'Site', 'k', '95CILow', '95CIHigh', 'p'], axis=1)
XName = X.columns
Y = dataBase[targetName]

xTrain, xTest, yTrain, yTest = TTS(X, Y, test_size=0.3, random_state=2023)
#%%======================================================
#优化参数

def objectFun(trial):
    max_depth = trial.suggest_int('max_depth', 1, 20)
    n_estimators = trial.suggest_int('n_estimators', 10, 1000)
    learning_rate = trial.suggest_float('learning_rate', 0, 1)
    reg_alpha = trial.suggest_float('reg_alpha', 0, 50)
    reg_lambda = trial.suggest_float('reg_lambda', 0, 50)
    gamma = trial.suggest_float('gamma', 0, 50)
    random_state = trial.suggest_int('random_state', 0, 3000)
    model = XGBRegressor(max_depth=max_depth,
                         n_estimators=n_estimators,
                         learning_rate=learning_rate,
                         reg_alpha=reg_alpha,
                         reg_lambda=reg_lambda,
                         gamma=gamma,
                         random_state=random_state)
    socre = CVS(model, xTrain, yTrain, cv=5, scoring='r2').mean()
    return socre

# study = optuna.create_study(direction='maximize')
# trialNum = 100
# study.optimize(objectFun, n_trials=trialNum)
# print('Best trial:', study.best_trial.params)

# # 优化后参数
# bestParams = study.best_trial.params

#%%
#进行精度测试
bestParams = {'max_depth': 17,
 'n_estimators': 855,
 'learning_rate': 0.19549990038696874,
 'reg_alpha': 1.282646777890526,
 'reg_lambda': 5.140178768001431,
 'gamma': 0.11585691459411045,
 'random_state': 673}

model = XGBRegressor(max_depth=bestParams['max_depth'],
                     n_estimators=bestParams['n_estimators'],
                     learning_rate=bestParams['learning_rate'],
                     reg_alpha=bestParams['reg_alpha'],
                     reg_lambda=bestParams['reg_lambda'],
                     gamma=bestParams['gamma'],
                     random_state=bestParams['random_state'])

model.fit(xTrain, yTrain)
modelPre = model.predict(X)
modelMAE = MAE(Y, modelPre)
modelMSE = MSE(Y, modelPre)
modelRMSE = np.sqrt(MSE(Y, modelPre))
modelEVS = EVS(Y, modelPre)
modelR2 = R2(Y, modelPre)

print('\n{} {} 评价指标:\n'.format(modelName, targetName))
print('MAE', modelMAE)
print('MSE', modelMSE)
print('RMSE', modelRMSE)
print('EVS', modelEVS)
print('R2', modelR2)


Max = max(max(Y), max(modelPre))
Min = min(min(Y), min(modelPre))

Max = Max + abs(0.2 * Max)
Min = Min - abs(0.2 * Min)

plt.figure(figsize=(10,8), dpi=100)
plt.scatter(Y, modelPre, color='black')
plt.plot([Min,Max], [Min,Max], linestyle='dashed', color='royalblue')
plt.xlim(Min, Max)
plt.ylim(Min, Max)
plt.xlabel('Ture')
plt.ylabel('Predicted')
plt.title('{} {}'.format(modelName, targetName))
plt.savefig(r'真实-预测图\{}-{}.jpg'.format(targetName, modelName))

dataBaseCopy['Pred {}'.format(targetName)] = modelPre
dataBaseCopy.to_excel(r'训练集预测结果\{}-{}.xlsx'.format(targetName, modelName), index=False)

plt.figure(figsize=(10,8),dpi=100)
nameScore = dict(zip(XName, model.feature_importances_ / sum(model.feature_importances_)))
nameScore = dict(sorted(nameScore.items(),key = lambda x:x[1],reverse = False))
plt.barh(list(nameScore.keys()),list(nameScore.values()), color='black')
plt.title('{} Importance'.format(modelName))
plt.xlabel('Score')
plt.ylabel('Features')
print('特征重要性分数')
print(nameScore)
plt.savefig(r'特征重要性图片\{}-{}.jpg'.format(targetName, modelName))
#%%
featureScorePath = r'{}-特征重要性.xlsx'.format(targetName)
featureScoreBase = pd.read_excel(featureScorePath, index_col=0)
for I in nameScore:
    featureScoreBase.loc[modelName, I] = nameScore[I]
featureScoreBase.to_excel(featureScorePath)
#%%
indexPath = r'{}-精度指标.xlsx'.format(targetName)
indexBase = pd.read_excel(indexPath, index_col=0)
indexBase.loc[modelName, ['均方误差MSE', '平均绝对误差MAE', '均方根误差RMSE', '可解释性方差EVS', '决定系数R2']] = [modelMSE, modelMAE, modelRMSE, modelEVS, modelR2]
indexBase.to_excel(indexPath)
#%%
predPath = r'预测集.xlsx'
predBaseTOP = pd.read_excel(predPath, sheet_name='TOP')
predBaseSUB = pd.read_excel(predPath, sheet_name='SUB')

predBaseTOPCopy = predBaseTOP.copy()
predBaseSUBCopy = predBaseSUB.copy()

# predBaseTOP['Ecosystem type'] = [EcosystemType.index(I) if I in EcosystemType else 100 for I in predBaseTOP['Ecosystem type'].values]
# predBaseSUB['Ecosystem type'] = [EcosystemType.index(I) if I in EcosystemType else 100 for I in predBaseSUB['Ecosystem type'].values]


TOPPred = model.predict(predBaseTOP[XName])
SUBPred = model.predict(predBaseSUB[XName])

predBaseTOPCopy[targetName] = TOPPred
predBaseSUBCopy[targetName] = SUBPred


predBaseTOPCopy.loc[predBaseTOPCopy['Ecosystem type'] == 'Desert', targetName] = pd.NA
predBaseSUBCopy.loc[predBaseSUBCopy['Ecosystem type'] == 'Desert', targetName] = pd.NA

predBaseTOPCopy.to_excel('预测集预测结果\TOP\{}-TOP-{}预测结果.xlsx'.format(targetName, modelName))
predBaseSUBCopy.to_excel('预测集预测结果\SUB\{}-SUB-{}预测结果.xlsx'.format(targetName, modelName))






