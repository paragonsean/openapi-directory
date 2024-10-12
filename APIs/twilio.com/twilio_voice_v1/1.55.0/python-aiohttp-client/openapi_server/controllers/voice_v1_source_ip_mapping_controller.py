from typing import List, Dict
from aiohttp import web

from openapi_server.models.list_source_ip_mapping_response import ListSourceIpMappingResponse
from openapi_server.models.voice_v1_source_ip_mapping import VoiceV1SourceIpMapping
from openapi_server import util


async def create_source_ip_mapping(request: web.Request, ip_record_sid, sip_domain_sid) -> web.Response:
    """create_source_ip_mapping

    

    :param ip_record_sid: The Twilio-provided string that uniquely identifies the IP Record resource to map from.
    :type ip_record_sid: str
    :param sip_domain_sid: The SID of the SIP Domain that the IP Record should be mapped to.
    :type sip_domain_sid: str

    """
    return web.Response(status=200)


async def delete_source_ip_mapping(request: web.Request, sid) -> web.Response:
    """delete_source_ip_mapping

    

    :param sid: The Twilio-provided string that uniquely identifies the IP Record resource to delete.
    :type sid: str

    """
    return web.Response(status=200)


async def fetch_source_ip_mapping(request: web.Request, sid) -> web.Response:
    """fetch_source_ip_mapping

    

    :param sid: The Twilio-provided string that uniquely identifies the IP Record resource to fetch.
    :type sid: str

    """
    return web.Response(status=200)


async def list_source_ip_mapping(request: web.Request, page_size=None, page=None, page_token=None) -> web.Response:
    """list_source_ip_mapping

    

    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)


async def update_source_ip_mapping(request: web.Request, sid, sip_domain_sid) -> web.Response:
    """update_source_ip_mapping

    

    :param sid: The Twilio-provided string that uniquely identifies the IP Record resource to update.
    :type sid: str
    :param sip_domain_sid: The SID of the SIP Domain that the IP Record should be mapped to.
    :type sip_domain_sid: str

    """
    return web.Response(status=200)
