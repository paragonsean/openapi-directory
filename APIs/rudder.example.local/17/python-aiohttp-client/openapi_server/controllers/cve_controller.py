from typing import List, Dict
from aiohttp import web

from openapi_server.models.check_cve200_response import CheckCVE200Response
from openapi_server.models.get_all_cve200_response import GetAllCve200Response
from openapi_server.models.get_cve_check_configuration200_response import GetCVECheckConfiguration200Response
from openapi_server.models.get_cve_list200_response import GetCVEList200Response
from openapi_server.models.get_cve_list_request import GetCVEListRequest
from openapi_server.models.get_cve200_response import GetCve200Response
from openapi_server.models.get_last_cve_check200_response import GetLastCVECheck200Response
from openapi_server.models.read_cv_efrom_fs200_response import ReadCVEfromFS200Response
from openapi_server.models.update_cve200_response import UpdateCVE200Response
from openapi_server.models.update_cve_check_configuration200_response import UpdateCVECheckConfiguration200Response
from openapi_server.models.update_cve_check_configuration_request import UpdateCVECheckConfigurationRequest
from openapi_server.models.update_cve_request import UpdateCVERequest
from openapi_server import util


async def check_cve(request: web.Request, ) -> web.Response:
    """Trigger a CVE check

    Trigger a CVE check


    """
    return web.Response(status=200)


async def get_all_cve(request: web.Request, ) -> web.Response:
    """Get all CVE details

    Get all CVE details


    """
    return web.Response(status=200)


async def get_cve(request: web.Request, cve_id) -> web.Response:
    """Get a CVE details

    Get a CVE details

    :param cve_id: Id of the CVE
    :type cve_id: str
    :type cve_id: str

    """
    return web.Response(status=200)


async def get_cve_check_configuration(request: web.Request, ) -> web.Response:
    """Get CVE check config

    Get CVE check config


    """
    return web.Response(status=200)


async def get_cve_list(request: web.Request, body=None) -> web.Response:
    """Get a list of CVE details

    Get CVE details, from a list passed as parameter

    :param body: 
    :type body: dict | bytes

    """
    body = GetCVEListRequest.from_dict(body)
    return web.Response(status=200)


async def get_last_cve_check(request: web.Request, group_id=None, node_id=None, cve_id=None, package=None, severity=None) -> web.Response:
    """Get last CVE check result

    Get last CVE check result

    :param group_id: Id of node groups you want to get from last CVE check
    :type group_id: str
    :param node_id: Id of nodes you want to get from last CVE check
    :type node_id: str
    :param cve_id: Id of CVE you want to get from last CVE check
    :type cve_id: str
    :param package: Name of packages you want to get from last CVE check
    :type package: str
    :param severity: Severity of the CVE you want to get from last CVE check
    :type severity: str

    """
    return web.Response(status=200)


async def read_cv_efrom_fs(request: web.Request, ) -> web.Response:
    """Update CVE database from file system

    Update CVE database from file system


    """
    return web.Response(status=200)


async def update_cve(request: web.Request, body=None) -> web.Response:
    """Update CVE database from remote source

    Update CVE database from remote source

    :param body: 
    :type body: dict | bytes

    """
    body = UpdateCVERequest.from_dict(body)
    return web.Response(status=200)


async def update_cve_check_configuration(request: web.Request, body=None) -> web.Response:
    """Update cve check config

    Update cve check config

    :param body: 
    :type body: dict | bytes

    """
    body = UpdateCVECheckConfigurationRequest.from_dict(body)
    return web.Response(status=200)
