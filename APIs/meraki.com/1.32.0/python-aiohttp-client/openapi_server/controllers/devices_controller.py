from typing import List, Dict
from aiohttp import web

from openapi_server.models.blink_device_leds_request import BlinkDeviceLedsRequest
from openapi_server.models.checkin_network_sm_devices200_response import CheckinNetworkSmDevices200Response
from openapi_server.models.checkin_network_sm_devices_request import CheckinNetworkSmDevicesRequest
from openapi_server.models.claim_network_devices_request import ClaimNetworkDevicesRequest
from openapi_server.models.clone_organization_switch_devices_request import CloneOrganizationSwitchDevicesRequest
from openapi_server.models.create_device_live_tools_ping201_response import CreateDeviceLiveToolsPing201Response
from openapi_server.models.create_device_live_tools_ping_device_request import CreateDeviceLiveToolsPingDeviceRequest
from openapi_server.models.create_device_live_tools_ping_request import CreateDeviceLiveToolsPingRequest
from openapi_server.models.get_device_live_tools_ping200_response import GetDeviceLiveToolsPing200Response
from openapi_server.models.get_device_wireless_connection_stats200_response import GetDeviceWirelessConnectionStats200Response
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
from openapi_server.models.get_organization_devices200_response_inner import GetOrganizationDevices200ResponseInner
from openapi_server.models.get_organization_devices_availabilities200_response_inner import GetOrganizationDevicesAvailabilities200ResponseInner
from openapi_server.models.get_organization_devices_power_modules_statuses_by_device200_response_inner import GetOrganizationDevicesPowerModulesStatusesByDevice200ResponseInner
from openapi_server.models.get_organization_devices_statuses200_response import GetOrganizationDevicesStatuses200Response
from openapi_server.models.get_organization_devices_statuses_overview200_response import GetOrganizationDevicesStatusesOverview200Response
from openapi_server.models.get_organization_devices_uplinks_addresses_by_device200_response_inner import GetOrganizationDevicesUplinksAddressesByDevice200ResponseInner
from openapi_server.models.get_organization_devices_uplinks_loss_and_latency200_response_inner import GetOrganizationDevicesUplinksLossAndLatency200ResponseInner
from openapi_server.models.get_organization_inventory_devices200_response_inner import GetOrganizationInventoryDevices200ResponseInner
from openapi_server.models.get_organization_summary_top_devices_by_usage200_response_inner import GetOrganizationSummaryTopDevicesByUsage200ResponseInner
from openapi_server.models.get_organization_summary_top_devices_models_by_usage200_response_inner import GetOrganizationSummaryTopDevicesModelsByUsage200ResponseInner
from openapi_server.models.get_organization_wireless_devices_ethernet_statuses200_response_inner import GetOrganizationWirelessDevicesEthernetStatuses200ResponseInner
from openapi_server.models.lock_network_sm_devices_request import LockNetworkSmDevicesRequest
from openapi_server.models.modify_network_sm_devices_tags200_response_inner import ModifyNetworkSmDevicesTags200ResponseInner
from openapi_server.models.modify_network_sm_devices_tags_request import ModifyNetworkSmDevicesTagsRequest
from openapi_server.models.move_network_sm_devices200_response import MoveNetworkSmDevices200Response
from openapi_server.models.move_network_sm_devices_request import MoveNetworkSmDevicesRequest
from openapi_server.models.remove_network_devices_request import RemoveNetworkDevicesRequest
from openapi_server.models.update_device_cellular_sims_request import UpdateDeviceCellularSimsRequest
from openapi_server.models.update_device_management_interface_request import UpdateDeviceManagementInterfaceRequest
from openapi_server.models.update_device_request import UpdateDeviceRequest
from openapi_server.models.update_network_sm_devices_fields200_response_inner import UpdateNetworkSmDevicesFields200ResponseInner
from openapi_server.models.update_network_sm_devices_fields_request import UpdateNetworkSmDevicesFieldsRequest
from openapi_server.models.vmx_network_devices_claim_request import VmxNetworkDevicesClaimRequest
from openapi_server.models.wipe_network_sm_devices200_response import WipeNetworkSmDevices200Response
from openapi_server.models.wipe_network_sm_devices_request import WipeNetworkSmDevicesRequest
from openapi_server import util


