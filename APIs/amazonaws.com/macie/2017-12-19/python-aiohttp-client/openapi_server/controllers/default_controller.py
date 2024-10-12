from typing import List, Dict
from aiohttp import web

from openapi_server.models.associate_member_account_request import AssociateMemberAccountRequest
from openapi_server.models.associate_s3_resources_request import AssociateS3ResourcesRequest
from openapi_server.models.associate_s3_resources_result import AssociateS3ResourcesResult
from openapi_server.models.disassociate_member_account_request import DisassociateMemberAccountRequest
from openapi_server.models.disassociate_s3_resources_request import DisassociateS3ResourcesRequest
from openapi_server.models.disassociate_s3_resources_result import DisassociateS3ResourcesResult
from openapi_server.models.list_member_accounts_request import ListMemberAccountsRequest
from openapi_server.models.list_member_accounts_result import ListMemberAccountsResult
from openapi_server.models.list_s3_resources_request import ListS3ResourcesRequest
from openapi_server.models.list_s3_resources_result import ListS3ResourcesResult
from openapi_server.models.update_s3_resources_request import UpdateS3ResourcesRequest
from openapi_server.models.update_s3_resources_result import UpdateS3ResourcesResult
from openapi_server import util


async def associate_member_account(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """associate_member_account

    (Discontinued) Associates a specified Amazon Web Services account with Amazon Macie Classic as a member account.

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
    body = AssociateMemberAccountRequest.from_dict(body)
    return web.Response(status=200)


async def associate_s3_resources(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """associate_s3_resources

    (Discontinued) Associates specified S3 resources with Amazon Macie Classic for monitoring and data classification. If &lt;code&gt;memberAccountId&lt;/code&gt; isn&#39;t specified, the action associates specified S3 resources with Macie Classic for the current Macie Classic administrator account. If &lt;code&gt;memberAccountId&lt;/code&gt; is specified, the action associates specified S3 resources with Macie Classic for the specified member account.

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
    body = AssociateS3ResourcesRequest.from_dict(body)
    return web.Response(status=200)


async def disassociate_member_account(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """disassociate_member_account

    (Discontinued) Removes the specified member account from Amazon Macie Classic.

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
    body = DisassociateMemberAccountRequest.from_dict(body)
    return web.Response(status=200)


async def disassociate_s3_resources(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """disassociate_s3_resources

    (Discontinued) Removes specified S3 resources from being monitored by Amazon Macie Classic. If &lt;code&gt;memberAccountId&lt;/code&gt; isn&#39;t specified, the action removes specified S3 resources from Macie Classic for the current Macie Classic administrator account. If &lt;code&gt;memberAccountId&lt;/code&gt; is specified, the action removes specified S3 resources from Macie Classic for the specified member account.

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
    body = DisassociateS3ResourcesRequest.from_dict(body)
    return web.Response(status=200)


async def list_member_accounts(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_member_accounts

    (Discontinued) Lists all Amazon Macie Classic member accounts for the current Macie Classic administrator account.

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
    body = ListMemberAccountsRequest.from_dict(body)
    return web.Response(status=200)


async def list_s3_resources(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_s3_resources

    (Discontinued) Lists all the S3 resources associated with Amazon Macie Classic. If &lt;code&gt;memberAccountId&lt;/code&gt; isn&#39;t specified, the action lists the S3 resources associated with Macie Classic for the current Macie Classic administrator account. If &lt;code&gt;memberAccountId&lt;/code&gt; is specified, the action lists the S3 resources associated with Macie Classic for the specified member account. 

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
    body = ListS3ResourcesRequest.from_dict(body)
    return web.Response(status=200)


async def update_s3_resources(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_s3_resources

    (Discontinued) Updates the classification types for the specified S3 resources. If &lt;code&gt;memberAccountId&lt;/code&gt; isn&#39;t specified, the action updates the classification types of the S3 resources associated with Amazon Macie Classic for the current Macie Classic administrator account. If &lt;code&gt;memberAccountId&lt;/code&gt; is specified, the action updates the classification types of the S3 resources associated with Macie Classic for the specified member account.

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
    body = UpdateS3ResourcesRequest.from_dict(body)
    return web.Response(status=200)
