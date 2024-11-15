# put streamlit code here as needed

import streamlit as st
import altair as alt
import pandas as pd

# Read the dataset
url = "https://raw.githubusercontent.com/UIUC-iSchool-DataViz/is445_data/main/ufo-scrubbed-geocoded-time-standardized-00.csv"
df = pd.read_csv(url)

# Display the dataframe
st.write(df)

# Convert 'year' column to numeric
df['Year'] = pd.to_numeric(df['year'], errors='coerce')

# First visualization [UFO Sighting by Year]
chart = alt.Chart(df).mark_bar().encode(
    x=alt.X('year:O', title='Year'),  
    y=alt.Y('count():Q', title='Count of Sightings')  
).properties(
    title="UFO Sightings by Year",
    width=600, 
    height=400  
)

st.altair_chart(chart)

# Second visualization [UFO Sighting via Location]
chart2 = alt.Chart(df).mark_circle().encode(
    x=alt.X('longitude:Q', title='Longitude'),
    y=alt.Y('latitude:Q', title='Latitude'),
    color=alt.Color('year:O', legend=alt.Legend(title="Year")),  
    size=alt.Size('count():Q', legend=alt.Legend(title="Count of Sightings"))  
).properties(
    title="UFO Sightings by Location",
    width=600,
    height=400
)

st.altair_chart(chart2)

# Write-up for the first visualization
st.write("UFO Sightings by Year")
st.write(
    "This bar chart shows the number of UFO sightings recorded over the years. "
    "The x-axis represents the years, while the y-axis represents the total number of sightings in each year. "
    "I chose a bar chart because it effectively highlights the comparison of sightings across different years, making trends more visible."
)
st.write(
    "In terms of design, I used a simple color scheme to maintain clarity and focus on the data."
)


# df = pd.read_csv("https://raw.githubusercontent.com/UIUC-iSchool-DataViz/is445_data/main/ufo-scrubbed-geocoded-time-standardized-00.csv")
# df.head()
# df['Year'] = pd.to_numeric(df['year'], errors='coerce')

# # First visualization [UFO Sighting by Year]
# chart = alt.Chart(df).mark_bar().encode(
#     x=alt.X('year:O', title='Year'),  
#     y=alt.Y('count():Q', title='Count of Sightings')  
# ).properties(
#     title="UFO Sightings by Year",
#     width=600, 
#     height=400  
# )

# st.altair_chart(chart)

# # Second visualization [UFO Sighting via Location]
# chart2 = alt.Chart(df).mark_circle().encode(
#     x=alt.X('longitude:Q', title='Longitude'),
#     y=alt.Y('latitude:Q', title='Latitude'),
#     color=alt.Color('year:O', legend=alt.Legend(title="Year")),  
#     size=alt.Size('count():Q', legend=alt.Legend(title="Count of Sightings"))  
# ).properties(
#     title="UFO Sightings by Location",
#     width=600,
#     height=400
# )

# st.altair_chart(chart2)

# # Write-up for the first visualization
# st.write("UFO Sightings by Year")
# st.write(
#     "This bar chart shows the number of UFO sightings recorded over the years. "
#     "The x-axis represents the years, while the y-axis represents the total number of sightings in each year. "
#     "I chose a bar chart because it effectively highlights the comparison of sightings across different years, making trends more visible."
# )
# st.write(
#     "In terms of design, I used a simple color scheme to maintain clarity and focus on the data. "
#     "If I had more time, I would include an interactive slider to allow users to explore specific ranges of years and further analyze trends."
# )

# # Write-up for the second visualization
# st.write("UFO Sightings by Location")
# st.write(
#     "This scatter plot visualizes UFO sightings based on their geographical coordinates, with the x-axis representing longitude "
#     "and the y-axis representing latitude. Each point represents a sighting, and its size reflects the frequency of sightings in that location. "
#     "The color of the points corresponds to the year of the sighting."
# )
# st.write(
#     "I used circles to represent the sightings because they allow for a clear view of the geographical distribution. "
#     "The color helps distinguish between different years, and the size emphasizes areas with more sightings. "
#     "If I had more time, I would consider overlaying the plot on a map for better geographic context and adding a filter to show sightings by year or location."
# )
