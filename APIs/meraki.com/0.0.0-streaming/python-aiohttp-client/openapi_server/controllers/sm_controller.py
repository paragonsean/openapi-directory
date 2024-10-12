from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_network_sm_bypass_activation_lock_attempt_request import CreateNetworkSmBypassActivationLockAttemptRequest
from openapi_server.models.lock_network_sm_devices_request import LockNetworkSmDevicesRequest
from openapi_server.models.update_network_sm_device_fields_request import UpdateNetworkSmDeviceFieldsRequest
from openapi_server.models.update_network_sm_devices_tags_request import UpdateNetworkSmDevicesTagsRequest
from openapi_server.models.wipe_network_sm_device_request import WipeNetworkSmDeviceRequest
from openapi_server import util


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


async def get_network_sm_bypass_activation_lock_attempt(request: web.Request, network_id, attempt_id) -> web.Response:
    """Bypass activation lock attempt status

    Bypass activation lock attempt status

    :param network_id: 
    :type network_id: str
    :param attempt_id: 
    :type attempt_id: str

    """
    return web.Response(status=200)


async def get_network_sm_cellular_usage_history(request: web.Request, network_id, device_id) -> web.Response:
    """Return the client&#39;s daily cellular data usage history

    Return the client&#39;s daily cellular data usage history. Usage data is in kilobytes.

    :param network_id: 
    :type network_id: str
    :param device_id: 
    :type device_id: str

    """
    return web.Response(status=200)


async def get_network_sm_certs(request: web.Request, network_id, device_id) -> web.Response:
    """List the certs on a device

    List the certs on a device

    :param network_id: 
    :type network_id: str
    :param device_id: 
    :type device_id: str

    """
    return web.Response(status=200)


async def get_network_sm_connectivity(request: web.Request, network_id, id, per_page=None, starting_after=None, ending_before=None) -> web.Response:
    """Returns historical connectivity data (whether a device is regularly checking in to Dashboard).

    Returns historical connectivity data (whether a device is regularly checking in to Dashboard).

    :param network_id: 
    :type network_id: str
    :param id: 
    :type id: str
    :param per_page: The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
    :type per_page: int
    :param starting_after: A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type starting_after: str
    :param ending_before: A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type ending_before: str

    """
    return web.Response(status=200)


async def get_network_sm_desktop_logs(request: web.Request, network_id, id, per_page=None, starting_after=None, ending_before=None) -> web.Response:
    """Return historical records of various Systems Manager network connection details for desktop devices.

    Return historical records of various Systems Manager network connection details for desktop devices.

    :param network_id: 
    :type network_id: str
    :param id: 
    :type id: str
    :param per_page: The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
    :type per_page: int
    :param starting_after: A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type starting_after: str
    :param ending_before: A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type ending_before: str

    """
    return web.Response(status=200)


async def get_network_sm_device_command_logs(request: web.Request, network_id, id, per_page=None, starting_after=None, ending_before=None) -> web.Response:
    """Return historical records of commands sent to Systems Manager devices

    Return historical records of commands sent to Systems Manager devices. Note that this will include the name of the Dashboard user who initiated the command if it was generated by a Dashboard admin rather than the automatic behavior of the system; you may wish to filter this out of any reports.

    :param network_id: 
    :type network_id: str
    :param id: 
    :type id: str
    :param per_page: The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
    :type per_page: int
    :param starting_after: A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type starting_after: str
    :param ending_before: A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type ending_before: str

    """
    return web.Response(status=200)


async def get_network_sm_device_profiles(request: web.Request, network_id, device_id) -> web.Response:
    """Get the profiles associated with a device

    Get the profiles associated with a device

    :param network_id: 
    :type network_id: str
    :param device_id: 
    :type device_id: str

    """
    return web.Response(status=200)


