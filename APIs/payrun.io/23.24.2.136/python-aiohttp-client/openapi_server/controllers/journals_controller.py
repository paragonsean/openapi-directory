from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_model import ErrorModel
from openapi_server.models.journal_instruction import JournalInstruction
from openapi_server.models.journal_line import JournalLine
from openapi_server.models.link import Link
from openapi_server.models.link_collection import LinkCollection
from openapi_server import util


async def delete_journal_instruction(request: web.Request, employer_id, journal_instruction_id, authorization, api_version) -> web.Response:
    """Deletes a Journal instruction

    Delete the specified Journal instruction

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param journal_instruction_id: The journal instruction unique identifier. E.g JI001
    :type journal_instruction_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def delete_journal_instruction_template(request: web.Request, journal_instruction_id, authorization, api_version) -> web.Response:
    """Deletes a Journal instruction template

    Delete the specified Journal instruction template object

    :param journal_instruction_id: The journal instruction unique identifier. E.g JI001
    :type journal_instruction_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_journal_instruction_from_employer(request: web.Request, employer_id, journal_instruction_id, authorization, api_version) -> web.Response:
    """Gets the specified journal instruction from the employer

    Returns the specified journal instruction from employer

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param journal_instruction_id: The journal instruction unique identifier. E.g JI001
    :type journal_instruction_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_journal_instruction_template(request: web.Request, journal_instruction_id, authorization, api_version) -> web.Response:
    """Gets the Journal instructions template for the application

    Retrurns the specified journal instruction from the application

    :param journal_instruction_id: The journal instruction unique identifier. E.g JI001
    :type journal_instruction_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_journal_instruction_templates(request: web.Request, authorization, api_version) -> web.Response:
    """Gets the Journal instructions templates for the application

    Get links to all journal instruction templates for the application

    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_journal_instructions_from_employer(request: web.Request, employer_id, authorization, api_version) -> web.Response:
    """Gets the Journal instructions from the specified employer

    Get links to all journal instructions for the specified employer

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_journal_line_from_employer(request: web.Request, employer_id, journal_line_id, authorization, api_version) -> web.Response:
    """Gets the specified journal Line from the employer

    Returns the specified journal Line from employer

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param journal_line_id: The journal line unique identifier. E.g JL001
    :type journal_line_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_journal_lines_from_employee(request: web.Request, employer_id, employee_id, authorization, api_version) -> web.Response:
    """Gets the journal Lines from the specified employee

    Get links to all journal lines for the specified employee

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


async def get_journal_lines_from_employer(request: web.Request, employer_id, authorization, api_version) -> web.Response:
    """Gets the Journal Lines from the specified employer

    Get links to all journal Lines for the specified employer

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_journal_lines_from_pay_run(request: web.Request, employer_id, pay_schedule_id, pay_run_id, authorization, api_version) -> web.Response:
    """Gets the journal Lines from the specified pay run

    Get links to all journal lines for the specified pay run

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


async def get_journal_lines_from_sub_contractor(request: web.Request, employer_id, sub_contractor_id, authorization, api_version) -> web.Response:
    """Gets the journal Lines from the specified sub contractor

    Get links to all journal lines for the specified sub contractor

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param sub_contractor_id: The sub contractors&#39; unique identifier. E.g SUB001
    :type sub_contractor_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def post_journal_instruction(request: web.Request, employer_id, authorization, api_version) -> web.Response:
    """Creates a new Journal Instruction

    Creates a new Journal instruction object

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def post_journal_instruction_template(request: web.Request, authorization, api_version) -> web.Response:
    """Creates a new Journal Instruction template

    Creates a new Journal instruction teamplte object

    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def put_journal_instruction(request: web.Request, employer_id, journal_instruction_id, authorization, api_version) -> web.Response:
    """Update a Journal Instruction

    Updates the existing specified Journal instruction object

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param journal_instruction_id: The journal instruction unique identifier. E.g JI001
    :type journal_instruction_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def put_journal_instruction_template(request: web.Request, journal_instruction_id, authorization, api_version) -> web.Response:
    """Update a Journal Instruction template

    Updates the existing specified Journal instruction template object

    :param journal_instruction_id: The journal instruction unique identifier. E.g JI001
    :type journal_instruction_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)
