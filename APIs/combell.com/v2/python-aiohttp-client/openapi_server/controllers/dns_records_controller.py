from typing import List, Dict
from aiohttp import web

from openapi_server.models.dns_record import DnsRecord
from openapi_server import util


async def dns_domain_name_records_get(request: web.Request, domain_name, domain_name2, skip=None, take=None, type=None, record_name=None, service=None) -> web.Response:
    """Get records

    

    :param domain_name: The domain name.
    :type domain_name: str
    :param domain_name2: Automatically added
    :type domain_name2: str
    :param skip: The number of items to skip in the resultset.
    :type skip: int
    :param take: The number of items to return in the resultset. The returned count can be equal or less than this number.
    :type take: int
    :param type: Filters records matching the type. Most other filters only apply when this filter is specified.
    :type type: str
    :param record_name: Filters records matching the record name. This filter only applies to lookups of A, CNAME, TXT, CAA, ALIAS and TLSA records.
    :type record_name: str
    :param service: Filters records for the service. This filter only applies to lookups of SRV records.
    :type service: str

    """
    return web.Response(status=200)


async def dns_domain_name_records_post(request: web.Request, domain_name, domain_name2, body=None) -> web.Response:
    """Create a record

    

    :param domain_name: The domain name.
    :type domain_name: str
    :param domain_name2: Automatically added
    :type domain_name2: str
    :param body: The record to create
    :type body: dict | bytes

    """
    body = DnsRecord.from_dict(body)
    return web.Response(status=200)


async def dns_domain_name_records_record_id_delete(request: web.Request, domain_name, record_id, domain_name2, record_id2) -> web.Response:
    """Delete a record

    

    :param domain_name: The domain name.
    :type domain_name: str
    :param record_id: The id of the record.
    :type record_id: str
    :param domain_name2: Automatically added
    :type domain_name2: str
    :param record_id2: Automatically added
    :type record_id2: str

    """
    return web.Response(status=200)


async def dns_domain_name_records_record_id_get(request: web.Request, domain_name, record_id, domain_name2, record_id2) -> web.Response:
    """Get specific record

    

    :param domain_name: The domain name.
    :type domain_name: str
    :param record_id: The id of the record.
    :type record_id: str
    :param domain_name2: Automatically added
    :type domain_name2: str
    :param record_id2: Automatically added
    :type record_id2: str

    """
    return web.Response(status=200)


async def dns_domain_name_records_record_id_put(request: web.Request, domain_name, record_id, domain_name2, record_id2, body=None) -> web.Response:
    """Edit a record

    

    :param domain_name: The domain name.
    :type domain_name: str
    :param record_id: The id of the record.
    :type record_id: str
    :param domain_name2: Automatically added
    :type domain_name2: str
    :param record_id2: Automatically added
    :type record_id2: str
    :param body: The record with updated values.
    :type body: dict | bytes

    """
    body = DnsRecord.from_dict(body)
    return web.Response(status=200)
