from typing import List, Dict
from aiohttp import web

from openapi_server.models.rechnungsdruck_web_app_controllers_api_api_result_system_collections_generic_list_billbee_interfaces_billbee_api_model_cloud_storage_api_model import RechnungsdruckWebAppControllersApiApiResultSystemCollectionsGenericListBillbeeInterfacesBillbeeAPIModelCloudStorageApiModel
from openapi_server import util


async def cloud_storage_api_get_list(request: web.Request, ) -> web.Response:
    """Gets a list of all connected cloud storage devices

    


    """
    return web.Response(status=200)
