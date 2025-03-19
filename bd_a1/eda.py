
import dpre

#Percentage of individuals with Sleep Disorders
sleep_disorder_pct = dpre.impute_df['Sleep Disorder'].value_counts(normalize=True) * 100
insight_1 = f"Percentage of individuals with Sleep Disorders after Imputation: Sleep Apnea = {sleep_disorder_pct[0]:.2f}%, Insomnia = {sleep_disorder_pct[1]:.2f}%"
with open('eda-in-1.txt', 'w') as f:
    f.write(insight_1)

#Average Sleep Duration by Gender
avg_sleep_by_gender = dpre.df.groupby('Gender')['Sleep Duration'].mean()
insight_2 = f"Average Sleep Duration by Gender: Female = {avg_sleep_by_gender['Female']:.2f} hours, Male = {avg_sleep_by_gender['Male']:.2f} hours"
with open('eda-in-2.txt', 'w') as f:
    f.write(insight_2)

# Most common Occupation among those with Sleep Disorders
disorder_df = dpre.df[dpre.df['Sleep Disorder'].notna()]
top_occupation = disorder_df['Occupation'].value_counts().idxmax()
top_occupation_count = disorder_df['Occupation'].value_counts().max()
insight_3 = f"Most common Occupation among those with Sleep Disorders: {top_occupation} (Count = {top_occupation_count})"
with open('eda-in-3.txt', 'w') as f:
    f.write(insight_3)
