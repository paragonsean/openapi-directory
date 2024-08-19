from typing import List, Dict
from aiohttp import web

from openapi_server.models.acl_list_collection_output import AclListCollectionOutput
from openapi_server.models.address import Address
from openapi_server.models.body_change_status_of_the_allowlist_v1_allowlist_public_allowlist_id_put import BodyChangeStatusOfTheAllowlistV1AllowlistPublicAllowlistIdPut
from openapi_server.models.body_change_status_of_the_origin_allowlist_v1_allowlist_private_allowlist_id_origin_put import BodyChangeStatusOfTheOriginAllowlistV1AllowlistPrivateAllowlistIdOriginPut
from openapi_server.models.body_change_status_of_the_origin_allowlist_v1_allowlist_public_allowlist_id_origin_put import BodyChangeStatusOfTheOriginAllowlistV1AllowlistPublicAllowlistIdOriginPut
from openapi_server.models.body_create_private_allowlist_of_the_user_v1_allowlist_private_post import BodyCreatePrivateAllowlistOfTheUserV1AllowlistPrivatePost
from openapi_server.models.body_update_private_allowlist_of_the_user_v1_allowlist_private_allowlist_id_put import BodyUpdatePrivateAllowlistOfTheUserV1AllowlistPrivateAllowlistIdPut
from openapi_server.models.body_update_private_content_of_the_allowlist_of_the_user_v1_allowlist_private_allowlist_id_content_put import BodyUpdatePrivateContentOfTheAllowlistOfTheUserV1AllowlistPrivateAllowlistIdContentPut
from openapi_server.models.http_validation_error import HTTPValidationError
from openapi_server.models.private_acl_group_list_collection_output import PrivateAclGroupListCollectionOutput
from openapi_server.models.private_acl_group_list_output import PrivateAclGroupListOutput
from openapi_server.models.private_acl_list_collection_output import PrivateAclListCollectionOutput
from openapi_server.models.public_acl_group_list_collection_output import PublicAclGroupListCollectionOutput
from openapi_server.models.public_acl_group_list_output import PublicAclGroupListOutput
from openapi_server import util


async def change_status_of_the_allowlist_v1_allowlist_public_allowlist_id_put(request: web.Request, allowlist_id, body) -> web.Response:
    """Toogle the status of an allow list.

    ### What Change the status of an allow list to &#x60;&#x60;ACTIVE&#x60;&#x60; or &#x60;&#x60;INACTIVE&#x60;&#x60;. An &#x60;&#x60;INACTIVE&#x60;&#x60; list will not be used by the service. An &#x60;&#x60;ACTIVE&#x60;&#x60; list will be used by the service. As an optional parameter it can be provided an &#x60;&#x60;expiry&#x60;&#x60; date in seconds since epoch. If not provided, the list will never expire.   This is an asynchronous operation. It can take several seconds until the operation completes, but the request will  immediately return a 202 Accepted response.  ### Parameters In the query string the ID of the allow list to change the status. In the body the JSON object with the following fields: - &#x60;&#x60;status&#x60;&#x60;: The status of the list. It can be &#x60;&#x60;ACTIVE&#x60;&#x60; or &#x60;&#x60;INACTIVE&#x60;&#x60;. - &#x60;&#x60;expiry&#x60;&#x60;: Unix timestamp in seconds when the list will expire. If it does not exist, it will never expire.  ### Result It should always return a 202 Accepted response with an empty body.  ### Errors  If the list does not exist, it will return a 404 error. If the status is not &#x60;&#x60;ACTIVE&#x60;&#x60; or &#x60;&#x60;INACTIVE&#x60;&#x60;, it will return a 422 error. If the expiry is not a valid timestamp, it will return a 422 error. If the allow list is not a valid UUID, it will return a 422 error.  It will return the API Global errors described in the API description.

    :param allowlist_id: 
    :type allowlist_id: str
    :type allowlist_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = BodyChangeStatusOfTheAllowlistV1AllowlistPublicAllowlistIdPut.from_dict(body)
    return web.Response(status=200)


async def change_status_of_the_origin_allowlist_v1_allowlist_private_allowlist_id_origin_put(request: web.Request, allowlist_id, body) -> web.Response:
    """Toogle the status of the origin in an allow list.

    ### What Change the status of the origin of an allow list to &#x60;&#x60;ACTIVE&#x60;&#x60;, &#x60;&#x60;INACTIVE&#x60;&#x60; or &#x60;&#x60;DELETED&#x60;&#x60;.  An &#x60;&#x60;ACTIVE&#x60;&#x60; origin will apply the allow list to the protocol and domain of the origin. An origin can be created and activated simply toogling the &#x60;&#x60;ACTIVE&#x60;&#x60; status. As an optional parameter it can be provided an &#x60;&#x60;ttl&#x60;&#x60; or Time To Live parameter of the origin in the list in seconds. After the TTL expires, the origin will be removed from the list.  If the TTL is not provided, the origin will never expire.  An &#x60;&#x60;INACTIVE&#x60;&#x60; origin will not apply the allow list to the protocol and domain of the origin.  A &#x60;&#x60;DELETED&#x60;&#x60; origin will be removed from the list. It will not be used by the service anymore. The user can activate it again with the &#x60;&#x60;ACTIVE&#x60;&#x60; status.  This is an asynchronous operation. It can take several seconds until the operation completes, but the request will  immediately return a 202 Accepted response.  *This operation is not available in the Freemium plan.*  ### Parameters In the query string the ID of the allow list to change the status. In the body the JSON object with the following fields: - &#x60;&#x60;origin&#x60;&#x60;: The protocol and domain of the origin. It can be &#x60;&#x60;http://example.com&#x60;&#x60; or &#x60;&#x60;https://example.com&#x60;&#x60;. - &#x60;&#x60;status&#x60;&#x60;: The status of the list. It can be &#x60;&#x60;ACTIVE&#x60;&#x60;, &#x60;&#x60;INACTIVE&#x60;&#x60; or &#x60;&#x60;DELETED&#x60;&#x60;.  ### Result It should always return a 202 Accepted response with an empty body.  ### Errors  If the list does not exist, it will return a 404 error. If the status is not &#x60;&#x60;ACTIVE&#x60;&#x60; or &#x60;&#x60;INACTIVE&#x60;&#x60;, it will return a 422 error. If the TTL is negative in the past, it will return a 422 error. If the allow list is not a valid UUID, it will return a 422 error. If the origin is not a valid URL, it will return a 400 error. If the allowlist is not active, it will returna 409 error. If the origin is not found in the set owned by the user, it will return a 404 error.  It will return the API Global errors described in the API description.

    :param allowlist_id: 
    :type allowlist_id: str
    :type allowlist_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = BodyChangeStatusOfTheOriginAllowlistV1AllowlistPrivateAllowlistIdOriginPut.from_dict(body)
    return web.Response(status=200)


