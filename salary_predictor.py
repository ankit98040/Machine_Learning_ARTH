import joblib
#using the saved model
model = joblib.load('salary.pk1')

exp = input("Enter the years of experience: ")

sal = model.predict([[float(exp)]])

print(sal)
