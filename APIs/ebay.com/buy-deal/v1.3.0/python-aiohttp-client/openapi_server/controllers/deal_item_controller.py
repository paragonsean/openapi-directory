from typing import List, Dict
from aiohttp import web

from openapi_server.models.deal_item_search_response import DealItemSearchResponse
from openapi_server import util


async def get_deal_items(request: web.Request, x_ebay_c_marketplace_id, category_ids=None, commissionable=None, delivery_country=None, limit=None, offset=None) -> web.Response:
    """get_deal_items

    This method retrieves a paginated set of deal items. The result set contains all deal items associated with the specified search criteria and marketplace ID. Request headers This method uses the X-EBAY-C-ENDUSERCTX request header to support revenue sharing for eBay Partner Networks and to improve the accuracy of shipping and delivery time estimations. For details see, Request headers in the Buying Integration Guide. Restrictions This method can return a maximum of 10,000 items. For a list of supported sites and other restrictions, see API Restrictions. eBay Partner Network: In order to receive a commission for your sales, you must use the URL returned in the itemAffiliateWebUrl field to forward your buyer to the ebay.com site.

    :param x_ebay_c_marketplace_id: A header used to specify the eBay marketplace ID.
    :type x_ebay_c_marketplace_id: str
    :param category_ids: The unique identifier of the eBay category for the search.
    :type category_ids: str
    :param commissionable: A filter for commissionable deals. Restriction: This filter is currently only supported for the US marketplace.
    :type commissionable: str
    :param delivery_country: A filter for items that can be shipped to the specified country.
    :type delivery_country: str
    :param limit: The maximum number of items, from the current result set, returned on a single page.
    :type limit: str
    :param offset: The number of items that will be skipped in the result set. This is used with the limit field to control the pagination of the output. For example, if the offset is set to 0 and the limit is set to 10, the method will retrieve items 1 through 10 from the list of items returned. If the offset is set to 10 and the limit is set to 10, the method will retrieve items 11 through 20 from the list of items returned. Default: 0
    :type offset: str

    """
    return web.Response(status=200)
