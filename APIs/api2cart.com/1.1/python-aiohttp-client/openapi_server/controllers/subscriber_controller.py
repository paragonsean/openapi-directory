from typing import List, Dict
from aiohttp import web

from openapi_server.models.subscriber_list200_response import SubscriberList200Response
from openapi_server import util


async def subscriber_list(request: web.Request, start=None, count=None, subscribed=None, store_id=None, email=None, params=None, exclude=None, created_from=None, created_to=None, modified_from=None, modified_to=None, page_cursor=None, response_fields=None) -> web.Response:
    """subscriber_list

    Get subscribers list

    :param start: This parameter sets the number from which you want to get entities
    :type start: int
    :param count: This parameter sets the entity amount that has to be retrieved. Max allowed count&#x3D;250
    :type count: int
    :param subscribed: Filter by subscription status
    :type subscribed: bool
    :param store_id: Store Id
    :type store_id: str
    :param email: Filter subscribers by email
    :type email: str
    :param params: Set this parameter in order to choose which entity fields you want to retrieve
    :type params: str
    :param exclude: Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter &#x60;params&#x60; equal force_all
    :type exclude: str
    :param created_from: Retrieve entities from their creation date
    :type created_from: str
    :param created_to: Retrieve entities to their creation date
    :type created_to: str
    :param modified_from: Retrieve entities from their modification date
    :type modified_from: str
    :param modified_to: Retrieve entities to their modification date
    :type modified_to: str
    :param page_cursor: Used to retrieve entities via cursor-based pagination (it can&#39;t be used with any other filtering parameter)
    :type page_cursor: str
    :param response_fields: Set this parameter in order to choose which entity fields you want to retrieve
    :type response_fields: str

    """
    return web.Response(status=200)
