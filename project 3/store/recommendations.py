import pandas as pd
from sklearn.neighbors import NearestNeighbors

# Dummy dataset for recommendations
data = {
    'product_id': [1, 2, 3, 4, 5],
    'features': [
        [0.1, 0.2, 0.3],
        [0.2, 0.1, 0.4],
        [0.3, 0.4, 0.2],
        [0.5, 0.6, 0.7],
        [0.4, 
