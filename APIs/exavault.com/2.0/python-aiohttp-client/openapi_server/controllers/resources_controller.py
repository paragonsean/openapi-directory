from typing import List, Dict
from aiohttp import web

from openapi_server.models.add_folder_request_body import AddFolderRequestBody
from openapi_server.models.compress_files_request_body import CompressFilesRequestBody
from openapi_server.models.copy_resources_request_body import CopyResourcesRequestBody
from openapi_server.models.delete_resources_request_body import DeleteResourcesRequestBody
from openapi_server.models.empty_response import EmptyResponse
from openapi_server.models.extract_files_request_body import ExtractFilesRequestBody
from openapi_server.models.move_resources_request_body import MoveResourcesRequestBody
from openapi_server.models.preview_file_response import PreviewFileResponse
from openapi_server.models.resource_collection_response import ResourceCollectionResponse
from openapi_server.models.resource_copy_move import ResourceCopyMove
from openapi_server.models.resource_multi_response import ResourceMultiResponse
from openapi_server.models.resource_response import ResourceResponse
from openapi_server.models.update_resource_by_id_request_body import UpdateResourceByIdRequestBody
from openapi_server import util


async def add_folder(request: web.Request, ev_api_key, ev_access_token, body=None) -> web.Response:
    """Create a folder

    Create a new empty folder at the specified path. New files can be uploaded via the [/resources/upload](#operation/uploadFile) endpoint.  **Notes:** - Authenticated user should have modify permission. 

    :param ev_api_key: API Key required to make the API call.
    :type ev_api_key: str
    :param ev_access_token: Access token required to make the API call.
    :type ev_access_token: str
    :param body: 
    :type body: dict | bytes

    """
    body = AddFolderRequestBody.from_dict(body)
    return web.Response(status=200)


async def compress_files(request: web.Request, ev_api_key, ev_access_token, body=None) -> web.Response:
    """Compress resources

    Create a zip archive containing the files from given set of paths. Note that this can be a very slow operation if you have indicated many files should be included in the archive.  **Notes:** - Authenticated user should have modify permission. 

    :param ev_api_key: API Key required to make the API call.
    :type ev_api_key: str
    :param ev_access_token: Access token required to make the API call.
    :type ev_access_token: str
    :param body: 
    :type body: dict | bytes

    """
    body = CompressFilesRequestBody.from_dict(body)
    return web.Response(status=200)


async def copy_resources(request: web.Request, ev_api_key, ev_access_token, body=None) -> web.Response:
    """Copy resources

    Copies a set of exisiting files/folders (provided by an array &#x60;resources&#x60;) to the requested &#x60;parentResource&#x60; in your account. In the &#x60;resources&#x60; array, you may specify paths pointing files/folders throughout the account, but everything will be copied to the  root of the &#x60;parentResource&#x60;.  **Notes:** - Authenticated user should have modify permission. 

    :param ev_api_key: API Key required to make the API call.
    :type ev_api_key: str
    :param ev_access_token: Access token required to make the API call.
    :type ev_access_token: str
    :param body: 
    :type body: dict | bytes

    """
    body = CopyResourcesRequestBody.from_dict(body)
    return web.Response(status=200)


async def delete_resource_by_id(request: web.Request, id, ev_api_key, ev_access_token) -> web.Response:
    """Delete a Resource

    Delete a single file or folder resource. Deleting a folder will also delete all of the contents.  **Notes:** - Authenticated user should have [delete permission](/docs/account/04-users/00-introduction#managing-user-roles-and-permissions). - There is no way to un-delete a deleted resource. 

    :param id: ID number of the resource
    :type id: int
    :param ev_api_key: API Key required to make the API call.
    :type ev_api_key: str
    :param ev_access_token: Access token required to make the API call.
    :type ev_access_token: str

    """
    return web.Response(status=200)


