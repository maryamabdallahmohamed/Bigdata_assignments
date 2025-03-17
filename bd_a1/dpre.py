import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler,OneHotEncoder
from load import load_dataset
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score,f1_score
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
df = load_dataset('Sleep_health_and_lifestyle_dataset.csv')
df['Sleep Disorder'] = df['Sleep Disorder'].map({'Sleep Apnea': 0, 'Insomnia': 1})
df.drop('Person ID', axis=1, inplace=True)
df[['Systolic', 'Diastolic']] = df['Blood Pressure'].str.split('/', expand=True).astype(int)
df.drop('Blood Pressure', axis=1, inplace=True)
df = df[df['Occupation'] != 'Manager']


clean_df = df.copy()
clean_df.dropna(inplace=True)
clean_df.reset_index(drop=True, inplace=True)
clean_df.drop(['BMI Category', 'Stress Level'], axis=1, inplace=True)



# One-hot encode categorical columns
cat_cols = ['Gender', 'Occupation']
encoder = OneHotEncoder(sparse_output=False)
encoded_cats = encoder.fit_transform(clean_df[cat_cols])
feature_names = encoder.get_feature_names_out(cat_cols)
encoded_df = pd.DataFrame(encoded_cats, columns=feature_names)


# Combine encoded columns with clean_df
encoded_df.index = clean_df.index
clean_df = clean_df.drop(columns=cat_cols, axis=1)
clean_df = pd.concat([clean_df, encoded_df], axis=1)

corr_with_sleep_disorder = clean_df.corr()['Sleep Disorder'].sort_values(ascending=False)
sns.heatmap(corr_with_sleep_disorder.to_frame(), annot=True, cmap='coolwarm', vmin=-1, vmax=1, cbar_kws={'label': 'Correlation'})
plt.title('Correlation with Sleep Disorder')
plt.savefig('vis.png', dpi=300, bbox_inches='tight')




X = clean_df.drop(columns=['Sleep Disorder'])  

y = clean_df['Sleep Disorder'].astype(int)

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
X_scaled = pd.DataFrame(X_scaled, columns=X.columns)

X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=2050)

model = RandomForestClassifier(random_state=2050)
model.fit(X_train, y_train)
predictions=model.predict(X_test)
print("Training score:", model.score(X_train, y_train))
print("Testing score:", model.score(X_test, y_test))
# Calculate metrics
y_pred=model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
f1 = f1_score(y_test,y_pred)
print("Acuuracy: ",accuracy)
print("f1_score:",f1)


print("---------------------------------")
impute_df = df.copy()
encoded_data = encoder.transform(impute_df[['Gender', 'Occupation']])
encoded_df = pd.DataFrame(encoded_data, columns=encoder.get_feature_names_out(['Gender', 'Occupation']))
impute_df = impute_df.drop(columns=['Gender', 'Occupation'])
impute_df = pd.concat([impute_df, encoded_df], axis=1)
# print(impute_df.info())
features=['Age', 'Sleep Duration', 'Quality of Sleep', 'Physical Activity Level', 'Heart Rate', 'Daily Steps','Systolic', 'Diastolic', 'Gender_Female',
       'Gender_Male', 'Occupation_Accountant', 'Occupation_Doctor',
       'Occupation_Engineer', 'Occupation_Lawyer', 'Occupation_Nurse',
       'Occupation_Sales Representative', 'Occupation_Salesperson',
       'Occupation_Scientist', 'Occupation_Software Engineer',
       'Occupation_Teacher']

features_scaled=scaler.transform(impute_df[features])

predictions = model.predict(features_scaled)


impute_df["predicted_sleep_disorder"] = impute_df["Sleep Disorder"].copy()
impute_df["predicted_sleep_disorder"].fillna(pd.Series(predictions, index=impute_df.index), inplace=True)



# Insight 1: Percentage of individuals with Sleep Disorders
sleep_disorder_pct = impute_df['Sleep Disorder'].value_counts(normalize=True) * 100
insight_1 = f"Percentage of individuals with Sleep Disorders after Imputation: Sleep Apnea = {sleep_disorder_pct[0]:.2f}%, Insomnia = {sleep_disorder_pct[1]:.2f}%"
with open('eda-in-1.txt', 'w') as f:
    f.write(insight_1)

# Insight 2: Average Sleep Duration by Gender
avg_sleep_by_gender = df.groupby('Gender')['Sleep Duration'].mean()
insight_2 = f"Average Sleep Duration by Gender: Female = {avg_sleep_by_gender['Female']:.2f} hours, Male = {avg_sleep_by_gender['Male']:.2f} hours"
with open('eda-in-2.txt', 'w') as f:
    f.write(insight_2)

# Insight 3: Most common Occupation among those with Sleep Disorders
disorder_df = df[df['Sleep Disorder'].notna()]
top_occupation = disorder_df['Occupation'].value_counts().idxmax()
top_occupation_count = disorder_df['Occupation'].value_counts().max()
insight_3 = f"Most common Occupation among those with Sleep Disorders: {top_occupation} (Count = {top_occupation_count})"
with open('eda-in-3.txt', 'w') as f:
    f.write(insight_3)


impute_df.to_csv('res_dpre.csv')