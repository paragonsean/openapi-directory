from typing import List, Dict
from aiohttp import web

from openapi_server.models.audit import Audit
from openapi_server.models.extension import Extension
from openapi_server.models.log import Log
from openapi_server.models.post_log import PostLog
from openapi_server.models.post_site import PostSite
from openapi_server.models.site import Site
from openapi_server.models.tag import Tag
from openapi_server import util


async def add_site_to_backup_queue(request: web.Request, id) -> web.Response:
    """Add the site to the backup queue

    Add the site to the backup queue

    :param id: ID of the website
    :type id: int

    """
    return web.Response(status=200)


async def create_audits(request: web.Request, id) -> web.Response:
    """Create an audit for the site

    Create an audit for the site

    :param id: ID of the website
    :type id: int

    """
    return web.Response(status=200)


async def create_log(request: web.Request, id, body) -> web.Response:
    """Create a custom log for a specific website

    Create a custom log for a specific website

    :param id: ID of the website
    :type id: int
    :param body: JSON object Log (only type custom)
    :type body: dict | bytes

    """
    body = PostLog.from_dict(body)
    return web.Response(status=200)


async def create_site(request: web.Request, body) -> web.Response:
    """Create a site

    Create a site

    :param body: JSON object Site
    :type body: dict | bytes

    """
    body = PostSite.from_dict(body)
    return web.Response(status=200)


async def delete_monitor(request: web.Request, id) -> web.Response:
    """Delete uptime monitor

    Return boolean

    :param id: ID of the website
    :type id: int

    """
    return web.Response(status=200)


async def get_backup_profiles(request: web.Request, id) -> web.Response:
    """Return backup profile

    Return backup profile

    :param id: ID of the website
    :type id: int

    """
    return web.Response(status=200)


async def get_list_backups(request: web.Request, id) -> web.Response:
    """List of latest backups

    List of latest backups

    :param id: ID of the website
    :type id: int

    """
    return web.Response(status=200)


async def get_site_audits(request: web.Request, id, fields=None, limit=None, limitstart=None, order=None) -> web.Response:
    """Return audits for a specific website

    Return audits for a specific website

    :param id: ID of the website
    :type id: int
    :param fields: Fields to return separate by comas: name,id
    :type fields: str
    :param limit: Number of object to return (max 100, default 25)
    :type limit: int
    :param limitstart: Start of the return (default 0)
    :type limitstart: int
    :param order: ORDER by this field
    :type order: str

    """
    return web.Response(status=200)


async def get_site_by_id(request: web.Request, id, fields=None) -> web.Response:
    """Find sites by ID

    Return a site based on ID

    :param id: ID that needs to be fetched
    :type id: int
    :param fields: Fields to return separate by comas: name,id
    :type fields: str

    """
    return web.Response(status=200)


async def get_sites(request: web.Request, siteids=None, name=None, access_url=None, j_version=None, ip=None, j_update=None, can_update=None, published=None, error=None, nb_updates=None, up=None, fields=None, limit=None, limitstart=None, order=None) -> web.Response:
    """Get a list of Sites

    Returns a list of Sites

    :param siteids: List of sites id separated by comma
    :type siteids: str
    :param name: Site name. Do a &#39;LIKE&#39; search, you can also use &#39;%&#39;
    :type name: str
    :param access_url: Access URL. Do a &#39;LIKE&#39; search, you can also use &#39;%&#39;
    :type access_url: str
    :param j_version: Joomla version. Do a &#39;LIKE&#39; search, you can also use &#39;%&#39;
    :type j_version: str
    :param ip: Ip address. Do a &#39;LIKE&#39; search, you can also use &#39;%&#39;
    :type ip: str
    :param j_update: Joomla core update status (1: update required, 0: update not required)
    :type j_update: int
    :param can_update: canUpdate
    :type can_update: int
    :param published: Is published
    :type published: int
    :param error: Has errors
    :type error: str
    :param nb_updates: 
    :type nb_updates: str
    :param up: Is online
    :type up: int
    :param fields: Fields to return separated by commas (e.g. name,id)
    :type fields: str
    :param limit: Number of objects to return (max 100, default 25)
    :type limit: int
    :param limitstart: Start of the return (default 0)
    :type limitstart: int
    :param order: ORDER by this field separete by comas. Add + / - after field for set ASC / DESC: type+,name-
    :type order: str

    """
    return web.Response(status=200)


async def get_uptime(request: web.Request, id) -> web.Response:
    """Return uptime data

    Return uptime data

    :param id: ID of the website
    :type id: int

    """
    return web.Response(status=200)


async def install_extension(request: web.Request, id, url) -> web.Response:
    """Install extension

    

    :param id: ID of the website
    :type id: int
    :param url: URL to install the extension from
    :type url: str

    """
    return web.Response(status=200)


