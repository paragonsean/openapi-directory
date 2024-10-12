from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.invalid_error import InvalidError
from openapi_server.models.kyc_document2 import KycDocument2
from openapi_server.models.kyc_document_rejection import KycDocumentRejection
from openapi_server.models.kyc_request import KycRequest
from openapi_server.models.patch_kyc_request_request import PatchKycRequestRequest
from openapi_server.models.post_kyc_document_matches_request import PostKycDocumentMatchesRequest
from openapi_server import util


async def delete_kyc_request(request: web.Request, id, organization_id=None) -> web.Response:
    """Delete the KYC request

    Delete the KYC request with the predefined identifier string. 

    :param id: The resource identifier string.
    :type id: str
    :param organization_id: Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    :type organization_id: str

    """
    return web.Response(status=200)


async def get_kyc_document(request: web.Request, id, organization_id=None) -> web.Response:
    """Retrieve a KYC Document

    Retrieve a KYC document with specified identifier string.

    :param id: The resource identifier string.
    :type id: str
    :param organization_id: Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    :type organization_id: str

    """
    return web.Response(status=200)


async def get_kyc_document_collection(request: web.Request, organization_id=None, limit=None, offset=None, filter=None, sort=None) -> web.Response:
    """Retrieve a list of KYC documents

    Retrieve a list of KYC documents. 

    :param organization_id: Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    :type organization_id: str
    :param limit: The collection items limit.
    :type limit: int
    :param offset: The collection items offset.
    :type offset: int
    :param filter: The collection items filter requires a special format. Use \&quot;,\&quot; for multiple allowed values.  Use \&quot;;\&quot; for multiple fields. See the [filter guide](https://api-reference.rebilly.com/#section/Using-filter-with-collections) for more options and examples about this format. 
    :type filter: str
    :param sort: The collection items sort field and order (prefix with \&quot;-\&quot; for descending sort).
    :type sort: List[str]

    """
    return web.Response(status=200)


async def get_kyc_request(request: web.Request, id, organization_id=None) -> web.Response:
    """Retrieve a KYC request

    Retrieve a KYC request with specified identifier string.

    :param id: The resource identifier string.
    :type id: str
    :param organization_id: Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    :type organization_id: str

    """
    return web.Response(status=200)


async def get_kyc_request_collection(request: web.Request, organization_id=None, limit=None, offset=None, filter=None, sort=None) -> web.Response:
    """Retrieve a list of KYC requests

    Retrieve a list of KYC requests. 

    :param organization_id: Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    :type organization_id: str
    :param limit: The collection items limit.
    :type limit: int
    :param offset: The collection items offset.
    :type offset: int
    :param filter: The collection items filter requires a special format. Use \&quot;,\&quot; for multiple allowed values.  Use \&quot;;\&quot; for multiple fields. See the [filter guide](https://api-reference.rebilly.com/#section/Using-filter-with-collections) for more options and examples about this format. 
    :type filter: str
    :param sort: The collection items sort field and order (prefix with \&quot;-\&quot; for descending sort).
    :type sort: List[str]

    """
    return web.Response(status=200)


async def patch_kyc_request(request: web.Request, id, organization_id=None, body=None) -> web.Response:
    """Update a KYC request

    Update a KYC request.

    :param id: The resource identifier string.
    :type id: str
    :param organization_id: Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    :type organization_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = PatchKycRequestRequest.from_dict(body)
    return web.Response(status=200)


async def post_kyc_document(request: web.Request, body, organization_id=None) -> web.Response:
    """Create a KYC Document

    Create a KYC Document. 

    :param body: Kyc document resource.
    :type body: dict | bytes
    :param organization_id: Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    :type organization_id: str

    """
    body = KycDocument2.from_dict(body)
    return web.Response(status=200)


async def post_kyc_document_acceptance(request: web.Request, id, organization_id=None) -> web.Response:
    """Accept a KYC document

    Marks that status of the document as &#x60;accepted&#x60;. Updates the review time and reviewer information. Intended to be used for manual overrides. 

    :param id: The resource identifier string.
    :type id: str
    :param organization_id: Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    :type organization_id: str

    """
    return web.Response(status=200)


async def post_kyc_document_matches(request: web.Request, id, body, organization_id=None) -> web.Response:
    """Update a KYC document&#39;s documentMatches

    Updates a KYC document&#39;s documentMatches. Intended to be used for manual overrides. 

    :param id: The resource identifier string.
    :type id: str
    :param body: Kyc document resource.
    :type body: dict | bytes
    :param organization_id: Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    :type organization_id: str

    """
    body = PostKycDocumentMatchesRequest.from_dict(body)
    return web.Response(status=200)


async def post_kyc_document_rejection(request: web.Request, id, body, organization_id=None) -> web.Response:
    """Reject a KYC document

    Marks that status of the document as &#x60;rejected&#x60;. Updates the review time and reviewer information. Intended to be used for manual overrides. 

    :param id: The resource identifier string.
    :type id: str
    :param body: KYC document resource.
    :type body: dict | bytes
    :param organization_id: Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    :type organization_id: str

    """
    body = KycDocumentRejection.from_dict(body)
    return web.Response(status=200)


async def post_kyc_document_review(request: web.Request, id, organization_id=None) -> web.Response:
    """Review a KYC document

    Mark the KYC document as reviewed. Updates the review time and reviewer. information.

    :param id: The resource identifier string.
    :type id: str
    :param organization_id: Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    :type organization_id: str

    """
    return web.Response(status=200)


async def post_kyc_request(request: web.Request, body, organization_id=None) -> web.Response:
    """Create a KYC Request

    Create a KYC Request. 

    :param body: Kyc request resource.
    :type body: dict | bytes
    :param organization_id: Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    :type organization_id: str

    """
    body = KycRequest.from_dict(body)
    return web.Response(status=200)


async def put_kyc_document(request: web.Request, id, body, organization_id=None) -> web.Response:
    """Create or update a KYC document with predefined ID

    Create or update a KYC document with predefined identifier string.

    :param id: The resource identifier string.
    :type id: str
    :param body: KYC document resource.
    :type body: dict | bytes
    :param organization_id: Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    :type organization_id: str

    """
    body = KycDocument2.from_dict(body)
    return web.Response(status=200)
