
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def normalize(df, columns):
    data = df.copy()
    result = None
    for province in data['Province/State'].unique():
        temp = data.loc[(data['Province/State'] == province), data.columns]
        for feature_name in columns:
            max_value = temp[feature_name].max()
            min_value = temp[feature_name].min()
            temp[feature_name] = (temp[feature_name] - min_value) / (max_value - min_value)
        if result is not None:
            result = pd.concat([result, temp])
        else:
            result = temp
    return result

def draw_group_chart(df, data, title = 'Global COVID-19 Data'):
    fig, axes = plt.subplots(3, 4, sharex=True, figsize=(20, 10))
    fig.suptitle(title, size= 18)
    pos_x = 0
    pos_y = 0
    sns.set_theme(style="whitegrid")
    pos_y = 0
    for province in df['Province/State'].unique():
        ax =  sns.lineplot(ax=axes[pos_x, pos_y], data=df[(df['Province/State'] == province)][data], palette='Set2') 
        handles, labels = ax.get_legend_handles_labels()
        fig.legend(handles, labels, loc='upper right')
        ax.get_legend().remove()
        ax.set_title(label=province, fontsize = 10)
        ax.set_xticks([])
        if pos_x == 2:
            pos_x = 0
        else:      
            pos_x += 1
        if pos_y == 3:
            pos_y = 0
        else:      
            pos_y += 1
            
    return

def normalize_simple(df, columns):
    result = df.copy()
    for feature_name in columns:
        max_value = result[feature_name].max()
        min_value = result[feature_name].min()
        result[feature_name] = (result[feature_name] - min_value) / (max_value - min_value)
    return result
