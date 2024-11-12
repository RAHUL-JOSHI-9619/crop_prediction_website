from flask import Flask, render_template, request, redirect, url_for
import joblib

# Initialize the Flask application
app = Flask(__name__)

# Load the pre-trained model
model = joblib.load('decision_tree_model.joblib')

# Define the home route
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Get data from form fields
        nitrogen = int(request.form['nitrogen'])
        phosphorous = int(request.form['phosphorous'])
        potassium = int(request.form['potassium'])
        temperature = float(request.form['temperature'])
        humidity = float(request.form['humidity'])
        ph = float(request.form['ph'])
        rainfall = float(request.form['rainfall'])

        # Prepare the data in the expected format
        sample_data = [[nitrogen, phosphorous, potassium, temperature, humidity, ph, rainfall]]

        # Predict using the loaded model
        prediction = model.predict(sample_data)[0]

        # Redirect to the result page with the predicted crop
        return redirect(url_for('result', crop=prediction))

    return render_template('index.html', prediction=None)

# Define the result route to display crop details
@app.route('/result')
def result():
    crop = request.args.get('crop')
    crop_details = {
        'apple': {
            'description': 'You can cultivate this crop for your given soil conditions. Apple trees require about 120-160 days to yield fruit. On average, an acre of apple trees uses around 1,200-1,500 liters of water per day during the growing season. Recommended fertilizers include nitrogen, phosphorus, and potassium (NPK) fertilizers to ensure healthy growth.'
        },
        'banana': {
            'description': 'You can cultivate this crop for your given soil conditions. Bananas take about 9-12 months to produce fruit. They require about 1,800-2,000 liters of water per day per acre. Fertilizers include high potassium content along with balanced NPK fertilizers for good fruit development.'
        },
        'blackgram': {
            'description': 'You can cultivate this crop for your given soil conditions. Blackgram (Urad) typically takes about 90-120 days to mature. Water requirement is around 400-600 liters per acre per day. Fertilizers include nitrogen and phosphorus-based fertilizers to boost growth.'
        },
        'chickpea': {
            'description': 'You can cultivate this crop for your given soil conditions. Chickpea is a leguminous crop that matures in 90-120 days. It requires around 600-800 liters of water per acre. Fertilizers recommended are nitrogen and phosphorus-based to encourage pod development.'
        },
        'coconut': {
            'description': 'You can cultivate this crop for your given soil conditions. Coconut palms take around 5-6 years to start yielding. They require approximately 1,500-2,500 liters of water per acre daily. Fertilizers like potassium and magnesium are used for better fruit production.'
        },
        'coffee': {
            'description': 'You can cultivate this crop for your given soil conditions. Coffee plants typically take 3-4 years to produce their first yield. They need about 1,500-2,000 liters of water per acre per day. Organic fertilizers, along with potassium and phosphorus, are ideal.'
        },
        'cotton': {
            'description': 'You can cultivate this crop for your given soil conditions. Cotton generally takes 180-200 days for harvesting. An acre of cotton requires around 1,200-1,500 liters of water per day during the growing season. Fertilizers include nitrogen and potassium-rich fertilizers.'
        },
        'grapes': {
            'description': 'You can cultivate this crop for your given soil conditions. Grapes take around 90-150 days to mature. An acre of grapevines requires about 1,000-1,200 liters of water daily. Fertilizers recommended include a balanced mix of NPK and micronutrients for fruit development.'
        },
        'jute': {
            'description': 'You can cultivate this crop for your given soil conditions. Jute crops typically take 120-150 days to harvest. They need about 1,500-2,000 liters of water per acre per day. Fertilizers like urea and superphosphate are commonly used.'
        },
        'kidneybeans': {
            'description': 'You can cultivate this crop for your given soil conditions. Kidney beans take about 90-120 days to mature. They require approximately 600-800 liters of water per acre per day. Fertilizers like nitrogen and phosphorus are ideal for good yield.'
        },
        'lentil': {
            'description': 'You can cultivate this crop for your given soil conditions. Lentils typically take 90-120 days to mature. They need about 300-500 liters of water per acre. Fertilizers recommended are nitrogen and phosphorus-rich ones.'
        },
        'maize': {
            'description': 'You can cultivate this crop for your given soil conditions. Maize (corn) typically takes 100-120 days to reach maturity. Water requirements range from 600-1,000 liters per acre daily. Fertilizers like nitrogen-rich ones are commonly used for higher yields.'
        },
        'mango': {
            'description': 'You can cultivate this crop for your given soil conditions. Mango trees usually take about 3-5 years to start fruiting. An acre of mango trees uses around 1,000-1,500 liters of water per day during the growing season. Fertilizers include potassium and nitrogen for better fruit quality.'
        },
        'mothbeans': {
            'description': 'You can cultivate this crop for your given soil conditions. Moth beans typically mature in 60-90 days. They require around 400-600 liters of water per acre daily. Fertilizers like urea and phosphorus are used for better yields.'
        },
        'mungbean': {
            'description': 'You can cultivate this crop for your given soil conditions. Mung beans mature in about 60-90 days. Water requirement is around 500-600 liters per acre. Fertilizers like nitrogen and phosphorus-based are recommended.'
        },
        'muskmelon': {
            'description': 'You can cultivate this crop for your given soil conditions. Muskmelon takes about 70-90 days to mature. It requires about 800-1,200 liters of water per acre daily. Fertilizers should include a balanced NPK mix along with micronutrients.'
        },
        'orange': {
            'description': 'You can cultivate this crop for your given soil conditions. Oranges take around 12-18 months to yield fruit. An acre of orange trees needs about 1,500-2,000 liters of water per day. Fertilizers like potassium and magnesium are ideal.'
        },
        'papaya': {
            'description': 'You can cultivate this crop for your given soil conditions. Papaya typically takes 6-9 months to start yielding fruit. It needs about 1,000-1,500 liters of water per acre daily. Fertilizers include a balanced NPK and organic compost.'
        },
        'pigeonpeas': {
            'description': 'You can cultivate this crop for your given soil conditions. Pigeonpeas generally take 150-180 days to harvest. They require around 600-800 liters of water per acre. Fertilizers with nitrogen and phosphorus are ideal.'
        },
        'pomegranate': {
            'description': 'You can cultivate this crop for your given soil conditions. Pomegranate is a nutritious fruit known for its juicy seeds and high antioxidant content. Pomegranate typically takes around 120-150 days to mature. An acre needs about 800-1,000 liters of water daily. Fertilizers include potassium and nitrogen.'
        },
        'watermelon': {
            'description': 'You can cultivate this crop for your given soil conditions. Watermelons take around 80-90 days to mature. They require about 1,200-1,500 liters of water per acre daily. Fertilizers should include a balanced NPK with potassium for sweeter fruits.'
        }
    }

    # Get crop-specific details
    details = crop_details.get(crop.lower(), {
        'description': 'Information not available for this crop.',
    })

    return render_template('result.html', crop=crop, details=details)

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
