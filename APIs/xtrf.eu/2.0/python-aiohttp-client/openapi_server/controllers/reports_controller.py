from typing import List, Dict
from aiohttp import web

from openapi_server.models.export_request_dto import ExportRequestDTO
from openapi_server.models.import_request_dto import ImportRequestDTO
from openapi_server.models.import_result_dto import ImportResultDTO
from openapi_server.models.preferred_request_dto import PreferredRequestDTO
from openapi_server.models.report_result_dto import ReportResultDTO
from openapi_server import util


async def delete11(request: web.Request, report_id) -> web.Response:
    """Removes a report.

    Removes a report.

    :param report_id: report&#39;s internal identifier
    :type report_id: int

    """
    return web.Response(status=200)


async def duplicate1(request: web.Request, report_id) -> web.Response:
    """Duplicates a report.

    Duplicates a report.

    :param report_id: report&#39;s internal identifier
    :type report_id: int

    """
    return web.Response(status=200)


async def export_to_xml(request: web.Request, body) -> web.Response:
    """Exports reports definition to XML.

    Exports reports definition to XML.

    :param body: Exported reports definition to XML.
    :type body: dict | bytes

    """
    body = ExportRequestDTO.from_dict(body)
    return web.Response(status=200)


async def generate_csv(request: web.Request, report_id) -> web.Response:
    """Generates CSV content for a report.

    Generates CSV content for a report.

    :param report_id: report&#39;s internal identifier
    :type report_id: int

    """
    return web.Response(status=200)


async def generate_printer_friendly(request: web.Request, report_id) -> web.Response:
    """Generates printer friendly content for a report.

    Generates printer friendly content for a report.

    :param report_id: report&#39;s internal identifier
    :type report_id: int

    """
    return web.Response(status=200)


async def import_from_xml(request: web.Request, body) -> web.Response:
    """Imports reports definition from XML.

    Imports a report definition from an XML using a file token. To obtain the token, you first need to upload a temporary XML file, as specified in the Files section. Note that the name of the imported report must be unique.

    :param body: Imported reports definition from XML.
    :type body: dict | bytes

    """
    body = ImportRequestDTO.from_dict(body)
    return web.Response(status=200)


async def set_preferred(request: web.Request, report_id, body) -> web.Response:
    """Marks report as preferred or not.

    Marks report as preferred or not.

    :param report_id: report&#39;s internal identifier
    :type report_id: int
    :param body: Marked report as preferred or not.
    :type body: dict | bytes

    """
    body = PreferredRequestDTO.from_dict(body)
    return web.Response(status=200)
