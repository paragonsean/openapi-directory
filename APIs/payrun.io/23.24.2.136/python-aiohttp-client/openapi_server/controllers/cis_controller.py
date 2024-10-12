from typing import List, Dict
from aiohttp import web

from openapi_server.models.cis_instruction import CisInstruction
from openapi_server.models.cis_line import CisLine
from openapi_server.models.cis_line_type import CisLineType
from openapi_server.models.cis_transaction import CisTransaction
from openapi_server.models.error_model import ErrorModel
from openapi_server.models.link import Link
from openapi_server.models.link_collection import LinkCollection
from openapi_server.models.tag import Tag
from openapi_server import util


async def delete_cis_instruction(request: web.Request, employer_id, sub_contractor_id, cis_instruction_id, authorization, api_version) -> web.Response:
    """Delete a CIS instruction

    Delete the specified CIS instruction

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param sub_contractor_id: The sub contractors&#39; unique identifier. E.g SUB001
    :type sub_contractor_id: str
    :param cis_instruction_id: The CIS instruction unique identifier. E.g. CIS001
    :type cis_instruction_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def delete_cis_instruction_tag_0(request: web.Request, employer_id, sub_contractor_id, cis_instruction_id, tag_id, authorization, api_version) -> web.Response:
    """Delete CIS instruction tag

    Deletes a tag from the CIS instruction

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param sub_contractor_id: The sub contractors&#39; unique identifier. E.g SUB001
    :type sub_contractor_id: str
    :param cis_instruction_id: The CIS instruction unique identifier. E.g. CIS001
    :type cis_instruction_id: str
    :param tag_id: The tag unique identifier. E.g. MyTag
    :type tag_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def delete_cis_line(request: web.Request, employer_id, sub_contractor_id, cis_line_id, authorization, api_version) -> web.Response:
    """Delete a CIS line

    Delete the specified CIS line

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param sub_contractor_id: The sub contractors&#39; unique identifier. E.g SUB001
    :type sub_contractor_id: str
    :param cis_line_id: The CIS line unique identifier. E.g. CISLN001
    :type cis_line_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def delete_cis_line_tag_0(request: web.Request, employer_id, sub_contractor_id, cis_line_id, tag_id, authorization, api_version) -> web.Response:
    """Delete CIS line tag

    Deletes a tag from the CIS line

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param sub_contractor_id: The sub contractors&#39; unique identifier. E.g SUB001
    :type sub_contractor_id: str
    :param cis_line_id: The CIS line unique identifier. E.g. CISLN001
    :type cis_line_id: str
    :param tag_id: The tag unique identifier. E.g. MyTag
    :type tag_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def delete_cis_line_type(request: web.Request, employer_id, cis_line_type_id, authorization, api_version) -> web.Response:
    """Delete an CIS line type

    Delete the specified CIS line type

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param cis_line_type_id: The CIS line type unique identifier. E.g. TYPEA
    :type cis_line_type_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def delete_cis_line_type_tag_0(request: web.Request, employer_id, cis_line_type_id, tag_id, authorization, api_version) -> web.Response:
    """Delete CIS line type tag

    Deletes a tag from the CIS line type

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param cis_line_type_id: The CIS line type unique identifier. E.g. TYPEA
    :type cis_line_type_id: str
    :param tag_id: The tag unique identifier. E.g. MyTag
    :type tag_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def delete_cis_transaction(request: web.Request, employer_id, cis_transaction_id, authorization, api_version) -> web.Response:
    """Delete the CIS transaction

    Deletes the specified CIS transaction

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param cis_transaction_id: The CIS transaction unique identifier. E.g. CISTRAN001
    :type cis_transaction_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def delete_sub_contractor_tag_0(request: web.Request, employer_id, sub_contractor_id, tag_id, authorization, api_version) -> web.Response:
    """Delete sub contractor tag

    Deletes a tag from the sub contractor

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param sub_contractor_id: The sub contractors&#39; unique identifier. E.g SUB001
    :type sub_contractor_id: str
    :param tag_id: The tag unique identifier. E.g. MyTag
    :type tag_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_all_cis_instruction_tags_0(request: web.Request, employer_id, sub_contractor_id, authorization, api_version) -> web.Response:
    """Get all CIS instruction tags

    Gets all the CIS instruction tags

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


async def get_all_cis_line_tags_0(request: web.Request, employer_id, sub_contractor_id, authorization, api_version) -> web.Response:
    """Get all CIS line tags

    Gets all the CIS line tags

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


