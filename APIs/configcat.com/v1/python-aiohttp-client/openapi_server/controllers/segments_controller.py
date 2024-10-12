from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_segment_model import CreateSegmentModel
from openapi_server.models.segment_list_model import SegmentListModel
from openapi_server.models.segment_list_model_haljson import SegmentListModelHaljson
from openapi_server.models.segment_model import SegmentModel
from openapi_server.models.segment_model_haljson import SegmentModelHaljson
from openapi_server.models.update_segment_model import UpdateSegmentModel
from openapi_server import util


async def create_segment(request: web.Request, product_id, body) -> web.Response:
    """Create Segment

    This endpoint creates a new Segment in a specified Product  identified by the &#x60;productId&#x60; parameter, which can be obtained from the [List Products](#operation/get-products) endpoint.

    :param product_id: The identifier of the Product.
    :type product_id: str
    :type product_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateSegmentModel.from_dict(body)
    return web.Response(status=200)


async def delete_segment(request: web.Request, segment_id) -> web.Response:
    """Delete Segment

    This endpoint removes a Segment identified by the &#x60;segmentId&#x60; parameter.

    :param segment_id: The identifier of the Segment.
    :type segment_id: str
    :type segment_id: str

    """
    return web.Response(status=200)


async def get_segment(request: web.Request, segment_id) -> web.Response:
    """Get Segment

    This endpoint returns the metadata of a Segment identified by the &#x60;segmentId&#x60;.

    :param segment_id: The identifier of the Segment.
    :type segment_id: str
    :type segment_id: str

    """
    return web.Response(status=200)


async def get_segments(request: web.Request, product_id) -> web.Response:
    """List Segments

    This endpoint returns the list of the Segments that belongs to the given Product identified by the &#x60;productId&#x60; parameter, which can be obtained from the [List Products](#operation/get-products) endpoint.

    :param product_id: The identifier of the Product.
    :type product_id: str
    :type product_id: str

    """
    return web.Response(status=200)


async def update_segment(request: web.Request, segment_id, body) -> web.Response:
    """Update Segment

    This endpoint updates a Segment identified by the &#x60;segmentId&#x60; parameter.

    :param segment_id: The identifier of the Segment.
    :type segment_id: str
    :type segment_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateSegmentModel.from_dict(body)
    return web.Response(status=200)
