from typing import List, Dict
from aiohttp import web

from openapi_server.models.credential import Credential
from openapi_server.models.credential_create_or_update_parameters import CredentialCreateOrUpdateParameters
from openapi_server.models.credential_get_default_response import CredentialGetDefaultResponse
from openapi_server.models.credential_list_result import CredentialListResult
from openapi_server.models.credential_update_parameters import CredentialUpdateParameters
from openapi_server import util


async def credential_create_or_update(request: web.Request, resource_group_name, automation_account_name, credential_name, subscription_id, api_version, parameters) -> web.Response:
    """credential_create_or_update

    Create a credential.

    :param resource_group_name: Name of an Azure Resource group.
    :type resource_group_name: str
    :param automation_account_name: The name of the automation account.
    :type automation_account_name: str
    :param credential_name: The parameters supplied to the create or update credential operation.
    :type credential_name: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param parameters: The parameters supplied to the create or update credential operation.
    :type parameters: dict | bytes

    """
    parameters = CredentialCreateOrUpdateParameters.from_dict(parameters)
    return web.Response(status=200)


async def credential_delete(request: web.Request, resource_group_name, automation_account_name, credential_name, subscription_id, api_version) -> web.Response:
    """credential_delete

    Delete the credential.

    :param resource_group_name: Name of an Azure Resource group.
    :type resource_group_name: str
    :param automation_account_name: The name of the automation account.
    :type automation_account_name: str
    :param credential_name: The name of credential.
    :type credential_name: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def credential_get(request: web.Request, resource_group_name, automation_account_name, credential_name, subscription_id, api_version) -> web.Response:
    """credential_get

    Retrieve the credential identified by credential name.

    :param resource_group_name: Name of an Azure Resource group.
    :type resource_group_name: str
    :param automation_account_name: The name of the automation account.
    :type automation_account_name: str
    :param credential_name: The name of credential.
    :type credential_name: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def credential_list_by_automation_account(request: web.Request, resource_group_name, automation_account_name, subscription_id, api_version) -> web.Response:
    """credential_list_by_automation_account

    Retrieve a list of credentials.

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


async def credential_update(request: web.Request, resource_group_name, automation_account_name, credential_name, subscription_id, api_version, parameters) -> web.Response:
    """credential_update

    Update a credential.

    :param resource_group_name: Name of an Azure Resource group.
    :type resource_group_name: str
    :param automation_account_name: The name of the automation account.
    :type automation_account_name: str
    :param credential_name: The parameters supplied to the Update credential operation.
    :type credential_name: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param parameters: The parameters supplied to the Update credential operation.
    :type parameters: dict | bytes

    """
    parameters = CredentialUpdateParameters.from_dict(parameters)
    return web.Response(status=200)
