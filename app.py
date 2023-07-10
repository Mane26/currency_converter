from flask import Flask, render_template, request
import requests

app = Flask(__name__)


@app.route('/', methods = ['GET', 'POST'])
def index():
    response = requests.get(url='https://api.exchangerate-api.com/v4/latest/USD').json()
    currencies = response.get('rates')

    context = {
        'currencies': currencies,
    }

    if request.method == 'POST':
        try:
            from_amount = float(request.form['from_amount'])
            from_curr = request.form['from_curr']
            to_curr = request.form['to_curr']
        except:
            context['error'] = 'Введите сумму для обмена'
            return render_template('index.html', context=context)
        
        converted_amount = round((currencies[to_curr] / currencies[from_curr]) * from_amount, 2)

        context['from_amount'] = from_amount
        context['from_curr'] = from_curr
        context['to_curr'] = to_curr
        context['converted_amount'] = 'Получаете: ' + str(converted_amount) + ' ' + to_curr

    return render_template('index.html', context=context)


if __name__ == '__main__':
    app.run(debug=True)