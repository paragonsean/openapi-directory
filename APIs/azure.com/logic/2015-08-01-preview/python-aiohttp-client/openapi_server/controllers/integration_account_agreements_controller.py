from typing import List, Dict
from aiohttp import web

from openapi_server.models.integration_account_agreement import IntegrationAccountAgreement
from openapi_server.models.integration_account_agreement_list_result import IntegrationAccountAgreementListResult
from openapi_server import util


async def integration_account_agreements_create_or_update(request: web.Request, subscription_id, resource_group_name, integration_account_name, agreement_name, api_version, agreement) -> web.Response:
    """integration_account_agreements_create_or_update

    Creates or updates an integration account agreement.

    :param subscription_id: The subscription id.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param integration_account_name: The integration account name.
    :type integration_account_name: str
    :param agreement_name: The integration account agreement name.
    :type agreement_name: str
    :param api_version: The API version.
    :type api_version: str
    :param agreement: The integration account agreement.
    :type agreement: dict | bytes

    """
    agreement = IntegrationAccountAgreement.from_dict(agreement)
    return web.Response(status=200)


async def integration_account_agreements_delete(request: web.Request, subscription_id, resource_group_name, integration_account_name, agreement_name, api_version) -> web.Response:
    """integration_account_agreements_delete

    Deletes an integration account agreement.

    :param subscription_id: The subscription id.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param integration_account_name: The integration account name.
    :type integration_account_name: str
    :param agreement_name: The integration account agreement name.
    :type agreement_name: str
    :param api_version: The API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def integration_account_agreements_get(request: web.Request, subscription_id, resource_group_name, integration_account_name, agreement_name, api_version) -> web.Response:
    """integration_account_agreements_get

    Gets an integration account agreement.

    :param subscription_id: The subscription id.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param integration_account_name: The integration account name.
    :type integration_account_name: str
    :param agreement_name: The integration account agreement name.
    :type agreement_name: str
    :param api_version: The API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def integration_account_agreements_list(request: web.Request, subscription_id, resource_group_name, integration_account_name, api_version, top=None, filter=None) -> web.Response:
    """integration_account_agreements_list

    Gets a list of integration account agreements.

    :param subscription_id: The subscription id.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param integration_account_name: The integration account name.
    :type integration_account_name: str
    :param api_version: The API version.
    :type api_version: str
    :param top: The number of items to be included in the result.
    :type top: int
    :param filter: The filter to apply on the operation.
    :type filter: str

    """
    return web.Response(status=200)
