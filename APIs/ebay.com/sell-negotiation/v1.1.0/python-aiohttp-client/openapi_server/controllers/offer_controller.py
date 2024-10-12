from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_offers_request import CreateOffersRequest
from openapi_server.models.paged_eligible_item_collection import PagedEligibleItemCollection
from openapi_server.models.send_offer_to_interested_buyers_collection_response import SendOfferToInterestedBuyersCollectionResponse
from openapi_server import util


async def find_eligible_items(request: web.Request, x_ebay_c_marketplace_id, limit=None, offset=None) -> web.Response:
    """find_eligible_items

    This method evaluates a seller&#39;s current listings and returns the set of IDs that are eligible for a seller-initiated discount offer to a buyer. A listing ID is returned only when one or more buyers have shown an &amp;quot;interest&amp;quot; in the listing. If any buyers have shown interest in a listing, the seller can initiate a &amp;quot;negotiation&amp;quot; with them by calling sendOfferToInterestedBuyers, which sends all interested buyers a message that offers the listing at a discount. For details about how to create seller offers to buyers, see Sending offers to buyers.

    :param x_ebay_c_marketplace_id: The eBay marketplace on which you want to search for eligible listings. For a complete list of supported marketplaces, see Negotiation API requirements and restrictions.
    :type x_ebay_c_marketplace_id: str
    :param limit: This query parameter specifies the maximum number of items to return from the result set on a page in the paginated response. Minimum: 1 &amp;nbsp; &amp;nbsp;Maximum: 200 Default: 10
    :type limit: str
    :param offset: This query parameter specifies the number of results to skip in the result set before returning the first result in the paginated response. Combine offset with the limit query parameter to control the items returned in the response. For example, if you supply an offset of 0 and a limit of 10, the first page of the response contains the first 10 results from the complete list of items retrieved by the call. If offset is 10 and limit is 20, the first page of the response contains items 11-30 from the complete result set. Default: 0
    :type offset: str

    """
    return web.Response(status=200)


async def send_offer_to_interested_buyers(request: web.Request, x_ebay_c_marketplace_id, body=None) -> web.Response:
    """send_offer_to_interested_buyers

    This method sends eligible buyers offers to purchase items in a listing at a discount. When a buyer has shown interest in a listing, they become &amp;quot;eligible&amp;quot; to receive a seller-initiated offer to purchase the item(s). Sellers use findEligibleItems to get the set of listings that have interested buyers. If a listing has interested buyers, sellers can use this method (sendOfferToInterestedBuyers) to send an offer to the buyers who are interested in the listing. The offer gives buyers the ability to purchase the associated listings at a discounted price. For details about how to create seller offers to buyers, see Sending offers to buyers.

    :param x_ebay_c_marketplace_id: The eBay marketplace on which your listings with &amp;quot;eligible&amp;quot; buyers appear. For a complete list of supported marketplaces, see Negotiation API requirements and restrictions.
    :type x_ebay_c_marketplace_id: str
    :param body: Send offer to eligible items request.
    :type body: dict | bytes

    """
    body = CreateOffersRequest.from_dict(body)
    return web.Response(status=200)
