from typing import List, Dict
from aiohttp import web

from openapi_server.models.new_project_member import NewProjectMember
from openapi_server.models.project_member_details import ProjectMemberDetails
from openapi_server.models.project_member_list import ProjectMemberList
from openapi_server.models.update_project_member import UpdateProjectMember
from openapi_server import util


async def project_member_get(request: web.Request, project_id=None, user_id=None) -> web.Response:
    """Gets list of Project Members

    Include at least one of ProjectID or UserID parameters.

    :param project_id: Get Project members filtered by ProjectID
    :type project_id: int
    :param user_id: Get Project members filtered by UserID
    :type user_id: int

    """
    return web.Response(status=200)


async def project_member_post(request: web.Request, model) -> web.Response:
    """Assign a user as a Member of a Project

    the Amount columns for Cost, Budget, Rates should be specified as a decimal. Financial amounts assume the currency of the Customer company. Budget units depend on the Budget method set on the Project.

    :param model: 
    :type model: dict | bytes

    """
    model = NewProjectMember.from_dict(model)
    return web.Response(status=200)


async def project_member_put(request: web.Request, model) -> web.Response:
    """Update a Member of a Project

    Fields are only updated if their field name is in the FieldsToUpdate string collection. The Amount columns for Cost, Budget, Rates if specified should be a decimal. Financial amounts assume the currency of the parent Company. Budget units depend on the Budget method set on the Project.

    :param model: 
    :type model: dict | bytes

    """
    model = UpdateProjectMember.from_dict(model)
    return web.Response(status=200)
