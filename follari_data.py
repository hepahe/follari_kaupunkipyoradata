import pandas as pd

follari_data= pd.read_csv("kaupunkipyoratilasto.csv")

print(follari_data["count"])