from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_model import ErrorModel
from openapi_server.models.link import Link
from openapi_server.models.link_collection import LinkCollection
from openapi_server.models.pay_instruction import PayInstruction
from openapi_server import util


async def delete_pay_instruction(request: web.Request, employer_id, employee_id, pay_instruction_id, authorization, api_version) -> web.Response:
    """Deletes a pay instruction

    Delete the specified pay instruction

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param employee_id: The employees&#39; unique identifier. E.g EE001
    :type employee_id: str
    :param pay_instruction_id: The pay instruction unique identifier. E.g. SAL001
    :type pay_instruction_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_all_pay_instruction_tags_0(request: web.Request, employer_id, employee_id, authorization, api_version) -> web.Response:
    """Get all pay instruction tags

    Gets all the pay instruction tags

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


async def get_pay_instruction_from_employee(request: web.Request, employer_id, employee_id, pay_instruction_id, authorization, api_version) -> web.Response:
    """Gets the specified pay instruction from the employee

    Returns the specified pay instruction from employee

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param employee_id: The employees&#39; unique identifier. E.g EE001
    :type employee_id: str
    :param pay_instruction_id: The pay instruction unique identifier. E.g. SAL001
    :type pay_instruction_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_pay_instructions_from_employee(request: web.Request, employer_id, employee_id, authorization, api_version) -> web.Response:
    """Gets the pay instructions from the specified employee

    Get links to all pay instructions for the specified employee

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


async def get_pay_instructions_with_tag_0(request: web.Request, employer_id, employee_id, tag_id, authorization, api_version) -> web.Response:
    """Get pay instructions with tag

    Gets the pay instructions with the tag

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


async def patch_pay_instruction(request: web.Request, employer_id, employee_id, pay_instruction_id, authorization, api_version, body) -> web.Response:
    """Sparse Update of a Pay Instruction

    Patches the specified pay instruction with the supplied values

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param employee_id: The employees&#39; unique identifier. E.g EE001
    :type employee_id: str
    :param pay_instruction_id: The pay instruction unique identifier. E.g. SAL001
    :type pay_instruction_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str
    :param body: The pay instruction object.
    :type body: dict | bytes

    """
    body = PayInstruction.from_dict(body)
    return web.Response(status=200)


async def post_pay_instruction(request: web.Request, employer_id, employee_id, authorization, api_version, body) -> web.Response:
    """Creates a new Pay Instruction

    Creates a new pay instruction object

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param employee_id: The employees&#39; unique identifier. E.g EE001
    :type employee_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str
    :param body: The pay instruction object.
    :type body: dict | bytes

    """
    body = PayInstruction.from_dict(body)
    return web.Response(status=200)


async def put_pay_instruction(request: web.Request, employer_id, employee_id, pay_instruction_id, authorization, api_version, body) -> web.Response:
    """Update a Pay Instruction

    Updates the existing specified pay instruction object

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param employee_id: The employees&#39; unique identifier. E.g EE001
    :type employee_id: str
    :param pay_instruction_id: The pay instruction unique identifier. E.g. SAL001
    :type pay_instruction_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str
    :param body: The pay instruction object.
    :type body: dict | bytes

    """
    body = PayInstruction.from_dict(body)
    return web.Response(status=200)
