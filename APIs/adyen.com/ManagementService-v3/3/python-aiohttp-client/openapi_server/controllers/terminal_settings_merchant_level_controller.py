from typing import List, Dict
from aiohttp import web

from openapi_server.models.logo import Logo
from openapi_server.models.rest_service_error import RestServiceError
from openapi_server.models.terminal_settings import TerminalSettings
from openapi_server import util


async def get_merchants_merchant_id_terminal_logos(request: web.Request, merchant_id, model) -> web.Response:
    """Get the terminal logo

    Returns the logo that is configured for a specific payment terminal model at the merchant account identified in the path.  The logo is returned as a Base64-encoded string. You need to Base64-decode the string to get the actual image file.  This logo applies to all terminals of the specified model under the merchant account, unless a different logo is configured at a lower level (store or individual terminal).  To make this request, your API credential must have one of the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Terminal settings read * Management API—Terminal settings read and write

    :param merchant_id: The unique identifier of the merchant account.
    :type merchant_id: str
    :param model: The terminal model. Possible values: E355, VX675WIFIBT, VX680, VX690, VX700, VX820, M400, MX925, P400Plus, UX300, UX410, V200cPlus, V240mPlus, V400cPlus, V400m, e280, e285, e285p, S1E, S1EL, S1F2, S1L, S1U, S7T.
    :type model: str

    """
    return web.Response(status=200)


async def get_merchants_merchant_id_terminal_settings(request: web.Request, merchant_id) -> web.Response:
    """Get terminal settings

    Returns the payment terminal settings that are configured for the merchant account identified in the path. These settings apply to all terminals under the merchant account unless different values are configured at a lower level (store or individual terminal).  To make this request, your API credential must have one of the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Terminal settings read * Management API—Terminal settings read and write

    :param merchant_id: The unique identifier of the merchant account.
    :type merchant_id: str

    """
    return web.Response(status=200)


async def patch_merchants_merchant_id_terminal_logos(request: web.Request, merchant_id, model, body=None) -> web.Response:
    """Update the terminal logo

    Updates the logo for a specific payment terminal model at the merchant account identified in the path. You can update the logo for only one terminal model at a time.  This logo applies to all terminals of the specified model under the merchant account, unless a different logo is configured at a lower level (store or individual terminal).  * To change the logo, specify the image file as a Base64-encoded string. * To restore the logo inherited from the company account, specify an empty logo value.  To make this request, your API credential must have the following [role](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Terminal settings read and write

    :param merchant_id: The unique identifier of the merchant account.
    :type merchant_id: str
    :param model: The terminal model. Allowed values: E355, VX675WIFIBT, VX680, VX690, VX700, VX820, M400, MX925, P400Plus, UX300, UX410, V200cPlus, V240mPlus, V400cPlus, V400m, e280, e285, e285p, S1E, S1EL, S1F2, S1L, S1U, S7T.
    :type model: str
    :param body: 
    :type body: dict | bytes

    """
    body = Logo.from_dict(body)
    return web.Response(status=200)


async def patch_merchants_merchant_id_terminal_settings(request: web.Request, merchant_id, body=None) -> web.Response:
    """Update terminal settings

    Updates payment terminal settings for the merchant account identified in the path. These settings apply to all terminals under the merchant account, unless different values are configured at a lower level (store or individual terminal).  * To change a parameter value, include the full object that contains the parameter, even if you don&#39;t want to change all parameters in the object. * To restore a parameter value inherited from a higher level, include the full object that contains the parameter, and specify an empty value for the parameter or omit the parameter. * Objects that are not included in the request are not updated.  To make this request, your API credential must have the following [role](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Terminal settings read and write

    :param merchant_id: The unique identifier of the merchant account.
    :type merchant_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = TerminalSettings.from_dict(body)
    return web.Response(status=200)
