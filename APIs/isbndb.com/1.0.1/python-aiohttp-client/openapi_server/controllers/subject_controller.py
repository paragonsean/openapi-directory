from typing import List, Dict
from aiohttp import web

from openapi_server.models.subject import Subject
from openapi_server import util


async def subject_name_get(request: web.Request, name) -> web.Response:
    """Gets subject details

    Returns details and a list of books with subject.

    :param name: A subject in the Subject&#39;s database
    :type name: str

    """
    return web.Response(status=200)


async def subjects_query_get(request: web.Request, query, page_size=None, page=None) -> web.Response:
    """Search subjects

    This returns a list of subjects that match the given query

    :param query: A string to search for in the Subject’s database
    :type query: str
    :param page_size: How many items should be returned per page, maximum of 1,000
    :type page_size: str
    :param page: The number of page to retrieve, please note the API will not return more than 10,000 results no matter how you paginate them
    :type page: str

    """
    return web.Response(status=200)