async def get_all_cis_line_type_tags_0(request: web.Request, employer_id, authorization, api_version) -> web.Response:
    """Get all CIS line type tags

    Gets all the CIS line type tags

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_all_sub_contractor_tags_0(request: web.Request, employer_id, authorization, api_version) -> web.Response:
    """Get all sub contractor tags

    Gets all the sub contractor tags

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_cis_instruction_from_sub_contractor(request: web.Request, employer_id, sub_contractor_id, cis_instruction_id, authorization, api_version) -> web.Response:
    """Get CIS instruction from sub contractor

    Gets the specified CIS instruction from sub contractor.

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param sub_contractor_id: The sub contractors&#39; unique identifier. E.g SUB001
    :type sub_contractor_id: str
    :param cis_instruction_id: The CIS instruction unique identifier. E.g. CIS001
    :type cis_instruction_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_cis_instructions_from_sub_contractor(request: web.Request, employer_id, sub_contractor_id, authorization, api_version) -> web.Response:
    """Get CIS instructions from sub contractor.

    Get links to all CIS instructions for the specified sub contractor.

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


async def get_cis_instructions_with_tag_0(request: web.Request, employer_id, sub_contractor_id, tag_id, authorization, api_version) -> web.Response:
    """Get CIS instructions with tag

    Gets the CIS instruction with the tag

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param sub_contractor_id: The sub contractors&#39; unique identifier. E.g SUB001
    :type sub_contractor_id: str
    :param tag_id: The tag unique identifier. E.g. MyTag
    :type tag_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_cis_line_from_sub_contractor(request: web.Request, employer_id, sub_contractor_id, cis_line_id, authorization, api_version) -> web.Response:
    """Get CIS line from sub contractor

    Gets the specified CIS line from sub contractor.

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param sub_contractor_id: The sub contractors&#39; unique identifier. E.g SUB001
    :type sub_contractor_id: str
    :param cis_line_id: The CIS line unique identifier. E.g. CISLN001
    :type cis_line_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_cis_line_type_from_employer(request: web.Request, employer_id, cis_line_type_id, authorization, api_version) -> web.Response:
    """Get CIS line type from employer

    Gets the specified CIS line type from employer.

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param cis_line_type_id: The CIS line type unique identifier. E.g. TYPEA
    :type cis_line_type_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_cis_line_types_from_employer(request: web.Request, employer_id, authorization, api_version) -> web.Response:
    """Get CIS line types from employer.

    Get links to all CIS line types for the specified employer.

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_cis_line_types_with_tag_0(request: web.Request, employer_id, tag_id, authorization, api_version) -> web.Response:
    """Get CIS line types with tag

    Gets the CIS line type with the tag

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


async def get_cis_lines_from_sub_contractor(request: web.Request, employer_id, sub_contractor_id, authorization, api_version) -> web.Response:
    """Get CIS lines from sub contractor.

    Get links to all CIS lines for the specified sub contractor.

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


async def get_cis_lines_with_tag_0(request: web.Request, employer_id, sub_contractor_id, tag_id, authorization, api_version) -> web.Response:
    """Get CIS lines with tag

    Gets the CIS line with the tag

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param sub_contractor_id: The sub contractors&#39; unique identifier. E.g SUB001
    :type sub_contractor_id: str
    :param tag_id: The tag unique identifier. E.g. MyTag
    :type tag_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_cis_transaction_from_employer(request: web.Request, employer_id, cis_transaction_id, authorization, api_version) -> web.Response:
    """Get the CIS transaction

    Returns the specified CIS transaction

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param cis_transaction_id: The CIS transaction unique identifier. E.g. CISTRAN001
    :type cis_transaction_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_cis_transactions_from_employer(request: web.Request, employer_id, authorization, api_version) -> web.Response:
    """Get all CIS transactions for the employer

    Get links for all CIS transactions for the specified employer

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_sub_contractors_with_tag_0(request: web.Request, employer_id, tag_id, authorization, api_version) -> web.Response:
    """Get sub contractors with tag

    Gets the sub contractor with the tag

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


