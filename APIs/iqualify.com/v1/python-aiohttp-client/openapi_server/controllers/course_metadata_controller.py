from typing import List, Dict
from aiohttp import web

from openapi_server.models.course_meta_response import CourseMetaResponse
from openapi_server.models.courses_content_id_metadata_category_put_request import CoursesContentIdMetadataCategoryPutRequest
from openapi_server.models.courses_content_id_metadata_level_put_request import CoursesContentIdMetadataLevelPutRequest
from openapi_server.models.courses_content_id_metadata_tags_put_request import CoursesContentIdMetadataTagsPutRequest
from openapi_server.models.courses_content_id_metadata_topic_put_request import CoursesContentIdMetadataTopicPutRequest
from openapi_server.models.error import Error
from openapi_server import util


async def courses_content_id_metadata_category_put(request: web.Request, content_id, body) -> web.Response:
    """Update course category

    Add or update course category in the metadata of a course.

    :param content_id: The content Id
    :type content_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CoursesContentIdMetadataCategoryPutRequest.from_dict(body)
    return web.Response(status=200)


async def courses_content_id_metadata_level_put(request: web.Request, content_id, body) -> web.Response:
    """Update course level

    Add or update the course level in the metadata of a course.

    :param content_id: The content Id
    :type content_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CoursesContentIdMetadataLevelPutRequest.from_dict(body)
    return web.Response(status=200)


async def courses_content_id_metadata_tags_put(request: web.Request, content_id, body) -> web.Response:
    """Update course tags

    Add or update course tags in the metadata of a course.

    :param content_id: The content Id
    :type content_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CoursesContentIdMetadataTagsPutRequest.from_dict(body)
    return web.Response(status=200)


async def courses_content_id_metadata_topic_put(request: web.Request, content_id, body) -> web.Response:
    """Update course topic

    Add or update the course topic in the metadata of a course.

    :param content_id: The content Id
    :type content_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CoursesContentIdMetadataTopicPutRequest.from_dict(body)
    return web.Response(status=200)
