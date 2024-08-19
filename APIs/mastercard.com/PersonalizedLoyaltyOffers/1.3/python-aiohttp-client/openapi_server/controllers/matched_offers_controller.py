from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.matched_offers_response import MatchedOffersResponse
from openapi_server import util


async def matchedoffers_get(request: web.Request, fid, user_token, lang=None, merchant_name=None, category=None, offer_type=None, page_number=None, items_per_page=None) -> web.Response:
    """Returns Matched Offers

    This resource returns offers that are available to the user and conform to the search criteria (if specified). 

    :param fid: Financial Institution Identifier. Code that specifies the platform and configuration instance, provided by Mastercard during implementation.
    :type fid: str
    :param user_token: Session identifier as returned by the UserToken resource.
    :type user_token: str
    :param lang: When utilized with a multi-lingual implementation, may be the tongue and country of the user in ISO 639-1, underscore, ISO 3166-1 alpha-2 format.
    :type lang: str
    :param merchant_name: Fuzzy term to search retailers with offers for the user. In general, searching of Matched Offers is not advised as users generally have a modest selection of highly relevant promotions.
    :type merchant_name: str
    :param category: Offer Categories.
    :type category: str
    :param offer_type: The kind of deal. POSTPAIDCREDIT- Statement Credit Offer, which is a discount that is automatically applied to the card linked to the user and utilized to make the purchase.
    :type offer_type: str
    :param page_number: Segment of offers to return.
    :type page_number: int
    :param items_per_page: Segment size of offer to be returned. Default is 25.
    :type items_per_page: int

    """
    return web.Response(status=200)
