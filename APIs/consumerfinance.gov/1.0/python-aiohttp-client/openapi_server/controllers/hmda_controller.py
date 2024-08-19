from typing import List, Dict
from aiohttp import web

from openapi_server.models.query_response import QueryResponse
from openapi_server import util


async def get_concept_hmda(request: web.Request, concept) -> web.Response:
    """Get information about a particular concept in this dataset.

    

    :param concept: Name of concept
    :type concept: str

    """
    return web.Response(status=200)


async def get_dataset_hmda(request: web.Request, ) -> web.Response:
    """Get metadata for this dataset.

    


    """
    return web.Response(status=200)


async def get_slice_metadata_hmda(request: web.Request, slice) -> web.Response:
    """Get the metadata for a slice in this dataset.

    

    :param slice: Name of slice
    :type slice: str

    """
    return web.Response(status=200)


async def query_slice_hmda(request: web.Request, slice, select=None, where=None, group=None, limit=None, offset=None, order_by=None, param_callback=None) -> web.Response:
    """Query a slice in this dataset.

    

    :param slice: Name of slice
    :type slice: str
    :param select: Fields to return, separated by commas.
    :type select: str
    :param where: Conditions to search for in the slice, in SQL WHERE style.
    :type where: str
    :param group: Fields to group by, summarizing the data, separated by commas.
    :type group: str
    :param limit: Number of records to return, 100 by default. Enter 0 for no limit.
    :type limit: int
    :param offset: Number of records to skip.
    :type offset: int
    :param order_by: Fields to order by, separated by commas. ASC and DESC can be used to modify the order.
    :type order_by: str
    :param param_callback: JavaScript callback to invoke. Only useful with JSONP requests.
    :type param_callback: str

    """
    return web.Response(status=200)
