import pandas as pd

df1 = pd.read_csv('L:/BUT/SD/Promo 2022/ltoinon/3eme_année/AZURE/iut_sd3_accidents/Data/carac.csv', sep=';')
df2 = pd.read_csv('L:/BUT/SD/Promo 2022/ltoinon/3eme_année/AZURE/iut_sd3_accidents/Data/lieux.csv', sep=';')
df3 = pd.read_csv('L:/BUT/SD/Promo 2022/ltoinon/3eme_année/AZURE/iut_sd3_accidents/Data/veh.csv', sep=';')
df4 = pd.read_csv('L:/BUT/SD/Promo 2022/ltoinon/3eme_année/AZURE/iut_sd3_accidents/Data/vict.csv', sep=';')
print("Colonnes df1:", df4.columns)

df_fusionne1 = pd.merge(df1, df2, left_index=True, right_index=True, how='outer')
df_fusionne2 = pd.merge(df3, df4, left_index=True, right_index=True, how='outer')
df_fusionne = pd.merge(df_fusionne1, df_fusionne2, left_index=True, right_index=True, how='outer')
# Exporter le dataframe fusionné dans un fichier CSV
df_fusionne.to_csv('L:/BUT/SD/Promo 2022/ltoinon/3eme_année/AZURE/iut_sd3_accidents/Data/step1/merged_data.csv', index=False)