async def change_status_of_the_origin_allowlist_v1_allowlist_public_allowlist_id_origin_put(request: web.Request, allowlist_id, body) -> web.Response:
    """Toogle the status of the origin in an allow list.

    ### What Change the status of the origin of an allow list to &#x60;&#x60;ACTIVE&#x60;&#x60;, &#x60;&#x60;INACTIVE&#x60;&#x60; or &#x60;&#x60;DELETED&#x60;&#x60;.  An &#x60;&#x60;ACTIVE&#x60;&#x60; origin will apply the allow list to the protocol and domain of the origin. An origin can be created and activated simply toogling the &#x60;&#x60;ACTIVE&#x60;&#x60; status. As an optional parameter it can be provided an &#x60;&#x60;ttl&#x60;&#x60; or Time To Live parameter of the origin in the list in seconds. After the TTL expires, the origin will be removed from the list.  If the TTL is not provided, the origin will never expire.  An &#x60;&#x60;INACTIVE&#x60;&#x60; origin will not apply the allow list to the protocol and domain of the origin.  A &#x60;&#x60;DELETED&#x60;&#x60; origin will be removed from the list. It will not be used by the service anymore. The user can activate it again with the &#x60;&#x60;ACTIVE&#x60;&#x60; status.  This is an asynchronous operation. It can take several seconds until the operation completes, but the request will  immediately return a 202 Accepted response.  *This operation is not available in the Freemium plan.*  ### Parameters In the query string the ID of the allow list to change the status. In the body the JSON object with the following fields: - &#x60;&#x60;origin&#x60;&#x60;: The protocol and domain of the origin. It can be &#x60;&#x60;http://example.com&#x60;&#x60; or &#x60;&#x60;https://example.com&#x60;&#x60;. - &#x60;&#x60;status&#x60;&#x60;: The status of the list. It can be &#x60;&#x60;ACTIVE&#x60;&#x60;, &#x60;&#x60;INACTIVE&#x60;&#x60; or &#x60;&#x60;DELETED&#x60;&#x60;.  ### Result It should always return a 202 Accepted response with an empty body.  ### Errors  If the list does not exist, it will return a 404 error. If the status is not &#x60;&#x60;ACTIVE&#x60;&#x60; or &#x60;&#x60;INACTIVE&#x60;&#x60;, it will return a 422 error. If the TTL is negative in the past, it will return a 422 error. If the allow list is not a valid UUID, it will return a 422 error. If the origin is not a valid URL, it will return a 400 error. If the allowlist is not active, it will returna 409 error. If the origin is not found in the set owned by the user, it will return a 404 error.  It will return the API Global errors described in the API description.

    :param allowlist_id: 
    :type allowlist_id: str
    :type allowlist_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = BodyChangeStatusOfTheOriginAllowlistV1AllowlistPublicAllowlistIdOriginPut.from_dict(body)
    return web.Response(status=200)


async def create_private_allowlist_of_the_user_v1_allowlist_private_post(request: web.Request, body) -> web.Response:
    """Creates a new private allowlist binded to the user.

    ### What Creates a new allowlist with the information given and binded to the current user. The parameters are:  - name  - description  - tags  - expiry  - Time to Live (TTL)  - Resource Type (&#x60;CIDR&#x60;, &#x60;AS&#x60;, &#x60;COUNTRY&#x60;, &#x60;CONTINENT&#x60;, &#x60;DATACENTER_ID&#x60; and &#x60;USER AGENT&#x60;)  This is an asynchronous operation. It can take several seconds until the operation completes, but the request will immediately return a 202 Accepted response. The operation will also return the UUID of the list.  ### Parameters In the query string the ID of the private allow list to delete.  In the body the following parameters: - &#x60;&#x60;name&#x60;&#x60;: A human readable name of the list. - &#x60;&#x60;description&#x60;&#x60;: A long detailed information about what the list contains and how it is used. - &#x60;&#x60;tags&#x60;&#x60;: A list of tags that describe the list. - &#x60;&#x60;ttl&#x60;&#x60;: (Optional) The Time To Live of the list, in seconds. If it does not exist, it will never expire. - &#x60;&#x60;resource_type&#x60;&#x60;: The type of resource that the list contains. It can be &#x60;&#x60;CIDR&#x60;&#x60;, &#x60;&#x60;AS&#x60;&#x60;, &#x60;&#x60;COUNTRY&#x60;&#x60;, &#x60;&#x60;CONTINENT&#x60;&#x60;,    &#x60;&#x60;DATACENTER_ID&#x60;&#x60; or &#x60;&#x60;USER AGENT&#x60;&#x60;.  ### Result It should always return a 202 Accepted response with the UUID of the new list in the body.  ### Errors  - If the information is not valid, it will return a &#x60;422&#x60; (Unprocessable Entity) error. - If the ttl is negative, it will return a &#x60;400&#x60; (Bad Request) error.  It will return the API Global errors described in the API description.

    :param body: 
    :type body: dict | bytes

    """
    body = BodyCreatePrivateAllowlistOfTheUserV1AllowlistPrivatePost.from_dict(body)
    return web.Response(status=200)


async def delete_the_allowlist_content_v1_allowlist_private_allowlist_id_content_delete(request: web.Request, allowlist_id) -> web.Response:
    """Delete all the content of a private allowlist of the user.

    ### What Delete all the content of a private allowlist of the user. This will remove all the elements, and there is no way to recover them.  ### Parameters Pass the private allowlist ID as query parameter.  ### Result If successful, it will return a &#x60;&#x60;202&#x60;&#x60; (Accepted) response with an empty body. The operation is asynchronous,and can take several seconds to complete.  ### Errors  - If the allow list is not a valid UUID, it will return a &#x60;&#x60;422&#x60;&#x60; (Unprocessable Entity) error. - If the private allowlist ID does not exist, it will return a &#x60;&#x60;404&#x60;&#x60; (Not found) error.  It will also return the API Global errors described in the API description.

    :param allowlist_id: 
    :type allowlist_id: str
    :type allowlist_id: str

    """
    return web.Response(status=200)


async def delete_the_allowlist_v1_allowlist_private_allowlist_id_delete(request: web.Request, allowlist_id) -> web.Response:
    """Delete all the bindings between a user and a private allowlist.

    ### What Delete all the bindings between a user and a private allowlist. This will remove the content of the allowlist, the allowlist from the user and also all the origins that are using the allowlist.  This is an asynchronous operation. It can take several seconds until the operation completes, but the request willimmediately return a 202 Accepted response.  ### Parameters In the query string the ID of the private allow list to delete.  ### Result It should always return a 202 Accepted response with an empty body.  ### Errors  - If the list does not exist, it will return a 404 error. - If the allow list is not a valid UUID, it will return a 422 error.  It will return the API Global errors described in the API description.

    :param allowlist_id: 
    :type allowlist_id: str
    :type allowlist_id: str

    """
    return web.Response(status=200)


async def delete_the_allowlist_v1_allowlist_public_allowlist_id_delete(request: web.Request, allowlist_id) -> web.Response:
    """Delete all the bindings between a user and an allowlist.

    ### What Delete all the bindings between a user and an allowlist. This will remove the allowlist from the user and also all the origins that are using the allowlist.   This is an asynchronous operation. It can take several seconds until the operation completes, but the request will  immediately return a 202 Accepted response.  ### Parameters In the query string the ID of the allow list to change the status.  ### Result It should always return a 202 Accepted response with an empty body.  ### Errors  If the list does not exist, it will return a 404 error. If the allow list is not a valid UUID, it will return a 422 error.  It will return the API Global errors described in the API description.

    :param allowlist_id: 
    :type allowlist_id: str
    :type allowlist_id: str

    """
    return web.Response(status=200)


async def get_all_owned_allowlists_by_resource_type_v1_allowlist_public_owned_resource_type_get(request: web.Request, resource_type) -> web.Response:
    """Get the set of public allowlists of a user by resource type.

    ### What Obtain the set of public allow lists selected by the user and wich ones are not filtering by the resource type.  ### Parameters The &#x60;&#x60;resource type&#x60;&#x60; to filter. The values can be &#x60;&#x60;CIDR&#x60;&#x60;, &#x60;&#x60;AS&#x60;&#x60;, &#x60;&#x60;COUNTRY&#x60;&#x60;, &#x60;&#x60;CONTINENT&#x60;&#x60; or &#x60;&#x60;DATACENTER_ID&#x60;&#x60;.  ### Result The result is a JSON object with a list of the following JSON objects: - &#x60;&#x60;self&#x60;&#x60;: the URI to the status of all the lists. - &#x60;&#x60;lists&#x60;&#x60;: a list of JSON objects with the available lists:     - &#x60;&#x60;self&#x60;&#x60;: the URI to individual information of the list.     - &#x60;&#x60;name&#x60;&#x60;: A human readable name of the list.     - &#x60;&#x60;description&#x60;&#x60;: A long detailed information about what the list contains and how it is used.     - &#x60;&#x60;resource_type&#x60;&#x60;: The type of the list. It can be &#x60;&#x60;CIDR&#x60;&#x60;, &#x60;&#x60;AS&#x60;&#x60;, &#x60;&#x60;COUNTRY&#x60;&#x60;, &#x60;&#x60;CONTINENT&#x60;&#x60; or &#x60;&#x60;DATACENTER_ID&#x60;&#x60;.     - &#x60;&#x60;list_type&#x60;&#x60;: The type of the list. It can be &#x60;&#x60;ALLOW&#x60;&#x60; or &#x60;&#x60;DENY&#x60;&#x60;.     - &#x60;&#x60;status&#x60;&#x60;: The status of the list. It can be &#x60;&#x60;ACTIVE&#x60;&#x60; or &#x60;&#x60;INACTIVE&#x60;&#x60; or &#x60;&#x60;EXPIRED&#x60;&#x60;. If the list is &#x60;&#x60;EXPIRED&#x60;&#x60;    it means that the list is not available anymore if not renewed.     - &#x60;&#x60;created_at&#x60;&#x60;: Unix timestamp in seconds when the list was created.     - &#x60;&#x60;updated_at&#x60;&#x60;: Unix timestamp in seconds when the list was updated.     - &#x60;&#x60;expiry&#x60;&#x60;: Unix timestamp in seconds when the list will expire. If it does not exist, it will never expire.     - &#x60;&#x60;origins&#x60;&#x60;: list of websites that are using the list as an allowlist.         - &#x60;&#x60;self&#x60;&#x60;: the URI to all the list of origins.         - &#x60;&#x60;lists&#x60;&#x60;: list of lists that the origin is using.             - &#x60;&#x60;self&#x60;&#x60;: the URI to the individual information of the list.             - &#x60;&#x60;origin&#x60;&#x60;: the protocol and domain of the website that is using the list.             - &#x60;&#x60;status&#x60;&#x60;: the status of the list. It can be &#x60;&#x60;ACTIVE&#x60;&#x60; or &#x60;&#x60;INACTIVE&#x60;&#x60; or &#x60;&#x60;EXPIRED&#x60;&#x60;. If the list is &#x60;&#x60;EXPIRED&#x60;&#x60;            it means that the list is not available anymore if not renewed.             - &#x60;&#x60;expiry&#x60;&#x60;: Unix timestamp in seconds when the list will expire. If it does not exist, it will never expire.             - &#x60;&#x60;created_at&#x60;&#x60;: Unix timestamp in seconds when the list was created.             - &#x60;&#x60;updated_at&#x60;&#x60;: Unix timestamp in seconds when the list was updated.  ### Errors  It will return the API Global errors described in the API description.

    :param resource_type: 
    :type resource_type: str

    """
    return web.Response(status=200)


async def get_all_private_allowlists_by_resource_type_v1_allowlist_private_all_resource_type_get(request: web.Request, resource_type) -> web.Response:
    """Get the set of private allowlists of the user by resource type.

    ### What Obtain the set of private allow lists of the user available in the service filtering by resource type. It can be &#x60;&#x60;CIDR&#x60;&#x60;, &#x60;&#x60;AS&#x60;&#x60;, &#x60;&#x60;COUNTRY&#x60;&#x60;, &#x60;&#x60;CONTINENT&#x60;&#x60; or &#x60;&#x60;DATACENTER_ID&#x60;&#x60;  ### Parameters The &#x60;&#x60;resource type&#x60;&#x60; to filter. The values can be &#x60;&#x60;CIDR&#x60;&#x60;, &#x60;&#x60;AS&#x60;&#x60;, &#x60;&#x60;COUNTRY&#x60;&#x60;, &#x60;&#x60;CONTINENT&#x60;&#x60; or &#x60;&#x60;DATACENTER_ID&#x60;&#x60;.  ### Result The result is a JSON object with a list of the following JSON objects: - &#x60;&#x60;self&#x60;&#x60;: the URI to the status of all the lists. - &#x60;&#x60;lists&#x60;&#x60;: a list of JSON objects with the available lists:     - &#x60;&#x60;self&#x60;&#x60;: the URI to individual information of the list.     - &#x60;&#x60;name&#x60;&#x60;: A human readable name of the list.     - &#x60;&#x60;description&#x60;&#x60;: A long detailed information about what the list contains and how it is used.     - &#x60;&#x60;resource_type&#x60;&#x60;: The type of the list. It can be &#x60;&#x60;CIDR&#x60;&#x60;, &#x60;&#x60;AS&#x60;&#x60;, &#x60;&#x60;COUNTRY&#x60;&#x60;, &#x60;&#x60;CONTINENT&#x60;&#x60; or &#x60;&#x60;DATACENTER_ID&#x60;&#x60;.     - &#x60;&#x60;list_type&#x60;&#x60;: The type of the list. It can be &#x60;&#x60;ALLOW&#x60;&#x60; or &#x60;&#x60;DENY&#x60;&#x60;.     - &#x60;&#x60;created_at&#x60;&#x60;: Unix timestamp in seconds when the list was created.     - &#x60;&#x60;updated_at&#x60;&#x60;: Unix timestamp in seconds when the list was updated.     - &#x60;&#x60;expiry&#x60;&#x60;: Unix timestamp in seconds when the list will expire. If it does not exist, it will never expire.     - &#x60;&#x60;origins&#x60;&#x60;: list of websites that are using the list as a allowlist.         - &#x60;&#x60;self&#x60;&#x60;: the URI to all the list of origins.         - &#x60;&#x60;lists&#x60;&#x60;: list of lists that the origin is using.             - &#x60;&#x60;self&#x60;&#x60;: the URI to the individual information of the list.             - &#x60;&#x60;origin&#x60;&#x60;: the protocol and domain of the website that is using the list.             - &#x60;&#x60;status&#x60;&#x60;: the status of the list. It can be &#x60;&#x60;ACTIVE&#x60;&#x60; or &#x60;&#x60;INACTIVE&#x60;&#x60; or &#x60;&#x60;EXPIRED&#x60;&#x60;. If the list is &#x60;&#x60;EXPIRED&#x60;&#x60; it means that the list is not available anymore if not renewed.             - &#x60;&#x60;expiry&#x60;&#x60;: Unix timestamp in seconds when the list will expire. If it does not exist, it will never expire.             - &#x60;&#x60;created_at&#x60;&#x60;: Unix timestamp in seconds when the list was created.             - &#x60;&#x60;updated_at&#x60;&#x60;: Unix timestamp in seconds when the list was updated.  ### Errors  - If the resource type is not valid, it will return a &#x60;&#x60;400&#x60;&#x60; error.  It will also return the API Global errors described in the API description.

    :param resource_type: 
    :type resource_type: str

    """
    return web.Response(status=200)


async def get_all_private_allowlists_v1_allowlist_private_all_get(request: web.Request, ) -> web.Response:
    """Get the set of private allowlists of the user.

    ### What Obtain the set of private allow lists of the user available in the service.  ### Parameters No parameters  ### Result The result is a JSON object with a list of the following JSON objects: - &#x60;&#x60;self&#x60;&#x60;: the URI to the status of all the lists. - &#x60;&#x60;lists&#x60;&#x60;: a list of JSON objects with the available lists:     - &#x60;&#x60;self&#x60;&#x60;: the URI to individual information of the list.     - &#x60;&#x60;name&#x60;&#x60;: A human readable name of the list.     - &#x60;&#x60;description&#x60;&#x60;: A long detailed information about what the list contains and how it is used.     - &#x60;&#x60;resource_type&#x60;&#x60;: The type of the list. It can be &#x60;&#x60;CIDR&#x60;&#x60;, &#x60;&#x60;AS&#x60;&#x60;, &#x60;&#x60;COUNTRY&#x60;&#x60;, &#x60;&#x60;CONTINENT&#x60;&#x60; or &#x60;&#x60;DATACENTER_ID&#x60;&#x60;.     - &#x60;&#x60;list_type&#x60;&#x60;: The type of the list. It can be &#x60;&#x60;ALLOW&#x60;&#x60; or &#x60;&#x60;DENY&#x60;&#x60;.     - &#x60;&#x60;created_at&#x60;&#x60;: Unix timestamp in seconds when the list was created.     - &#x60;&#x60;updated_at&#x60;&#x60;: Unix timestamp in seconds when the list was updated.     - &#x60;&#x60;expiry&#x60;&#x60;: Unix timestamp in seconds when the list will expire. If it does not exist, it will never expire.     - &#x60;&#x60;origins&#x60;&#x60;: list of websites that are using the list as a allowlist.         - &#x60;&#x60;self&#x60;&#x60;: the URI to all the list of origins.         - &#x60;&#x60;lists&#x60;&#x60;: list of lists that the origin is using.             - &#x60;&#x60;self&#x60;&#x60;: the URI to the individual information of the list.             - &#x60;&#x60;origin&#x60;&#x60;: the protocol and domain of the website that is using the list.             - &#x60;&#x60;status&#x60;&#x60;: the status of the list. It can be &#x60;&#x60;ACTIVE&#x60;&#x60; or &#x60;&#x60;INACTIVE&#x60;&#x60; or &#x60;&#x60;EXPIRED&#x60;&#x60;. If the list is &#x60;&#x60;EXPIRED&#x60;&#x60; it means that the list is not available anymore if not renewed.             - &#x60;&#x60;expiry&#x60;&#x60;: Unix timestamp in seconds when the list will expire. If it does not exist, it will never expire.             - &#x60;&#x60;created_at&#x60;&#x60;: Unix timestamp in seconds when the list was created.             - &#x60;&#x60;updated_at&#x60;&#x60;: Unix timestamp in seconds when the list was updated.  ### Errors  It will return the API Global errors described in the API description.


    """
    return web.Response(status=200)


async def get_all_public_allowlists_by_resource_type_v1_allowlist_public_all_resource_type_get(request: web.Request, resource_type) -> web.Response:
    """Get the set of public allowlists by resource type.

    ### What Obtain the set of public allow lists available in the service and also which ones are already selected by the user and wich ones are not filtering by the resource type.  ### Parameters The &#x60;&#x60;resource type&#x60;&#x60; to filter. The values can be &#x60;&#x60;CIDR&#x60;&#x60;, &#x60;&#x60;AS&#x60;&#x60;, &#x60;&#x60;COUNTRY&#x60;&#x60;, &#x60;&#x60;CONTINENT&#x60;&#x60; or &#x60;&#x60;DATACENTER_ID&#x60;&#x60;.  ### Result The result is a JSON object with a list of the following JSON objects: - &#x60;&#x60;self&#x60;&#x60;: the URI to the status of all the lists. - &#x60;&#x60;lists&#x60;&#x60;: a list of JSON objects with the available lists:     - &#x60;&#x60;self&#x60;&#x60;: the URI to individual information of the list.     - &#x60;&#x60;name&#x60;&#x60;: A human readable name of the list.     - &#x60;&#x60;description&#x60;&#x60;: A long detailed information about what the list contains and how it is used.     - &#x60;&#x60;resource_type&#x60;&#x60;: The type of the list. It can be &#x60;&#x60;CIDR&#x60;&#x60;, &#x60;&#x60;AS&#x60;&#x60;, &#x60;&#x60;COUNTRY&#x60;&#x60;, &#x60;&#x60;CONTINENT&#x60;&#x60; or &#x60;&#x60;DATACENTER_ID&#x60;&#x60;.     - &#x60;&#x60;list_type&#x60;&#x60;: The type of the list. It can be &#x60;&#x60;ALLOW&#x60;&#x60; or &#x60;&#x60;DENY&#x60;&#x60;.     - &#x60;&#x60;status&#x60;&#x60;: The status of the list. It can be &#x60;&#x60;ACTIVE&#x60;&#x60; or &#x60;&#x60;INACTIVE&#x60;&#x60; or &#x60;&#x60;EXPIRED&#x60;&#x60;. If the list is &#x60;&#x60;EXPIRED&#x60;&#x60;    it means that the list is not available anymore if not renewed.     - &#x60;&#x60;created_at&#x60;&#x60;: Unix timestamp in seconds when the list was created.     - &#x60;&#x60;updated_at&#x60;&#x60;: Unix timestamp in seconds when the list was updated.  If the list is already selected by the user, the JSON object will also contain the following fields: - &#x60;&#x60;expiry&#x60;&#x60;: Unix timestamp in seconds when the list will expire. If it does not exist, it will never expire. - &#x60;&#x60;origins&#x60;&#x60;: list of websites that are using the list as an allowlist.     - &#x60;&#x60;self&#x60;&#x60;: the URI to all the list of origins.     - &#x60;&#x60;lists&#x60;&#x60;: list of lists that the origin is using.         - &#x60;&#x60;self&#x60;&#x60;: the URI to the individual information of the list.         - &#x60;&#x60;origin&#x60;&#x60;: the protocol and domain of the website that is using the list.         - &#x60;&#x60;status&#x60;&#x60;: the status of the list. It can be &#x60;&#x60;ACTIVE&#x60;&#x60; or &#x60;&#x60;INACTIVE&#x60;&#x60; or &#x60;&#x60;EXPIRED&#x60;&#x60;. If the list is &#x60;&#x60;EXPIRED&#x60;&#x60;        it means that the list is not available anymore if not renewed.         - &#x60;&#x60;expiry&#x60;&#x60;: Unix timestamp in seconds when the list will expire. If it does not exist, it will never expire.         - &#x60;&#x60;created_at&#x60;&#x60;: Unix timestamp in seconds when the list was created.         - &#x60;&#x60;updated_at&#x60;&#x60;: Unix timestamp in seconds when the list was updated.  ### Errors  It will return the API Global errors described in the API description.

    :param resource_type: 
    :type resource_type: str

    """
    return web.Response(status=200)


async def get_all_public_allowlists_v1_allowlist_public_all_get(request: web.Request, ) -> web.Response:
    """Get the set of public allowlists.

    ### What Obtain the set of public allow lists available in the service and also which ones are already selected by the user and wich ones are not.  ### Parameters No parameters  ### Result The result is a JSON object with a list of the following JSON objects: - &#x60;&#x60;self&#x60;&#x60;: the URI to the status of all the lists. - &#x60;&#x60;lists&#x60;&#x60;: a list of JSON objects with the available lists:     - &#x60;&#x60;self&#x60;&#x60;: the URI to individual information of the list.     - &#x60;&#x60;name&#x60;&#x60;: A human readable name of the list.     - &#x60;&#x60;description&#x60;&#x60;: A long detailed information about what the list contains and how it is used.     - &#x60;&#x60;resource_type&#x60;&#x60;: The type of the list. It can be &#x60;&#x60;CIDR&#x60;&#x60;, &#x60;&#x60;AS&#x60;&#x60;, &#x60;&#x60;COUNTRY&#x60;&#x60;, &#x60;&#x60;CONTINENT&#x60;&#x60; or &#x60;&#x60;DATACENTER_ID&#x60;&#x60;.     - &#x60;&#x60;list_type&#x60;&#x60;: The type of the list. It can be &#x60;&#x60;ALLOW&#x60;&#x60; or &#x60;&#x60;DENY&#x60;&#x60;.     - &#x60;&#x60;status&#x60;&#x60;: The status of the list. It can be &#x60;&#x60;ACTIVE&#x60;&#x60; or &#x60;&#x60;INACTIVE&#x60;&#x60; or &#x60;&#x60;EXPIRED&#x60;&#x60;. If the list is &#x60;&#x60;EXPIRED&#x60;&#x60;    it means that the list is not available anymore if not renewed.     - &#x60;&#x60;created_at&#x60;&#x60;: Unix timestamp in seconds when the list was created.     - &#x60;&#x60;updated_at&#x60;&#x60;: Unix timestamp in seconds when the list was updated.  If the list is already selected by the user, the JSON object will also contain the following fields: - &#x60;&#x60;expiry&#x60;&#x60;: Unix timestamp in seconds when the list will expire. If it does not exist, it will never expire. - &#x60;&#x60;origins&#x60;&#x60;: list of websites that are using the list as an allowlist.     - &#x60;&#x60;self&#x60;&#x60;: the URI to all the list of origins.     - &#x60;&#x60;lists&#x60;&#x60;: list of lists that the origin is using.         - &#x60;&#x60;self&#x60;&#x60;: the URI to the individual information of the list.         - &#x60;&#x60;origin&#x60;&#x60;: the protocol and domain of the website that is using the list.         - &#x60;&#x60;status&#x60;&#x60;: the status of the list. It can be &#x60;&#x60;ACTIVE&#x60;&#x60; or &#x60;&#x60;INACTIVE&#x60;&#x60; or &#x60;&#x60;EXPIRED&#x60;&#x60;. If the list is &#x60;&#x60;EXPIRED&#x60;&#x60;        it means that the list is not available anymore if not renewed.         - &#x60;&#x60;expiry&#x60;&#x60;: Unix timestamp in seconds when the list will expire. If it does not exist, it will never expire.         - &#x60;&#x60;created_at&#x60;&#x60;: Unix timestamp in seconds when the list was created.         - &#x60;&#x60;updated_at&#x60;&#x60;: Unix timestamp in seconds when the list was updated.  ### Errors  It will return the API Global errors described in the API description.


    """
    return web.Response(status=200)


async def get_allowlist_content_v1_allowlist_private_allowlist_id_content_get(request: web.Request, allowlist_id, page=None, page_size=None) -> web.Response:
    """Get the content of a private allowlist of the user.

    ### What Returns the content of the private allowlist of the user. The content can be CIDRs, ASNs, countries, continents or    datacenter IDs.  ### Parameters Pass the private allowlist ID as query parameter.  The following pagination parameters are required as query string parameters: - &#x60;&#x60;page&#x60;&#x60;: (Optional) the page number to retrieve. The first page is 1. Default is 1. - &#x60;&#x60;page_size&#x60;&#x60;: (Optional) the number of items per page. Default is 20.   ### Result The result is a JSON object with the following structure: - &#x60;&#x60;self&#x60;&#x60;: the URI to the content of the list. - &#x60;&#x60;cidrs&#x60;&#x60;: (Optional) list of CIDRs in the list. - &#x60;&#x60;asns&#x60;&#x60;: (Optional) list of ASNs in the list. - &#x60;&#x60;countries&#x60;&#x60;: (Optional) list of countries in the list. - &#x60;&#x60;continents&#x60;&#x60;: (Optional) list of continents in the list. - &#x60;&#x60;datacenters&#x60;&#x60;: (Optional) list of datacenters in the list.  ### Errors  - If the allow list is not a valid UUID, it will return a &#x60;&#x60;422&#x60;&#x60; (Unprocessable Entity) error. - If the private allowlist ID does not exist, it will return a &#x60;&#x60;404&#x60;&#x60; (Not found) error.  It will also return the API Global errors described in the API description.

    :param allowlist_id: 
    :type allowlist_id: str
    :type allowlist_id: str
    :param page: The page to be returned
    :type page: int
    :param page_size: The number of items per page
    :type page_size: int

    """
    return web.Response(status=200)


async def get_public_allowlists_owned_by_the_user_v1_allowlist_public_owned_get(request: web.Request, ) -> web.Response:
    """Get the set of owned allowlists.

    ### What Obtain the set of public allow lists available in the service selected by the user.  ### Parameters No parameters  ### Result The result is a JSON object with a list of the following JSON objects: - &#x60;&#x60;self&#x60;&#x60;: the URI to the status of all the lists. - &#x60;&#x60;lists&#x60;&#x60;: a list of JSON objects with the available lists:     - &#x60;&#x60;self&#x60;&#x60;: the URI to individual information of the list.     - &#x60;&#x60;name&#x60;&#x60;: A human readable name of the list.     - &#x60;&#x60;description&#x60;&#x60;: A long detailed information about what the list contains and how it is used.     - &#x60;&#x60;resource_type&#x60;&#x60;: The type of the list. It can be &#x60;&#x60;CIDR&#x60;&#x60;, &#x60;&#x60;AS&#x60;&#x60;, &#x60;&#x60;COUNTRY&#x60;&#x60;, &#x60;&#x60;CONTINENT&#x60;&#x60; or &#x60;&#x60;DATACENTER_ID&#x60;&#x60;.     - &#x60;&#x60;list_type&#x60;&#x60;: The type of the list. It can be &#x60;&#x60;ALLOW&#x60;&#x60; or &#x60;&#x60;DENY&#x60;&#x60;.     - &#x60;&#x60;status&#x60;&#x60;: The status of the list. It can be &#x60;&#x60;ACTIVE&#x60;&#x60; or &#x60;&#x60;INACTIVE&#x60;&#x60; or &#x60;&#x60;EXPIRED&#x60;&#x60;. If the list is &#x60;&#x60;EXPIRED&#x60;&#x60;    it means that the list is not available anymore if not renewed.     - &#x60;&#x60;created_at&#x60;&#x60;: Unix timestamp in seconds when the list was created.     - &#x60;&#x60;updated_at&#x60;&#x60;: Unix timestamp in seconds when the list was updated.     - &#x60;&#x60;expiry&#x60;&#x60;: Unix timestamp in seconds when the list will expire. If it does not exist, it will never expire.     - &#x60;&#x60;origins&#x60;&#x60;: list of websites that are using the list as an allowlist.         - &#x60;&#x60;self&#x60;&#x60;: the URI to all the list of origins.         - &#x60;&#x60;lists&#x60;&#x60;: list of lists that the origin is using.             - &#x60;&#x60;self&#x60;&#x60;: the URI to the individual information of the list.             - &#x60;&#x60;origin&#x60;&#x60;: the protocol and domain of the website that is using the list.             - &#x60;&#x60;status&#x60;&#x60;: the status of the list. It can be &#x60;&#x60;ACTIVE&#x60;&#x60; or &#x60;&#x60;INACTIVE&#x60;&#x60; or &#x60;&#x60;EXPIRED&#x60;&#x60;. If the list is &#x60;&#x60;EXPIRED&#x60;&#x60;            it means that the list is not available anymore if not renewed.             - &#x60;&#x60;expiry&#x60;&#x60;: Unix timestamp in seconds when the list will expire. If it does not exist, it will never expire.             - &#x60;&#x60;created_at&#x60;&#x60;: Unix timestamp in seconds when the list was created.             - &#x60;&#x60;updated_at&#x60;&#x60;: Unix timestamp in seconds when the list was updated.  ### Errors  It will return the API Global errors described in the API description.


    """
    return web.Response(status=200)


async def get_single_allowlist_v1_allowlist_private_allowlist_id_get(request: web.Request, allowlist_id) -> web.Response:
    """Get the details of a specific private allowlist of the user.

    ### What Obtain the details of the private allow list of the user available in the service.  ### Parameters Pass the private allowlist ID as query parameter.  ### Result The result is a JSON object with the following structure: - &#x60;&#x60;self&#x60;&#x60;: the URI to individual information of the list. - &#x60;&#x60;name&#x60;&#x60;: A human readable name of the list. - &#x60;&#x60;description&#x60;&#x60;: A long detailed information about what the list contains and how it is used. - &#x60;&#x60;resource_type&#x60;&#x60;: The type of the list. It can be &#x60;&#x60;CIDR&#x60;&#x60;, &#x60;&#x60;AS&#x60;&#x60;, &#x60;&#x60;COUNTRY&#x60;&#x60;, &#x60;&#x60;CONTINENT&#x60;&#x60; or &#x60;&#x60;DATACENTER_ID&#x60;&#x60;. - &#x60;&#x60;list_type&#x60;&#x60;: The type of the list. It can be &#x60;&#x60;ALLOW&#x60;&#x60; or &#x60;&#x60;DENY&#x60;&#x60;. - &#x60;&#x60;created_at&#x60;&#x60;: Unix timestamp in seconds when the list was created. - &#x60;&#x60;updated_at&#x60;&#x60;: Unix timestamp in seconds when the list was updated. - &#x60;&#x60;expiry&#x60;&#x60;: Unix timestamp in seconds when the list will expire. If it does not exist, it will never expire. - &#x60;&#x60;origins&#x60;&#x60;: list of websites that are using the list as a allowlist.     - &#x60;&#x60;self&#x60;&#x60;: the URI to all the list of origins.     - &#x60;&#x60;lists&#x60;&#x60;: list of lists that the origin is using.         - &#x60;&#x60;self&#x60;&#x60;: the URI to the individual information of the list.         - &#x60;&#x60;origin&#x60;&#x60;: the protocol and domain of the website that is using the list.         - &#x60;&#x60;status&#x60;&#x60;: the status of the list. It can be &#x60;&#x60;ACTIVE&#x60;&#x60; or &#x60;&#x60;INACTIVE&#x60;&#x60; or &#x60;&#x60;EXPIRED&#x60;&#x60;. If the list is &#x60;&#x60;EXPIRED&#x60;&#x60; it means that the list is not available anymore if not renewed.         - &#x60;&#x60;expiry&#x60;&#x60;: Unix timestamp in seconds when the list will expire. If it does not exist, it will never expire.         - &#x60;&#x60;created_at&#x60;&#x60;: Unix timestamp in seconds when the list was created.         - &#x60;&#x60;updated_at&#x60;&#x60;: Unix timestamp in seconds when the list was updated.  ### Errors  - If the allow list is not a valid UUID, it will return a 422 error. - If the private allowlist ID does not exist, it will return a &#x60;&#x60;404&#x60;&#x60; error.  It will also return the API Global errors described in the API description.

    :param allowlist_id: 
    :type allowlist_id: str
    :type allowlist_id: str

    """
    return web.Response(status=200)


async def get_single_allowlist_v1_allowlist_public_allowlist_id_get(request: web.Request, allowlist_id) -> web.Response:
    """Get the details of the allowlist.

    ### What Obtain the details of an allow list available in the service.  ### Parameters No parameters  ### Result The result is a JSON object with a list of the following JSON objects: - &#x60;&#x60;self&#x60;&#x60;: the URI to individual information of the list. - &#x60;&#x60;name&#x60;&#x60;: A human readable name of the list. - &#x60;&#x60;description&#x60;&#x60;: A long detailed information about what the list contains and how it is used. - &#x60;&#x60;resource_type&#x60;&#x60;: The type of the list. It can be &#x60;&#x60;CIDR&#x60;&#x60;, &#x60;&#x60;AS&#x60;&#x60;, &#x60;&#x60;COUNTRY&#x60;&#x60;, &#x60;&#x60;CONTINENT&#x60;&#x60; or &#x60;&#x60;DATACENTER_ID&#x60;&#x60;. - &#x60;&#x60;list_type&#x60;&#x60;: The type of the list. It can be &#x60;&#x60;ALLOW&#x60;&#x60; or &#x60;&#x60;DENY&#x60;&#x60;. - &#x60;&#x60;status&#x60;&#x60;: The status of the list. It can be &#x60;&#x60;ACTIVE&#x60;&#x60; or &#x60;&#x60;INACTIVE&#x60;&#x60; or &#x60;&#x60;EXPIRED&#x60;&#x60;. If the list is &#x60;&#x60;EXPIRED&#x60;&#x60;it means that the list is not available anymore if not renewed. - &#x60;&#x60;created_at&#x60;&#x60;: Unix timestamp in seconds when the list was created. - &#x60;&#x60;updated_at&#x60;&#x60;: Unix timestamp in seconds when the list was updated.  If the list is already selected by the user, the JSON object will also contain the following fields:     - &#x60;&#x60;expiry&#x60;&#x60;: Unix timestamp in seconds when the list will expire. If it does not exist, it will never expire.     - &#x60;&#x60;origins&#x60;&#x60;: list of websites that are using the list as an allowlist.         - &#x60;&#x60;self&#x60;&#x60;: the URI to all the list of origins.         - &#x60;&#x60;lists&#x60;&#x60;: list of lists that the origin is using.             - &#x60;&#x60;self&#x60;&#x60;: the URI to the individual information of the list.             - &#x60;&#x60;origin&#x60;&#x60;: the protocol and domain of the website that is using the list.             - &#x60;&#x60;status&#x60;&#x60;: the status of the list. It can be &#x60;&#x60;ACTIVE&#x60;&#x60; or &#x60;&#x60;INACTIVE&#x60;&#x60; or &#x60;&#x60;EXPIRED&#x60;&#x60;. If the list is &#x60;&#x60;EXPIRED&#x60;&#x60;            it means that the list is not available anymore if not renewed.             - &#x60;&#x60;expiry&#x60;&#x60;: Unix timestamp in seconds when the list will expire. If it does not exist, it will never expire.             - &#x60;&#x60;created_at&#x60;&#x60;: Unix timestamp in seconds when the list was created.             - &#x60;&#x60;updated_at&#x60;&#x60;: Unix timestamp in seconds when the list was updated.  ### Errors  If the list does not exist, it will return a 404 error.  It will return the API Global errors described in the API description.

    :param allowlist_id: 
    :type allowlist_id: str
    :type allowlist_id: str

    """
    return web.Response(status=200)


async def query_resource_allowlists_v1_allowlist_public_ip_address_get(request: web.Request, address) -> web.Response:
    """Get the different public allowlists where the IP address was found.

    ### What Obtain the list of all the different public allowlists where the IP address entered by the user is. The public allowlists are the ones activated by the user, but managed by Threatjammer administrators.  ### Parameters The endpoint accepts the &#x60;address&#x60; parameter as query string.  ### Result The result is a JSON object with a list of the following JSON objects: - &#x60;&#x60;self&#x60;&#x60;: the URI to individual status. - &#x60;&#x60;cidrs&#x60;&#x60;: the URI of the lists of CIDRs where the IP was found. - &#x60;&#x60;country&#x60;&#x60;: the URIs where the lists of countries where the IP address was found - &#x60;&#x60;continent&#x60;&#x60;: the URI where the continent where the IP address was found. - &#x60;&#x60;asn&#x60;&#x60;: the URIs where the list of continents of the ASN where the IP address was found. - &#x60;&#x60;datacenter&#x60;&#x60;: the URIs of the lists of datacenters where the IP address was found. If not found, the result is an empty string.  ### Errors - a &#x60;422 Unprocessable Entity&#x60; error if the IP address was malformed.  It will also return the API Global errors described in the API description.

    :param address: 
    :type address: dict | bytes

    """
    address = .from_dict(address)
    return web.Response(status=200)


async def query_resource_denylists_v1_allowlist_private_ip_address_get(request: web.Request, address) -> web.Response:
    """Get the different private allowlists where the IP address was found.

    ### What Obtain the list of all the different private allowlists where the IP address entered by the user. The allowlisted forbidden datasets are the ones submitted manually by the user from files or indidual items.  ### Parameters The endpoint accepts the &#x60;address&#x60; parameter as query string.  ### Result The result is a JSON object with a list of the following JSON objects: - &#x60;&#x60;self&#x60;&#x60;: the URI to individual status. - &#x60;&#x60;cidrs&#x60;&#x60;: the URI of the lists of CIDRs where the IP was found. - &#x60;&#x60;country&#x60;&#x60;: the URIs where the lists of countries where the IP address was found - &#x60;&#x60;continent&#x60;&#x60;: the URI where the continent where the IP address was found. - &#x60;&#x60;asn&#x60;&#x60;: the URIs where the list of continents of the ASN where the IP address was found. - &#x60;&#x60;datacenter&#x60;&#x60;: the URIs of the lists of datacenters where the IP address was found. If not found, the result is an empty string. - &#x60;&#x60;reported&#x60;&#x60;: the URI of the information of the IP address reported by the user. For allowlist should be empty.  ### Errors - a &#x60;422 Unprocessable Entity&#x60; error if the IP address was malformed.  It will also return the API Global errors described in the API description.

    :param address: 
    :type address: dict | bytes

    """
    address = .from_dict(address)
    return web.Response(status=200)


async def update_private_allowlist_of_the_user_v1_allowlist_private_allowlist_id_put(request: web.Request, allowlist_id, body=None) -> web.Response:
    """Update the information of an existing private allowlist of the user.

    ### What Updates the information that describes the allowlist of the user in the system. The parameters that can be modified are:  - name  - description  - tags  - expiry  This is an asynchronous operation. It can take several seconds until the operation completes, but the request will immediately return a 202 Accepted response.  ### Parameters In the query string the ID of the private allow list to delete.  In the body the following parameters: - &#x60;&#x60;name&#x60;&#x60;: (Optional) A human readable name of the list. - &#x60;&#x60;description&#x60;&#x60;: (Optional) A long detailed information about what the list contains and how it is used. - &#x60;&#x60;tags&#x60;&#x60;: (Optional) A list of tags that describe the list. - &#x60;&#x60;expiry&#x60;&#x60;: (Optional) Unix timestamp in seconds when the list will expire. If it does not exist, it will never expire.  ### Result It should always return a 202 Accepted response with an empty body.  ### Errors  - If the list does not exist, it will return a &#x60;404&#x60; (Not found) error. - If the list is a default list, it will return a &#x60;403&#x60; (Forbidden) error. - If the allow list is not a valid UUID, it will return a &#x60;422&#x60; (Unprocessable Entity) error. - If the expiry is not a valid timestamp, it will return a &#x60;422&#x60; (Unprocessable Entity) error. - If the expiry is in the past, it will return a &#x60;400&#x60; (Bad Request) error. - If the name is not a string, it will return a &#x60;422&#x60; (Unprocessable Entity) error. - If the description is not a string, it will return a &#x60;422&#x60; (Unprocessable Entity) error.  It will return the API Global errors described in the API description.

    :param allowlist_id: 
    :type allowlist_id: str
    :type allowlist_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = BodyUpdatePrivateAllowlistOfTheUserV1AllowlistPrivateAllowlistIdPut.from_dict(body)
    return web.Response(status=200)


