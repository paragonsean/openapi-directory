from typing import List, Dict
from aiohttp import web

from openapi_server.models.commentary import Commentary
from openapi_server.models.error_model import ErrorModel
from openapi_server.models.link_collection import LinkCollection
from openapi_server.models.pay_run import PayRun
from openapi_server import util


async def delete_pay_run(request: web.Request, employer_id, pay_schedule_id, pay_run_id, authorization, api_version) -> web.Response:
    """Deletes a pay run

    Delete the specified pay run

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param pay_schedule_id: The pay schedules&#39; unique identifier. E.g SCH001
    :type pay_schedule_id: str
    :param pay_run_id: The pay runs&#39; unique identifier. E.g. PR001
    :type pay_run_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def delete_pay_run_employee(request: web.Request, employer_id, pay_schedule_id, pay_run_id, employee_id, authorization, api_version) -> web.Response:
    """Deletes a pay run employee

    Delete pay run results for a single employee

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param pay_schedule_id: The pay schedules&#39; unique identifier. E.g SCH001
    :type pay_schedule_id: str
    :param pay_run_id: The pay runs&#39; unique identifier. E.g. PR001
    :type pay_run_id: str
    :param employee_id: The employees&#39; unique identifier. E.g EE001
    :type employee_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_ae_assessments_from_pay_run_0(request: web.Request, employer_id, pay_schedule_id, pay_run_id, authorization, api_version) -> web.Response:
    """Get the auto enrolment assessments

    Gets all auto enrolment assessments from the specified pay run

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param pay_schedule_id: The pay schedules&#39; unique identifier. E.g SCH001
    :type pay_schedule_id: str
    :param pay_run_id: The pay runs&#39; unique identifier. E.g. PR001
    :type pay_run_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_all_pay_run_tags_0(request: web.Request, employer_id, pay_schedule_id, authorization, api_version) -> web.Response:
    """Get all pay run tags

    Gets all the pay run tags

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param pay_schedule_id: The pay schedules&#39; unique identifier. E.g SCH001
    :type pay_schedule_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_commentaries_from_pay_run(request: web.Request, employer_id, pay_schedule_id, pay_run_id, authorization, api_version) -> web.Response:
    """Get links to all commentaries for the specified pay run

    Get links to all commentaries for the specified pay run.

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param pay_schedule_id: The pay schedules&#39; unique identifier. E.g SCH001
    :type pay_schedule_id: str
    :param pay_run_id: The pay runs&#39; unique identifier. E.g. PR001
    :type pay_run_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_commentary_from_pay_run_by_employee_0(request: web.Request, employer_id, pay_schedule_id, pay_run_id, employee_id, authorization, api_version) -> web.Response:
    """Get commentary from payrun by specified employee.

    Get commentary from payrun by specified employee.

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param pay_schedule_id: The pay schedules&#39; unique identifier. E.g SCH001
    :type pay_schedule_id: str
    :param pay_run_id: The pay runs&#39; unique identifier. E.g. PR001
    :type pay_run_id: str
    :param employee_id: The employees&#39; unique identifier. E.g EE001
    :type employee_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_employees_from_pay_run_0(request: web.Request, employer_id, pay_schedule_id, pay_run_id, authorization, api_version) -> web.Response:
    """Get employees from the pay run

    Gets links to all employees included in the specified pay run.

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param pay_schedule_id: The pay schedules&#39; unique identifier. E.g SCH001
    :type pay_schedule_id: str
    :param pay_run_id: The pay runs&#39; unique identifier. E.g. PR001
    :type pay_run_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_pay_run_from_pay_schedule(request: web.Request, employer_id, pay_schedule_id, pay_run_id, authorization, api_version) -> web.Response:
    """Gets the pay run from the pay schedule

    Returns the pay run from the pay schedule

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param pay_schedule_id: The pay schedules&#39; unique identifier. E.g SCH001
    :type pay_schedule_id: str
    :param pay_run_id: The pay runs&#39; unique identifier. E.g. PR001
    :type pay_run_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_pay_runs_from_employee(request: web.Request, employer_id, employee_id, authorization, api_version) -> web.Response:
    """Gets the pay runs from the employee

    Get links to all pay runs for the specified employee.

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param employee_id: The employees&#39; unique identifier. E.g EE001
    :type employee_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_pay_runs_from_pay_schedule(request: web.Request, employer_id, pay_schedule_id, authorization, api_version) -> web.Response:
    """Gets the pay runs from the pay schedule

    Get links to all pay runs for the specified pay schedule

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param pay_schedule_id: The pay schedules&#39; unique identifier. E.g SCH001
    :type pay_schedule_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_pay_runs_with_tag_0(request: web.Request, employer_id, pay_schedule_id, tag_id, authorization, api_version) -> web.Response:
    """Get pay runs with tag

    Gets the pay runs with the tag

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param pay_schedule_id: The pay schedules&#39; unique identifier. E.g SCH001
    :type pay_schedule_id: str
    :param tag_id: The tag unique identifier. E.g. MyTag
    :type tag_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_report_lines_from_pay_run_0(request: web.Request, employer_id, pay_schedule_id, pay_run_id, authorization, api_version) -> web.Response:
    """Gets the report lines from the specified pay run

    Returns all report lines associated with the specified pay run

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param pay_schedule_id: The pay schedules&#39; unique identifier. E.g SCH001
    :type pay_schedule_id: str
    :param pay_run_id: The pay runs&#39; unique identifier. E.g. PR001
    :type pay_run_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)
