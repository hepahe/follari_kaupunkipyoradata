import pandas as pd

follari_data= pd.read_csv("kaupunkipyoratilasto.csv")

follari_jan_2019 = follari_data[follari_data["month"] == "2019-01"]
follari_feb_2019 = follari_data[follari_data["month"] == "2019-02"]
follari_mar_2019 = follari_data[follari_data["month"] == "2019-03"]
follari_apr_2019 = follari_data[follari_data["month"] == "2019-04"]
follari_may_2019 = follari_data[follari_data["month"] == "2019-05"]
follari_jun_2019 = follari_data[follari_data["month"] == "2019-06"]
follari_jul_2019 = follari_data[follari_data["month"] == "2019-07"]
follari_aug_2019 = follari_data[follari_data["month"] == "2019-08"]
follari_sep_2019 = follari_data[follari_data["month"] == "2019-09"]
follari_oct_2019 = follari_data[follari_data["month"] == "2019-10"]
follari_nov_2019 = follari_data[follari_data["month"] == "2019-11"]
follari_dec_2019 = follari_data[follari_data["month"] == "2019-12"]

print(follari_dec_2019.head())