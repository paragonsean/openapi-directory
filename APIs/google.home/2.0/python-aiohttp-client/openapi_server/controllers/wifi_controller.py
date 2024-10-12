from typing import List, Dict
from aiohttp import web

from openapi_server.models.connectto_wi_fi_network_request import ConnecttoWiFiNetworkRequest
from openapi_server.models.example113 import Example113
from openapi_server.models.example114 import Example114
from openapi_server.models.forget_wi_fi_network_request import ForgetWiFiNetworkRequest
from openapi_server import util


async def connectto_wi_fi_network(request: web.Request, body) -> web.Response:
    """Connect to Wi-Fi Network

    **Note:** Not sure how the password is encrypted. Might be using the public certificate from /setup/eureka_info. So this cannot be used as of now. If someone figures it out, please [create a new issue here](https://github.com/rithvikvibhu/GHLocalApi/issues/new).

    :param body: 
    :type body: dict | bytes

    """
    body = ConnecttoWiFiNetworkRequest.from_dict(body)
    return web.Response(status=200)


async def forget_wi_fi_network(request: web.Request, body) -> web.Response:
    """Forget Wi-Fi Network

    This is to forget a saved network by &#x60;wpa_id&#x60;. Get the &#x60;wpa_id&#x60; from /setup/configured_networks

    :param body: 
    :type body: dict | bytes

    """
    body = ForgetWiFiNetworkRequest.from_dict(body)
    return web.Response(status=200)


async def get_saved_networks(request: web.Request, ) -> web.Response:
    """Get Saved Networks

    This gets a list of all saved Wi-Fi networks.  Each network has &#x60;ssid&#x60;, &#x60;wpa_auth&#x60;, &#x60;wpa_cipher&#x60; and &#x60;wpa_id&#x60;.   &#x60;wpa_id&#x60; is an incrementing number used to identify a saved network.   #TODO: Add values for &#x60;wpa_auth&#x60; and &#x60;wpa_cipher&#x60;.


    """
    return web.Response(status=200)


async def get_wi_fi_scan_results(request: web.Request, ) -> web.Response:
    """Get Wi-Fi Scan Results

    This gets a list of all nearby Wi-Fi access points.  The list only has the connected AP by default. Once a scan is triggered by &#x60;/setup/scan_wifi&#x60;, the whole list is cached for ~3 minutes. Then it will revert to returning only the connected AP again.


    """
    return web.Response(status=200)


async def scanfor_networks(request: web.Request, ) -> web.Response:
    """Scan for Networks

    This initiates scanning for Wi-Fi networks.  The results can be obtained with &#x60;/setup/scan_results&#x60; after triggering the scan with this request.


    """
    return web.Response(status=200)
