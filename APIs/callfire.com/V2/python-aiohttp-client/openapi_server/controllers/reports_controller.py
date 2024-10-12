from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.page_delivery_report import PageDeliveryReport
from openapi_server import util


async def get_delivery_reports(request: web.Request, start_date=None, end_date=None, limit=None, offset=None, campaign_id=None, from_number=None, to_number=None, delivery_category=None, delivery_state=None, carrier=None, message_text=None) -> web.Response:
    """Get delivery reports by ad hoc criteria

    Get delivery reports

    :param start_date: ~
    :type start_date: str
    :param end_date: ~
    :type end_date: str
    :param limit: To set the maximum number of records to return in a paged list response. The default is 100
    :type limit: int
    :param offset: Offset to the start of a given page. The default is 0. Check [pagination](https://developers.callfire.com/docs.html#pagination) page for more information about pagination in CallFire API.
    :type offset: int
    :param campaign_id: ~
    :type campaign_id: int
    :param from_number: ~
    :type from_number: str
    :param to_number: ~
    :type to_number: str
    :param delivery_category: ~
    :type delivery_category: str
    :param delivery_state: ~
    :type delivery_state: str
    :param carrier: ~
    :type carrier: str
    :param message_text: ~
    :type message_text: str

    """
    return web.Response(status=200)
