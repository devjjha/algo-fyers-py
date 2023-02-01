import threading

from flask import Flask, request

import socketDataSubscription
import symbolDataProducer

# app_id = "PWX6BM1OI5-100:"
# access_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJhcGkuZnllcnMuaW4iLCJpYXQiOjE2NzUxNTUxMjUsImV4cCI6MTY3NTIxMTQwNSwibmJmIjoxNjc1MTU1MTI1LCJhdWQiOlsieDowIiwieDoxIiwieDoyIiwiZDoxIiwiZDoyIiwieDoxIiwieDowIl0sInN1YiI6ImFjY2Vzc190b2tlbiIsImF0X2hhc2giOiJnQUFBQUFCajJOYTE0ckJuQzhHWUlYT0M2ZHBuYnd1RHM3UE9TbzM3OGdod2RHSktTYkg0c05Oem9mdldiRXJidWhYanNBcXkyMjh2Y3FJRVZjbnEtcTl1T3hFM2hMamtqdUdGWGIyYjVQYy03UjR3bEtrVUNocz0iLCJkaXNwbGF5X25hbWUiOiJKSVRFU0hLVU1BUiBNQU5PSktVTUFSIEpIIiwib21zIjpudWxsLCJmeV9pZCI6IlhKMDMzOTIiLCJhcHBUeXBlIjoxMDAsInBvYV9mbGFnIjoiTiJ9.C_ETAnuXtWrRvz74vnT4bzDnNuzO7opfiaskn8c25e8"

ack_tkn = ""
run_background = False
symbols = []

app = Flask(__name__)

exit_event = threading.Event()


def socketSymbolDataResponse(msg):
    print("Inside socketSymbolDataResponse")
    symbolDataProducer.sendSymbolData(msg)


def socketOrderUpdateDataResponse(msg):
    print("Inside socketOrderUpdateDataResponse")
    symbolDataProducer.sendOrderUpdateData(msg)


def socketOpenResponse(msg):
    print(f'Opened Socket {msg}')


def socketErrorResponse(msg):
    print(f'Error in Socket {msg}')
    return msg


# def testT():
#     i = 0
#     while True:
#         i = +1
#         print(f'{symbols}')
#         time.sleep(1)
#         if exit_event.is_set():
#             break
#         print(f'Sleeping 1 sec for count {i}')
#
#
# #t = threading.Thread(target=testT)
# t = threading.Thread(target=testT)


@app.route("/api/subscribe", methods=['POST'])
def startThread():
    print(f'request json: {request.json}')
    symbols.extend(request.json['symbols'])
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
