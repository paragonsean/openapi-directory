from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_model import ErrorModel
from openapi_server.models.link import Link
from openapi_server.models.link_collection import LinkCollection
from openapi_server.models.reporting_instruction import ReportingInstruction
from openapi_server import util


async def delete_reporting_instruction(request: web.Request, employer_id, reporting_instruction_id, authorization, api_version) -> web.Response:
    """Deletes a reporting instruction

    Delete the specified reporting instruction

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param reporting_instruction_id: The reporting instruction unique identifier. E.g. SERRPT001
    :type reporting_instruction_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_reporting_instruction_from_employer(request: web.Request, employer_id, reporting_instruction_id, authorization, api_version) -> web.Response:
    """Gets the specified reporting instruction from the employer

    Returns the specified pay instruction from employee

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param reporting_instruction_id: The reporting instruction unique identifier. E.g. SERRPT001
    :type reporting_instruction_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_reporting_instructions_from_employer(request: web.Request, employer_id, authorization, api_version) -> web.Response:
    """Gets the reporting instructions from the specified employer

    Get links to all pay instructions for the specified employee

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def post_reporting_instruction(request: web.Request, employer_id, authorization, api_version, body) -> web.Response:
    """Creates a new Reporting Instruction

    Creates a new reporting instruction object

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str
    :param body: The reporting instruction object.
    :type body: dict | bytes

    """
    body = ReportingInstruction.from_dict(body)
    return web.Response(status=200)


async def put_reporting_instruction(request: web.Request, employer_id, reporting_instruction_id, authorization, api_version, body) -> web.Response:
    """Update a reporting Instruction

    Updates the existing specified reporting instruction object

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param reporting_instruction_id: The reporting instruction unique identifier. E.g. SERRPT001
    :type reporting_instruction_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str
    :param body: The reporting instruction object.
    :type body: dict | bytes

    """
    body = ReportingInstruction.from_dict(body)
    return web.Response(status=200)
