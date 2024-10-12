from typing import List, Dict
from aiohttp import web

from openapi_server.models.integration_account_partner import IntegrationAccountPartner
from openapi_server.models.integration_account_partner_list_result import IntegrationAccountPartnerListResult
from openapi_server import util


async def integration_account_partners_create_or_update(request: web.Request, subscription_id, resource_group_name, integration_account_name, partner_name, api_version, partner) -> web.Response:
    """integration_account_partners_create_or_update

    Creates or updates an integration account partner.

    :param subscription_id: The subscription id.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param integration_account_name: The integration account name.
    :type integration_account_name: str
    :param partner_name: The integration account partner name.
    :type partner_name: str
    :param api_version: The API version.
    :type api_version: str
    :param partner: The integration account partner.
    :type partner: dict | bytes

    """
    partner = IntegrationAccountPartner.from_dict(partner)
    return web.Response(status=200)


async def integration_account_partners_delete(request: web.Request, subscription_id, resource_group_name, integration_account_name, partner_name, api_version) -> web.Response:
    """integration_account_partners_delete

    Deletes an integration account partner.

    :param subscription_id: The subscription id.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param integration_account_name: The integration account name.
    :type integration_account_name: str
    :param partner_name: The integration account partner name.
    :type partner_name: str
    :param api_version: The API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def integration_account_partners_get(request: web.Request, subscription_id, resource_group_name, integration_account_name, partner_name, api_version) -> web.Response:
    """integration_account_partners_get

    Gets an integration account partner.

    :param subscription_id: The subscription id.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param integration_account_name: The integration account name.
    :type integration_account_name: str
    :param partner_name: The integration account partner name.
    :type partner_name: str
    :param api_version: The API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def integration_account_partners_list(request: web.Request, subscription_id, resource_group_name, integration_account_name, api_version, top=None, filter=None) -> web.Response:
    """integration_account_partners_list

    Gets a list of integration account partners.

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
