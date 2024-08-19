from typing import List, Dict
from aiohttp import web

from openapi_server.models.rest_lookups_icis_law_sections_get200_response import RestLookupsIcisLawSectionsGet200Response
from openapi_server import util


async def rest_lookups_icis_law_sections_get(request: web.Request, output=None, param_callback=None, statute_code=None, status_flag=None, search_term=None, search_code=None, sort_order=None) -> web.Response:
    """ECHO ICIS Law Sections Lookup Service

    Returns the ICIS Law Section Descriptions.

    :param output: Output Format Flag.  Enter one of the following keywords: - JSON &#x3D; Data model formatted as Javascript Object Notation (default). - JSONP &#x3D; Data model formatted as Javascript Object Notation with Padding.   - XML &#x3D; Data model formatted as Extensible Markup Language.
    :type output: str
    :param param_callback: JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
    :type param_callback: str
    :param statute_code: 
    :type statute_code: str
    :param status_flag: 
    :type status_flag: str
    :param search_term: Enter a partial or complete search phrase or word.
    :type search_term: str
    :param search_code: Enter a partial or complete code value.
    :type search_code: str
    :param sort_order: 
    :type sort_order: 

    """
    return web.Response(status=200)


async def rest_lookups_icis_law_sections_post(request: web.Request, output=None, param_callback=None, statute_code=None, status_flag=None, search_term=None, search_code=None, sort_order=None) -> web.Response:
    """ECHO ICIS Law Sections Lookup Service

    Returns the ICIS Law Section Descriptions.

    :param output: Output Format Flag.  Enter one of the following keywords: - JSON &#x3D; Data model formatted as Javascript Object Notation (default). - JSONP &#x3D; Data model formatted as Javascript Object Notation with Padding.   - XML &#x3D; Data model formatted as Extensible Markup Language.
    :type output: str
    :param param_callback: JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
    :type param_callback: str
    :param statute_code: 
    :type statute_code: str
    :param status_flag: 
    :type status_flag: str
    :param search_term: Enter a partial or complete search phrase or word.
    :type search_term: str
    :param search_code: Enter a partial or complete code value.
    :type search_code: str
    :param sort_order: 
    :type sort_order: 

    """
    return web.Response(status=200)
