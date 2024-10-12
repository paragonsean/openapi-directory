from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_identity_pool_input import CreateIdentityPoolInput
from openapi_server.models.delete_identities_input import DeleteIdentitiesInput
from openapi_server.models.delete_identities_response import DeleteIdentitiesResponse
from openapi_server.models.delete_identity_pool_input import DeleteIdentityPoolInput
from openapi_server.models.describe_identity_input import DescribeIdentityInput
from openapi_server.models.describe_identity_pool_input import DescribeIdentityPoolInput
from openapi_server.models.get_credentials_for_identity_input import GetCredentialsForIdentityInput
from openapi_server.models.get_credentials_for_identity_response import GetCredentialsForIdentityResponse
from openapi_server.models.get_id_input import GetIdInput
from openapi_server.models.get_id_response import GetIdResponse
from openapi_server.models.get_identity_pool_roles_input import GetIdentityPoolRolesInput
from openapi_server.models.get_identity_pool_roles_response import GetIdentityPoolRolesResponse
from openapi_server.models.get_open_id_token_for_developer_identity_input import GetOpenIdTokenForDeveloperIdentityInput
from openapi_server.models.get_open_id_token_for_developer_identity_response import GetOpenIdTokenForDeveloperIdentityResponse
from openapi_server.models.get_open_id_token_input import GetOpenIdTokenInput
from openapi_server.models.get_open_id_token_response import GetOpenIdTokenResponse
from openapi_server.models.get_principal_tag_attribute_map_input import GetPrincipalTagAttributeMapInput
from openapi_server.models.get_principal_tag_attribute_map_response import GetPrincipalTagAttributeMapResponse
from openapi_server.models.identity_description import IdentityDescription
from openapi_server.models.identity_pool import IdentityPool
from openapi_server.models.list_identities_input import ListIdentitiesInput
from openapi_server.models.list_identities_response import ListIdentitiesResponse
from openapi_server.models.list_identity_pools_input import ListIdentityPoolsInput
from openapi_server.models.list_identity_pools_response import ListIdentityPoolsResponse
from openapi_server.models.list_tags_for_resource_input import ListTagsForResourceInput
from openapi_server.models.list_tags_for_resource_response import ListTagsForResourceResponse
from openapi_server.models.lookup_developer_identity_input import LookupDeveloperIdentityInput
from openapi_server.models.lookup_developer_identity_response import LookupDeveloperIdentityResponse
from openapi_server.models.merge_developer_identities_input import MergeDeveloperIdentitiesInput
from openapi_server.models.merge_developer_identities_response import MergeDeveloperIdentitiesResponse
from openapi_server.models.set_identity_pool_roles_input import SetIdentityPoolRolesInput
from openapi_server.models.set_principal_tag_attribute_map_input import SetPrincipalTagAttributeMapInput
from openapi_server.models.set_principal_tag_attribute_map_response import SetPrincipalTagAttributeMapResponse
from openapi_server.models.tag_resource_input import TagResourceInput
from openapi_server.models.unlink_developer_identity_input import UnlinkDeveloperIdentityInput
from openapi_server.models.unlink_identity_input import UnlinkIdentityInput
from openapi_server.models.untag_resource_input import UntagResourceInput
from openapi_server import util


