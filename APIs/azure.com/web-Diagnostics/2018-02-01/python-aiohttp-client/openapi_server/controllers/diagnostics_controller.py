from typing import List, Dict
from aiohttp import web

from openapi_server.models.detector_response import DetectorResponse
from openapi_server.models.detector_response_collection import DetectorResponseCollection
from openapi_server.models.diagnostic_analysis import DiagnosticAnalysis
from openapi_server.models.diagnostic_analysis_collection import DiagnosticAnalysisCollection
from openapi_server.models.diagnostic_category import DiagnosticCategory
from openapi_server.models.diagnostic_category_collection import DiagnosticCategoryCollection
from openapi_server.models.diagnostic_detector_collection import DiagnosticDetectorCollection
from openapi_server.models.diagnostic_detector_response import DiagnosticDetectorResponse
from openapi_server.models.diagnostics_list_hosting_environment_detector_responses_default_response import DiagnosticsListHostingEnvironmentDetectorResponsesDefaultResponse
from openapi_server import util


async def diagnostics_execute_site_analysis(request: web.Request, resource_group_name, site_name, diagnostic_category, analysis_name, subscription_id, api_version, start_time=None, end_time=None, time_grain=None) -> web.Response:
    """Execute Analysis

    Execute Analysis

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param site_name: Site Name
    :type site_name: str
    :param diagnostic_category: Category Name
    :type diagnostic_category: str
    :param analysis_name: Analysis Resource Name
    :type analysis_name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param start_time: Start Time
    :type start_time: str
    :param end_time: End Time
    :type end_time: str
    :param time_grain: Time Grain
    :type time_grain: str

    """
    start_time = util.deserialize_datetime(start_time)
    end_time = util.deserialize_datetime(end_time)
    return web.Response(status=200)


async def diagnostics_execute_site_analysis_slot(request: web.Request, resource_group_name, site_name, diagnostic_category, analysis_name, slot, subscription_id, api_version, start_time=None, end_time=None, time_grain=None) -> web.Response:
    """Execute Analysis

    Execute Analysis

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param site_name: Site Name
    :type site_name: str
    :param diagnostic_category: Category Name
    :type diagnostic_category: str
    :param analysis_name: Analysis Resource Name
    :type analysis_name: str
    :param slot: Slot Name
    :type slot: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param start_time: Start Time
    :type start_time: str
    :param end_time: End Time
    :type end_time: str
    :param time_grain: Time Grain
    :type time_grain: str

    """
    start_time = util.deserialize_datetime(start_time)
    end_time = util.deserialize_datetime(end_time)
    return web.Response(status=200)


async def diagnostics_execute_site_detector(request: web.Request, resource_group_name, site_name, detector_name, diagnostic_category, subscription_id, api_version, start_time=None, end_time=None, time_grain=None) -> web.Response:
    """Execute Detector

    Execute Detector

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param site_name: Site Name
    :type site_name: str
    :param detector_name: Detector Resource Name
    :type detector_name: str
    :param diagnostic_category: Category Name
    :type diagnostic_category: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param start_time: Start Time
    :type start_time: str
    :param end_time: End Time
    :type end_time: str
    :param time_grain: Time Grain
    :type time_grain: str

    """
    start_time = util.deserialize_datetime(start_time)
    end_time = util.deserialize_datetime(end_time)
    return web.Response(status=200)


async def diagnostics_execute_site_detector_slot(request: web.Request, resource_group_name, site_name, detector_name, diagnostic_category, slot, subscription_id, api_version, start_time=None, end_time=None, time_grain=None) -> web.Response:
    """Execute Detector

    Execute Detector

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param site_name: Site Name
    :type site_name: str
    :param detector_name: Detector Resource Name
    :type detector_name: str
    :param diagnostic_category: Category Name
    :type diagnostic_category: str
    :param slot: Slot Name
    :type slot: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param start_time: Start Time
    :type start_time: str
    :param end_time: End Time
    :type end_time: str
    :param time_grain: Time Grain
    :type time_grain: str

    """
    start_time = util.deserialize_datetime(start_time)
    end_time = util.deserialize_datetime(end_time)
    return web.Response(status=200)


async def diagnostics_get_hosting_environment_detector_response(request: web.Request, resource_group_name, name, detector_name, subscription_id, api_version, start_time=None, end_time=None, time_grain=None) -> web.Response:
    """Get Hosting Environment Detector Response

    Get Hosting Environment Detector Response

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: App Service Environment Name
    :type name: str
    :param detector_name: Detector Resource Name
    :type detector_name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param start_time: Start Time
    :type start_time: str
    :param end_time: End Time
    :type end_time: str
    :param time_grain: Time Grain
    :type time_grain: str

    """
    start_time = util.deserialize_datetime(start_time)
    end_time = util.deserialize_datetime(end_time)
    return web.Response(status=200)


