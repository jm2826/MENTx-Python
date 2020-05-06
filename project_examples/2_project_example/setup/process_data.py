import sys
import pandas as pd
from sqlalchemy import create_engine


def load_data(filepath):
    '''
    Returns the dataframe with file type

    Parameters:
        filepath (str):The file path to the project data.

    Returns:
        df (DataFrame):A dataframe with the project data.
        file_type (str):The type of file that contains the project data.   
    '''

    return pd.read_csv(filepath, index_col='Id')


def clean_data(df):
    '''
    Returns a clean dataframe

    Parameters:
        df (DataFrame):The dataframe with the project data.
        file_type (str):The file path to the project data.

    Returns:
        df (DataFrame):A dataframe with the project data.   
    '''

    return df


def save_data(df, database_filename):
    '''
    Returns a clean dataframe

    Parameters:
        df (DataFrame):The dataframe with the project data.
        file_type (str):The file path to the project data.

    Returns:
        df (DataFrame):A dataframe with the project data.   
    '''
    
    engine = create_engine('sqlite:///' + database_filename)
    df.to_sql("prices", engine, index=False)


def main():
    if len(sys.argv) == 3:

        house_filepath, database_filepath = sys.argv[1:]

        print('Loading data...\n    TWEETS: {}'.format(house_filepath))
        df = load_data(house_filepath)

        print('Cleaning data...')
        df = clean_data(df)
        
        print('Saving data...\n    DATABASE: {}'.format(database_filepath))
        save_data(df, database_filepath)
        
        print('Cleaned data saved to database!')
    
    else:
        print('Please provide the filepaths of the tweets'\
              'dataset as the first argument, as '\
              'well as the filepath of the database to save the cleaned data '\
              'to as the second argument. \n\nExample: python process_data.py '\
              'tweet_train.csv TweetSentiment.db')


if __name__ == '__main__':
    main()