async def blink_device_leds(request: web.Request, serial, body=None) -> web.Response:
    """Blink the LEDs on a device

    Blink the LEDs on a device

    :param serial: 
    :type serial: str
    :param body: 
    :type body: dict | bytes

    """
    body = BlinkDeviceLedsRequest.from_dict(body)
    return web.Response(status=200)


async def checkin_network_sm_devices_1(request: web.Request, network_id, body=None) -> web.Response:
    """Force check-in a set of devices

    Force check-in a set of devices

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CheckinNetworkSmDevicesRequest.from_dict(body)
    return web.Response(status=200)


async def claim_network_devices_1(request: web.Request, network_id, body) -> web.Response:
    """Claim devices into a network. (Note: for recently claimed devices, it may take a few minutes for API requsts against that device to succeed)

    Claim devices into a network. (Note: for recently claimed devices, it may take a few minutes for API requsts against that device to succeed)

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = ClaimNetworkDevicesRequest.from_dict(body)
    return web.Response(status=200)


async def clone_organization_switch_devices_1(request: web.Request, organization_id, body) -> web.Response:
    """Clone port-level and some switch-level configuration settings from a source switch to one or more target switches

    Clone port-level and some switch-level configuration settings from a source switch to one or more target switches. Cloned settings include: Aggregation Groups, Power Settings, Multicast Settings, MTU Configuration, STP Bridge priority, Port Mirroring

    :param organization_id: 
    :type organization_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CloneOrganizationSwitchDevicesRequest.from_dict(body)
    return web.Response(status=200)


async def create_device_live_tools_ping(request: web.Request, serial, body) -> web.Response:
    """Enqueue a job to ping a target host from the device

    Enqueue a job to ping a target host from the device

    :param serial: 
    :type serial: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateDeviceLiveToolsPingRequest.from_dict(body)
    return web.Response(status=200)


async def create_device_live_tools_ping_device(request: web.Request, serial, body=None) -> web.Response:
    """Enqueue a job to check connectivity status to the device

    Enqueue a job to check connectivity status to the device

    :param serial: 
    :type serial: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateDeviceLiveToolsPingDeviceRequest.from_dict(body)
    return web.Response(status=200)


async def get_device(request: web.Request, serial) -> web.Response:
    """Return a single device

    Return a single device

    :param serial: 
    :type serial: str

    """
    return web.Response(status=200)


async def get_device_cellular_sims(request: web.Request, serial) -> web.Response:
    """Return the SIM and APN configurations for a cellular device.

    Return the SIM and APN configurations for a cellular device.

    :param serial: 
    :type serial: str

    """
    return web.Response(status=200)


async def get_device_clients(request: web.Request, serial, t0=None, timespan=None) -> web.Response:
    """List the clients of a device, up to a maximum of a month ago

    List the clients of a device, up to a maximum of a month ago. The usage of each client is returned in kilobytes. If the device is a switch, the switchport is returned; otherwise the switchport field is null.

    :param serial: 
    :type serial: str
    :param t0: The beginning of the timespan for the data. The maximum lookback period is 31 days from today.
    :type t0: str
    :param timespan: The timespan for which the information will be fetched. If specifying timespan, do not specify parameter t0. The value must be in seconds and be less than or equal to 31 days. The default is 1 day.
    :type timespan: float

    """
    return web.Response(status=200)


async def get_device_live_tools_ping(request: web.Request, serial, id) -> web.Response:
    """Return a ping job

    Return a ping job. Latency unit in response is in milliseconds. Size is in bytes.

    :param serial: 
    :type serial: str
    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def get_device_live_tools_ping_device(request: web.Request, serial, id) -> web.Response:
    """Return a ping device job

    Return a ping device job. Latency unit in response is in milliseconds. Size is in bytes.

    :param serial: 
    :type serial: str
    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def get_device_lldp_cdp(request: web.Request, serial) -> web.Response:
    """List LLDP and CDP information for a device

    List LLDP and CDP information for a device

    :param serial: 
    :type serial: str

    """
    return web.Response(status=200)


async def get_device_loss_and_latency_history(request: web.Request, serial, ip, t0=None, t1=None, timespan=None, resolution=None, uplink=None) -> web.Response:
    """Get the uplink loss percentage and latency in milliseconds, and goodput in kilobits per second for a wired network device.

    Get the uplink loss percentage and latency in milliseconds, and goodput in kilobits per second for a wired network device.

    :param serial: 
    :type serial: str
    :param ip: The destination IP used to obtain the requested stats. This is required.
    :type ip: str
    :param t0: The beginning of the timespan for the data. The maximum lookback period is 60 days from today.
    :type t0: str
    :param t1: The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
    :type t1: str
    :param timespan: The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 1 day.
    :type timespan: float
    :param resolution: The time resolution in seconds for returned data. The valid resolutions are: 60, 600, 3600, 86400. The default is 60.
    :type resolution: int
    :param uplink: The WAN uplink used to obtain the requested stats. Valid uplinks are wan1, wan2, cellular. The default is wan1.
    :type uplink: str

    """
    return web.Response(status=200)


async def get_device_management_interface(request: web.Request, serial) -> web.Response:
    """Return the management interface settings for a device

    Return the management interface settings for a device

    :param serial: 
    :type serial: str

    """
    return web.Response(status=200)


async def get_network_devices_1(request: web.Request, network_id) -> web.Response:
    """List the devices in a network

    List the devices in a network

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def get_network_sm_device_cellular_usage_history_1(request: web.Request, network_id, device_id) -> web.Response:
    """Return the client&#39;s daily cellular data usage history

    Return the client&#39;s daily cellular data usage history. Usage data is in kilobytes.

    :param network_id: 
    :type network_id: str
    :param device_id: 
    :type device_id: str

    """
    return web.Response(status=200)


