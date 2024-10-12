from typing import List, Dict
from aiohttp import web

from openapi_server.models.checkin_network_sm_devices200_response import CheckinNetworkSmDevices200Response
from openapi_server.models.checkin_network_sm_devices_request import CheckinNetworkSmDevicesRequest
from openapi_server.models.create_network_sm_bypass_activation_lock_attempt_request import CreateNetworkSmBypassActivationLockAttemptRequest
from openapi_server.models.create_network_sm_target_group_request import CreateNetworkSmTargetGroupRequest
from openapi_server.models.get_network_sm_device_cellular_usage_history200_response_inner import GetNetworkSmDeviceCellularUsageHistory200ResponseInner
from openapi_server.models.get_network_sm_device_certs200_response_inner import GetNetworkSmDeviceCerts200ResponseInner
from openapi_server.models.get_network_sm_device_connectivity200_response_inner import GetNetworkSmDeviceConnectivity200ResponseInner
from openapi_server.models.get_network_sm_device_desktop_logs200_response_inner import GetNetworkSmDeviceDesktopLogs200ResponseInner
from openapi_server.models.get_network_sm_device_device_command_logs200_response_inner import GetNetworkSmDeviceDeviceCommandLogs200ResponseInner
from openapi_server.models.get_network_sm_device_device_profiles200_response_inner import GetNetworkSmDeviceDeviceProfiles200ResponseInner
from openapi_server.models.get_network_sm_device_network_adapters200_response_inner import GetNetworkSmDeviceNetworkAdapters200ResponseInner
from openapi_server.models.get_network_sm_device_performance_history200_response_inner import GetNetworkSmDevicePerformanceHistory200ResponseInner
from openapi_server.models.get_network_sm_device_security_centers200_response_inner import GetNetworkSmDeviceSecurityCenters200ResponseInner
from openapi_server.models.get_network_sm_device_softwares200_response_inner import GetNetworkSmDeviceSoftwares200ResponseInner
from openapi_server.models.get_network_sm_device_wlan_lists200_response_inner import GetNetworkSmDeviceWlanLists200ResponseInner
from openapi_server.models.get_network_sm_devices200_response_inner import GetNetworkSmDevices200ResponseInner
from openapi_server.models.get_network_sm_profiles200_response_inner import GetNetworkSmProfiles200ResponseInner
from openapi_server.models.get_network_sm_trusted_access_configs200_response_inner import GetNetworkSmTrustedAccessConfigs200ResponseInner
from openapi_server.models.get_network_sm_user_access_devices200_response_inner import GetNetworkSmUserAccessDevices200ResponseInner
from openapi_server.models.get_network_sm_users200_response_inner import GetNetworkSmUsers200ResponseInner
from openapi_server.models.get_organization_sm_apns_cert200_response import GetOrganizationSmApnsCert200Response
from openapi_server.models.get_organization_sm_vpp_accounts200_response_inner import GetOrganizationSmVppAccounts200ResponseInner
from openapi_server.models.lock_network_sm_devices_request import LockNetworkSmDevicesRequest
from openapi_server.models.modify_network_sm_devices_tags200_response_inner import ModifyNetworkSmDevicesTags200ResponseInner
from openapi_server.models.modify_network_sm_devices_tags_request import ModifyNetworkSmDevicesTagsRequest
from openapi_server.models.move_network_sm_devices200_response import MoveNetworkSmDevices200Response
from openapi_server.models.move_network_sm_devices_request import MoveNetworkSmDevicesRequest
from openapi_server.models.update_network_sm_devices_fields200_response_inner import UpdateNetworkSmDevicesFields200ResponseInner
from openapi_server.models.update_network_sm_devices_fields_request import UpdateNetworkSmDevicesFieldsRequest
from openapi_server.models.wipe_network_sm_devices200_response import WipeNetworkSmDevices200Response
from openapi_server.models.wipe_network_sm_devices_request import WipeNetworkSmDevicesRequest
from openapi_server import util


async def checkin_network_sm_devices(request: web.Request, network_id, body=None) -> web.Response:
    """Force check-in a set of devices

    Force check-in a set of devices

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CheckinNetworkSmDevicesRequest.from_dict(body)
    return web.Response(status=200)


async def create_network_sm_bypass_activation_lock_attempt(request: web.Request, network_id, body) -> web.Response:
    """Bypass activation lock attempt

    Bypass activation lock attempt

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateNetworkSmBypassActivationLockAttemptRequest.from_dict(body)
    return web.Response(status=200)


