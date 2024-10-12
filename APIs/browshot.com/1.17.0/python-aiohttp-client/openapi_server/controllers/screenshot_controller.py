from typing import List, Dict
from aiohttp import web

from openapi_server.models.screenshot import Screenshot
from openapi_server.models.screenshot_error import ScreenshotError
from openapi_server.models.screenshot_host import ScreenshotHost
from openapi_server.models.screenshot_info_error import ScreenshotInfoError
from openapi_server.models.screenshot_list import ScreenshotList
from openapi_server.models.screenshot_short import ScreenshotShort
from openapi_server import util


async def create_multiple_screenshots(request: web.Request, url, instance_id, size=None, cache=None, delay=None, flash_delay=None, screen_width=None, screen_height=None, priority=None, referer=None, post_data=None, cookie=None, script=None, details=None, html=None, max_wait=None, headers=None, hosting=None, hosting_height=None, hosting_width=None, hosting_scale=None, hosting_bucket=None, hosting_file=None, hosting_headers=None) -> web.Response:
    """Request multiple screenshots

    Request multiple screenshots in one API call. The API call accepts all the parameters supported by screenshot/create. You can specify up to 10 URLs and 10 instances for a total of 100 screenshots in one API call. 

    :param url: URL of the page to get a screenshot for. You can specify multiple url parameters (up to 10).
    :type url: str
    :param instance_id: instance ID to use. You can specify multiple instance_id parameters (up to 10).
    :type instance_id: int
    :param size: screenshot size - \&quot;screen\&quot; (default) or \&quot;page\&quot;
    :type size: str
    :param cache: use a previous screenshot (same URL, same instance) if it was done within &lt;cache_value&gt; seconds. The default value is 24hours. Specify cache&#x3D;0 if you want a new screenshot.
    :type cache: int
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

    """
    return web.Response(status=200)


async def create_screenshot(request: web.Request, url, instance_id, size=None, cache=None, delay=None, flash_delay=None, screen_width=None, screen_height=None, priority=None, referer=None, post_data=None, cookie=None, script=None, details=None, html=None, max_wait=None, headers=None, shots=None, shot_interval=None, hosting=None, hosting_height=None, hosting_width=None, hosting_scale=None, hosting_bucket=None, hosting_file=None, hosting_headers=None) -> web.Response:
    """Request a screenshot

    Screenshots requests to private and shared instances require a positive balance.  *IMPORTANT*: Remember that you can only do 100 free screenshots per month. To used a premium instance, use instance_id&#x3D;65 for example. 

    :param url: URL of the page to get a screenshot for
    :type url: str
    :param instance_id: instance ID to use
    :type instance_id: int
    :param size: screenshot size - \&quot;screen\&quot; (default) or \&quot;page\&quot;
    :type size: str
    :param cache: use a previous screenshot (same URL, same instance) if it was done within &lt;cache_value&gt; seconds. The default value is 24hours. Specify cache&#x3D;0 if you want a new screenshot.
    :type cache: int
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
    :param shots: take multiple screenshots of the same page. This costs 1 additional credit for every 2 additional screenshots.
    :type shots: int
    :param shot_interval: number of seconds between 2 screenshots
    :type shot_interval: int
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

    """
    return web.Response(status=200)


async def delete_screenshot(request: web.Request, id, data=None) -> web.Response:
    """Delete screenshot data

    You can delete details of your screenshots to remove any confidential information. 

    :param id: screenshot ID
    :type id: int
    :param data: data to remove. You can specify multiple of them (separated by a ,): *image* (image files), *url* (url requested), *metadata* (time added, time finished, post data, cookie and referer used for the screenshot), *all* (all data and files) 
    :type data: str

    """
    return web.Response(status=200)


async def get_html(request: web.Request, id) -> web.Response:
    """Get the HTML code

    Retrieve the HTML code of the rendered page. This API call should be used when html&#x3D;1 was specified in the screenshot request. 

    :param id: screenshot ID
    :type id: int

    """
    return web.Response(status=200)


async def get_multiple_screenshots_info(request: web.Request, limit=None, status=None) -> web.Response:
    """Get information about screenshots

    Get information about the last 100 screenshots requested.

    :param limit: maximum number of screenshots&#39; information to return
    :type limit: int
    :param status: get list of screenshot in a given status (error, finished, in_process)
    :type status: str

    """
    return web.Response(status=200)


