from typing import List, Dict
from aiohttp import web

from openapi_server.models.logo import Logo
from openapi_server.models.rest_service_error import RestServiceError
from openapi_server.models.terminal_settings import TerminalSettings
from openapi_server import util


async def get_terminals_terminal_id_terminal_logos(request: web.Request, terminal_id) -> web.Response:
    """Get the terminal logo

    Returns the logo that is configured for the payment terminal identified in the path. The logo is returned as a Base64-encoded string. You need to Base64-decode the string to get the actual image file.  To make this request, your API credential must have one of the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Terminal settings read * Management API—Terminal settings read and write

    :param terminal_id: The unique identifier of the payment terminal.
    :type terminal_id: str

    """
    return web.Response(status=200)


async def get_terminals_terminal_id_terminal_settings(request: web.Request, terminal_id) -> web.Response:
    """Get terminal settings

    Returns the settings that are configured for the payment terminal identified in the path.  To make this request, your API credential must have one of the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Terminal settings read * Management API—Terminal settings read and write  For [sensitive terminal settings](https://docs.adyen.com/point-of-sale/automating-terminal-management/configure-terminals-api#sensitive-terminal-settings), your API credential must have the following role: * Management API—Terminal settings Advanced read and write

    :param terminal_id: The unique identifier of the payment terminal.
    :type terminal_id: str

    """
    return web.Response(status=200)


async def patch_terminals_terminal_id_terminal_logos(request: web.Request, terminal_id, body=None) -> web.Response:
    """Update the logo

    Updates the logo for the payment terminal identified in the path.  * To change the logo, specify the image file as a Base64-encoded string. * To restore the logo inherited from a higher level (store, merchant account, or company account), specify an empty logo value.  To make this request, your API credential must have the following [role](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Terminal settings read and write

    :param terminal_id: The unique identifier of the payment terminal.
    :type terminal_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = Logo.from_dict(body)
    return web.Response(status=200)


async def patch_terminals_terminal_id_terminal_settings(request: web.Request, terminal_id, body=None) -> web.Response:
    """Update terminal settings

    Updates the settings that are configured for the payment terminal identified in the path.  * To change a parameter value, include the full object that contains the parameter, even if you don&#39;t want to change all parameters in the object. * To restore a parameter value inherited from a higher level, include the full object that contains the parameter, and specify an empty value for the parameter or omit the parameter. * Objects that are not included in the request are not updated.  To make this request, your API credential must have the following [role](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Terminal settings read and write  For [sensitive terminal settings](https://docs.adyen.com/point-of-sale/automating-terminal-management/configure-terminals-api#sensitive-terminal-settings), your API credential must have the following role: * Management API—Terminal settings Advanced read and write

    :param terminal_id: The unique identifier of the payment terminal.
    :type terminal_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = TerminalSettings.from_dict(body)
    return web.Response(status=200)
