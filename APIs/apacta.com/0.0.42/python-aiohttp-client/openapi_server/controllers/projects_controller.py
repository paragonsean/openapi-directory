from typing import List, Dict
from aiohttp import web

from openapi_server.models.clocking_records_clocking_record_id_delete200_response import ClockingRecordsClockingRecordIdDelete200Response
from openapi_server.models.clocking_records_clocking_record_id_put200_response import ClockingRecordsClockingRecordIdPut200Response
from openapi_server.models.clocking_records_post201_response import ClockingRecordsPost201Response
from openapi_server.models.empty_success_response import EmptySuccessResponse
from openapi_server.models.error_not_found import ErrorNotFound
from openapi_server.models.error_validation import ErrorValidation
from openapi_server.models.expense_files_expense_file_id_put200_response import ExpenseFilesExpenseFileIdPut200Response
from openapi_server.models.projects_get200_response import ProjectsGet200Response
from openapi_server.models.projects_has_projects_with_custom_statuses_get200_response import ProjectsHasProjectsWithCustomStatusesGet200Response
from openapi_server.models.projects_post_request import ProjectsPostRequest
from openapi_server.models.projects_project_id_all_files_get200_response import ProjectsProjectIdAllFilesGet200Response
from openapi_server.models.projects_project_id_get200_response import ProjectsProjectIdGet200Response
from openapi_server.models.projects_project_id_put_request import ProjectsProjectIdPutRequest
from openapi_server.models.projects_project_id_send_bulk_pdf_post_request import ProjectsProjectIdSendBulkPdfPostRequest
from openapi_server.models.projects_project_id_users_get200_response import ProjectsProjectIdUsersGet200Response
from openapi_server.models.projects_project_id_users_post_request import ProjectsProjectIdUsersPostRequest
from openapi_server.models.projects_project_id_users_user_id_get200_response import ProjectsProjectIdUsersUserIdGet200Response
from openapi_server import util


async def projects_get(request: web.Request, show_all=None, sort=None, direction=None, contact_id=None, company_id=None, project_status_id=None, project_status_ids=None, name=None, erp_project_id=None, erp_task_id=None, start_time_gte=None, start_time_lte=None, start_time_eq=None, event_start_gt=None, event_start_lt=None, event_start_eq=None, event_end_gt=None, event_end_lt=None, event_end_eq=None) -> web.Response:
    """View list of projects

    

    :param show_all: Unless this is set to &#x60;true&#x60; only open projects will be shown
    :type show_all: bool
    :param sort: Sort projects by &#x60;not_invoiced_amount&#x60;
    :type sort: str
    :param direction: 
    :type direction: str
    :param contact_id: Used to filter on the &#x60;contact_id&#x60; of the projects
    :type contact_id: str
    :type contact_id: str
    :param company_id: Used to filter on the &#x60;company_id&#x60; of the projects
    :type company_id: str
    :type company_id: str
    :param project_status_id: Used to filter on the &#x60;project_status_id&#x60; of the projects
    :type project_status_id: str
    :type project_status_id: str
    :param project_status_ids: Used to filter on the &#x60;project_status_id&#x60; of the projects (match any of the provided values)
    :type project_status_ids: List[str]
    :param name: Used to search on the &#x60;name&#x60; of the projects
    :type name: str
    :param erp_project_id: Used to search on the &#x60;erp_project_id&#x60; of the projects
    :type erp_project_id: str
    :param erp_task_id: Used to search on the &#x60;erp_task_id&#x60; of the projects
    :type erp_task_id: str
    :param start_time_gte: Show projects with start time after than this value
    :type start_time_gte: str
    :param start_time_lte: Show projects with start time before this value
    :type start_time_lte: str
    :param start_time_eq: Show only projects with start time on specific date
    :type start_time_eq: str
    :param event_start_gt: 
    :type event_start_gt: str
    :param event_start_lt: 
    :type event_start_lt: str
    :param event_start_eq: 
    :type event_start_eq: str
    :param event_end_gt: 
    :type event_end_gt: str
    :param event_end_lt: 
    :type event_end_lt: str
    :param event_end_eq: 
    :type event_end_eq: str

    """
    return web.Response(status=200)


async def projects_has_projects_with_custom_statuses_get_0(request: web.Request, ) -> web.Response:
    """Check if the company has projects with custom statuses

    


    """
    return web.Response(status=200)


async def projects_post(request: web.Request, body=None) -> web.Response:
    """Add a project

    

    :param body: 
    :type body: dict | bytes

    """
    body = ProjectsPostRequest.from_dict(body)
    return web.Response(status=200)


