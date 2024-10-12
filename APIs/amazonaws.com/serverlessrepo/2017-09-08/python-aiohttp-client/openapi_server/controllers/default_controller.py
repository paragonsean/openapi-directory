from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_application_request import CreateApplicationRequest
from openapi_server.models.create_application_response import CreateApplicationResponse
from openapi_server.models.create_application_version_request import CreateApplicationVersionRequest
from openapi_server.models.create_application_version_response import CreateApplicationVersionResponse
from openapi_server.models.create_cloud_formation_change_set_request import CreateCloudFormationChangeSetRequest
from openapi_server.models.create_cloud_formation_change_set_response import CreateCloudFormationChangeSetResponse
from openapi_server.models.create_cloud_formation_template_request import CreateCloudFormationTemplateRequest
from openapi_server.models.create_cloud_formation_template_response import CreateCloudFormationTemplateResponse
from openapi_server.models.get_application_policy_response import GetApplicationPolicyResponse
from openapi_server.models.get_application_response import GetApplicationResponse
from openapi_server.models.get_cloud_formation_template_response import GetCloudFormationTemplateResponse
from openapi_server.models.list_application_dependencies_response import ListApplicationDependenciesResponse
from openapi_server.models.list_application_versions_response import ListApplicationVersionsResponse
from openapi_server.models.list_applications_response import ListApplicationsResponse
from openapi_server.models.put_application_policy_request import PutApplicationPolicyRequest
from openapi_server.models.put_application_policy_response import PutApplicationPolicyResponse
from openapi_server.models.unshare_application_request import UnshareApplicationRequest
from openapi_server.models.update_application_request import UpdateApplicationRequest
from openapi_server.models.update_application_response import UpdateApplicationResponse
from openapi_server import util


async def create_application(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_application

    Creates an application, optionally including an AWS SAM file to create the first application version in the same call.

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
    body = CreateApplicationRequest.from_dict(body)
    return web.Response(status=200)


async def create_application_version(request: web.Request, application_id, semantic_version, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_application_version

    Creates an application version.

    :param application_id: The Amazon Resource Name (ARN) of the application.
    :type application_id: str
    :param semantic_version: The semantic version of the new version.
    :type semantic_version: str
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
    body = CreateApplicationVersionRequest.from_dict(body)
    return web.Response(status=200)


async def create_cloud_formation_change_set(request: web.Request, application_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_cloud_formation_change_set

    Creates an AWS CloudFormation change set for the given application.

    :param application_id: The Amazon Resource Name (ARN) of the application.
    :type application_id: str
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
    body = CreateCloudFormationChangeSetRequest.from_dict(body)
    return web.Response(status=200)


async def create_cloud_formation_template(request: web.Request, application_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_cloud_formation_template

    Creates an AWS CloudFormation template.

    :param application_id: The Amazon Resource Name (ARN) of the application.
    :type application_id: str
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
    body = CreateCloudFormationTemplateRequest.from_dict(body)
    return web.Response(status=200)


async def delete_application(request: web.Request, application_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_application

    Deletes the specified application.

    :param application_id: The Amazon Resource Name (ARN) of the application.
    :type application_id: str
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


async def get_application(request: web.Request, application_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, semantic_version=None) -> web.Response:
    """get_application

    Gets the specified application.

    :param application_id: The Amazon Resource Name (ARN) of the application.
    :type application_id: str
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
    :param semantic_version: The semantic version of the application to get.
    :type semantic_version: str

    """
    return web.Response(status=200)


async def get_application_policy(request: web.Request, application_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_application_policy

    Retrieves the policy for the application.

    :param application_id: The Amazon Resource Name (ARN) of the application.
    :type application_id: str
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


async def get_cloud_formation_template(request: web.Request, application_id, template_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_cloud_formation_template

    Gets the specified AWS CloudFormation template.

    :param application_id: The Amazon Resource Name (ARN) of the application.
    :type application_id: str
    :param template_id: &lt;p&gt;The UUID returned by CreateCloudFormationTemplate.&lt;/p&gt;&lt;p&gt;Pattern: [0-9a-fA-F]{8}\\-[0-9a-fA-F]{4}\\-[0-9a-fA-F]{4}\\-[0-9a-fA-F]{4}\\-[0-9a-fA-F]{12}&lt;/p&gt;
    :type template_id: str
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


async def list_application_dependencies(request: web.Request, application_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_items=None, next_token=None, semantic_version=None, max_items2=None, next_token2=None) -> web.Response:
    """list_application_dependencies

    Retrieves the list of applications nested in the containing application.

    :param application_id: The Amazon Resource Name (ARN) of the application.
    :type application_id: str
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
    :param max_items: The total number of items to return.
    :type max_items: int
    :param next_token: A token to specify where to start paginating.
    :type next_token: str
    :param semantic_version: The semantic version of the application to get.
    :type semantic_version: str
    :param max_items2: Pagination limit
    :type max_items2: str
    :param next_token2: Pagination token
    :type next_token2: str

    """
    return web.Response(status=200)


async def list_application_versions(request: web.Request, application_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_items=None, next_token=None, max_items2=None, next_token2=None) -> web.Response:
    """list_application_versions

    Lists versions for the specified application.

    :param application_id: The Amazon Resource Name (ARN) of the application.
    :type application_id: str
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
    :param max_items: The total number of items to return.
    :type max_items: int
    :param next_token: A token to specify where to start paginating.
    :type next_token: str
    :param max_items2: Pagination limit
    :type max_items2: str
    :param next_token2: Pagination token
    :type next_token2: str

    """
    return web.Response(status=200)


async def list_applications(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_items=None, next_token=None, max_items2=None, next_token2=None) -> web.Response:
    """list_applications

    Lists applications owned by the requester.

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
    :param max_items: The total number of items to return.
    :type max_items: int
    :param next_token: A token to specify where to start paginating.
    :type next_token: str
    :param max_items2: Pagination limit
    :type max_items2: str
    :param next_token2: Pagination token
    :type next_token2: str

    """
    return web.Response(status=200)


async def put_application_policy(request: web.Request, application_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """put_application_policy

    Sets the permission policy for an application. For the list of actions supported for this operation, see  &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/serverlessrepo/latest/devguide/access-control-resource-based.html#application-permissions\&quot;&gt;Application   Permissions&lt;/a&gt;  .

    :param application_id: The Amazon Resource Name (ARN) of the application.
    :type application_id: str
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
    body = PutApplicationPolicyRequest.from_dict(body)
    return web.Response(status=200)


async def unshare_application(request: web.Request, application_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """unshare_application

    &lt;p&gt;Unshares an application from an AWS Organization.&lt;/p&gt;&lt;p&gt;This operation can be called only from the organization&#39;s master account.&lt;/p&gt;

    :param application_id: The Amazon Resource Name (ARN) of the application.
    :type application_id: str
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
    body = UnshareApplicationRequest.from_dict(body)
    return web.Response(status=200)


async def update_application(request: web.Request, application_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_application

    Updates the specified application.

    :param application_id: The Amazon Resource Name (ARN) of the application.
    :type application_id: str
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
    body = UpdateApplicationRequest.from_dict(body)
    return web.Response(status=200)
