from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_error import ApiError
from openapi_server.models.document import Document
from openapi_server.models.document_update import DocumentUpdate
from openapi_server.models.paginated_response_of_document import PaginatedResponseOfDocument
from openapi_server import util


async def create_document(request: web.Request, organization_id, id4n, content) -> web.Response:
    """Create an document for an id4n

    The documents&#39; mime type is suggested on octet-stream data. Otherwise the specified content mime type is used.

    :param organization_id: organizationId
    :type organization_id: str
    :param id4n: id4n
    :type id4n: str
    :param content: content
    :type content: str

    """
    return web.Response(status=200)


async def delete_document(request: web.Request, organization_id, id4n, file_name) -> web.Response:
    """Delete a document

    

    :param organization_id: organizationId
    :type organization_id: str
    :param id4n: id4n
    :type id4n: str
    :param file_name: fileName
    :type file_name: str

    """
    return web.Response(status=200)


async def get_document(request: web.Request, organization_id, id4n, file_name) -> web.Response:
    """Retrieve a document (meta-data only, no content)

    

    :param organization_id: organizationId
    :type organization_id: str
    :param id4n: id4n
    :type id4n: str
    :param file_name: fileName
    :type file_name: str

    """
    return web.Response(status=200)


async def get_public_document_0(request: web.Request, organization_id, id4n, file_name) -> web.Response:
    """Retrieve a public document (meta-data only, no content)

    

    :param organization_id: organizationId
    :type organization_id: str
    :param id4n: id4n
    :type id4n: str
    :param file_name: fileName
    :type file_name: str

    """
    return web.Response(status=200)


async def list_all_documents(request: web.Request, id4n, owner=None, offset=None, limit=None) -> web.Response:
    """List documents

    Listing all documents of an id4n

    :param id4n: id4n
    :type id4n: str
    :param owner: Filter by owner organization
    :type owner: str
    :param offset: Start with the n-th element
    :type offset: int
    :param limit: The maximum count of returned elements
    :type limit: int

    """
    return web.Response(status=200)


async def list_all_public_documents_0(request: web.Request, id4n, organization_id=None, owner=None, offset=None, limit=None) -> web.Response:
    """List public documents

    Listing all public documents of an id4n

    :param id4n: id4n
    :type id4n: str
    :param organization_id: organizationId
    :type organization_id: str
    :param owner: Filter by owner organization
    :type owner: str
    :param offset: Start with the n-th element
    :type offset: int
    :param limit: The maximum count of returned elements
    :type limit: int

    """
    return web.Response(status=200)


async def list_documents(request: web.Request, organization_id, id4n, owner=None, offset=None, limit=None) -> web.Response:
    """List organization specific documents

    Listing documents of an id4n seen by a specified organization

    :param organization_id: organizationId
    :type organization_id: str
    :param id4n: id4n
    :type id4n: str
    :param owner: Filter by owner organization
    :type owner: str
    :param offset: Start with the n-th element
    :type offset: int
    :param limit: The maximum count of returned elements
    :type limit: int

    """
    return web.Response(status=200)


async def put_document(request: web.Request, organization_id, id4n, content) -> web.Response:
    """Put an document for an id4n

    Creating or overwriting an existing document 

    :param organization_id: organizationId
    :type organization_id: str
    :param id4n: id4n
    :type id4n: str
    :param content: content
    :type content: str

    """
    return web.Response(status=200)


async def read_document(request: web.Request, organization_id, id4n, file_name) -> web.Response:
    """Read document contents

    

    :param organization_id: organizationId
    :type organization_id: str
    :param id4n: id4n
    :type id4n: str
    :param file_name: fileName
    :type file_name: str

    """
    return web.Response(status=200)


async def read_from_microstorage(request: web.Request, organization, id4n) -> web.Response:
    """Read data from microstorage

    

    :param organization: organization
    :type organization: str
    :param id4n: id4n
    :type id4n: str

    """
    return web.Response(status=200)


async def read_public_document_0(request: web.Request, organization_id, id4n, file_name) -> web.Response:
    """Read public document contents

    

    :param organization_id: organizationId
    :type organization_id: str
    :param id4n: id4n
    :type id4n: str
    :param file_name: fileName
    :type file_name: str

    """
    return web.Response(status=200)


async def update_document_metadata(request: web.Request, organization_id, id4n, file_name, body) -> web.Response:
    """Update a document

    

    :param organization_id: organizationId
    :type organization_id: str
    :param id4n: id4n
    :type id4n: str
    :param file_name: fileName
    :type file_name: str
    :param body: document
    :type body: dict | bytes

    """
    body = DocumentUpdate.from_dict(body)
    return web.Response(status=200)


async def write_to_microstorage(request: web.Request, organization, id4n, content_type=None, content_length=None, body=None) -> web.Response:
    """Write data to microstorage

    

    :param organization: organization
    :type organization: str
    :param id4n: id4n
    :type id4n: str
    :param content_type: Content-Type
    :type content_type: str
    :param content_length: Content-Length
    :type content_length: int
    :param body: body
    :type body: str

    """
    return web.Response(status=200)
