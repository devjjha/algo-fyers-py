from fyers_api.Websocket import ws

from main import app_id, access_token, symbols


def unsubscribe(app_token, symbol):
    fyersSocket = ws.FyersSocket(access_token=app_token, run_background=True, log_path='../logs/')
    fyersSocket.unsubscribe(symbol=symbol)


if __name__ == '__main__':
    unsubscribe(app_id+access_token, symbols)