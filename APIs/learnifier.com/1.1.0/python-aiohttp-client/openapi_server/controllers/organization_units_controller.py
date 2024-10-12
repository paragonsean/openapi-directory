from typing import List, Dict
from aiohttp import web

from openapi_server.models.add_organization_unit import AddOrganizationUnit
from openapi_server.models.add_organization_unit_response import AddOrganizationUnitResponse
from openapi_server.models.error import Error
from openapi_server.models.org_unit import OrgUnit
from openapi_server.models.org_units import OrgUnits
from openapi_server.models.update_organization_unit import UpdateOrganizationUnit
from openapi_server import util


async def extorgunit_get(request: web.Request, extid) -> web.Response:
    """Get Organization Unit with External Id

    Returns information about the organization unit with the specified external id. 

    :param extid: The external id of the organization unit
    :type extid: str

    """
    return web.Response(status=200)


async def orgunits_get(request: web.Request, ) -> web.Response:
    """Organization Units

    The orgunits endpoint returns information about the available organization units (orgunits). The response includes the display name, internal and external id and client number. 


    """
    return web.Response(status=200)


async def orgunits_orgid_get(request: web.Request, orgid) -> web.Response:
    """Get Organization Unit

    Returns information about the specified organization unit. The response includes the display name, internal and external id and client number. 

    :param orgid: Id of the organization unit
    :type orgid: int

    """
    return web.Response(status=200)


async def orgunits_orgid_patch(request: web.Request, orgid, body) -> web.Response:
    """Updates an Organization Unit

    Adds an Organization Unit

    :param orgid: 
    :type orgid: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateOrganizationUnit.from_dict(body)
    return web.Response(status=200)


async def orgunits_post(request: web.Request, body) -> web.Response:
    """Adds an Organization Unit

    Adds an Organization Unit

    :param body: 
    :type body: dict | bytes

    """
    body = AddOrganizationUnit.from_dict(body)
    return web.Response(status=200)
