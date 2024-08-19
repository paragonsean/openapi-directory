from typing import List, Dict
from aiohttp import web

from openapi_server.models.android_mam_policy import AndroidMAMPolicy
from openapi_server.models.android_mam_policy_collection import AndroidMAMPolicyCollection
from openapi_server.models.application_collection import ApplicationCollection
from openapi_server.models.device import Device
from openapi_server.models.device_collection import DeviceCollection
from openapi_server.models.error import Error
from openapi_server.models.flagged_enrolled_app_collection import FlaggedEnrolledAppCollection
from openapi_server.models.flagged_user import FlaggedUser
from openapi_server.models.flagged_user_collection import FlaggedUserCollection
from openapi_server.models.groups_collection import GroupsCollection
from openapi_server.models.iosmam_policy import IOSMAMPolicy
from openapi_server.models.iosmam_policy_collection import IOSMAMPolicyCollection
from openapi_server.models.location import Location
from openapi_server.models.location_collection import LocationCollection
from openapi_server.models.mam_policy_app_id_or_group_id_payload import MAMPolicyAppIdOrGroupIdPayload
from openapi_server.models.operation_result_collection import OperationResultCollection
from openapi_server.models.statuses_default import StatusesDefault
from openapi_server.models.wipe_device_operation_result import WipeDeviceOperationResult
from openapi_server import util


async def android_add_app_for_mam_policy(request: web.Request, host_name, policy_name, app_name, api_version, parameters) -> web.Response:
    """android_add_app_for_mam_policy

    Add app to an AndroidMAMPolicy.

    :param host_name: Location hostName for the tenant
    :type host_name: str
    :param policy_name: Unique name for the policy
    :type policy_name: str
    :param app_name: application unique Name
    :type app_name: str
    :param api_version: Service Api Version.
    :type api_version: str
    :param parameters: Parameters supplied to the Create or update app to an android policy operation.
    :type parameters: dict | bytes

    """
    parameters = MAMPolicyAppIdOrGroupIdPayload.from_dict(parameters)
    return web.Response(status=200)


async def android_add_group_for_mam_policy(request: web.Request, host_name, policy_name, group_id, api_version, parameters) -> web.Response:
    """android_add_group_for_mam_policy

    Add group to an AndroidMAMPolicy.

    :param host_name: Location hostName for the tenant
    :type host_name: str
    :param policy_name: Unique name for the policy
    :type policy_name: str
    :param group_id: group Id
    :type group_id: str
    :param api_version: Service Api Version.
    :type api_version: str
    :param parameters: Parameters supplied to the Create or update app to an android policy operation.
    :type parameters: dict | bytes

    """
    parameters = MAMPolicyAppIdOrGroupIdPayload.from_dict(parameters)
    return web.Response(status=200)


async def android_create_or_update_mam_policy(request: web.Request, host_name, policy_name, api_version, parameters) -> web.Response:
    """android_create_or_update_mam_policy

    Creates or updates AndroidMAMPolicy.

    :param host_name: Location hostName for the tenant
    :type host_name: str
    :param policy_name: Unique name for the policy
    :type policy_name: str
    :param api_version: Service Api Version.
    :type api_version: str
    :param parameters: Parameters supplied to the Create or update an android policy operation.
    :type parameters: dict | bytes

    """
    parameters = AndroidMAMPolicy.from_dict(parameters)
    return web.Response(status=200)


