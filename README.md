# Citrex

## REST Usage

```python

from citrex.client import CitrexClient
from citrex.enums import OrderSide, OrderType, TimeInForce

PRIVATE_KEY = "*********"

client = CitrexClient(private_key=PRIVATE_KEY)

# List available products
products = client.list_products()
print(products)

# Get the current info for a specific product
product = client.get_product("ethperp")
print(product)

# Create a limit order (buy 1 XRP at $3.1)
order = client.create_order(
    subaccount_id=0,
    product_id=1006,  # xrpperp
    quantity=1,
    side=OrderSide.BUY,
    order_type=OrderType.LIMIT,
    time_in_force=TimeInForce.GTC,
    price="3.1",
)
print(order)

# Get open orders
open_orders = client.get_open_orders()
print(open_orders)

# Cancel an order, here we cancel the first open order from the list
client.cancel_order(
    order_id=open_orders[0]["id"], product_id=open_orders[0]["productId"]
)

# Cancel all orders for a specific market
client.cancel_all_orders(subaccount_id=0, product_id=1006)  # xrpperp

```

## Async Usage


```python
import asyncio

from citrex.async_client import AsyncCitrexClient
from citrex.enums import OrderSide, OrderType, TimeInForce

client = AsyncCitrexClient(private_key="*********")


async def main():
    # Get the current info for a specific product
    product = await client.get_product("ethperp")
    print(product)

    # Create a limit order (buy 1 XRP at $3.1)
    order = await client.create_order(
        subaccount_id=0,
        product_id=1006,  # xrpperp
        quantity=1,
        side=OrderSide.BUY,
        order_type=OrderType.LIMIT,
        time_in_force=TimeInForce.GTC,
        price="3.1",
    )

    print(order)

    # Get open orders
    open_orders = await client.get_open_orders()
    print(open_orders)

    # Cancel an order, here we cancel the first open order from the list
    await client.cancel_order(
        order_id=open_orders[0]["id"], product_id=open_orders[0]["productId"]
    )

    # Cancel all orders for a specific market
    await client.cancel_all_orders(subaccount_id=0, product_id=1006)  # xrpperp


if __name__ == "__main__":
    asyncio.run(main())

```
