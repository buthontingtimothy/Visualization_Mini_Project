# Visualization_Mini_Project

This repository is to collect data from the Hong Kong Observatory (HKO) and transform it ready to use in tableau.

There are 4 jupyter notebooks. Each one will generate one csv file.

1. Web_scraping.ipynb
2. GCS.ipynb
3. Combine.ipynb
4. Region_update.ipynb

# Notebook Explanation

## Web_scraping.ipynb

0. This notebook collect data from the link provided in https://data.gov.hk/
1. This notebook collects 15 meteorological data including "Mean HKHI", "Max HKHI", "Mean Amount of Cloud (%)", "Mean Pressure (hPa)", "Total Rainfall (mm)", "Mean Relative Humidity (%)", "Maximum Temperature (°C)", "Minimum Temperature (°C)", "Mean Temperature (°C)", "Global Solar Radiation (MJ/m&sup2;)", "Max UV Indices(15-minute average)", "Mean UV Indices(7 a.m. to 6 p.m.)", "Total Bright Sunshine (hours)", "Prevailing Wind Direction (°)" and "Mean Wind Speed (km/h)"
2. The data is from 2014 by default or from date of available to latest monthly update.
3. The data includes 52 stations in Hong Kong for these 15 meteorological data.
4. Not all stations have all 15 meteorological data, some meteorological data such as "Global Solar Radiation (MJ/m&sup2;)" appear only in one station.
5. data_final.csv is the result generated in this notebook

## GCS.ipynb

0. This notebook collects data from website of HKO "https://www.hko.gov.hk/tc/cis/stn.htm"
1. This notebook collects Latitude and Longitude for 52 stations
2. gcs.csv is the result generated in this notebook

## Combine.ipynb

0. This notebook collects data from data_final.csv and gcs.csv generated from Web_scraping.ipynb and GCS.ipynb respectively.
1. This notebook combines the data using left join from Web_scraping.ipynb as left table and GCS.ipynb as right table
2. data_gcs_combine.csv is the result generated in this notebook

## Region_update.ipynb

0. This notebook collects data from data_gcs_combine.csv generated from Combine.ipynb
1. This notebook merges the data from old station to new station and remove old station
2. data_gcs_combine_updat.csv is the result generated in this notebook