async def get_network_sm_devices(request: web.Request, network_id, fields=None, wifi_macs=None, serials=None, ids=None, scope=None, batch_size=None, batch_token=None) -> web.Response:
    """List the devices enrolled in an SM network with various specified fields and filters

    List the devices enrolled in an SM network with various specified fields and filters

    :param network_id: 
    :type network_id: str
    :param fields: Additional fields that will be displayed for each device. Multiple fields can be passed in as comma separated values.     The default fields are: id, name, tags, ssid, wifiMac, osName, systemModel, uuid, and serialNumber. The additional fields are: ip,     systemType, availableDeviceCapacity, kioskAppName, biosVersion, lastConnected, missingAppsCount, userSuppliedAddress, location, lastUser,     ownerEmail, ownerUsername, publicIp, phoneNumber, diskInfoJson, deviceCapacity, isManaged, hadMdm, isSupervised, meid, imei, iccid,     simCarrierNetwork, cellularDataUsed, isHotspotEnabled, createdAt, batteryEstCharge, quarantined, avName, avRunning, asName, fwName,     isRooted, loginRequired, screenLockEnabled, screenLockDelay, autoLoginDisabled, autoTags, hasMdm, hasDesktopAgent, diskEncryptionEnabled,     hardwareEncryptionCaps, passCodeLock, usesHardwareKeystore, and androidSecurityPatchVersion.
    :type fields: str
    :param wifi_macs: Filter devices by wifi mac(s). Multiple wifi macs can be passed in as comma separated values.
    :type wifi_macs: str
    :param serials: Filter devices by serial(s). Multiple serials can be passed in as comma separated values.
    :type serials: str
    :param ids: Filter devices by id(s). Multiple ids can be passed in as comma separated values.
    :type ids: str
    :param scope: Specify a scope (one of all, none, withAny, withAll, withoutAny, or withoutAll) and a set of tags as comma separated values.
    :type scope: str
    :param batch_size: Number of devices to return, 1000 is the default as well as the max.
    :type batch_size: int
    :param batch_token: If the network has more devices than the batch size, a batch token will be returned     as a part of the device list. To see the remainder of the devices, pass in the batchToken as a parameter in the next request.     Requests made with the batchToken do not require additional parameters as the batchToken includes the parameters passed in     with the original request. Additional parameters passed in with the batchToken will be ignored.
    :type batch_token: str

    """
    return web.Response(status=200)


async def get_network_sm_network_adapters(request: web.Request, network_id, device_id) -> web.Response:
    """List the network adapters of a device

    List the network adapters of a device

    :param network_id: 
    :type network_id: str
    :param device_id: 
    :type device_id: str

    """
    return web.Response(status=200)


async def get_network_sm_performance_history(request: web.Request, network_id, id, per_page=None, starting_after=None, ending_before=None) -> web.Response:
    """Return historical records of various Systems Manager client metrics for desktop devices.

    Return historical records of various Systems Manager client metrics for desktop devices.

    :param network_id: 
    :type network_id: str
    :param id: 
    :type id: str
    :param per_page: The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
    :type per_page: int
    :param starting_after: A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type starting_after: str
    :param ending_before: A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type ending_before: str

    """
    return web.Response(status=200)


async def get_network_sm_profiles(request: web.Request, network_id) -> web.Response:
    """List all the profiles in the network

    List all the profiles in the network

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def get_network_sm_restrictions(request: web.Request, network_id, device_id) -> web.Response:
    """List the restrictions on a device

    List the restrictions on a device

    :param network_id: 
    :type network_id: str
    :param device_id: 
    :type device_id: str

    """
    return web.Response(status=200)


async def get_network_sm_security_centers(request: web.Request, network_id, device_id) -> web.Response:
    """List the security centers on a device

    List the security centers on a device

    :param network_id: 
    :type network_id: str
    :param device_id: 
    :type device_id: str

    """
    return web.Response(status=200)


async def get_network_sm_softwares(request: web.Request, network_id, device_id) -> web.Response:
    """Get a list of softwares associated with a device

    Get a list of softwares associated with a device

    :param network_id: 
    :type network_id: str
    :param device_id: 
    :type device_id: str

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
    :param ids: Filter users by id(s). Multiple ids can be passed in as comma separated values.
    :type ids: str
    :param usernames: Filter users by username(s). Multiple usernames can be passed in as comma separated values.
    :type usernames: str
    :param emails: Filter users by email(s). Multiple emails can be passed in as comma separated values.
    :type emails: str
    :param scope: Specifiy a scope (one of all, none, withAny, withAll, withoutAny, withoutAll) and a set of tags as comma separated values.
    :type scope: str

    """
    return web.Response(status=200)


async def get_network_sm_wlan_lists(request: web.Request, network_id, device_id) -> web.Response:
    """List the saved SSID names on a device

    List the saved SSID names on a device

    :param network_id: 
    :type network_id: str
    :param device_id: 
    :type device_id: str

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


async def update_network_sm_device_fields(request: web.Request, network_id, body) -> web.Response:
    """Modify the fields of a device

    Modify the fields of a device

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkSmDeviceFieldsRequest.from_dict(body)
    return web.Response(status=200)


async def update_network_sm_devices_tags(request: web.Request, network_id, body) -> web.Response:
    """Add, delete, or update the tags of a set of devices

    Add, delete, or update the tags of a set of devices

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkSmDevicesTagsRequest.from_dict(body)
    return web.Response(status=200)


async def wipe_network_sm_device(request: web.Request, network_id, body=None) -> web.Response:
    """Wipe a device

    Wipe a device

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = WipeNetworkSmDeviceRequest.from_dict(body)
    return web.Response(status=200)
