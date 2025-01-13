# Weather Data Transformation for Tableau Visualization

This repository contains tools for collecting and preparing weather data from the Hong Kong Observatory (HKO) for visualization in Tableau. The workflow is divided into five Jupyter notebooks, with each generating a specific CSV file.

---

## Project Overview

### Notebooks and Outputs

1. **`Web_scraping.ipynb`**  
   Output: `data_final.csv`
2. **`GCS.ipynb`**  
   Output: `gcs.csv`
3. **`Combine.ipynb`**  
   Output: `data_gcs_combine.csv`
4. **`Region_update.ipynb`**  
   Output: `data_gcs_combine_update.csv`
5. **`District_update.ipynb`**  
   Output: `data_gcs_combine_update_district.csv`

---

## Notebook Descriptions

### 1. `Web_scraping.ipynb`

- Collects meteorological data from [data.gov.hk](https://data.gov.hk/).
- Retrieves 15 key metrics:
  - Mean and Max HKHI (Hong Kong Heat Index)
  - Cloud cover, pressure, rainfall, and humidity
  - Temperatures (mean, maximum, and minimum)
  - Solar radiation, UV indices, and sunshine hours
  - Wind direction and speed
- Covers data from 52 stations in Hong Kong, starting in 2014 or the earliest available date.
- **Notes**:
  - Some metrics (e.g., "Global Solar Radiation") are available at specific stations only.
- **Output**: `data_final.csv`

---

### 2. `GCS.ipynb`

- Extracts latitude and longitude data for the 52 stations from the [HKO website](https://www.hko.gov.hk/tc/cis/stn.htm).
- **Output**: `gcs.csv`

---

### 3. `Combine.ipynb`

- Combines data from `data_final.csv` (meteorological data) and `gcs.csv` (station coordinates).
- Uses a left join with `data_final.csv` as the primary table.
- **Output**: `data_gcs_combine.csv`

---

### 4. `Region_update.ipynb`

- Updates station data in `data_gcs_combine.csv`:
  - Merges old station data into new stations.
  - Removes redundant station entries.
- **Output**: `data_gcs_combine_update.csv`

---

### 5. `District_update.ipynb`

- Maps stations into districts based on a dictionary:
  - **Key**: Station name
  - **Value**: Corresponding district (one of 18 districts in Hong Kong)
- Adds a new column to the dataframe with the mapped district names.
- Input: `data_gcs_combine_update.csv`
- **Output**: `data_gcs_combine_update_district.csv`

---

## Purpose

This repository ensures the weather data is collected, cleaned, enriched, and transformed, making it ready for analysis and visualization in Tableau.
