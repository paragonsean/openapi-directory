from typing import List, Dict
from aiohttp import web

from openapi_server.models.address import Address
from openapi_server.models.update_client_address_request import UpdateClientAddressRequest
from openapi_server import util


async def create_client_address(request: web.Request, content_type, accept, profile_id, alternative_key=None, body=None) -> web.Response:
    """Create client address

    Creates new address for a given client profile.    &gt; The &#x60;id&#x60; field returned by this request is the &#x60;addressId&#x60; used to retrieve or update information of a specific address later.    &gt; Learn more about the [Profile System](https://developers.vtex.com/vtex-rest-api/docs/profile-system) and its other API endpoints.

    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param profile_id: ID of the client&#39;s profile as returned by the Create profile endpoint&#39;s response, in the &#x60;id&#x60; field. It can also be an &#x60;alternativeKey&#x60; according to your custom profile schema. In this case, this request should also send the &#x60;alternativeKey&#x60; parameter.
    :type profile_id: str
    :param alternative_key: The &#x60;profileId&#x60; path parameter may be substituted by other profile fields in this request. When making this request, send the &#x60;alternativeKey&#x60; parameter with a value equal to the key of the field you wish to use as &#x60;profileId&#x60;.    &gt; Currently, there are two possible values for this parameter: &#x60;email&#x60; and &#x60;document&#x60;.
    :type alternative_key: str
    :param body: 
    :type body: dict | bytes

    """
    body = Address.from_dict(body)
    return web.Response(status=200)


async def delete_address(request: web.Request, content_type, accept, profile_id, address_id, alternative_key=None) -> web.Response:
    """Delete address

    Deletes a client&#39;s address by &#x60;profileId&#x60; and &#x60;addressId&#x60;.    &gt; Learn more about the [Profile System](https://developers.vtex.com/vtex-rest-api/docs/profile-system) and its other API endpoints.

    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param profile_id: ID of the client&#39;s profile as returned by the Create profile endpoint&#39;s response, in the &#x60;id&#x60; field. It can also be an &#x60;alternativeKey&#x60; according to your custom profile schema. In this case, this request should also send the &#x60;alternativeKey&#x60; parameter.
    :type profile_id: str
    :param address_id: ID of a client&#39;s specific address as returned in the Create client address endpoint&#39;s response, in the &#x60;id&#x60; field.
    :type address_id: str
    :param alternative_key: The &#x60;profileId&#x60; path parameter may be substituted by other profile fields in this request. When making this request, send the &#x60;alternativeKey&#x60; parameter with a value equal to the key of the field you wish to use as &#x60;profileId&#x60;.    &gt; Currently, there are two possible values for this parameter: &#x60;email&#x60; and &#x60;document&#x60;.
    :type alternative_key: str

    """
    return web.Response(status=200)


async def get_address(request: web.Request, content_type, accept, profile_id, address_id, alternative_key=None) -> web.Response:
    """Get address

    Retrieves information of a specific address of a given client, by its respectives &#x60;adderssId&#x60; and &#x60;profileId&#x60;.    &gt; For security and privacy reasons, this request returns masked address data. For unmasked information, see Get unmasked address.    &gt; Learn more about the [Profile System](https://developers.vtex.com/vtex-rest-api/docs/profile-system) and its other API endpoints.

    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param profile_id: ID of the client&#39;s profile as returned by the Create profile endpoint&#39;s response, in the &#x60;id&#x60; field. It can also be an &#x60;alternativeKey&#x60; according to your custom profile schema. In this case, this request should also send the &#x60;alternativeKey&#x60; parameter.
    :type profile_id: str
    :param address_id: ID of a client&#39;s specific address as returned in the Create client address endpoint&#39;s response, in the &#x60;id&#x60; field.
    :type address_id: str
    :param alternative_key: The &#x60;profileId&#x60; path parameter may be substituted by other profile fields in this request. When making this request, send the &#x60;alternativeKey&#x60; parameter with a value equal to the key of the field you wish to use as &#x60;profileId&#x60;.    &gt; Currently, there are two possible values for this parameter: &#x60;email&#x60; and &#x60;document&#x60;.
    :type alternative_key: str

    """
    return web.Response(status=200)


