from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_model import ErrorModel
from openapi_server.models.link import Link
from openapi_server.models.link_collection import LinkCollection
from openapi_server.models.sub_contractor import SubContractor
from openapi_server import util


async def delete_sub_contractor(request: web.Request, employer_id, sub_contractor_id, authorization, api_version) -> web.Response:
    """Delete an sub contractor

    Delete the specified sub contractor

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


async def delete_sub_contractor_revision(request: web.Request, employer_id, sub_contractor_id, effective_date, authorization, api_version) -> web.Response:
    """Delete an sub contractor revision matching the specified revision date.

    Deletes the specified sub contractor revision for the matching revision date

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param sub_contractor_id: The sub contractors&#39; unique identifier. E.g SUB001
    :type sub_contractor_id: str
    :param effective_date: The effective date to be applied. E.g 2016-04-06
    :type effective_date: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    effective_date = util.deserialize_date(effective_date)
    return web.Response(status=200)


async def delete_sub_contractor_revision_by_number(request: web.Request, employer_id, sub_contractor_id, revision_number, authorization, api_version) -> web.Response:
    """Delete an SubContractor revision matching the specified revision number.

    Deletes the specified sub contractor revision for the matching revision number

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param sub_contractor_id: The sub contractors&#39; unique identifier. E.g SUB001
    :type sub_contractor_id: str
    :param revision_number: The revision number. E.g. 1
    :type revision_number: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_sub_contractor_by_effective_date(request: web.Request, employer_id, sub_contractor_id, effective_date, authorization, api_version) -> web.Response:
    """Get sub contractor by effective date.

    Returns the sub contractor&#39;s state at the specified effective date.

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param sub_contractor_id: The sub contractors&#39; unique identifier. E.g SUB001
    :type sub_contractor_id: str
    :param effective_date: The effective date to be applied. E.g 2016-04-06
    :type effective_date: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    effective_date = util.deserialize_date(effective_date)
    return web.Response(status=200)


async def get_sub_contractor_from_employer(request: web.Request, employer_id, sub_contractor_id, authorization, api_version) -> web.Response:
    """Get sub contractor from employer

    Gets the specified sub contractor from employer.

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


async def get_sub_contractor_revision_by_number(request: web.Request, employer_id, sub_contractor_id, revision_number, authorization, api_version) -> web.Response:
    """Gets the sub contractor by revision number

    Get the sub contractor revision matching the specified revision number

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param sub_contractor_id: The sub contractors&#39; unique identifier. E.g SUB001
    :type sub_contractor_id: str
    :param revision_number: The revision number. E.g. 1
    :type revision_number: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_sub_contractor_revisions(request: web.Request, employer_id, sub_contractor_id, authorization, api_version) -> web.Response:
    """Get all sub contractor revisions

    Gets links to all the sub contractor revisions

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


async def get_sub_contractors_by_effective_date(request: web.Request, employer_id, effective_date, authorization, api_version) -> web.Response:
    """Get sub contractors from employer at a given effective date.

    Get links to all sub contractors for the employer on specified effective date.

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


async def get_sub_contractors_from_employer(request: web.Request, employer_id, authorization, api_version) -> web.Response:
    """Get sub contractors from employer.

    Get links to all sub contractors for the specified employer.

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def patch_sub_contractor(request: web.Request, employer_id, sub_contractor_id, authorization, api_version, body) -> web.Response:
    """Patches the sub contractor

    Patches the specified sub contractor with the supplied values

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param sub_contractor_id: The sub contractors&#39; unique identifier. E.g SUB001
    :type sub_contractor_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str
    :param body: The sub contractor object.
    :type body: dict | bytes

    """
    body = SubContractor.from_dict(body)
    return web.Response(status=200)


async def post_sub_contractor_into_employer(request: web.Request, employer_id, authorization, api_version, body) -> web.Response:
    """Create a new sub contractor

    Create a new sub contractor object

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str
    :param body: The sub contractor object.
    :type body: dict | bytes

    """
    body = SubContractor.from_dict(body)
    return web.Response(status=200)


async def put_sub_contractor_into_employer(request: web.Request, employer_id, sub_contractor_id, authorization, api_version, body) -> web.Response:
    """Updates the sub contractor

    Updates the existing specified sub contractor object

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param sub_contractor_id: The sub contractors&#39; unique identifier. E.g SUB001
    :type sub_contractor_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str
    :param body: The sub contractor object.
    :type body: dict | bytes

    """
    body = SubContractor.from_dict(body)
    return web.Response(status=200)
