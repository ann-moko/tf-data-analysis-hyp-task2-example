import pandas as pd
import numpy as np


chat_id = 371784753 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    alpha = 0.03
    return (stats.anderson_ksamp([x, y]).significance_level < alpha)
    
