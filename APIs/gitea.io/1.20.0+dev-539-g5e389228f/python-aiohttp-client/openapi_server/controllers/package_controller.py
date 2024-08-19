from typing import List, Dict
from aiohttp import web

from openapi_server.models.package import Package
from openapi_server.models.package_file import PackageFile
from openapi_server import util


async def delete_package(request: web.Request, owner, type, name, version) -> web.Response:
    """Delete a package

    

    :param owner: owner of the package
    :type owner: str
    :param type: type of the package
    :type type: str
    :param name: name of the package
    :type name: str
    :param version: version of the package
    :type version: str

    """
    return web.Response(status=200)


async def get_package(request: web.Request, owner, type, name, version) -> web.Response:
    """Gets a package

    

    :param owner: owner of the package
    :type owner: str
    :param type: type of the package
    :type type: str
    :param name: name of the package
    :type name: str
    :param version: version of the package
    :type version: str

    """
    return web.Response(status=200)


async def list_package_files(request: web.Request, owner, type, name, version) -> web.Response:
    """Gets all files of a package

    

    :param owner: owner of the package
    :type owner: str
    :param type: type of the package
    :type type: str
    :param name: name of the package
    :type name: str
    :param version: version of the package
    :type version: str

    """
    return web.Response(status=200)


async def list_packages(request: web.Request, owner, page=None, limit=None, type=None, q=None) -> web.Response:
    """Gets all packages of an owner

    

    :param owner: owner of the packages
    :type owner: str
    :param page: page number of results to return (1-based)
    :type page: int
    :param limit: page size of results
    :type limit: int
    :param type: package type filter
    :type type: str
    :param q: name filter
    :type q: str

    """
    return web.Response(status=200)
