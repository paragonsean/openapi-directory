from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def feature_categories_get(request: web.Request, output_format) -> web.Response:
    """Get all feature categories

    Gets a list of all feature categories used by the BC Geographical Names Information System (BCGNIS).  Note: there are three levels of classification in the BCGNIS feature taxonomy: classes, categories and types.  A type is a subset of a category, and a category is a subset of a class.

    :param output_format: The format of the output.
    :type output_format: str

    """
    return web.Response(status=200)


async def feature_classes_get(request: web.Request, output_format) -> web.Response:
    """Get all feature classes

    Gets a list of all feature classes used by the BC Geographical Names Information System (BCGNIS).  Note: there are three levels of classification in the BCGNIS feature taxonomy: classes, categories and types.  A type is a subset of a category, and a category is a subset of a class.

    :param output_format: The format of the output.
    :type output_format: str

    """
    return web.Response(status=200)


async def feature_types_get(request: web.Request, output_format) -> web.Response:
    """Get all feature types

    Gets a list of all feature types used by the BC Geographical Names Information System (BCGNIS).  Note: there are three levels of classification in the BCGNIS feature taxonomy: classes, categories and types.  A type is a subset of a category, and a category is a subset of a class.

    :param output_format: The format of the output.
    :type output_format: str

    """
    return web.Response(status=200)
