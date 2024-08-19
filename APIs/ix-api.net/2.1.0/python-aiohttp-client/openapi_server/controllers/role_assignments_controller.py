from typing import List, Dict
from aiohttp import web

from openapi_server.models.accounts_list400_response import AccountsList400Response
from openapi_server.models.accounts_list401_response import AccountsList401Response
from openapi_server.models.accounts_list403_response import AccountsList403Response
from openapi_server.models.accounts_read404_response import AccountsRead404Response
from openapi_server.models.contacts_destroy400_response import ContactsDestroy400Response
from openapi_server.models.role_assignment import RoleAssignment
from openapi_server.models.role_assignment_request import RoleAssignmentRequest
from openapi_server.models.role_assignments_create400_response import RoleAssignmentsCreate400Response
from openapi_server import util


async def role_assignments_create(request: web.Request, body=None) -> web.Response:
    """role_assignments_create

    Assign a &#x60;Role&#x60; to a &#x60;Contact&#x60;.  The contact needs to have all fields filled, which the role requires. If this is not the case a &#x60;400&#x60; &#x60;UnableToFulfill&#x60; will be returned.

    :param body: A role assignment request
    :type body: dict | bytes

    """
    body = RoleAssignmentRequest.from_dict(body)
    return web.Response(status=200)


async def role_assignments_destroy(request: web.Request, assignment_id) -> web.Response:
    """role_assignments_destroy

    Remove a role assignment from a contact.  If the contact is still in use with a given role required, this will yield an &#x60;UnableToFulfill&#x60; error.

    :param assignment_id: Get by assignment_id
    :type assignment_id: str

    """
    return web.Response(status=200)


async def role_assignments_list(request: web.Request, id=None, contact=None, role=None) -> web.Response:
    """role_assignments_list

    List all role assignments for a contact.

    :param id: Filter by id
    :type id: List[str]
    :param contact: Filter by contact
    :type contact: str
    :param role: Filter by role
    :type role: str

    """
    return web.Response(status=200)


async def role_assignments_read(request: web.Request, assignment_id) -> web.Response:
    """role_assignments_read

    Get a role assignment for a contact.

    :param assignment_id: Get by assignment_id
    :type assignment_id: str

    """
    return web.Response(status=200)
