from typing import List, Dict
from aiohttp import web

from openapi_server.models.rest_lookups_cwa_parameters_get200_response import RestLookupsCwaParametersGet200Response
from openapi_server import util


async def rest_lookups_cwa_parameters_get(request: web.Request, output=None, param_callback=None, search_term=None, search_code=None) -> web.Response:
    """ECHO CWA Parameter Lookup Service

    Look up Clean Water Act parameter codes and descriptions in the Integrated Compliance Information System - National Pollutant Discharge Elimination System (ICIS-NPDES) by code or term.

    :param output: Output Format Flag.  Enter one of the following keywords: - JSON &#x3D; Data model formatted as Javascript Object Notation (default). - JSONP &#x3D; Data model formatted as Javascript Object Notation with Padding.   - XML &#x3D; Data model formatted as Extensible Markup Language.
    :type output: str
    :param param_callback: JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
    :type param_callback: str
    :param search_term: Enter a partial or complete search phrase or word.
    :type search_term: str
    :param search_code: Enter a partial or complete code value.
    :type search_code: str

    """
    return web.Response(status=200)


async def rest_lookups_cwa_parameters_post(request: web.Request, output=None, param_callback=None, search_term=None, search_code=None) -> web.Response:
    """ECHO CWA Parameter Lookup Service

    Look up Clean Water Act parameter codes and descriptions in the Integrated Compliance Information System - National Pollutant Discharge Elimination System (ICIS-NPDES) by code or term.

    :param output: Output Format Flag.  Enter one of the following keywords: - JSON &#x3D; Data model formatted as Javascript Object Notation (default). - JSONP &#x3D; Data model formatted as Javascript Object Notation with Padding.   - XML &#x3D; Data model formatted as Extensible Markup Language.
    :type output: str
    :param param_callback: JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
    :type param_callback: str
    :param search_term: Enter a partial or complete search phrase or word.
    :type search_term: str
    :param search_code: Enter a partial or complete code value.
    :type search_code: str

    """
    return web.Response(status=200)
