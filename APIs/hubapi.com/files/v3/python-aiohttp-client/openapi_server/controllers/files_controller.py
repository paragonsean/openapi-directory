from typing import List, Dict
from aiohttp import web

from openapi_server.models.collection_response_file import CollectionResponseFile
from openapi_server.models.error import Error
from openapi_server.models.file import File
from openapi_server.models.file_action_response import FileActionResponse
from openapi_server.models.file_stat import FileStat
from openapi_server.models.file_update_input import FileUpdateInput
from openapi_server.models.import_from_url_input import ImportFromUrlInput
from openapi_server.models.import_from_url_task_locator import ImportFromUrlTaskLocator
from openapi_server.models.signed_url import SignedUrl
from openapi_server import util


async def delete_files_v3_files_file_id_archive(request: web.Request, file_id) -> web.Response:
    """Delete file

    Delete file by ID

    :param file_id: FileId to delete
    :type file_id: str

    """
    return web.Response(status=200)


async def delete_files_v3_files_file_id_gdpr_delete_archive_gdpr(request: web.Request, file_id) -> web.Response:
    """GDPR delete

    GDRP delete file

    :param file_id: ID of file to GDPR delete
    :type file_id: str

    """
    return web.Response(status=200)


async def get_files_v3_files_file_id_get_by_id(request: web.Request, file_id, properties=None) -> web.Response:
    """Get file.

    Get file by ID.

    :param file_id: ID of the desired file.
    :type file_id: str
    :param properties: 
    :type properties: List[str]

    """
    return web.Response(status=200)


async def get_files_v3_files_file_id_signed_url_get_signed_url(request: web.Request, file_id, size=None, expiration_seconds=None, upscale=None) -> web.Response:
    """Get signed URL to access private file.

    Generates signed URL that allows temporary access to a private file.

    :param file_id: ID of file.
    :type file_id: str
    :param size: For image files. This will resize the image to the desired size before sharing. Does not affect the original file, just the file served by this signed URL.
    :type size: str
    :param expiration_seconds: How long in seconds the link will provide access to the file.
    :type expiration_seconds: int
    :param upscale: If size is provided, this will upscale the image to fit the size dimensions.
    :type upscale: bool

    """
    return web.Response(status=200)


async def get_files_v3_files_import_from_url_async_tasks_task_id_status_check_import(request: web.Request, task_id) -> web.Response:
    """Check import status.

    Check the status of requested import.

    :param task_id: Import by URL task ID
    :type task_id: str

    """
    return web.Response(status=200)


async def get_files_v3_files_search_do_search(request: web.Request, properties=None, after=None, before=None, limit=None, sort=None, id=None, created_at=None, created_at_lte=None, created_at_gte=None, updated_at=None, updated_at_lte=None, updated_at_gte=None, name=None, path=None, parent_folder_id=None, size=None, height=None, width=None, encoding=None, type=None, extension=None, url=None, is_usable_in_content=None, allows_anonymous_access=None) -> web.Response:
    """Search files

    Search through files in the file manager. Does not display hidden or archived files.

    :param properties: Desired file properties in the return object.
    :type properties: List[str]
    :param after: The maximum offset of items for a given search is 10000. Narrow your search down if you are reaching this limit.
    :type after: str
    :param before: 
    :type before: str
    :param limit: Number of items to return. Maximum limit is 100.
    :type limit: int
    :param sort: Sort files by a given field.
    :type sort: List[str]
    :param id: Search files by given ID.
    :type id: str
    :param created_at: Search files by time of creation.
    :type created_at: str
    :param created_at_lte: 
    :type created_at_lte: str
    :param created_at_gte: 
    :type created_at_gte: str
    :param updated_at: Search files by time of latest updated.
    :type updated_at: str
    :param updated_at_lte: 
    :type updated_at_lte: str
    :param updated_at_gte: 
    :type updated_at_gte: str
    :param name: Search for files containing the given name.
    :type name: str
    :param path: Search files by path.
    :type path: str
    :param parent_folder_id: Search files within given folderId.
    :type parent_folder_id: int
    :param size: Query by file size.
    :type size: int
    :param height: Search files by height of image or video.
    :type height: int
    :param width: Search files by width of image or video.
    :type width: int
    :param encoding: Search files with specified encoding.
    :type encoding: str
    :param type: Filter by provided file type.
    :type type: str
    :param extension: Search files by given extension.
    :type extension: str
    :param url: Search for given URL
    :type url: str
    :param is_usable_in_content: If true shows files that have been marked to be used in new content. It false shows files that should not be used in new content.
    :type is_usable_in_content: bool
    :param allows_anonymous_access: If &#39;true&#39; will show private files; if &#39;false&#39; will show public files
    :type allows_anonymous_access: bool

    """
    created_at = util.deserialize_datetime(created_at)
    created_at_lte = util.deserialize_datetime(created_at_lte)
    created_at_gte = util.deserialize_datetime(created_at_gte)
    updated_at = util.deserialize_datetime(updated_at)
    updated_at_lte = util.deserialize_datetime(updated_at_lte)
    updated_at_gte = util.deserialize_datetime(updated_at_gte)
    return web.Response(status=200)


async def get_files_v3_files_stat_path_get_metadata(request: web.Request, path, properties=None) -> web.Response:
    """get_files_v3_files_stat_path_get_metadata

    

    :param path: 
    :type path: str
    :param properties: 
    :type properties: List[str]

    """
    return web.Response(status=200)


async def patch_files_v3_files_file_id_update_properties(request: web.Request, file_id, body) -> web.Response:
    """update file properties

    Update properties of file by ID.

    :param file_id: ID of file to update
    :type file_id: str
    :param body: Options to update.
    :type body: dict | bytes

    """
    body = FileUpdateInput.from_dict(body)
    return web.Response(status=200)


async def post_files_v3_files_import_from_url_async_import_from_url(request: web.Request, body) -> web.Response:
    """Import a file from a URL into the file manager.

    Asynchronously imports the file at the given URL into the file manager.

    :param body: 
    :type body: dict | bytes

    """
    body = ImportFromUrlInput.from_dict(body)
    return web.Response(status=200)


async def post_files_v3_files_upload(request: web.Request, charset_hunch=None, file=None, file_name=None, folder_id=None, folder_path=None, options=None) -> web.Response:
    """Upload file

    Upload a single file with content specified in request body.

    :param charset_hunch: Character set of the uploaded file.
    :type charset_hunch: str
    :param file: File to be uploaded.
    :type file: str
    :param file_name: Desired name for the uploaded file.
    :type file_name: str
    :param folder_id: Either &#39;folderId&#39; or &#39;folderPath&#39; is required. folderId is the ID of the folder the file will be uploaded to.
    :type folder_id: str
    :param folder_path: Either &#39;folderPath&#39; or &#39;folderId&#39; is required. This field represents the destination folder path for the uploaded file. If a path doesn&#39;t exist, the system will try to create one.
    :type folder_path: str
    :param options: JSON string representing FileUploadOptions.
    :type options: str

    """
    return web.Response(status=200)


async def put_files_v3_files_file_id_replace(request: web.Request, file_id, charset_hunch=None, file=None, options=None) -> web.Response:
    """Replace file.

    Replace existing file data with new file data. Can be used to change image content without having to upload a new file and update all references.

    :param file_id: ID of the desired file.
    :type file_id: str
    :param charset_hunch: Character set of given file data.
    :type charset_hunch: str
    :param file: File data that will replace existing file in the file manager.
    :type file: str
    :param options: JSON String representing FileReplaceOptions
    :type options: str

    """
    return web.Response(status=200)
