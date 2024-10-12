from typing import List, Dict
from aiohttp import web

from openapi_server.models.employer import Employer
from openapi_server.models.employer_secret import EmployerSecret
from openapi_server.models.employer_summary import EmployerSummary
from openapi_server.models.error_model import ErrorModel
from openapi_server.models.link import Link
from openapi_server.models.link_collection import LinkCollection
from openapi_server import util


async def delete_employer(request: web.Request, employer_id, authorization, api_version) -> web.Response:
    """Delete an Employer

    Delete the specified employer

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def delete_employer_revision(request: web.Request, employer_id, effective_date, authorization, api_version) -> web.Response:
    """Delete an Employer revision matching the specified revision date.

    Deletes the specified employer revision for the matching revision date

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


async def delete_employer_revision_by_number(request: web.Request, employer_id, revision_number, authorization, api_version) -> web.Response:
    """Delete an Employer revision matching the specified revision number.

    Deletes the specified employer revision for the matching revision number

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param revision_number: The revision number. E.g. 1
    :type revision_number: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def delete_employer_secret(request: web.Request, employer_id, secret_id, authorization, api_version) -> web.Response:
    """Deletes employer secret

    Deletes an employer secret from the given resource location

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param secret_id: The secret unique identifier. E.g ERSEC001
    :type secret_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_all_employer_tags_0(request: web.Request, authorization, api_version) -> web.Response:
    """Get all employer tags

    Gets all the employer tags

    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_employer(request: web.Request, employer_id, authorization, api_version) -> web.Response:
    """Gets the employer

    Get the specified employer object

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_employer_by_effective_date(request: web.Request, employer_id, effective_date, authorization, api_version) -> web.Response:
    """Gets the employer at the specified effective

    Returns the employer&#39;s state at the specified effective date.

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


async def get_employer_revision_by_number(request: web.Request, employer_id, revision_number, authorization, api_version) -> web.Response:
    """Gets the employer by revision number

    Get the employer revision matching the specified revision number

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param revision_number: The revision number. E.g. 1
    :type revision_number: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_employer_revision_summaries(request: web.Request, employer_id, authorization, api_version) -> web.Response:
    """Get all employer revision summaries

    Gets links to all employer revision summaries

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_employer_revision_summary_by_number(request: web.Request, employer_id, revision_number, authorization, api_version) -> web.Response:
    """Gets the employer summary by revision number

    Get the employer revision summary matching the specified revision number

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param revision_number: The revision number. E.g. 1
    :type revision_number: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_employer_revisions(request: web.Request, employer_id, authorization, api_version) -> web.Response:
    """Gets the employer revisions

    Gets links to all the employer revisions

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_employer_secret(request: web.Request, employer_id, secret_id, authorization, api_version) -> web.Response:
    """Get employer secret

    Get the public visible employer secret object

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param secret_id: The secret unique identifier. E.g ERSEC001
    :type secret_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_employer_secrets(request: web.Request, employer_id, authorization, api_version) -> web.Response:
    """Get all employer secret links

    Get all the employer secret links

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_employer_summaries(request: web.Request, authorization, api_version) -> web.Response:
    """Get employer summaries.

    Get links to all employer summaries.

    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_employer_summaries_by_effective_date(request: web.Request, effective_date, authorization, api_version) -> web.Response:
    """Get employer summaries at a given effective date.

    Get links to all employer summaries on specified effective date.

    :param effective_date: The effective date to be applied. E.g 2016-04-06
    :type effective_date: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    effective_date = util.deserialize_date(effective_date)
    return web.Response(status=200)


async def get_employer_summary(request: web.Request, employer_id, authorization, api_version) -> web.Response:
    """Get employer summary

    Gets the specified employer summary data.

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_employer_summary_by_effective_date(request: web.Request, employer_id, effective_date, authorization, api_version) -> web.Response:
    """Get employer summary by effective date.

    Gets the employer summary for the specified effective date.

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


async def get_employers(request: web.Request, authorization, api_version) -> web.Response:
    """Gets all employers

    Gets links to all employers contained under the authorised application scope

    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_employers_by_effective_date(request: web.Request, effective_date, authorization, api_version) -> web.Response:
    """Gets all employers at the specified effective date

    Gets links to all employers contained under the authorised application scope for the specified effective date.

    :param effective_date: The effective date to be applied. E.g 2016-04-06
    :type effective_date: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    effective_date = util.deserialize_date(effective_date)
    return web.Response(status=200)


async def get_employers_with_tag_0(request: web.Request, tag_id, authorization, api_version) -> web.Response:
    """Get employers with tag

    Gets the employers with the tag

    :param tag_id: The tag unique identifier. E.g. MyTag
    :type tag_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def patch_employer(request: web.Request, employer_id, authorization, api_version, body) -> web.Response:
    """Patches the employer

    Patches the specified employer with the supplied values

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str
    :param body: The employer object.
    :type body: dict | bytes

    """
    body = Employer.from_dict(body)
    return web.Response(status=200)


async def post_employer(request: web.Request, authorization, api_version, body) -> web.Response:
    """Create a new Employer

    Create a new employer object

    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str
    :param body: The employer object.
    :type body: dict | bytes

    """
    body = Employer.from_dict(body)
    return web.Response(status=200)


async def post_employer_secret(request: web.Request, employer_id, authorization, api_version) -> web.Response:
    """Create a new employer secret

    Create new employer secret using auto generated resource location key

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def put_employer(request: web.Request, employer_id, authorization, api_version, body) -> web.Response:
    """Updates the Employer

    Updates the existing specified employer object

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str
    :param body: The employer object.
    :type body: dict | bytes

    """
    body = Employer.from_dict(body)
    return web.Response(status=200)


async def put_employer_secret(request: web.Request, employer_id, secret_id, authorization, api_version) -> web.Response:
    """Create a new employer secret

    Create / update an employer secret at the given resource location

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param secret_id: The secret unique identifier. E.g ERSEC001
    :type secret_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)