async def get_network_sm_device_certs_1(request: web.Request, network_id, device_id) -> web.Response:
    """List the certs on a device

    List the certs on a device

    :param network_id: 
    :type network_id: str
    :param device_id: 
    :type device_id: str

    """
    return web.Response(status=200)


async def get_network_sm_device_connectivity_1(request: web.Request, network_id, device_id, per_page=None, starting_after=None, ending_before=None) -> web.Response:
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


async def get_network_sm_device_desktop_logs_1(request: web.Request, network_id, device_id, per_page=None, starting_after=None, ending_before=None) -> web.Response:
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


async def get_network_sm_device_device_command_logs_1(request: web.Request, network_id, device_id, per_page=None, starting_after=None, ending_before=None) -> web.Response:
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


async def get_network_sm_device_device_profiles_1(request: web.Request, network_id, device_id) -> web.Response:
    """Get the installed profiles associated with a device

    Get the installed profiles associated with a device

    :param network_id: 
    :type network_id: str
    :param device_id: 
    :type device_id: str

    """
    return web.Response(status=200)


async def get_network_sm_device_network_adapters_1(request: web.Request, network_id, device_id) -> web.Response:
    """List the network adapters of a device

    List the network adapters of a device

    :param network_id: 
    :type network_id: str
    :param device_id: 
    :type device_id: str

    """
    return web.Response(status=200)


async def get_network_sm_device_performance_history_1(request: web.Request, network_id, device_id, per_page=None, starting_after=None, ending_before=None) -> web.Response:
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


async def get_network_sm_device_restrictions_1(request: web.Request, network_id, device_id) -> web.Response:
    """List the restrictions on a device

    List the restrictions on a device

    :param network_id: 
    :type network_id: str
    :param device_id: 
    :type device_id: str

    """
    return web.Response(status=200)


async def get_network_sm_device_security_centers_1(request: web.Request, network_id, device_id) -> web.Response:
    """List the security centers on a device

    List the security centers on a device

    :param network_id: 
    :type network_id: str
    :param device_id: 
    :type device_id: str

    """
    return web.Response(status=200)


async def get_network_sm_device_softwares_1(request: web.Request, network_id, device_id) -> web.Response:
    """Get a list of softwares associated with a device

    Get a list of softwares associated with a device

    :param network_id: 
    :type network_id: str
    :param device_id: 
    :type device_id: str

    """
    return web.Response(status=200)


