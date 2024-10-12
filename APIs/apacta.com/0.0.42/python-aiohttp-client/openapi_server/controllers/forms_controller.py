from typing import List, Dict
from aiohttp import web

from openapi_server.models.clocking_records_post201_response import ClockingRecordsPost201Response
from openapi_server.models.empty_success_response import EmptySuccessResponse
from openapi_server.models.error_validation import ErrorValidation
from openapi_server.models.forms_form_id_get200_response import FormsFormIdGet200Response
from openapi_server.models.forms_get200_response import FormsGet200Response
from openapi_server.models.forms_post_request import FormsPostRequest
from openapi_server import util


async def forms_form_id_delete(request: web.Request, form_id) -> web.Response:
    """Delete a form

    You can only delete the forms that you&#39;ve submitted yourself

    :param form_id: 
    :type form_id: str

    """
    return web.Response(status=200)


async def forms_form_id_get(request: web.Request, form_id) -> web.Response:
    """View form

    

    :param form_id: 
    :type form_id: str

    """
    return web.Response(status=200)


async def forms_form_id_put(request: web.Request, form_id) -> web.Response:
    """Edit a form

    

    :param form_id: 
    :type form_id: str

    """
    return web.Response(status=200)


async def forms_get(request: web.Request, extended=None, date_from=None, date_to=None, show=None, project_id=None, created_by_id=None, form_template_id=None, form_template_type=None, employee_name=None) -> web.Response:
    """Retrieve array of forms

    

    :param extended: Used to have extended details from the forms from the &#x60;Form&#x60;&#39;s &#x60;FormFields&#x60;
    :type extended: str
    :param date_from: Used in conjunction with &#x60;date_to&#x60; to only show forms within these dates - format like &#x60;2016-28-05&#x60;
    :type date_from: str
    :param date_to: Used in conjunction with &#x60;date_from&#x60; to only show forms within these dates - format like &#x60;2016-28-30&#x60;
    :type date_to: str
    :param show: Used to show forms with trashed
    :type show: str
    :param project_id: Used to filter on the &#x60;project_id&#x60; of the forms
    :type project_id: str
    :type project_id: str
    :param created_by_id: Used to filter on the &#x60;created_by_id&#x60; of the forms
    :type created_by_id: str
    :param form_template_id: Used to filter on the &#x60;form_template_id&#x60; of the forms. Accept single value and array.
    :type form_template_id: List[str]
    :param form_template_type: Filter by &#x60;form_templates.identifier&#x60; containing string passed in &#x60;form_template_type&#x60;. Accept strings like [&#x60;qa&#x60;, &#x60;dagseddel&#x60;]
    :type form_template_type: str
    :param employee_name: Used to filter forms by user&#39;s first or last name
    :type employee_name: str

    """
    return web.Response(status=200)


async def forms_post(request: web.Request, body=None) -> web.Response:
    """Add new form

    Used to add a form into the system

    :param body: 
    :type body: dict | bytes

    """
    body = FormsPostRequest.from_dict(body)
    return web.Response(status=200)


async def forms_undelete_form_id_get(request: web.Request, form_id) -> web.Response:
    """Undelete form and related entities to it

    

    :param form_id: 
    :type form_id: str

    """
    return web.Response(status=200)


async def forms_view_time_form_pdf_form_id_get(request: web.Request, form_id) -> web.Response:
    """Generate time form pdf

    

    :param form_id: 
    :type form_id: str

    """
    return web.Response(status=200)
