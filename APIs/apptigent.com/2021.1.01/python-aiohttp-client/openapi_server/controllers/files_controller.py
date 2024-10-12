from typing import List, Dict
from aiohttp import web

from openapi_server.models.input_qr_code import InputQRCode
from openapi_server.models.output_string import OutputString
from openapi_server import util


async def convert_image(request: web.Request, file, format) -> web.Response:
    """Files - Convert Image

    Convert an image from one format to another

    :param file: Source image file
    :type file: str
    :param format: Output file format
    :type format: str

    """
    return web.Response(status=200)


async def crop_image(request: web.Request, height, width, file, position) -> web.Response:
    """Files - Crop Image

    Crop an image

    :param height: Height (Y-axis down, negative to reverse)
    :type height: 
    :param width: Width (X-axis right, negative to reverse)
    :type width: 
    :param file: Source image file
    :type file: str
    :param position: Crop start position (use negative values to reverse crop area)
    :type position: str

    """
    return web.Response(status=200)


async def file_to_string(request: web.Request, file) -> web.Response:
    """Files - File to string

    Convert a file to a Base64 string

    :param file: Source file (10MB limit)
    :type file: str

    """
    return web.Response(status=200)


async def flip_image(request: web.Request, file, orientation) -> web.Response:
    """Files - Flip Image

    Flip an image (horizontal or vertical)

    :param file: Source image file
    :type file: str
    :param orientation: Horizontal or Vertical
    :type orientation: str

    """
    return web.Response(status=200)


async def generate_qr_code(request: web.Request, input_qr_code=None) -> web.Response:
    """Files - Generate QR code

    Generate a QR code image

    :param input_qr_code: 
    :type input_qr_code: dict | bytes

    """
    input_qr_code = InputQRCode.from_dict(input_qr_code)
    return web.Response(status=200)


async def resize_image(request: web.Request, algorithm, file, units, height=None, width=None) -> web.Response:
    """Files - Resize Image

    Resize an image

    :param algorithm: Optimize output quality of the target image
    :type algorithm: str
    :param file: Source image file
    :type file: str
    :param units: Image adjustment units
    :type units: str
    :param height: Image height (pixels or percent)
    :type height: 
    :param width: Image width (pixels or percent)
    :type width: 

    """
    return web.Response(status=200)


async def rotate_image(request: web.Request, degrees, file) -> web.Response:
    """Files - Rotate Image

    Rotate an image by specified number of degrees

    :param degrees: Number of degrees
    :type degrees: str
    :param file: Source image file
    :type file: str

    """
    return web.Response(status=200)


async def watermark_image(request: web.Request, color, file, font, horizontal, size, text, vertical) -> web.Response:
    """Files - Watermark Image

    Add watermark text to an image

    :param color: Text color hex value
    :type color: str
    :param file: Source image file
    :type file: str
    :param font: Text font
    :type font: str
    :param horizontal: Horizontal alignment
    :type horizontal: str
    :param size: Font size (points)
    :type size: 
    :param text: Watermark text
    :type text: str
    :param vertical: Vertical alignment
    :type vertical: str

    """
    return web.Response(status=200)
