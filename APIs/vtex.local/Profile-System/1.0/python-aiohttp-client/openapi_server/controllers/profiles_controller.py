from typing import List, Dict
from aiohttp import web

from openapi_server.models.profile import Profile
from openapi_server.models.update_client_profile_request import UpdateClientProfileRequest
from openapi_server import util


async def create_client_profile(request: web.Request, content_type, accept, ttl=None, body=None) -> web.Response:
    """Create client profile

    Creates new client profile.    &gt; Since your store&#39;s profile schema is customizable, the schema and examples presented below may differ from yours. Your integration must be adapted accordingly.    &gt; The &#x60;id&#x60; field returned by this request is the &#x60;profileId&#x60; used to retrieve information on a specific profile later.    &gt; Learn more about the [Profile System](https://developers.vtex.com/vtex-rest-api/docs/profile-system) and its other API endpoints.

    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param ttl: This parameter sets the the Time To Live (TTL), in days, of the specific document being created or updated with this request. After this period of time from the moment of the request, the document is deleted. By sending this parameter you override the TTL set for the schema.    &gt; Currently, the available default document schemas have no TTL. This means that documents are stored indefinitely, unless a TTL is sent when creating or updating.
    :type ttl: int
    :param body: 
    :type body: dict | bytes

    """
    body = Profile.from_dict(body)
    return web.Response(status=200)


async def delete_client_profile(request: web.Request, content_type, accept, profile_id) -> web.Response:
    """Delete client profile

    Deletes a client profile by &#x60;profileId&#x60;.    &gt; Learn more about the [Profile System](https://developers.vtex.com/vtex-rest-api/docs/profile-system) and its other API endpoints.

    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param profile_id: ID of the client&#39;s profile as returned by the Create profile endpoint&#39;s response, in the &#x60;id&#x60; field. It can also be an &#x60;alternativeKey&#x60; according to your custom profile schema. In this case, this request should also send the &#x60;alternativeKey&#x60; parameter.
    :type profile_id: str

    """
    return web.Response(status=200)


