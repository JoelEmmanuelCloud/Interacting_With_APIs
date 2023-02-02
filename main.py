from Lib.OpenExchange import OpenExchangeClient

API_ID = 'c2c1b453169b4765b79bafcbbfdf4632'

client = OpenExchangeClient(API_ID)

usd_amount = 1000
gbp_amount = client.convert(usd_amount, "USD", "GBP")

print(f'USD{usd_amount} is GBP{gbp_amount:.2f}')
