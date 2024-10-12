from typing import List, Dict
from aiohttp import web

from openapi_server.models.auto_import_configuration import AutoImportConfiguration
from openapi_server.models.beez_up_common_error_response_message import BeezUPCommonErrorResponseMessage
from openapi_server.models.configure_auto_import_interval_request import ConfigureAutoImportIntervalRequest
from openapi_server.models.links_importation_get_importation_monitoring_link import LinksImportationGetImportationMonitoringLink
from openapi_server.models.schedule_auto_import_request import ScheduleAutoImportRequest
from openapi_server import util


async def auto_configure_auto_import_interval(request: web.Request, store_id, body) -> web.Response:
    """Configure Auto Import Interval

    

    :param store_id: Your store identifier
    :type store_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = ConfigureAutoImportIntervalRequest.from_dict(body)
    return web.Response(status=200)


async def auto_delete_auto_import(request: web.Request, store_id) -> web.Response:
    """Delete Auto Import

    

    :param store_id: Your store identifier
    :type store_id: str

    """
    return web.Response(status=200)


async def auto_get_auto_import_configuration(request: web.Request, store_id) -> web.Response:
    """Get the auto import configuration

    

    :param store_id: Your store identifier
    :type store_id: str

    """
    return web.Response(status=200)


async def auto_pause_auto_import(request: web.Request, store_id) -> web.Response:
    """Pause Auto Import

    

    :param store_id: Your store identifier
    :type store_id: str

    """
    return web.Response(status=200)


async def auto_resume_auto_import(request: web.Request, store_id) -> web.Response:
    """Resume Auto Import

    

    :param store_id: Your store identifier
    :type store_id: str

    """
    return web.Response(status=200)


async def auto_schedule_auto_import(request: web.Request, store_id, body) -> web.Response:
    """Configure Auto Import Schedules

    

    :param store_id: Your store identifier
    :type store_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = ScheduleAutoImportRequest.from_dict(body)
    return web.Response(status=200)


async def auto_start_auto_import(request: web.Request, store_id) -> web.Response:
    """Start Auto Import Manually

    

    :param store_id: Your store identifier
    :type store_id: str

    """
    return web.Response(status=200)


async def importation_activate_auto_import(request: web.Request, store_id) -> web.Response:
    """Activate the auto importation of the last successful manual catalog importation.

    Once you have made your fist manual catalog importation with success, you can call this operation to import it automatically. No parameter required, we know which one it is.

    :param store_id: Your store identifier
    :type store_id: str

    """
    return web.Response(status=200)
