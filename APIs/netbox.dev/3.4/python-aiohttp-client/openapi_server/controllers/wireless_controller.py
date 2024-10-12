from typing import List, Dict
from aiohttp import web

from openapi_server.models.wireless_lan import WirelessLAN
from openapi_server.models.wireless_lan_group import WirelessLANGroup
from openapi_server.models.wireless_link import WirelessLink
from openapi_server.models.wireless_wireless_lan_groups_list200_response import WirelessWirelessLanGroupsList200Response
from openapi_server.models.wireless_wireless_lans_list200_response import WirelessWirelessLansList200Response
from openapi_server.models.wireless_wireless_links_list200_response import WirelessWirelessLinksList200Response
from openapi_server.models.writable_wireless_lan import WritableWirelessLAN
from openapi_server.models.writable_wireless_lan_group import WritableWirelessLANGroup
from openapi_server.models.writable_wireless_link import WritableWirelessLink
from openapi_server import util


async def wireless_wireless_lan_groups_bulk_delete(request: web.Request, ) -> web.Response:
    """wireless_wireless_lan_groups_bulk_delete

    


    """
    return web.Response(status=200)


async def wireless_wireless_lan_groups_bulk_partial_update(request: web.Request, body) -> web.Response:
    """wireless_wireless_lan_groups_bulk_partial_update

    

    :param body: 
    :type body: dict | bytes

    """
    body = WritableWirelessLANGroup.from_dict(body)
    return web.Response(status=200)


async def wireless_wireless_lan_groups_bulk_update(request: web.Request, body) -> web.Response:
    """wireless_wireless_lan_groups_bulk_update

    

    :param body: 
    :type body: dict | bytes

    """
    body = WritableWirelessLANGroup.from_dict(body)
    return web.Response(status=200)


async def wireless_wireless_lan_groups_create(request: web.Request, body) -> web.Response:
    """wireless_wireless_lan_groups_create

    

    :param body: 
    :type body: dict | bytes

    """
    body = WritableWirelessLANGroup.from_dict(body)
    return web.Response(status=200)


async def wireless_wireless_lan_groups_delete(request: web.Request, id) -> web.Response:
    """wireless_wireless_lan_groups_delete

    

    :param id: A unique integer value identifying this Wireless LAN Group.
    :type id: int

    """
    return web.Response(status=200)


