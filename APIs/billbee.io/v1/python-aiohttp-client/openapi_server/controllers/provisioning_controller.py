from typing import List, Dict
from aiohttp import web

from openapi_server.models.rechnungsdruck_web_app_controllers_api_automatic_provisioning_controller_create_account_container import RechnungsdruckWebAppControllersApiAutomaticProvisioningControllerCreateAccountContainer
from openapi_server import util


async def automatic_provisioning_create_account(request: web.Request, body) -> web.Response:
    """Creates a new Billbee user account with the data passed

    

    :param body: 
    :type body: dict | bytes

    """
    body = RechnungsdruckWebAppControllersApiAutomaticProvisioningControllerCreateAccountContainer.from_dict(body)
    return web.Response(status=200)


async def automatic_provisioning_terms_info(request: web.Request, ) -> web.Response:
    """Returns infos about Billbee terms and conditions

    


    """
    return web.Response(status=200)