async def get_network_sm_device_wlan_lists_1(request: web.Request, network_id, device_id) -> web.Response:
    """List the saved SSID names on a device

    List the saved SSID names on a device

    :param network_id: 
    :type network_id: str
    :param device_id: 
    :type device_id: str

    """
    return web.Response(status=200)


async def get_network_sm_devices_1(request: web.Request, network_id, fields=None, wifi_macs=None, serials=None, ids=None, scope=None, per_page=None, starting_after=None, ending_before=None) -> web.Response:
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


async def get_network_wireless_devices_connection_stats_1(request: web.Request, network_id, t0=None, t1=None, timespan=None, band=None, ssid=None, vlan=None, ap_tag=None) -> web.Response:
    """Aggregated connectivity info for this network, grouped by node

    Aggregated connectivity info for this network, grouped by node

    :param network_id: 
    :type network_id: str
    :param t0: The beginning of the timespan for the data. The maximum lookback period is 180 days from today.
    :type t0: str
    :param t1: The end of the timespan for the data. t1 can be a maximum of 7 days after t0.
    :type t1: str
    :param timespan: The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days.
    :type timespan: float
    :param band: Filter results by band (either &#39;2.4&#39;, &#39;5&#39; or &#39;6&#39;). Note that data prior to February 2020 will not have band information.
    :type band: str
    :param ssid: Filter results by SSID
    :type ssid: int
    :param vlan: Filter results by VLAN
    :type vlan: int
    :param ap_tag: Filter results by AP Tag
    :type ap_tag: str

    """
    return web.Response(status=200)


async def get_network_wireless_devices_latency_stats_1(request: web.Request, network_id, t0=None, t1=None, timespan=None, band=None, ssid=None, vlan=None, ap_tag=None, fields=None) -> web.Response:
    """Aggregated latency info for this network, grouped by node

    Aggregated latency info for this network, grouped by node

    :param network_id: 
    :type network_id: str
    :param t0: The beginning of the timespan for the data. The maximum lookback period is 180 days from today.
    :type t0: str
    :param t1: The end of the timespan for the data. t1 can be a maximum of 7 days after t0.
    :type t1: str
    :param timespan: The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days.
    :type timespan: float
    :param band: Filter results by band (either &#39;2.4&#39;, &#39;5&#39; or &#39;6&#39;). Note that data prior to February 2020 will not have band information.
    :type band: str
    :param ssid: Filter results by SSID
    :type ssid: int
    :param vlan: Filter results by VLAN
    :type vlan: int
    :param ap_tag: Filter results by AP Tag
    :type ap_tag: str
    :param fields: Partial selection: If present, this call will return only the selected fields of [\&quot;rawDistribution\&quot;, \&quot;avg\&quot;]. All fields will be returned by default. Selected fields must be entered as a comma separated string.
    :type fields: str

    """
    return web.Response(status=200)


