from typing import List, Dict
from aiohttp import web

from openapi_server.models.job_resource import JobResource
from openapi_server import util


async def backup_crr_job_details_get(request: web.Request, api_version, azure_region, subscription_id) -> web.Response:
    """Get CRR job details from target region.

    

    :param api_version: Client Api Version.
    :type api_version: str
    :param azure_region: Azure region to hit Api
    :type azure_region: str
    :param subscription_id: The subscription Id.
    :type subscription_id: str

    """
    return web.Response(status=200)