async def delete_resources(request: web.Request, ev_api_key, ev_access_token, body=None) -> web.Response:
    """Delete Resources

    Delete multiple file or folder resourcess. Deleting a folder resource will also delete any resources in that folder.  **Notes:** - Authenticated user should have [delete permission](/docs/account/04-users/00-introduction#managing-user-roles-and-permissions). - It is not possible to un-delete a deleted resource. 

    :param ev_api_key: API Key
    :type ev_api_key: str
    :param ev_access_token: Access Token
    :type ev_access_token: str
    :param body: 
    :type body: dict | bytes

    """
    body = DeleteResourcesRequestBody.from_dict(body)
    return web.Response(status=200)


async def download(request: web.Request, ev_api_key, ev_access_token, resources, download_archive_name=None) -> web.Response:
    """Download a file

    Downloads a file from the server. Whenever more than one file is being downloaded, the file are first zipped into  a single file before the download starts, and the resulting zip file is named to match the &#x60;downloadArchiveName&#x60; parameter.  **NOTE**: Downloading many files at once  may result in a long delay before the API will return a response. You may need to override default timeout values in your API client, or download files individually.

    :param ev_api_key: API Key required to make the API call.
    :type ev_api_key: str
    :param ev_access_token: Access token required to make the API call.
    :type ev_access_token: str
    :param resources: Path of file or folder to be downloaded, starting from the root. Can also be an array of paths.
    :type resources: List[str]
    :param download_archive_name: When downloading multiple files, this will be used as the name of the zip file that is created.
    :type download_archive_name: str

    """
    return web.Response(status=200)


async def extract_files(request: web.Request, ev_api_key, ev_access_token, body=None) -> web.Response:
    """Extract resources

    Extract the contents of a zip archive to a specified directory. Note that this can be a very slow operation.  **Notes:** - You must have  [modify permission](/docs/account/04-users/00-introduction#managing-user-roles-and-permissions) to do this. 

    :param ev_api_key: API Key required to make the API call.
    :type ev_api_key: str
    :param ev_access_token: Access token required to make the API call.
    :type ev_access_token: str
    :param body: 
    :type body: dict | bytes

    """
    body = ExtractFilesRequestBody.from_dict(body)
    return web.Response(status=200)


async def get_preview_image(request: web.Request, ev_api_key, ev_access_token, resource, size, width=None, height=None, page=None) -> web.Response:
    """Preview a file

    Returns a resized image of the specified document for supported file types.  Image data returned is encoded in base64 format and can be viewed using the &#x60;&lt;img&gt;&#x60; element.   &#x60;&#x60;&#x60;&lt;img src&#x3D;&#39;data:image/jpeg;base64&#39; + meta.image/&gt;&#x60;&#x60;&#x60;  **Notes:** - Supported files types are &#x60;&#39;jpg&#39;&#x60;, &#x60;&#39;jpeg&#39;&#x60;, &#x60;&#39;gif&#39;&#x60;, &#x60;&#39;png&#39;&#x60;, &#x60;&#39;bmp&#39;&#x60;, &#x60;&#39;pdf&#39;&#x60;, &#x60;&#39;psd&#39;&#x60;, &#x60;&#39;doc&#39;&#x60; 

    :param ev_api_key: API Key
    :type ev_api_key: str
    :param ev_access_token: Access Token
    :type ev_access_token: str
    :param resource: Resource identifier for the image file.
    :type resource: str
    :param size: The size of the image.
    :type size: str
    :param width: Overrides sizes. Sets to a specific width.
    :type width: int
    :param height: Overrides sizes. Sets to a specific height.
    :type height: int
    :param page: Page number to extract from a multi-page document (0 is the first page). Vaild for **.pdf** or **.doc** files.
    :type page: int

    """
    return web.Response(status=200)


async def get_resource_info(request: web.Request, ev_api_key, ev_access_token, resource, include=None) -> web.Response:
    """Get Resource Properties

    Returns details for specified file/folder id or hash, including upload date, size and type. For the full list of returned properties, see the response syntax, below.  **Notes:** - Authenticated user should have list permission. 

    :param ev_api_key: API Key required to make the API call.
    :type ev_api_key: str
    :param ev_access_token: Access token required to make the API call.
    :type ev_access_token: str
    :param resource: Resource identifier of the file or folder to get metadata for.
    :type resource: str
    :param include: Comma separated list of relationships to include in response. Possible values are **share**, **notifications**, **directFile**, **parentResource**, **ownerUser**, **ownerUser**.
    :type include: str

    """
    return web.Response(status=200)


