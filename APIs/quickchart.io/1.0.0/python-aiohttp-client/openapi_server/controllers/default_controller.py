from typing import List, Dict
from aiohttp import web

from openapi_server.models.chart_post_request import ChartPostRequest
from openapi_server.models.qr_post_request import QrPostRequest
from openapi_server import util


async def chart_get(request: web.Request, chart=None, width=None, height=None, format=None, background_color=None) -> web.Response:
    """Generate a chart (GET)

    Generate a chart based on the provided parameters.

    :param chart: The chart configuration in Chart.js format (JSON or Javascript).
    :type chart: str
    :param width: The width of the chart in pixels.
    :type width: int
    :param height: The height of the chart in pixels.
    :type height: int
    :param format: The output format of the chart, &#39;png&#39;, &#39;jpg&#39;, &#39;svg&#39;, or &#39;webp&#39;.
    :type format: str
    :param background_color: The background color of the chart.
    :type background_color: str

    """
    return web.Response(status=200)


async def chart_post(request: web.Request, body) -> web.Response:
    """Generate a chart (POST)

    Generate a chart based on the provided configuration in the request body.

    :param body: 
    :type body: dict | bytes

    """
    body = ChartPostRequest.from_dict(body)
    return web.Response(status=200)


async def qr_get(request: web.Request, text=None, width=None, height=None, format=None, margin=None) -> web.Response:
    """Generate a QR code (GET)

    Generate a QR code based on the provided parameters.

    :param text: The text to be encoded in the QR code.
    :type text: str
    :param width: The width of the QR code in pixels.
    :type width: int
    :param height: The height of the QR code in pixels.
    :type height: int
    :param format: The output format of the QR code, e.g., &#39;png&#39; or &#39;svg&#39;.
    :type format: str
    :param margin: The margin around the QR code in pixels.
    :type margin: int

    """
    return web.Response(status=200)


async def qr_post(request: web.Request, body) -> web.Response:
    """Generate a QR code (POST)

    Generate a QR code based on the provided configuration in the request body.

    :param body: 
    :type body: dict | bytes

    """
    body = QrPostRequest.from_dict(body)
    return web.Response(status=200)
