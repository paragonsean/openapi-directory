from typing import List, Dict
from aiohttp import web

from openapi_server.models.search_results import SearchResults
from openapi_server.models.update_model import UpdateModel
from openapi_server import util


async def domains_tld_zone_id_download_get(request: web.Request, zone_id, api_key=None, _date=None) -> web.Response:
    """Download Whole Dataset for TLD

    

    :param zone_id: 
    :type zone_id: str
    :param api_key: API key
    :type api_key: str
    :param _date: Request date
    :type _date: str

    """
    return web.Response(status=200)


async def domains_tld_zone_id_search_get(request: web.Request, zone_id, api_key=None, _date=None, page=None, limit=None, domain=None, country=None, is_dead=None, a=None, ns=None, cname=None, mx=None, txt=None) -> web.Response:
    """Domains Search for TLD

    

    :param zone_id: 
    :type zone_id: str
    :param api_key: API key
    :type api_key: str
    :param _date: Request date
    :type _date: str
    :param page: Search page to request
    :type page: str
    :param limit: Results per page
    :type limit: int
    :param domain: Domain includes
    :type domain: str
    :param country: Hosting Country
    :type country: str
    :param is_dead: Dead or Not, default not
    :type is_dead: bool
    :param a: A record includes
    :type a: str
    :param ns: NS record includes
    :type ns: str
    :param cname: CNAME record includes
    :type cname: str
    :param mx: MX record includes
    :type mx: str
    :param txt: TXT record includes
    :type txt: str

    """
    return web.Response(status=200)


async def domains_updates_added_download_get(request: web.Request, api_key=None, _date=None) -> web.Response:
    """Download added domains, latest if date not specified

    

    :param api_key: API key
    :type api_key: str
    :param _date: Request date
    :type _date: str

    """
    return web.Response(status=200)


async def domains_updates_added_get(request: web.Request, api_key=None, _date=None, page=None, limit=None) -> web.Response:
    """Get added domains, latest if date not specified

    

    :param api_key: API key
    :type api_key: str
    :param _date: Request date
    :type _date: str
    :param page: Search page to request
    :type page: str
    :param limit: Results per page
    :type limit: int

    """
    return web.Response(status=200)


async def domains_updates_deleted_download_get(request: web.Request, api_key=None, _date=None) -> web.Response:
    """Download deleted domains, latest if date not specified

    

    :param api_key: API key
    :type api_key: str
    :param _date: Request date
    :type _date: str

    """
    return web.Response(status=200)


async def domains_updates_deleted_get(request: web.Request, api_key=None, _date=None, page=None, limit=None) -> web.Response:
    """Get deleted domains, latest if date not specified

    

    :param api_key: API key
    :type api_key: str
    :param _date: Request date
    :type _date: str
    :param page: Search page to request
    :type page: str
    :param limit: Results per page
    :type limit: int

    """
    return web.Response(status=200)


async def domains_updates_list_get(request: web.Request, api_key=None) -> web.Response:
    """List of updates

    

    :param api_key: API key
    :type api_key: str

    """
    return web.Response(status=200)


async def get_search_domain_item(request: web.Request, api_key=None, _date=None, page=None, limit=None, domain=None, zone=None, country=None, is_dead=None, a=None, ns=None, cname=None, mx=None, txt=None) -> web.Response:
    """Domains Database Search

    

    :param api_key: API key
    :type api_key: str
    :param _date: Request date
    :type _date: str
    :param page: Search page to request
    :type page: str
    :param limit: Results per page
    :type limit: int
    :param domain: Domain includes
    :type domain: str
    :param zone: In Zone
    :type zone: str
    :param country: Hosting Country
    :type country: str
    :param is_dead: Dead or Not, default not
    :type is_dead: bool
    :param a: A record includes
    :type a: str
    :param ns: NS record includes
    :type ns: str
    :param cname: CNAME record includes
    :type cname: str
    :param mx: MX record includes
    :type mx: str
    :param txt: TXT record includes
    :type txt: str

    """
    return web.Response(status=200)


async def get_tld_domain_item(request: web.Request, zone_id, api_key=None, _date=None, page=None, limit=None, domain=None, country=None, is_dead=None, a=None, ns=None, cname=None, mx=None, txt=None) -> web.Response:
    """Get TLD records

    

    :param zone_id: 
    :type zone_id: str
    :param api_key: API key
    :type api_key: str
    :param _date: Request date
    :type _date: str
    :param page: Search page to request
    :type page: str
    :param limit: Results per page
    :type limit: int
    :param domain: Domain includes
    :type domain: str
    :param country: Hosting Country
    :type country: str
    :param is_dead: Dead or Not, default not
    :type is_dead: bool
    :param a: A record includes
    :type a: str
    :param ns: NS record includes
    :type ns: str
    :param cname: CNAME record includes
    :type cname: str
    :param mx: MX record includes
    :type mx: str
    :param txt: TXT record includes
    :type txt: str

    """
    return web.Response(status=200)
