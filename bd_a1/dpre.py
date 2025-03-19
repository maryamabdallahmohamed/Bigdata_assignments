import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler,OneHotEncoder
import load
import sys
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score,f1_score
dataset_path = sys.argv[1]
df=load.load_dataset(dataset_path)
df['Sleep Disorder'] = df['Sleep Disorder'].map({'Sleep Apnea': 0, 'Insomnia': 1})
df.drop('Person ID', axis=1, inplace=True)
df[['Systolic', 'Diastolic']] = df['Blood Pressure'].str.split('/', expand=True).astype(int)
df.drop('Blood Pressure', axis=1, inplace=True)
df = df[df['Occupation'] != 'Manager']


clean_df = df.copy()
clean_df.dropna(inplace=True)
clean_df.reset_index(drop=True,inplace=True)
clean_df.drop(['BMI Category', 'Stress Level'], axis=1, inplace=True)

print(clean_df.info())


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
impute_df.drop( 'Sleep Disorder',axis=1,inplace=True)
impute_df.to_csv('res_dpre.csv')
print(impute_df.info())