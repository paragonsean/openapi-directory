from typing import List, Dict
from aiohttp import web

from openapi_server.models.eff_rest_services_get_effluent_chart_get200_response import EffRestServicesGetEffluentChartGet200Response
from openapi_server.models.eff_rest_services_get_summary_chart_get200_response import EffRestServicesGetSummaryChartGet200Response
from openapi_server import util


async def eff_rest_services_download_effluent_chart_get(request: web.Request, p_id, outfall=None, parameter_code=None, start_date=None, end_date=None) -> web.Response:
    """Effluent Charts Download Service

    Downloads tabular Discharge Monitoring Report (DMR) and compliance data for one NPDES permit as a CSV.

    :param p_id: Identifier for the service.
    :type p_id: str
    :param outfall: Three-character code that identifies the point of discharge (e.g., pipe or outfall) for a facility. A single NPDES ID may have multiple points of discharge.
    :type outfall: str
    :param parameter_code: Five-digit numeric code identifying the parameter. See Parameter Lookup documentation for a complete list of codes.
    :type parameter_code: str
    :param start_date: The start date (mm/dd/yyyy) for the date range of interest. Must be used in conjunction with end_date. If start_date and end_date are not specified, the service will return the last three years of data.
    :type start_date: str
    :param end_date: The end date (mm/dd/yyyy) for the date range of interest. Must be used in conjunction with start_date. If start_date and end_date are not specified, the service will return the last three years of data.
    :type end_date: str

    """
    return web.Response(status=200)


async def eff_rest_services_download_effluent_chart_post(request: web.Request, p_id, outfall=None, parameter_code=None, start_date=None, end_date=None) -> web.Response:
    """Effluent Charts Download Service

    Downloads tabular Discharge Monitoring Report (DMR) and compliance data for one NPDES permit as a CSV.

    :param p_id: Identifier for the service.
    :type p_id: str
    :param outfall: Three-character code that identifies the point of discharge (e.g., pipe or outfall) for a facility. A single NPDES ID may have multiple points of discharge.
    :type outfall: str
    :param parameter_code: Five-digit numeric code identifying the parameter. See Parameter Lookup documentation for a complete list of codes.
    :type parameter_code: str
    :param start_date: The start date (mm/dd/yyyy) for the date range of interest. Must be used in conjunction with end_date. If start_date and end_date are not specified, the service will return the last three years of data.
    :type start_date: str
    :param end_date: The end date (mm/dd/yyyy) for the date range of interest. Must be used in conjunction with start_date. If start_date and end_date are not specified, the service will return the last three years of data.
    :type end_date: str

    """
    return web.Response(status=200)


async def eff_rest_services_get_effluent_chart_get(request: web.Request, p_id, outfall=None, parameter_code=None, start_date=None, end_date=None, output=None, param_callback=None) -> web.Response:
    """Detailed Effluent Chart Service

    Discharge Monitoring Report (DMR) data supporting each effluent chart for one NPDES permit. Includes Discharge Monitoring Reports and NPDES Violations.   

    :param p_id: Identifier for the service.
    :type p_id: str
    :param outfall: Three-character code that identifies the point of discharge (e.g., pipe or outfall) for a facility. A single NPDES ID may have multiple points of discharge.
    :type outfall: str
    :param parameter_code: Five-digit numeric code identifying the parameter. See Parameter Lookup documentation for a complete list of codes.
    :type parameter_code: str
    :param start_date: The start date (mm/dd/yyyy) for the date range of interest. Must be used in conjunction with end_date. If start_date and end_date are not specified, the service will return the last three years of data.
    :type start_date: str
    :param end_date: The end date (mm/dd/yyyy) for the date range of interest. Must be used in conjunction with start_date. If start_date and end_date are not specified, the service will return the last three years of data.
    :type end_date: str
    :param output: Output Format Flag.  Enter one of the following keywords: - JSON &#x3D; Data model formatted as Javascript Object Notation (default). - JSONP &#x3D; Data model formatted as Javascript Object Notation with Padding.   - XML &#x3D; Data model formatted as Extensible Markup Language.
    :type output: str
    :param param_callback: JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
    :type param_callback: str

    """
    return web.Response(status=200)