async def wireless_wireless_lan_groups_list(request: web.Request, id=None, name=None, slug=None, description=None, created=None, last_updated=None, q=None, tag=None, parent_id=None, parent=None, id__n=None, id__lte=None, id__lt=None, id__gte=None, id__gt=None, name__n=None, name__ic=None, name__nic=None, name__iew=None, name__niew=None, name__isw=None, name__nisw=None, name__ie=None, name__nie=None, name__empty=None, slug__n=None, slug__ic=None, slug__nic=None, slug__iew=None, slug__niew=None, slug__isw=None, slug__nisw=None, slug__ie=None, slug__nie=None, slug__empty=None, description__n=None, description__ic=None, description__nic=None, description__iew=None, description__niew=None, description__isw=None, description__nisw=None, description__ie=None, description__nie=None, description__empty=None, created__n=None, created__lte=None, created__lt=None, created__gte=None, created__gt=None, last_updated__n=None, last_updated__lte=None, last_updated__lt=None, last_updated__gte=None, last_updated__gt=None, tag__n=None, parent_id__n=None, parent__n=None, ordering=None, limit=None, offset=None) -> web.Response:
    """wireless_wireless_lan_groups_list

    

    :param id: 
    :type id: str
    :param name: 
    :type name: str
    :param slug: 
    :type slug: str
    :param description: 
    :type description: str
    :param created: 
    :type created: str
    :param last_updated: 
    :type last_updated: str
    :param q: 
    :type q: str
    :param tag: 
    :type tag: str
    :param parent_id: 
    :type parent_id: str
    :param parent: 
    :type parent: str
    :param id__n: 
    :type id__n: str
    :param id__lte: 
    :type id__lte: str
    :param id__lt: 
    :type id__lt: str
    :param id__gte: 
    :type id__gte: str
    :param id__gt: 
    :type id__gt: str
    :param name__n: 
    :type name__n: str
    :param name__ic: 
    :type name__ic: str
    :param name__nic: 
    :type name__nic: str
    :param name__iew: 
    :type name__iew: str
    :param name__niew: 
    :type name__niew: str
    :param name__isw: 
    :type name__isw: str
    :param name__nisw: 
    :type name__nisw: str
    :param name__ie: 
    :type name__ie: str
    :param name__nie: 
    :type name__nie: str
    :param name__empty: 
    :type name__empty: str
    :param slug__n: 
    :type slug__n: str
    :param slug__ic: 
    :type slug__ic: str
    :param slug__nic: 
    :type slug__nic: str
    :param slug__iew: 
    :type slug__iew: str
    :param slug__niew: 
    :type slug__niew: str
    :param slug__isw: 
    :type slug__isw: str
    :param slug__nisw: 
    :type slug__nisw: str
    :param slug__ie: 
    :type slug__ie: str
    :param slug__nie: 
    :type slug__nie: str
    :param slug__empty: 
    :type slug__empty: str
    :param description__n: 
    :type description__n: str
    :param description__ic: 
    :type description__ic: str
    :param description__nic: 
    :type description__nic: str
    :param description__iew: 
    :type description__iew: str
    :param description__niew: 
    :type description__niew: str
    :param description__isw: 
    :type description__isw: str
    :param description__nisw: 
    :type description__nisw: str
    :param description__ie: 
    :type description__ie: str
    :param description__nie: 
    :type description__nie: str
    :param description__empty: 
    :type description__empty: str
    :param created__n: 
    :type created__n: str
    :param created__lte: 
    :type created__lte: str
    :param created__lt: 
    :type created__lt: str
    :param created__gte: 
    :type created__gte: str
    :param created__gt: 
    :type created__gt: str
    :param last_updated__n: 
    :type last_updated__n: str
    :param last_updated__lte: 
    :type last_updated__lte: str
    :param last_updated__lt: 
    :type last_updated__lt: str
    :param last_updated__gte: 
    :type last_updated__gte: str
    :param last_updated__gt: 
    :type last_updated__gt: str
    :param tag__n: 
    :type tag__n: str
    :param parent_id__n: 
    :type parent_id__n: str
    :param parent__n: 
    :type parent__n: str
    :param ordering: Which field to use when ordering the results.
    :type ordering: str
    :param limit: Number of results to return per page.
    :type limit: int
    :param offset: The initial index from which to return the results.
    :type offset: int

    """
    return web.Response(status=200)


async def wireless_wireless_lan_groups_partial_update(request: web.Request, id, body) -> web.Response:
    """wireless_wireless_lan_groups_partial_update

    

    :param id: A unique integer value identifying this Wireless LAN Group.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = WritableWirelessLANGroup.from_dict(body)
    return web.Response(status=200)


async def wireless_wireless_lan_groups_read(request: web.Request, id) -> web.Response:
    """wireless_wireless_lan_groups_read

    

    :param id: A unique integer value identifying this Wireless LAN Group.
    :type id: int

    """
    return web.Response(status=200)


async def wireless_wireless_lan_groups_update(request: web.Request, id, body) -> web.Response:
    """wireless_wireless_lan_groups_update

    

    :param id: A unique integer value identifying this Wireless LAN Group.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = WritableWirelessLANGroup.from_dict(body)
    return web.Response(status=200)


async def wireless_wireless_lans_bulk_delete(request: web.Request, ) -> web.Response:
    """wireless_wireless_lans_bulk_delete

    


    """
    return web.Response(status=200)


async def wireless_wireless_lans_bulk_partial_update(request: web.Request, body) -> web.Response:
    """wireless_wireless_lans_bulk_partial_update

    

    :param body: 
    :type body: dict | bytes

    """
    body = WritableWirelessLAN.from_dict(body)
    return web.Response(status=200)


