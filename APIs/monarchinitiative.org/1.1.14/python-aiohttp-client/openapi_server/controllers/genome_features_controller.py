from typing import List, Dict
from aiohttp import web

from openapi_server.models.sequence_feature import SequenceFeature
from openapi_server import util


async def get_features_within_resource(request: web.Request, build, reference, begin, end) -> web.Response:
    """Returns list of matches

    

    :param build: 
    :type build: str
    :param reference: 
    :type reference: str
    :param begin: 
    :type begin: str
    :param end: 
    :type end: str

    """
    return web.Response(status=200)
