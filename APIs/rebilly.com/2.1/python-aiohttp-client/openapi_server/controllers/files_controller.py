from typing import List, Dict
from aiohttp import web

from openapi_server.models.attachment import Attachment
from openapi_server.models.error import Error
from openapi_server.models.file import File
from openapi_server.models.invalid_error import InvalidError
from openapi_server.models.post_file_request import PostFileRequest
from openapi_server import util


async def delete_attachment(request: web.Request, id, organization_id=None) -> web.Response:
    """Delete an Attachment

    Delete the Attachment with predefined identifier string. 

    :param id: The resource identifier string.
    :type id: str
    :param organization_id: Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    :type organization_id: str

    """
    return web.Response(status=200)


async def delete_file(request: web.Request, id, organization_id=None) -> web.Response:
    """Delete a File

    Delete the File with predefined identifier string. 

    :param id: The resource identifier string.
    :type id: str
    :param organization_id: Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    :type organization_id: str

    """
    return web.Response(status=200)


async def get_attachment(request: web.Request, id, organization_id=None) -> web.Response:
    """Retrieve an Attachment

    Retrieve a Attachment with specified identifier string. 

    :param id: The resource identifier string.
    :type id: str
    :param organization_id: Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    :type organization_id: str

    """
    return web.Response(status=200)


async def get_attachment_collection(request: web.Request, organization_id=None, limit=None, offset=None, filter=None, q=None, expand=None, fields=None, sort=None) -> web.Response:
    """Retrieve a list of Attachments

    Retrieve a list of attachments. You may sort by the id, name, relatedId, relatedType, fileId, createdTime, and updatedTime. 

    :param organization_id: Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    :type organization_id: str
    :param limit: The collection items limit.
    :type limit: int
    :param offset: The collection items offset.
    :type offset: int
    :param filter: The collection items filter requires a special format. Use \&quot;,\&quot; for multiple allowed values.  Use \&quot;;\&quot; for multiple fields. See the [filter guide](https://api-reference.rebilly.com/#section/Using-filter-with-collections) for more options and examples about this format. 
    :type filter: str
    :param q: The partial search of the text fields.
    :type q: str
    :param expand: Expand a response to get a full related object included inside of the &#x60;_embedded&#x60; path in the response. It accepts a comma-separated list of objects to expand. See the [expand guide](https://api-reference.rebilly.com/#section/Expand-to-include-embedded-objects) for more info. 
    :type expand: str
    :param fields: Limit the returned fields to the list specified, separated by comma. Note that id is always returned.
    :type fields: str
    :param sort: The collection items sort field and order (prefix with \&quot;-\&quot; for descending sort).
    :type sort: List[str]

    """
    return web.Response(status=200)


async def get_file(request: web.Request, id, organization_id=None) -> web.Response:
    """Retrieve a File Record

    Retrieve a File with specified identifier string. 

    :param id: The resource identifier string.
    :type id: str
    :param organization_id: Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    :type organization_id: str

    """
    return web.Response(status=200)


async def get_file_collection(request: web.Request, organization_id=None, limit=None, offset=None, filter=None, q=None, expand=None, fields=None, sort=None) -> web.Response:
    """Retrieve a list of files

    Retrieve a list of files. 

    :param organization_id: Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    :type organization_id: str
    :param limit: The collection items limit.
    :type limit: int
    :param offset: The collection items offset.
    :type offset: int
    :param filter: The collection items filter requires a special format. Use \&quot;,\&quot; for multiple allowed values.  Use \&quot;;\&quot; for multiple fields. See the [filter guide](https://api-reference.rebilly.com/#section/Using-filter-with-collections) for more options and examples about this format. 
    :type filter: str
    :param q: The partial search of the text fields.
    :type q: str
    :param expand: Expand a response to get a full related object included inside of the &#x60;_embedded&#x60; path in the response. It accepts a comma-separated list of objects to expand. See the [expand guide](https://api-reference.rebilly.com/#section/Expand-to-include-embedded-objects) for more info. 
    :type expand: str
    :param fields: Limit the returned fields to the list specified, separated by comma. Note that id is always returned.
    :type fields: str
    :param sort: The collection items sort field and order (prefix with \&quot;-\&quot; for descending sort).
    :type sort: List[str]

    """
    return web.Response(status=200)


async def get_file_download(request: web.Request, id, organization_id=None, image_size=None) -> web.Response:
    """Download a file

    Download a file. 

    :param id: The resource identifier string.
    :type id: str
    :param organization_id: Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    :type organization_id: str
    :param image_size: Resize image to specified size. Supports any sizes from 10x10 to 2000x2000 (format &#x60;{width}x{height}&#x60;). The image will be returned in the original size if the value is invalid. This parameter will be ignored for non-image files.
    :type image_size: str

    """
    return web.Response(status=200)


async def get_file_download_extension(request: web.Request, id, extension, organization_id=None) -> web.Response:
    """Download image in specific format

    Download image in specific format. Images are converted server-side. 

    :param id: The resource identifier string.
    :type id: str
    :param extension: File extension which also indicates the desired file format.
    :type extension: str
    :param organization_id: Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    :type organization_id: str

    """
    return web.Response(status=200)


async def post_attachment(request: web.Request, body, organization_id=None) -> web.Response:
    """Create an Attachment

    Create an Attachment. 

    :param body: Attachment resource.
    :type body: dict | bytes
    :param organization_id: Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    :type organization_id: str

    """
    body = Attachment.from_dict(body)
    return web.Response(status=200)


async def post_file(request: web.Request, body, organization_id=None) -> web.Response:
    """Create a file

    Additionally, a file can be sent with:.  - multipart/form-data POST request: in this case all property names are the same as the JSON ones (&#x60;file&#x60; is an uploaded file)  - file body request: the file body is sent as the request body, with the appropriate &#x60;Content-Type&#x60;. No additional  properties can be set along the request data  The following file types only are allowed:  - jpg  - png  - gif  - pdf  - mp3   If using a Publishable Api Key, only private files can be created. The files can later on be modified or used using  a secret API key. 

    :param body: 
    :type body: dict | bytes
    :param organization_id: Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    :type organization_id: str

    """
    body = PostFileRequest.from_dict(body)
    return web.Response(status=200)


async def put_attachment(request: web.Request, id, body, organization_id=None) -> web.Response:
    """Update the Attachment with predefined ID

    Update the Attachment with predefined ID. 

    :param id: The resource identifier string.
    :type id: str
    :param body: Attachment resource.
    :type body: dict | bytes
    :param organization_id: Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    :type organization_id: str

    """
    body = Attachment.from_dict(body)
    return web.Response(status=200)


async def put_file(request: web.Request, id, body, organization_id=None) -> web.Response:
    """Update the File with predefined ID

    Update the File with predefined ID. Note that file can be uploaded with POST. only. 

    :param id: The resource identifier string.
    :type id: str
    :param body: File resource.
    :type body: dict | bytes
    :param organization_id: Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    :type organization_id: str

    """
    body = File.from_dict(body)
    return web.Response(status=200)
