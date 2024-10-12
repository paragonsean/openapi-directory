from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.report_output import ReportOutput
from openapi_server.models.reports_output import ReportsOutput
from openapi_server import util


async def batch_upload(request: web.Request, report_id, file) -> web.Response:
    """Batch Upload

    Upload multiple checks and associate them to the report. The inputs for these checks must be sent in an xlsx file, please use the following templates:  **Person:** [Chile](https://app.truora.com/files/person/person-input-cl.xlsx), [Colombia](https://app.truora.com/files/person/person-input-co.xlsx), [Mexico](https://app.truora.com/files/person/person-input-mx.xlsx), [Peru](https://app.truora.com/files/person/person-input-pe.xlsx), [Costa Rica](https://app.truora.com/files/person/person-input-cr.xlsx), [Brazil](https://app.truora.com/files/person/person-input-br.xlsx)  **Vehicle:** [Chile](https://app.truora.com/files/vehicle/vehicle-input-cl.xlsx), [Colombia](https://app.truora.com/files/vehicle/vehicle-input-co.xlsx), [Mexico](https://app.truora.com/files/vehicle/vehicle-input-mx.xlsx), [Peru](https://app.truora.com/files/vehicle/vehicle-input-pe.xlsx)  **Company** [Colombia](https://app.truora.com/files/company/company-input-co.xlsx), [Mexico](https://app.truora.com/files/company/company-input-mx.xlsx), [Brazil](https://app.truora.com/files/company/company-input-br.xlsx)  Keep in mind that we currently do not support batch uploads for custom check types. Background checks created by batch upload are processed with low priority.

    :param report_id: The ID of the Report
    :type report_id: str
    :param file: Uploaded file name
    :type file: List[str]

    """
    return web.Response(status=200)


async def create_report(request: web.Request, name) -> web.Response:
    """Create Report

    Creates a Report to which it is possible to associate multiple Checks.

    :param name: Report name
    :type name: str

    """
    return web.Response(status=200)


async def get_report(request: web.Request, report_id) -> web.Response:
    """Get Report

    Returns a report with the given ID.

    :param report_id: The ID of the Report
    :type report_id: str

    """
    return web.Response(status=200)


async def list_reports(request: web.Request, start_key=None, username=None) -> web.Response:
    """List Reports

    Lists all reports asociated with the client or user requesting.

    :param start_key: Start value for pagination.
    :type start_key: str
    :param username: filter reports created by the specified username
    :type username: str

    """
    return web.Response(status=200)
