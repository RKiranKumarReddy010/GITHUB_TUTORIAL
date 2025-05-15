import requests

url = 'https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_DAILY&symbol=BTC&market=EUR&apikey=CEOM4WZT9GXAFNYF&datatype=csv'
response = requests.get(url)
if response.status_code == 200:
    with open('static/stocks.csv', 'wb') as file:
        file.write(response.content)
    print("File downloaded successfully.")
else:
    print("Failed to download file. Status code:", response.status_code)
    
if response.status_code == 200:
    with open('stocks.csv', 'wb') as file:
        file.write(response.content)
    print("File downloaded successfully.")
else:
    print("Failed to download file. Status code:", response.status_code)