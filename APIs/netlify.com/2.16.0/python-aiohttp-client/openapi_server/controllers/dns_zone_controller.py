from typing import List, Dict
from aiohttp import web

from openapi_server.models.dns_record import DnsRecord
from openapi_server.models.dns_record_create import DnsRecordCreate
from openapi_server.models.dns_zone import DnsZone
from openapi_server.models.dns_zone_setup import DnsZoneSetup
from openapi_server.models.error import Error
from openapi_server import util


async def configure_dns_for_site(request: web.Request, site_id) -> web.Response:
    """configure_dns_for_site

    

    :param site_id: 
    :type site_id: str

    """
    return web.Response(status=200)


async def create_dns_record(request: web.Request, zone_id, dns_record) -> web.Response:
    """create_dns_record

    

    :param zone_id: 
    :type zone_id: str
    :param dns_record: 
    :type dns_record: dict | bytes

    """
    dns_record = DnsRecordCreate.from_dict(dns_record)
    return web.Response(status=200)


async def create_dns_zone(request: web.Request, dns_zone_params) -> web.Response:
    """create_dns_zone

    

    :param dns_zone_params: 
    :type dns_zone_params: dict | bytes

    """
    dns_zone_params = DnsZoneSetup.from_dict(dns_zone_params)
    return web.Response(status=200)


async def delete_dns_record(request: web.Request, zone_id, dns_record_id) -> web.Response:
    """delete_dns_record

    

    :param zone_id: 
    :type zone_id: str
    :param dns_record_id: 
    :type dns_record_id: str

    """
    return web.Response(status=200)


async def delete_dns_zone(request: web.Request, zone_id) -> web.Response:
    """delete_dns_zone

    

    :param zone_id: 
    :type zone_id: str

    """
    return web.Response(status=200)


async def get_dns_for_site(request: web.Request, site_id) -> web.Response:
    """get_dns_for_site

    

    :param site_id: 
    :type site_id: str

    """
    return web.Response(status=200)


async def get_dns_records(request: web.Request, zone_id) -> web.Response:
    """get_dns_records

    

    :param zone_id: 
    :type zone_id: str

    """
    return web.Response(status=200)


async def get_dns_zone(request: web.Request, zone_id) -> web.Response:
    """get_dns_zone

    

    :param zone_id: 
    :type zone_id: str

    """
    return web.Response(status=200)


async def get_dns_zones(request: web.Request, account_slug=None) -> web.Response:
    """get_dns_zones

    

    :param account_slug: 
    :type account_slug: str

    """
    return web.Response(status=200)


async def get_individual_dns_record(request: web.Request, zone_id, dns_record_id) -> web.Response:
    """get_individual_dns_record

    

    :param zone_id: 
    :type zone_id: str
    :param dns_record_id: 
    :type dns_record_id: str

    """
    return web.Response(status=200)


async def transfer_dns_zone(request: web.Request, zone_id, account_id, transfer_account_id, transfer_user_id) -> web.Response:
    """transfer_dns_zone

    

    :param zone_id: 
    :type zone_id: str
    :param account_id: the account of the dns zone
    :type account_id: str
    :param transfer_account_id: the account you want to transfer the dns zone to
    :type transfer_account_id: str
    :param transfer_user_id: the user you want to transfer the dns zone to
    :type transfer_user_id: str

    """
    return web.Response(status=200)
