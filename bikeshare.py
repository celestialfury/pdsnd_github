#!/usr/bin/env python
# coding: utf-8

# In[4]:


import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    
    while 1 == 1:
        city = input("Please Select one of the city; new york city, chicago or washington\n").lower()
        if city in ['chicago', 'new york city', 'washington']:
            break
        else:
            print("Sorry, This city is not in my DB. Please select from NYC, Chicago or Washington\n") 
        
    # TO DO: get user input for month (all, january, february, ... , june)
        
    while 1 == 1:
        month = input("Please select the month; january, february, march, april, may, june or none\n").lower()
        if month in ('january', 'february', 'march', 'april', 'may', 'june', 'none'):
            break
        else:
            print("Sorry, This month is not in my DB. Please select the month; january, february, march, april, may, june or none\n")    
       
 
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
        
    while 1 == 1:
        day = input("Please select a specific day or type none\n").lower()
        if day in ('monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'none'):
            break
        else:
            print("Sorry, This day is not in my DB. Please select the day from; monday, tuesday, wednesday, thursday, friday, saturday, sunday or type 'none'")
            
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    
  
    # convert the time format
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # select month and day from Start Time data
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # month filtering
    if month != 'none':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    # day filtering
    if day != 'none':
        df = df[df['day_of_week'] == day.title()]
        
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month = df['month'].mode()[0]
    print("Most Common Month: ", most_common_month)

    # TO DO: display the most common day of week
    most_common_day = df['day_of_week'].mode()[0]
    print("Most Common Day: ", most_common_day)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    most_common_start_hour = df['hour'].mode()[0]
    print("Most Common Hour: ", most_common_start_hour)

    print('\nThis took %s seconds.' % (time.time() - start_time))
    print('-'*40)
    
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_used_start_station = df['Start Station'].mode()[0]
    print("Most Used Start Station: ", most_used_start_station)

    # TO DO: display most commonly used end station
    most_used_end_station = df['End Station'].mode()[0]
    print("Most Used End Station: ", most_used_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    df['Start End Station'] = df['Start Station'] + ' and ' + df['End Station'] 
    most_used_start_end_station = df['Start End Station'].mode()[0]
    print("Most frequent start and end station trip :", most_used_start_end_station)

    print('\nThis took %s seconds.' % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = sum(df['Trip Duration'])
    print("Total Travel Time: ", total_travel_time, "seconds")

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("Mean Travel Time: ", mean_travel_time, "seconds")

    print('\nThis took %s seconds.' % (time.time() - start_time))
    print('-'*40)
    
def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    count_user_types = df['User Type'].value_counts()
    print("Counts of user types: \n",count_user_types,"\n")

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        gender_counts = df['Gender'].value_counts()
        print("Counts of gender: \n", gender_counts,"\n")
    else:
        print("There is no information in Gender\n")
        
    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        earliest_birth = int(df['Birth Year'].min())
        print('Earliest Birth: ', earliest_birth,"\n")
        most_recent_birth = int(df['Birth Year'].max())
        print('Most Recent Birth: ', most_recent_birth,"\n")
        most_common_birth = int(df['Birth Year'].mode())        
        print('Most Common Birth: ', most_common_birth,"\n")
    else:
        print("There is no Birth Year data")

    print('\nThis took %s seconds.' % (time.time() - start_time))
    print('-'*40)

def raw_data(df):
    view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n')
    start_loc = 0
    while True:
        if view_data.lower() != 'yes':
            return
        else:
            print(df.iloc[start_loc : start_loc + 5])
            start_loc += 5
            view_display = input("Do you wish to continue?: ").lower()
            break
        
                         
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()


# In[ ]:




