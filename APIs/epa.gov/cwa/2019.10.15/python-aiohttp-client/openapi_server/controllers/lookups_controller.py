from typing import List, Dict
from aiohttp import web

from openapi_server.models.rest_lookups_bp_tribes_get200_response import RestLookupsBpTribesGet200Response
from openapi_server.models.rest_lookups_cwa_parameters_get200_response import RestLookupsCwaParametersGet200Response
from openapi_server.models.rest_lookups_cwa_pollutants_get200_response import RestLookupsCwaPollutantsGet200Response
from openapi_server.models.rest_lookups_federal_agencies_get200_response import RestLookupsFederalAgenciesGet200Response
from openapi_server.models.rest_lookups_icis_inspection_types_get200_response import RestLookupsIcisInspectionTypesGet200Response
from openapi_server.models.rest_lookups_icis_law_sections_get200_response import RestLookupsIcisLawSectionsGet200Response
from openapi_server.models.rest_lookups_naics_codes_get200_response import RestLookupsNaicsCodesGet200Response
from openapi_server.models.rest_lookups_npdes_parameters_get200_response import RestLookupsNpdesParametersGet200Response
from openapi_server.models.rest_lookups_wbd_code_lu_get200_response import RestLookupsWbdCodeLuGet200Response
from openapi_server.models.rest_lookups_wbd_name_lu_get200_response import RestLookupsWbdNameLuGet200Response
from openapi_server import util


async def rest_lookups_bp_tribes_get(request: web.Request, output=None, param_callback=None, search_term=None, search_code=None) -> web.Response:
    """ECHO BP Tribes Lookup Service

    Returns the EPA Standard Indian Tribes and Native Alaskan Villages tribal_id and tribe_name.

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


async def rest_lookups_bp_tribes_post(request: web.Request, output=None, param_callback=None, search_term=None, search_code=None) -> web.Response:
    """ECHO BP Tribes Lookup Service

    Returns the EPA Standard Indian Tribes and Native Alaskan Villages tribal_id and tribe_name.

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


async def rest_lookups_cwa_pollutants_get(request: web.Request, output=None, param_callback=None, search_term=None, search_code=None) -> web.Response:
    """ECHO CWA Pollutants Lookup Service

    Look up Clean Water Act pollutants by name

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


async def rest_lookups_cwa_pollutants_post(request: web.Request, output=None, param_callback=None, search_term=None, search_code=None) -> web.Response:
    """ECHO CWA Pollutants Lookup Service

    Look up Clean Water Act pollutants by name

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


async def rest_lookups_federal_agencies_get(request: web.Request, output=None, param_callback=None, search_term=None, search_code=None) -> web.Response:
    """ECHO Federal Agency Lookup Service

    Look up Federal Agency Code

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


async def rest_lookups_federal_agencies_post(request: web.Request, output=None, param_callback=None, search_term=None, search_code=None) -> web.Response:
    """ECHO Federal Agency Lookup Service

    Look up Federal Agency Code

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


async def rest_lookups_icis_inspection_types_get(request: web.Request, output=None, param_callback=None, search_term=None, search_code=None) -> web.Response:
    """ECHO ICIS NPDES Inspection Types Lookup Service

    Returns the ICIS NPDES Compliance Monitoring Type Code and Description.

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


async def rest_lookups_icis_inspection_types_post(request: web.Request, output=None, param_callback=None, search_term=None, search_code=None) -> web.Response:
    """ECHO ICIS NPDES Inspection Types Lookup Service

    Returns the ICIS NPDES Compliance Monitoring Type Code and Description.

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


async def rest_lookups_icis_law_sections_get(request: web.Request, output=None, param_callback=None, statute_code=None, status_flag=None, search_term=None, search_code=None, sort_order=None) -> web.Response:
    """ECHO ICIS NPDES Law Sections Lookup Service

    Returns the ICIS NPDES Law Section Descriptions.

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
    """ECHO ICIS NPDES Law Sections Lookup Service

    Returns the ICIS NPDES Law Section Descriptions.

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


async def rest_lookups_naics_codes_get(request: web.Request, output=None, param_callback=None, search_term=None, search_code=None) -> web.Response:
    """ECHO NAICS Codes Lookup Service

    

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


async def rest_lookups_naics_codes_post(request: web.Request, output=None, param_callback=None, search_term=None, search_code=None) -> web.Response:
    """ECHO NAICS Codes Lookup Service

    

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


async def rest_lookups_npdes_parameters_get(request: web.Request, output=None, param_callback=None, search_term=None) -> web.Response:
    """ECHO NPDES Parameters Lookup Service

    ICIS Limit Parameter Code and Name lookup based on the supply of a partial parameter name. (NPDES &#x3D; National Pollutant Discharge Elimination System)

    :param output: Output Format Flag.  Enter one of the following keywords: - JSON &#x3D; Data model formatted as Javascript Object Notation (default). - JSONP &#x3D; Data model formatted as Javascript Object Notation with Padding.   - XML &#x3D; Data model formatted as Extensible Markup Language.
    :type output: str
    :param param_callback: JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
    :type param_callback: str
    :param search_term: Enter a partial or complete search phrase or word.
    :type search_term: str

    """
    return web.Response(status=200)


async def rest_lookups_npdes_parameters_post(request: web.Request, output=None, param_callback=None, search_term=None) -> web.Response:
    """ECHO NPDES Parameters Lookup Service

    ICIS Limit Parameter Code and Name lookup based on the supply of a partial parameter name. (NPDES &#x3D; National Pollutant Discharge Elimination System)

    :param output: Output Format Flag.  Enter one of the following keywords: - JSON &#x3D; Data model formatted as Javascript Object Notation (default). - JSONP &#x3D; Data model formatted as Javascript Object Notation with Padding.   - XML &#x3D; Data model formatted as Extensible Markup Language.
    :type output: str
    :param param_callback: JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
    :type param_callback: str
    :param search_term: Enter a partial or complete search phrase or word.
    :type search_term: str

    """
    return web.Response(status=200)


async def rest_lookups_wbd_code_lu_get(request: web.Request, output=None, param_callback=None, wbd_code=None, wbd_level=None) -> web.Response:
    """ECHO WBD Code Lookup Service

    USGS Watershed Boundary Dataset (WBD) Name lookup based on a supplied WBD Code and Watershed Level

    :param output: Output Format Flag.  Enter one of the following keywords: - JSON &#x3D; Data model formatted as Javascript Object Notation (default). - JSONP &#x3D; Data model formatted as Javascript Object Notation with Padding.   - XML &#x3D; Data model formatted as Extensible Markup Language.
    :type output: str
    :param param_callback: JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
    :type param_callback: str
    :param wbd_code: Two-digit watershed code [Hydrologic Unit Code (HUC)].
    :type wbd_code: str
    :param wbd_level: The number of digits of the watershed code [Hydrologic Unit Code (HUC)] returned in the ValueCode. Must be an even number between 4 and 12.
    :type wbd_level: str

    """
    return web.Response(status=200)


async def rest_lookups_wbd_code_lu_post(request: web.Request, output=None, param_callback=None, wbd_code=None, wbd_level=None) -> web.Response:
    """ECHO WBD Code Lookup Service

    USGS Watershed Boundary Dataset (WBD) Name lookup based on a supplied WBD Code and Watershed Level

    :param output: Output Format Flag.  Enter one of the following keywords: - JSON &#x3D; Data model formatted as Javascript Object Notation (default). - JSONP &#x3D; Data model formatted as Javascript Object Notation with Padding.   - XML &#x3D; Data model formatted as Extensible Markup Language.
    :type output: str
    :param param_callback: JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
    :type param_callback: str
    :param wbd_code: Two-digit watershed code [Hydrologic Unit Code (HUC)].
    :type wbd_code: str
    :param wbd_level: The number of digits of the watershed code [Hydrologic Unit Code (HUC)] returned in the ValueCode. Must be an even number between 4 and 12.
    :type wbd_level: str

    """
    return web.Response(status=200)


async def rest_lookups_wbd_name_lu_get(request: web.Request, wbd_name, output=None, param_callback=None, wbd_level=None) -> web.Response:
    """ECHO WBD Name Lookup Service

    USGS Watershed Boundary Dataset (WBD) Code lookup based on a supplied WBD Name and Watershed Level

    :param wbd_name: Watershed Name Filter.
    :type wbd_name: str
    :param output: Output Format Flag.  Enter one of the following keywords: - JSON &#x3D; Data model formatted as Javascript Object Notation (default). - JSONP &#x3D; Data model formatted as Javascript Object Notation with Padding.   - XML &#x3D; Data model formatted as Extensible Markup Language.
    :type output: str
    :param param_callback: JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
    :type param_callback: str
    :param wbd_level: The number of digits of the watershed code [Hydrologic Unit Code (HUC)] returned in the ValueCode. Must be an even number between 4 and 12.
    :type wbd_level: str

    """
    return web.Response(status=200)


async def rest_lookups_wbd_name_lu_post(request: web.Request, wbd_name, output=None, param_callback=None, wbd_level=None) -> web.Response:
    """ECHO WBD Name Lookup Service

    USGS Watershed Boundary Dataset (WBD) Code lookup based on a supplied WBD Name and Watershed Level

    :param wbd_name: Watershed Name Filter.
    :type wbd_name: str
    :param output: Output Format Flag.  Enter one of the following keywords: - JSON &#x3D; Data model formatted as Javascript Object Notation (default). - JSONP &#x3D; Data model formatted as Javascript Object Notation with Padding.   - XML &#x3D; Data model formatted as Extensible Markup Language.
    :type output: str
    :param param_callback: JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
    :type param_callback: str
    :param wbd_level: The number of digits of the watershed code [Hydrologic Unit Code (HUC)] returned in the ValueCode. Must be an even number between 4 and 12.
    :type wbd_level: str

    """
    return web.Response(status=200)
