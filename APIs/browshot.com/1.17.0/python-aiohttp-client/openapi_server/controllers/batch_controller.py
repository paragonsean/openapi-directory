from typing import List, Dict
from aiohttp import web

from openapi_server.models.batch import Batch
from openapi_server.models.batch_error import BatchError
from openapi_server import util


async def create_batch(request: web.Request, instance_id, hosting=None, hosting_height=None, hosting_width=None, hosting_scale=None, hosting_bucket=None, hosting_file=None, hosting_headers=None, file=None, size=None, name=None, width=None, height=None, delay=None, flash_delay=None, screen_width=None, screen_height=None, priority=None, referer=None, post_data=None, cookie=None, script=None, details=None, html=None, max_wait=None, headers=None, format=None) -> web.Response:
    """Requests thousands of screenshtos at once

    Get hundreds or thousands of screenshots from a text file. You can use this API call or the dashboard. Unlike the other API calls, you must issue a POST request with the Content-Type \&quot;multipart/form-data\&quot; in order to upload the text file. The text file must contain the list of URLs to request, 1 URL per line. Failed screenshots will be tried up to 3 times before giving up. 

    :param instance_id: instance ID to use
    :type instance_id: int
    :param hosting: hosting option - s3 or browshot
    :type hosting: str
    :param hosting_height: maximum height of the thumbnail to host
    :type hosting_height: int
    :param hosting_width: maximum height of the thumbnail to host
    :type hosting_width: int
    :param hosting_scale: scale of the thumbnail to host
    :type hosting_scale: float
    :param hosting_bucket: S3 bucket to upload the screenshot or thumbnail (required for S3)
    :type hosting_bucket: str
    :param hosting_file: file name to use (for S3 only)
    :type hosting_file: str
    :param hosting_headers: list of headers to add to the S3 object (for S3 only)
    :type hosting_headers: str
    :param file: text file to use
    :type file: str
    :param size: screenshots size - \\\&quot;screen\\\&quot; (default) or \\\&quot;page\\\&quot;
    :type size: str
    :param name: name of the batch
    :type name: str
    :param width: thumbnail width.
    :type width: int
    :param height: thumbnail height
    :type height: int
    :param delay: number of seconds to wait after the page has loaded. This is used to let JavaScript run longer before taking the screenshot. Use delay&#x3D;0 to take screenshots faster.
    :type delay: int
    :param flash_delay: number of seconds to wait after the page has loaded if Flash elements are present. Use flash_delay&#x3D;0 to take screenshots faster.
    :type flash_delay: int
    :param screen_width: width of the browser window. For desktop browsers only.
    :type screen_width: int
    :param screen_height: height of the browser window. For desktop browsers only. (Note: full-page screenshots can have a height of up to 15,000px)
    :type screen_height: int
    :param priority: assign priority to the screenshot (for private instances only)
    :type priority: int
    :param referer: use a custom referrer header - paid screenshots only
    :type referer: str
    :param post_data: send a POST requests with post_data, useful for filling out forms - paid screenshots only
    :type post_data: str
    :param cookie: set a cookie for the URL requested (see Custom POST Data, Referer and Cookie) Cookies should be separated by a ; - paid screenshots only
    :type cookie: str
    :param script: URL of javascript file to execute after the page load event
    :type script: str
    :param details: level of information available with screenshot/info
    :type details: int
    :param html: saves the HTML of the rendered page which can be retrieved by the API call screenshot/html. This feature costs *1 credit* per screenshot.
    :type html: int
    :param max_wait: maximum number of seconds to wait before triggering the PageLoad event. Note that delay will still be used. (default: 0 &#x3D; disabled)
    :type max_wait: int
    :param headers: any custom HTTP headers. (Not supported with Internet Explorer)
    :type headers: str
    :param format: image as PNG or JPEG
    :type format: str

    """
    return web.Response(status=200)


async def get_batch_info(request: web.Request, id) -> web.Response:
    """Get the batch status

    Get the status of a batch requested through the API or through the dashboard. 

    :param id: batch ID
    :type id: int

    """
    return web.Response(status=200)
