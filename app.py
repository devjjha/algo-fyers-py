import threading

from flask import Flask, request
import socketDataSubscription

ack_tkn = ""
symbols = []

app = Flask(__name__)

exit_event = threading.Event()


@app.route("/api/subscribe", methods=['POST'])
def startThread():
    print(f'request json: {request.json}')
    symbols.extend(request.json['symbols'])
    global ack_tkn
    ack_tkn = request.json['access_token']

    print(f'Access token: {ack_tkn}')
    print(f'Symbols: {symbols}')
    socketDataSubscription.subscribeUpdates(symbols, ack_tkn)
    socketDataSubscription.orderUpdates(ack_tkn)
    return 'Ok'


@app.route("/api/unsubscribe")
def stopThread():
    exit_event.set()
    symbols.clear()
    return 'Ok'


@app.route("/api/unsubscribe/symbols", methods=['POST'])
def removeSymbols():
    print(f'{ack_tkn}')
    socketDataSubscription.unsubscribeSymbols(request.json['symbols'], ack_tkn)
    return 'Ok'


if __name__ == '__main__':
    app.run(host="localhost", port=8888, debug=True)