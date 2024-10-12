from typing import List, Dict
from aiohttp import web

from openapi_server.models.list_workspace_quotas import ListWorkspaceQuotas
from openapi_server.models.machine_learning_service_error import MachineLearningServiceError
from openapi_server.models.quota_update_parameters import QuotaUpdateParameters
from openapi_server.models.update_workspace_quotas_result import UpdateWorkspaceQuotasResult
from openapi_server import util


async def quotas_list(request: web.Request, api_version, subscription_id, location) -> web.Response:
    """quotas_list

    Gets the currently assigned Workspace Quotas based on VMFamily.

    :param api_version: Version of Azure Machine Learning resource provider API.
    :type api_version: str
    :param subscription_id: Azure subscription identifier.
    :type subscription_id: str
    :param location: The location for which resource usage is queried.
    :type location: str

    """
    return web.Response(status=200)


async def quotas_update(request: web.Request, location, api_version, subscription_id, parameters) -> web.Response:
    """quotas_update

    Update quota for each VM family in workspace.

    :param location: The location for update quota is queried.
    :type location: str
    :param api_version: Version of Azure Machine Learning resource provider API.
    :type api_version: str
    :param subscription_id: Azure subscription identifier.
    :type subscription_id: str
    :param parameters: Quota update parameters.
    :type parameters: dict | bytes

    """
    parameters = QuotaUpdateParameters.from_dict(parameters)
    return web.Response(status=200)
