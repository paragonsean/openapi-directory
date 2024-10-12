from typing import List, Dict
from aiohttp import web

from openapi_server.models.get_role_credentials_response import GetRoleCredentialsResponse
from openapi_server.models.list_account_roles_response import ListAccountRolesResponse
from openapi_server.models.list_accounts_response import ListAccountsResponse
from openapi_server import util


async def get_role_credentials(request: web.Request, role_name, account_id, x_amz_sso_bearer_token, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_role_credentials

    Returns the STS short-term credentials for a given role name that is assigned to the user.

    :param role_name: The friendly name of the role that is assigned to the user.
    :type role_name: str
    :param account_id: The identifier for the AWS account that is assigned to the user.
    :type account_id: str
    :param x_amz_sso_bearer_token: The token issued by the &lt;code&gt;CreateToken&lt;/code&gt; API call. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/singlesignon/latest/OIDCAPIReference/API_CreateToken.html\&quot;&gt;CreateToken&lt;/a&gt; in the &lt;i&gt;IAM Identity Center OIDC API Reference Guide&lt;/i&gt;.
    :type x_amz_sso_bearer_token: str
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
    return web.Response(status=200)


async def list_account_roles(request: web.Request, x_amz_sso_bearer_token, account_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None, max_result=None, max_results=None, next_token2=None) -> web.Response:
    """list_account_roles

    Lists all roles that are assigned to the user for a given AWS account.

    :param x_amz_sso_bearer_token: The token issued by the &lt;code&gt;CreateToken&lt;/code&gt; API call. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/singlesignon/latest/OIDCAPIReference/API_CreateToken.html\&quot;&gt;CreateToken&lt;/a&gt; in the &lt;i&gt;IAM Identity Center OIDC API Reference Guide&lt;/i&gt;.
    :type x_amz_sso_bearer_token: str
    :param account_id: The identifier for the AWS account that is assigned to the user.
    :type account_id: str
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
    :param next_token: The page token from the previous response output when you request subsequent pages.
    :type next_token: str
    :param max_result: The number of items that clients can request per page.
    :type max_result: int
    :param max_results: Pagination limit
    :type max_results: str
    :param next_token2: Pagination token
    :type next_token2: str

    """
    return web.Response(status=200)


async def list_accounts(request: web.Request, x_amz_sso_bearer_token, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None, max_result=None, max_results=None, next_token2=None) -> web.Response:
    """list_accounts

    Lists all AWS accounts assigned to the user. These AWS accounts are assigned by the administrator of the account. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/singlesignon/latest/userguide/useraccess.html#assignusers\&quot;&gt;Assign User Access&lt;/a&gt; in the &lt;i&gt;IAM Identity Center User Guide&lt;/i&gt;. This operation returns a paginated response.

    :param x_amz_sso_bearer_token: The token issued by the &lt;code&gt;CreateToken&lt;/code&gt; API call. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/singlesignon/latest/OIDCAPIReference/API_CreateToken.html\&quot;&gt;CreateToken&lt;/a&gt; in the &lt;i&gt;IAM Identity Center OIDC API Reference Guide&lt;/i&gt;.
    :type x_amz_sso_bearer_token: str
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
    :param next_token: (Optional) When requesting subsequent pages, this is the page token from the previous response output.
    :type next_token: str
    :param max_result: This is the number of items clients can request per page.
    :type max_result: int
    :param max_results: Pagination limit
    :type max_results: str
    :param next_token2: Pagination token
    :type next_token2: str

    """
    return web.Response(status=200)


async def logout(request: web.Request, x_amz_sso_bearer_token, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """logout

    &lt;p&gt;Removes the locally stored SSO tokens from the client-side cache and sends an API call to the IAM Identity Center service to invalidate the corresponding server-side IAM Identity Center sign in session.&lt;/p&gt; &lt;note&gt; &lt;p&gt;If a user uses IAM Identity Center to access the AWS CLI, the user’s IAM Identity Center sign in session is used to obtain an IAM session, as specified in the corresponding IAM Identity Center permission set. More specifically, IAM Identity Center assumes an IAM role in the target account on behalf of the user, and the corresponding temporary AWS credentials are returned to the client.&lt;/p&gt; &lt;p&gt;After user logout, any existing IAM role sessions that were created by using IAM Identity Center permission sets continue based on the duration configured in the permission set. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/singlesignon/latest/userguide/authconcept.html\&quot;&gt;User authentications&lt;/a&gt; in the &lt;i&gt;IAM Identity Center User Guide&lt;/i&gt;.&lt;/p&gt; &lt;/note&gt;

    :param x_amz_sso_bearer_token: The token issued by the &lt;code&gt;CreateToken&lt;/code&gt; API call. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/singlesignon/latest/OIDCAPIReference/API_CreateToken.html\&quot;&gt;CreateToken&lt;/a&gt; in the &lt;i&gt;IAM Identity Center OIDC API Reference Guide&lt;/i&gt;.
    :type x_amz_sso_bearer_token: str
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
    return web.Response(status=200)