async def create_identity_pool(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_identity_pool

    &lt;p&gt;Creates a new identity pool. The identity pool is a store of user identity information that is specific to your AWS account. The keys for &lt;code&gt;SupportedLoginProviders&lt;/code&gt; are as follows:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Facebook: &lt;code&gt;graph.facebook.com&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Google: &lt;code&gt;accounts.google.com&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Amazon: &lt;code&gt;www.amazon.com&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Twitter: &lt;code&gt;api.twitter.com&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Digits: &lt;code&gt;www.digits.com&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;You must use AWS Developer credentials to call this API.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = CreateIdentityPoolInput.from_dict(body)
    return web.Response(status=200)


async def delete_identities(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_identities

    &lt;p&gt;Deletes identities from an identity pool. You can specify a list of 1-60 identities that you want to delete.&lt;/p&gt; &lt;p&gt;You must use AWS Developer credentials to call this API.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = DeleteIdentitiesInput.from_dict(body)
    return web.Response(status=200)


async def delete_identity_pool(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_identity_pool

    &lt;p&gt;Deletes an identity pool. Once a pool is deleted, users will not be able to authenticate with the pool.&lt;/p&gt; &lt;p&gt;You must use AWS Developer credentials to call this API.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = DeleteIdentityPoolInput.from_dict(body)
    return web.Response(status=200)


async def describe_identity(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_identity

    &lt;p&gt;Returns metadata related to the given identity, including when the identity was created and any associated linked logins.&lt;/p&gt; &lt;p&gt;You must use AWS Developer credentials to call this API.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = DescribeIdentityInput.from_dict(body)
    return web.Response(status=200)


async def describe_identity_pool(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_identity_pool

    &lt;p&gt;Gets details about a particular identity pool, including the pool name, ID description, creation date, and current number of users.&lt;/p&gt; &lt;p&gt;You must use AWS Developer credentials to call this API.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = DescribeIdentityPoolInput.from_dict(body)
    return web.Response(status=200)


async def get_credentials_for_identity(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_credentials_for_identity

    &lt;p&gt;Returns credentials for the provided identity ID. Any provided logins will be validated against supported login providers. If the token is for cognito-identity.amazonaws.com, it will be passed through to AWS Security Token Service with the appropriate role for the token.&lt;/p&gt; &lt;p&gt;This is a public API. You do not need any credentials to call this API.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = GetCredentialsForIdentityInput.from_dict(body)
    return web.Response(status=200)


async def get_id(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_id

    &lt;p&gt;Generates (or retrieves) a Cognito ID. Supplying multiple logins will create an implicit linked account.&lt;/p&gt; &lt;p&gt;This is a public API. You do not need any credentials to call this API.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = GetIdInput.from_dict(body)
    return web.Response(status=200)


async def get_identity_pool_roles(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_identity_pool_roles

    &lt;p&gt;Gets the roles for an identity pool.&lt;/p&gt; &lt;p&gt;You must use AWS Developer credentials to call this API.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = GetIdentityPoolRolesInput.from_dict(body)
    return web.Response(status=200)


async def get_open_id_token(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_open_id_token

    &lt;p&gt;Gets an OpenID token, using a known Cognito ID. This known Cognito ID is returned by &lt;a&gt;GetId&lt;/a&gt;. You can optionally add additional logins for the identity. Supplying multiple logins creates an implicit link.&lt;/p&gt; &lt;p&gt;The OpenID token is valid for 10 minutes.&lt;/p&gt; &lt;p&gt;This is a public API. You do not need any credentials to call this API.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = GetOpenIdTokenInput.from_dict(body)
    return web.Response(status=200)


async def get_open_id_token_for_developer_identity(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_open_id_token_for_developer_identity

    &lt;p&gt;Registers (or retrieves) a Cognito &lt;code&gt;IdentityId&lt;/code&gt; and an OpenID Connect token for a user authenticated by your backend authentication process. Supplying multiple logins will create an implicit linked account. You can only specify one developer provider as part of the &lt;code&gt;Logins&lt;/code&gt; map, which is linked to the identity pool. The developer provider is the \&quot;domain\&quot; by which Cognito will refer to your users.&lt;/p&gt; &lt;p&gt;You can use &lt;code&gt;GetOpenIdTokenForDeveloperIdentity&lt;/code&gt; to create a new identity and to link new logins (that is, user credentials issued by a public provider or developer provider) to an existing identity. When you want to create a new identity, the &lt;code&gt;IdentityId&lt;/code&gt; should be null. When you want to associate a new login with an existing authenticated/unauthenticated identity, you can do so by providing the existing &lt;code&gt;IdentityId&lt;/code&gt;. This API will create the identity in the specified &lt;code&gt;IdentityPoolId&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;You must use AWS Developer credentials to call this API.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = GetOpenIdTokenForDeveloperIdentityInput.from_dict(body)
    return web.Response(status=200)


async def get_principal_tag_attribute_map(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_principal_tag_attribute_map

    Use &lt;code&gt;GetPrincipalTagAttributeMap&lt;/code&gt; to list all mappings between &lt;code&gt;PrincipalTags&lt;/code&gt; and user attributes.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = GetPrincipalTagAttributeMapInput.from_dict(body)
    return web.Response(status=200)


async def list_identities(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """list_identities

    &lt;p&gt;Lists the identities in an identity pool.&lt;/p&gt; &lt;p&gt;You must use AWS Developer credentials to call this API.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = ListIdentitiesInput.from_dict(body)
    return web.Response(status=200)


async def list_identity_pools(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_identity_pools

    &lt;p&gt;Lists all of the Cognito identity pools registered for your account.&lt;/p&gt; &lt;p&gt;You must use AWS Developer credentials to call this API.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param max_results: Pagination limit
    :type max_results: str
    :param next_token: Pagination token
    :type next_token: str

    """
    body = ListIdentityPoolsInput.from_dict(body)
    return web.Response(status=200)


async def list_tags_for_resource(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """list_tags_for_resource

    &lt;p&gt;Lists the tags that are assigned to an Amazon Cognito identity pool.&lt;/p&gt; &lt;p&gt;A tag is a label that you can apply to identity pools to categorize and manage them in different ways, such as by purpose, owner, environment, or other criteria.&lt;/p&gt; &lt;p&gt;You can use this action up to 10 times per second, per account.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = ListTagsForResourceInput.from_dict(body)
    return web.Response(status=200)


async def lookup_developer_identity(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """lookup_developer_identity

    &lt;p&gt;Retrieves the &lt;code&gt;IdentityID&lt;/code&gt; associated with a &lt;code&gt;DeveloperUserIdentifier&lt;/code&gt; or the list of &lt;code&gt;DeveloperUserIdentifier&lt;/code&gt; values associated with an &lt;code&gt;IdentityId&lt;/code&gt; for an existing identity. Either &lt;code&gt;IdentityID&lt;/code&gt; or &lt;code&gt;DeveloperUserIdentifier&lt;/code&gt; must not be null. If you supply only one of these values, the other value will be searched in the database and returned as a part of the response. If you supply both, &lt;code&gt;DeveloperUserIdentifier&lt;/code&gt; will be matched against &lt;code&gt;IdentityID&lt;/code&gt;. If the values are verified against the database, the response returns both values and is the same as the request. Otherwise a &lt;code&gt;ResourceConflictException&lt;/code&gt; is thrown.&lt;/p&gt; &lt;p&gt; &lt;code&gt;LookupDeveloperIdentity&lt;/code&gt; is intended for low-throughput control plane operations: for example, to enable customer service to locate an identity ID by username. If you are using it for higher-volume operations such as user authentication, your requests are likely to be throttled. &lt;a&gt;GetOpenIdTokenForDeveloperIdentity&lt;/a&gt; is a better option for higher-volume operations for user authentication.&lt;/p&gt; &lt;p&gt;You must use AWS Developer credentials to call this API.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = LookupDeveloperIdentityInput.from_dict(body)
    return web.Response(status=200)


async def merge_developer_identities(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """merge_developer_identities

    &lt;p&gt;Merges two users having different &lt;code&gt;IdentityId&lt;/code&gt;s, existing in the same identity pool, and identified by the same developer provider. You can use this action to request that discrete users be merged and identified as a single user in the Cognito environment. Cognito associates the given source user (&lt;code&gt;SourceUserIdentifier&lt;/code&gt;) with the &lt;code&gt;IdentityId&lt;/code&gt; of the &lt;code&gt;DestinationUserIdentifier&lt;/code&gt;. Only developer-authenticated users can be merged. If the users to be merged are associated with the same public provider, but as two different users, an exception will be thrown.&lt;/p&gt; &lt;p&gt;The number of linked logins is limited to 20. So, the number of linked logins for the source user, &lt;code&gt;SourceUserIdentifier&lt;/code&gt;, and the destination user, &lt;code&gt;DestinationUserIdentifier&lt;/code&gt;, together should not be larger than 20. Otherwise, an exception will be thrown.&lt;/p&gt; &lt;p&gt;You must use AWS Developer credentials to call this API.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = MergeDeveloperIdentitiesInput.from_dict(body)
    return web.Response(status=200)


async def set_identity_pool_roles(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """set_identity_pool_roles

    &lt;p&gt;Sets the roles for an identity pool. These roles are used when making calls to &lt;a&gt;GetCredentialsForIdentity&lt;/a&gt; action.&lt;/p&gt; &lt;p&gt;You must use AWS Developer credentials to call this API.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = SetIdentityPoolRolesInput.from_dict(body)
    return web.Response(status=200)


async def set_principal_tag_attribute_map(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """set_principal_tag_attribute_map

    You can use this operation to use default (username and clientID) attribute or custom attribute mappings.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = SetPrincipalTagAttributeMapInput.from_dict(body)
    return web.Response(status=200)


async def tag_resource(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """tag_resource

    &lt;p&gt;Assigns a set of tags to the specified Amazon Cognito identity pool. A tag is a label that you can use to categorize and manage identity pools in different ways, such as by purpose, owner, environment, or other criteria.&lt;/p&gt; &lt;p&gt;Each tag consists of a key and value, both of which you define. A key is a general category for more specific values. For example, if you have two versions of an identity pool, one for testing and another for production, you might assign an &lt;code&gt;Environment&lt;/code&gt; tag key to both identity pools. The value of this key might be &lt;code&gt;Test&lt;/code&gt; for one identity pool and &lt;code&gt;Production&lt;/code&gt; for the other.&lt;/p&gt; &lt;p&gt;Tags are useful for cost tracking and access control. You can activate your tags so that they appear on the Billing and Cost Management console, where you can track the costs associated with your identity pools. In an IAM policy, you can constrain permissions for identity pools based on specific tags or tag values.&lt;/p&gt; &lt;p&gt;You can use this action up to 5 times per second, per account. An identity pool can have as many as 50 tags.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = TagResourceInput.from_dict(body)
    return web.Response(status=200)


async def unlink_developer_identity(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """unlink_developer_identity

    &lt;p&gt;Unlinks a &lt;code&gt;DeveloperUserIdentifier&lt;/code&gt; from an existing identity. Unlinked developer users will be considered new identities next time they are seen. If, for a given Cognito identity, you remove all federated identities as well as the developer user identifier, the Cognito identity becomes inaccessible.&lt;/p&gt; &lt;p&gt;You must use AWS Developer credentials to call this API.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = UnlinkDeveloperIdentityInput.from_dict(body)
    return web.Response(status=200)


async def unlink_identity(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """unlink_identity

    &lt;p&gt;Unlinks a federated identity from an existing account. Unlinked logins will be considered new identities next time they are seen. Removing the last linked login will make this identity inaccessible.&lt;/p&gt; &lt;p&gt;This is a public API. You do not need any credentials to call this API.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = UnlinkIdentityInput.from_dict(body)
    return web.Response(status=200)


async def untag_resource(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """untag_resource

    Removes the specified tags from the specified Amazon Cognito identity pool. You can use this action up to 5 times per second, per account

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = UntagResourceInput.from_dict(body)
    return web.Response(status=200)


async def update_identity_pool(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_identity_pool

    &lt;p&gt;Updates an identity pool.&lt;/p&gt; &lt;p&gt;You must use AWS Developer credentials to call this API.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = IdentityPool.from_dict(body)
    return web.Response(status=200)
