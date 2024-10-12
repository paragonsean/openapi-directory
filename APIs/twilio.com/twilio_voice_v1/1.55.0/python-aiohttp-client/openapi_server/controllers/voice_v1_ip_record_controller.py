from typing import List, Dict
from aiohttp import web

from openapi_server.models.list_ip_record_response import ListIpRecordResponse
from openapi_server.models.voice_v1_ip_record import VoiceV1IpRecord
from openapi_server import util


async def create_ip_record(request: web.Request, ip_address, cidr_prefix_length=None, friendly_name=None) -> web.Response:
    """create_ip_record

    

    :param ip_address: An IP address in dotted decimal notation, IPv4 only.
    :type ip_address: str
    :param cidr_prefix_length: An integer representing the length of the [CIDR](https://tools.ietf.org/html/rfc4632) prefix to use with this IP address. By default the entire IP address is used, which for IPv4 is value 32.
    :type cidr_prefix_length: int
    :param friendly_name: A descriptive string that you create to describe the resource. It is not unique and can be up to 255 characters long.
    :type friendly_name: str

    """
    return web.Response(status=200)


async def delete_ip_record(request: web.Request, sid) -> web.Response:
    """delete_ip_record

    

    :param sid: The Twilio-provided string that uniquely identifies the IP Record resource to delete.
    :type sid: str

    """
    return web.Response(status=200)


async def fetch_ip_record(request: web.Request, sid) -> web.Response:
    """fetch_ip_record

    

    :param sid: The Twilio-provided string that uniquely identifies the IP Record resource to fetch.
    :type sid: str

    """
    return web.Response(status=200)


async def list_ip_record(request: web.Request, page_size=None, page=None, page_token=None) -> web.Response:
    """list_ip_record

    

    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)


async def update_ip_record(request: web.Request, sid, friendly_name=None) -> web.Response:
    """update_ip_record

    

    :param sid: The Twilio-provided string that uniquely identifies the IP Record resource to update.
    :type sid: str
    :param friendly_name: A descriptive string that you create to describe the resource. It is not unique and can be up to 255 characters long.
    :type friendly_name: str

    """
    return web.Response(status=200)
