from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def create_prospect(request: web.Request, content_type, accept, body=None) -> web.Response:
    """Create prospect

    Creates new prospect.    &gt; The &#x60;id&#x60; field returned by this request is the &#x60;prospectId&#x60; used to retrieve information on a specific prospect later.    &gt; Learn more about the [Profile System](https://developers.vtex.com/vtex-rest-api/docs/profile-system) and its other API endpoints.

    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param body: 
    :type body: 

    """
    return web.Response(status=200)


async def delete_prospect(request: web.Request, content_type, accept, prospect_id) -> web.Response:
    """Delete prospect

    Deletes a prospect by &#x60;prospectId&#x60;.    &gt; Learn more about the [Profile System](https://developers.vtex.com/vtex-rest-api/docs/profile-system) and its other API endpoints.

    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param prospect_id: ID of the prospect as returned by the Create prospect endpoint&#39;s response, in the &#x60;id&#x60; field.
    :type prospect_id: str

    """
    return web.Response(status=200)


async def get_prospect(request: web.Request, content_type, accept, prospect_id) -> web.Response:
    """Get prospect

    Retrieves the information of a specific prospect, by its &#x60;prospectId&#x60;.    &gt; For security and privacy reasons, this request returns masked prospect data. For unmasked information, see Get unmasked prospect.    &gt; Learn more about the [Profile System](https://developers.vtex.com/vtex-rest-api/docs/profile-system) and its other API endpoints.

    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param prospect_id: ID of the prospect as returned by the Create prospect endpoint&#39;s response, in the &#x60;id&#x60; field.
    :type prospect_id: str

    """
    return web.Response(status=200)


async def get_unmasked_prospect(request: web.Request, content_type, accept, prospect_id, reason) -> web.Response:
    """Get unmasked prospect

    Retrieves unmasked information of a specific prospect, by its &#x60;prospectId&#x60;.    &gt; Learn more about the [Profile System](https://developers.vtex.com/vtex-rest-api/docs/profile-system) and its other API endpoints.

    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param prospect_id: ID of the prospect as returned by the Create prospect endpoint&#39;s response, in the &#x60;id&#x60; field.
    :type prospect_id: str
    :param reason: Reason for requesting unmasked data.
    :type reason: str

    """
    return web.Response(status=200)


async def update_prospect(request: web.Request, content_type, accept, prospect_id, body=None) -> web.Response:
    """Update prospect

    Updates one or more fields of an existing prospect.    &gt; Learn more about the [Profile System](https://developers.vtex.com/vtex-rest-api/docs/profile-system) and its other API endpoints.

    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param prospect_id: ID of the prospect as returned by the Create prospect endpoint&#39;s response, in the &#x60;id&#x60; field.
    :type prospect_id: str
    :param body: 
    :type body: 

    """
    return web.Response(status=200)
