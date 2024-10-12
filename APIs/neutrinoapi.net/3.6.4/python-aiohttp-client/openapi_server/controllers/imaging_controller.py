from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_error import APIError
from openapi_server import util


async def h_tml_render(request: web.Request, content, css=None, delay=None, footer=None, format=None, grayscale=None, header=None, ignore_certificate_errors=None, image_height=None, image_width=None, landscape=None, margin=None, margin_bottom=None, margin_left=None, margin_right=None, margin_top=None, page_height=None, page_size=None, page_width=None, timeout=None, title=None, zoom=None) -> web.Response:
    """HTML Render

    Render HTML content to PDF, JPG or PNG

    :param content: The HTML content. This can be either a URL to load from, a file upload (multipart/form-data) or an HTML content string
    :type content: str
    :param css: Inject custom CSS into the HTML. e.g. &#39;body { background-color: red;}&#39;
    :type css: str
    :param delay: Number of seconds to wait before rendering the page (can be useful for pages with animations etc)
    :type delay: int
    :param footer: The footer HTML to insert into each page. The following dynamic tags are supported: {date}, {title}, {url}, {pageNumber}, {totalPages}
    :type footer: str
    :param format: Which format to output, available options are: PDF, PNG, JPG
    :type format: str
    :param grayscale: Render the final document in grayscale
    :type grayscale: bool
    :param header: The header HTML to insert into each page. The following dynamic tags are supported: {date}, {title}, {url}, {pageNumber}, {totalPages}
    :type header: str
    :param ignore_certificate_errors: Ignore any TLS/SSL certificate errors
    :type ignore_certificate_errors: bool
    :param image_height: If rendering to an image format (PNG or JPG) use this image height (in pixels). The default is automatic which dynamically sets the image height based on the content
    :type image_height: int
    :param image_width: If rendering to an image format (PNG or JPG) use this image width (in pixels)
    :type image_width: int
    :param landscape: Set the document to landscape orientation
    :type landscape: bool
    :param margin: The document margin (in mm)
    :type margin: float
    :param margin_bottom: The document bottom margin (in mm)
    :type margin_bottom: float
    :param margin_left: The document left margin (in mm)
    :type margin_left: float
    :param margin_right: The document right margin (in mm)
    :type margin_right: float
    :param margin_top: The document top margin (in mm)
    :type margin_top: float
    :param page_height: Set the PDF page height explicitly (in mm)
    :type page_height: float
    :param page_size: Set the document page size, can be one of: A0 - A9, B0 - B10, Comm10E, DLE or Letter
    :type page_size: str
    :param page_width: Set the PDF page width explicitly (in mm)
    :type page_width: float
    :param timeout: Timeout in seconds. Give up if still trying to load the HTML content after this number of seconds
    :type timeout: int
    :param title: The document title
    :type title: str
    :param zoom: Set the zoom factor when rendering the page (2.0 for double size, 0.5 for half size)
    :type zoom: float

    """
    return web.Response(status=200)


async def image_resize(request: web.Request, image_url, width, bg_color=None, format=None, height=None, resize_mode=None) -> web.Response:
    """Image Resize

    Resize an image and output as either JPEG or PNG

    :param image_url: The URL or Base64 encoded Data URL for the source image. You can also upload an image file directly using multipart/form-data
    :type image_url: str
    :param width: The width to resize to (in px)
    :type width: int
    :param bg_color: The image background color in hexadecimal notation (e.g. #0000ff). For PNG output the special value of &#39;transparent&#39; can also be used. For JPG output the default is black (#000000)
    :type bg_color: str
    :param format: The output image format, can be either png or jpg
    :type format: str
    :param height: The height to resize to (in px). If you don&#39;t set this field then the height will be automatic based on the requested width and image aspect ratio
    :type height: int
    :param resize_mode: The resize mode to use, we support 3 main resizing modes: &lt;ul&gt; &lt;li&gt;&lt;b&gt;scale&lt;/b&gt;&lt;br&gt;Resize to within the width and height specified while preserving aspect ratio. In this mode the width or height will be automatically adjusted to fit the aspect ratio&lt;/li&gt; &lt;li&gt;&lt;b&gt;pad&lt;/b&gt;&lt;br&gt;Resize to exactly the width and height specified while preserving aspect ratio and pad any space left over. Any padded space will be filled in with the &#39;bg-color&#39; value&lt;/li&gt; &lt;li&gt;&lt;b&gt;crop&lt;/b&gt;&lt;br&gt;Resize to exactly the width and height specified while preserving aspect ratio and crop any space which fall outside the area. The cropping window is centered on the original image&lt;/li&gt; &lt;/ul&gt;
    :type resize_mode: str

    """
    return web.Response(status=200)


async def image_watermark(request: web.Request, image_url, watermark_url, bg_color=None, format=None, height=None, opacity=None, position=None, resize_mode=None, width=None) -> web.Response:
    """Image Watermark

    Watermark one image with another image

    :param image_url: The URL or Base64 encoded Data URL for the source image. You can also upload an image file directly using multipart/form-data
    :type image_url: str
    :param watermark_url: The URL or Base64 encoded Data URL for the watermark image. You can also upload an image file directly using multipart/form-data
    :type watermark_url: str
    :param bg_color: The image background color in hexadecimal notation (e.g. #0000ff). For PNG output the special value of &#39;transparent&#39; can also be used. For JPG output the default is black (#000000)
    :type bg_color: str
    :param format: The output image format, can be either png or jpg
    :type format: str
    :param height: If set resize the resulting image to this height (in px)
    :type height: int
    :param opacity: The opacity of the watermark (0 to 100)
    :type opacity: int
    :param position: The position of the watermark image, possible values are: &lt;br&gt;center, top-left, top-center, top-right, bottom-left, bottom-center, bottom-right
    :type position: str
    :param resize_mode: The resize mode to use, we support 3 main resizing modes: &lt;ul&gt; &lt;li&gt;&lt;b&gt;scale&lt;/b&gt;&lt;br&gt;Resize to within the width and height specified while preserving aspect ratio. In this mode the width or height will be automatically adjusted to fit the aspect ratio&lt;/li&gt; &lt;li&gt;&lt;b&gt;pad&lt;/b&gt;&lt;br&gt;Resize to exactly the width and height specified while preserving aspect ratio and pad any space left over. Any padded space will be filled in with the &#39;bg-color&#39; value&lt;/li&gt; &lt;li&gt;&lt;b&gt;crop&lt;/b&gt;&lt;br&gt;Resize to exactly the width and height specified while preserving aspect ratio and crop any space which fall outside the area. The cropping window is centered on the original image&lt;/li&gt; &lt;/ul&gt;
    :type resize_mode: str
    :param width: If set resize the resulting image to this width (in px)
    :type width: int

    """
    return web.Response(status=200)


async def q_r_code(request: web.Request, content, bg_color=None, fg_color=None, height=None, width=None) -> web.Response:
    """QR Code

    Generate a QR code as a PNG image

    :param content: The content to encode into the QR code (e.g. a URL or a phone number)
    :type content: str
    :param bg_color: The QR code background color
    :type bg_color: str
    :param fg_color: The QR code foreground color
    :type fg_color: str
    :param height: The height of the QR code (in px)
    :type height: int
    :param width: The width of the QR code (in px)
    :type width: int

    """
    return web.Response(status=200)
