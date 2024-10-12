from typing import List, Dict
from aiohttp import web

from openapi_server.models.default_directory_browser_info_dto import DefaultDirectoryBrowserInfoDto
from openapi_server.models.file_system_entry_info import FileSystemEntryInfo
from openapi_server.models.problem_details import ProblemDetails
from openapi_server.models.validate_path_dto import ValidatePathDto
from openapi_server import util


async def get_default_directory_browser(request: web.Request, ) -> web.Response:
    """Get Default directory browser.

    


    """
    return web.Response(status=200)


async def get_directory_contents(request: web.Request, path, include_files=None, include_directories=None) -> web.Response:
    """Gets the contents of a given directory in the file system.

    

    :param path: The path.
    :type path: str
    :param include_files: An optional filter to include or exclude files from the results. true/false.
    :type include_files: bool
    :param include_directories: An optional filter to include or exclude folders from the results. true/false.
    :type include_directories: bool

    """
    return web.Response(status=200)


async def get_drives(request: web.Request, ) -> web.Response:
    """Gets available drives from the server&#39;s file system.

    


    """
    return web.Response(status=200)


async def get_network_shares(request: web.Request, ) -> web.Response:
    """Gets network paths.

    


    """
    return web.Response(status=200)


async def get_parent_path(request: web.Request, path) -> web.Response:
    """Gets the parent path of a given path.

    

    :param path: The path.
    :type path: str

    """
    return web.Response(status=200)


async def validate_path(request: web.Request, body) -> web.Response:
    """Validates path.

    

    :param body: Validate request object.
    :type body: dict | bytes

    """
    body = ValidatePathDto.from_dict(body)
    return web.Response(status=200)
