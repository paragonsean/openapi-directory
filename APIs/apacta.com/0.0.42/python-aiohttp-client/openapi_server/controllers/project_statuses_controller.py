from typing import List, Dict
from aiohttp import web

from openapi_server.models.bad_request_response import BadRequestResponse
from openapi_server.models.bulk_action_request_body import BulkActionRequestBody
from openapi_server.models.create_success_response import CreateSuccessResponse
from openapi_server.models.empty_success_response import EmptySuccessResponse
from openapi_server.models.error_not_found import ErrorNotFound
from openapi_server.models.error_validation import ErrorValidation
from openapi_server.models.forbidden_error import ForbiddenError
from openapi_server.models.project_statuses_get200_response import ProjectStatusesGet200Response
from openapi_server.models.project_statuses_post_request import ProjectStatusesPostRequest
from openapi_server.models.project_statuses_project_status_id_get200_response import ProjectStatusesProjectStatusIdGet200Response
from openapi_server.models.projects_has_projects_with_custom_statuses_get200_response import ProjectsHasProjectsWithCustomStatusesGet200Response
from openapi_server import util


async def project_statuses_bulk_delete_delete(request: web.Request, body) -> web.Response:
    """Bulk delete project statuses

    

    :param body: Project statuses ids
    :type body: dict | bytes

    """
    body = BulkActionRequestBody.from_dict(body)
    return web.Response(status=200)


async def project_statuses_get(request: web.Request, ) -> web.Response:
    """Get list of project statuses

    


    """
    return web.Response(status=200)


async def project_statuses_post(request: web.Request, body) -> web.Response:
    """Create a new project status

    

    :param body: 
    :type body: dict | bytes

    """
    body = ProjectStatusesPostRequest.from_dict(body)
    return web.Response(status=200)


async def project_statuses_project_status_id_delete(request: web.Request, project_status_id) -> web.Response:
    """Delete a project status

    

    :param project_status_id: 
    :type project_status_id: str
    :type project_status_id: str

    """
    return web.Response(status=200)


async def project_statuses_project_status_id_get(request: web.Request, project_status_id) -> web.Response:
    """Get a single project status

    

    :param project_status_id: 
    :type project_status_id: str

    """
    return web.Response(status=200)


async def project_statuses_project_status_id_put(request: web.Request, project_status_id) -> web.Response:
    """Edit a project status

    

    :param project_status_id: 
    :type project_status_id: str

    """
    return web.Response(status=200)


async def projects_has_projects_with_custom_statuses_get(request: web.Request, ) -> web.Response:
    """Check if the company has projects with custom statuses

    


    """
    return web.Response(status=200)
