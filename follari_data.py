import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

follari_data= pd.read_csv("kaupunkipyoratilasto.csv")

all_trips_2019 = follari_data[(follari_data["month"] >= "2019-01") & (follari_data["month"] <= "2019-12")]

#removing trips which started and ended at the same stop

outbound_trips = all_trips_2019[all_trips_2019.start_place_name != all_trips_2019.end_place_name]

#end destinations by popularity, categorized by start place 
end_destinations = outbound_trips.groupby(["start_place_name","end_place_name"]).sum()
end_destinations = end_destinations.sort_values(["start_place_name","count","end_place_name"],ascending=[True,False,False])


#most popular starting and ending stations 
start_place_popularity = outbound_trips.groupby("start_place_name").sum() 
start_place_popularity = start_place_popularity.sort_values("count",ascending=False)

end_place_popularity = outbound_trips.groupby("end_place_name").sum()
end_place_popularity = end_place_popularity.sort_values("count",ascending=False)

#total trips
trips_by_month = outbound_trips.groupby("month").sum()

# graphs
#vertaa kaikkia matkoja vs. kuinka moni päättyi samalle pysäkille kuin alkoi 

trips_by_month.plot(color="#2c7f91", title="Number of Föllari-trips by month in 2019 (outbound trips)",legend=None,marker="s")
plt.ylabel("Individual bike trips")
plt.xlabel("Month")
plt.xticks([0,1,2,3,4,5,6,7,8,9,10,11],["jan","feb","march","apr","may","jun","jul","aug","sep","oct","nov","dec"])
plt.style.use("seaborn")
plt.show()
