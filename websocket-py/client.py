import asyncio
import websockets

async def binance():
    async with websockets.connect("wss://stream.binance.com:9443/ws/USDTDAI@trade") as websocket:
        # await websocket.send("Hello world!")
        async for message in websocket:
            print(message)

'''
{
  "e": "aggTrade",  // Event type
  "E": 123456789,   // Event time
  "s": "BNBBTC",    // Symbol
  "a": 12345,       // Aggregate trade ID
  "p": "0.001",     // Price
  "q": "100",       // Quantity
  "f": 100,         // First trade ID
  "l": 105,         // Last trade ID
  "T": 123456785,   // Trade time
  "m": true,        // Is the buyer the market maker?
  "M": true         // Ignore
}
'''

asyncio.run(binance())