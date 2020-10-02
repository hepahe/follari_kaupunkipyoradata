import pandas as pd
import matplotlib.pyplot as plt

follari_data= pd.read_csv("kaupunkipyoratilasto.csv")

all_trips_2019 = follari_data[(follari_data["month"] >= "2019-01") & (follari_data["month"] <= "2019-12")]

#removing trips which started and ended at the same stop

outbound_trips = all_trips_2019[all_trips_2019.start_place_name != all_trips_2019.end_place_name]

end_destinations = outbound_trips.groupby(["start_place_name","end_place_name"]).sum()
end_destinations = end_destinations.sort_values(["start_place_name","count","end_place_name"],ascending=[True,False,False])

start_place_popularity = outbound_trips.groupby("start_place_name").sum() 
start_place_popularity = start_place_popularity.sort_values("count",ascending=False)

end_place_popularity = outbound_trips.groupby("end_place_name").sum()
end_place_popularity = end_place_popularity.sort_values("count",ascending=False)

print(start_place_popularity.head())
print(end_place_popularity.head())

# graphs
start_place_popularity.plot(kind="bar")
plt.show()
