import requests
from flask import Flask, render_template, request

app = Flask(__name__)

ALPHA_VANTAGE_API_KEY = 'YOUR_API_KEY'  # Replace with your actual Alpha Vantage API key
BASE_URL = 'https://www.alphavantage.co/query'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            from_currency = request.form['from_currency']
            to_currency = request.form['to_currency']
            amount = float(request.form['amount'])

            print(f"Converting from {from_currency} to {to_currency} with amount {amount}")

            # Fetch the exchange rate from Alpha Vantage
            response = requests.get(f'{BASE_URL}?function=CURRENCY_EXCHANGE_RATE&from_currency={from_currency}&to_currency={to_currency}&apikey={ALPHA_VANTAGE_API_KEY}')
            print("Raw API Response:", response.text)  # Debug: Print the raw response text

            if response.status_code == 200:
                data = response.json()
                print("API Response:", data)  # Debug: Print the parsed JSON response

                if 'Realtime Currency Exchange Rate' in data:
                    rate = float(data['Realtime Currency Exchange Rate']['5. Exchange Rate'])
                    converted_amount = amount * rate
                    return render_template(
                        'index.html',
                        converted_amount=converted_amount,
                        from_currency=from_currency,
                        to_currency=to_currency,
                        amount=amount
                    )
                else:
                    error = "Unexpected data format from API: No exchange rate found."
                    return render_template('index.html', error=error)
            else:
                error = f"API request failed with status code {response.status_code}."
                print("API Error:", response.text)  # Print the raw response text
                return render_template('index.html', error=error)

        except Exception as e:
            print("Error:", e)
            error = f"An error occurred during the conversion process: {e}"
            return render_template('index.html', error=error)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
