from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_model import ErrorModel
from openapi_server.models.link import Link
from openapi_server.models.link_collection import LinkCollection
from openapi_server.models.pay_code import PayCode
from openapi_server import util


async def delete_pay_code(request: web.Request, employer_id, pay_code_id, authorization, api_version) -> web.Response:
    """Deletes a pay code

    Delete the specified pay code

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param pay_code_id: The pay code unique identifier. E.g. BASIC
    :type pay_code_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def delete_pay_code_revision(request: web.Request, employer_id, pay_code_id, effective_date, authorization, api_version) -> web.Response:
    """Deletes a pay code revision

    Delete the pay code revision for the specified date

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param pay_code_id: The pay code unique identifier. E.g. BASIC
    :type pay_code_id: str
    :param effective_date: The effective date to be applied. E.g 2016-04-06
    :type effective_date: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    effective_date = util.deserialize_date(effective_date)
    return web.Response(status=200)


async def delete_pay_code_revision_by_number(request: web.Request, employer_id, pay_code_id, revision_number, authorization, api_version) -> web.Response:
    """Delete an PayCode revision matching the specified revision number.

    Deletes the specified pay code revision for the matching revision number

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param pay_code_id: The pay code unique identifier. E.g. BASIC
    :type pay_code_id: str
    :param revision_number: The revision number. E.g. 1
    :type revision_number: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_all_pay_code_tags_0(request: web.Request, employer_id, authorization, api_version) -> web.Response:
    """Get all pay code tags

    Gets all the pay code tags

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_pay_code_by_effective_date(request: web.Request, employer_id, pay_code_id, effective_date, authorization, api_version) -> web.Response:
    """Gets pay code for specified date

    Gets the pay code revision for the specified effective date

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param pay_code_id: The pay code unique identifier. E.g. BASIC
    :type pay_code_id: str
    :param effective_date: The effective date to be applied. E.g 2016-04-06
    :type effective_date: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    effective_date = util.deserialize_date(effective_date)
    return web.Response(status=200)


async def get_pay_code_from_employer(request: web.Request, employer_id, pay_code_id, authorization, api_version) -> web.Response:
    """Gets the specified pay code from the employer

    Returns the specified pay code from the employer

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param pay_code_id: The pay code unique identifier. E.g. BASIC
    :type pay_code_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_pay_code_revision_by_number(request: web.Request, employer_id, pay_code_id, revision_number, authorization, api_version) -> web.Response:
    """Gets the pay code by revision number

    Get the pay code revision matching the specified revision number

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param pay_code_id: The pay code unique identifier. E.g. BASIC
    :type pay_code_id: str
    :param revision_number: The revision number. E.g. 1
    :type revision_number: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_pay_code_revisions(request: web.Request, employer_id, pay_code_id, authorization, api_version) -> web.Response:
    """Get all revisions of the Pay Code

    Returns links to all revisions of the pay code

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param pay_code_id: The pay code unique identifier. E.g. BASIC
    :type pay_code_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_pay_codes_by_effective_date(request: web.Request, employer_id, effective_date, authorization, api_version) -> web.Response:
    """Gets all pay codes for specified date

    Gets the effective pay code revision for the specified date

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param effective_date: The effective date to be applied. E.g 2016-04-06
    :type effective_date: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    effective_date = util.deserialize_date(effective_date)
    return web.Response(status=200)


async def get_pay_codes_from_employer(request: web.Request, employer_id, authorization, api_version) -> web.Response:
    """Gets the pay codes from the employer

    Get links to all the pay codes for the specified employer

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_pay_codes_from_nominal_code(request: web.Request, employer_id, nominal_code_id, authorization, api_version) -> web.Response:
    """Gets the pay codes by nominal code

    Get the pay codes that share the specified nominal code

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param nominal_code_id: The nominal code unique identifier. E.g. NOM001
    :type nominal_code_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_pay_codes_with_tag_0(request: web.Request, employer_id, tag_id, authorization, api_version) -> web.Response:
    """Get pay codes with tag

    Gets the pay codes with the tag

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param tag_id: The tag unique identifier. E.g. MyTag
    :type tag_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def patch_pay_code(request: web.Request, employer_id, pay_code_id, authorization, api_version, body) -> web.Response:
    """Patches the pay code

    Patches the specified pay code object with the supplied values

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param pay_code_id: The pay code unique identifier. E.g. BASIC
    :type pay_code_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str
    :param body: The pay code object.
    :type body: dict | bytes

    """
    body = PayCode.from_dict(body)
    return web.Response(status=200)


async def post_pay_code(request: web.Request, employer_id, authorization, api_version, body) -> web.Response:
    """Create a new pay code

    Create a new pay code object

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str
    :param body: The pay code object.
    :type body: dict | bytes

    """
    body = PayCode.from_dict(body)
    return web.Response(status=200)


async def put_pay_code(request: web.Request, employer_id, pay_code_id, authorization, api_version, body) -> web.Response:
    """Updates a pay code

    Updates the existing specified pay code object

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param pay_code_id: The pay code unique identifier. E.g. BASIC
    :type pay_code_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str
    :param body: The pay code object.
    :type body: dict | bytes

    """
    body = PayCode.from_dict(body)
    return web.Response(status=200)