async def android_delete_app_for_mam_policy(request: web.Request, host_name, policy_name, app_name, api_version) -> web.Response:
    """android_delete_app_for_mam_policy

    Delete App for Android Policy

    :param host_name: Location hostName for the tenant
    :type host_name: str
    :param policy_name: Unique name for the policy
    :type policy_name: str
    :param app_name: application unique Name
    :type app_name: str
    :param api_version: Service Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def android_delete_group_for_mam_policy(request: web.Request, host_name, policy_name, group_id, api_version) -> web.Response:
    """android_delete_group_for_mam_policy

    Delete Group for Android Policy

    :param host_name: Location hostName for the tenant
    :type host_name: str
    :param policy_name: Unique name for the policy
    :type policy_name: str
    :param group_id: application unique Name
    :type group_id: str
    :param api_version: Service Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def android_delete_mam_policy(request: web.Request, host_name, policy_name, api_version) -> web.Response:
    """android_delete_mam_policy

    Delete Android Policy

    :param host_name: Location hostName for the tenant
    :type host_name: str
    :param policy_name: Unique name for the policy
    :type policy_name: str
    :param api_version: Service Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def android_get_app_for_mam_policy(request: web.Request, host_name, policy_name, api_version, filter=None, top=None, select=None) -> web.Response:
    """android_get_app_for_mam_policy

    Get apps for an AndroidMAMPolicy.

    :param host_name: Location hostName for the tenant
    :type host_name: str
    :param policy_name: Unique name for the policy
    :type policy_name: str
    :param api_version: Service Api Version.
    :type api_version: str
    :param filter: The filter to apply on the operation.
    :type filter: str
    :param top: 
    :type top: int
    :param select: select specific fields in entity.
    :type select: str

    """
    return web.Response(status=200)


async def android_get_groups_for_mam_policy(request: web.Request, host_name, policy_name, api_version) -> web.Response:
    """android_get_groups_for_mam_policy

    Returns groups for a given AndroidMAMPolicy.

    :param host_name: Location hostName for the tenant
    :type host_name: str
    :param policy_name: policy name for the tenant
    :type policy_name: str
    :param api_version: Service Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def android_get_mam_policies(request: web.Request, host_name, api_version, filter=None, top=None, select=None) -> web.Response:
    """android_get_mam_policies

    Returns Intune Android policies.

    :param host_name: Location hostName for the tenant
    :type host_name: str
    :param api_version: Service Api Version.
    :type api_version: str
    :param filter: The filter to apply on the operation.
    :type filter: str
    :param top: 
    :type top: int
    :param select: select specific fields in entity.
    :type select: str

    """
    return web.Response(status=200)


async def android_get_mam_policy_by_name(request: web.Request, host_name, policy_name, api_version, select=None) -> web.Response:
    """android_get_mam_policy_by_name

    Returns AndroidMAMPolicy with given name.

    :param host_name: Location hostName for the tenant
    :type host_name: str
    :param policy_name: Unique name for the policy
    :type policy_name: str
    :param api_version: Service Api Version.
    :type api_version: str
    :param select: select specific fields in entity.
    :type select: str

    """
    return web.Response(status=200)


async def android_patch_mam_policy(request: web.Request, host_name, policy_name, api_version, parameters) -> web.Response:
    """android_patch_mam_policy

    Patch AndroidMAMPolicy.

    :param host_name: Location hostName for the tenant
    :type host_name: str
    :param policy_name: Unique name for the policy
    :type policy_name: str
    :param api_version: Service Api Version.
    :type api_version: str
    :param parameters: Parameters supplied to the Create or update an android policy operation.
    :type parameters: dict | bytes

    """
    parameters = AndroidMAMPolicy.from_dict(parameters)
    return web.Response(status=200)


async def get_apps(request: web.Request, host_name, api_version, filter=None, top=None, select=None) -> web.Response:
    """get_apps

    Returns Intune Manageable apps.

    :param host_name: Location hostName for the tenant
    :type host_name: str
    :param api_version: Service Api Version.
    :type api_version: str
    :param filter: The filter to apply on the operation.
    :type filter: str
    :param top: 
    :type top: int
    :param select: select specific fields in entity.
    :type select: str

    """
    return web.Response(status=200)


async def get_location_by_host_name(request: web.Request, api_version) -> web.Response:
    """get_location_by_host_name

    Returns location for given tenant.

    :param api_version: Service Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_locations(request: web.Request, api_version) -> web.Response:
    """get_locations

    Returns location for user tenant.

    :param api_version: Service Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_mam_flagged_user_by_name(request: web.Request, host_name, user_name, api_version, select=None) -> web.Response:
    """get_mam_flagged_user_by_name

    Returns Intune flagged user details

    :param host_name: Location hostName for the tenant
    :type host_name: str
    :param user_name: Flagged userName
    :type user_name: str
    :param api_version: Service Api Version.
    :type api_version: str
    :param select: select specific fields in entity.
    :type select: str

    """
    return web.Response(status=200)


async def get_mam_flagged_users(request: web.Request, host_name, api_version, filter=None, top=None, select=None) -> web.Response:
    """get_mam_flagged_users

    Returns Intune flagged user collection

    :param host_name: Location hostName for the tenant
    :type host_name: str
    :param api_version: Service Api Version.
    :type api_version: str
    :param filter: The filter to apply on the operation.
    :type filter: str
    :param top: 
    :type top: int
    :param select: select specific fields in entity.
    :type select: str

    """
    return web.Response(status=200)


