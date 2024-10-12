from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def get_feature(request: web.Request, feature_id) -> web.Response:
    """Feature Detail

    Return the content of the selected feature.

    :param feature_id: The identifier for the selected feature.
    :type feature_id: str

    """
    return web.Response(status=200)


async def list_feature_types(request: web.Request, ) -> web.Response:
    """Feature Type Collection

    Return a collection of Feature Types.


    """
    return web.Response(status=200)


async def list_features(request: web.Request, type=None, _date=None, start=None, end=None) -> web.Response:
    """Feature Collection

    Return a collection of Feature.

    :param type: The namespace of the feature type.
    :type type: str
    :param _date: Date of the collection of feature items.
    :type _date: str
    :param start: Start date for a range of features.
    :type start: str
    :param end: End date for a range of features.
    :type end: str

    """
    return web.Response(status=200)