async def get_organization_devices_1(request: web.Request, organization_id, per_page=None, starting_after=None, ending_before=None, configuration_updated_after=None, network_ids=None, product_types=None, tags=None, tags_filter_type=None, name=None, mac=None, serial=None, model=None, macs=None, serials=None, sensor_metrics=None, sensor_alert_profile_ids=None, models=None) -> web.Response:
    """List the devices in an organization

    List the devices in an organization

    :param organization_id: 
    :type organization_id: str
    :param per_page: The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
    :type per_page: int
    :param starting_after: A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type starting_after: str
    :param ending_before: A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type ending_before: str
    :param configuration_updated_after: Filter results by whether or not the device&#39;s configuration has been updated after the given timestamp
    :type configuration_updated_after: str
    :param network_ids: Optional parameter to filter devices by network.
    :type network_ids: List[str]
    :param product_types: Optional parameter to filter devices by product type. Valid types are wireless, appliance, switch, systemsManager, camera, cellularGateway, and sensor.
    :type product_types: List[str]
    :param tags: Optional parameter to filter devices by tags.
    :type tags: List[str]
    :param tags_filter_type: Optional parameter of value &#39;withAnyTags&#39; or &#39;withAllTags&#39; to indicate whether to return networks which contain ANY or ALL of the included tags. If no type is included, &#39;withAnyTags&#39; will be selected.
    :type tags_filter_type: str
    :param name: Optional parameter to filter devices by name. All returned devices will have a name that contains the search term or is an exact match.
    :type name: str
    :param mac: Optional parameter to filter devices by MAC address. All returned devices will have a MAC address that contains the search term or is an exact match.
    :type mac: str
    :param serial: Optional parameter to filter devices by serial number. All returned devices will have a serial number that contains the search term or is an exact match.
    :type serial: str
    :param model: Optional parameter to filter devices by model. All returned devices will have a model that contains the search term or is an exact match.
    :type model: str
    :param macs: Optional parameter to filter devices by one or more MAC addresses. All returned devices will have a MAC address that is an exact match.
    :type macs: List[str]
    :param serials: Optional parameter to filter devices by one or more serial numbers. All returned devices will have a serial number that is an exact match.
    :type serials: List[str]
    :param sensor_metrics: Optional parameter to filter devices by the metrics that they provide. Only applies to sensor devices.
    :type sensor_metrics: List[str]
    :param sensor_alert_profile_ids: Optional parameter to filter devices by the alert profiles that are bound to them. Only applies to sensor devices.
    :type sensor_alert_profile_ids: List[str]
    :param models: Optional parameter to filter devices by one or more models. All returned devices will have a model that is an exact match.
    :type models: List[str]

    """
    return web.Response(status=200)


async def get_organization_devices_availabilities_1(request: web.Request, organization_id, per_page=None, starting_after=None, ending_before=None, network_ids=None, product_types=None, serials=None, tags=None, tags_filter_type=None) -> web.Response:
    """List the availability information for devices in an organization

    List the availability information for devices in an organization. The data returned by this endpoint is updated every 5 minutes.

    :param organization_id: 
    :type organization_id: str
    :param per_page: The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
    :type per_page: int
    :param starting_after: A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type starting_after: str
    :param ending_before: A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type ending_before: str
    :param network_ids: Optional parameter to filter device availabilities by network ID. This filter uses multiple exact matches.
    :type network_ids: List[str]
    :param product_types: Optional parameter to filter device availabilities by device product types. This filter uses multiple exact matches.
    :type product_types: List[str]
    :param serials: Optional parameter to filter device availabilities by device serial numbers. This filter uses multiple exact matches.
    :type serials: List[str]
    :param tags: An optional parameter to filter devices by tags. The filtering is case-sensitive. If tags are included, &#39;tagsFilterType&#39; should also be included (see below). This filter uses multiple exact matches.
    :type tags: List[str]
    :param tags_filter_type: An optional parameter of value &#39;withAnyTags&#39; or &#39;withAllTags&#39; to indicate whether to return devices which contain ANY or ALL of the included tags. If no type is included, &#39;withAnyTags&#39; will be selected.
    :type tags_filter_type: str

    """
    return web.Response(status=200)


async def get_organization_devices_power_modules_statuses_by_device_1(request: web.Request, organization_id, per_page=None, starting_after=None, ending_before=None, network_ids=None, product_types=None, serials=None, tags=None, tags_filter_type=None) -> web.Response:
    """List the power status information for devices in an organization

    List the power status information for devices in an organization. The data returned by this endpoint is updated every 5 minutes.

    :param organization_id: 
    :type organization_id: str
    :param per_page: The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
    :type per_page: int
    :param starting_after: A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type starting_after: str
    :param ending_before: A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type ending_before: str
    :param network_ids: Optional parameter to filter device availabilities by network ID. This filter uses multiple exact matches.
    :type network_ids: List[str]
    :param product_types: Optional parameter to filter device availabilities by device product types. This filter uses multiple exact matches.
    :type product_types: List[str]
    :param serials: Optional parameter to filter device availabilities by device serial numbers. This filter uses multiple exact matches.
    :type serials: List[str]
    :param tags: An optional parameter to filter devices by tags. The filtering is case-sensitive. If tags are included, &#39;tagsFilterType&#39; should also be included (see below). This filter uses multiple exact matches.
    :type tags: List[str]
    :param tags_filter_type: An optional parameter of value &#39;withAnyTags&#39; or &#39;withAllTags&#39; to indicate whether to return devices which contain ANY or ALL of the included tags. If no type is included, &#39;withAnyTags&#39; will be selected.
    :type tags_filter_type: str

    """
    return web.Response(status=200)


