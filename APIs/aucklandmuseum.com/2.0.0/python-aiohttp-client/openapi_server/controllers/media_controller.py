from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def get_media(request: web.Request, path, rendering=None) -> web.Response:
    """Retrieve media associated with Collections and Cenotaph subjects in Auckland Museum

    Gets &#x60;media&#x60; at a given path 

    :param path: The media &#x60;identifier&#x60; 
    :type path: str
    :param rendering: The desired media &#x60;rendering&#x60;  Possible values: * &#x60;original.jpg&#x60; * &#x60;original.pdf&#x60; * &#x60;thumbnail.jpg&#x60; (fixed with 70px) * &#x60;standard.jpg&#x60; (fixed width 440px and height 440px) * &#x60;preview.jpg&#x60; (fixed height 100px) 
    :type rendering: str

    """
    return web.Response(status=200)
