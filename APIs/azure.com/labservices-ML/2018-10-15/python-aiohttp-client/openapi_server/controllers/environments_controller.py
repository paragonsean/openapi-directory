from typing import List, Dict
from aiohttp import web

from openapi_server.models.cloud_error import CloudError
from openapi_server.models.environment import Environment
from openapi_server.models.environment_fragment import EnvironmentFragment
from openapi_server.models.reset_password_payload import ResetPasswordPayload
from openapi_server.models.response_with_continuation_environment import ResponseWithContinuationEnvironment
from openapi_server import util


async def environments_claim(request: web.Request, subscription_id, resource_group_name, lab_account_name, lab_name, environment_setting_name, environment_name, api_version) -> web.Response:
    """environments_claim

    Claims the environment and assigns it to the user

    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param lab_account_name: The name of the lab Account.
    :type lab_account_name: str
    :param lab_name: The name of the lab.
    :type lab_name: str
    :param environment_setting_name: The name of the environment Setting.
    :type environment_setting_name: str
    :param environment_name: The name of the environment.
    :type environment_name: str
    :param api_version: Client API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def environments_create_or_update(request: web.Request, subscription_id, resource_group_name, lab_account_name, lab_name, environment_setting_name, environment_name, api_version, environment) -> web.Response:
    """environments_create_or_update

    Create or replace an existing Environment.

    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param lab_account_name: The name of the lab Account.
    :type lab_account_name: str
    :param lab_name: The name of the lab.
    :type lab_name: str
    :param environment_setting_name: The name of the environment Setting.
    :type environment_setting_name: str
    :param environment_name: The name of the environment.
    :type environment_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param environment: Represents an environment instance
    :type environment: dict | bytes

    """
    environment = Environment.from_dict(environment)
    return web.Response(status=200)


async def environments_delete(request: web.Request, subscription_id, resource_group_name, lab_account_name, lab_name, environment_setting_name, environment_name, api_version) -> web.Response:
    """environments_delete

    Delete environment. This operation can take a while to complete

    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param lab_account_name: The name of the lab Account.
    :type lab_account_name: str
    :param lab_name: The name of the lab.
    :type lab_name: str
    :param environment_setting_name: The name of the environment Setting.
    :type environment_setting_name: str
    :param environment_name: The name of the environment.
    :type environment_name: str
    :param api_version: Client API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def environments_get(request: web.Request, subscription_id, resource_group_name, lab_account_name, lab_name, environment_setting_name, environment_name, api_version, expand=None) -> web.Response:
    """environments_get

    Get environment

    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param lab_account_name: The name of the lab Account.
    :type lab_account_name: str
    :param lab_name: The name of the lab.
    :type lab_name: str
    :param environment_setting_name: The name of the environment Setting.
    :type environment_setting_name: str
    :param environment_name: The name of the environment.
    :type environment_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param expand: Specify the $expand query. Example: &#39;properties($expand&#x3D;networkInterface)&#39;
    :type expand: str

    """
    return web.Response(status=200)


async def environments_list(request: web.Request, subscription_id, resource_group_name, lab_account_name, lab_name, environment_setting_name, api_version, expand=None, filter=None, top=None, orderby=None) -> web.Response:
    """environments_list

    List environments in a given environment setting.

    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param lab_account_name: The name of the lab Account.
    :type lab_account_name: str
    :param lab_name: The name of the lab.
    :type lab_name: str
    :param environment_setting_name: The name of the environment Setting.
    :type environment_setting_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param expand: Specify the $expand query. Example: &#39;properties($expand&#x3D;networkInterface)&#39;
    :type expand: str
    :param filter: The filter to apply to the operation.
    :type filter: str
    :param top: The maximum number of resources to return from the operation.
    :type top: int
    :param orderby: The ordering expression for the results, using OData notation.
    :type orderby: str

    """
    return web.Response(status=200)


async def environments_reset_password(request: web.Request, subscription_id, resource_group_name, lab_account_name, lab_name, environment_setting_name, environment_name, api_version, reset_password_payload) -> web.Response:
    """environments_reset_password

    Resets the user password on an environment This operation can take a while to complete

    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param lab_account_name: The name of the lab Account.
    :type lab_account_name: str
    :param lab_name: The name of the lab.
    :type lab_name: str
    :param environment_setting_name: The name of the environment Setting.
    :type environment_setting_name: str
    :param environment_name: The name of the environment.
    :type environment_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param reset_password_payload: Represents the payload for resetting passwords.
    :type reset_password_payload: dict | bytes

    """
    reset_password_payload = ResetPasswordPayload.from_dict(reset_password_payload)
    return web.Response(status=200)


async def environments_start(request: web.Request, subscription_id, resource_group_name, lab_account_name, lab_name, environment_setting_name, environment_name, api_version) -> web.Response:
    """environments_start

    Starts an environment by starting all resources inside the environment. This operation can take a while to complete

    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param lab_account_name: The name of the lab Account.
    :type lab_account_name: str
    :param lab_name: The name of the lab.
    :type lab_name: str
    :param environment_setting_name: The name of the environment Setting.
    :type environment_setting_name: str
    :param environment_name: The name of the environment.
    :type environment_name: str
    :param api_version: Client API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def environments_stop(request: web.Request, subscription_id, resource_group_name, lab_account_name, lab_name, environment_setting_name, environment_name, api_version) -> web.Response:
    """environments_stop

    Stops an environment by stopping all resources inside the environment This operation can take a while to complete

    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param lab_account_name: The name of the lab Account.
    :type lab_account_name: str
    :param lab_name: The name of the lab.
    :type lab_name: str
    :param environment_setting_name: The name of the environment Setting.
    :type environment_setting_name: str
    :param environment_name: The name of the environment.
    :type environment_name: str
    :param api_version: Client API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def environments_update(request: web.Request, subscription_id, resource_group_name, lab_account_name, lab_name, environment_setting_name, environment_name, api_version, environment) -> web.Response:
    """environments_update

    Modify properties of environments.

    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param lab_account_name: The name of the lab Account.
    :type lab_account_name: str
    :param lab_name: The name of the lab.
    :type lab_name: str
    :param environment_setting_name: The name of the environment Setting.
    :type environment_setting_name: str
    :param environment_name: The name of the environment.
    :type environment_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param environment: Represents an environment instance
    :type environment: dict | bytes

    """
    environment = EnvironmentFragment.from_dict(environment)
    return web.Response(status=200)