async def get_organization_devices_statuses_1(request: web.Request, organization_id, per_page=None, starting_after=None, ending_before=None, network_ids=None, serials=None, statuses=None, product_types=None, models=None, tags=None, tags_filter_type=None) -> web.Response:
    """List the status of every Meraki device in the organization

    List the status of every Meraki device in the organization

    :param organization_id: 
    :type organization_id: str
    :param per_page: The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
    :type per_page: int
    :param starting_after: A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type starting_after: str
    :param ending_before: A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type ending_before: str
    :param network_ids: Optional parameter to filter devices by network ids.
    :type network_ids: List[str]
    :param serials: Optional parameter to filter devices by serials.
    :type serials: List[str]
    :param statuses: Optional parameter to filter devices by statuses. Valid statuses are [\&quot;online\&quot;, \&quot;alerting\&quot;, \&quot;offline\&quot;, \&quot;dormant\&quot;].
    :type statuses: List[str]
    :param product_types: An optional parameter to filter device statuses by product type. Valid types are wireless, appliance, switch, systemsManager, camera, cellularGateway, and sensor.
    :type product_types: List[str]
    :param models: Optional parameter to filter devices by models.
    :type models: List[str]
    :param tags: An optional parameter to filter devices by tags. The filtering is case-sensitive. If tags are included, &#39;tagsFilterType&#39; should also be included (see below).
    :type tags: List[str]
    :param tags_filter_type: An optional parameter of value &#39;withAnyTags&#39; or &#39;withAllTags&#39; to indicate whether to return devices which contain ANY or ALL of the included tags. If no type is included, &#39;withAnyTags&#39; will be selected.
    :type tags_filter_type: str

    """
    return web.Response(status=200)


async def get_organization_devices_statuses_overview_1(request: web.Request, organization_id, product_types=None, network_ids=None) -> web.Response:
    """Return an overview of current device statuses

    Return an overview of current device statuses

    :param organization_id: 
    :type organization_id: str
    :param product_types: An optional parameter to filter device statuses by product type. Valid types are wireless, appliance, switch, systemsManager, camera, cellularGateway, and sensor.
    :type product_types: List[str]
    :param network_ids: An optional parameter to filter device statuses by network.
    :type network_ids: List[str]

    """
    return web.Response(status=200)


async def get_organization_devices_uplinks_addresses_by_device_1(request: web.Request, organization_id, per_page=None, starting_after=None, ending_before=None, network_ids=None, product_types=None, serials=None, tags=None, tags_filter_type=None) -> web.Response:
    """List the current uplink addresses for devices in an organization.

    List the current uplink addresses for devices in an organization.

    :param organization_id: 
    :type organization_id: str
    :param per_page: The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
    :type per_page: int
    :param starting_after: A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type starting_after: str
    :param ending_before: A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type ending_before: str
    :param network_ids: Optional parameter to filter device uplinks by network ID. This filter uses multiple exact matches.
    :type network_ids: List[str]
    :param product_types: Optional parameter to filter device uplinks by device product types. This filter uses multiple exact matches.
    :type product_types: List[str]
    :param serials: Optional parameter to filter device availabilities by device serial numbers. This filter uses multiple exact matches.
    :type serials: List[str]
    :param tags: An optional parameter to filter devices by tags. The filtering is case-sensitive. If tags are included, &#39;tagsFilterType&#39; should also be included (see below). This filter uses multiple exact matches.
    :type tags: List[str]
    :param tags_filter_type: An optional parameter of value &#39;withAnyTags&#39; or &#39;withAllTags&#39; to indicate whether to return devices which contain ANY or ALL of the included tags. If no type is included, &#39;withAnyTags&#39; will be selected.
    :type tags_filter_type: str

    """
    return web.Response(status=200)


