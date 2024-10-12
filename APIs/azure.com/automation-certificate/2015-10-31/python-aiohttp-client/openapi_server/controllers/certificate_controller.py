from typing import List, Dict
from aiohttp import web

from openapi_server.models.certificate import Certificate
from openapi_server.models.certificate_create_or_update_parameters import CertificateCreateOrUpdateParameters
from openapi_server.models.certificate_list_by_automation_account_default_response import CertificateListByAutomationAccountDefaultResponse
from openapi_server.models.certificate_list_result import CertificateListResult
from openapi_server.models.certificate_update_parameters import CertificateUpdateParameters
from openapi_server import util


async def certificate_create_or_update(request: web.Request, resource_group_name, automation_account_name, certificate_name, subscription_id, api_version, parameters) -> web.Response:
    """certificate_create_or_update

    Create a certificate.

    :param resource_group_name: Name of an Azure Resource group.
    :type resource_group_name: str
    :param automation_account_name: The name of the automation account.
    :type automation_account_name: str
    :param certificate_name: The parameters supplied to the create or update certificate operation.
    :type certificate_name: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param parameters: The parameters supplied to the create or update certificate operation.
    :type parameters: dict | bytes

    """
    parameters = CertificateCreateOrUpdateParameters.from_dict(parameters)
    return web.Response(status=200)


async def certificate_delete(request: web.Request, resource_group_name, automation_account_name, certificate_name, subscription_id, api_version) -> web.Response:
    """certificate_delete

    Delete the certificate.

    :param resource_group_name: Name of an Azure Resource group.
    :type resource_group_name: str
    :param automation_account_name: The name of the automation account.
    :type automation_account_name: str
    :param certificate_name: The name of certificate.
    :type certificate_name: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def certificate_get(request: web.Request, resource_group_name, automation_account_name, certificate_name, subscription_id, api_version) -> web.Response:
    """certificate_get

    Retrieve the certificate identified by certificate name.

    :param resource_group_name: Name of an Azure Resource group.
    :type resource_group_name: str
    :param automation_account_name: The name of the automation account.
    :type automation_account_name: str
    :param certificate_name: The name of certificate.
    :type certificate_name: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def certificate_list_by_automation_account(request: web.Request, resource_group_name, automation_account_name, subscription_id, api_version) -> web.Response:
    """certificate_list_by_automation_account

    Retrieve a list of certificates.

    :param resource_group_name: Name of an Azure Resource group.
    :type resource_group_name: str
    :param automation_account_name: The name of the automation account.
    :type automation_account_name: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def certificate_update(request: web.Request, resource_group_name, automation_account_name, certificate_name, subscription_id, api_version, parameters) -> web.Response:
    """certificate_update

    Update a certificate.

    :param resource_group_name: Name of an Azure Resource group.
    :type resource_group_name: str
    :param automation_account_name: The name of the automation account.
    :type automation_account_name: str
    :param certificate_name: The parameters supplied to the update certificate operation.
    :type certificate_name: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param parameters: The parameters supplied to the update certificate operation.
    :type parameters: dict | bytes

    """
    parameters = CertificateUpdateParameters.from_dict(parameters)
    return web.Response(status=200)
