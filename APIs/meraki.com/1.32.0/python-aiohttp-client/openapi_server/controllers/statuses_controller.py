from typing import List, Dict
from aiohttp import web

from openapi_server.models.get_device_switch_ports_statuses200_response_inner import GetDeviceSwitchPortsStatuses200ResponseInner
from openapi_server.models.get_organization_cellular_gateway_uplink_statuses200_response_inner import GetOrganizationCellularGatewayUplinkStatuses200ResponseInner
from openapi_server.models.get_organization_devices_power_modules_statuses_by_device200_response_inner import GetOrganizationDevicesPowerModulesStatusesByDevice200ResponseInner
from openapi_server.models.get_organization_devices_statuses200_response import GetOrganizationDevicesStatuses200Response
from openapi_server.models.get_organization_devices_statuses_overview200_response import GetOrganizationDevicesStatusesOverview200Response
from openapi_server.models.get_organization_uplinks_statuses200_response_inner import GetOrganizationUplinksStatuses200ResponseInner
from openapi_server.models.get_organization_wireless_devices_ethernet_statuses200_response_inner import GetOrganizationWirelessDevicesEthernetStatuses200ResponseInner
from openapi_server.models.update_organization_camera_onboarding_statuses_request import UpdateOrganizationCameraOnboardingStatusesRequest
from openapi_server import util


async def get_device_switch_ports_statuses_2(request: web.Request, serial, t0=None, timespan=None) -> web.Response:
    """Return the status for all the ports of a switch

    Return the status for all the ports of a switch

    :param serial: 
    :type serial: str
    :param t0: The beginning of the timespan for the data. The maximum lookback period is 31 days from today.
    :type t0: str
    :param timespan: The timespan for which the information will be fetched. If specifying timespan, do not specify parameter t0. The value must be in seconds and be less than or equal to 31 days. The default is 1 day.
    :type timespan: float

    """
    return web.Response(status=200)


async def get_device_switch_ports_statuses_packets_2(request: web.Request, serial, t0=None, timespan=None) -> web.Response:
    """Return the packet counters for all the ports of a switch

    Return the packet counters for all the ports of a switch

    :param serial: 
    :type serial: str
    :param t0: The beginning of the timespan for the data. The maximum lookback period is 1 day from today.
    :type t0: str
    :param timespan: The timespan for which the information will be fetched. If specifying timespan, do not specify parameter t0. The value must be in seconds and be less than or equal to 1 day. The default is 1 day.
    :type timespan: float

    """
    return web.Response(status=200)


async def get_organization_appliance_uplink_statuses_2(request: web.Request, organization_id, per_page=None, starting_after=None, ending_before=None, network_ids=None, serials=None, iccids=None) -> web.Response:
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


async def get_organization_appliance_vpn_statuses_2(request: web.Request, organization_id, per_page=None, starting_after=None, ending_before=None, network_ids=None) -> web.Response:
    """Show VPN status for networks in an organization

    Show VPN status for networks in an organization

    :param organization_id: 
    :type organization_id: str
    :param per_page: The number of entries per page returned. Acceptable range is 3 - 300. Default is 300.
    :type per_page: int
    :param starting_after: A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type starting_after: str
    :param ending_before: A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type ending_before: str
    :param network_ids: A list of Meraki network IDs to filter results to contain only specified networks. E.g.: networkIds[]&#x3D;N_12345678&amp;networkIds[]&#x3D;L_3456
    :type network_ids: List[str]

    """
    return web.Response(status=200)


async def get_organization_camera_onboarding_statuses_2(request: web.Request, organization_id, serials=None, network_ids=None) -> web.Response:
    """Fetch onboarding status of cameras

    Fetch onboarding status of cameras

    :param organization_id: 
    :type organization_id: str
    :param serials: A list of serial numbers. The returned cameras will be filtered to only include these serials.
    :type serials: List[str]
    :param network_ids: A list of network IDs. The returned cameras will be filtered to only include these networks.
    :type network_ids: List[str]

    """
    return web.Response(status=200)


async def get_organization_cellular_gateway_uplink_statuses_2(request: web.Request, organization_id, per_page=None, starting_after=None, ending_before=None, network_ids=None, serials=None, iccids=None) -> web.Response:
    """List the uplink status of every Meraki MG cellular gateway in the organization

    List the uplink status of every Meraki MG cellular gateway in the organization

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


async def get_organization_devices_power_modules_statuses_by_device_3(request: web.Request, organization_id, per_page=None, starting_after=None, ending_before=None, network_ids=None, product_types=None, serials=None, tags=None, tags_filter_type=None) -> web.Response:
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


async def get_organization_devices_statuses_2(request: web.Request, organization_id, per_page=None, starting_after=None, ending_before=None, network_ids=None, serials=None, statuses=None, product_types=None, models=None, tags=None, tags_filter_type=None) -> web.Response:
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


async def get_organization_devices_statuses_overview_2(request: web.Request, organization_id, product_types=None, network_ids=None) -> web.Response:
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


async def get_organization_uplinks_statuses_2(request: web.Request, organization_id, per_page=None, starting_after=None, ending_before=None, network_ids=None, serials=None, iccids=None) -> web.Response:
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


async def get_organization_wireless_devices_ethernet_statuses_3(request: web.Request, organization_id, per_page=None, starting_after=None, ending_before=None, network_ids=None) -> web.Response:
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


async def update_organization_camera_onboarding_statuses_2(request: web.Request, organization_id, body=None) -> web.Response:
    """Notify that credential handoff to camera has completed

    Notify that credential handoff to camera has completed

    :param organization_id: 
    :type organization_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateOrganizationCameraOnboardingStatusesRequest.from_dict(body)
    return web.Response(status=200)