async def wireless_wireless_lans_bulk_update(request: web.Request, body) -> web.Response:
    """wireless_wireless_lans_bulk_update

    

    :param body: 
    :type body: dict | bytes

    """
    body = WritableWirelessLAN.from_dict(body)
    return web.Response(status=200)


async def wireless_wireless_lans_create(request: web.Request, body) -> web.Response:
    """wireless_wireless_lans_create

    

    :param body: 
    :type body: dict | bytes

    """
    body = WritableWirelessLAN.from_dict(body)
    return web.Response(status=200)


async def wireless_wireless_lans_delete(request: web.Request, id) -> web.Response:
    """wireless_wireless_lans_delete

    

    :param id: A unique integer value identifying this Wireless LAN.
    :type id: int

    """
    return web.Response(status=200)


async def wireless_wireless_lans_list(request: web.Request, id=None, ssid=None, auth_psk=None, description=None, created=None, last_updated=None, q=None, tag=None, tenant_group_id=None, tenant_group=None, tenant_id=None, tenant=None, group_id=None, group=None, status=None, vlan_id=None, auth_type=None, auth_cipher=None, id__n=None, id__lte=None, id__lt=None, id__gte=None, id__gt=None, ssid__n=None, ssid__ic=None, ssid__nic=None, ssid__iew=None, ssid__niew=None, ssid__isw=None, ssid__nisw=None, ssid__ie=None, ssid__nie=None, ssid__empty=None, auth_psk__n=None, auth_psk__ic=None, auth_psk__nic=None, auth_psk__iew=None, auth_psk__niew=None, auth_psk__isw=None, auth_psk__nisw=None, auth_psk__ie=None, auth_psk__nie=None, auth_psk__empty=None, description__n=None, description__ic=None, description__nic=None, description__iew=None, description__niew=None, description__isw=None, description__nisw=None, description__ie=None, description__nie=None, description__empty=None, created__n=None, created__lte=None, created__lt=None, created__gte=None, created__gt=None, last_updated__n=None, last_updated__lte=None, last_updated__lt=None, last_updated__gte=None, last_updated__gt=None, tag__n=None, tenant_group_id__n=None, tenant_group__n=None, tenant_id__n=None, tenant__n=None, group_id__n=None, group__n=None, status__n=None, vlan_id__n=None, auth_type__n=None, auth_cipher__n=None, ordering=None, limit=None, offset=None) -> web.Response:
    """wireless_wireless_lans_list

    

    :param id: 
    :type id: str
    :param ssid: 
    :type ssid: str
    :param auth_psk: 
    :type auth_psk: str
    :param description: 
    :type description: str
    :param created: 
    :type created: str
    :param last_updated: 
    :type last_updated: str
    :param q: 
    :type q: str
    :param tag: 
    :type tag: str
    :param tenant_group_id: 
    :type tenant_group_id: str
    :param tenant_group: 
    :type tenant_group: str
    :param tenant_id: 
    :type tenant_id: str
    :param tenant: 
    :type tenant: str
    :param group_id: 
    :type group_id: str
    :param group: 
    :type group: str
    :param status: 
    :type status: str
    :param vlan_id: 
    :type vlan_id: str
    :param auth_type: 
    :type auth_type: str
    :param auth_cipher: 
    :type auth_cipher: str
    :param id__n: 
    :type id__n: str
    :param id__lte: 
    :type id__lte: str
    :param id__lt: 
    :type id__lt: str
    :param id__gte: 
    :type id__gte: str
    :param id__gt: 
    :type id__gt: str
    :param ssid__n: 
    :type ssid__n: str
    :param ssid__ic: 
    :type ssid__ic: str
    :param ssid__nic: 
    :type ssid__nic: str
    :param ssid__iew: 
    :type ssid__iew: str
    :param ssid__niew: 
    :type ssid__niew: str
    :param ssid__isw: 
    :type ssid__isw: str
    :param ssid__nisw: 
    :type ssid__nisw: str
    :param ssid__ie: 
    :type ssid__ie: str
    :param ssid__nie: 
    :type ssid__nie: str
    :param ssid__empty: 
    :type ssid__empty: str
    :param auth_psk__n: 
    :type auth_psk__n: str
    :param auth_psk__ic: 
    :type auth_psk__ic: str
    :param auth_psk__nic: 
    :type auth_psk__nic: str
    :param auth_psk__iew: 
    :type auth_psk__iew: str
    :param auth_psk__niew: 
    :type auth_psk__niew: str
    :param auth_psk__isw: 
    :type auth_psk__isw: str
    :param auth_psk__nisw: 
    :type auth_psk__nisw: str
    :param auth_psk__ie: 
    :type auth_psk__ie: str
    :param auth_psk__nie: 
    :type auth_psk__nie: str
    :param auth_psk__empty: 
    :type auth_psk__empty: str
    :param description__n: 
    :type description__n: str
    :param description__ic: 
    :type description__ic: str
    :param description__nic: 
    :type description__nic: str
    :param description__iew: 
    :type description__iew: str
    :param description__niew: 
    :type description__niew: str
    :param description__isw: 
    :type description__isw: str
    :param description__nisw: 
    :type description__nisw: str
    :param description__ie: 
    :type description__ie: str
    :param description__nie: 
    :type description__nie: str
    :param description__empty: 
    :type description__empty: str
    :param created__n: 
    :type created__n: str
    :param created__lte: 
    :type created__lte: str
    :param created__lt: 
    :type created__lt: str
    :param created__gte: 
    :type created__gte: str
    :param created__gt: 
    :type created__gt: str
    :param last_updated__n: 
    :type last_updated__n: str
    :param last_updated__lte: 
    :type last_updated__lte: str
    :param last_updated__lt: 
    :type last_updated__lt: str
    :param last_updated__gte: 
    :type last_updated__gte: str
    :param last_updated__gt: 
    :type last_updated__gt: str
    :param tag__n: 
    :type tag__n: str
    :param tenant_group_id__n: 
    :type tenant_group_id__n: str
    :param tenant_group__n: 
    :type tenant_group__n: str
    :param tenant_id__n: 
    :type tenant_id__n: str
    :param tenant__n: 
    :type tenant__n: str
    :param group_id__n: 
    :type group_id__n: str
    :param group__n: 
    :type group__n: str
    :param status__n: 
    :type status__n: str
    :param vlan_id__n: 
    :type vlan_id__n: str
    :param auth_type__n: 
    :type auth_type__n: str
    :param auth_cipher__n: 
    :type auth_cipher__n: str
    :param ordering: Which field to use when ordering the results.
    :type ordering: str
    :param limit: Number of results to return per page.
    :type limit: int
    :param offset: The initial index from which to return the results.
    :type offset: int

    """
    return web.Response(status=200)


