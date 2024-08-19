from typing import List, Dict
from aiohttp import web

from openapi_server.models.basic_error import BasicError
from openapi_server.models.license import License
from openapi_server.models.license_content import LicenseContent
from openapi_server.models.license_simple import LicenseSimple
from openapi_server import util


async def licenses_get(request: web.Request, license) -> web.Response:
    """Get a license

    

    :param license: 
    :type license: str

    """
    return web.Response(status=200)


async def licenses_get_all_commonly_used(request: web.Request, featured=None, per_page=None, page=None) -> web.Response:
    """Get all commonly used licenses

    

    :param featured: 
    :type featured: bool
    :param per_page: Results per page (max 100)
    :type per_page: int
    :param page: Page number of the results to fetch.
    :type page: int

    """
    return web.Response(status=200)


async def licenses_get_for_repo(request: web.Request, owner, repo) -> web.Response:
    """Get the license for a repository

    This method returns the contents of the repository&#39;s license file, if one is detected.  Similar to [Get repository content](https://docs.github.com/enterprise-server@2.22/rest/reference/repos#get-repository-content), this method also supports [custom media types](https://docs.github.com/enterprise-server@2.22/rest/overview/media-types) for retrieving the raw license content or rendered license HTML.

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str

    """
    return web.Response(status=200)
