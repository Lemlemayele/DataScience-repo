#!/usr/bin/env python
# coding: utf-8

# In[17]:


import pandas as pd


# 
# 
# 
# <h1><center>Best Nieghborhood for technology Company in Toronto</center></h1>

# <h2><center>Lemlem Ayele</center></h2>

# <h2><center>Nov 3rd, 2019</center></h2>

# ## 1. Introduction
# 

# ### 1.1 Background

# <p>
# With over $8 billion in contributions to annual employee wages,
# Toronto's technology sector is one of the fast-growing in north America. Its great infrastructure, the ease of connection to the rest of the world,  good transit, and strong business-centric nature makes Toronto very attractive to international firms and companies.
# DexTR, a technology company based in San Francisco: engaged in design graphics processing units (GPUs), system chip for smartphone and vehicle navigation processors, is looking to open the second largest center in North America. 
# </p>

# ### 1.2 Problem.

# <p>
# After months of regress research and analysis, DexTR has been decided Toronto as the next logical location for expansion in North America. 
# Now that the decision has been made, the objective of this capstone is to analyze and select the optimal location for the DexTR office in the city of Toronto. Some of the criteria are as follow:
#     
# 1. Neighborhood score
# 2. Accessibility and public transit
# 3. Venues
# 4. Population density.
# 5. Crime
# 
# </p>
# 
# ### 1.3 Interest
# 
# <p>
#     While the DexTR has a vested interest in gaining insight for their next office location, this information will be helpful for any startup or business considering Toronto. The analysis will also have some useful insight for real estate companies or individuals.
# </p>

# ## 2.0 Data Acquisition and wrangling
# 
# ### 2.1 Data Source

# <p> The data for the city of Toronto neighborhood was obtained by scraping the Wikipedia page for the postal code of the city of Toronto, which consisted of corresponding borough and neighborhood. Additional dataset to evaluate crime and population density is obtained from the Toronto Police service: public safety data portal. 
# </p>
# 
# #### 2.2 Data Wrangling
# <p>
# The CSV file obtained by scraping the Wikipedia page was transformed into a pandas dataframe. They're some missing data, for example, rows with no assigned borough and neighborhood were dropped. While rows with postal code and borough, but no neighborhood, the neighborhood was set the same as its borough.
# We will then use a foursquare API to explore the different neighborhoods and boroughs to gain insight. Then we will do farther analysis by merging the two datasets for more in-depth insight.
# </p>
# 
