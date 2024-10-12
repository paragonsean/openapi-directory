from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_model import ErrorModel
from openapi_server.models.link_collection import LinkCollection
from openapi_server.models.tag import Tag
from openapi_server import util


async def delete_journal_line_tag_0(request: web.Request, employer_id, journal_line_id, tag_id, authorization, api_version) -> web.Response:
    """Delete journal line tag

    Deletes a tag from the journal line

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param journal_line_id: The journal line unique identifier. E.g JL001
    :type journal_line_id: str
    :param tag_id: The tag unique identifier. E.g. MyTag
    :type tag_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_all_journal_line_tags_0(request: web.Request, employer_id, authorization, api_version) -> web.Response:
    """Get all journal line tags

    Gets all the journal line tags

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_all_journal_lines_with_tag_0(request: web.Request, employer_id, tag_id, authorization, api_version) -> web.Response:
    """Get links to tagged journal lines

    Gets the journal lines with the specified tag

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


async def get_tag_from_journal_line_0(request: web.Request, employer_id, journal_line_id, tag_id, authorization, api_version) -> web.Response:
    """Get journal line tag

    Gets a tag from the journal line

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param journal_line_id: The journal line unique identifier. E.g JL001
    :type journal_line_id: str
    :param tag_id: The tag unique identifier. E.g. MyTag
    :type tag_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_tags_from_journal_line_0(request: web.Request, employer_id, journal_line_id, authorization, api_version) -> web.Response:
    """Get tags from journal line

    Gets all tags from the journal line

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


async def put_journal_line_tag_0(request: web.Request, employer_id, journal_line_id, tag_id, authorization, api_version) -> web.Response:
    """Insert journal line tag

    Inserts a tag on the journal line

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param journal_line_id: The journal line unique identifier. E.g JL001
    :type journal_line_id: str
    :param tag_id: The tag unique identifier. E.g. MyTag
    :type tag_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)
