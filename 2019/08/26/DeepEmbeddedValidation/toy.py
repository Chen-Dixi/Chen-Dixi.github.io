#生成两个概率分布？

import numpy as np

from sklearn.linear_model import LinearRegression

from scipy.stats import norm
import matplotlib.pyplot as plt

def f(x):
    return np.sin(x * np.pi) / (x * np.pi)

def important_weighted(x):
    #pdf就是计算 给定x的概率密度结果，
    return norm.pdf(x, loc=2, scale=0.25) / norm.pdf(x, loc=1, scale=0.5)

def experiment(lambda_value):
    #训练集按照x_training来
    #训练集数据，源域，分布P
    x_training = np.random.randn(150,1)*0.5 + 1
    y_training = f(x_training) + np.random.randn(150, 1)*0.25

    density_ratio = important_weighted(x_training) #shape(150,1)

    
    #这个weight的权重不清楚是怎么算出来的
    weight = density_ratio ** lambda_value

    #测试集数据，目标域，分布Q
    x_test = np.random.randn(150,1)*0.25+2
    y_test = f(x_test) + np.random.randn(150,1)*0.25
    x_val = np.random.randn(150,1)*0.5+1
    y_val = f(x_val) + np.random.randn(150,1)*0.25
    # 线性回归模型
    model = LinearRegression()

    #不知道为什么这里要用weight.flatten
    model.fit(x_training, y_training, weight.flatten())


    predict_source = model.predict(x_val)

    #Source Risk
    err_source = np.mean((predict_source - y_val) ** 2)

    predict_test = model.predict(x_test)

    #Target Risk
    err_target = np.mean((predict_test - y_test) ** 2)

    #Importance-weighted cross validation
    density_ratio = important_weighted(x_val)
    wl = density_ratio * ((predict_source - y_val) ** 2)
    err_iwcv = np.mean( wl )

    #计算DEV 度量
    # 计算\eta - cov/var
    cov = np.cov(np.concatenate((wl, density_ratio),axis = 1 ), rowvar=False)[0][1] 
    #ddof=1 provides an unbiased estimator of the variance of a hypothetical infinite population.
    #ddof=0 provides a maximum likelihood estimate of the variance for normally distributed variables.
    var = np.var(density_ratio, ddof=1) 

    eta = - cov / var
    err_dev = err_iwcv + eta*np.mean(density_ratio) - eta

    return err_source, err_target, err_iwcv, err_dev


def main():
    source_means = []
    source_stds = []
    target_means = []
    target_stds = []
    iwcv_means = []
    iwcv_stds = []
    dev_means = []
    dev_stds = []

    for i in range(11):
        lambda_value = 0.1*i
        target_errors = []
        source_errors = []
        iwcv_errors = []
        dev_errors = []
        for j in range(1000):
            err_source, err_target, err_iwcv, err_dev = experiment(lambda_value)
            target_errors.append(err_target)
            source_errors.append(err_source)
            iwcv_errors.append(err_iwcv)
            dev_errors.append(err_dev)

        m,s = np.mean(source_errors) , np.std(source_errors,ddof=1)
        source_means.append(m)
        source_stds.append(s)
        m,s = np.mean(target_errors) , np.std(target_errors,ddof=1)
        target_means.append(m)
        target_stds.append(s)
        m,s = np.mean(iwcv_errors) , np.std(iwcv_errors,ddof=1)
        iwcv_means.append(m)
        target_stds.append(s)
        m,s = np.mean(dev_errors) , np.std(dev_errors,ddof=1)
        dev_means.append(m)
        dev_stds.append(s)

    # 画图 pyplot
    x_axix = np.array(list(range(11)))*0.1
    plt.title('Result Analysis')
    plt.plot(x_axix, source_means, color='green', label='Source Risk')
    plt.plot(x_axix, iwcv_means, color='red', label='IWCV')
    plt.plot(x_axix, dev_means, color='skyblue', label='DEV')
    plt.plot(x_axix, target_means, color='blue', label='Target_Risk')
    plt.xlabel('λ')
    plt.ylabel('Error Rate')
    plt.legend()
    plt.show()


if __name__ == '__main__':
    main()