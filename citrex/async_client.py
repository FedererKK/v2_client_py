"""
Async client for the Citrex API
"""

from typing import Any

from citrex.enums import Environment, SupportedChains
import httpx

from citrex.client import CitrexClient
from citrex.exceptions import ClientError
from citrex.utils import from_message_to_payload
from citrex.eip_712 import CancelOrders


class AsyncCitrexClient(CitrexClient):
    """
    Asynchronous client for the Citrex API.
    """
    
    def __init__(
        self,
        chain: SupportedChains = SupportedChains.SEI,
        env: Environment = Environment.PROD,
        private_key: str = None,
        subaccount_id: int = 0,
        
    ):
        
        
        # Call the parent class constructor
        super().__init__(
            chain,
            env,
            private_key,
            subaccount_id,

        )
    
    async def get_product(self, symbol: str = None):
        """
        Get the product infos.
        If symbol is None, return all products.
        """
        async with httpx.AsyncClient() as client:
            if symbol:
                response = await client.get(self.api_url + f"/v1/products/{symbol}")
            else:
                response = await client.get(self.api_url + "/v1/products")
            return response.json()

    async def get_symbol(self, symbol: str = None):
        """
        Get the symbol infos.
        If symbol is None, return all symbols.
        """
        async with httpx.AsyncClient() as client:
            if symbol:
                response = await client.get(self.api_url + f"/v1/symbols/{symbol}")
            else:
                response = await client.get(self.api_url + "/v1/symbols")
            return response.json()

    async def get_account_health(self) -> Any:
        """
        Get the account health.
        """
        return await super().get_account_health()

    async def get_depth(self, symbol: str, **kwargs) -> Any:
        """
        Get the depth for a specific symbol.
        """
        return await super().get_depth(symbol, **kwargs)

    async def get_trade_history(self, symbol: str, lookback: int = 10, **kwargs) -> Any:
        """
        Get the trade history for a specific symbol.
        if symbol is None, return all trade history.
        """
        return await super().get_trade_history(symbol, lookback, **kwargs)

    async def get_positions(self, symbol: str = None):
        """
        Get all positions for the subaccount.
        If a symbol is provided, return only that position.
        """
        params = {
            "account": self.public_key,
            "subAccountId": self.subaccount_id,
        }
        if symbol:
            params["symbol"] = symbol

        return await self.send_message_to_endpoint(
            endpoint="/v1/positionRisk",
            method="GET",
            params=params,
            authenticated=True,
        )

    async def get_spot_balances(self):
        """
        Get the spot balances.
        """
        return await super().get_spot_balances()

    async def get_open_orders(self, symbol: str = None):
        """
        Get the open orders for a specific symbol.
        """
        return await super().get_open_orders(symbol)

    async def create_order(self, *args, **kwargs):
        """
        Create and send order.
        """
        return await super().create_order(*args, **kwargs)

    async def cancel_order(self, *args, **kwargs):
        """
        Cancel an order.
        """
        return await super().cancel_order(*args, **kwargs)

    async def cancel_and_replace_order(self, *args, **kwargs):
        """
        Cancel and replace an order.
        """
        return await super().cancel_and_replace_order(*args, **kwargs)

    
    async def cancel_all_orders(
        self,
        subaccount_id: int,
        product_id: int,
    ):
        """
        Cancel all orders for a product on a given subaccount.
        Private endpoint.
        """
        message = self.generate_and_sign_message(
            CancelOrders,
            subAccountId=subaccount_id,
            productId=product_id,
            **self.get_shared_params(),
        )

        return await self.send_message_to_endpoint(
            endpoint="/v1/openOrders",
            method="DELETE",
            message=message,
            authenticated=True,
        )

    
    async def send_message_to_endpoint(
        self, endpoint: str, method: str, message: dict = {}, authenticated: bool = True, params: dict = {}
    ):
        """
        Send a message to an endpoint.
        """
        if not self._validate_function(
            endpoint,
        ):
            raise ClientError(f"Invalid endpoint: {endpoint}")
        payload = from_message_to_payload(message)

        async with httpx.AsyncClient() as client:
            response = await client.request(
                method,
                self.rest_url + endpoint,
                params=params,
                headers={} if not authenticated else self.authenticated_headers,
                json=payload,
            )

            if response.status_code != 200:
                raise Exception(
                    f"Failed to send message: {response.text} {response.status_code} {self.rest_url} {payload}"
                )
            return response.json()