async def diagnostics_get_site_analysis(request: web.Request, resource_group_name, site_name, diagnostic_category, analysis_name, subscription_id, api_version) -> web.Response:
    """Get Site Analysis

    Get Site Analysis

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param site_name: Site Name
    :type site_name: str
    :param diagnostic_category: Diagnostic Category
    :type diagnostic_category: str
    :param analysis_name: Analysis Name
    :type analysis_name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def diagnostics_get_site_analysis_slot(request: web.Request, resource_group_name, site_name, diagnostic_category, analysis_name, slot, subscription_id, api_version) -> web.Response:
    """Get Site Analysis

    Get Site Analysis

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param site_name: Site Name
    :type site_name: str
    :param diagnostic_category: Diagnostic Category
    :type diagnostic_category: str
    :param analysis_name: Analysis Name
    :type analysis_name: str
    :param slot: Slot - optional
    :type slot: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def diagnostics_get_site_detector(request: web.Request, resource_group_name, site_name, diagnostic_category, detector_name, subscription_id, api_version) -> web.Response:
    """Get Detector

    Get Detector

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param site_name: Site Name
    :type site_name: str
    :param diagnostic_category: Diagnostic Category
    :type diagnostic_category: str
    :param detector_name: Detector Name
    :type detector_name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def diagnostics_get_site_detector_response(request: web.Request, resource_group_name, site_name, detector_name, subscription_id, api_version, start_time=None, end_time=None, time_grain=None) -> web.Response:
    """Get site detector response

    Get site detector response

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param site_name: Site Name
    :type site_name: str
    :param detector_name: Detector Resource Name
    :type detector_name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param start_time: Start Time
    :type start_time: str
    :param end_time: End Time
    :type end_time: str
    :param time_grain: Time Grain
    :type time_grain: str

    """
    start_time = util.deserialize_datetime(start_time)
    end_time = util.deserialize_datetime(end_time)
    return web.Response(status=200)


async def diagnostics_get_site_detector_response_slot(request: web.Request, resource_group_name, site_name, detector_name, slot, subscription_id, api_version, start_time=None, end_time=None, time_grain=None) -> web.Response:
    """Get site detector response

    Get site detector response

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param site_name: Site Name
    :type site_name: str
    :param detector_name: Detector Resource Name
    :type detector_name: str
    :param slot: Slot Name
    :type slot: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param start_time: Start Time
    :type start_time: str
    :param end_time: End Time
    :type end_time: str
    :param time_grain: Time Grain
    :type time_grain: str

    """
    start_time = util.deserialize_datetime(start_time)
    end_time = util.deserialize_datetime(end_time)
    return web.Response(status=200)


async def diagnostics_get_site_detector_slot(request: web.Request, resource_group_name, site_name, diagnostic_category, detector_name, slot, subscription_id, api_version) -> web.Response:
    """Get Detector

    Get Detector

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param site_name: Site Name
    :type site_name: str
    :param diagnostic_category: Diagnostic Category
    :type diagnostic_category: str
    :param detector_name: Detector Name
    :type detector_name: str
    :param slot: Slot Name
    :type slot: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def diagnostics_get_site_diagnostic_category(request: web.Request, resource_group_name, site_name, diagnostic_category, subscription_id, api_version) -> web.Response:
    """Get Diagnostics Category

    Get Diagnostics Category

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param site_name: Site Name
    :type site_name: str
    :param diagnostic_category: Diagnostic Category
    :type diagnostic_category: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def diagnostics_get_site_diagnostic_category_slot(request: web.Request, resource_group_name, site_name, diagnostic_category, slot, subscription_id, api_version) -> web.Response:
    """Get Diagnostics Category

    Get Diagnostics Category

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param site_name: Site Name
    :type site_name: str
    :param diagnostic_category: Diagnostic Category
    :type diagnostic_category: str
    :param slot: Slot Name
    :type slot: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def diagnostics_list_hosting_environment_detector_responses(request: web.Request, resource_group_name, name, subscription_id, api_version) -> web.Response:
    """List Hosting Environment Detector Responses

    List Hosting Environment Detector Responses

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Site Name
    :type name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def diagnostics_list_site_analyses(request: web.Request, resource_group_name, site_name, diagnostic_category, subscription_id, api_version) -> web.Response:
    """Get Site Analyses

    Get Site Analyses

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param site_name: Site Name
    :type site_name: str
    :param diagnostic_category: Diagnostic Category
    :type diagnostic_category: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def diagnostics_list_site_analyses_slot(request: web.Request, resource_group_name, site_name, diagnostic_category, slot, subscription_id, api_version) -> web.Response:
    """Get Site Analyses

    Get Site Analyses

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param site_name: Site Name
    :type site_name: str
    :param diagnostic_category: Diagnostic Category
    :type diagnostic_category: str
    :param slot: Slot Name
    :type slot: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def diagnostics_list_site_detector_responses(request: web.Request, resource_group_name, site_name, subscription_id, api_version) -> web.Response:
    """List Site Detector Responses

    List Site Detector Responses

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param site_name: Site Name
    :type site_name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def diagnostics_list_site_detector_responses_slot(request: web.Request, resource_group_name, site_name, slot, subscription_id, api_version) -> web.Response:
    """List Site Detector Responses

    List Site Detector Responses

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param site_name: Site Name
    :type site_name: str
    :param slot: Slot Name
    :type slot: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def diagnostics_list_site_detectors(request: web.Request, resource_group_name, site_name, diagnostic_category, subscription_id, api_version) -> web.Response:
    """Get Detectors

    Get Detectors

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param site_name: Site Name
    :type site_name: str
    :param diagnostic_category: Diagnostic Category
    :type diagnostic_category: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def diagnostics_list_site_detectors_slot(request: web.Request, resource_group_name, site_name, diagnostic_category, slot, subscription_id, api_version) -> web.Response:
    """Get Detectors

    Get Detectors

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param site_name: Site Name
    :type site_name: str
    :param diagnostic_category: Diagnostic Category
    :type diagnostic_category: str
    :param slot: Slot Name
    :type slot: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def diagnostics_list_site_diagnostic_categories(request: web.Request, resource_group_name, site_name, subscription_id, api_version) -> web.Response:
    """Get Diagnostics Categories

    Get Diagnostics Categories

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param site_name: Site Name
    :type site_name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def diagnostics_list_site_diagnostic_categories_slot(request: web.Request, resource_group_name, site_name, slot, subscription_id, api_version) -> web.Response:
    """Get Diagnostics Categories

    Get Diagnostics Categories

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param site_name: Site Name
    :type site_name: str
    :param slot: Slot Name
    :type slot: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)