async def create_network_sm_target_group(request: web.Request, network_id, body=None) -> web.Response:
    """Add a target group

    Add a target group

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateNetworkSmTargetGroupRequest.from_dict(body)
    return web.Response(status=200)


async def delete_network_sm_target_group(request: web.Request, network_id, target_group_id) -> web.Response:
    """Delete a target group from a network

    Delete a target group from a network

    :param network_id: 
    :type network_id: str
    :param target_group_id: 
    :type target_group_id: str

    """
    return web.Response(status=200)


async def delete_network_sm_user_access_device(request: web.Request, network_id, user_access_device_id) -> web.Response:
    """Delete a User Access Device

    Delete a User Access Device

    :param network_id: 
    :type network_id: str
    :param user_access_device_id: 
    :type user_access_device_id: str

    """
    return web.Response(status=200)


async def get_network_sm_bypass_activation_lock_attempt(request: web.Request, network_id, attempt_id) -> web.Response:
    """Bypass activation lock attempt status

    Bypass activation lock attempt status

    :param network_id: 
    :type network_id: str
    :param attempt_id: 
    :type attempt_id: str

    """
    return web.Response(status=200)


async def get_network_sm_device_cellular_usage_history(request: web.Request, network_id, device_id) -> web.Response:
    """Return the client&#39;s daily cellular data usage history

    Return the client&#39;s daily cellular data usage history. Usage data is in kilobytes.

    :param network_id: 
    :type network_id: str
    :param device_id: 
    :type device_id: str

    """
    return web.Response(status=200)


async def get_network_sm_device_certs(request: web.Request, network_id, device_id) -> web.Response:
    """List the certs on a device

    List the certs on a device

    :param network_id: 
    :type network_id: str
    :param device_id: 
    :type device_id: str

    """
    return web.Response(status=200)


async def get_network_sm_device_connectivity(request: web.Request, network_id, device_id, per_page=None, starting_after=None, ending_before=None) -> web.Response:
    """Returns historical connectivity data (whether a device is regularly checking in to Dashboard).

    Returns historical connectivity data (whether a device is regularly checking in to Dashboard).

    :param network_id: 
    :type network_id: str
    :param device_id: 
    :type device_id: str
    :param per_page: The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
    :type per_page: int
    :param starting_after: A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type starting_after: str
    :param ending_before: A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type ending_before: str

    """
    return web.Response(status=200)


async def get_network_sm_device_desktop_logs(request: web.Request, network_id, device_id, per_page=None, starting_after=None, ending_before=None) -> web.Response:
    """Return historical records of various Systems Manager network connection details for desktop devices.

    Return historical records of various Systems Manager network connection details for desktop devices.

    :param network_id: 
    :type network_id: str
    :param device_id: 
    :type device_id: str
    :param per_page: The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
    :type per_page: int
    :param starting_after: A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type starting_after: str
    :param ending_before: A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type ending_before: str

    """
    return web.Response(status=200)


async def get_network_sm_device_device_command_logs(request: web.Request, network_id, device_id, per_page=None, starting_after=None, ending_before=None) -> web.Response:
    """Return historical records of commands sent to Systems Manager devices

    Return historical records of commands sent to Systems Manager devices. Note that this will include the name of the Dashboard user who initiated the command if it was generated by a Dashboard admin rather than the automatic behavior of the system; you may wish to filter this out of any reports.

    :param network_id: 
    :type network_id: str
    :param device_id: 
    :type device_id: str
    :param per_page: The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
    :type per_page: int
    :param starting_after: A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type starting_after: str
    :param ending_before: A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type ending_before: str

    """
    return web.Response(status=200)


async def get_network_sm_device_device_profiles(request: web.Request, network_id, device_id) -> web.Response:
    """Get the installed profiles associated with a device

    Get the installed profiles associated with a device

    :param network_id: 
    :type network_id: str
    :param device_id: 
    :type device_id: str

    """
    return web.Response(status=200)


async def get_network_sm_device_network_adapters(request: web.Request, network_id, device_id) -> web.Response:
    """List the network adapters of a device

    List the network adapters of a device

    :param network_id: 
    :type network_id: str
    :param device_id: 
    :type device_id: str

    """
    return web.Response(status=200)


async def get_network_sm_device_performance_history(request: web.Request, network_id, device_id, per_page=None, starting_after=None, ending_before=None) -> web.Response:
    """Return historical records of various Systems Manager client metrics for desktop devices.

    Return historical records of various Systems Manager client metrics for desktop devices.

    :param network_id: 
    :type network_id: str
    :param device_id: 
    :type device_id: str
    :param per_page: The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
    :type per_page: int
    :param starting_after: A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type starting_after: str
    :param ending_before: A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type ending_before: str

    """
    return web.Response(status=200)


async def get_network_sm_device_restrictions(request: web.Request, network_id, device_id) -> web.Response:
    """List the restrictions on a device

    List the restrictions on a device

    :param network_id: 
    :type network_id: str
    :param device_id: 
    :type device_id: str

    """
    return web.Response(status=200)


async def get_network_sm_device_security_centers(request: web.Request, network_id, device_id) -> web.Response:
    """List the security centers on a device

    List the security centers on a device

    :param network_id: 
    :type network_id: str
    :param device_id: 
    :type device_id: str

    """
    return web.Response(status=200)


async def get_network_sm_device_softwares(request: web.Request, network_id, device_id) -> web.Response:
    """Get a list of softwares associated with a device

    Get a list of softwares associated with a device

    :param network_id: 
    :type network_id: str
    :param device_id: 
    :type device_id: str

    """
    return web.Response(status=200)


async def get_network_sm_device_wlan_lists(request: web.Request, network_id, device_id) -> web.Response:
    """List the saved SSID names on a device

    List the saved SSID names on a device

    :param network_id: 
    :type network_id: str
    :param device_id: 
    :type device_id: str

    """
    return web.Response(status=200)


async def get_network_sm_devices(request: web.Request, network_id, fields=None, wifi_macs=None, serials=None, ids=None, scope=None, per_page=None, starting_after=None, ending_before=None) -> web.Response:
    """List the devices enrolled in an SM network with various specified fields and filters

    List the devices enrolled in an SM network with various specified fields and filters

    :param network_id: 
    :type network_id: str
    :param fields: Additional fields that will be displayed for each device.     The default fields are: id, name, tags, ssid, wifiMac, osName, systemModel, uuid, and serialNumber. The additional fields are: ip,     systemType, availableDeviceCapacity, kioskAppName, biosVersion, lastConnected, missingAppsCount, userSuppliedAddress, location, lastUser,     ownerEmail, ownerUsername, osBuild, publicIp, phoneNumber, diskInfoJson, deviceCapacity, isManaged, hadMdm, isSupervised, meid, imei, iccid,     simCarrierNetwork, cellularDataUsed, isHotspotEnabled, createdAt, batteryEstCharge, quarantined, avName, avRunning, asName, fwName,     isRooted, loginRequired, screenLockEnabled, screenLockDelay, autoLoginDisabled, autoTags, hasMdm, hasDesktopAgent, diskEncryptionEnabled,     hardwareEncryptionCaps, passCodeLock, usesHardwareKeystore, androidSecurityPatchVersion, and url.
    :type fields: List[str]
    :param wifi_macs: Filter devices by wifi mac(s).
    :type wifi_macs: List[str]
    :param serials: Filter devices by serial(s).
    :type serials: List[str]
    :param ids: Filter devices by id(s).
    :type ids: List[str]
    :param scope: Specify a scope (one of all, none, withAny, withAll, withoutAny, or withoutAll) and a set of tags.
    :type scope: List[str]
    :param per_page: The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
    :type per_page: int
    :param starting_after: A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type starting_after: str
    :param ending_before: A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type ending_before: str

    """
    return web.Response(status=200)


async def get_network_sm_profiles(request: web.Request, network_id) -> web.Response:
    """List all profiles in a network

    List all profiles in a network

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def get_network_sm_target_group(request: web.Request, network_id, target_group_id, with_details=None) -> web.Response:
    """Return a target group

    Return a target group

    :param network_id: 
    :type network_id: str
    :param target_group_id: 
    :type target_group_id: str
    :param with_details: Boolean indicating if the the ids of the devices or users scoped by the target group should be included in the response
    :type with_details: bool

    """
    return web.Response(status=200)


