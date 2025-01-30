# Citrex

## Usage

```python

from citrex.client import CitrexClient
from citrex.enums import OrderSide, OrderType, TimeInForce

PRIVATE_KEY = "*********"

client = CitrexClient(private_key=PRIVATE_KEY)

# List available products
products = client.list_products()
print(products)

# Get the current price of a symbol
price = client.get_product("ethperp")
print(price)

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

For asynchronous usage, refer to 'examples/async_client.py'.

## Development

### Prequisites

- Python 3.8+
- [Poetry](https://python-poetry.org/)

### Setup

1. Clone the repository:

```shell
git clone https://github.com/rysk-finance/v2_client_py.git && cd v2_client_py
```

2. Create a development environment:

```shell
poetry install && poetry shell
```

### Development Commands

```shell
# Format Code
make fmt

# Lint Code
make lint

# Run Tests
make tests

# Run all checks
make all

# Create a new release
make release
```

### Docker Environemnt

```shell
# Build Docker Image
docker buildx build --platform linux/amd64 . -t test

# Run tests in Docker
docker run -v (pwd):/app -it test
```

### Contributing

### Contributors

<table>
<tr>
    <td align="center" style="word-wrap: break-word; width: 150.0; height: 150.0">
        <a href=https://github.com/8ball030>
            <img src=https://avatars.githubusercontent.com/u/35799987?v=4 width="100;"  style="border-radius:50%;align-items:center;justify-content:center;overflow:hidden;padding-top:10px" alt=8ball030/>
            <br />
            <sub style="font-size:14px"><b>8ball030</b></sub>
        </a>
    </td>
    <td align="center" style="word-wrap: break-word; width: 150.0; height: 150.0">
        <a href=https://github.com/kjr217>
            <img src=https://avatars.githubusercontent.com/u/55159119?v=4 width="100;"  style="border-radius:50%;align-items:center;justify-content:center;overflow:hidden;padding-top:10px" alt=kjr217/>
            <br />
            <sub style="font-size:14px"><b>kjr217</b></sub>
        </a>
    </td>
    <td align="center" style="word-wrap: break-word; width: 150.0; height: 150.0">
        <a href=https://github.com/thegeronimo>
            <img src=https://avatars.githubusercontent.com/u/59147332?v=4 width="100;"  style="border-radius:50%;align-items:center;justify-content:center;overflow:hidden;padding-top:10px" alt=thegeronimo/>
            <br />
            <sub style="font-size:14px"><b>thegeronimo</b></sub>
        </a>
    </td>
</tr>
<tr>
    <td align="center" style="word-wrap: break-word; width: 150.0; height: 150.0">
        <a href=https://github.com/xiuxiuxar>
            <img src=https://avatars.githubusercontent.com/u/174127740?v=4 width="100;"  style="border-radius:50%;align-items:center;justify-content:center;overflow:hidden;padding-top:10px" alt=xiuxiuxar/>
            <br />
            <sub style="font-size:14px"><b>xiuxiuxar</b></sub>
        </a>
    </td>
    <td align="center" style="word-wrap: break-word; width: 150.0; height: 150.0">
        <a href=https://github.com/wakamex>
            <img src=https://avatars.githubusercontent.com/u/16990562?v=4 width="100;"  style="border-radius:50%;align-items:center;justify-content:center;overflow:hidden;padding-top:10px" alt=Mihai/>
            <br />
            <sub style="font-size:14px"><b>Mihai</b></sub>
        </a>
    </td>
</tr>
</table>