async def get_tag_from_cis_instruction_0(request: web.Request, employer_id, sub_contractor_id, cis_instruction_id, tag_id, authorization, api_version) -> web.Response:
    """Get CIS instruction tag

    Gets the tag from the CIS instruction

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param sub_contractor_id: The sub contractors&#39; unique identifier. E.g SUB001
    :type sub_contractor_id: str
    :param cis_instruction_id: The CIS instruction unique identifier. E.g. CIS001
    :type cis_instruction_id: str
    :param tag_id: The tag unique identifier. E.g. MyTag
    :type tag_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_tag_from_cis_line_0(request: web.Request, employer_id, sub_contractor_id, cis_line_id, tag_id, authorization, api_version) -> web.Response:
    """Get CIS line tag

    Gets the tag from the CIS line

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param sub_contractor_id: The sub contractors&#39; unique identifier. E.g SUB001
    :type sub_contractor_id: str
    :param cis_line_id: The CIS line unique identifier. E.g. CISLN001
    :type cis_line_id: str
    :param tag_id: The tag unique identifier. E.g. MyTag
    :type tag_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_tag_from_cis_line_type_0(request: web.Request, employer_id, cis_line_type_id, tag_id, authorization, api_version) -> web.Response:
    """Get CIS line type tag

    Gets the tag from the CIS line type

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param cis_line_type_id: The CIS line type unique identifier. E.g. TYPEA
    :type cis_line_type_id: str
    :param tag_id: The tag unique identifier. E.g. MyTag
    :type tag_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_tag_from_sub_contractor_0(request: web.Request, employer_id, sub_contractor_id, tag_id, authorization, api_version) -> web.Response:
    """Get sub contractor tag

    Gets the tag from the sub contractor

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param sub_contractor_id: The sub contractors&#39; unique identifier. E.g SUB001
    :type sub_contractor_id: str
    :param tag_id: The tag unique identifier. E.g. MyTag
    :type tag_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_tag_from_sub_contractor_revision_0(request: web.Request, employer_id, sub_contractor_id, tag_id, effective_date, authorization, api_version) -> web.Response:
    """Get sub contractor revision tag

    Gets the tag from the sub contractor revision

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param sub_contractor_id: The sub contractors&#39; unique identifier. E.g SUB001
    :type sub_contractor_id: str
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


async def get_tags_from_cis_instruction_0(request: web.Request, employer_id, sub_contractor_id, cis_instruction_id, authorization, api_version) -> web.Response:
    """Get all tags from the CIS instruction

    Gets all the tags from the CIS instruction

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param sub_contractor_id: The sub contractors&#39; unique identifier. E.g SUB001
    :type sub_contractor_id: str
    :param cis_instruction_id: The CIS instruction unique identifier. E.g. CIS001
    :type cis_instruction_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_tags_from_cis_line_0(request: web.Request, employer_id, sub_contractor_id, cis_line_id, authorization, api_version) -> web.Response:
    """Get all tags from the CIS line

    Gets all the tags from the CIS line

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param sub_contractor_id: The sub contractors&#39; unique identifier. E.g SUB001
    :type sub_contractor_id: str
    :param cis_line_id: The CIS line unique identifier. E.g. CISLN001
    :type cis_line_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_tags_from_cis_line_type_0(request: web.Request, employer_id, cis_line_type_id, authorization, api_version) -> web.Response:
    """Get all tags from the CIS line type

    Gets all the tags from the CIS line type

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param cis_line_type_id: The CIS line type unique identifier. E.g. TYPEA
    :type cis_line_type_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_tags_from_sub_contractor_0(request: web.Request, employer_id, sub_contractor_id, authorization, api_version) -> web.Response:
    """Get all tags from the sub contractor

    Gets all the tags from the sub contractor

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


async def get_tags_from_sub_contractor_revision_0(request: web.Request, employer_id, sub_contractor_id, effective_date, authorization, api_version) -> web.Response:
    """Get all sub contractor revision tags

    Gets all the tags from the sub contractor revision

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