async def eff_rest_services_get_effluent_chart_post(request: web.Request, p_id, outfall=None, parameter_code=None, start_date=None, end_date=None, output=None, param_callback=None) -> web.Response:
    """Detailed Effluent Chart Service

    Discharge Monitoring Report (DMR) data supporting each effluent chart for one NPDES permit. Includes Discharge Monitoring Reports and NPDES Violations.   

    :param p_id: Identifier for the service.
    :type p_id: str
    :param outfall: Three-character code that identifies the point of discharge (e.g., pipe or outfall) for a facility. A single NPDES ID may have multiple points of discharge.
    :type outfall: str
    :param parameter_code: Five-digit numeric code identifying the parameter. See Parameter Lookup documentation for a complete list of codes.
    :type parameter_code: str
    :param start_date: The start date (mm/dd/yyyy) for the date range of interest. Must be used in conjunction with end_date. If start_date and end_date are not specified, the service will return the last three years of data.
    :type start_date: str
    :param end_date: The end date (mm/dd/yyyy) for the date range of interest. Must be used in conjunction with start_date. If start_date and end_date are not specified, the service will return the last three years of data.
    :type end_date: str
    :param output: Output Format Flag.  Enter one of the following keywords: - JSON &#x3D; Data model formatted as Javascript Object Notation (default). - JSONP &#x3D; Data model formatted as Javascript Object Notation with Padding.   - XML &#x3D; Data model formatted as Extensible Markup Language.
    :type output: str
    :param param_callback: JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
    :type param_callback: str

    """
    return web.Response(status=200)


async def eff_rest_services_get_summary_chart_get(request: web.Request, p_id, output=None, param_callback=None, start_date=None, end_date=None) -> web.Response:
    """Summary Effluent Chart Service

    Summary of compliance status each outfall and parameter for one NPDES permit. Provides the current compliance status and overall compliance status for the date range of interest. This service supports the Summary Matrix on the Effluent Charts.

    :param p_id: Identifier for the service.
    :type p_id: str
    :param output: Output Format Flag.  Enter one of the following keywords: - JSON &#x3D; Data model formatted as Javascript Object Notation (default). - JSONP &#x3D; Data model formatted as Javascript Object Notation with Padding.   - XML &#x3D; Data model formatted as Extensible Markup Language.
    :type output: str
    :param param_callback: JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
    :type param_callback: str
    :param start_date: The start date (mm/dd/yyyy) for the date range of interest. Must be used in conjunction with end_date. If start_date and end_date are not specified, the service will return the last three years of data.
    :type start_date: str
    :param end_date: The end date (mm/dd/yyyy) for the date range of interest. Must be used in conjunction with start_date. If start_date and end_date are not specified, the service will return the last three years of data.
    :type end_date: str

    """
    return web.Response(status=200)


async def eff_rest_services_get_summary_chart_post(request: web.Request, p_id, output=None, param_callback=None, start_date=None, end_date=None) -> web.Response:
    """Summary Effluent Chart Service

    Summary of compliance status each outfall and parameter for one NPDES permit. Provides the current compliance status and overall compliance status for the date range of interest. This service supports the Summary Matrix on the Effluent Charts.

    :param p_id: Identifier for the service.
    :type p_id: str
    :param output: Output Format Flag.  Enter one of the following keywords: - JSON &#x3D; Data model formatted as Javascript Object Notation (default). - JSONP &#x3D; Data model formatted as Javascript Object Notation with Padding.   - XML &#x3D; Data model formatted as Extensible Markup Language.
    :type output: str
    :param param_callback: JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
    :type param_callback: str
    :param start_date: The start date (mm/dd/yyyy) for the date range of interest. Must be used in conjunction with end_date. If start_date and end_date are not specified, the service will return the last three years of data.
    :type start_date: str
    :param end_date: The end date (mm/dd/yyyy) for the date range of interest. Must be used in conjunction with start_date. If start_date and end_date are not specified, the service will return the last three years of data.
    :type end_date: str

    """
    return web.Response(status=200)
