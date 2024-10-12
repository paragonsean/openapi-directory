from typing import List, Dict
from aiohttp import web

from openapi_server.models.bad_request import BadRequest
from openapi_server.models.not_found import NotFound
from openapi_server.models.token_create_payload import TokenCreatePayload
from openapi_server.models.token_list_response import TokenListResponse
from openapi_server.models.upload_token import UploadToken
from openapi_server.models.video import Video
from openapi_server import util


async def d_elete_upload_tokens_upload_token(request: web.Request, upload_token) -> web.Response:
    """Delete an upload token

    Delete an existing upload token. This is especially useful for tokens you may have created that do not expire.

    :param upload_token: The unique identifier for the upload token you want to delete. Deleting a token will make it so the token can no longer be used for authentication.
    :type upload_token: str

    """
    return web.Response(status=200)


async def g_et_upload_tokens(request: web.Request, sort_by=None, sort_order=None, current_page=None, page_size=None) -> web.Response:
    """List all active upload tokens.

    A delegated token is used to allow secure uploads without exposing your API key. Use this endpoint to retrieve a list of all currently active delegated tokens. Tutorials using [delegated upload](https://api.video/blog/endpoints/delegated-upload).

    :param sort_by: Allowed: createdAt, ttl. You can use these to sort by when a token was created, or how much longer the token will be active (ttl - time to live). Date and time is presented in ISO-8601 format.
    :type sort_by: str
    :param sort_order: Allowed: asc, desc. Ascending is 0-9 or A-Z. Descending is 9-0 or Z-A.
    :type sort_order: str
    :param current_page: Choose the number of search results to return per page. Minimum value: 1
    :type current_page: int
    :param page_size: Results per page. Allowed values 1-100, default is 25.
    :type page_size: int

    """
    return web.Response(status=200)


async def g_et_upload_tokens_upload_token(request: web.Request, upload_token) -> web.Response:
    """Show upload token

    You can retrieve details about a specific upload token if you have the unique identifier for the upload token. Add it in the path of the endpoint. Details include time-to-live (ttl), when the token was created, and when it will expire.

    :param upload_token: The unique identifier for the token you want information about.
    :type upload_token: str

    """
    return web.Response(status=200)


async def p_ost_upload(request: web.Request, token, file, content_range=None, video_id=None) -> web.Response:
    """Upload with an upload token

    When given a token, anyone can upload a file to the URI &#x60;https://ws.api.video/upload?token&#x3D;&lt;tokenId&gt;&#x60;.  Example with cURL:  &#x60;&#x60;&#x60;curl $ curl  --request POST --url &#39;https://ws.api.video/upload?token&#x3D;toXXX&#39;  --header &#39;content-type: multipart/form-data&#39;  -F file&#x3D;@video.mp4 &#x60;&#x60;&#x60;  Or in an HTML form, with a little JavaScript to convert the form into JSON: &#x60;&#x60;&#x60;html &lt;!--form for user interaction--&gt; &lt;form name&#x3D;\&quot;videoUploadForm\&quot; &gt;   &lt;label for&#x3D;video&gt;Video:&lt;/label&gt;   &lt;input type&#x3D;file name&#x3D;source/&gt;&lt;br/&gt;   &lt;input value&#x3D;\&quot;Submit\&quot; type&#x3D;\&quot;submit\&quot;&gt; &lt;/form&gt; &lt;div&gt;&lt;/div&gt; &lt;!--JS takes the form data      uses FormData to turn the response into JSON.     then uses POST to upload the video file.     Update the token parameter in the url to your upload token.     --&gt; &lt;script&gt;    var form &#x3D; document.forms.namedItem(\&quot;videoUploadForm\&quot;);     form.addEventListener(&#39;submit&#39;, function(ev) {   ev.preventDefault();      var oOutput &#x3D; document.querySelector(\&quot;div\&quot;),          oData &#x3D; new FormData(form);      var oReq &#x3D; new XMLHttpRequest();         oReq.open(\&quot;POST\&quot;, \&quot;https://ws.api.video/upload?token&#x3D;toXXX\&quot;, true);      oReq.send(oData);   oReq.onload &#x3D; function(oEvent) {        if (oReq.status &#x3D;&#x3D;201) {          oOutput.innerHTML &#x3D; \&quot;Your video is uploaded!&lt;br/&gt;\&quot;  + oReq.response;        } else {          oOutput.innerHTML &#x3D; \&quot;Error \&quot; + oReq.status + \&quot; occurred when trying to upload your file.&lt;br /&gt;\&quot;;        }      };    }, false);  &lt;/script&gt; &#x60;&#x60;&#x60;   ### Dealing with large files  We have created a &lt;a href&#x3D;&#39;https://api.video/blog/tutorials/uploading-large-files-with-javascript&#39;&gt;tutorial&lt;/a&gt; to walk through the steps required.

    :param token: The unique identifier for the token you want to use to upload a video.
    :type token: str
    :param file: The path to the video you want to upload.
    :type file: str
    :param content_range: Content-Range represents the range of bytes that will be returned as a result of the request. Byte ranges are inclusive, meaning that bytes 0-999 represents the first 1000 bytes in a file or object.
    :type content_range: str
    :param video_id: The video id returned by the first call to this endpoint in a large video upload scenario.
    :type video_id: str

    """
    return web.Response(status=200)


async def p_ost_upload_tokens(request: web.Request, body=None) -> web.Response:
    """Generate an upload token

    Use this endpoint to generate an upload token. You can use this token to authenticate video uploads while keeping your API key safe. Tutorials using [delegated upload](https://api.video/blog/endpoints/delegated-upload).

    :param body: 
    :type body: dict | bytes

    """
    body = TokenCreatePayload.from_dict(body)
    return web.Response(status=200)
