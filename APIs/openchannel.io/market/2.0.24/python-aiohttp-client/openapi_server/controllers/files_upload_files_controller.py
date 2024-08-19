from typing import List, Dict
from aiohttp import web

from openapi_server.models.file import File
from openapi_server.models.file_download import FileDownload
from openapi_server import util


async def files_by_id_or_url_get(request: web.Request, file_id_or_url) -> web.Response:
    """Get the details for a file.

    

    :param file_id_or_url: The fileId or fileUrl of the file to be returned
    :type file_id_or_url: str

    """
    return web.Response(status=200)


async def files_download_get(request: web.Request, file_id, valid_seconds=None) -> web.Response:
    """A signed URL for downloading a private file can be returned by providing the fileId.

    

    :param file_id: The URL of the file to be uploaded
    :type file_id: str
    :param valid_seconds: The number of seconds that this signed URL should be valid for. The default is 60.
    :type valid_seconds: int

    """
    return web.Response(status=200)


async def files_get(request: web.Request, query=None, sort=None, page_number=None, limit=None) -> web.Response:
    """Returns a paginated list of files

    

    :param query: A query document. Example: {&#39;name&#39;:&#39;file.txt&#39;} matches all the files that have the name &#39;file.txt&#39;
    :type query: str
    :param sort: A sort document. Example: {&#39;name&#39;:1} sorts the results by name in ascending order
    :type sort: str
    :param page_number: The result set page number to be returned
    :type page_number: int
    :param limit: The maximum number of results to return per page
    :type limit: int

    """
    return web.Response(status=200)


async def files_post(request: web.Request, file, is_private=None, hash=None) -> web.Response:
    """Uploads a file.

    - WARNING: File URLs or fileIds must be stored somewhere within the customData field for an app, review, developer or user. Unused files will be removed after a few days.  - This method is called on behalf of a developer. 

    :param file: The file to be uploaded
    :type file: str
    :param is_private: If true, this file will be protected as a private file and require the generation of a signed URL in order to download using the Download File API. The default is false.
    :type is_private: bool
    :param hash: A comma separated list of hashes to return in order to verify file integrity.
    :type hash: str

    """
    return web.Response(status=200)


async def files_url_post(request: web.Request, url, is_private=None) -> web.Response:
    """Uploads a file from a URL

    - WARNING: File URLs or fileIds must be stored somewhere within the customData field for an app, review, developer or user. Unused files will be removed after a few days. - This method is called on behalf of a developer. 

    :param url: The URL of the file to be uploaded
    :type url: str
    :param is_private: If true, this file will be protected as a private file and require the generation of a signed URL in order to download using the Download File API. The default is false.
    :type is_private: bool

    """
    return web.Response(status=200)