async def get_network_sm_target_groups(request: web.Request, network_id, with_details=None) -> web.Response:
    """List the target groups in this network

    List the target groups in this network

    :param network_id: 
    :type network_id: str
    :param with_details: Boolean indicating if the the ids of the devices or users scoped by the target group should be included in the response
    :type with_details: bool

    """
    return web.Response(status=200)


async def get_network_sm_trusted_access_configs(request: web.Request, network_id, per_page=None, starting_after=None, ending_before=None) -> web.Response:
    """List Trusted Access Configs

    List Trusted Access Configs

    :param network_id: 
    :type network_id: str
    :param per_page: The number of entries per page returned. Acceptable range is 3 - 1000. Default is 100.
    :type per_page: int
    :param starting_after: A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type starting_after: str
    :param ending_before: A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type ending_before: str

    """
    return web.Response(status=200)


async def get_network_sm_user_access_devices(request: web.Request, network_id, per_page=None, starting_after=None, ending_before=None) -> web.Response:
    """List User Access Devices and its Trusted Access Connections

    List User Access Devices and its Trusted Access Connections

    :param network_id: 
    :type network_id: str
    :param per_page: The number of entries per page returned. Acceptable range is 3 - 1000. Default is 100.
    :type per_page: int
    :param starting_after: A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type starting_after: str
    :param ending_before: A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type ending_before: str

    """
    return web.Response(status=200)


