from typing import List, Dict
from aiohttp import web

from openapi_server.models.apply_yara_rules200_response import ApplyYaraRules200Response
from openapi_server.models.emulation_output200_response import EmulationOutput200Response
from openapi_server.models.error import Error
from openapi_server.models.generate_partial_yara_rule200_response import GeneratePartialYaraRule200Response
from openapi_server import util


async def apply_yara_rules(request: web.Request, file, rules, is_unpacking_required=None) -> web.Response:
    """apply_yara_rules

    apply given YARA rules to the given executable. (upto 10 rules)

    :param file: file
    :type file: str
    :param rules: 
    :type rules: List[str]
    :param is_unpacking_required: 
    :type is_unpacking_required: str

    """
    return web.Response(status=200)


async def clean(request: web.Request, ) -> web.Response:
    """clean

    clean up the uploaded files


    """
    return web.Response(status=200)


async def emulation_output(request: web.Request, file) -> web.Response:
    """emulation_output

    try to get the emulation output after unpacking the file

    :param file: file
    :type file: str

    """
    return web.Response(status=200)


async def generate_partial_yara_rule(request: web.Request, file, is_unpacking_required=None, minimum_string_length=None, strings_to_ignore=None) -> web.Response:
    """generate_partial_yara_rule

    generate partial YARA rules for give executable. (Rule without the condition section)

    :param file: file
    :type file: str
    :param is_unpacking_required: 
    :type is_unpacking_required: str
    :param minimum_string_length: 
    :type minimum_string_length: str
    :param strings_to_ignore: 
    :type strings_to_ignore: List[str]

    """
    return web.Response(status=200)


async def unpack(request: web.Request, file) -> web.Response:
    """unpack

    try to unpack the given file

    :param file: file
    :type file: str

    """
    return web.Response(status=200)
