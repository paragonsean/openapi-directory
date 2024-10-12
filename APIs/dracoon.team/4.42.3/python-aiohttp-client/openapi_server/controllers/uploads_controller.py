from typing import List, Dict
from aiohttp import web

from openapi_server.models.chunk_upload_response import ChunkUploadResponse
from openapi_server.models.complete_upload_request import CompleteUploadRequest
from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.node import Node
from openapi_server import util


async def cancel_file_upload_by_token(request: web.Request, token) -> web.Response:
    """Cancel file upload

    ### Description: Cancel file upload.  ### Precondition: Valid upload token.  ### Postcondition: Upload canceled, token invalidated and all already transfered chunks removed.  ### Further Information: It is recommended to notify the API about cancelled uploads if possible.

    :param token: Upload token
    :type token: str

    """
    return web.Response(status=200)


async def complete_file_upload_by_token(request: web.Request, token, x_sds_date_format=None, body=None) -> web.Response:
    """Complete file upload

    ### Description: Finish uploading a file.  ### Precondition: Valid upload token.  ### Postcondition: File created.  ### Further Information: The provided file name might be changed in accordance with the resolution strategy:  * **autorename**: changes the file name and adds a number to avoid conflicts. * **overwrite**: deletes any old file with the same file name. * **fail**: returns an error; in this case, another &#x60;PUT&#x60; request with a different file name may be sent.  Please ensure that all chunks have been transferred correctly before finishing the upload.  Download share id (if exists) gets changed if: - node with the same name exists in the target container - &#x60;resolutionStrategy&#x60; is &#x60;overwrite&#x60; - &#x60;keepShareLinks&#x60; is &#x60;true&#x60;

    :param token: Upload token
    :type token: str
    :param x_sds_date_format: Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) &amp; [leettime.de](http://leettime.de/))
    :type x_sds_date_format: str
    :param body: 
    :type body: dict | bytes

    """
    body = CompleteUploadRequest.from_dict(body)
    return web.Response(status=200)


async def upload_file_by_token_as_multipart1(request: web.Request, token, file, content_range=None) -> web.Response:
    """Upload file

    ### Description:   Upload a (chunk of a) file.  ### Precondition: Valid upload token.  ### Postcondition: Chunk uploaded.  ### Further Information: Range requests are supported.    Following &#x60;Content-Types&#x60; are supported by this API: * &#x60;multipart/form-data&#x60; * provided &#x60;Content-Type&#x60;  For both file upload types set the correct &#x60;Content-Type&#x60; header and body.    ### Examples:    * &#x60;multipart/form-data&#x60; &#x60;&#x60;&#x60; POST /api/v4/uploads/{token} HTTP/1.1  Header: ... Content-Type: multipart/form-data; boundary&#x3D;----WebKitFormBoundary7MA4YWxkTrZu0gW ...  Body: ------WebKitFormBoundary7MA4YWxkTrZu0gW Content-Disposition: form-data; name&#x3D;\&quot;file\&quot;; filename&#x3D;\&quot;file.txt\&quot; Content-Type: text/plain  Content of file.txt ------WebKitFormBoundary7MA4YWxkTrZu0gW-- &#x60;&#x60;&#x60;  * any other &#x60;Content-Type&#x60;  &#x60;&#x60;&#x60; POST /api/v4/uploads/{token} HTTP/1.1  Header: ... Content-Type: { ... } ...  Body: raw content &#x60;&#x60;&#x60; 

    :param token: Upload token
    :type token: str
    :param file: File
    :type file: str
    :param content_range: Content-Range   e.g. &#x60;bytes 0-999/3980&#x60;
    :type content_range: str

    """
    return web.Response(status=200)
