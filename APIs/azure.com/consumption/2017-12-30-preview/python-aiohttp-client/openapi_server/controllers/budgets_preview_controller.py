from typing import List, Dict
from aiohttp import web

from openapi_server.models.budget import Budget
from openapi_server.models.budgets_list_result import BudgetsListResult
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def budgets_create_or_update(request: web.Request, api_version, subscription_id, name, parameters) -> web.Response:
    """budgets_create_or_update

    The operation to create or update a budget. Update operation requires latest eTag to be set in the request mandatorily. You may obtain the latest eTag by performing a get operation. Create operation does not require eTag.

    :param api_version: Version of the API to be used with the client request. The current version is 2017-12-30-preview.
    :type api_version: str
    :param subscription_id: Azure Subscription ID.
    :type subscription_id: str
    :param name: Budget name.
    :type name: str
    :param parameters: Parameters supplied to the Create Budget operation.
    :type parameters: dict | bytes

    """
    parameters = Budget.from_dict(parameters)
    return web.Response(status=200)


async def budgets_delete(request: web.Request, api_version, subscription_id, name) -> web.Response:
    """budgets_delete

    The operation to delete a budget.

    :param api_version: Version of the API to be used with the client request. The current version is 2017-12-30-preview.
    :type api_version: str
    :param subscription_id: Azure Subscription ID.
    :type subscription_id: str
    :param name: Budget name.
    :type name: str

    """
    return web.Response(status=200)


async def budgets_get(request: web.Request, api_version, subscription_id, name) -> web.Response:
    """budgets_get

    Gets the budget for a subscription by budget name.

    :param api_version: Version of the API to be used with the client request. The current version is 2017-12-30-preview.
    :type api_version: str
    :param subscription_id: Azure Subscription ID.
    :type subscription_id: str
    :param name: Budget name.
    :type name: str

    """
    return web.Response(status=200)


async def budgets_list(request: web.Request, api_version, subscription_id) -> web.Response:
    """budgets_list

    Lists all budgets for a subscription.

    :param api_version: Version of the API to be used with the client request. The current version is 2017-12-30-preview.
    :type api_version: str
    :param subscription_id: Azure Subscription ID.
    :type subscription_id: str

    """
    return web.Response(status=200)
