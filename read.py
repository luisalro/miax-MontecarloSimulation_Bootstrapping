import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

def read_data_ibex_div(file_path_ibex='ibex_div_data_close.csv',
              from_date='2004'):
    names = ['date','close_ibex_div']
    ibex_div = pd.read_csv(file_path_ibex, parse_dates=True, index_col=0,names=names)
    ibex_div = ibex_div[from_date:]

    return ibex_div