async def get_screenshot_info(request: web.Request, id, details=None) -> web.Response:
    """Query screenshot status

    Once a screenshot has been requested, its status must be checked until it is either \&quot;error\&quot; or \&quot;finished\&quot;.

    :param id: screenshot ID received from /api/v1/screenshot/create
    :type id: int
    :param details: level of details about the screenshot and the page
    :type details: int

    """
    return web.Response(status=200)


async def get_thumbnail(request: web.Request, id, width=None, height=None, scale=None, zoom=None, ratio=None, left=None, right=None, top=None, bottom=None, format=None, shot=None, quality=None) -> web.Response:
    """Retrieve a thumbnail image

    Unlike the other API calls, this API sends back the thumbnail as a PNG file, not JSON. The HTTP response code indicates whether the screenshot was successful (200), or incomplete (404) or failed (404). If the screenshot failed or is not finished, a default image \&quot;Not found\&quot; is sent.  You can crop your screenshots. The crop is done first, then the thumbnail. You can take a 1024x768 screenshot, crop it to 768x768, and get it scaled down to 300x300. 

    :param id: screenshot ID
    :type id: int
    :param width: width of the thumbnail
    :type width: int
    :param height: height of the thumbnail
    :type height: int
    :param scale: scale of the thumbnail
    :type scale: float
    :param zoom: zoom 1 to 100 percent
    :type zoom: int
    :param ratio: Use fit to keep the original page ration, and fill to get a thumbnail for the exact width and height.  specified. If you provide both width and height, you need to specify the ratio: fit to keep the original width/height ratio (the thumbnail might be smaller than the specified width and height), or fill to crop the image if necessary.
    :type ratio: str
    :param left: left edge of the area to be cropped
    :type left: int
    :param right: right edge of the area to be cropped
    :type right: int
    :param top: top edge of the area to be cropped
    :type top: int
    :param bottom: bottom edge of the area to be cropped
    :type bottom: int
    :param format: image as PNG or JPEG
    :type format: str
    :param shot: get the second or third screenshot if multiple screenshots were requested
    :type shot: int
    :param quality: JPEG quality factor (for JPEG thumbnails only)
    :type quality: int

    """
    return web.Response(status=200)


async def host_screenshot(request: web.Request, id, hosting, width=None, height=None, scale=None, bucket=None, file=None, headers=None) -> web.Response:
    """Host thumbnails on your own S3 account or on Browshot.

    You can host screenshots and thumbnails on your own S3 account or on Browshot.

    :param id: screenshot ID
    :type id: int
    :param hosting: hosting option: s3 or browshot
    :type hosting: str
    :param width: width of the thumbnail
    :type width: int
    :param height: height of the thumbnail
    :type height: int
    :param scale: scale of the thumbnail
    :type scale: float
    :param bucket: S3 bucket to upload the screenshot or thumbnail - required with hosting&#x3D;s3
    :type bucket: str
    :param file: file name to use - optional, used with hosting&#x3D;s3
    :type file: str
    :param headers: HTTP headers to add to your S3 object - optional, used with hosting&#x3D;s3
    :type headers: str

    """
    return web.Response(status=200)


async def search_screenshot(request: web.Request, url, limit=None, status=None) -> web.Response:
    """Search for screenshots

    Search for screenshots of a specific URL.

    :param url: look for a string matching the URL requested
    :type url: str
    :param limit: maximum number of screenshots&#39; information to return
    :type limit: int
    :param status: get list of screenshot in a given status (error, finished, in_process)
    :type status: str

    """
    return web.Response(status=200)


async def share_screenshot(request: web.Request, id, note=None) -> web.Response:
    """Share a screenshot

    You can make your screenshots public, add notes, and share it with your friends and colleagues. Only screenshots which are successfully completed can be shared.n the thumbnail. You can take a 1024x768 screenshot, crop it to 768x768, and get it scaled down to 300x300. 

    :param id: screenshot ID
    :type id: int
    :param note: note to add on the sharing page
    :type note: str

    """
    return web.Response(status=200)
