import json

from confluent_kafka import Producer

p = Producer({'bootstrap.servers': 'localhost'})


def sendSymbolData(symbolsFeedData):
    # kafka_config = config["kafka"] | {
    #     "key.serializer": StringSerializer(),
    #     "value.serializer": JSONSerializer()
    # }
    for data in symbolsFeedData:
        p.produce('symbol_feed', key=data['symbol'], value=json.dumps(data),
                  callback=lambda err, msg: print(
                      f'Message delivered to topic => {msg.topic()} with key => {msg.key()} @Partition {msg.partition()}')
                  )

    p.flush()


def sendOrderUpdateData(orderUpdateData):
    p.produce('order_update_feed', value=json.dumps(orderUpdateData),
              callback=lambda err, msg: print(
                  f'Message delivered to topic => {msg.topic()} with key => {msg.key()} @Partition {msg.partition()}')
              )

    p.flush()



# orderData = {"s": "ok",
#              "d": {"orderDateTime": 1673507236, "id": "2230112358425", "exchOrdId": "1800000116334204", "side": 1,
#                    "segment": "D", "instrument": "", "productType": "INTRADAY", "status": 6, "qty": 25,
#                    "remainingQuantity": 25, "filledQty": 0, "limitPrice": 35.0, "stopPrice": 0.0, "type": 1,
#                    "discloseQty": 0, "dqQtyRem": 0, "orderValidity": "DAY", "slNo": 2, "offlineOrder": False,
#                    "message": "CONFIRMED", "orderNumStatus": "2230112358425:6", "tradedPrice": 0.0,
#                    "fyToken": "101123011240706", "symbol": "NSE:BANKNIFTY2311241700PE"}, "ws_type": 1}


# sendOrderUpdateData(orderData)