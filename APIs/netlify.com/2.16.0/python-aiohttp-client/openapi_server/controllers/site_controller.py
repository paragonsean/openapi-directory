from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.site import Site
from openapi_server.models.site_setup import SiteSetup
from openapi_server import util


async def create_site(request: web.Request, site, configure_dns=None) -> web.Response:
    """create_site

    **Note:** Environment variable keys and values will soon be moved from &#x60;build_settings.env&#x60; and &#x60;repo.env&#x60; to a new endpoint. Please use [createEnvVars](#tag/environmentVariables/operation/createEnvVars) to create environment variables for a site.

    :param site: 
    :type site: dict | bytes
    :param configure_dns: 
    :type configure_dns: bool

    """
    site = SiteSetup.from_dict(site)
    return web.Response(status=200)


async def create_site_in_team(request: web.Request, account_slug, configure_dns=None, site=None) -> web.Response:
    """create_site_in_team

    **Note:** Environment variable keys and values will soon be moved from &#x60;build_settings.env&#x60; and &#x60;repo.env&#x60; to a new endpoint. Please use [createEnvVars](#tag/environmentVariables/operation/createEnvVars) to create environment variables for a site.

    :param account_slug: 
    :type account_slug: str
    :param configure_dns: 
    :type configure_dns: bool
    :param site: 
    :type site: dict | bytes

    """
    site = SiteSetup.from_dict(site)
    return web.Response(status=200)


async def delete_site(request: web.Request, site_id) -> web.Response:
    """delete_site

    

    :param site_id: 
    :type site_id: str

    """
    return web.Response(status=200)


async def get_site(request: web.Request, site_id) -> web.Response:
    """get_site

    **Note:** Environment variable keys and values will soon be moved from &#x60;build_settings.env&#x60; and &#x60;repo.env&#x60; to a new endpoint. Please use [getEnvVars](#tag/environmentVariables/operation/getEnvVars) to retrieve site environment variables.

    :param site_id: 
    :type site_id: str

    """
    return web.Response(status=200)


async def list_sites(request: web.Request, name=None, filter=None, page=None, per_page=None) -> web.Response:
    """list_sites

    **Note:** Environment variable keys and values will soon be moved from &#x60;build_settings.env&#x60; and &#x60;repo.env&#x60; to a new endpoint. Please use [getEnvVars](#tag/environmentVariables/operation/getEnvVars) to retrieve site environment variables.

    :param name: 
    :type name: str
    :param filter: 
    :type filter: str
    :param page: 
    :type page: int
    :param per_page: 
    :type per_page: int

    """
    return web.Response(status=200)


async def list_sites_for_account(request: web.Request, account_slug, name=None, page=None, per_page=None) -> web.Response:
    """list_sites_for_account

    **Note:** Environment variable keys and values will soon be moved from &#x60;build_settings.env&#x60; and &#x60;repo.env&#x60; to a new endpoint. Please use [getEnvVars](#tag/environmentVariables/operation/getEnvVars) to retrieve site environment variables.

    :param account_slug: 
    :type account_slug: str
    :param name: 
    :type name: str
    :param page: 
    :type page: int
    :param per_page: 
    :type per_page: int

    """
    return web.Response(status=200)


async def unlink_site_repo(request: web.Request, site_id) -> web.Response:
    """unlink_site_repo

    [Beta] Unlinks the repo from the site.  This action will also: - Delete associated deploy keys - Delete outgoing webhooks for the repo - Delete the site&#39;s build hooks

    :param site_id: 
    :type site_id: str

    """
    return web.Response(status=200)


async def update_site(request: web.Request, site_id, site) -> web.Response:
    """update_site

    **Note:** Environment variable keys and values will soon be moved from &#x60;build_settings.env&#x60; and &#x60;repo.env&#x60; to a new endpoint. Please use [updateEnvVar](#tag/environmentVariables/operation/updateEnvVar) to update a site&#39;s environment variables.

    :param site_id: 
    :type site_id: str
    :param site: 
    :type site: dict | bytes

    """
    site = SiteSetup.from_dict(site)
    return web.Response(status=200)
