from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_model import ErrorModel
from openapi_server.models.link import Link
from openapi_server.models.link_collection import LinkCollection
from openapi_server.models.pension import Pension
from openapi_server import util


async def delete_pension(request: web.Request, employer_id, pension_id, authorization, api_version) -> web.Response:
    """Delete a Pension

    Delete the specified ppension

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param pension_id: The pensions&#39; unique identifier. E.g PEN001
    :type pension_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def delete_pension_revision(request: web.Request, employer_id, pension_id, effective_date, authorization, api_version) -> web.Response:
    """Delete an Pension revision matching the specified revision date.

    Deletes the specified pension revision for the matching revision date

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param pension_id: The pensions&#39; unique identifier. E.g PEN001
    :type pension_id: str
    :param effective_date: The effective date to be applied. E.g 2016-04-06
    :type effective_date: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    effective_date = util.deserialize_date(effective_date)
    return web.Response(status=200)


async def delete_pension_revision_by_number(request: web.Request, employer_id, pension_id, revision_number, authorization, api_version) -> web.Response:
    """Delete an Pension revision matching the specified revision number.

    Deletes the specified pension revision for the matching revision number

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param pension_id: The pensions&#39; unique identifier. E.g PEN001
    :type pension_id: str
    :param revision_number: The revision number. E.g. 1
    :type revision_number: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_pension_by_effective_date(request: web.Request, employer_id, pension_id, effective_date, authorization, api_version) -> web.Response:
    """Get pension by effective date.

    Returns the penion&#39;s state at the specified effective date.

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param pension_id: The pensions&#39; unique identifier. E.g PEN001
    :type pension_id: str
    :param effective_date: The effective date to be applied. E.g 2016-04-06
    :type effective_date: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    effective_date = util.deserialize_date(effective_date)
    return web.Response(status=200)


async def get_pension_from_employer(request: web.Request, employer_id, pension_id, authorization, api_version) -> web.Response:
    """Get pension from employer

    Gets the specified pension from employer by pension code.

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param pension_id: The pensions&#39; unique identifier. E.g PEN001
    :type pension_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_pension_revision_by_number(request: web.Request, employer_id, pension_id, revision_number, authorization, api_version) -> web.Response:
    """Gets the pension by revision number

    Get the pension revision matching the specified revision number

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param pension_id: The pensions&#39; unique identifier. E.g PEN001
    :type pension_id: str
    :param revision_number: The revision number. E.g. 1
    :type revision_number: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_pension_revisions(request: web.Request, employer_id, pension_id, authorization, api_version) -> web.Response:
    """Get all pension revisions

    Returns links to all revisions of the pension

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param pension_id: The pensions&#39; unique identifier. E.g PEN001
    :type pension_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_pensions_by_effective_date(request: web.Request, employer_id, effective_date, authorization, api_version) -> web.Response:
    """Get pensions from employer at a given effective date.

    Get links to all pensions for the employer on specified effective date.

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


async def get_pensions_from_employer(request: web.Request, employer_id, authorization, api_version) -> web.Response:
    """Get pensions from employer.

    Get links to all pensions for the specified employer.

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def patch_pension(request: web.Request, employer_id, pension_id, authorization, api_version, body) -> web.Response:
    """Patches the pension

    Patches the specified pension with the supplied values

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param pension_id: The pensions&#39; unique identifier. E.g PEN001
    :type pension_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str
    :param body: The pension object.
    :type body: dict | bytes

    """
    body = Pension.from_dict(body)
    return web.Response(status=200)


async def post_pension_into_employer(request: web.Request, employer_id, authorization, api_version, body) -> web.Response:
    """Create a new Pension

    Create a new pension object

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str
    :param body: The pension object.
    :type body: dict | bytes

    """
    body = Pension.from_dict(body)
    return web.Response(status=200)


async def put_pension_into_employer(request: web.Request, employer_id, pension_id, authorization, api_version, body) -> web.Response:
    """Updates the Pension

    Updates existing or inserts the specified pension object

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param pension_id: The pensions&#39; unique identifier. E.g PEN001
    :type pension_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str
    :param body: The pension object.
    :type body: dict | bytes

    """
    body = Pension.from_dict(body)
    return web.Response(status=200)
