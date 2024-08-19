from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.hybrid_use_benefit_model import HybridUseBenefitModel
from openapi_server import util


async def hybrid_use_benefit_create(request: web.Request, scope, plan_id, api_version, body) -> web.Response:
    """hybrid_use_benefit_create

    Create a new hybrid use benefit under a given scope

    :param scope: The scope at which the operation is performed. This is limited to Microsoft.Compute/virtualMachines and Microsoft.Compute/hostGroups/hosts for now
    :type scope: str
    :param plan_id: This is a unique identifier for a plan. Should be a guid.
    :type plan_id: str
    :param api_version: The api-version to be used by the service
    :type api_version: str
    :param body: Request body for creating a hybrid use benefit
    :type body: dict | bytes

    """
    body = HybridUseBenefitModel.from_dict(body)
    return web.Response(status=200)


async def hybrid_use_benefit_delete(request: web.Request, scope, plan_id, api_version) -> web.Response:
    """hybrid_use_benefit_delete

    Deletes a given plan ID

    :param scope: The scope at which the operation is performed. This is limited to Microsoft.Compute/virtualMachines and Microsoft.Compute/hostGroups/hosts for now
    :type scope: str
    :param plan_id: This is a unique identifier for a plan. Should be a guid.
    :type plan_id: str
    :param api_version: The api-version to be used by the service
    :type api_version: str

    """
    return web.Response(status=200)


async def hybrid_use_benefit_get(request: web.Request, scope, plan_id, api_version) -> web.Response:
    """hybrid_use_benefit_get

    Gets a given plan ID

    :param scope: The scope at which the operation is performed. This is limited to Microsoft.Compute/virtualMachines and Microsoft.Compute/hostGroups/hosts for now
    :type scope: str
    :param plan_id: This is a unique identifier for a plan. Should be a guid.
    :type plan_id: str
    :param api_version: The api-version to be used by the service
    :type api_version: str

    """
    return web.Response(status=200)


async def hybrid_use_benefit_update(request: web.Request, scope, plan_id, api_version, body) -> web.Response:
    """hybrid_use_benefit_update

    Updates an existing hybrid use benefit

    :param scope: The scope at which the operation is performed. This is limited to Microsoft.Compute/virtualMachines and Microsoft.Compute/hostGroups/hosts for now
    :type scope: str
    :param plan_id: This is a unique identifier for a plan. Should be a guid.
    :type plan_id: str
    :param api_version: The api-version to be used by the service
    :type api_version: str
    :param body: Request body for creating a hybrid use benefit
    :type body: dict | bytes

    """
    body = HybridUseBenefitModel.from_dict(body)
    return web.Response(status=200)
