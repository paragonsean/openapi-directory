from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_response import ApiResponse
from openapi_server.models.findings_inner import FindingsInner
from openapi_server.models.scan_definition import ScanDefinition
from openapi_server import util


async def clean_scan_page(request: web.Request, scan_id) -> web.Response:
    """Clean scan

    Clean scan identified by id.

    :param scan_id: Numeric ID of the scan to clean
    :type scan_id: int

    """
    return web.Response(status=200)


async def clean_scans_page(request: web.Request, ) -> web.Response:
    """Clean all scans

    Clean all current scans.


    """
    return web.Response(status=200)


async def get_default_page(request: web.Request, ) -> web.Response:
    """Index page

    Return index page


    """
    return web.Response(status=200)


async def get_finding_page(request: web.Request, scan_id) -> web.Response:
    """Get findings on finished scans

    Get findings on finished scans.

    :param scan_id: Numeric ID of the scan to get findings
    :type scan_id: int

    """
    return web.Response(status=200)


async def get_info_page(request: web.Request, ) -> web.Response:
    """Engine info page

    Return information on engine.


    """
    return web.Response(status=200)


async def get_liveness_page(request: web.Request, ) -> web.Response:
    """Liveness page

    Return liveness page


    """
    return web.Response(status=200)


async def get_readiness_page(request: web.Request, ) -> web.Response:
    """Readiness page

    Return liveness page


    """
    return web.Response(status=200)


async def get_test_page(request: web.Request, ) -> web.Response:
    """Test page

    Return test page


    """
    return web.Response(status=200)


async def reload_configuration_page(request: web.Request, ) -> web.Response:
    """Configuration reloading page

    Reload the configuration file.


    """
    return web.Response(status=200)


async def start_scan_page(request: web.Request, body) -> web.Response:
    """Start a new scan

    Start a new scan.

    :param body: 
    :type body: dict | bytes

    """
    body = ScanDefinition.from_dict(body)
    return web.Response(status=200)


async def status_scan_page(request: web.Request, scan_id) -> web.Response:
    """Status of a scan

    Status of a scan identified by id.

    :param scan_id: Numeric ID of the scan to get status
    :type scan_id: int

    """
    return web.Response(status=200)


async def status_scans_page(request: web.Request, ) -> web.Response:
    """Status on all scans

    Status all current scans.


    """
    return web.Response(status=200)


async def stop_scan_page(request: web.Request, scan_id) -> web.Response:
    """Stop a scan

    Stop a scan identified by id.

    :param scan_id: Numeric ID of the scan to stop
    :type scan_id: int

    """
    return web.Response(status=200)


async def stop_scans_page(request: web.Request, ) -> web.Response:
    """Stop all scans

    Stop all current scans.


    """
    return web.Response(status=200)
