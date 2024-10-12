from typing import List, Dict
from aiohttp import web

from openapi_server.models.list_supporting_document_response import ListSupportingDocumentResponse
from openapi_server.models.numbers_v2_regulatory_compliance_supporting_document import NumbersV2RegulatoryComplianceSupportingDocument
from openapi_server import util


async def create_supporting_document(request: web.Request, friendly_name, type, attributes=None) -> web.Response:
    """create_supporting_document

    Create a new Supporting Document.

    :param friendly_name: The string that you assigned to describe the resource.
    :type friendly_name: str
    :param type: The type of the Supporting Document.
    :type type: str
    :param attributes: The set of parameters that are the attributes of the Supporting Documents resource which are derived Supporting Document Types.
    :type attributes: dict | bytes

    """
    attributes = object.from_dict(attributes)
    return web.Response(status=200)


async def delete_supporting_document(request: web.Request, sid) -> web.Response:
    """delete_supporting_document

    Delete a specific Supporting Document.

    :param sid: The unique string created by Twilio to identify the Supporting Document resource.
    :type sid: str

    """
    return web.Response(status=200)


async def fetch_supporting_document(request: web.Request, sid) -> web.Response:
    """fetch_supporting_document

    Fetch specific Supporting Document Instance.

    :param sid: The unique string created by Twilio to identify the Supporting Document resource.
    :type sid: str

    """
    return web.Response(status=200)


async def list_supporting_document(request: web.Request, page_size=None, page=None, page_token=None) -> web.Response:
    """list_supporting_document

    Retrieve a list of all Supporting Document for an account.

    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)


async def update_supporting_document(request: web.Request, sid, attributes=None, friendly_name=None) -> web.Response:
    """update_supporting_document

    Update an existing Supporting Document.

    :param sid: The unique string created by Twilio to identify the Supporting Document resource.
    :type sid: str
    :param attributes: The set of parameters that are the attributes of the Supporting Document resource which are derived Supporting Document Types.
    :type attributes: dict | bytes
    :param friendly_name: The string that you assigned to describe the resource.
    :type friendly_name: str

    """
    attributes = object.from_dict(attributes)
    return web.Response(status=200)
