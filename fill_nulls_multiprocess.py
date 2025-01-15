import pandas as pd
import numpy as np

def process_date_subset(args):
    """
    Process a single date subset to fill nulls using weighted average.
    """
    date, daily_data, fields, distance_matrix = args
    daily_data = daily_data.copy()  # Avoid modifying the input directly

    for field in fields:
        stations_with_data = daily_data[daily_data[field].notnull()]
        stations_without_data = daily_data[daily_data[field].isnull()]

        for idx, row in stations_without_data.iterrows():
            region = row['region']

            valid_distances = distance_matrix[
                distance_matrix['station1'] == region
            ].merge(stations_with_data[['region', field]], left_on='station2', right_on='region')

            if not valid_distances.empty:
                # Calculate weighted average
                weighted_avg = np.sum(valid_distances['weight'] * valid_distances[field]) / np.sum(valid_distances['weight'])
                daily_data.loc[idx, field] = weighted_avg

    return daily_data
