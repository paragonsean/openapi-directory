from typing import List, Dict
from aiohttp import web

from openapi_server.models.previous_asset_purchases import PreviousAssetPurchases
from openapi_server import util


async def v3_purchased_assets_get(request: web.Request, accept_language=None, date_to=None, page=None, page_size=None, date_from=None, company_purchases=None) -> web.Response:
    """Get Previously Purchased Images and Video

    This endpoint returns a list of all assets purchased on gettyimages.com by the username used for authentication.  Use of this endpoint requires configuration changes to your API key. Please contact your sales representative to learn more.  You&#39;ll need an API key and access token to use this resource. 

    :param accept_language: Provide a header to specify the language of result values. Supported values: cs (iStock only), de, en-GB, en-US, es, fi (iStock only), fr, hu (iStock only), id (iStock only), it, ja, ko (creative assets only), nl, pl (creative assets only), pt-BR, pt-PT, ro (iStock only), ru (creative assets only), sv, th (iStock only), tr, uk (iStock only), vi (iStock only), zh-HK (creative assets only).
    :type accept_language: str
    :param date_to: If specified, retrieves previous purchases on or before this date. Dates should be submitted in ISO 8601 format (i.e., YYYY-MM-DD).
    :type date_to: str
    :param page: Identifies page to return. Default is 1.
    :type page: int
    :param page_size: Specifies page size. Default is 75, maximum page_size is 100.
    :type page_size: int
    :param date_from: If specified, retrieves previous purchases on or after this date. Dates should be submitted in ISO 8601 format (i.e., YYYY-MM-DD).
    :type date_from: str
    :param company_purchases: If specified, returns the list of previously purchased assets for all users in your company. Your account must be enabled for this functionality. Contact your Getty Images account rep for more information. Default is false.
    :type company_purchases: bool

    """
    date_to = util.deserialize_datetime(date_to)
    date_from = util.deserialize_datetime(date_from)
    return web.Response(status=200)
