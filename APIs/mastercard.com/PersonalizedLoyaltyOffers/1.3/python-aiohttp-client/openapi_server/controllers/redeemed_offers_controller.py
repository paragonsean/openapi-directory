from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.redeemed_offers_response import RedeemedOffersResponse
from openapi_server import util


async def redeemedoffers_get(request: web.Request, fid, user_token, lang=None, page_number=None, items_per_page=None) -> web.Response:
    """Returns Redeemed Offers

    This resource returns offers that have been fulfilled by the user. 

    :param fid: Financial Institution Identifier. Code that specifies the platform and configuration instance, provided by Mastercard during implementation.
    :type fid: str
    :param user_token: Session identifier as returned by the UserToken resource.
    :type user_token: str
    :param lang: When utilized with a multi-lingual implementation, may be the tongue and country of the user in ISO 639-1, underscore, ISO 3166-1 alpha-2 format.
    :type lang: str
    :param page_number: Segment of offers to return.
    :type page_number: int
    :param items_per_page: Segment size of offer to be returned. Default is 25.
    :type items_per_page: int

    """
    return web.Response(status=200)
