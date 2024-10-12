from typing import List, Dict
from aiohttp import web

from openapi_server.models.numbers_v2_bulk_hosted_number_order import NumbersV2BulkHostedNumberOrder
from openapi_server import util


async def fetch_bulk_hosted_number_order(request: web.Request, bulk_hosting_sid, order_status=None) -> web.Response:
    """fetch_bulk_hosted_number_order

    Fetch a specific BulkHostedNumberOrder.

    :param bulk_hosting_sid: A 34 character string that uniquely identifies this BulkHostedNumberOrder.
    :type bulk_hosting_sid: str
    :param order_status: Order status can be used for filtering on Hosted Number Order status values. To see a complete list of order statuses, please check &#39;https://www.twilio.com/docs/phone-numbers/hosted-numbers/hosted-numbers-api/hosted-number-order-resource#status-values&#39;.
    :type order_status: str

    """
    return web.Response(status=200)
