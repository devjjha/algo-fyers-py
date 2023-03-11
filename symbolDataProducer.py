import json

from confluent_kafka import Producer

import pyServiceLogger

p = Producer({'bootstrap.servers': 'localhost'})
log = pyServiceLogger.logger


def sendSymbolData(symbolsFeedData):
    log.debug(symbolsFeedData)
    for data in symbolsFeedData:
        p.produce('symbol_feed', key=data['symbol'], value=json.dumps(data), callback=callbackFunction)

    p.flush()


def sendOrderUpdateData(orderUpdateData):
    p.produce('order_update_feed', key=None, value=orderUpdateData,
              callback=callbackFunction)

    p.flush()


def callbackFunction(err, msg):
    if err is not None:
        log.error(err)
    else:
        log.debug('Message delivered to topic => {} with key => {} @Partition {}'
                  .format(msg.topic(), msg.key(), msg.partition()))

#
# orderData = {"s": "ok",
#              "d": {"orderDateTime": 1673507236, "id": "2230112358425", "exchOrdId": "1800000116334204", "side": 1,
#                    "segment": "D", "instrument": "", "productType": "INTRADAY", "status": 6, "qty": 25,
#                    "remainingQuantity": 25, "filledQty": 0, "limitPrice": 35.0, "stopPrice": 0.0, "type": 1,
#                    "discloseQty": 0, "dqQtyRem": 0, "orderValidity": "DAY", "slNo": 2, "offlineOrder": False,
#                    "message": "CONFIRMED", "orderNumStatus": "2230112358425:6", "tradedPrice": 0.0,
#                    "fyToken": "101123011240706", "symbol": "NSE:BANKNIFTY2311241700PE"}, "ws_type": 1}
#
# var = {"s": "ok", "d": {"orderDateTime": 315532800, "id": "1210412103802", "exchOrdId": "", "side": 1, "segment": "E",
#                         "instrument": "", "productType": "INTRADAY", "status": 5, "qty": 1, "remainingQuantity": 1,
#                         "filledQty": 0, "limitPrice": 0.0, "stopPrice": 0.0, "type": 2, "discloseQty": 0, "dqQtyRem": 0,
#                         "orderValidity": "DAY", "slNo": 1, "offlineOrder": False,
#                         "message": "RMS:1210412103802:NSE,EQUITY,1624,IOC,INTRADAY,,EQ,FY0001,B,1,I,87.20000,INTRADAY_SQUARE_OFF_INTIATED_ORDERS_NOT_ALLOWED_FOR_PRODUCT_SELECTED",
#                         "orderNumStatus": "1210412103802:5", "tradedPrice": 0.0, "fyToken": "10100000001624",
#                         "symbol": "NSE:IOC-EQ"}}
#
# sendOrderUpdateData(var)