async def get_organization_devices_uplinks_loss_and_latency_1(request: web.Request, organization_id, t0=None, t1=None, timespan=None, uplink=None, ip=None) -> web.Response:
    """Return the uplink loss and latency for every MX in the organization from at latest 2 minutes ago

    Return the uplink loss and latency for every MX in the organization from at latest 2 minutes ago

    :param organization_id: 
    :type organization_id: str
    :param t0: The beginning of the timespan for the data. The maximum lookback period is 60 days from today.
    :type t0: str
    :param t1: The end of the timespan for the data. t1 can be a maximum of 5 minutes after t0. The latest possible time that t1 can be is 2 minutes into the past.
    :type t1: str
    :param timespan: The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 5 minutes. The default is 5 minutes.
    :type timespan: float
    :param uplink: Optional filter for a specific WAN uplink. Valid uplinks are wan1, wan2, cellular. Default will return all uplinks.
    :type uplink: str
    :param ip: Optional filter for a specific destination IP. Default will return all destination IPs.
    :type ip: str

    """
    return web.Response(status=200)


async def get_organization_inventory_device_2(request: web.Request, organization_id, serial) -> web.Response:
    """Return a single device from the inventory of an organization

    Return a single device from the inventory of an organization

    :param organization_id: 
    :type organization_id: str
    :param serial: 
    :type serial: str

    """
    return web.Response(status=200)


async def get_organization_inventory_devices_2(request: web.Request, organization_id, per_page=None, starting_after=None, ending_before=None, used_state=None, search=None, macs=None, network_ids=None, serials=None, models=None, order_numbers=None, tags=None, tags_filter_type=None, product_types=None) -> web.Response:
    """Return the device inventory for an organization

    Return the device inventory for an organization

    :param organization_id: 
    :type organization_id: str
    :param per_page: The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
    :type per_page: int
    :param starting_after: A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type starting_after: str
    :param ending_before: A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type ending_before: str
    :param used_state: Filter results by used or unused inventory. Accepted values are &#39;used&#39; or &#39;unused&#39;.
    :type used_state: str
    :param search: Search for devices in inventory based on serial number, mac address, or model.
    :type search: str
    :param macs: Search for devices in inventory based on mac addresses.
    :type macs: List[str]
    :param network_ids: Search for devices in inventory based on network ids.
    :type network_ids: List[str]
    :param serials: Search for devices in inventory based on serials.
    :type serials: List[str]
    :param models: Search for devices in inventory based on model.
    :type models: List[str]
    :param order_numbers: Search for devices in inventory based on order numbers.
    :type order_numbers: List[str]
    :param tags: Filter devices by tags. The filtering is case-sensitive. If tags are included, &#39;tagsFilterType&#39; should also be included (see below).
    :type tags: List[str]
    :param tags_filter_type: To use with &#39;tags&#39; parameter, to filter devices which contain ANY or ALL given tags. Accepted values are &#39;withAnyTags&#39; or &#39;withAllTags&#39;, default is &#39;withAnyTags&#39;.
    :type tags_filter_type: str
    :param product_types: Filter devices by product type. Accepted values are appliance, camera, cellularGateway, sensor, switch, systemsManager, and wireless.
    :type product_types: List[str]

    """
    return web.Response(status=200)


async def get_organization_summary_top_devices_by_usage_3(request: web.Request, organization_id, t0=None, t1=None, timespan=None) -> web.Response:
    """Return metrics for organization&#39;s top 10 devices sorted by data usage over given time range

    Return metrics for organization&#39;s top 10 devices sorted by data usage over given time range. Default unit is megabytes.

    :param organization_id: 
    :type organization_id: str
    :param t0: The beginning of the timespan for the data.
    :type t0: str
    :param t1: The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
    :type t1: str
    :param timespan: The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 1 day.
    :type timespan: float

    """
    return web.Response(status=200)


async def get_organization_summary_top_devices_models_by_usage_3(request: web.Request, organization_id, t0=None, t1=None, timespan=None) -> web.Response:
    """Return metrics for organization&#39;s top 10 device models sorted by data usage over given time range

    Return metrics for organization&#39;s top 10 device models sorted by data usage over given time range. Default unit is megabytes.

    :param organization_id: 
    :type organization_id: str
    :param t0: The beginning of the timespan for the data.
    :type t0: str
    :param t1: The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
    :type t1: str
    :param timespan: The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 1 day.
    :type timespan: float

    """
    return web.Response(status=200)


