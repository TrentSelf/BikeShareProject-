import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new York City': 'new_york_city.csv',
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
    
    
    while True:
        city = input('What city do you want to research; Chicago, New York City, Washington? \n')
        if city.lower() in CITY_DATA:
          break
        else:
            print('Sorry that was not an option please try again')
        
    # TO DO: get user input for month (all, january, february, ... , june)
    months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
    while True:
        month = input('What month would you like to select? \n')
        if month.lower() in months:
            break
        else:
            print('Sorry that was not an option please select from one of the options')
        
        

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['all', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
    while True:
        day = input('Select what day you would like to see? \n')
        if day.lower() in days:
            break
        else:
            print('Sorry that was not an option please select from one of the options')
       
            

    print(f'You have entered City: {city.lower()} , Month: {month.lower()} , Day: {day.lower()}')
    return city.lower(), month.lower(), day.lower()


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
    #Code from my practice question #3
    
    df = pd.read_csv(CITY_DATA[city])
    

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['hour'] = df['Start Time'].dt.hour

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name


    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month)+1
    
        # filter by month to create the new dataframe
        months_2 = df['month'] == month
        df = df[months_2]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        weekdays = df['day_of_week'] == day.title()
        df = df[weekdays]

    return df

    #Code is from precourse material
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    x = 0
    while x < len(df.index):
        print('\nCalculating The Most Frequent Times of Travel...\n')
        start_time = time.time() 
    
    # Populate 5 rows of the most common data
        most_common_month = df['month'].value_counts().iloc[x:x+6]
        if most_common_month.size == 0:
            print('There is no data to display: Please select N to continue.')    
        else:
            print('The most common month from the filtered data is: ' , most_common_month)
               

    # TO DO: display the most common day of week
        most_common_day_of_week = df['day_of_week'].value_counts().iloc[x:x+6]
        if most_common_day_of_week.size == 0:
            print('There is not data to display: Please select N to continue.')
        else:    
            print('The most common day of the week from the filtered data is: ' , most_common_day_of_week)

    # TO DO: display the most common start hour
        most_common_hour = df['hour'].value_counts().iloc[x:x+6]
        if most_common_hour.size == 0:
            print('There is no data to display: Please select N to continue.')
        else:
            print('Most Common Hour:', most_common_hour)
        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)
        view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n')
        start_loc = 0
        keep_asking = True
        while (keep_asking):
            print(df.iloc[0:5])
            start_loc += 5
            view_data = input("Do you wish to continue?: ").lower()
            if view_data == "no":
                keep_asking = False
            return
            


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    x = 0
    # Populate 5 rows the most popular data
    while x < len(df.index):
        print('\nCalculating The Most Popular Stations and Trip...\n')
        start_time = time.time()

    # TO DO: display most commonly used start station
        most_common_start_station = df['Start Station'].value_counts().iloc[x:x+6]
        if most_common_start_station.size == 0:
            print('There is no more data to display: Please select N to continue.')
        else:
            print('The most common start station from the filtered data is : ' , most_common_start_station)

    # TO DO: display most commonly used end station
        most_common_end_station = df['End Station'].value_counts().iloc[x:x+6]
        if most_common_end_station.size == 0:
            print('There is no datat to display: Please select N to continue.')
        else:
            print('The most common end station from the filtered data is : ' , most_common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
        frequent_combination = df.groupby(['Start Station', 'End Station']).count()
        frequent = frequent_combination['Trip Duration'].sort_values(ascending = False).iloc[x:x+6]
        if frequent.size == 0:
            print('There is no more data to display: Please select N to contineu')
        else:
            print('Most frequent combination;' , frequent_combination)
        print("This took %s seconds." % (time.time() - start_time))
        print('-'*40)
        view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n')
        start_loc = 0
        keep_asking = True
        while (keep_asking):
            print(df.iloc[0:5])
            start_loc += 5
            view_data = input("Do you wish to continue?: ").lower()
            if view_data == "no":
                keep_asking = False
            return



def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = sum(df['Trip Duration'])
    print('total travel time:' , total_travel_time/3600, 'hour')

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('mean travel:', mean_travel_time/60, 'minutes')

    print("This took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""
    x = 0 
    # This code was copied from question #2
    while x < len(df.index):
        if 'Gender' not in df.columns:
            print('Calculating User Stats...')
            start_time = time.time()

    # TO DO: Display counts of user types
        
            user_types = df['User Type'].value_counts()
            print('User Types:', user_types)
            print('This %s seconds.' % (time.time() - start_time))
            print('-'*40)
            break
        else:
            print('Calculating User Stats...')
            start_time = time.time()
            user_types = df['User Type'].value_counts()
            print('User Types:', user_types)
            print(' ')

    # TO DO: Display counts of gender
            gender_types = df['Gender'].value_counts()
            print('The gender types are as follows:' , gender_types)
            print(' ')
    
    
                        
    # TO DO: Display earliest, most recent, and most common year of birth
    
            earliest_birth_year = df['Birth Year'].sort_values(ascending = True).unique()[x:x+6]
            if earliest_birth_year.size == 0:
                print('There is no more data to be display: Please enter N to continue')
            else:
                print('Earliest birth Year:' , earliest_birth_year)
        
            most_recent_birth_year = df['Birth Year'].sort_values(ascending = False).unique()[x:x+6]
            if most_recent_birth_year.size == 0:
                print('There is no more data to be display: Please enter N to continue')
            else:
                print('Most recent birth year:' , most_recent_birth_year)

            most_common_birth_year = df['Birth Year'].value_counts().iloc[x:x+6]
            if most_common_birth_year.size == 0:
                print('There is no more data to display: Please select N to continue')
            else:
                print('Most common birth year:' , most_common_birth_year)
            print(' ')
            print('This took %s seconds.' % (time.time() - start_time))
            print('-'*40)
            view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n')
            start_loc = 0
            keep_asking = True
            while (keep_asking):
                print(df.iloc[0:5])
                start_loc += 5
                view_data = input("Do you wish to continue?: ").lower()
                if view_data == "no":
                    keep_asking = False
                return

def main():
    while True:
       city, month, day = get_filters()
       df = load_data(city, month, day)

       time_stats(df)
       station_stats(df)
       trip_duration_stats(df)
       user_stats(df)

       restart = input('\nWould you like to restart? Enter yes or no.\n')
       if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()

"""Sources"""
#Selected code was adapted from the following
#https://notebooks.githubusercontent.com/view/ipynb?browser=chrome&color_mode=auto&commit=18e7ba5339ecc0656ef01f32b2eba03314c3a6b5&device=unknown&enc_url=68747470733a2f2f7261772e67697468756275736572636f6e74656e742e636f6d2f706f6f6a61323531322f55535f42696b6573686172652f313865376261353333396563633036353665663031663332623265626130333331346333613662352f55535f42696b6573686172652e6970796e62&logged_in=false&nwo=pooja2512%2FUS_Bikeshare&path=US_Bikeshare.ipynb&platform=android&repository_id=134308081&repository_type=Repository&version=100
## https://www.python-course.eu/python3_input.php
# https://stackoverflow.com/questions/23294658/asking-the-user-for-input-until-they-give-a-valid-response
# https://stackoverflow.com/questions/2847386/python-string-and-integer-concatenation
# https://stackoverflow.com/questions/19377969/combine-two-columns-of-text-in-dataframe-in-pandas-python