from typing import List, Dict
from aiohttp import web

from openapi_server.models.courses_content_id_metadata_category_put_request import CoursesContentIdMetadataCategoryPutRequest
from openapi_server.models.courses_content_id_metadata_level_put_request import CoursesContentIdMetadataLevelPutRequest
from openapi_server.models.courses_content_id_metadata_tags_put_request import CoursesContentIdMetadataTagsPutRequest
from openapi_server.models.courses_content_id_metadata_topic_put_request import CoursesContentIdMetadataTopicPutRequest
from openapi_server.models.error import Error
from openapi_server.models.offering_metadata_response import OfferingMetadataResponse
from openapi_server import util


async def offerings_offering_id_metadata_category_put(request: web.Request, offering_id, body) -> web.Response:
    """Update offering category metadata

    Updates the offering category metadata.

    :param offering_id: offering&#39;s id
    :type offering_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CoursesContentIdMetadataCategoryPutRequest.from_dict(body)
    return web.Response(status=200)


async def offerings_offering_id_metadata_level_put(request: web.Request, offering_id, body) -> web.Response:
    """Update offering level metadata

    Updates the offering level metadata.

    :param offering_id: offering&#39;s id
    :type offering_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CoursesContentIdMetadataLevelPutRequest.from_dict(body)
    return web.Response(status=200)


async def offerings_offering_id_metadata_tags_put(request: web.Request, offering_id, body) -> web.Response:
    """Update offering tags metadata

    Updates the offering tags metadata.

    :param offering_id: offering&#39;s id
    :type offering_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CoursesContentIdMetadataTagsPutRequest.from_dict(body)
    return web.Response(status=200)


async def offerings_offering_id_metadata_topic_put(request: web.Request, offering_id, body) -> web.Response:
    """Update offering topic metadata

    Updates the offering topic metadata.

    :param offering_id: offering&#39;s id
    :type offering_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CoursesContentIdMetadataTopicPutRequest.from_dict(body)
    return web.Response(status=200)