async def wireless_wireless_lans_partial_update(request: web.Request, id, body) -> web.Response:
    """wireless_wireless_lans_partial_update

    

    :param id: A unique integer value identifying this Wireless LAN.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = WritableWirelessLAN.from_dict(body)
    return web.Response(status=200)


async def wireless_wireless_lans_read(request: web.Request, id) -> web.Response:
    """wireless_wireless_lans_read

    

    :param id: A unique integer value identifying this Wireless LAN.
    :type id: int

    """
    return web.Response(status=200)


async def wireless_wireless_lans_update(request: web.Request, id, body) -> web.Response:
    """wireless_wireless_lans_update

    

    :param id: A unique integer value identifying this Wireless LAN.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = WritableWirelessLAN.from_dict(body)
    return web.Response(status=200)


async def wireless_wireless_links_bulk_delete(request: web.Request, ) -> web.Response:
    """wireless_wireless_links_bulk_delete

    


    """
    return web.Response(status=200)


async def wireless_wireless_links_bulk_partial_update(request: web.Request, body) -> web.Response:
    """wireless_wireless_links_bulk_partial_update

    

    :param body: 
    :type body: dict | bytes

    """
    body = WritableWirelessLink.from_dict(body)
    return web.Response(status=200)


async def wireless_wireless_links_bulk_update(request: web.Request, body) -> web.Response:
    """wireless_wireless_links_bulk_update

    

    :param body: 
    :type body: dict | bytes

    """
    body = WritableWirelessLink.from_dict(body)
    return web.Response(status=200)


