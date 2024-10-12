from typing import List, Dict
from aiohttp import web

from openapi_server.models.get_organization_licensing_coterm_licenses200_response_inner import GetOrganizationLicensingCotermLicenses200ResponseInner
from openapi_server.models.move_organization_licensing_coterm_licenses200_response import MoveOrganizationLicensingCotermLicenses200Response
from openapi_server.models.move_organization_licensing_coterm_licenses_request import MoveOrganizationLicensingCotermLicensesRequest
from openapi_server import util


async def get_organization_licensing_coterm_licenses(request: web.Request, organization_id, per_page=None, starting_after=None, ending_before=None, invalidated=None, expired=None) -> web.Response:
    """List the licenses in a coterm organization

    List the licenses in a coterm organization

    :param organization_id: 
    :type organization_id: str
    :param per_page: The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
    :type per_page: int
    :param starting_after: A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type starting_after: str
    :param ending_before: A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type ending_before: str
    :param invalidated: Filter for licenses that are invalidated
    :type invalidated: bool
    :param expired: Filter for licenses that are expired
    :type expired: bool

    """
    return web.Response(status=200)


async def move_organization_licensing_coterm_licenses(request: web.Request, organization_id, body) -> web.Response:
    """Moves a license to a different organization (coterm only)

    Moves a license to a different organization (coterm only)

    :param organization_id: 
    :type organization_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = MoveOrganizationLicensingCotermLicensesRequest.from_dict(body)
    return web.Response(status=200)
