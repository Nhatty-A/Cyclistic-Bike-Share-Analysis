#!/usr/bin/env python
# coding: utf-8

# ## Cyclistic Bike-Share Analysis
# ### How does a bike-share navigate speedy success?

# ##### This project analyzes Cyclistic bike-share data to uncover trends and differences in usage patterns between annual members and casual riders. The goal is to provide actionable insights to increase membership conversions and optimize operations.

# ### Introduction:
# ##### Cyclistic is a bike-share program that offers bikes for rental in urban areas. 

# ### Objective: 
# ##### Understand how annual members and casual riders use Cyclistic bikes differently.
# ##### Identify actionable insights to drive membership growth and improve customer experience.
# 
# #### Analyse Cyclistic bike-sharing data to identify differences in usage patterns between annual members and casual riders.

# ### Methodology 
# #### The analysis involves:
#             - Exploring and cleaning the data
#             - Calculating key metrics such as average ride length
#             - Analyzing usage patterns by day of the week and peak hours
#             - Visualizing popular stations and ride distributions
#             - Deveoping actionable recommendationstions

# In[1]:


import numpy as np
import pandas as pd

import matplotlib.pyplot as plt #vizualization
import seaborn as sns


# In[3]:


# Load the datasets
data_2 = pd.read_csv("C:\\Users\\HP\\Downloads\\Divvy_Trips_2020_Q1.csv")


# In[5]:


data_1.head()


# In[6]:


data_2.head()


# In[7]:


data_2.info()


# In[9]:


data_2.shape


# In[17]:


data_2.isnull().sum()


# In[24]:


data_2["end_station_name"]= data_2["end_station_name"].fillna("HQ QR")
data_2["end_station_id"]= data_2["end_station_id"].fillna(675)
data_2["end_lat"] =data_2["end_lat"].fillna(41.8899)
data_2["end_lng"] = data_2["end_lng"].fillna(-87.6803)
                                            
                                           


# In[25]:


data_2.isnull().sum()


# In[26]:


data_2['started_at'] = pd.to_datetime(data_2['started_at'])
data_2['ended_at'] = pd.to_datetime(data_2['ended_at'])


# In[28]:


data_2['started_at'], data_2['ended_at']


# In[29]:


data_2.head()


# In[32]:


data_2.duplicated()


# In[33]:


data_2.describe()


# In[43]:


data_2['ride_length_in_min'] = (data_2['ended_at'] - data_2['started_at']).dt.total_seconds() / 60
data_2['day_of_week'] = data_2['started_at'].dt.day_name()
data_2


# ### Tasks:
# #### 1. Analyze average ride length and usage patterns by membership type.
# #### 2. Compare usage by the day of the week for members vs. casual riders.

# In[46]:


avg_ride_length = data_2.groupby('member_casual')['ride_length_in_min'].mean()
avg_ride_length


# In[49]:


usage_by_day = data_2.groupby(['day_of_week', 'member_casual']).size().unstack()
usage_by_day


# ### Create visualizations and a report.
# 
# #### 1. Average ride length by membership type.
# #### 2. Weekly usage patterns by membership type.

# In[50]:


import seaborn as sns
import matplotlib.pyplot as plt


# In[52]:


sns.barplot(x= avg_ride_length.index, y=avg_ride_length.values)
plt.title('Average Ride Length by Customer Type')
plt.ylabel('Ride Length (min)')
plt.show()


# In[53]:


usage_by_day.plot(kind='bar', stacked=True)
plt.title('Usage by Day of the Week')
plt.ylabel('Number of Rides')
plt.show()


# ### Station Popularity
# #### Identify the most popular start and end stations for both members and casual riders.

# In[71]:


freq_start_station = data_2['start_station_name'].value_counts().head(5)
freq_start_station


# In[72]:


sns.barplot(x=freq_start_station.values, y=freq_start_station.index)
plt.title('Top 10 Start Stations')
plt.xlabel('Number of Rides')
plt.ylabel('Start Station')
plt.show()


# #### Examine peak hours for ride starts.
# #### Compare trends between members and casual riders.

# In[78]:


data_2['hour_of_day'] = data_2['started_at'].dt.hour

sns.histplot(data=data_2, x='hour_of_day', hue='member_casual', multiple='stack', bins=24)
plt.title('Ride Distribution by Hour of Day')
plt.xlabel('Hour of Day')
plt.ylabel('Number of Rides')
plt.show()


# #### Map the geographical distribution of rides using latitude and longitude data.
# #### Show the most used stations on a map.

# In[86]:


import folium
from IPython.display import display, IFrame
m = folium.Map(location=[data_2['start_lat'].mean(), data_2['start_lng'].mean()], zoom_start=12)


top_stations = data_2['start_station_name'].value_counts().head(10).index
for station in top_stations:
    station_data = data_2[data_2['start_station_name'] == station].iloc[0]
    folium.Marker(
        [station_data['start_lat'], station_data['start_lng']],
        popup=station,
        tooltip=f"Station: {station}"
    ).add_to(m)

# Save to an HTML file (optional for backup)
map_file = 'Top_Start_Stations_Map.html'
m.save(map_file)

# Display in the notebook
display(IFrame(map_file, width=700, height=500))


# ## Key Insights: 
# 
# 1. Annual members have shorter, more frequent rides, while casual riders tend to take longer, recreational rides.
# 2. Casual rider activity peaks on weekends, suggesting leisure-driven behavior.
# 3. Popular stations and peak hours highlight opportunities for targeted marketing.
# 

# ## Recommendations

# ### 1. Target Casual Riders with a Membership Campaign:
# ##### Develop a marketing campaign that highlights the cost benefits and convenience of annual memberships for leisure riders.
# ##### Focus messaging around weekend activities, such as exploring the city, visiting parks, or participating in events.
# ##### Use promotions like “First Month Free” or “Weekend Special Membership” to attract casual riders.

# ### 2. Enhance Digital Engagement
# ##### Create targeted social media campaigns featuring testimonials and stories of how annual memberships benefit regular users.
# ##### Incorporate location-based advertising to target users near popular stations or areas with high casual ridership.