async def get_mam_statuses(request: web.Request, host_name, api_version) -> web.Response:
    """get_mam_statuses

    Returns Intune Tenant level statuses.

    :param host_name: Location hostName for the tenant
    :type host_name: str
    :param api_version: Service Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_mam_user_device_by_device_name(request: web.Request, host_name, user_name, device_name, api_version, select=None) -> web.Response:
    """get_mam_user_device_by_device_name

    Get a unique device for a user.

    :param host_name: Location hostName for the tenant
    :type host_name: str
    :param user_name: unique user name
    :type user_name: str
    :param device_name: device name
    :type device_name: str
    :param api_version: Service Api Version.
    :type api_version: str
    :param select: select specific fields in entity.
    :type select: str

    """
    return web.Response(status=200)


async def get_mam_user_devices(request: web.Request, host_name, user_name, api_version, filter=None, top=None, select=None) -> web.Response:
    """get_mam_user_devices

    Get devices for a user.

    :param host_name: Location hostName for the tenant
    :type host_name: str
    :param user_name: user unique Name
    :type user_name: str
    :param api_version: Service Api Version.
    :type api_version: str
    :param filter: The filter to apply on the operation.
    :type filter: str
    :param top: 
    :type top: int
    :param select: select specific fields in entity.
    :type select: str

    """
    return web.Response(status=200)


async def get_mam_user_flagged_enrolled_apps(request: web.Request, host_name, user_name, api_version, filter=None, top=None, select=None) -> web.Response:
    """get_mam_user_flagged_enrolled_apps

    Returns Intune flagged enrolled app collection for the User

    :param host_name: Location hostName for the tenant
    :type host_name: str
    :param user_name: User name for the tenant
    :type user_name: str
    :param api_version: Service Api Version.
    :type api_version: str
    :param filter: The filter to apply on the operation.
    :type filter: str
    :param top: 
    :type top: int
    :param select: select specific fields in entity.
    :type select: str

    """
    return web.Response(status=200)


async def get_operation_results(request: web.Request, host_name, api_version, filter=None, top=None, select=None) -> web.Response:
    """get_operation_results

    Returns operationResults.

    :param host_name: Location hostName for the tenant
    :type host_name: str
    :param api_version: Service Api Version.
    :type api_version: str
    :param filter: The filter to apply on the operation.
    :type filter: str
    :param top: 
    :type top: int
    :param select: select specific fields in entity.
    :type select: str

    """
    return web.Response(status=200)


async def ios_add_app_for_mam_policy(request: web.Request, host_name, policy_name, app_name, api_version, parameters) -> web.Response:
    """ios_add_app_for_mam_policy

    Add app to an iOSMAMPolicy.

    :param host_name: Location hostName for the tenant
    :type host_name: str
    :param policy_name: Unique name for the policy
    :type policy_name: str
    :param app_name: application unique Name
    :type app_name: str
    :param api_version: Service Api Version.
    :type api_version: str
    :param parameters: Parameters supplied to add an app to an ios policy.
    :type parameters: dict | bytes

    """
    parameters = MAMPolicyAppIdOrGroupIdPayload.from_dict(parameters)
    return web.Response(status=200)


async def ios_add_group_for_mam_policy(request: web.Request, host_name, policy_name, group_id, api_version, parameters) -> web.Response:
    """ios_add_group_for_mam_policy

    Add group to an iOSMAMPolicy.

    :param host_name: Location hostName for the tenant
    :type host_name: str
    :param policy_name: Unique name for the policy
    :type policy_name: str
    :param group_id: group Id
    :type group_id: str
    :param api_version: Service Api Version.
    :type api_version: str
    :param parameters: Parameters supplied to the Create or update app to an android policy operation.
    :type parameters: dict | bytes

    """
    parameters = MAMPolicyAppIdOrGroupIdPayload.from_dict(parameters)
    return web.Response(status=200)


async def ios_create_or_update_mam_policy(request: web.Request, host_name, policy_name, api_version, parameters) -> web.Response:
    """ios_create_or_update_mam_policy

    Creates or updates iOSMAMPolicy.

    :param host_name: Location hostName for the tenant
    :type host_name: str
    :param policy_name: Unique name for the policy
    :type policy_name: str
    :param api_version: Service Api Version.
    :type api_version: str
    :param parameters: Parameters supplied to the Create or update an android policy operation.
    :type parameters: dict | bytes

    """
    parameters = IOSMAMPolicy.from_dict(parameters)
    return web.Response(status=200)


async def ios_delete_app_for_mam_policy(request: web.Request, host_name, policy_name, app_name, api_version) -> web.Response:
    """ios_delete_app_for_mam_policy

    Delete App for Ios Policy

    :param host_name: Location hostName for the tenant
    :type host_name: str
    :param policy_name: Unique name for the policy
    :type policy_name: str
    :param app_name: application unique Name
    :type app_name: str
    :param api_version: Service Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def ios_delete_group_for_mam_policy(request: web.Request, host_name, policy_name, group_id, api_version) -> web.Response:
    """ios_delete_group_for_mam_policy

    Delete Group for iOS Policy

    :param host_name: Location hostName for the tenant
    :type host_name: str
    :param policy_name: Unique name for the policy
    :type policy_name: str
    :param group_id: application unique Name
    :type group_id: str
    :param api_version: Service Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def ios_delete_mam_policy(request: web.Request, host_name, policy_name, api_version) -> web.Response:
    """ios_delete_mam_policy

    Delete Ios Policy

    :param host_name: Location hostName for the tenant
    :type host_name: str
    :param policy_name: Unique name for the policy
    :type policy_name: str
    :param api_version: Service Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def ios_get_app_for_mam_policy(request: web.Request, host_name, policy_name, api_version, filter=None, top=None, select=None) -> web.Response:
    """ios_get_app_for_mam_policy

    Get apps for an iOSMAMPolicy.

    :param host_name: Location hostName for the tenant
    :type host_name: str
    :param policy_name: Unique name for the policy
    :type policy_name: str
    :param api_version: Service Api Version.
    :type api_version: str
    :param filter: The filter to apply on the operation.
    :type filter: str
    :param top: 
    :type top: int
    :param select: select specific fields in entity.
    :type select: str

    """
    return web.Response(status=200)