async def get_network_sm_user_device_profiles(request: web.Request, network_id, user_id) -> web.Response:
    """Get the profiles associated with a user

    Get the profiles associated with a user

    :param network_id: 
    :type network_id: str
    :param user_id: 
    :type user_id: str

    """
    return web.Response(status=200)


async def get_network_sm_user_softwares(request: web.Request, network_id, user_id) -> web.Response:
    """Get a list of softwares associated with a user

    Get a list of softwares associated with a user

    :param network_id: 
    :type network_id: str
    :param user_id: 
    :type user_id: str

    """
    return web.Response(status=200)


async def get_network_sm_users(request: web.Request, network_id, ids=None, usernames=None, emails=None, scope=None) -> web.Response:
    """List the owners in an SM network with various specified fields and filters

    List the owners in an SM network with various specified fields and filters

    :param network_id: 
    :type network_id: str
    :param ids: Filter users by id(s).
    :type ids: List[str]
    :param usernames: Filter users by username(s).
    :type usernames: List[str]
    :param emails: Filter users by email(s).
    :type emails: List[str]
    :param scope: Specifiy a scope (one of all, none, withAny, withAll, withoutAny, withoutAll) and a set of tags.
    :type scope: List[str]

    """
    return web.Response(status=200)


async def get_organization_sm_apns_cert(request: web.Request, organization_id) -> web.Response:
    """Get the organization&#39;s APNS certificate

    Get the organization&#39;s APNS certificate

    :param organization_id: 
    :type organization_id: str

    """
    return web.Response(status=200)


async def get_organization_sm_vpp_account(request: web.Request, organization_id, vpp_account_id) -> web.Response:
    """Get a hash containing the unparsed token of the VPP account with the given ID

    Get a hash containing the unparsed token of the VPP account with the given ID

    :param organization_id: 
    :type organization_id: str
    :param vpp_account_id: 
    :type vpp_account_id: str

    """
    return web.Response(status=200)


async def get_organization_sm_vpp_accounts(request: web.Request, organization_id) -> web.Response:
    """List the VPP accounts in the organization

    List the VPP accounts in the organization

    :param organization_id: 
    :type organization_id: str

    """
    return web.Response(status=200)


async def lock_network_sm_devices(request: web.Request, network_id, body=None) -> web.Response:
    """Lock a set of devices

    Lock a set of devices

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = LockNetworkSmDevicesRequest.from_dict(body)
    return web.Response(status=200)


async def modify_network_sm_devices_tags(request: web.Request, network_id, body) -> web.Response:
    """Add, delete, or update the tags of a set of devices

    Add, delete, or update the tags of a set of devices

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = ModifyNetworkSmDevicesTagsRequest.from_dict(body)
    return web.Response(status=200)


async def move_network_sm_devices(request: web.Request, network_id, body) -> web.Response:
    """Move a set of devices to a new network

    Move a set of devices to a new network

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = MoveNetworkSmDevicesRequest.from_dict(body)
    return web.Response(status=200)


async def refresh_network_sm_device_details(request: web.Request, network_id, device_id) -> web.Response:
    """Refresh the details of a device

    Refresh the details of a device

    :param network_id: 
    :type network_id: str
    :param device_id: 
    :type device_id: str

    """
    return web.Response(status=200)


async def unenroll_network_sm_device(request: web.Request, network_id, device_id) -> web.Response:
    """Unenroll a device

    Unenroll a device

    :param network_id: 
    :type network_id: str
    :param device_id: 
    :type device_id: str

    """
    return web.Response(status=200)


async def update_network_sm_devices_fields(request: web.Request, network_id, body) -> web.Response:
    """Modify the fields of a device

    Modify the fields of a device

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkSmDevicesFieldsRequest.from_dict(body)
    return web.Response(status=200)


async def update_network_sm_target_group(request: web.Request, network_id, target_group_id, body=None) -> web.Response:
    """Update a target group

    Update a target group

    :param network_id: 
    :type network_id: str
    :param target_group_id: 
    :type target_group_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateNetworkSmTargetGroupRequest.from_dict(body)
    return web.Response(status=200)


async def wipe_network_sm_devices(request: web.Request, network_id, body=None) -> web.Response:
    """Wipe a device

    Wipe a device

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = WipeNetworkSmDevicesRequest.from_dict(body)
    return web.Response(status=200)
