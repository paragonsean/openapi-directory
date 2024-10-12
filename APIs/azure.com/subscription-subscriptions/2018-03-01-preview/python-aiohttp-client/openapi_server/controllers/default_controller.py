from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.subscription_creation_parameters import SubscriptionCreationParameters
from openapi_server.models.subscription_creation_result import SubscriptionCreationResult
from openapi_server.models.subscription_operation_list_result import SubscriptionOperationListResult
from openapi_server import util


async def subscription_factory_create_subscription_in_enrollment_account(request: web.Request, enrollment_account_name, api_version, body) -> web.Response:
    """subscription_factory_create_subscription_in_enrollment_account

    Creates an Azure subscription

    :param enrollment_account_name: The name of the enrollment account to which the subscription will be billed.
    :type enrollment_account_name: str
    :param api_version: Version of the API to be used with the client request. Current version is 2015-06-01
    :type api_version: str
    :param body: The subscription creation parameters.
    :type body: dict | bytes

    """
    body = SubscriptionCreationParameters.from_dict(body)
    return web.Response(status=200)


async def subscription_operations_list(request: web.Request, api_version) -> web.Response:
    """subscription_operations_list

    Lists all of the available pending Microsoft.Subscription API operations.

    :param api_version: Version of the API to be used with the client request. Current version is 2015-06-01
    :type api_version: str

    """
    return web.Response(status=200)