async def get_address_by_version(request: web.Request, content_type, accept, profile_id, address_id, address_version_id, reason, alternative_key=None) -> web.Response:
    """Get address by version

    Retrieves information of a specific version address of a given client.    &gt; For security and privacy reasons, this request returns masked address data by version. For unmasked information, see Get unmasked address by version.    &gt; Learn more about the [Profile System](https://developers.vtex.com/vtex-rest-api/docs/profile-system) and its other API endpoints.

    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param profile_id: ID of the client&#39;s profile as returned by the Create profile endpoint&#39;s response, in the &#x60;id&#x60; field. It can also be an &#x60;alternativeKey&#x60; according to your custom profile schema. In this case, this request should also send the &#x60;alternativeKey&#x60; parameter.
    :type profile_id: str
    :param address_id: ID of a client&#39;s specific address as returned in the Create client address endpoint&#39;s response, in the &#x60;id&#x60; field.
    :type address_id: str
    :param address_version_id: ID of the version of a given client&#39;s address as returned by endpoints that create or update address information in the &#x60;version&#x60; field.
    :type address_version_id: str
    :param reason: Reason for requesting unmasked data.
    :type reason: str
    :param alternative_key: The &#x60;profileId&#x60; path parameter may be substituted by other profile fields in this request. When making this request, send the &#x60;alternativeKey&#x60; parameter with a value equal to the key of the field you wish to use as &#x60;profileId&#x60;.    &gt; Currently, there are two possible values for this parameter: &#x60;email&#x60; and &#x60;document&#x60;.
    :type alternative_key: str

    """
    return web.Response(status=200)


async def get_client_addresses(request: web.Request, content_type, accept, profile_id, alternative_key=None) -> web.Response:
    """Get client addresses

    Retrieves information of all addresses of a given client, by its &#x60;profileId&#x60;.    &gt; For security and privacy reasons, this request returns masked address data. For unmasked information, see Get unmasked client addresses.    &gt; Learn more about the [Profile System](https://developers.vtex.com/vtex-rest-api/docs/profile-system) and its other API endpoints.

    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param profile_id: ID of the client&#39;s profile as returned by the Create profile endpoint&#39;s response, in the &#x60;id&#x60; field. It can also be an &#x60;alternativeKey&#x60; according to your custom profile schema. In this case, this request should also send the &#x60;alternativeKey&#x60; parameter.
    :type profile_id: str
    :param alternative_key: The &#x60;profileId&#x60; path parameter may be substituted by other profile fields in this request. When making this request, send the &#x60;alternativeKey&#x60; parameter with a value equal to the key of the field you wish to use as &#x60;profileId&#x60;.    &gt; Currently, there are two possible values for this parameter: &#x60;email&#x60; and &#x60;document&#x60;.
    :type alternative_key: str

    """
    return web.Response(status=200)


async def get_unmasked_address(request: web.Request, content_type, accept, profile_id, address_id, reason, alternative_key=None) -> web.Response:
    """Get unmasked address

    Retrieves unmasked information of a specific address of a given client, by its respectives &#x60;adderssId&#x60; and &#x60;profileId&#x60;.    &gt; Learn more about the [Profile System](https://developers.vtex.com/vtex-rest-api/docs/profile-system) and its other API endpoints.

    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param profile_id: ID of the client&#39;s profile as returned by the Create profile endpoint&#39;s response, in the &#x60;id&#x60; field. It can also be an &#x60;alternativeKey&#x60; according to your custom profile schema. In this case, this request should also send the &#x60;alternativeKey&#x60; parameter.
    :type profile_id: str
    :param address_id: ID of a client&#39;s specific address as returned in the Create client address endpoint&#39;s response, in the &#x60;id&#x60; field.
    :type address_id: str
    :param reason: Reason for requesting unmasked data.
    :type reason: str
    :param alternative_key: The &#x60;profileId&#x60; path parameter may be substituted by other profile fields in this request. When making this request, send the &#x60;alternativeKey&#x60; parameter with a value equal to the key of the field you wish to use as &#x60;profileId&#x60;.    &gt; Currently, there are two possible values for this parameter: &#x60;email&#x60; and &#x60;document&#x60;.
    :type alternative_key: str

    """
    return web.Response(status=200)