async def ios_get_groups_for_mam_policy(request: web.Request, host_name, policy_name, api_version) -> web.Response:
    """ios_get_groups_for_mam_policy

    Returns groups for a given iOSMAMPolicy.

    :param host_name: Location hostName for the tenant
    :type host_name: str
    :param policy_name: policy name for the tenant
    :type policy_name: str
    :param api_version: Service Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def ios_get_mam_policies(request: web.Request, host_name, api_version, filter=None, top=None, select=None) -> web.Response:
    """ios_get_mam_policies

    Returns Intune iOSPolicies.

    :param host_name: Location hostName for the tenant
    :type host_name: str
    :param api_version: Service Api Version.
    :type api_version: str
    :param filter: The filter to apply on the operation.
    :type filter: str
    :param top: 
    :type top: int
    :param select: select specific fields in entity.
    :type select: str

    """
    return web.Response(status=200)


async def ios_get_mam_policy_by_name(request: web.Request, host_name, policy_name, api_version, select=None) -> web.Response:
    """ios_get_mam_policy_by_name

    Returns Intune iOS policies.

    :param host_name: Location hostName for the tenant
    :type host_name: str
    :param policy_name: Unique name for the policy
    :type policy_name: str
    :param api_version: Service Api Version.
    :type api_version: str
    :param select: select specific fields in entity.
    :type select: str

    """
    return web.Response(status=200)


async def ios_patch_mam_policy(request: web.Request, host_name, policy_name, api_version, parameters) -> web.Response:
    """ios_patch_mam_policy

     patch an iOSMAMPolicy.

    :param host_name: Location hostName for the tenant
    :type host_name: str
    :param policy_name: Unique name for the policy
    :type policy_name: str
    :param api_version: Service Api Version.
    :type api_version: str
    :param parameters: Parameters supplied to the Create or update an android policy operation.
    :type parameters: dict | bytes

    """
    parameters = IOSMAMPolicy.from_dict(parameters)
    return web.Response(status=200)


async def wipe_mam_user_device(request: web.Request, host_name, user_name, device_name, api_version) -> web.Response:
    """wipe_mam_user_device

    Wipe a device for a user.

    :param host_name: Location hostName for the tenant
    :type host_name: str
    :param user_name: unique user name
    :type user_name: str
    :param device_name: device name
    :type device_name: str
    :param api_version: Service Api Version.
    :type api_version: str

    """
    return web.Response(status=200)
