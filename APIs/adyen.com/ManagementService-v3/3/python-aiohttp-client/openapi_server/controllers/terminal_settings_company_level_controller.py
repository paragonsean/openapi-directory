from typing import List, Dict
from aiohttp import web

from openapi_server.models.logo import Logo
from openapi_server.models.rest_service_error import RestServiceError
from openapi_server.models.terminal_settings import TerminalSettings
from openapi_server import util


async def get_companies_company_id_terminal_logos(request: web.Request, company_id, model) -> web.Response:
    """Get the terminal logo

    Returns the logo that is configured for a specific payment terminal model at the company identified in the path.   The logo is returned as a Base64-encoded string. You need to Base64-decode the string to get the actual image file.  This logo applies to all terminals of the specified model under the company, unless a different logo is configured at a lower level (merchant account, store, or individual terminal).  To make this request, your API credential must have one of the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Terminal settings read * Management API—Terminal settings read and write

    :param company_id: The unique identifier of the company account.
    :type company_id: str
    :param model: The terminal model. Possible values: E355, VX675WIFIBT, VX680, VX690, VX700, VX820, M400, MX925, P400Plus, UX300, UX410, V200cPlus, V240mPlus, V400cPlus, V400m, e280, e285, e285p, S1E, S1EL, S1F2, S1L, S1U, S7T.
    :type model: str

    """
    return web.Response(status=200)


async def get_companies_company_id_terminal_settings(request: web.Request, company_id) -> web.Response:
    """Get terminal settings

    Returns the payment terminal settings that are configured for the company identified in the path. These settings apply to all terminals under the company, unless different values are configured at a lower level (merchant account, store, or individual terminal).  To make this request, your API credential must have one of the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Terminal settings read * Management API—Terminal settings read and write  For [sensitive terminal settings](https://docs.adyen.com/point-of-sale/automating-terminal-management/configure-terminals-api#sensitive-terminal-settings), your API credential must have the following role: * Management API—Terminal settings Advanced read and write

    :param company_id: The unique identifier of the company account.
    :type company_id: str

    """
    return web.Response(status=200)


async def patch_companies_company_id_terminal_logos(request: web.Request, company_id, model, body=None) -> web.Response:
    """Update the terminal logo

    Updates the logo that is configured for a specific payment terminal model at the company identified in the path. You can update the logo for only one terminal model at a time. This logo applies to all terminals of the specified model under the company, unless a different logo is configured at a lower level (merchant account, store, or individual terminal).  * To change the logo, specify the image file as a Base64-encoded string. * To restore the logo inherited from the Adyen PSP level, specify an empty logo value.  To make this request, your API credential must have the following [role](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Terminal settings read and write

    :param company_id: The unique identifier of the company account.
    :type company_id: str
    :param model: The terminal model. Possible values: E355, VX675WIFIBT, VX680, VX690, VX700, VX820, M400, MX925, P400Plus, UX300, UX410, V200cPlus, V240mPlus, V400cPlus, V400m, e280, e285, e285p, S1E, S1EL, S1F2, S1L, S1U, S7T.
    :type model: str
    :param body: 
    :type body: dict | bytes

    """
    body = Logo.from_dict(body)
    return web.Response(status=200)


async def patch_companies_company_id_terminal_settings(request: web.Request, company_id, body=None) -> web.Response:
    """Update terminal settings

    Updates payment terminal settings for the company identified in the path. These settings apply to all terminals under the company, unless different values are configured at a lower level (merchant account, store, or individual terminal).  * To change a parameter value, include the full object that contains the parameter, even if you don&#39;t want to change all parameters in the object. * To restore a parameter value inherited from the Adyen PSP level, include the full object that contains the parameter, and specify an empty value for the parameter or omit the parameter. * Objects that are not included in the request are not updated.  To make this request, your API credential must have the following [role](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Terminal settings read and write  For [sensitive terminal settings](https://docs.adyen.com/point-of-sale/automating-terminal-management/configure-terminals-api#sensitive-terminal-settings), your API credential must have the following role: * Management API—Terminal settings Advanced read and write

    :param company_id: The unique identifier of the company account.
    :type company_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = TerminalSettings.from_dict(body)
    return web.Response(status=200)
