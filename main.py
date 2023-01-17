import symbolDataProducer

app_id = "PWX6BM1OI5-100:"
access_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJhcGkuZnllcnMuaW4iLCJpYXQiOjE2NzM1OTE4NzAsImV4cCI6MTY3MzY1NjI1MCwibmJmIjoxNjczNTkxODcwLCJhdWQiOlsieDowIiwieDoxIiwieDoyIiwiZDoxIiwiZDoyIiwieDoxIiwieDowIl0sInN1YiI6ImFjY2Vzc190b2tlbiIsImF0X2hhc2giOiJnQUFBQUFCandQdy1seXRWeURlck5ndmVjNmxzNWVrVFhBYVlPTmxlZG1YVWExU3NjeXAzQTMtM0YyNXhCcTdnRDc3QnllSjhYSHhsc2JiUmhNdHhjRkFhTmUyM2FoY2Ffd2hzSTcxdmpQcHV3Mm00Y3dqMFFrdz0iLCJkaXNwbGF5X25hbWUiOiJKSVRFU0hLVU1BUiBNQU5PSktVTUFSIEpIIiwib21zIjpudWxsLCJmeV9pZCI6IlhKMDMzOTIiLCJhcHBUeXBlIjoxMDAsInBvYV9mbGFnIjoiTiJ9.q7PPIta_fRDv-Jivdbuk2-8QN0RX1pYr05_vLakODjE"
run_background = True
symbols = ['NSE:BANKNIFTY2311942000PE', 'NSE:BANKNIFTY2311942000CE']


def socketSymbolDataResponse(msg):
    print("Inside socketSymbolDataResponse")
    symbolDataProducer.sendSymbolData(msg)


def socketOrderUpdateDataResponse(msg):
    print("Inside socketOrderUpdateDataResponse")
    symbolDataProducer.sendOrderUpdateData(msg)


def socketOpenResponse(msg):
    print('Opened Socket')
    return msg


def socketErrorResponse(msg):
    print(f'Error in Socket {msg}')
    return msg
