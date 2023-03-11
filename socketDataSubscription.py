import threading
import time

from fyers_api.Websocket import ws

import symbolDataProducer

backgroundProcess = False

exit_event = threading.Event()


def socketSymbolDataResponse(msg):
    symbolDataProducer.sendSymbolData(msg)


def socketOrderUpdateDataResponse(msg):
    symbolDataProducer.sendOrderUpdateData(msg)


def socketOpenResponse(msg):
    print(f'Opened Socket {msg}')


def socketErrorResponse(msg):
    print(f'Error in Socket {msg}')
    return msg


def symbolData(subscribedSymbol, ack_tkn):
    symbolSocket = ws.FyersSocket(access_token=ack_tkn, run_background=backgroundProcess,
                                  log_path='../logs/')
    #    symbolSocket.on_open = socketOpenResponse
    #    symbolSocket.on_error = socketErrorResponse
    symbolSocket.websocket_data = socketSymbolDataResponse
    symbolSocket.subscribe(symbol=subscribedSymbol, data_type="symbolData")


def orderUpdateData(ack_tkn):
    orderSocket = ws.FyersSocket(access_token=ack_tkn, run_background=backgroundProcess,
                                 log_path='../logs/')
    orderSocket.websocket_data = socketOrderUpdateDataResponse
    orderSocket.subscribe(data_type="orderUpdate")


def subscribeUpdates(argSymbols, token):
    symbolT = threading.Thread(target=symbolData, args=(argSymbols, token,))
    symbolT.start()


def orderUpdates(token):
    orderT = threading.Thread(target=orderUpdateData, args=(token,))
    orderT.start()


def stopRunningFeeds():
    exit_event.set()


def unsubscribeSymbols(symbols, ack_tkn):
    symbolSocket = ws.FyersSocket(access_token=ack_tkn, run_background=backgroundProcess,
                                  log_path='../logs/')
    symbolSocket.unsubscribe(symbols)


def trigger_subscription():
    while True:
        time.sleep(1)
        exit_event.set()
        if exit_event.is_set():
            break