async def patch_cis_instruction(request: web.Request, employer_id, sub_contractor_id, cis_instruction_id, authorization, api_version) -> web.Response:
    """Patches the CIS instruction

    Update an existing CIS instruction object

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param sub_contractor_id: The sub contractors&#39; unique identifier. E.g SUB001
    :type sub_contractor_id: str
    :param cis_instruction_id: The CIS instruction unique identifier. E.g. CIS001
    :type cis_instruction_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def post_cis_instruction_into_sub_contractor(request: web.Request, employer_id, sub_contractor_id, authorization, api_version, body) -> web.Response:
    """Create a new CIS instruction

    Create a new CIS instruction object

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param sub_contractor_id: The sub contractors&#39; unique identifier. E.g SUB001
    :type sub_contractor_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str
    :param body: The CIS instruction object.
    :type body: dict | bytes

    """
    body = CisInstruction.from_dict(body)
    return web.Response(status=200)


async def post_cis_line_type_into_employer(request: web.Request, employer_id, authorization, api_version, body) -> web.Response:
    """Create a new CIS line type

    Create a new CIS line type object

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str
    :param body: The CIS line type object.
    :type body: dict | bytes

    """
    body = CisLineType.from_dict(body)
    return web.Response(status=200)


async def put_cis_instruction_into_sub_contractor(request: web.Request, employer_id, sub_contractor_id, cis_instruction_id, authorization, api_version, body) -> web.Response:
    """Updates the CIS instruction

    Insert or update existing CIS instruction object

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param sub_contractor_id: The sub contractors&#39; unique identifier. E.g SUB001
    :type sub_contractor_id: str
    :param cis_instruction_id: The CIS instruction unique identifier. E.g. CIS001
    :type cis_instruction_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str
    :param body: The CIS instruction object.
    :type body: dict | bytes

    """
    body = CisInstruction.from_dict(body)
    return web.Response(status=200)


async def put_cis_instruction_tag_0(request: web.Request, employer_id, sub_contractor_id, cis_instruction_id, tag_id, authorization, api_version) -> web.Response:
    """Insert CIS instruction tag

    Inserts a new tag on the CIS instruction

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param sub_contractor_id: The sub contractors&#39; unique identifier. E.g SUB001
    :type sub_contractor_id: str
    :param cis_instruction_id: The CIS instruction unique identifier. E.g. CIS001
    :type cis_instruction_id: str
    :param tag_id: The tag unique identifier. E.g. MyTag
    :type tag_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def put_cis_line_tag_0(request: web.Request, employer_id, sub_contractor_id, cis_line_id, tag_id, authorization, api_version) -> web.Response:
    """Insert CIS line tag

    Inserts a new tag on the CIS line

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param sub_contractor_id: The sub contractors&#39; unique identifier. E.g SUB001
    :type sub_contractor_id: str
    :param cis_line_id: The CIS line unique identifier. E.g. CISLN001
    :type cis_line_id: str
    :param tag_id: The tag unique identifier. E.g. MyTag
    :type tag_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def put_cis_line_type_into_employer(request: web.Request, employer_id, cis_line_type_id, authorization, api_version, body) -> web.Response:
    """Updates the CIS line type

    Updates the existing specified CIS line type object

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param cis_line_type_id: The CIS line type unique identifier. E.g. TYPEA
    :type cis_line_type_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str
    :param body: The CIS line type object.
    :type body: dict | bytes

    """
    body = CisLineType.from_dict(body)
    return web.Response(status=200)


async def put_cis_line_type_tag_0(request: web.Request, employer_id, cis_line_type_id, tag_id, authorization, api_version) -> web.Response:
    """Insert CIS line type tag

    Inserts a new tag on the CIS line type

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param cis_line_type_id: The CIS line type unique identifier. E.g. TYPEA
    :type cis_line_type_id: str
    :param tag_id: The tag unique identifier. E.g. MyTag
    :type tag_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def put_sub_contractor_tag_0(request: web.Request, employer_id, sub_contractor_id, tag_id, authorization, api_version) -> web.Response:
    """Insert sub contractor tag

    Inserts a new tag on the sub contractor

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param sub_contractor_id: The sub contractors&#39; unique identifier. E.g SUB001
    :type sub_contractor_id: str
    :param tag_id: The tag unique identifier. E.g. MyTag
    :type tag_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)
