# import packages
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
# show the title
st.title('Titanic app by Wentian Lv')

# read csv and show the dataframe
t = pd.read_csv('train.csv')
st.write(t)

# create a figure with three subplots, size should be (15, 5)
i = 0
fig, ax = plt.subplots(1, 3, figsize=(15, 5))

# show the box plot for ticket price with different classes
# you need to set the x labels and y labels
for c, c_info in t.groupby('Pclass'):
    ax[i].boxplot(c_info['Fare'])
    ax[i].set_xlabel(f'Pclass = {c}')
    ax[i].set_ylabel('Fare')
    i += 1

# a sample diagram is shown below
st.pyplot(fig)
