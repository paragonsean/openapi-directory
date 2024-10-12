from typing import List, Dict
from aiohttp import web

from openapi_server.models.collection_response_folder import CollectionResponseFolder
from openapi_server.models.error import Error
from openapi_server.models.folder import Folder
from openapi_server.models.folder_action_response import FolderActionResponse
from openapi_server.models.folder_input import FolderInput
from openapi_server.models.folder_update_input import FolderUpdateInput
from openapi_server.models.folder_update_task_locator import FolderUpdateTaskLocator
from openapi_server import util


async def delete_files_v3_folders_folder_id_archive(request: web.Request, folder_id) -> web.Response:
    """Delete folder.

    Delete folder by ID.

    :param folder_id: ID of folder to delete.
    :type folder_id: str

    """
    return web.Response(status=200)


async def delete_files_v3_folders_folder_path_archive_by_path(request: web.Request, folder_path) -> web.Response:
    """Delete folder.

    Delete folder by path.

    :param folder_path: Path of folder to delete
    :type folder_path: str

    """
    return web.Response(status=200)


async def get_files_v3_folders_folder_id_get_by_id(request: web.Request, folder_id, properties=None) -> web.Response:
    """Get folder

    Get folder by ID

    :param folder_id: ID of desired folder
    :type folder_id: str
    :param properties: Properties to set on returned folder.
    :type properties: List[str]

    """
    return web.Response(status=200)


async def get_files_v3_folders_folder_path_get_by_path(request: web.Request, folder_path, properties=None) -> web.Response:
    """Get folder.

    Get folder by path.

    :param folder_path: Path of desired folder.
    :type folder_path: str
    :param properties: Properties to set on returned folder.
    :type properties: List[str]

    """
    return web.Response(status=200)


async def get_files_v3_folders_search_do_search(request: web.Request, properties=None, after=None, before=None, limit=None, sort=None, id=None, created_at=None, created_at_lte=None, created_at_gte=None, updated_at=None, updated_at_lte=None, updated_at_gte=None, name=None, path=None, parent_folder_id=None) -> web.Response:
    """Search folders

    Search for folders. Does not contain hidden or archived folders.

    :param properties: Properties that should be included in the returned folders.
    :type properties: List[str]
    :param after: The maximum offset of items for a given search is 10000. Narrow your search down if you are reaching this limit.
    :type after: str
    :param before: 
    :type before: str
    :param limit: Limit of results to return. Max limit is 100.
    :type limit: int
    :param sort: Sort results by given property. For example -name sorts by name field descending, name sorts by name field ascending.
    :type sort: List[str]
    :param id: Search folder by given ID.
    :type id: str
    :param created_at: Search for folders with the given creation timestamp.
    :type created_at: str
    :param created_at_lte: 
    :type created_at_lte: str
    :param created_at_gte: 
    :type created_at_gte: str
    :param updated_at: Search for folder at given update timestamp.
    :type updated_at: str
    :param updated_at_lte: 
    :type updated_at_lte: str
    :param updated_at_gte: 
    :type updated_at_gte: str
    :param name: Search for folders containing the specified name.
    :type name: str
    :param path: Search for folders by path.
    :type path: str
    :param parent_folder_id: Search for folders with the given parent folderId.
    :type parent_folder_id: int

    """
    created_at = util.deserialize_datetime(created_at)
    created_at_lte = util.deserialize_datetime(created_at_lte)
    created_at_gte = util.deserialize_datetime(created_at_gte)
    updated_at = util.deserialize_datetime(updated_at)
    updated_at_lte = util.deserialize_datetime(updated_at_lte)
    updated_at_gte = util.deserialize_datetime(updated_at_gte)
    return web.Response(status=200)


async def get_files_v3_folders_update_async_tasks_task_id_status_check_update_status(request: web.Request, task_id) -> web.Response:
    """Check folder update status.

    Check status of folder update. Folder updates happen asynchronously.

    :param task_id: TaskId of folder update
    :type task_id: str

    """
    return web.Response(status=200)


async def post_files_v3_folders_create(request: web.Request, body) -> web.Response:
    """Create folder.

    Creates a folder.

    :param body: Folder creation options
    :type body: dict | bytes

    """
    body = FolderInput.from_dict(body)
    return web.Response(status=200)


async def post_files_v3_folders_update_async_update_properties(request: web.Request, body) -> web.Response:
    """Update folder properties

    Update properties of folder by given ID. This action happens asynchronously and will update all of the folder&#39;s children as well.

    :param body: Properties to change in the folder
    :type body: dict | bytes

    """
    body = FolderUpdateInput.from_dict(body)
    return web.Response(status=200)
