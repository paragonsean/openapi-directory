from typing import List, Dict
from aiohttp import web

from openapi_server.models.get_organization_firmware_upgrades200_response_inner import GetOrganizationFirmwareUpgrades200ResponseInner
from openapi_server.models.get_organization_firmware_upgrades_by_device200_response_inner import GetOrganizationFirmwareUpgradesByDevice200ResponseInner
from openapi_server import util


async def get_organization_firmware_upgrades_1(request: web.Request, organization_id, status=None, product_type=None) -> web.Response:
    """Get firmware upgrade information for an organization

    Get firmware upgrade information for an organization

    :param organization_id: 
    :type organization_id: str
    :param status: The status of an upgrade 
    :type status: List[str]
    :param product_type: The product type in a given upgrade ID
    :type product_type: List[str]

    """
    return web.Response(status=200)


async def get_organization_firmware_upgrades_by_device_1(request: web.Request, organization_id, per_page=None, starting_after=None, ending_before=None, network_ids=None, serials=None, macs=None, firmware_upgrade_ids=None, firmware_upgrade_batch_ids=None) -> web.Response:
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
