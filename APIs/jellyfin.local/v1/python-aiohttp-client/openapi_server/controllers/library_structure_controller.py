from typing import List, Dict
from aiohttp import web

from openapi_server.models.add_virtual_folder_dto import AddVirtualFolderDto
from openapi_server.models.media_path_dto import MediaPathDto
from openapi_server.models.media_path_info import MediaPathInfo
from openapi_server.models.problem_details import ProblemDetails
from openapi_server.models.update_library_options_dto import UpdateLibraryOptionsDto
from openapi_server.models.virtual_folder_info import VirtualFolderInfo
from openapi_server import util


async def add_media_path(request: web.Request, body, refresh_library=None) -> web.Response:
    """Add a media path to a library.

    

    :param body: The media path dto.
    :type body: dict | bytes
    :param refresh_library: Whether to refresh the library.
    :type refresh_library: bool

    """
    body = MediaPathDto.from_dict(body)
    return web.Response(status=200)


async def add_virtual_folder(request: web.Request, name=None, collection_type=None, paths=None, refresh_library=None, body=None) -> web.Response:
    """Adds a virtual folder.

    

    :param name: The name of the virtual folder.
    :type name: str
    :param collection_type: The type of the collection.
    :type collection_type: str
    :param paths: The paths of the virtual folder.
    :type paths: List[str]
    :param refresh_library: Whether to refresh the library.
    :type refresh_library: bool
    :param body: The library options.
    :type body: dict | bytes

    """
    body = AddVirtualFolderDto.from_dict(body)
    return web.Response(status=200)


async def get_virtual_folders(request: web.Request, ) -> web.Response:
    """Gets all virtual folders.

    


    """
    return web.Response(status=200)


async def remove_media_path(request: web.Request, name=None, path=None, refresh_library=None) -> web.Response:
    """Remove a media path.

    

    :param name: The name of the library.
    :type name: str
    :param path: The path to remove.
    :type path: str
    :param refresh_library: Whether to refresh the library.
    :type refresh_library: bool

    """
    return web.Response(status=200)


async def remove_virtual_folder(request: web.Request, name=None, refresh_library=None) -> web.Response:
    """Removes a virtual folder.

    

    :param name: The name of the folder.
    :type name: str
    :param refresh_library: Whether to refresh the library.
    :type refresh_library: bool

    """
    return web.Response(status=200)


async def rename_virtual_folder(request: web.Request, name=None, new_name=None, refresh_library=None) -> web.Response:
    """Renames a virtual folder.

    

    :param name: The name of the virtual folder.
    :type name: str
    :param new_name: The new name.
    :type new_name: str
    :param refresh_library: Whether to refresh the library.
    :type refresh_library: bool

    """
    return web.Response(status=200)


async def update_library_options(request: web.Request, body=None) -> web.Response:
    """Update library options.

    

    :param body: The library name and options.
    :type body: dict | bytes

    """
    body = UpdateLibraryOptionsDto.from_dict(body)
    return web.Response(status=200)


async def update_media_path(request: web.Request, name=None, body=None) -> web.Response:
    """Updates a media path.

    

    :param name: The name of the library.
    :type name: str
    :param body: The path info.
    :type body: dict | bytes

    """
    body = MediaPathInfo.from_dict(body)
    return web.Response(status=200)