async def get_profile(request: web.Request, content_type, accept, profile_id, alternative_key=None) -> web.Response:
    """Get profile

    Retrieves the information of a specific client, by its &#x60;profileId&#x60;.    &gt; Since your store&#39;s profile schema is customizable, the schema and examples presented below may differ from yours. Your integration must be adapted accordingly.    &gt; For security and privacy reasons, this request returns masked profile data. For unmasked information, see Get unmasked profile.    &gt; Learn more about the [Profile System](https://developers.vtex.com/vtex-rest-api/docs/profile-system) and its other API endpoints.

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


async def get_profile_by_version(request: web.Request, content_type, accept, profile_id, profile_version_id) -> web.Response:
    """Get profile by version

    Retrieves the information of a specific version of a client profile.    &gt; Since your store&#39;s profile schema is customizable, the schema and examples presented below may differ from yours. Your integration must be adapted accordingly.    &gt; For security and privacy reasons, this request returns masked profile data. For unmasked information, see Get unmasked profile by version.    &gt; Learn more about the [Profile System](https://developers.vtex.com/vtex-rest-api/docs/profile-system) and its other API endpoints.

    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param profile_id: ID of the client&#39;s profile as returned by the Create profile endpoint&#39;s response, in the &#x60;id&#x60; field. It can also be an &#x60;alternativeKey&#x60; according to your custom profile schema. In this case, this request should also send the &#x60;alternativeKey&#x60; parameter.
    :type profile_id: str
    :param profile_version_id: ID of the version of the client&#39;s profile as returned by endpoints that create or update profile information in the &#x60;version&#x60; field.
    :type profile_version_id: str

    """
    return web.Response(status=200)


async def get_unmasked_profile(request: web.Request, content_type, accept, profile_id, reason, alternative_key=None) -> web.Response:
    """Get unmasked profile

    Retrieves unmasked information of a specific client, by its &#x60;profileId&#x60;.    &gt; Since your store&#39;s profile schema is customizable, the schema and examples presented below may differ from yours. Your integration must be adapted accordingly.    &gt; Learn more about the [Profile System](https://developers.vtex.com/vtex-rest-api/docs/profile-system) and its other API endpoints.

    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param profile_id: ID of the client&#39;s profile as returned by the Create profile endpoint&#39;s response, in the &#x60;id&#x60; field. It can also be an &#x60;alternativeKey&#x60; according to your custom profile schema. In this case, this request should also send the &#x60;alternativeKey&#x60; parameter.
    :type profile_id: str
    :param reason: Reason for requesting unmasked data.
    :type reason: str
    :param alternative_key: The &#x60;profileId&#x60; path parameter may be substituted by other profile fields in this request. When making this request, send the &#x60;alternativeKey&#x60; parameter with a value equal to the key of the field you wish to use as &#x60;profileId&#x60;.    &gt; Currently, there are two possible values for this parameter: &#x60;email&#x60; and &#x60;document&#x60;.
    :type alternative_key: str

    """
    return web.Response(status=200)


async def get_unmasked_profile_by_version(request: web.Request, content_type, accept, profile_id, profile_version_id, reason) -> web.Response:
    """Get unmasked profile by version

    Retrieves unmasked information of a specific version of a client profile.    &gt; Since your store&#39;s profile schema is customizable, the schema and examples presented below may differ from yours. Your integration must be adapted accordingly.    &gt; Learn more about the [Profile System](https://developers.vtex.com/vtex-rest-api/docs/profile-system) and its other API endpoints.

    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param profile_id: ID of the client&#39;s profile as returned by the Create profile endpoint&#39;s response, in the &#x60;id&#x60; field. It can also be an &#x60;alternativeKey&#x60; according to your custom profile schema. In this case, this request should also send the &#x60;alternativeKey&#x60; parameter.
    :type profile_id: str
    :param profile_version_id: ID of the version of the client&#39;s profile as returned by endpoints that create or update profile information in the &#x60;version&#x60; field.
    :type profile_version_id: str
    :param reason: Reason for requesting unmasked data.
    :type reason: str

    """
    return web.Response(status=200)


async def update_client_profile(request: web.Request, content_type, accept, profile_id, alternative_key=None, ttl=None, body=None) -> web.Response:
    """Updates client profile

    Updates one or more fields of an existing client profile.    &gt; Since your store&#39;s profile schema is customizable, the schema and examples presented below may differ from yours. Your integration must be adapted accordingly.    &gt; Learn more about the [Profile System](https://developers.vtex.com/vtex-rest-api/docs/profile-system) and its other API endpoints.

    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param profile_id: ID of the client&#39;s profile as returned by the Create profile endpoint&#39;s response, in the &#x60;id&#x60; field. It can also be an &#x60;alternativeKey&#x60; according to your custom profile schema. In this case, this request should also send the &#x60;alternativeKey&#x60; parameter.
    :type profile_id: str
    :param alternative_key: The &#x60;profileId&#x60; path parameter may be substituted by other profile fields in this request. When making this request, send the &#x60;alternativeKey&#x60; parameter with a value equal to the key of the field you wish to use as &#x60;profileId&#x60;.    &gt; Currently, there are two possible values for this parameter: &#x60;email&#x60; and &#x60;document&#x60;.
    :type alternative_key: str
    :param ttl: This parameter sets the the Time To Live (TTL), in days, of the specific document being created or updated with this request. After this period of time from the moment of the request, the document is deleted. By sending this parameter you override the TTL set for the schema.    &gt; Currently, the available default document schemas have no TTL. This means that documents are stored indefinitely, unless a TTL is sent when creating or updating.
    :type ttl: int
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateClientProfileRequest.from_dict(body)
    return web.Response(status=200)