async def wireless_wireless_links_create(request: web.Request, body) -> web.Response:
    """wireless_wireless_links_create

    

    :param body: 
    :type body: dict | bytes

    """
    body = WritableWirelessLink.from_dict(body)
    return web.Response(status=200)


async def wireless_wireless_links_delete(request: web.Request, id) -> web.Response:
    """wireless_wireless_links_delete

    

    :param id: A unique integer value identifying this wireless link.
    :type id: int

    """
    return web.Response(status=200)


async def wireless_wireless_links_list(request: web.Request, id=None, ssid=None, auth_psk=None, description=None, created=None, last_updated=None, q=None, tag=None, tenant_group_id=None, tenant_group=None, tenant_id=None, tenant=None, interface_a_id=None, interface_b_id=None, status=None, auth_type=None, auth_cipher=None, id__n=None, id__lte=None, id__lt=None, id__gte=None, id__gt=None, ssid__n=None, ssid__ic=None, ssid__nic=None, ssid__iew=None, ssid__niew=None, ssid__isw=None, ssid__nisw=None, ssid__ie=None, ssid__nie=None, ssid__empty=None, auth_psk__n=None, auth_psk__ic=None, auth_psk__nic=None, auth_psk__iew=None, auth_psk__niew=None, auth_psk__isw=None, auth_psk__nisw=None, auth_psk__ie=None, auth_psk__nie=None, auth_psk__empty=None, description__n=None, description__ic=None, description__nic=None, description__iew=None, description__niew=None, description__isw=None, description__nisw=None, description__ie=None, description__nie=None, description__empty=None, created__n=None, created__lte=None, created__lt=None, created__gte=None, created__gt=None, last_updated__n=None, last_updated__lte=None, last_updated__lt=None, last_updated__gte=None, last_updated__gt=None, tag__n=None, tenant_group_id__n=None, tenant_group__n=None, tenant_id__n=None, tenant__n=None, interface_a_id__n=None, interface_a_id__lte=None, interface_a_id__lt=None, interface_a_id__gte=None, interface_a_id__gt=None, interface_b_id__n=None, interface_b_id__lte=None, interface_b_id__lt=None, interface_b_id__gte=None, interface_b_id__gt=None, status__n=None, auth_type__n=None, auth_cipher__n=None, ordering=None, limit=None, offset=None) -> web.Response:
    """wireless_wireless_links_list

    

    :param id: 
    :type id: str
    :param ssid: 
    :type ssid: str
    :param auth_psk: 
    :type auth_psk: str
    :param description: 
    :type description: str
    :param created: 
    :type created: str
    :param last_updated: 
    :type last_updated: str
    :param q: 
    :type q: str
    :param tag: 
    :type tag: str
    :param tenant_group_id: 
    :type tenant_group_id: str
    :param tenant_group: 
    :type tenant_group: str
    :param tenant_id: 
    :type tenant_id: str
    :param tenant: 
    :type tenant: str
    :param interface_a_id: 
    :type interface_a_id: str
    :param interface_b_id: 
    :type interface_b_id: str
    :param status: 
    :type status: str
    :param auth_type: 
    :type auth_type: str
    :param auth_cipher: 
    :type auth_cipher: str
    :param id__n: 
    :type id__n: str
    :param id__lte: 
    :type id__lte: str
    :param id__lt: 
    :type id__lt: str
    :param id__gte: 
    :type id__gte: str
    :param id__gt: 
    :type id__gt: str
    :param ssid__n: 
    :type ssid__n: str
    :param ssid__ic: 
    :type ssid__ic: str
    :param ssid__nic: 
    :type ssid__nic: str
    :param ssid__iew: 
    :type ssid__iew: str
    :param ssid__niew: 
    :type ssid__niew: str
    :param ssid__isw: 
    :type ssid__isw: str
    :param ssid__nisw: 
    :type ssid__nisw: str
    :param ssid__ie: 
    :type ssid__ie: str
    :param ssid__nie: 
    :type ssid__nie: str
    :param ssid__empty: 
    :type ssid__empty: str
    :param auth_psk__n: 
    :type auth_psk__n: str
    :param auth_psk__ic: 
    :type auth_psk__ic: str
    :param auth_psk__nic: 
    :type auth_psk__nic: str
    :param auth_psk__iew: 
    :type auth_psk__iew: str
    :param auth_psk__niew: 
    :type auth_psk__niew: str
    :param auth_psk__isw: 
    :type auth_psk__isw: str
    :param auth_psk__nisw: 
    :type auth_psk__nisw: str
    :param auth_psk__ie: 
    :type auth_psk__ie: str
    :param auth_psk__nie: 
    :type auth_psk__nie: str
    :param auth_psk__empty: 
    :type auth_psk__empty: str
    :param description__n: 
    :type description__n: str
    :param description__ic: 
    :type description__ic: str
    :param description__nic: 
    :type description__nic: str
    :param description__iew: 
    :type description__iew: str
    :param description__niew: 
    :type description__niew: str
    :param description__isw: 
    :type description__isw: str
    :param description__nisw: 
    :type description__nisw: str
    :param description__ie: 
    :type description__ie: str
    :param description__nie: 
    :type description__nie: str
    :param description__empty: 
    :type description__empty: str
    :param created__n: 
    :type created__n: str
    :param created__lte: 
    :type created__lte: str
    :param created__lt: 
    :type created__lt: str
    :param created__gte: 
    :type created__gte: str
    :param created__gt: 
    :type created__gt: str
    :param last_updated__n: 
    :type last_updated__n: str
    :param last_updated__lte: 
    :type last_updated__lte: str
    :param last_updated__lt: 
    :type last_updated__lt: str
    :param last_updated__gte: 
    :type last_updated__gte: str
    :param last_updated__gt: 
    :type last_updated__gt: str
    :param tag__n: 
    :type tag__n: str
    :param tenant_group_id__n: 
    :type tenant_group_id__n: str
    :param tenant_group__n: 
    :type tenant_group__n: str
    :param tenant_id__n: 
    :type tenant_id__n: str
    :param tenant__n: 
    :type tenant__n: str
    :param interface_a_id__n: 
    :type interface_a_id__n: str
    :param interface_a_id__lte: 
    :type interface_a_id__lte: str
    :param interface_a_id__lt: 
    :type interface_a_id__lt: str
    :param interface_a_id__gte: 
    :type interface_a_id__gte: str
    :param interface_a_id__gt: 
    :type interface_a_id__gt: str
    :param interface_b_id__n: 
    :type interface_b_id__n: str
    :param interface_b_id__lte: 
    :type interface_b_id__lte: str
    :param interface_b_id__lt: 
    :type interface_b_id__lt: str
    :param interface_b_id__gte: 
    :type interface_b_id__gte: str
    :param interface_b_id__gt: 
    :type interface_b_id__gt: str
    :param status__n: 
    :type status__n: str
    :param auth_type__n: 
    :type auth_type__n: str
    :param auth_cipher__n: 
    :type auth_cipher__n: str
    :param ordering: Which field to use when ordering the results.
    :type ordering: str
    :param limit: Number of results to return per page.
    :type limit: int
    :param offset: The initial index from which to return the results.
    :type offset: int

    """
    return web.Response(status=200)


async def wireless_wireless_links_partial_update(request: web.Request, id, body) -> web.Response:
    """wireless_wireless_links_partial_update

    

    :param id: A unique integer value identifying this wireless link.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = WritableWirelessLink.from_dict(body)
    return web.Response(status=200)


async def wireless_wireless_links_read(request: web.Request, id) -> web.Response:
    """wireless_wireless_links_read

    

    :param id: A unique integer value identifying this wireless link.
    :type id: int

    """
    return web.Response(status=200)


async def wireless_wireless_links_update(request: web.Request, id, body) -> web.Response:
    """wireless_wireless_links_update

    

    :param id: A unique integer value identifying this wireless link.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = WritableWirelessLink.from_dict(body)
    return web.Response(status=200)
