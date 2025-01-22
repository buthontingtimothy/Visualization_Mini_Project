# Weather Comfort Analysis in Hong Kong

This repository contains tools for collecting, processing, and visualizing weather data from the Hong Kong Observatory (HKO) to determine the most comfortable districts to live in across Hong Kong. The final output is an interactive Tableau dashboard.

---

## Project Objective

To analyze weather data from 52 stations across Hong Kong and determine the most comfortable living district based on weather metrics such as temperature, humidity, rainfall, and wind speed.

---

## Methodology Overview

The project uses six Jupyter notebooks and one Python module for data collection, processing, and transformation:

1. **`Web_scraping.ipynb`**: Scrapes 15 key weather metrics from HKO data.
2. **`GCS.ipynb`**: Extracts station coordinates (latitude and longitude).
3. **`Combine.ipynb`**: Merges weather data with station coordinates via a left join.
4. **`Region_update.ipynb`**: Updates old station records and removes redundancies.
5. **`District_update.ipynb`**: Maps stations to 18 districts using a station-to-district dictionary.
6. **`Parallel_weighted_average_fill_nulls.ipynb`**: Fills null values using distance-weighted averaging with a 30 km threshold.
7. **`fill_nulls_multiprocess.py`**: Supports multi-processing for efficient null value filling.

---

## Key Metrics Collected

The project analyzes 15 weather metrics, essential for understanding comfort levels:

- Mean and Max Hong Kong Heat Index (HKHI)
- Mean Amount of Cloud (%)
- Mean Pressure (hPa)
- Total Rainfall (mm)
- Mean Relative Humidity (%)
- Maximum, Minimum, and Mean Temperature (°C)
- Global Solar Radiation (MJ/m²)
- Max and Mean UV Indices
- Total Bright Sunshine (hours)
- Prevailing Wind Direction (°)
- Mean Wind Speed (km/h)

**Note**: Not all metrics are available for all stations. Metrics like Global Solar Radiation are recorded only at specific stations.

---

## Outputs and Next Steps

### Intermediate Outputs

1. **`data_final.csv`**: Raw weather data collected via scraping.
2. **`gcs.csv`**: Station coordinates.
3. **`data_gcs_combine.csv`**: Combined weather data and station coordinates.
4. **`data_gcs_combine_update.csv`**: Updated data with redundant stations removed.
5. **`data_gcs_combine_update_district.csv`**: District mapping added.
6. **`data_gcs_combine_update_district_fillna.csv`**: Final dataset with null values filled.

### Tableau Dashboards

The Tableau dashboards provide insights into weather patterns and comfort levels across Hong Kong districts. The dashboards include:

1. **Weather Overview**: Graphs of temperature, humidity, rainfall, and wind speed from 2014–2024.
2. **Weather Data Mapping**: Visualization of weather data and the calculation of comfort scores.
3. **Comfort Score by District**: Heatmaps and scatter plots of comfort scores for districts.
4. **District Ranking**: Ranking of districts by comfort score, adjustable by season and weightings for metrics.

[**View the Tableau dashboards here**](https://public.tableau.com/app/profile/hon.ting.but/viz/CA_DataAnalysis_Visulization_HKObersatory_20250118_17375299271320/Observatory_Story).

### Sample Dashboards

Below are screenshots from the Tableau dashboards:  
![Dashboard 1](![dashboard preview 1](https://github.com/user-attachments/assets/eba04d50-9c6c-40ca-b320-d65fc1abf1f9)
)  
_Overview of weather metrics (2014–2024)_  
![Dashboard 2](![dashboard preview 2](https://github.com/user-attachments/assets/5b938674-9ba9-4356-9ef9-6f92b27594ed)
)  
_Weather comfort score mapping process_

---

## Methodology Details

### Null Value Filling

- **Method**: Distance-weighted averaging with weights proportional to \( \frac{1}{\text{distance}^2} \).
- **Threshold**: Only nearby stations within 30 km are considered for filling.
- **Limitations**:
  - Metrics available at only one station (e.g., Global Solar Radiation) cannot have nulls filled.
  - For stations at the edges of Hong Kong or isolated locations, the reliability of filled values may be lower.

### Station-to-District Mapping

- Each station is mapped to one district using a dictionary (station as key, district as value).
- Mapping was double-checked against official records for accuracy.

### Performance Optimization

- Initial null value filling process took over 6 hours.
- Optimization with multi-processing reduced the runtime to approximately 15 minutes.

---

## Data Collection and Scalability

- Weather data is sourced from the [Hong Kong Observatory Open Data API](https://data.gov.hk/).
- Due to API limitations, the entire dataset must be re-downloaded monthly to avoid duplicates.

---

## Data Privacy

- All data used in this project is publicly available and free to access, ensuring no privacy concerns.

---

## Disclaimer

This project is part of a data analytics course assignment and is intended for educational purposes only. The data and analysis are based on publicly available resources from the Hong Kong Observatory and are not intended for commercial use.
