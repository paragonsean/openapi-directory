from typing import List, Dict
from aiohttp import web

from openapi_server.models.sdw_rest_services_metadata_get200_response import SdwRestServicesMetadataGet200Response
from openapi_server import util


async def sdw_rest_services_metadata_get(request: web.Request, output=None, param_callback=None) -> web.Response:
    """Safe Drinking Water Act (SDWA) Metadata Service

    Returns the JSON Object Name and ColumnId for usage with the qcolumns parameter for get_systems endpoint.

    :param output: Output Format Flag.  Enter one of the following keywords: - JSON &#x3D; Data model formatted as Javascript Object Notation (default). - JSONP &#x3D; Data model formatted as Javascript Object Notation with Padding.   - XML &#x3D; Data model formatted as Extensible Markup Language.
    :type output: str
    :param param_callback: JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
    :type param_callback: str

    """
    return web.Response(status=200)


async def sdw_rest_services_metadata_post(request: web.Request, output=None, param_callback=None) -> web.Response:
    """Safe Drinking Water Act (SDWA) Metadata Service

    Returns the JSON Object Name and ColumnId for usage with the qcolumns parameter for get_systems endpoint.

    :param output: Output Format Flag.  Enter one of the following keywords: - JSON &#x3D; Data model formatted as Javascript Object Notation (default). - JSONP &#x3D; Data model formatted as Javascript Object Notation with Padding.   - XML &#x3D; Data model formatted as Extensible Markup Language.
    :type output: str
    :param param_callback: JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
    :type param_callback: str

    """
    return web.Response(status=200)