async def update_private_content_of_the_allowlist_of_the_user_v1_allowlist_private_allowlist_id_content_put(request: web.Request, allowlist_id, body=None) -> web.Response:
    """Add or remove content of a private allowlist of the user.

    ### What Add or remove content of a private allowlist of the user. The content can be CIDRs, ASNs, countries, continents or datacenter IDs.  The number of elements allowed in all the lists are limited depending on the plan of the user: - Free: 100 elements - Basic: 1000 elements - Pro: 10000 elements  ### Parameters Pass the private allowlist ID as query parameter.  In the body the following parameters: - &#x60;&#x60;append&#x60;&#x60;: (Optional) Add CIDRs, ASNs, countries, continents or datacenter IDs to add to the list. It&#39;s not possible to mix different resource types in the same list. - &#x60;&#x60;remove&#x60;&#x60;: (Optional) Extract CIDRs, ASNs, countries, continents or datacenter IDs to add to the list. It&#39;s not possible to mix different resource types in the same list.   ### Result If successful, it will return a &#x60;&#x60;202&#x60;&#x60; (Accepted) response with an empty body. The operation is asynchronous,and can take several seconds to complete.  ### Errors  - If the allow list is not a valid UUID, it will return a &#x60;&#x60;422&#x60;&#x60; (Unprocessable Entity) error. - If the private allowlist ID does not exist, it will return a &#x60;&#x60;404&#x60;&#x60; (Not found) error. - If the &#x60;&#x60;append&#x60;&#x60; or &#x60;&#x60;remove&#x60;&#x60; parameters are not processable, it will return a &#x60;&#x60;422&#x60;&#x60; (Unprocessable Entity) error. - If the number of elements in the lists is over the limit, it will return a &#x60;&#x60;413&#x60;&#x60; (Payload Too Large) error.  It will also return the API Global errors described in the API description.

    :param allowlist_id: 
    :type allowlist_id: str
    :type allowlist_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = BodyUpdatePrivateContentOfTheAllowlistOfTheUserV1AllowlistPrivateAllowlistIdContentPut.from_dict(body)
    return web.Response(status=200)
