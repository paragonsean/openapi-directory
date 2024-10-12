from typing import List, Dict
from aiohttp import web

from openapi_server.models.get_network_switch_dhcp_server_policy_arp_inspection_warnings_by_device200_response_inner import GetNetworkSwitchDhcpServerPolicyArpInspectionWarningsByDevice200ResponseInner
from openapi_server.models.get_organization_devices_power_modules_statuses_by_device200_response_inner import GetOrganizationDevicesPowerModulesStatusesByDevice200ResponseInner
from openapi_server.models.get_organization_devices_uplinks_addresses_by_device200_response_inner import GetOrganizationDevicesUplinksAddressesByDevice200ResponseInner
from openapi_server.models.get_organization_firmware_upgrades_by_device200_response_inner import GetOrganizationFirmwareUpgradesByDevice200ResponseInner
from openapi_server import util


async def get_network_switch_dhcp_server_policy_arp_inspection_warnings_by_device_4(request: web.Request, network_id, per_page=None, starting_after=None, ending_before=None) -> web.Response:
    """Return the devices that have a Dynamic ARP Inspection warning and their warnings

    Return the devices that have a Dynamic ARP Inspection warning and their warnings

    :param network_id: 
    :type network_id: str
    :param per_page: The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
    :type per_page: int
    :param starting_after: A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type starting_after: str
    :param ending_before: A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type ending_before: str

    """
    return web.Response(status=200)


async def get_organization_devices_power_modules_statuses_by_device_4(request: web.Request, organization_id, per_page=None, starting_after=None, ending_before=None, network_ids=None, product_types=None, serials=None, tags=None, tags_filter_type=None) -> web.Response:
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


async def get_organization_devices_uplinks_addresses_by_device_4(request: web.Request, organization_id, per_page=None, starting_after=None, ending_before=None, network_ids=None, product_types=None, serials=None, tags=None, tags_filter_type=None) -> web.Response:
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


async def get_organization_firmware_upgrades_by_device_3(request: web.Request, organization_id, per_page=None, starting_after=None, ending_before=None, network_ids=None, serials=None, macs=None, firmware_upgrade_ids=None, firmware_upgrade_batch_ids=None) -> web.Response:
    """Get firmware upgrade status for the filtered devices

    Get firmware upgrade status for the filtered devices

    :param organization_id: 
    :type organization_id: str
    :param per_page: The number of entries per page returned. Acceptable range is 3 - 50. Default is 50.
    :type per_page: int
    :param starting_after: A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type starting_after: str
    :param ending_before: A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type ending_before: str
    :param network_ids: Optional parameter to filter by network
    :type network_ids: List[str]
    :param serials: Optional parameter to filter by serial number.  All returned devices will have a serial number that is an exact match.
    :type serials: List[str]
    :param macs: Optional parameter to filter by one or more MAC addresses belonging to devices. All devices returned belong to MAC addresses that are an exact match.
    :type macs: List[str]
    :param firmware_upgrade_ids: Optional parameter to filter by firmware upgrade ids.
    :type firmware_upgrade_ids: List[str]
    :param firmware_upgrade_batch_ids: Optional parameter to filter by firmware upgrade batch ids.
    :type firmware_upgrade_batch_ids: List[str]

    """
    return web.Response(status=200)
