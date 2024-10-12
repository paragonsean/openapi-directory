from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def document(request: web.Request, output_format, api_key, project_id) -> web.Response:
    """Project Details

    

    :param output_format: Response Format
    :type output_format: str
    :param api_key: API Key
    :type api_key: str
    :param project_id: Project ID
    :type project_id: int

    """
    return web.Response(status=200)


async def project(request: web.Request, output_format, api_key, search=None, portal=None, page=None, city=None, province=None, region=None) -> web.Response:
    """A filterable list of projects.

    

    :param output_format: Response Format
    :type output_format: str
    :param api_key: API Key
    :type api_key: str
    :param search: Search Text
    :type search: str
    :param portal: Portal ID
    :type portal: str
    :param page: Page Number
    :type page: int
    :param city: City
    :type city: str
    :param province: State or Province (ex: &#39;CO&#39;, &#39;AZ&#39;)
    :type province: str
    :param region: Climate Region.  Use integer from mapping (256: &#39;1A: Very Hot - Humid&#39;, 257: &#39;1B: Very Hot - Dry&#39;, 258: &#39;2A: Hot - Humid&#39;, 259: &#39;2B: Hot - Dry&#39;, 260: &#39;3A: Warm - Humid&#39;, 261: &#39;3B: Warm - Dry&#39;, 262: &#39;3C: Warm - Marine&#39;, 263: &#39;4A: Mixed - Humid&#39;, 264: &#39;4B: Mixed - Dry&#39;, 265: &#39;4C: Mixed - Marine&#39;, 266: &#39;5A: Cool - Humid&#39;, 267: &#39;5B: Cool - Dry&#39;, 268: &#39;5C: Cool - Marine&#39;, 269: &#39;6A: Cold - Humid&#39;, 270: &#39;6B: Cold - Dry&#39;, 271: &#39;7: Very Cold&#39;, 272: &#39;8: Subarctic&#39;)
    :type region: str

    """
    return web.Response(status=200)
