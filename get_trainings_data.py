import pandas as pd

df = pd.read_csv('Beispieldaten_convertiert.csv')

df = df[['TitlePlain','DeliveryContentsText','UserInstructions','SalesArgument']].dropna()
df = df.reset_index()

"with pd.option_context('display.max_rows', None, 'display.max_columns', None):"

print(df.head())

new_structure_df = pd.DataFrame(columns=['Prompts'])


for index, row in df.iterrows():

    string = "DescriptionLongMarketplaces für  #### " + row['TitlePlain'] + " #### Lieferumfang: " + row[
        'DeliveryContentsText'] + " #### " + row['UserInstructions'] + " #### " + row['SalesArgument']
    new_row = {'Prompts': string}

    new_structure_df.loc[len(new_structure_df)] = new_row


new_structure_df.to_csv('output.csv', index=False)

