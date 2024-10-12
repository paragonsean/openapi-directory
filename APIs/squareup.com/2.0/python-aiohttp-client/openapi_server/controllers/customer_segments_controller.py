from typing import List, Dict
from aiohttp import web

from openapi_server.models.list_customer_segments_response import ListCustomerSegmentsResponse
from openapi_server.models.retrieve_customer_segment_response import RetrieveCustomerSegmentResponse
from openapi_server import util


async def list_customer_segments(request: web.Request, cursor=None, limit=None) -> web.Response:
    """ListCustomerSegments

    Retrieves the list of customer segments of a business.

    :param cursor: A pagination cursor returned by previous calls to &#x60;ListCustomerSegments&#x60;. This cursor is used to retrieve the next set of query results.  For more information, see [Pagination](https://developer.squareup.com/docs/working-with-apis/pagination).
    :type cursor: str
    :param limit: The maximum number of results to return in a single page. This limit is advisory. The response might contain more or fewer results.  The limit is ignored if it is less than 1 or greater than 50. The default value is 50.  For more information, see [Pagination](https://developer.squareup.com/docs/working-with-apis/pagination).
    :type limit: int

    """
    return web.Response(status=200)


async def retrieve_customer_segment(request: web.Request, segment_id) -> web.Response:
    """RetrieveCustomerSegment

    Retrieves a specific customer segment as identified by the &#x60;segment_id&#x60; value.

    :param segment_id: The Square-issued ID of the customer segment.
    :type segment_id: str

    """
    return web.Response(status=200)
