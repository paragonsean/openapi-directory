from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_model import ErrorModel
from openapi_server.models.holiday_scheme import HolidayScheme
from openapi_server.models.link import Link
from openapi_server.models.link_collection import LinkCollection
from openapi_server.models.tag import Tag
from openapi_server import util


async def delete_holiday_scheme(request: web.Request, employer_id, holiday_scheme_id, authorization, api_version) -> web.Response:
    """Delete an holiday scheme

    Delete the specified holiday scheme

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param holiday_scheme_id: The holiday schemes&#39; unique identifier. E.g HOLSCH001
    :type holiday_scheme_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def delete_holiday_scheme_revision(request: web.Request, employer_id, holiday_scheme_id, effective_date, authorization, api_version) -> web.Response:
    """Delete an holiday scheme revision matching the specified revision date.

    Deletes the specified holiday scheme revision for the matching revision date

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param holiday_scheme_id: The holiday schemes&#39; unique identifier. E.g HOLSCH001
    :type holiday_scheme_id: str
    :param effective_date: The effective date to be applied. E.g 2016-04-06
    :type effective_date: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    effective_date = util.deserialize_date(effective_date)
    return web.Response(status=200)


async def delete_holiday_scheme_revision_by_number(request: web.Request, employer_id, holiday_scheme_id, revision_number, authorization, api_version) -> web.Response:
    """Delete an HolidayScheme revision matching the specified revision number.

    Deletes the specified holiday scheme revision for the matching revision number

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param holiday_scheme_id: The holiday schemes&#39; unique identifier. E.g HOLSCH001
    :type holiday_scheme_id: str
    :param revision_number: The revision number. E.g. 1
    :type revision_number: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def delete_holiday_scheme_tag_0(request: web.Request, employer_id, holiday_scheme_id, tag_id, authorization, api_version) -> web.Response:
    """Delete holiday scheme tag

    Deletes a tag from the holiday scheme

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param holiday_scheme_id: The holiday schemes&#39; unique identifier. E.g HOLSCH001
    :type holiday_scheme_id: str
    :param tag_id: The tag unique identifier. E.g. MyTag
    :type tag_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_all_holiday_scheme_tags_0(request: web.Request, employer_id, authorization, api_version) -> web.Response:
    """Get all holiday scheme tags

    Gets all the holiday scheme tags

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_holiday_scheme_by_effective_date(request: web.Request, employer_id, holiday_scheme_id, effective_date, authorization, api_version) -> web.Response:
    """Get holiday scheme by effective date.

    Returns the holiday scheme&#39;s state at the specified effective date.

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param holiday_scheme_id: The holiday schemes&#39; unique identifier. E.g HOLSCH001
    :type holiday_scheme_id: str
    :param effective_date: The effective date to be applied. E.g 2016-04-06
    :type effective_date: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    effective_date = util.deserialize_date(effective_date)
    return web.Response(status=200)


async def get_holiday_scheme_from_employer(request: web.Request, employer_id, holiday_scheme_id, authorization, api_version) -> web.Response:
    """Get holiday scheme from employer

    Gets the specified holiday scheme from employer.

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param holiday_scheme_id: The holiday schemes&#39; unique identifier. E.g HOLSCH001
    :type holiday_scheme_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_holiday_scheme_revision_by_number(request: web.Request, employer_id, holiday_scheme_id, revision_number, authorization, api_version) -> web.Response:
    """Gets the holiday scheme revision by revision number

    Get the holiday scheme revision matching the specified revision number

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param holiday_scheme_id: The holiday schemes&#39; unique identifier. E.g HOLSCH001
    :type holiday_scheme_id: str
    :param revision_number: The revision number. E.g. 1
    :type revision_number: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_holiday_scheme_revisions(request: web.Request, employer_id, holiday_scheme_id, authorization, api_version) -> web.Response:
    """Get all holiday scheme revisions

    Gets links to all the holiday scheme revisions

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param holiday_scheme_id: The holiday schemes&#39; unique identifier. E.g HOLSCH001
    :type holiday_scheme_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_holiday_schemes_by_effective_date(request: web.Request, employer_id, effective_date, authorization, api_version) -> web.Response:
    """Get holiday schemes from employer at a given effective date.

    Get links to all holiday schemes for the employer on specified effective date.

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


