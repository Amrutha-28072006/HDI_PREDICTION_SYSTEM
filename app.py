from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    life = float(request.form['life'])
    education = float(request.form['education'])
    income = float(request.form['income'])

    hdi = (life + education + income) / 3

    if hdi >= 0.80:
        category = "Very High Human Development"
    elif hdi >= 0.70:
        category = "High Human Development"
    elif hdi >= 0.55:
        category = "Medium Human Development"
    else:
        category = "Low Human Development"

    return render_template(
        'result.html',
        score=round(hdi, 3),
        category=category
    )

if __name__ == "__main__":
    app.run(debug=True)