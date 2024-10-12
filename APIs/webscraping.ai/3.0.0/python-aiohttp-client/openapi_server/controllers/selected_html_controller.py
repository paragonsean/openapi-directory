from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.page_error import PageError
from openapi_server import util


async def get_selected(request: web.Request, url, selector=None, headers=None, timeout=None, js=None, js_timeout=None, proxy=None, country=None, device=None, error_on_404=None, error_on_redirect=None) -> web.Response:
    """HTML of a selected page area by URL and CSS selector

    Returns just HTML on success, JSON on error

    :param url: URL of the target page
    :type url: str
    :param selector: CSS selector (null by default, returns whole page HTML)
    :type selector: str
    :param headers: HTTP headers to pass to the target page. Can be specified either via a nested query parameter (...&amp;headers[One]&#x3D;value1&amp;headers&#x3D;[Another]&#x3D;value2) or as a JSON encoded object (...&amp;headers&#x3D;{\&quot;One\&quot;: \&quot;value1\&quot;, \&quot;Another\&quot;: \&quot;value2\&quot;})
    :type headers: Dict[str, ]
    :param timeout: Maximum processing time in ms. Increase it in case of timeout errors (10000 by default, maximum is 30000)
    :type timeout: int
    :param js: Execute on-page JavaScript using a headless browser (true by default)
    :type js: bool
    :param js_timeout: Maximum JavaScript rendering time in ms. Increase it in case if you see a loading indicator instead of data on the target page.
    :type js_timeout: int
    :param proxy: Type of proxy, use residential proxies if your site restricts traffic from datacenters (datacenter by default). Note that residential proxy requests are more expensive than datacenter, see the pricing page for details.
    :type proxy: str
    :param country: Country of the proxy to use (US by default). Only available on Startup and Custom plans.
    :type country: str
    :param device: Type of device emulation.
    :type device: str
    :param error_on_404: Return error on 404 HTTP status on the target page (false by default).
    :type error_on_404: bool
    :param error_on_redirect: Return error on redirect on the target page (false by default).
    :type error_on_redirect: bool

    """
    return web.Response(status=200)


async def get_selected_multiple(request: web.Request, url, selectors=None, headers=None, timeout=None, js=None, js_timeout=None, proxy=None, country=None, device=None, error_on_404=None, error_on_redirect=None) -> web.Response:
    """HTML of multiple page areas by URL and CSS selectors

    Always returns JSON

    :param url: URL of the target page
    :type url: str
    :param selectors: Multiple CSS selectors (null by default, returns whole page HTML)
    :type selectors: List[str]
    :param headers: HTTP headers to pass to the target page. Can be specified either via a nested query parameter (...&amp;headers[One]&#x3D;value1&amp;headers&#x3D;[Another]&#x3D;value2) or as a JSON encoded object (...&amp;headers&#x3D;{\&quot;One\&quot;: \&quot;value1\&quot;, \&quot;Another\&quot;: \&quot;value2\&quot;})
    :type headers: Dict[str, ]
    :param timeout: Maximum processing time in ms. Increase it in case of timeout errors (10000 by default, maximum is 30000)
    :type timeout: int
    :param js: Execute on-page JavaScript using a headless browser (true by default)
    :type js: bool
    :param js_timeout: Maximum JavaScript rendering time in ms. Increase it in case if you see a loading indicator instead of data on the target page.
    :type js_timeout: int
    :param proxy: Type of proxy, use residential proxies if your site restricts traffic from datacenters (datacenter by default). Note that residential proxy requests are more expensive than datacenter, see the pricing page for details.
    :type proxy: str
    :param country: Country of the proxy to use (US by default). Only available on Startup and Custom plans.
    :type country: str
    :param device: Type of device emulation.
    :type device: str
    :param error_on_404: Return error on 404 HTTP status on the target page (false by default).
    :type error_on_404: bool
    :param error_on_redirect: Return error on redirect on the target page (false by default).
    :type error_on_redirect: bool

    """
    return web.Response(status=200)
