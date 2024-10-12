from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def job_cancellations_trigger(request: web.Request, api_version, vault_name, resource_group_name, subscription_id, job_name) -> web.Response:
    """job_cancellations_trigger

    Cancels the job. This is an asynchronous operation. To know the status of the cancellation, call the GetCancelOperationResult API.

    :param api_version: Client API version.
    :type api_version: str
    :param vault_name: The name of the Recovery Services vault.
    :type vault_name: str
    :param resource_group_name: The name of the resource group associated with the Recovery Services vault.
    :type resource_group_name: str
    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param job_name: Name of the job to cancel.
    :type job_name: str

    """
    return web.Response(status=200)