async def get_unmasked_address_by_version(request: web.Request, content_type, accept, profile_id, address_id, address_version_id, reason, alternative_key=None) -> web.Response:
    """Get unmasked address by version

    Retrieves unmasked information of a specific address version of a given client.    &gt; Learn more about the [Profile System](https://developers.vtex.com/vtex-rest-api/docs/profile-system) and its other API endpoints.

    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param profile_id: ID of the client&#39;s profile as returned by the Create profile endpoint&#39;s response, in the &#x60;id&#x60; field. It can also be an &#x60;alternativeKey&#x60; according to your custom profile schema. In this case, this request should also send the &#x60;alternativeKey&#x60; parameter.
    :type profile_id: str
    :param address_id: ID of a client&#39;s specific address as returned in the Create client address endpoint&#39;s response, in the &#x60;id&#x60; field.
    :type address_id: str
    :param address_version_id: ID of the version of a given client&#39;s address as returned by endpoints that create or update address information in the &#x60;version&#x60; field.
    :type address_version_id: str
    :param reason: Reason for requesting unmasked data.
    :type reason: str
    :param alternative_key: The &#x60;profileId&#x60; path parameter may be substituted by other profile fields in this request. When making this request, send the &#x60;alternativeKey&#x60; parameter with a value equal to the key of the field you wish to use as &#x60;profileId&#x60;.    &gt; Currently, there are two possible values for this parameter: &#x60;email&#x60; and &#x60;document&#x60;.
    :type alternative_key: str

    """
    return web.Response(status=200)


async def get_unmasked_client_addresses(request: web.Request, content_type, accept, profile_id, alternative_key=None) -> web.Response:
    """Get unmasked client addresses

    Retrieves unmasked information of all addresses of a given client, by its &#x60;profileId&#x60;.    &gt; Learn more about the [Profile System](https://developers.vtex.com/vtex-rest-api/docs/profile-system) and its other API endpoints.

    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param profile_id: ID of the client&#39;s profile as returned by the Create profile endpoint&#39;s response, in the &#x60;id&#x60; field. It can also be an &#x60;alternativeKey&#x60; according to your custom profile schema. In this case, this request should also send the &#x60;alternativeKey&#x60; parameter.
    :type profile_id: str
    :param alternative_key: The &#x60;profileId&#x60; path parameter may be substituted by other profile fields in this request. When making this request, send the &#x60;alternativeKey&#x60; parameter with a value equal to the key of the field you wish to use as &#x60;profileId&#x60;.    &gt; Currently, there are two possible values for this parameter: &#x60;email&#x60; and &#x60;document&#x60;.
    :type alternative_key: str

    """
    return web.Response(status=200)


async def update_client_address(request: web.Request, content_type, accept, profile_id, address_id, alternative_key=None, body=None) -> web.Response:
    """Update client address

    Updates one or more fields of an existing address for a given client profile.    &gt; Learn more about the [Profile System](https://developers.vtex.com/vtex-rest-api/docs/profile-system) and its other API endpoints.

    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param profile_id: ID of the client&#39;s profile as returned by the Create profile endpoint&#39;s response, in the &#x60;id&#x60; field. It can also be an &#x60;alternativeKey&#x60; according to your custom profile schema. In this case, this request should also send the &#x60;alternativeKey&#x60; parameter.
    :type profile_id: str
    :param address_id: ID of a client&#39;s specific address as returned in the Create client address endpoint&#39;s response, in the &#x60;id&#x60; field.
    :type address_id: str
    :param alternative_key: The &#x60;profileId&#x60; path parameter may be substituted by other profile fields in this request. When making this request, send the &#x60;alternativeKey&#x60; parameter with a value equal to the key of the field you wish to use as &#x60;profileId&#x60;.    &gt; Currently, there are two possible values for this parameter: &#x60;email&#x60; and &#x60;document&#x60;.
    :type alternative_key: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateClientAddressRequest.from_dict(body)
    return web.Response(status=200)
