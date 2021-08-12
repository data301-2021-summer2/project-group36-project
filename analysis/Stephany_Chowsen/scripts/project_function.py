import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from collections import Counter

def load_and_process(url_or_path_to_csv_file):
    
    df1 = (
    pd.read_csv('Athenslistings.csv')
    .dropna()
    .reset_index(drop=True)
    .drop(columns =['id','listing_url','scrape_id','last_scraped','name',
        'description','neighborhood_overview','picture_url','host_id',
        'host_url','host_name','host_since','host_location','host_about',
        'host_response_time','host_thumbnail_url','host_picture_url','host_neighbourhood',
        'host_listings_count','host_total_listings_count','host_verifications','host_has_profile_pic',
        'host_identity_verified','neighbourhood','neighbourhood_cleansed',
        'neighbourhood_group_cleansed',
        'latitude','longitude','property_type','room_type','accommodates','bathrooms',
        'bathrooms_text','bedrooms','beds','amenities','price','minimum_nights',
        'maximum_nights','minimum_minimum_nights','maximum_minimum_nights',
        'minimum_maximum_nights','maximum_maximum_nights','minimum_nights_avg_ntm',
        'maximum_nights_avg_ntm','calendar_updated','has_availability','availability_30',
        'availability_60','availability_90','availability_365',
         'calendar_last_scraped','number_of_reviews_ltm','number_of_reviews_l30d','first_review',
        'last_review','review_scores_rating','review_scores_accuracy',
        'review_scores_cleanliness','review_scores_checkin',
        'review_scores_communication','review_scores_location','review_scores_value',
        'license','instant_bookable','calculated_host_listings_count',
        'calculated_host_listings_count_entire_homes','calculated_host_listings_count_private_rooms',
        'calculated_host_listings_count_shared_rooms','reviews_per_month'])
                        )
    
     df2 =(
    df1
    .loc[df1.number_of_reviews > 10]
    .replace({r'\%':''}, regex=True)
    .to_numeric(df1['host_acceptance_rate'])
    .to_numeric(df1['host_response_rate'])
    .reset_index(drop=True)
               )
    
    return df2
                
                

    
    