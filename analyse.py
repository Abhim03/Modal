import pandas as pd


# Read the Excel files into dataframes
pre_game_df = pd.read_excel('préjeu.xlsx')
post_game_df = pd.read_excel('postjeu.xlsx')


print(pre_game_df.head())
print(post_game_df.head())
