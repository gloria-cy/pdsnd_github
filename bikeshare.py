import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

cities = ['chicago', 'new york city', 'washington']
months = ['1', '2', '3', '4', '5', '6', 'All']
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday','All']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "All" to apply no month filter
        (str) day - name of the day of week to filter by, or "All" to apply no day filter
    """
    print('Welcome to the Bikeshare database!! Let\'s explore Bikeshare\'s users behavior!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
          city = input('Would you like to see the data for Chicago, New York City or Washington?\n').lower()
          if city not in cities:
             print('Sorry, this is not one of the cities available in our database! Please select among Chicago, New York City or Washington.')
             continue
          else:
              break

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
          month = input('Which month of data between January to June you would like to look at?\n For example, please input "1" for January and "All" if you want to see all data.\n')
          if month not in months:
             print('Sorry, we don\'t have the data of this month in our database. Please input again.')
             continue
          else:
              break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
          day = input('Which day of the week would you like to look at? Please input "All" if you want to see all data.\n').title()
          if day not in days:
             print('Invalid input, please try again. Example: Monday')
             continue
          else:
              break

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

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    # filter by month if applicable
    if month != 'All':
        # use the index of the months list to get the corresponding int
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'All':
        # filter by day of week to create the new dataframe
        df = df[df['day'] == day.title()]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    print('The most common month of travel is in {}.\n'.format(popular_month))

    # TO DO: display the most common day of week
    popular_day = df['day'].mode()[0]
    print('The most common day of week of travel is on {}.\n'.format(popular_day))

    # TO DO: display the most common start hour
    popular_hour = df['hour'].mode()[0]
    print('The most common hour of travel is at {}.\n'.format(popular_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('The most commonly used start station is at {}.\n'.format(popular_start_station))

    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('The most commonly used end station is at {}.\n'.format(popular_end_station))

    # TO DO: display most frequent combination of start station and end station trip
    df['combination'] = df['Start Station'] + df['End Station']
    print('The most combination of start station and end station trip is\n {}'.format((df['combination'].mode()[0])))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel = df['Trip Duration'].sum()
    print('The total travel time is {}'.format(total_travel))

    # TO DO: display mean travel time
    average_travel = df['Trip Duration'].mean()
    print('The mean travel time is {}'.format(average_travel))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)

    # TO DO: Display counts of gender
    try:
       gender_types = df['Gender'].value_counts()
       print(gender_types)
    except KeyError:
           print("Gender column is not available")

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
       earliest = min(df['Birth Year'])
       most_recent = max(df['Birth Year'])
       most_common = df['Birth Year'].mode()[0]
       print('The earliest year of birth was {}.\n'.format(earliest))
       print('The most recent year of birth was {}.\n'.format(most_recent))
       print('The most common year of birth was {}.\n'.format(most_common))
    except KeyError:
           print("Birth Year column is not available for this dataset")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

# TO DO: Script should prompt the user if they want to see 5 lines of raw data
def display_data(df):
    lower = 0
    upper = 3
    while True:
          display = input('\nWould you like to see 5 more records of raw data? Enter yes or no.\n')
          if display.lower() != 'yes':
             break
          else:
             print(df[df.columns[0:]].iloc[lower:upper])
             lower += 3
             upper += 3

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