async def get_resource_info_by_id(request: web.Request, id, ev_api_key, ev_access_token, include=None) -> web.Response:
    """Get resource metadata

    Returns metadata for specified file/folder path, including upload date, size and type. For the full list of returned properties, see the response syntax, below.  **Notes:** - Authenticated user should have list permission. 

    :param id: ID number of the resource
    :type id: int
    :param ev_api_key: API Key required to make the API call.
    :type ev_api_key: str
    :param ev_access_token: Access token required to make the API call.
    :type ev_access_token: str
    :param include: Comma separated list of relationships to include in response. Possible values are **share**, **notifications**, **directFile**, **parentResource**, **ownerUser**, **ownerAccount**.
    :type include: str

    """
    return web.Response(status=200)


async def list_resource_contents(request: web.Request, ev_api_key, ev_access_token, id, sort=None, offset=None, limit=None, type=None, include=None) -> web.Response:
    """List contents of folder

    Returns a list of files/folders for the parent resource ID.   You can use this API call to get information about all files and folders at a specified path. By default, the API returns basic metadata on each file/folder. An optional &#x60;include&#x60; parameter forces the return of additional metadata. As with all API calls, the path should be the full path relative to the user&#39;s home directory (e.g. **/myfiles/some_folder**).  **Notes:** - Authenticated user should have list permission. 

    :param ev_api_key: API Key required to make the API call. 
    :type ev_api_key: str
    :param ev_access_token: Access token required to make the API call.
    :type ev_access_token: str
    :param id: ID of the parent resource to get a list of resources for.
    :type id: int
    :param sort: Endpoint support multiple sort fields by allowing array of sort params. Sort fields should be applied in the order specified. The sort order for each sort field is ascending unless it is prefixed with a minus (“-“), in which case it will be descending.
    :type sort: str
    :param offset: Determines which item to start on for pagination. Use zero (0) to start at the beginning of the list.
    :type offset: int
    :param limit: The number of files to limit the result. Cannot be set higher than 100. If you have more than one hundred files in your directory, make multiple calls, incrementing the &#x60;offset parameter, above.
    :type limit: int
    :param type: Limit types of resources returned to \&quot;file\&quot; or \&quot;dir\&quot; only.
    :type type: str
    :param include: Comma separated list of relationships to include in response. Possible values are **share**, **notifications**, **directFile**, **parentResource**, **ownerUser**, **ownerUser**.
    :type include: str

    """
    return web.Response(status=200)