async def get_holiday_schemes_from_employer(request: web.Request, employer_id, authorization, api_version) -> web.Response:
    """Get holiday schemes from employer.

    Get links to all holiday schemes for the specified employer.

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_holiday_schemes_with_tag_0(request: web.Request, employer_id, tag_id, authorization, api_version) -> web.Response:
    """Get holiday schemes with tag

    Gets the holiday scheme with the tag

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


async def get_tag_from_holiday_scheme_0(request: web.Request, employer_id, holiday_scheme_id, tag_id, authorization, api_version) -> web.Response:
    """Get holiday scheme tag

    Gets the tag from the holiday scheme

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param holiday_scheme_id: The holiday schemes&#39; unique identifier. E.g HOLSCH001
    :type holiday_scheme_id: str
    :param tag_id: The tag unique identifier. E.g. MyTag
    :type tag_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_tag_from_holiday_scheme_revision_0(request: web.Request, employer_id, holiday_scheme_id, tag_id, effective_date, authorization, api_version) -> web.Response:
    """Get holiday scheme revision tag

    Gets the tag from the holiday scheme revision

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param holiday_scheme_id: The holiday schemes&#39; unique identifier. E.g HOLSCH001
    :type holiday_scheme_id: str
    :param tag_id: The tag unique identifier. E.g. MyTag
    :type tag_id: str
    :param effective_date: The effective date to be applied. E.g 2016-04-06
    :type effective_date: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    effective_date = util.deserialize_date(effective_date)
    return web.Response(status=200)


async def get_tags_from_holiday_scheme_0(request: web.Request, employer_id, holiday_scheme_id, authorization, api_version) -> web.Response:
    """Get all tags from the holiday scheme

    Gets all the tags from the holiday scheme

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param holiday_scheme_id: The holiday schemes&#39; unique identifier. E.g HOLSCH001
    :type holiday_scheme_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_tags_from_holiday_scheme_revision_0(request: web.Request, employer_id, holiday_scheme_id, effective_date, authorization, api_version) -> web.Response:
    """Get all holiday scheme revision tags

    Gets all the tags from the holiday scheme revision

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param holiday_scheme_id: The holiday schemes&#39; unique identifier. E.g HOLSCH001
    :type holiday_scheme_id: str
    :param effective_date: The effective date to be applied. E.g 2016-04-06
    :type effective_date: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    effective_date = util.deserialize_date(effective_date)
    return web.Response(status=200)


async def patch_holiday_scheme(request: web.Request, employer_id, holiday_scheme_id, authorization, api_version, body) -> web.Response:
    """Patches the holiday scheme

    Patches the specified holiday scheme with the supplied values

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param holiday_scheme_id: The holiday schemes&#39; unique identifier. E.g HOLSCH001
    :type holiday_scheme_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str
    :param body: The holiday scheme object.
    :type body: dict | bytes

    """
    body = HolidayScheme.from_dict(body)
    return web.Response(status=200)


async def post_holiday_scheme_into_employer(request: web.Request, employer_id, authorization, api_version, body) -> web.Response:
    """Create a new holiday scheme

    Create a new holiday scheme object

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str
    :param body: The holiday scheme object.
    :type body: dict | bytes

    """
    body = HolidayScheme.from_dict(body)
    return web.Response(status=200)


async def put_holiday_scheme_into_employer(request: web.Request, employer_id, holiday_scheme_id, authorization, api_version, body) -> web.Response:
    """Updates the holiday scheme

    Updates the existing specified holiday scheme object

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param holiday_scheme_id: The holiday schemes&#39; unique identifier. E.g HOLSCH001
    :type holiday_scheme_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str
    :param body: The holiday scheme object.
    :type body: dict | bytes

    """
    body = HolidayScheme.from_dict(body)
    return web.Response(status=200)


async def put_holiday_scheme_tag_0(request: web.Request, employer_id, holiday_scheme_id, tag_id, authorization, api_version) -> web.Response:
    """Insert holiday scheme tag

    Inserts a new tag on the holiday scheme

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param holiday_scheme_id: The holiday schemes&#39; unique identifier. E.g HOLSCH001
    :type holiday_scheme_id: str
    :param tag_id: The tag unique identifier. E.g. MyTag
    :type tag_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)
