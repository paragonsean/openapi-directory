from typing import List, Dict
from aiohttp import web

from openapi_server.models.new_project_model import NewProjectModel
from openapi_server.models.project_details import ProjectDetails
from openapi_server.models.project_dropdown_list import ProjectDropdownList
from openapi_server.models.project_list import ProjectList
from openapi_server.models.update_project_model import UpdateProjectModel
from openapi_server import util


async def project_get(request: web.Request, updated_after=None, page_size=None, page_number=None, sort=None, timesheet_user_id=None, include_archived=None) -> web.Response:
    """Gets list of Projects

    

    :param updated_after: Only show project records updated after a certain date (UTC)
    :type updated_after: str
    :param page_size: Number of items per page (max 1000)
    :type page_size: int
    :param page_number: Page to display. Starts from 1.
    :type page_number: int
    :param sort: A column to sort on. Current possible values: \&quot;DateUpdated\&quot;, \&quot;DateCreated\&quot;, \&quot;DateUpdated desc\&quot;, \&quot;DateCreated desc\&quot;
    :type sort: str
    :param timesheet_user_id: Filter to the projects that the supplied UserID can add timesheets to
    :type timesheet_user_id: int
    :param include_archived: Include Archived Projects in the results
    :type include_archived: bool

    """
    updated_after = util.deserialize_datetime(updated_after)
    return web.Response(status=200)


async def project_get_by_id(request: web.Request, id) -> web.Response:
    """Gets Project by Project ID

    

    :param id: Project ID number
    :type id: int

    """
    return web.Response(status=200)


async def project_lookup(request: web.Request, page_size=None, page_number=None, timesheet_user_id=None, company_idfk=None, search=None) -> web.Response:
    """Gets minimal list of active Projects for the current user

    

    :param page_size: Number of items per page (max 1000)
    :type page_size: int
    :param page_number: Page to display. Starts from 1.
    :type page_number: int
    :param timesheet_user_id: Optionally Filter to the projects that the supplied UserID can add timesheets to
    :type timesheet_user_id: int
    :param company_idfk: Optionally Filter for a specific Company ID
    :type company_idfk: int
    :param search: Search string to match against Project title and Customer name
    :type search: str

    """
    return web.Response(status=200)


async def project_post(request: web.Request, model) -> web.Response:
    """Create a Project

    

    :param model: 
    :type model: dict | bytes

    """
    model = NewProjectModel.from_dict(model)
    return web.Response(status=200)


async def project_put(request: web.Request, model) -> web.Response:
    """Update an Project

    Update a Project

    :param model: 
    :type model: dict | bytes

    """
    model = UpdateProjectModel.from_dict(model)
    return web.Response(status=200)