async def list_resources(request: web.Request, ev_api_key, ev_access_token, resource, sort=None, offset=None, limit=None, type=None, name=None, include=None) -> web.Response:
    """Get a list of all resources

    Returns a list of files and folders in the account. Use the &#x60;resource&#x60; query parameter to indicate the folder you wish to search in (which can be /).   **Searching for Files and Folders**  Using the &#x60;name&#x60; parameter triggers search mode, which will search the entire directory structure under the provided &#x60;resource&#x60; for files or folders with names matching the provided &#x60;name&#x60;. This supports wildcard matching such as:  - \\*Report\\* would find any files or folders with \&quot;Report\&quot; in the name. - Data\\_202?-09-30.xlsx would match items such as \&quot;Data\\_2020-09-30.xlsx\&quot;, \&quot;DATA\\_2021-09-30.xlsx\&quot;, \&quot;data\\_2022-09-30.xlsx\&quot; etc. - sales\\* would find any files or folders starting with the word \&quot;Sales\&quot; - \\*.csv would locate any files ending in \&quot;.csv\&quot; - \\* matches everything within the directory tree starting at your given &#x60;resource&#x60;  The search is not case-sensitive. Searching for Clients\\* or clients\\* or CLIENTS\\*, etc. will provide identical results  If you are using the &#x60;name&#x60; parameter to run a search, the &#x60;type&#x60; parameter will be ignored by the server.

    :param ev_api_key: API Key required to make the API call.
    :type ev_api_key: str
    :param ev_access_token: Access token required to make the API call.
    :type ev_access_token: str
    :param resource: Resource identifier to get resources for. Can be path/id/name.
    :type resource: str
    :param sort: Endpoint support multiple sort fields by allowing array of sort params. Sort fields should be applied in the order specified. The sort order for each sort field is ascending unless it is prefixed with a minus (“-“), in which case it will be descending.
    :type sort: str
    :param offset: Determines which item to start on for pagination. Use zero (0) to start at the beginning of the list. e.g, setting &#x60;offset&#x3D;200&#x60; would trigger the server to skip the first 200 matching entries when returning the results.
    :type offset: int
    :param limit: The number of files to limit the result. If you have more files in your directory than this limit, make multiple calls, incrementing the &#x60;offset&#x60; parameter, above.
    :type limit: int
    :param type: Limit types of resources returned to \&quot;file\&quot; or \&quot;dir\&quot; only. This is ignored if you are using the &#x60;name&#x60; parameter to trigger a search.
    :type type: str
    :param name: Text to match resource names. This allows you to filter the results returned. For example, to locate only zip archive files, you can enter &#x60;*zip&#x60; and only resources ending in \&quot;zip\&quot; will be included in the list of results.
    :type name: str
    :param include: Comma separated list of relationships to include in response. Possible values are **share**, **notifications**, **directFile**, **parentResource**, **ownerUser**, **ownerAccount**.
    :type include: str

    """
    return web.Response(status=200)


async def move_resources(request: web.Request, ev_api_key, ev_access_token, body=None) -> web.Response:
    """Move resources

    Moves a set of exisiting files/folders (provided by an array &#x60;resources&#x60;) to the requested &#x60;parentResource&#x60; in your account. In the &#x60;resources&#x60; array, you may specify paths pointing files/folders throughout the account, but everything will be moved to the root of the &#x60;parentResource&#x60;.  **Notes:** - Authenticated user should have modify permission. 

    :param ev_api_key: API Key required to make the API call.
    :type ev_api_key: str
    :param ev_access_token: Access token required to make the API call.
    :type ev_access_token: str
    :param body: 
    :type body: dict | bytes

    """
    body = MoveResourcesRequestBody.from_dict(body)
    return web.Response(status=200)


async def update_resource_by_id(request: web.Request, id, ev_access_token, ev_api_key, body=None) -> web.Response:
    """Rename a resource.

    Update the specified file or folder resource record&#39;s \&quot;name\&quot; parameter. The resource is identified by the numeric resource ID that is passed in as the last segment of the URI. 

    :param id: ID number of the resource
    :type id: int
    :param ev_access_token: Access token required to make the API call.
    :type ev_access_token: str
    :param ev_api_key: API key required to make the API call.
    :type ev_api_key: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateResourceByIdRequestBody.from_dict(body)
    return web.Response(status=200)


async def upload_file(request: web.Request, ev_api_key, ev_access_token, path, file_size, offset_bytes=None, resume=None, allow_overwrite=None, file=None) -> web.Response:
    """Upload a file

    Uploads a file to a specified path, with optional support for resuming a partially uploaded existing file. 

    :param ev_api_key: API Key required to make the API call.
    :type ev_api_key: str
    :param ev_access_token: Access token required to make the API call.
    :type ev_access_token: str
    :param path: Destination path for the file being uploaded, including the file name.
    :type path: str
    :param file_size: File size, in bits, of the file being uploaded.
    :type file_size: int
    :param offset_bytes: Allows a file upload to resume at a certain number of bytes.
    :type offset_bytes: int
    :param resume: True if upload resume is supported, false if it isn&#39;t. 
    :type resume: bool
    :param allow_overwrite: True if a file with the same name is found in the designated path, should be overwritten. False if different file names should be generated. 
    :type allow_overwrite: bool
    :param file: 
    :type file: str

    """
    return web.Response(status=200)