async def post_monitor(request: web.Request, id) -> web.Response:
    """Post uptime monitor

    Return boolean

    :param id: ID of the website
    :type id: int

    """
    return web.Response(status=200)


async def post_tags(request: web.Request, id, body) -> web.Response:
    """Add tags for a specific website

    Add tags for a specific website

    :param id: ID of the website
    :type id: int
    :param body: JSON object Tag
    :type body: dict | bytes

    """
    body = Tag.from_dict(body)
    return web.Response(status=200)


async def scanner(request: web.Request, id) -> web.Response:
    """Scan the site for malware

    Scan the site for malware

    :param id: ID of the website
    :type id: int

    """
    return web.Response(status=200)


async def seo_analyze(request: web.Request, id) -> web.Response:
    """SEO analyze for a page

    SEO analyze for a page

    :param id: ID of the website
    :type id: int

    """
    return web.Response(status=200)


async def sites_id_delete(request: web.Request, id) -> web.Response:
    """Delete a specific Site

    Delete a specific Site

    :param id: ID of Site that needs to be deleted
    :type id: int

    """
    return web.Response(status=200)


async def sites_id_extensions_get(request: web.Request, id, fields=None, limit=None, limitstart=None, order=None) -> web.Response:
    """Get extensions for a site

    Get extensions for a site

    :param id: ID of the website
    :type id: int
    :param fields: Fields to return separate by comas: name,id
    :type fields: str
    :param limit: Number of object to return (max 100, default 25)
    :type limit: int
    :param limitstart: Start of the return (default 0)
    :type limitstart: int
    :param order: ORDER by this field
    :type order: str

    """
    return web.Response(status=200)


async def sites_id_logs_get(request: web.Request, id, log_entry=None, log_type=None, _from=None, to=None, fields=None, limit=None, limitstart=None, order=None) -> web.Response:
    """Return logs for a specific website

    Return logs for a specific website

    :param id: ID of the website
    :type id: int
    :param log_entry: Do a &#39;LIKE&#39; search, you can also use &#39;%&#39;
    :type log_entry: str
    :param log_type: Type of the log
    :type log_type: str
    :param _from: Logs after this date, format YYYY-MM-DD HH:MM:SS
    :type _from: str
    :param to: Logs before this date, format YYYY-MM-DD HH:MM:SS
    :type to: str
    :param fields: Fields to return separate by comas: name,id
    :type fields: str
    :param limit: Number of object to return (max 100, default 25)
    :type limit: int
    :param limitstart: Start of the return (default 0)
    :type limitstart: int
    :param order: ORDER by this field separete by comas. Add + / - after field for set ASC / DESC: type+,name-
    :type order: str

    """
    return web.Response(status=200)


async def sites_id_put(request: web.Request, id, body) -> web.Response:
    """Update a site

    Update a site

    :param id: ID of the website that needs to be update
    :type id: int
    :param body: JSON object Site
    :type body: dict | bytes

    """
    body = PostSite.from_dict(body)
    return web.Response(status=200)


async def sites_id_tags_get(request: web.Request, id, name=None, type=None, fields=None, limit=None, limitstart=None, order=None) -> web.Response:
    """Return tags for a specific website

    Return tags for a specific website

    :param id: ID of the website
    :type id: int
    :param name: Do a &#39;LIKE&#39; search, you can also use &#39;%&#39;
    :type name: str
    :param type: Bootstrap color of the tag
    :type type: str
    :param fields: Fields to return separate by comas: name,id
    :type fields: str
    :param limit: Number of object to return (max 100, default 25)
    :type limit: int
    :param limitstart: Start of the return (default 0)
    :type limitstart: int
    :param order: ORDER by this field
    :type order: str

    """
    return web.Response(status=200)


async def sites_metadata_get(request: web.Request, ) -> web.Response:
    """Get the list of fields

    Returns a list of fields


    """
    return web.Response(status=200)


async def start_site_backup(request: web.Request, id) -> web.Response:
    """Start a remote backup for the site

    Start a remote backup for the site

    :param id: ID of the website
    :type id: int

    """
    return web.Response(status=200)


async def step_site_backup(request: web.Request, id) -> web.Response:
    """Step (continue) a remote backup for the site

    Step (continue) a remote backup for the site

    :param id: ID of the website
    :type id: int

    """
    return web.Response(status=200)


async def update_joomla(request: web.Request, id) -> web.Response:
    """Update Joomla core on the remote site

    Update Joomla core on the remote site

    :param id: ID of the website
    :type id: int

    """
    return web.Response(status=200)


async def validate_debug_site(request: web.Request, id) -> web.Response:
    """validate the site, return the debug information

    

    :param id: ID of the website
    :type id: int

    """
    return web.Response(status=200)


async def validate_site(request: web.Request, id) -> web.Response:
    """validate the site, return the new logs

    validate the site

    :param id: ID of the website
    :type id: int

    """
    return web.Response(status=200)
