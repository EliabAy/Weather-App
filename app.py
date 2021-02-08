from flask import Flask, render_template, request
import requests, json

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def weather():
    if request.method == 'POST':
        location = request.form
        city = str(location['Location'])
        api_key = '98c27c057d268db468f040e11dc59192'
        url = 'http://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=' + api_key 
        response = requests.get(url)
        x = response.json()
        weather = x['main']
        description = x['weather']
        temp = str((weather['temp'] - 273) * 9/5 + 32) + ' degrees'
        des = str(description[0]['description'])
        return render_template('weather.html', city=city, temp = temp, des=des)
    else:
        return render_template('location.html')

if __name__ == '__main__':
    app.run(port=5000, debug=True)