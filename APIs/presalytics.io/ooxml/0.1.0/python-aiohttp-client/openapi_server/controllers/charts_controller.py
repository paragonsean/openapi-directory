from typing import List, Dict
from aiohttp import web

from openapi_server.models.chart_chart_data_dto import ChartChartDataDTO
from openapi_server.models.chart_charts import ChartCharts
from openapi_server.models.chart_charts_details import ChartChartsDetails
from openapi_server.models.child_objects import ChildObjects
from openapi_server.models.ooxml_dto import OoxmlDTO
from openapi_server.models.problem_details import ProblemDetails
from openapi_server import util


async def charts_charts_chartupdate_get_id(request: web.Request, id) -> web.Response:
    """Charts: Get Chart Data

    Gets a ChartDataDTO object, usually used for downstream analytics and chart updates

    :param id: 
    :type id: str
    :type id: str

    """
    return web.Response(status=200)


async def charts_charts_chartupdate_put_id(request: web.Request, id, body=None) -> web.Response:
    """Charts: Update Chart Data

    Simplifies chart update by allowing users to supply data via ChartDataDTO

    :param id: The Chart Id
    :type id: str
    :type id: str
    :param body: The ChartDataDto Object
    :type body: dict | bytes

    """
    body = ChartChartDataDTO.from_dict(body)
    return web.Response(status=200)


async def charts_charts_childobjects_get_id(request: web.Request, id) -> web.Response:
    """Charts: Get Dependent Objects Tree

    This endpoint is helpful for helping users and bots identify dependent objects to this Chart and retreive their corresponding metadata in order to make modifications to those objects in downstream operations.

    :param id: 
    :type id: str
    :type id: str

    """
    return web.Response(status=200)


async def charts_charts_details_get_id(request: web.Request, id) -> web.Response:
    """Charts: Get Details

    Returns object metadata and information about relative dependent objects 

    :param id: 
    :type id: str
    :type id: str

    """
    return web.Response(status=200)


async def charts_charts_get_id(request: web.Request, id) -> web.Response:
    """Charts: Get by Id

    Get by Id: Use this method to retrieve a Charts object by its primary key (id)

    :param id: An Id of the respository DTO elemennt
    :type id: str
    :type id: str

    """
    return web.Response(status=200)


async def charts_charts_openofficexml_get_id_updated(request: web.Request, id, updated=None) -> web.Response:
    """Charts: Get Underlying Xml

    Return the subset of the xml content from within the latest edited version of the OpenXmlDocument from this Chart object.  The returned xml data conforms to the [Ecma-376 standard](http://www.ecma-international.org/publications/standards/Ecma-376.htm).  Use this endpoint a starting point for building client-side extensions that modify Presalytics widgets containing Chart objects.

    :param id: 
    :type id: str
    :type id: str
    :param updated: Indicates whether API should return the orginal uploaded xml (false) or the actively updated version (true, default)
    :type updated: bool

    """
    return web.Response(status=200)


async def charts_charts_openofficexml_put_id(request: web.Request, id, body=None) -> web.Response:
    """Charts: Modify Underlying Xml

    Directly eidt the underlying xml of a Chart object within an OpenOpenXml (e.g. Excel, Powerpoint) document. This endpoint will validatate the submitted xml against the [Ecma-376 standard](http://www.ecma-international.org/publications/standards/Ecma-376.htm) prior to saving modification.  Invalid xml will rejected by this endpoint and a (hopefully) helpful error message will be returned.  Use this endpoint for client-side automation of modifications ot Chart objects.

    :param id: 
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = OoxmlDTO.from_dict(body)
    return web.Response(status=200)


async def charts_charts_svg_get_id_use_cache(request: web.Request, id, use_cache=None) -> web.Response:
    """Charts: Get Svg file

    This endpoint is helpful for rending this Chart as an svg or image object that can then be rendered in a story, dashboard or website.

    :param id: 
    :type id: str
    :type id: str
    :param use_cache: Indicates whether API should retrieve content from a cache if aviable (true, default), or force an update (false)
    :type use_cache: bool

    """
    return web.Response(status=200)