async def projects_project_id_all_files_get(request: web.Request, project_id) -> web.Response:
    """Show list of all files uploaded to project

    Used to show files uploaded to a project from form, expense and project

    :param project_id: 
    :type project_id: str

    """
    return web.Response(status=200)


async def projects_project_id_delete(request: web.Request, project_id) -> web.Response:
    """Delete a project

    

    :param project_id: 
    :type project_id: str

    """
    return web.Response(status=200)


async def projects_project_id_files_file_id_delete(request: web.Request, project_id, file_id) -> web.Response:
    """Delete file

    Delete file uploaded to a project from wall post or form

    :param project_id: 
    :type project_id: str
    :type project_id: str
    :param file_id: 
    :type file_id: str
    :type file_id: str

    """
    return web.Response(status=200)


async def projects_project_id_files_file_id_get(request: web.Request, project_id, file_id) -> web.Response:
    """Show file

    Show file uploaded to a project from wall post or form

    :param project_id: 
    :type project_id: str
    :param file_id: 
    :type file_id: str

    """
    return web.Response(status=200)


async def projects_project_id_files_file_id_put(request: web.Request, project_id, file_id) -> web.Response:
    """Edit file

    Edit file uploaded to a project from wall post or form

    :param project_id: 
    :type project_id: str
    :type project_id: str
    :param file_id: 
    :type file_id: str
    :type file_id: str

    """
    return web.Response(status=200)


async def projects_project_id_files_get(request: web.Request, project_id) -> web.Response:
    """Show list of files uploaded to project

    Used to show files uploaded to a project from wall post or form

    :param project_id: 
    :type project_id: str

    """
    return web.Response(status=200)


async def projects_project_id_get(request: web.Request, project_id) -> web.Response:
    """View specific project

    

    :param project_id: 
    :type project_id: str

    """
    return web.Response(status=200)


async def projects_project_id_project_files_get(request: web.Request, project_id) -> web.Response:
    """Show list of project files uploaded to project

    Returns files belonging to the project, not uploaded from wall post or form

    :param project_id: 
    :type project_id: str

    """
    return web.Response(status=200)


async def projects_project_id_project_files_post(request: web.Request, project_id, file) -> web.Response:
    """Add project file to projects

    

    :param project_id: 
    :type project_id: str
    :param file: 
    :type file: str

    """
    return web.Response(status=200)


async def projects_project_id_project_files_project_file_id_delete(request: web.Request, project_file_id, project_id) -> web.Response:
    """Delete project file

    

    :param project_file_id: 
    :type project_file_id: str
    :type project_file_id: str
    :param project_id: 
    :type project_id: str
    :type project_id: str

    """
    return web.Response(status=200)


async def projects_project_id_project_files_project_file_id_get(request: web.Request, project_id, project_file_id) -> web.Response:
    """Show project file

    

    :param project_id: 
    :type project_id: str
    :param project_file_id: 
    :type project_file_id: str

    """
    return web.Response(status=200)


async def projects_project_id_project_files_project_file_id_put(request: web.Request, project_id, project_file_id) -> web.Response:
    """Edit project file

    

    :param project_id: 
    :type project_id: str
    :type project_id: str
    :param project_file_id: 
    :type project_file_id: str
    :type project_file_id: str

    """
    return web.Response(status=200)


async def projects_project_id_put(request: web.Request, project_id, body=None) -> web.Response:
    """Edit a project

    

    :param project_id: 
    :type project_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = ProjectsProjectIdPutRequest.from_dict(body)
    return web.Response(status=200)


async def projects_project_id_send_bulk_pdf_post(request: web.Request, project_id, body) -> web.Response:
    """Send bulk forms pdf by email

    

    :param project_id: 
    :type project_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = ProjectsProjectIdSendBulkPdfPostRequest.from_dict(body)
    return web.Response(status=200)


async def projects_project_id_users_get(request: web.Request, project_id) -> web.Response:
    """Show list of users added to project

    

    :param project_id: 
    :type project_id: str

    """
    return web.Response(status=200)


async def projects_project_id_users_post(request: web.Request, project_id, body=None) -> web.Response:
    """Add user to project

    

    :param project_id: 
    :type project_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = ProjectsProjectIdUsersPostRequest.from_dict(body)
    return web.Response(status=200)


async def projects_project_id_users_user_id_delete(request: web.Request, user_id, project_id) -> web.Response:
    """Delete user from project

    

    :param user_id: 
    :type user_id: str
    :param project_id: 
    :type project_id: str

    """
    return web.Response(status=200)


async def projects_project_id_users_user_id_get(request: web.Request, user_id, project_id) -> web.Response:
    """View specific user assigned to project

    

    :param user_id: 
    :type user_id: str
    :param project_id: 
    :type project_id: str

    """
    return web.Response(status=200)
