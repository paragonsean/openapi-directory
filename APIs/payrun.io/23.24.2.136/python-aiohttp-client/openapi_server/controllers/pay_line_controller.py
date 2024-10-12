from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_model import ErrorModel
from openapi_server.models.link_collection import LinkCollection
from openapi_server.models.pay_line import PayLine
from openapi_server import util


async def get_all_pay_line_tags_0(request: web.Request, employer_id, employee_id, authorization, api_version) -> web.Response:
    """Get all pay line tags

    Gets all the pay line tags

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


async def get_pay_line_from_employee(request: web.Request, employer_id, employee_id, pay_line_id, authorization, api_version) -> web.Response:
    """Gets the specified pay line from the employee

    Returns the specified pay line from employee

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param employee_id: The employees&#39; unique identifier. E.g EE001
    :type employee_id: str
    :param pay_line_id: The pay line unique identifier. E.g. PL001
    :type pay_line_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_pay_lines_from_employee(request: web.Request, employer_id, employee_id, authorization, api_version) -> web.Response:
    """Gets the pay lines from the specified employee

    Get links to all pay lines for the specified employee

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


async def get_pay_lines_from_pay_run(request: web.Request, employer_id, pay_schedule_id, pay_run_id, authorization, api_version) -> web.Response:
    """Gets the pay lines from the specified pay run

    Get links to all pay lines for the specified pay run

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


async def get_pay_lines_with_tag_0(request: web.Request, employer_id, employee_id, tag_id, authorization, api_version) -> web.Response:
    """Get pay lines with tag

    Gets the pay line with the tag

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param employee_id: The employees&#39; unique identifier. E.g EE001
    :type employee_id: str
    :param tag_id: The tag unique identifier. E.g. MyTag
    :type tag_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)
