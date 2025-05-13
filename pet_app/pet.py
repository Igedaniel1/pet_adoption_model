from flask import Flask, request, render_template
import pickle
import numpy as np

app = Flask(__name__)
model = pickle.load(open("../pet_model.pkl", "rb"))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    try:
        data = [
            request.form['PetType'],
            request.form['Breed'],
            int(request.form['AgeMonths']),
            request.form['Color'],
            request.form['Size'],
            float(request.form['WeightKg']),
            int(request.form['Vaccinated']),
            int(request.form['HealthCondition']),
            int(request.form['TimeInShelterDays']),
            float(request.form['AdoptionFee']),
            int(request.form['PreviousOwner'])
        ]
    except ValueError: 
        return render_template('index.html', recommend_text='Invalid input! Enter valid input')
    
    input = [np.array(data)]
    prediction = model.predict(input)[0]
    result = "✅This is good for adoption!" if prediction == 1 else "🟢This is not good for adoption"

    return render_template('index.html', recommend_text=f"Recommendation: {result}")

if __name__ == '__main__':
    app.run(debug=True)


