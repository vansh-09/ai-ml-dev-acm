import pandas as pd

df = pd.read_csv('Titanic-Dataset.csv')

print(df.head())
print(df.info())
print(df.describe())

survived = df['Survived'].mean()
print('Survival rate:\n', survived)

mean_age = df['Age'].mean()
print('Average age:\n', mean_age)
min_age = df['Age'].min()
print('Minimum age:\n', min_age)
max_age = df['Age'].max()
print('Maximum age:\n', max_age)

class_counts = df['Pclass'].value_counts()
top_class = class_counts.idxmax()
print('Class with most passengers:\n', top_class)

youngest = df[df['Age'] == df['Age'].min()]
print('Youngest passenger:\n', youngest['Name'].values[0])
oldest = df[df['Age'] == df['Age'].max()]
print('Oldest passenger:\n', oldest['Name'].values[0])

least_fare = df[df['Fare'] == df['Fare'].min()]
print('Passenger with least fare:\n', least_fare[['Name', 'Fare']].values[0])
most_fare = df[df['Fare'] == df['Fare'].max()]
print('Passenger with highest fare:\n', most_fare[['Name', 'Fare']].values[0])

high_fare = df[df['Fare'] >= 100]
print('Passengers who paid 100+ fare:\n', high_fare[['Name', 'Fare']])