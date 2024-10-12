from typing import List, Dict
from aiohttp import web

from openapi_server.models.assign_project_timesheet_category import AssignProjectTimesheetCategory
from openapi_server.models.project_timesheet_category_details import ProjectTimesheetCategoryDetails
from openapi_server.models.project_timesheet_category_list import ProjectTimesheetCategoryList
from openapi_server import util


async def project_timesheet_category_get(request: web.Request, project_id=None) -> web.Response:
    """Gets list of Project Timesheet Categories

    The default sort order is by isBillable desc, Name asc

    :param project_id: Get categories filtered by ProjectID
    :type project_id: int

    """
    return web.Response(status=200)


async def project_timesheet_category_post(request: web.Request, model) -> web.Response:
    """Assign a TimeSheetCategory to a Project.

    

    :param model: 
    :type model: dict | bytes

    """
    model = AssignProjectTimesheetCategory.from_dict(model)
    return web.Response(status=200)
