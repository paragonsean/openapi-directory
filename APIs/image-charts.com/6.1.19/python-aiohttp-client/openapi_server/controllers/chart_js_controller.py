from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def get_chartjs280(request: web.Request, c=None, chart=None, width=None, height=None, background_color=None, bkg=None, encoding=None, icac=None, ichm=None, icretina=None) -> web.Response:
    """Chart.js as image API

    Image-charts

    :param c: Javascript/JSON definition of the chart. Use a Chart.js configuration object.
    :type c: str
    :param chart: Javascript/JSON definition of the chart. Use a Chart.js configuration object.
    :type chart: str
    :param width: Width of the chart
    :type width: int
    :param height: Height of the chart
    :type height: int
    :param background_color: Background of the chart canvas. Accepts rgb (rgb(255,255,120)), colors (red), and url-encoded hex values (%23ff00ff). Abbreviated as \&quot;bkg\&quot;
    :type background_color: str
    :param bkg: Background of the chart canvas. Accepts rgb (rgb(255,255,120)), colors (red), and url-encoded hex values (%23ff00ff). Abbreviated as \&quot;bkg\&quot;
    :type bkg: str
    :param encoding: Encoding of your \&quot;chart\&quot; parameter. Accepted values are url and base64.
    :type encoding: str
    :param icac: image-charts enterprise &#x60;account_id&#x60;
    :type icac: str
    :param ichm: HMAC-SHA256 signature required to activate paid features
    :type ichm: str
    :param icretina: retina mode
    :type icretina: str

    """
    return web.Response(status=200)
