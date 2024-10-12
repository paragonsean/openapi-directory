from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.gift_wrapping_data_wrapping_interface import GiftWrappingDataWrappingInterface
from openapi_server.models.gift_wrapping_wrapping_repository_v1_save_post_request import GiftWrappingWrappingRepositoryV1SavePostRequest
from openapi_server import util


async def gift_wrapping_wrapping_repository_v1_save_put(request: web.Request, wrapping_id, body=None) -> web.Response:
    """gift-wrappings/{wrappingId}

    Create/Update new gift wrapping with data object values

    :param wrapping_id: 
    :type wrapping_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = GiftWrappingWrappingRepositoryV1SavePostRequest.from_dict(body)
    return web.Response(status=200)
