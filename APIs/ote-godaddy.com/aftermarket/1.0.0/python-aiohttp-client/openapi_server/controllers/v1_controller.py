from typing import List, Dict
from aiohttp import web

from openapi_server.models.aftermarket_listing_action import AftermarketListingAction
from openapi_server.models.aftermarket_listing_expiry_create import AftermarketListingExpiryCreate
from openapi_server.models.error import Error
from openapi_server.models.error_limit import ErrorLimit
from openapi_server import util


async def add_expiry_listings(request: web.Request, body) -> web.Response:
    """Add expiry listings into GoDaddy Auction

    

    :param body: An array of expiry listings to be loaded
    :type body: list | bytes

    """
    body = [AftermarketListingExpiryCreate.from_dict(d) for d in body]
    return web.Response(status=200)


async def delete_listings(request: web.Request, domains) -> web.Response:
    """Remove listings from GoDaddy Auction

    

    :param domains: A comma separated list of domain names
    :type domains: List[str]

    """
    return web.Response(status=200)
