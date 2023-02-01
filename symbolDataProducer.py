import json

from confluent_kafka import Producer

p = Producer({'bootstrap.servers': 'localhost'})


def sendSymbolData(symbolsFeedData):
    for data in symbolsFeedData:
        p.produce('symbol_feed', key=data['symbol'], value=json.dumps(data),
                  callback=lambda err, msg: print("Message delivered to topic => ", msg.topic(), "with key => ",
                                                  msg.key(), "@Partition",
                                                  msg.partition()))

    p.flush()


def sendOrderUpdateData(orderUpdateData):
    p.produce('order_update_feed', value=json.dumps(orderUpdateData).encode('utf-8'),
              callback=lambda err, msg: print("Message delivered to topic => ", msg.topic(), "with key => ",
                                              msg.key(), "@Partition",
                                              msg.partition()))

    p.flush()


symbolData = [
    {'symbol': 'NSE:BANKNIFTY2311942000CE', 'timestamp': 1673600908, 'fyCode': 7208, 'fyFlag': 2, 'pktLen': 200,
     'ltp': 563.0, 'open_price': 499.65, 'high_price': 655.0, 'low_price': 335.7, 'close_price': 444.2,
     'min_open_price': 568.5, 'min_high_price': 568.95, 'min_low_price': 559.6, 'min_close_price': 563.0,
     'min_volume': 33500, 'last_traded_qty': 25, 'last_traded_time': 1673600907, 'avg_trade_price': 43127,
     'vol_traded_today': 63103400, 'tot_buy_qty': 632975, 'tot_sell_qty': 146550,
     'market_pic': [{'price': 563.2, 'qty': 125, 'num_orders': 1}, {'price': 563.1, 'qty': 50, 'num_orders': 1},
                    {'price': 563.0, 'qty': 125, 'num_orders': 1}, {'price': 562.9, 'qty': 50, 'num_orders': 1},
                    {'price': 562.85, 'qty': 50, 'num_orders': 1}, {'price': 564.1, 'qty': 150, 'num_orders': 2},
                    {'price': 564.15, 'qty': 200, 'num_orders': 2}, {'price': 564.2, 'qty': 50, 'num_orders': 1},
                    {'price': 564.25, 'qty': 50, 'num_orders': 1}, {'price': 564.29, 'qty': 125, 'num_orders': 2}]
     }]

orderData = {"s": "ok",
             "d": {"orderDateTime": 1673507236, "id": "2230112358425", "exchOrdId": "1800000116334204", "side": 1,
                   "segment": "D", "instrument": "", "productType": "INTRADAY", "status": 6, "qty": 25,
                   "remainingQuantity": 25, "filledQty": 0, "limitPrice": 35.0, "stopPrice": 0.0, "type": 1,
                   "discloseQty": 0, "dqQtyRem": 0, "orderValidity": "DAY", "slNo": 2, "offlineOrder": False,
                   "message": "CONFIRMED", "orderNumStatus": "2230112358425:6", "tradedPrice": 0.0,
                   "fyToken": "101123011240706", "symbol": "NSE:BANKNIFTY2311241700PE"}, "ws_type": 1}

# for _ in range(10):
#     sendSymbolData(symbolData)
#     sendOrderUpdateData(orderData)
