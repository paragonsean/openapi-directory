from typing import List, Dict
from aiohttp import web

from openapi_server.models.dataview_type import DataviewType
from openapi_server.models.response_data import ResponseData
from openapi_server.models.timespan_data import TimespanData
from openapi_server.models.timespan_model import TimespanModel
from openapi_server.models.timespan_type import TimespanType
from openapi_server.models.year_data import YearData
from openapi_server import util


async def get_namespace_data_by_timespan(request: web.Request, namespace, year, timespantype, timespan, dataview) -> web.Response:
    """Get namespace data for timespan

    Gets a list of URLs that can be used to download the pull data for the given namespace and timespan

    :param namespace: Namespace to fetch data for
    :type namespace: str
    :param year: Year to fetch data for
    :type year: int
    :param timespantype: Type of timespan to fetch data for
    :type timespantype: dict | bytes
    :param timespan: Timespan to fetch data for
    :type timespan: int
    :param dataview: Type of data to fetch
    :type dataview: dict | bytes

    """
    timespantype = .from_dict(timespantype)
    dataview = .from_dict(dataview)
    return web.Response(status=200)


async def get_namespace_timespan_metadata(request: web.Request, namespace, year, timespantype, timespan) -> web.Response:
    """Get namespace metadata for timespan

    Gets info about data for the given namespace and timespan

    :param namespace: Namespace to fetch data for
    :type namespace: str
    :param year: Year to fetch data for
    :type year: int
    :param timespantype: Type of timespan to fetch data for
    :type timespantype: dict | bytes
    :param timespan: Timespan to fetch data for
    :type timespan: int

    """
    timespantype = .from_dict(timespantype)
    return web.Response(status=200)


async def get_namespace_timespans(request: web.Request, namespace, year, timespantype) -> web.Response:
    """Get timespans with data

    Gets a list of timespans of the given type that have data for the given namespace and year

    :param namespace: Namespace to fetch data for
    :type namespace: str
    :param year: Year to fetch data for
    :type year: int
    :param timespantype: Type of timespan to fetch data for
    :type timespantype: dict | bytes

    """
    timespantype = .from_dict(timespantype)
    return web.Response(status=200)


async def get_namespace_years(request: web.Request, namespace) -> web.Response:
    """Get years with data

    Gets a list of years that have data for the given namespace

    :param namespace: Namespace to fetch data for
    :type namespace: str

    """
    return web.Response(status=200)
