from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def inventory_notification(request: web.Request, account_name, environment, accept, content_type, seller_id, sku_id) -> web.Response:
    """Notify marketplace of inventory update

    This endpoint is used by *sellers* to notify marketplaces that the inventory level has changed for one of their SKUs.   There is no request body in this call, indicating the new inventory level, for instance. It only notifies a specific marketplace (&#x60;accountName&#x60;) that a seller (&#x60;sellerId&#x60;) has changed the inventory level of an SKU (&#x60;skuId&#x60;).   *Marketplaces* will then call the [fulfillment endpoint](https://developers.vtex.com/vtex-rest-api/reference/fulfillment-simulation) provided in the seller registration form to get the updated inventory  information.

    :param account_name: Name of the VTEX account that belongs to the marketplace. The notification will be posted into this account.
    :type account_name: str
    :param environment: Environment to use. Used as part of the URL.
    :type environment: str
    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param content_type: Describes the type of the content being sent.
    :type content_type: str
    :param seller_id: A string that identifies the seller in the marketplace. This ID must be created by the marketplace and informed to the seller before the integration is built.
    :type seller_id: str
    :param sku_id: A string that identifies the SKU in the seller, that suffered the change. This is the ID that the marketplace will use for all  references to this SKU, such as price and inventory notifications.
    :type sku_id: str

    """
    return web.Response(status=200)


async def price_notification(request: web.Request, account_name, content_type, environment, accept, seller_id, sku_id) -> web.Response:
    """Notify marketplace of price update

    This endpoint is used by *sellers* to notify marketplaces that the price has changed for one of their SKUs.   There is no request body in this call, indicating the new price value, for instance. It only notifies a specific marketplace (&#x60;accountName&#x60;) that a seller (&#x60;sellerId&#x60;) has changed the price of an SKU (&#x60;skuId&#x60;).   *Marketplaces* will then call the [fulfillment endpoint](https://developers.vtex.com/vtex-rest-api/reference/fulfillment-simulation) provided in the seller registration form to get the updated price information.

    :param account_name: Name of the VTEX account that belongs to the marketplace. The notification will be posted into this account.
    :type account_name: str
    :param content_type: Describes the type of the content being sent.
    :type content_type: str
    :param environment: Environment to use. Used as part of the URL.
    :type environment: str
    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param seller_id: A string that identifies the seller in the marketplace. This ID must be created by the marketplace and informed to the seller before the integration is built.
    :type seller_id: str
    :param sku_id: A string that identifies the seller&#39;s SKU that suffered the change. This is the ID that the marketplace will use for all  references to this SKU, such as price and inventory notifications.
    :type sku_id: str

    """
    return web.Response(status=200)
