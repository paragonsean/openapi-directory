from typing import List, Dict
from aiohttp import web

from openapi_server.models.assign_organization_licenses_seats200_response import AssignOrganizationLicensesSeats200Response
from openapi_server.models.assign_organization_licenses_seats_request import AssignOrganizationLicensesSeatsRequest
from openapi_server.models.get_organization_licenses200_response_inner import GetOrganizationLicenses200ResponseInner
from openapi_server.models.get_organization_licensing_coterm_licenses200_response_inner import GetOrganizationLicensingCotermLicenses200ResponseInner
from openapi_server.models.move_organization_licenses200_response import MoveOrganizationLicenses200Response
from openapi_server.models.move_organization_licenses_request import MoveOrganizationLicensesRequest
from openapi_server.models.move_organization_licenses_seats200_response import MoveOrganizationLicensesSeats200Response
from openapi_server.models.move_organization_licenses_seats_request import MoveOrganizationLicensesSeatsRequest
from openapi_server.models.move_organization_licensing_coterm_licenses200_response import MoveOrganizationLicensingCotermLicenses200Response
from openapi_server.models.move_organization_licensing_coterm_licenses_request import MoveOrganizationLicensingCotermLicensesRequest
from openapi_server.models.renew_organization_licenses_seats_request import RenewOrganizationLicensesSeatsRequest
from openapi_server.models.update_organization_license_request import UpdateOrganizationLicenseRequest
from openapi_server import util


async def assign_organization_licenses_seats_1(request: web.Request, organization_id, body) -> web.Response:
    """Assign SM seats to a network

    Assign SM seats to a network. This will increase the managed SM device limit of the network

    :param organization_id: 
    :type organization_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = AssignOrganizationLicensesSeatsRequest.from_dict(body)
    return web.Response(status=200)


async def get_organization_license_1(request: web.Request, organization_id, license_id) -> web.Response:
    """Display a license

    Display a license

    :param organization_id: 
    :type organization_id: str
    :param license_id: 
    :type license_id: str

    """
    return web.Response(status=200)


async def get_organization_licenses_1(request: web.Request, organization_id, per_page=None, starting_after=None, ending_before=None, device_serial=None, network_id=None, state=None) -> web.Response:
    """List the licenses for an organization

    List the licenses for an organization

    :param organization_id: 
    :type organization_id: str
    :param per_page: The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
    :type per_page: int
    :param starting_after: A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type starting_after: str
    :param ending_before: A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type ending_before: str
    :param device_serial: Filter the licenses to those assigned to a particular device. Returned in the same order that they are queued to the device.
    :type device_serial: str
    :param network_id: Filter the licenses to those assigned in a particular network
    :type network_id: str
    :param state: Filter the licenses to those in a particular state. Can be one of &#39;active&#39;, &#39;expired&#39;, &#39;expiring&#39;, &#39;recentlyQueued&#39;, &#39;unused&#39; or &#39;unusedActive&#39;
    :type state: str

    """
    return web.Response(status=200)


async def get_organization_licenses_overview_1(request: web.Request, organization_id) -> web.Response:
    """Return an overview of the license state for an organization

    Return an overview of the license state for an organization

    :param organization_id: 
    :type organization_id: str

    """
    return web.Response(status=200)


async def get_organization_licensing_coterm_licenses_2(request: web.Request, organization_id, per_page=None, starting_after=None, ending_before=None, invalidated=None, expired=None) -> web.Response:
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


async def move_organization_licenses_1(request: web.Request, organization_id, body) -> web.Response:
    """Move licenses to another organization

    Move licenses to another organization. This will also move any devices that the licenses are assigned to

    :param organization_id: 
    :type organization_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = MoveOrganizationLicensesRequest.from_dict(body)
    return web.Response(status=200)


async def move_organization_licenses_seats_1(request: web.Request, organization_id, body) -> web.Response:
    """Move SM seats to another organization

    Move SM seats to another organization

    :param organization_id: 
    :type organization_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = MoveOrganizationLicensesSeatsRequest.from_dict(body)
    return web.Response(status=200)


async def move_organization_licensing_coterm_licenses_2(request: web.Request, organization_id, body) -> web.Response:
    """Moves a license to a different organization (coterm only)

    Moves a license to a different organization (coterm only)

    :param organization_id: 
    :type organization_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = MoveOrganizationLicensingCotermLicensesRequest.from_dict(body)
    return web.Response(status=200)


async def renew_organization_licenses_seats_1(request: web.Request, organization_id, body) -> web.Response:
    """Renew SM seats of a license

    Renew SM seats of a license. This will extend the license expiration date of managed SM devices covered by this license

    :param organization_id: 
    :type organization_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = RenewOrganizationLicensesSeatsRequest.from_dict(body)
    return web.Response(status=200)


async def update_organization_license_1(request: web.Request, organization_id, license_id, body=None) -> web.Response:
    """Update a license

    Update a license

    :param organization_id: 
    :type organization_id: str
    :param license_id: 
    :type license_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateOrganizationLicenseRequest.from_dict(body)
    return web.Response(status=200)