async def get_organization_wireless_devices_ethernet_statuses_1(request: web.Request, organization_id, per_page=None, starting_after=None, ending_before=None, network_ids=None) -> web.Response:
    """Endpoint to see power status for wireless devices

    Endpoint to see power status for wireless devices

    :param organization_id: 
    :type organization_id: str
    :param per_page: The number of entries per page returned. Acceptable range is 3 - 1000. Default is 100.
    :type per_page: int
    :param starting_after: A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type starting_after: str
    :param ending_before: A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type ending_before: str
    :param network_ids: A list of Meraki network IDs to filter results to contain only specified networks. E.g.: networkIds[]&#x3D;N_12345678&amp;networkIds[]&#x3D;L_3456
    :type network_ids: List[str]

    """
    return web.Response(status=200)


async def lock_network_sm_devices_1(request: web.Request, network_id, body=None) -> web.Response:
    """Lock a set of devices

    Lock a set of devices

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = LockNetworkSmDevicesRequest.from_dict(body)
    return web.Response(status=200)


async def modify_network_sm_devices_tags_1(request: web.Request, network_id, body) -> web.Response:
    """Add, delete, or update the tags of a set of devices

    Add, delete, or update the tags of a set of devices

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = ModifyNetworkSmDevicesTagsRequest.from_dict(body)
    return web.Response(status=200)


async def move_network_sm_devices_1(request: web.Request, network_id, body) -> web.Response:
    """Move a set of devices to a new network

    Move a set of devices to a new network

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = MoveNetworkSmDevicesRequest.from_dict(body)
    return web.Response(status=200)


async def reboot_device(request: web.Request, serial) -> web.Response:
    """Reboot a device

    Reboot a device

    :param serial: 
    :type serial: str

    """
    return web.Response(status=200)


async def refresh_network_sm_device_details_1(request: web.Request, network_id, device_id) -> web.Response:
    """Refresh the details of a device

    Refresh the details of a device

    :param network_id: 
    :type network_id: str
    :param device_id: 
    :type device_id: str

    """
    return web.Response(status=200)


async def remove_network_devices_1(request: web.Request, network_id, body) -> web.Response:
    """Remove a single device

    Remove a single device

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = RemoveNetworkDevicesRequest.from_dict(body)
    return web.Response(status=200)


async def unenroll_network_sm_device_1(request: web.Request, network_id, device_id) -> web.Response:
    """Unenroll a device

    Unenroll a device

    :param network_id: 
    :type network_id: str
    :param device_id: 
    :type device_id: str

    """
    return web.Response(status=200)


async def update_device(request: web.Request, serial, body=None) -> web.Response:
    """Update the attributes of a device

    Update the attributes of a device

    :param serial: 
    :type serial: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateDeviceRequest.from_dict(body)
    return web.Response(status=200)


async def update_device_cellular_sims(request: web.Request, serial, body=None) -> web.Response:
    """Updates the SIM and APN configurations for a cellular device.

    Updates the SIM and APN configurations for a cellular device.

    :param serial: 
    :type serial: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateDeviceCellularSimsRequest.from_dict(body)
    return web.Response(status=200)


async def update_device_management_interface(request: web.Request, serial, body=None) -> web.Response:
    """Update the management interface settings for a device

    Update the management interface settings for a device

    :param serial: 
    :type serial: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateDeviceManagementInterfaceRequest.from_dict(body)
    return web.Response(status=200)


async def update_network_sm_devices_fields_1(request: web.Request, network_id, body) -> web.Response:
    """Modify the fields of a device

    Modify the fields of a device

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkSmDevicesFieldsRequest.from_dict(body)
    return web.Response(status=200)


async def vmx_network_devices_claim_1(request: web.Request, network_id, body) -> web.Response:
    """Claim a vMX into a network

    Claim a vMX into a network

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = VmxNetworkDevicesClaimRequest.from_dict(body)
    return web.Response(status=200)


async def wipe_network_sm_devices_1(request: web.Request, network_id, body=None) -> web.Response:
    """Wipe a device

    Wipe a device

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = WipeNetworkSmDevicesRequest.from_dict(body)
    return web.Response(status=200)
