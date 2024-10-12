from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.filter_contents import FilterContents
from openapi_server.models.filter_dates import FilterDates
from openapi_server.models.language_pairs_report import LanguagePairsReport
from openapi_server.models.project_list import ProjectList
from openapi_server.models.qa_filter import QaFilter
from openapi_server.models.qa_warnings import QaWarnings
from openapi_server.models.report_filter import ReportFilter
from openapi_server.models.users_report import UsersReport
from openapi_server import util


async def generate_qa_report(request: web.Request, body=None) -> web.Response:
    """Generate a QA report for given filter

    Generate a QA report for given filter

    :param body: 
    :type body: dict | bytes

    """
    body = QaFilter.from_dict(body)
    return web.Response(status=200)


async def get_filter_contents(request: web.Request, body=None) -> web.Response:
    """Returns available options for selected timeframe.

    

    :param body: 
    :type body: dict | bytes

    """
    body = FilterDates.from_dict(body)
    return web.Response(status=200)


async def get_language_pairs_report(request: web.Request, body=None) -> web.Response:
    """Language pairs report

    View translation reports for each language pair with translations under your account. You can view company-wide language pairs if you have the user permission.

    :param body: 
    :type body: dict | bytes

    """
    body = ReportFilter.from_dict(body)
    return web.Response(status=200)


async def get_projects_report(request: web.Request, body=None) -> web.Response:
    """Projects report

    View projects under your account, with advanced filtering. You can view company-wide projects if you have the user permission.

    :param body: 
    :type body: dict | bytes

    """
    body = ReportFilter.from_dict(body)
    return web.Response(status=200)


async def get_users_report(request: web.Request, body=None) -> web.Response:
    """Company users report

    View translation reports for each user under your company account. You need the permission to view users in your company.

    :param body: 
    :type body: dict | bytes

    """
    body = ReportFilter.from_dict(body)
    return web.Response(status=200)
