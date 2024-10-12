from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.invalid_error import InvalidError
from openapi_server.models.post_tag_customer_collection_request import PostTagCustomerCollectionRequest
from openapi_server.models.tag import Tag
from openapi_server import util


async def delete_tag(request: web.Request, tag, organization_id=None) -> web.Response:
    """Delete a tag

    Delete a tag. It&#39;s an asynchronous operation. 

    :param tag: The tag name.
    :type tag: str
    :param organization_id: Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    :type organization_id: str

    """
    return web.Response(status=200)


async def delete_tag_customer(request: web.Request, tag, customer_id, organization_id=None) -> web.Response:
    """Untag a customer

    Untag a customer. 

    :param tag: The tag name.
    :type tag: str
    :param customer_id: The customer identifier string.
    :type customer_id: str
    :param organization_id: Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    :type organization_id: str

    """
    return web.Response(status=200)


async def delete_tag_customer_collection(request: web.Request, tag, body, organization_id=None) -> web.Response:
    """Untag a list of customers

    Untag a list of customers. If the customer from the list is already untagged it will be ignored. It&#39;s an asynchronous operation. 

    :param tag: The tag name.
    :type tag: str
    :param body: 
    :type body: dict | bytes
    :param organization_id: Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    :type organization_id: str

    """
    body = PostTagCustomerCollectionRequest.from_dict(body)
    return web.Response(status=200)


async def get_tag(request: web.Request, tag, organization_id=None) -> web.Response:
    """Retrieve a tag

    Retrieve a tag. 

    :param tag: The tag name.
    :type tag: str
    :param organization_id: Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    :type organization_id: str

    """
    return web.Response(status=200)


async def get_tag_collection(request: web.Request, organization_id=None, limit=None, offset=None, filter=None, q=None, sort=None) -> web.Response:
    """Retrieve a list of tags

    Retrieve a list of tags. 

    :param organization_id: Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    :type organization_id: str
    :param limit: The collection items limit.
    :type limit: int
    :param offset: The collection items offset.
    :type offset: int
    :param filter: The collection items filter requires a special format. Use \&quot;,\&quot; for multiple allowed values.  Use \&quot;;\&quot; for multiple fields. See the [filter guide](https://api-reference.rebilly.com/#section/Using-filter-with-collections) for more options and examples about this format. 
    :type filter: str
    :param q: The partial search of the text fields.
    :type q: str
    :param sort: The collection items sort field and order (prefix with \&quot;-\&quot; for descending sort).
    :type sort: List[str]

    """
    return web.Response(status=200)


async def patch_tag(request: web.Request, tag, body, organization_id=None) -> web.Response:
    """Update a tag

    Update a tag. 

    :param tag: The tag name.
    :type tag: str
    :param body: Tag resource.
    :type body: dict | bytes
    :param organization_id: Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    :type organization_id: str

    """
    body = Tag.from_dict(body)
    return web.Response(status=200)


async def post_tag(request: web.Request, body, organization_id=None) -> web.Response:
    """Create a tag

    Create a tag. 

    :param body: Tag resource.
    :type body: dict | bytes
    :param organization_id: Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    :type organization_id: str

    """
    body = Tag.from_dict(body)
    return web.Response(status=200)


async def post_tag_customer(request: web.Request, tag, customer_id, organization_id=None) -> web.Response:
    """Tag a customer

    Tag a customer. 

    :param tag: The tag name.
    :type tag: str
    :param customer_id: The customer identifier string.
    :type customer_id: str
    :param organization_id: Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    :type organization_id: str

    """
    return web.Response(status=200)


async def post_tag_customer_collection(request: web.Request, tag, body, organization_id=None) -> web.Response:
    """Tag a list of customers

    Tag a list of customers. If the customer from the list is already tagged it will be ignored. It&#39;s an asynchronous operation. 

    :param tag: The tag name.
    :type tag: str
    :param body: 
    :type body: dict | bytes
    :param organization_id: Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    :type organization_id: str

    """
    body = PostTagCustomerCollectionRequest.from_dict(body)
    return web.Response(status=200)
