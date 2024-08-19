from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def get_capabilities(request: web.Request, version_number, service, request, version=None) -> web.Response:
    """GetCapabilities

    The GetCapabilities call is part of TomTom&#39;s implementation of version 1.1.1 the Web Map Service (WMS). It provides descriptions of the other calls that are available in the implementation.

    :param version_number: 
    :type version_number: int
    :param service: 
    :type service: str
    :param request: 
    :type request: str
    :param version: WMS service version
    :type version: str

    """
    return web.Response(status=200)


async def map_version_number_wmts_key_wmts_version_wmts_capabilities_xml_get(request: web.Request, version_number, key, wmts_version) -> web.Response:
    """WMTS

    The WMTS GetCapabilities call implements version 1.0.0 of the &lt;a href&#x3D;\&quot;http://www.opengeospatial.org/standards/wmts\&quot;&gt;Web Map Tile Service&lt;/a&gt; (WMTS) standard. It returns metadata that allows compatible calling systems to construct calls to TomTom&#39;s raster map tile service. See the &lt;a href&#x3D;\&quot;/maps-api/maps-api-documentation-raster/wmts\&quot;&gt;documentation&lt;/a&gt; for more information on WMTS.

    :param version_number: Version of the service to call. The current version is 1
    :type version_number: int
    :param key: Your API key for calling this service.
    :type key: str
    :param wmts_version: 
    :type wmts_version: str

    """
    return web.Response(status=200)
