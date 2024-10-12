from typing import List, Dict
from aiohttp import web

from openapi_server.models.package_info import PackageInfo
from openapi_server.models.problem_details import ProblemDetails
from openapi_server.models.repository_info import RepositoryInfo
from openapi_server import util


async def cancel_package_installation(request: web.Request, package_id) -> web.Response:
    """Cancels a package installation.

    

    :param package_id: Installation Id.
    :type package_id: str
    :type package_id: str

    """
    return web.Response(status=200)


async def get_package_info(request: web.Request, name, assembly_guid=None) -> web.Response:
    """Gets a package by name or assembly GUID.

    

    :param name: The name of the package.
    :type name: str
    :param assembly_guid: The GUID of the associated assembly.
    :type assembly_guid: str
    :type assembly_guid: str

    """
    return web.Response(status=200)


async def get_packages(request: web.Request, ) -> web.Response:
    """Gets available packages.

    


    """
    return web.Response(status=200)


async def get_repositories(request: web.Request, ) -> web.Response:
    """Gets all package repositories.

    


    """
    return web.Response(status=200)


async def install_package(request: web.Request, name, assembly_guid=None, version=None, repository_url=None) -> web.Response:
    """Installs a package.

    

    :param name: Package name.
    :type name: str
    :param assembly_guid: GUID of the associated assembly.
    :type assembly_guid: str
    :type assembly_guid: str
    :param version: Optional version. Defaults to latest version.
    :type version: str
    :param repository_url: Optional. Specify the repository to install from.
    :type repository_url: str

    """
    return web.Response(status=200)


async def set_repositories(request: web.Request, body=None) -> web.Response:
    """Sets the enabled and existing package repositories.

    

    :param body: The list of package repositories.
    :type body: list | bytes

    """
    body = [RepositoryInfo.from_dict(d) for d in body]
    return web.Response(status=200)
