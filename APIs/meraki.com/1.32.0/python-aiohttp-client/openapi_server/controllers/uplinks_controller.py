from typing import List, Dict
from aiohttp import web

from openapi_server.models.get_device_appliance_uplinks_settings200_response import GetDeviceApplianceUplinksSettings200Response
from openapi_server.models.get_organization_devices_uplinks_addresses_by_device200_response_inner import GetOrganizationDevicesUplinksAddressesByDevice200ResponseInner
from openapi_server.models.get_organization_devices_uplinks_loss_and_latency200_response_inner import GetOrganizationDevicesUplinksLossAndLatency200ResponseInner
from openapi_server.models.get_organization_uplinks_statuses200_response_inner import GetOrganizationUplinksStatuses200ResponseInner
from openapi_server.models.update_device_appliance_uplinks_settings_request import UpdateDeviceApplianceUplinksSettingsRequest
from openapi_server import util


async def get_device_appliance_uplinks_settings_1(request: web.Request, serial) -> web.Response:
    """Return the uplink settings for an MX appliance

    Return the uplink settings for an MX appliance

    :param serial: 
    :type serial: str

    """
    return web.Response(status=200)


async def get_device_loss_and_latency_history_1(request: web.Request, serial, ip, t0=None, t1=None, timespan=None, resolution=None, uplink=None) -> web.Response:
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


async def get_network_appliance_uplinks_usage_history_1(request: web.Request, network_id, t0=None, t1=None, timespan=None, resolution=None) -> web.Response:
    """Get the sent and received bytes for each uplink of a network.

    Get the sent and received bytes for each uplink of a network.

    :param network_id: 
    :type network_id: str
    :param t0: The beginning of the timespan for the data. The maximum lookback period is 365 days from today.
    :type t0: str
    :param t1: The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
    :type t1: str
    :param timespan: The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 10 minutes.
    :type timespan: float
    :param resolution: The time resolution in seconds for returned data. The valid resolutions are: 60, 300, 600, 1800, 3600, 86400. The default is 60.
    :type resolution: int

    """
    return web.Response(status=200)


async def get_organization_appliance_uplink_statuses_1(request: web.Request, organization_id, per_page=None, starting_after=None, ending_before=None, network_ids=None, serials=None, iccids=None) -> web.Response:
    """List the uplink status of every Meraki MX and Z series appliances in the organization

    List the uplink status of every Meraki MX and Z series appliances in the organization

    :param organization_id: 
    :type organization_id: str
    :param per_page: The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
    :type per_page: int
    :param starting_after: A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type starting_after: str
    :param ending_before: A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type ending_before: str
    :param network_ids: A list of network IDs. The returned devices will be filtered to only include these networks.
    :type network_ids: List[str]
    :param serials: A list of serial numbers. The returned devices will be filtered to only include these serials.
    :type serials: List[str]
    :param iccids: A list of ICCIDs. The returned devices will be filtered to only include these ICCIDs.
    :type iccids: List[str]

    """
    return web.Response(status=200)


async def get_organization_devices_uplinks_addresses_by_device_2(request: web.Request, organization_id, per_page=None, starting_after=None, ending_before=None, network_ids=None, product_types=None, serials=None, tags=None, tags_filter_type=None) -> web.Response:
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


async def get_organization_devices_uplinks_loss_and_latency_2(request: web.Request, organization_id, t0=None, t1=None, timespan=None, uplink=None, ip=None) -> web.Response:
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


async def get_organization_uplinks_statuses_1(request: web.Request, organization_id, per_page=None, starting_after=None, ending_before=None, network_ids=None, serials=None, iccids=None) -> web.Response:
    """List the uplink status of every Meraki MX, MG and Z series devices in the organization

    List the uplink status of every Meraki MX, MG and Z series devices in the organization

    :param organization_id: 
    :type organization_id: str
    :param per_page: The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
    :type per_page: int
    :param starting_after: A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type starting_after: str
    :param ending_before: A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type ending_before: str
    :param network_ids: A list of network IDs. The returned devices will be filtered to only include these networks.
    :type network_ids: List[str]
    :param serials: A list of serial numbers. The returned devices will be filtered to only include these serials.
    :type serials: List[str]
    :param iccids: A list of ICCIDs. The returned devices will be filtered to only include these ICCIDs.
    :type iccids: List[str]

    """
    return web.Response(status=200)


async def update_device_appliance_uplinks_settings_1(request: web.Request, serial, body) -> web.Response:
    """Update the uplink settings for an MX appliance

    Update the uplink settings for an MX appliance

    :param serial: 
    :type serial: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateDeviceApplianceUplinksSettingsRequest.from_dict(body)
    return web.Response(status=200)
