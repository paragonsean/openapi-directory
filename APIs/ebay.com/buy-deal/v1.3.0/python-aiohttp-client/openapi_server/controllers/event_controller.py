from typing import List, Dict
from aiohttp import web

from openapi_server.models.event import Event
from openapi_server.models.event_search_response import EventSearchResponse
from openapi_server import util


async def get_event(request: web.Request, x_ebay_c_marketplace_id, event_id) -> web.Response:
    """get_event

    This method retrieves the details for an eBay event. The result set contains detailed information associated with the specified event ID, such as applicable coupons, start and end dates, and event terms. Request headers This method uses the X-EBAY-C-ENDUSERCTX request header to support revenue sharing for eBay Partner Networks and to improve the accuracy of shipping and delivery time estimations. For details see, Request headers in the Buying Integration Guide. Restrictions This method can return a maximum of 10,000 items. For a list of supported sites and other restrictions, see API Restrictions. eBay Partner Network: In order to receive a commission for your sales, you must use the URL returned in the itemAffiliateWebUrl field to forward your buyer to the ebay.com site.

    :param x_ebay_c_marketplace_id: A header used to specify the eBay marketplace ID.
    :type x_ebay_c_marketplace_id: str
    :param event_id: The unique identifier for the eBay event.
    :type event_id: str

    """
    return web.Response(status=200)


async def get_events(request: web.Request, x_ebay_c_marketplace_id, limit=None, offset=None) -> web.Response:
    """get_events

    This method returns paginated results containing all eBay events for the specified marketplace. Request headers This method uses the X-EBAY-C-ENDUSERCTX request header to support revenue sharing for eBay Partner Networks and to improve the accuracy of shipping and delivery time estimations. For details see, Request headers in the Buying Integration Guide. Restrictions This method can return a maximum of 10,000 items. For a list of supported sites and other restrictions, see API Restrictions. eBay Partner Network: In order to receive a commission for your sales, you must use the URL returned in the itemAffiliateWebUrl field to forward your buyer to the ebay.com site.

    :param x_ebay_c_marketplace_id: A header used to specify the eBay marketplace ID.
    :type x_ebay_c_marketplace_id: str
    :param limit: The maximum number of items, from the current result set, returned on a single page. Default: 20 Maximum Value: 100
    :type limit: str
    :param offset: The number of items that will be skipped in the result set. This is used with the limit field to control the pagination of the output. For example, if the offset is set to 0 and the limit is set to 10, the method will retrieve items 1 through 10 from the list of items returned. If the offset is set to 10 and the limit is set to 10, the method will retrieve items 11 through 20 from the list of items returned. Default: 0
    :type offset: str

    """
    return web.Response(status=200)
