from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.instruction import Instruction
from openapi_server.models.instruction_list_result import InstructionListResult
from openapi_server import util


async def instructions_get(request: web.Request, api_version, billing_account_name, billing_profile_name, instruction_name) -> web.Response:
    """instructions_get

    Get the instruction by name.

    :param api_version: Version of the API to be used with the client request. The current version is 2019-10-01-preview.
    :type api_version: str
    :param billing_account_name: billing Account Id.
    :type billing_account_name: str
    :param billing_profile_name: Billing Profile Id.
    :type billing_profile_name: str
    :param instruction_name: Instruction Name.
    :type instruction_name: str

    """
    return web.Response(status=200)


async def instructions_list_by_billing_profile(request: web.Request, billing_account_name, billing_profile_name, api_version) -> web.Response:
    """instructions_list_by_billing_profile

    Lists the instructions by billing profile id.

    :param billing_account_name: billing Account Id.
    :type billing_account_name: str
    :param billing_profile_name: Billing Profile Id.
    :type billing_profile_name: str
    :param api_version: Version of the API to be used with the client request. The current version is 2019-10-01-preview.
    :type api_version: str

    """
    return web.Response(status=200)


async def instructions_put(request: web.Request, api_version, billing_account_name, billing_profile_name, instruction_name, parameters) -> web.Response:
    """instructions_put

    The operation to create or update a instruction.

    :param api_version: Version of the API to be used with the client request. The current version is 2019-10-01-preview.
    :type api_version: str
    :param billing_account_name: billing Account Id.
    :type billing_account_name: str
    :param billing_profile_name: Billing Profile Id.
    :type billing_profile_name: str
    :param instruction_name: Instruction Name.
    :type instruction_name: str
    :param parameters: The new instruction.
    :type parameters: dict | bytes

    """
    parameters = Instruction.from_dict(parameters)
    return web.Response(status=200)
