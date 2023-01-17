import threading

from fyers_api.Websocket import ws

from main import app_id, access_token, run_background, socketOpenResponse, socketErrorResponse, \
    socketSymbolDataResponse, symbols, socketOrderUpdateDataResponse


def symbolData(subscribedSymbol):
    symbolSocket = ws.FyersSocket(access_token=app_id + access_token, run_background=run_background,
                                  log_path='../logs/')
    symbolSocket.on_open = socketOpenResponse
    symbolSocket.on_error = socketErrorResponse
    symbolSocket.websocket_data = socketSymbolDataResponse
    symbolSocket.subscribe(symbol=subscribedSymbol, data_type="symbolData")


def orderUpdateData():
    orderSocket = ws.FyersSocket(access_token=app_id + access_token, run_background=run_background,
                                 log_path='../logs/')
    orderSocket.on_open = socketOpenResponse
    orderSocket.on_error = socketErrorResponse
    orderSocket.websocket_data = socketOrderUpdateDataResponse
    orderSocket.subscribe(data_type="orderUpdate")


def subscribeUpdates(subscribedSymbol):
    threading.Thread(target=symbolData, args=(subscribedSymbol,)).start()
    threading.Thread(target=orderUpdateData, args=()).start()


while True:
    subscribeUpdates(symbols)
