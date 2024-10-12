from typing import List, Dict
from aiohttp import web

from openapi_server.models.integration_account_certificate import IntegrationAccountCertificate
from openapi_server.models.integration_account_certificate_list_result import IntegrationAccountCertificateListResult
from openapi_server import util


async def integration_account_certificates_create_or_update(request: web.Request, subscription_id, resource_group_name, integration_account_name, certificate_name, api_version, certificate) -> web.Response:
    """integration_account_certificates_create_or_update

    Creates or updates an integration account certificate.

    :param subscription_id: The subscription id.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param integration_account_name: The integration account name.
    :type integration_account_name: str
    :param certificate_name: The integration account certificate name.
    :type certificate_name: str
    :param api_version: The API version.
    :type api_version: str
    :param certificate: The integration account certificate.
    :type certificate: dict | bytes

    """
    certificate = IntegrationAccountCertificate.from_dict(certificate)
    return web.Response(status=200)


async def integration_account_certificates_delete(request: web.Request, subscription_id, resource_group_name, integration_account_name, certificate_name, api_version) -> web.Response:
    """integration_account_certificates_delete

    Deletes an integration account certificate.

    :param subscription_id: The subscription id.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param integration_account_name: The integration account name.
    :type integration_account_name: str
    :param certificate_name: The integration account certificate name.
    :type certificate_name: str
    :param api_version: The API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def integration_account_certificates_get(request: web.Request, subscription_id, resource_group_name, integration_account_name, certificate_name, api_version) -> web.Response:
    """integration_account_certificates_get

    Gets an integration account certificate.

    :param subscription_id: The subscription id.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param integration_account_name: The integration account name.
    :type integration_account_name: str
    :param certificate_name: The integration account certificate name.
    :type certificate_name: str
    :param api_version: The API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def integration_account_certificates_list(request: web.Request, subscription_id, resource_group_name, integration_account_name, api_version, top=None) -> web.Response:
    """integration_account_certificates_list

    Gets a list of integration account certificates.

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

    """
    return web.Response(status=200)
