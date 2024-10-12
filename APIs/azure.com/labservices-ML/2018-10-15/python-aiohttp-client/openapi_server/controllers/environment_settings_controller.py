from typing import List, Dict
from aiohttp import web

from openapi_server.models.cloud_error import CloudError
from openapi_server.models.environment_setting import EnvironmentSetting
from openapi_server.models.environment_setting_fragment import EnvironmentSettingFragment
from openapi_server.models.publish_payload import PublishPayload
from openapi_server.models.response_with_continuation_environment_setting import ResponseWithContinuationEnvironmentSetting
from openapi_server import util


async def environment_settings_claim_any(request: web.Request, subscription_id, resource_group_name, lab_account_name, lab_name, environment_setting_name, api_version) -> web.Response:
    """environment_settings_claim_any

    Claims a random environment for a user in an environment settings

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

    """
    return web.Response(status=200)


async def environment_settings_create_or_update(request: web.Request, subscription_id, resource_group_name, lab_account_name, lab_name, environment_setting_name, api_version, environment_setting) -> web.Response:
    """environment_settings_create_or_update

    Create or replace an existing Environment Setting. This operation can take a while to complete

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
    :param environment_setting: Represents settings of an environment, from which environment instances would be created
    :type environment_setting: dict | bytes

    """
    environment_setting = EnvironmentSetting.from_dict(environment_setting)
    return web.Response(status=200)


async def environment_settings_delete(request: web.Request, subscription_id, resource_group_name, lab_account_name, lab_name, environment_setting_name, api_version) -> web.Response:
    """environment_settings_delete

    Delete environment setting. This operation can take a while to complete

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

    """
    return web.Response(status=200)


async def environment_settings_get(request: web.Request, subscription_id, resource_group_name, lab_account_name, lab_name, environment_setting_name, api_version, expand=None) -> web.Response:
    """environment_settings_get

    Get environment setting

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
    :param expand: Specify the $expand query. Example: &#39;properties($select&#x3D;publishingState)&#39;
    :type expand: str

    """
    return web.Response(status=200)


async def environment_settings_list(request: web.Request, subscription_id, resource_group_name, lab_account_name, lab_name, api_version, expand=None, filter=None, top=None, orderby=None) -> web.Response:
    """environment_settings_list

    List environment setting in a given lab.

    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param lab_account_name: The name of the lab Account.
    :type lab_account_name: str
    :param lab_name: The name of the lab.
    :type lab_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param expand: Specify the $expand query. Example: &#39;properties($select&#x3D;publishingState)&#39;
    :type expand: str
    :param filter: The filter to apply to the operation.
    :type filter: str
    :param top: The maximum number of resources to return from the operation.
    :type top: int
    :param orderby: The ordering expression for the results, using OData notation.
    :type orderby: str

    """
    return web.Response(status=200)


async def environment_settings_publish(request: web.Request, subscription_id, resource_group_name, lab_account_name, lab_name, environment_setting_name, api_version, publish_payload) -> web.Response:
    """environment_settings_publish

    Provisions/deprovisions required resources for an environment setting based on current state of the lab/environment setting.

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
    :param publish_payload: Payload for Publish operation on EnvironmentSetting.
    :type publish_payload: dict | bytes

    """
    publish_payload = PublishPayload.from_dict(publish_payload)
    return web.Response(status=200)


async def environment_settings_start(request: web.Request, subscription_id, resource_group_name, lab_account_name, lab_name, environment_setting_name, api_version) -> web.Response:
    """environment_settings_start

    Starts a template by starting all resources inside the template. This operation can take a while to complete

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

    """
    return web.Response(status=200)


async def environment_settings_stop(request: web.Request, subscription_id, resource_group_name, lab_account_name, lab_name, environment_setting_name, api_version) -> web.Response:
    """environment_settings_stop

    Starts a template by starting all resources inside the template. This operation can take a while to complete

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

    """
    return web.Response(status=200)


async def environment_settings_update(request: web.Request, subscription_id, resource_group_name, lab_account_name, lab_name, environment_setting_name, api_version, environment_setting) -> web.Response:
    """environment_settings_update

    Modify properties of environment setting.

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
    :param environment_setting: Represents settings of an environment, from which environment instances would be created
    :type environment_setting: dict | bytes

    """
    environment_setting = EnvironmentSettingFragment.from_dict(environment_setting)
    return web.Response(status=200)
