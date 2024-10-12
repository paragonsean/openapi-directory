from typing import List, Dict
from aiohttp import web

from openapi_server.models.external_terminal_action import ExternalTerminalAction
from openapi_server.models.list_external_terminal_actions_response import ListExternalTerminalActionsResponse
from openapi_server.models.rest_service_error import RestServiceError
from openapi_server import util


async def get_companies_company_id_terminal_actions(request: web.Request, company_id, page_number=None, page_size=None, status=None, type=None) -> web.Response:
    """Get a list of terminal actions

    Returns the [terminal actions](https://docs.adyen.com/point-of-sale/automating-terminal-management/terminal-actions-api) that have been scheduled for the company identified in the path.The response doesn&#39;t include actions that are scheduled by Adyen. To make this request, your API credential must have one of the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Terminal actions read * Management API—Terminal actions read and write

    :param company_id: The unique identifier of the company account.
    :type company_id: str
    :param page_number: The number of the page to fetch.
    :type page_number: int
    :param page_size: The number of items to have on a page, maximum 100. The default is 20 items on a page.
    :type page_size: int
    :param status: Returns terminal actions with the specified status.  Allowed values: **pending**, **successful**, **failed**, **cancelled**, **tryLater**.
    :type status: str
    :param type: Returns terminal actions of the specified type.  Allowed values: **InstallAndroidApp**, **UninstallAndroidApp**, **InstallAndroidCertificate**, **UninstallAndroidCertificate**.
    :type type: str

    """
    return web.Response(status=200)


async def get_companies_company_id_terminal_actions_action_id(request: web.Request, company_id, action_id) -> web.Response:
    """Get terminal action

    Returns the details of the [terminal action](https://docs.adyen.com/point-of-sale/automating-terminal-management/terminal-actions-api) identified in the path. To make this request, your API credential must have one of the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Terminal actions read * Management API—Terminal actions read and write

    :param company_id: The unique identifier of the company account.
    :type company_id: str
    :param action_id: The unique identifier of the terminal action.
    :type action_id: str

    """
    return web.Response(status=200)
