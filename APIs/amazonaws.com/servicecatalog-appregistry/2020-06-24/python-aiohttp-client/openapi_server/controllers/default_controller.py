from typing import List, Dict
from aiohttp import web

from openapi_server.models.associate_attribute_group_response import AssociateAttributeGroupResponse
from openapi_server.models.associate_resource_response import AssociateResourceResponse
from openapi_server.models.create_application_request import CreateApplicationRequest
from openapi_server.models.create_application_response import CreateApplicationResponse
from openapi_server.models.create_attribute_group_request import CreateAttributeGroupRequest
from openapi_server.models.create_attribute_group_response import CreateAttributeGroupResponse
from openapi_server.models.delete_application_response import DeleteApplicationResponse
from openapi_server.models.delete_attribute_group_response import DeleteAttributeGroupResponse
from openapi_server.models.disassociate_attribute_group_response import DisassociateAttributeGroupResponse
from openapi_server.models.disassociate_resource_response import DisassociateResourceResponse
from openapi_server.models.get_application_response import GetApplicationResponse
from openapi_server.models.get_associated_resource_response import GetAssociatedResourceResponse
from openapi_server.models.get_attribute_group_response import GetAttributeGroupResponse
from openapi_server.models.get_configuration_response import GetConfigurationResponse
from openapi_server.models.list_applications_response import ListApplicationsResponse
from openapi_server.models.list_associated_attribute_groups_response import ListAssociatedAttributeGroupsResponse
from openapi_server.models.list_associated_resources_response import ListAssociatedResourcesResponse
from openapi_server.models.list_attribute_groups_for_application_response import ListAttributeGroupsForApplicationResponse
from openapi_server.models.list_attribute_groups_response import ListAttributeGroupsResponse
from openapi_server.models.list_tags_for_resource_response import ListTagsForResourceResponse
from openapi_server.models.put_configuration_request import PutConfigurationRequest
from openapi_server.models.sync_resource_response import SyncResourceResponse
from openapi_server.models.tag_resource_request import TagResourceRequest
from openapi_server.models.update_application_request import UpdateApplicationRequest
from openapi_server.models.update_application_response import UpdateApplicationResponse
from openapi_server.models.update_attribute_group_request import UpdateAttributeGroupRequest
from openapi_server.models.update_attribute_group_response import UpdateAttributeGroupResponse
from openapi_server import util


async def associate_attribute_group(request: web.Request, application, attribute_group, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """associate_attribute_group

    Associates an attribute group with an application to augment the application&#39;s metadata with the group&#39;s attributes. This feature enables applications to be described with user-defined details that are machine-readable, such as third-party integrations.

    :param application:  The name, ID, or ARN of the application. 
    :type application: str
    :param attribute_group:  The name, ID, or ARN of the attribute group that holds the attributes to describe the application. 
    :type attribute_group: str
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


async def associate_resource(request: web.Request, application, resource_type, resource, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """associate_resource

     Associates a resource with an application. The resource can be specified by its ARN or name. The application can be specified by ARN, ID, or name. 

    :param application:  The name, ID, or ARN of the application. 
    :type application: str
    :param resource_type: The type of resource of which the application will be associated.
    :type resource_type: str
    :param resource: The name or ID of the resource of which the application will be associated.
    :type resource: str
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


async def create_application(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_application

    Creates a new application that is the top-level node in a hierarchy of related cloud resource abstractions.

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


async def create_attribute_group(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_attribute_group

    Creates a new attribute group as a container for user-defined attributes. This feature enables users to have full control over their cloud application&#39;s metadata in a rich machine-readable format to facilitate integration with automated workflows and third-party tools.

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
    body = CreateAttributeGroupRequest.from_dict(body)
    return web.Response(status=200)


async def delete_application(request: web.Request, application, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_application

    Deletes an application that is specified either by its application ID, name, or ARN. All associated attribute groups and resources must be disassociated from it before deleting an application.

    :param application:  The name, ID, or ARN of the application. 
    :type application: str
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


async def delete_attribute_group(request: web.Request, attribute_group, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_attribute_group

    Deletes an attribute group, specified either by its attribute group ID, name, or ARN.

    :param attribute_group:  The name, ID, or ARN of the attribute group that holds the attributes to describe the application. 
    :type attribute_group: str
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


async def disassociate_attribute_group(request: web.Request, application, attribute_group, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """disassociate_attribute_group

    Disassociates an attribute group from an application to remove the extra attributes contained in the attribute group from the application&#39;s metadata. This operation reverts &lt;code&gt;AssociateAttributeGroup&lt;/code&gt;.

    :param application:  The name, ID, or ARN of the application. 
    :type application: str
    :param attribute_group:  The name, ID, or ARN of the attribute group that holds the attributes to describe the application. 
    :type attribute_group: str
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


async def disassociate_resource(request: web.Request, application, resource_type, resource, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """disassociate_resource

    Disassociates a resource from application. Both the resource and the application can be specified either by ID or name.

    :param application: The name or ID of the application.
    :type application: str
    :param resource_type: The type of the resource that is being disassociated.
    :type resource_type: str
    :param resource: The name or ID of the resource.
    :type resource: str
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


async def get_application(request: web.Request, application, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_application

     Retrieves metadata information about one of your applications. The application can be specified by its ARN, ID, or name (which is unique within one account in one region at a given point in time). Specify by ARN or ID in automated workflows if you want to make sure that the exact same application is returned or a &lt;code&gt;ResourceNotFoundException&lt;/code&gt; is thrown, avoiding the ABA addressing problem. 

    :param application:  The name, ID, or ARN of the application. 
    :type application: str
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


async def get_associated_resource(request: web.Request, application, resource_type, resource, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_associated_resource

    Gets the resource associated with the application.

    :param application:  The name, ID, or ARN of the application. 
    :type application: str
    :param resource_type: The type of resource associated with the application.
    :type resource_type: str
    :param resource: The name or ID of the resource associated with the application.
    :type resource: str
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


async def get_attribute_group(request: web.Request, attribute_group, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_attribute_group

     Retrieves an attribute group by its ARN, ID, or name. The attribute group can be specified by its ARN, ID, or name. 

    :param attribute_group:  The name, ID, or ARN of the attribute group that holds the attributes to describe the application. 
    :type attribute_group: str
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


async def get_configuration(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_configuration

     Retrieves a &lt;code&gt;TagKey&lt;/code&gt; configuration from an account. 

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


async def list_applications(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None, max_results=None) -> web.Response:
    """list_applications

    Retrieves a list of all of your applications. Results are paginated.

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
    :param next_token: The token to use to get the next page of results after a previous API call. 
    :type next_token: str
    :param max_results: The upper bound of the number of results to return (cannot exceed 25). If this parameter is omitted, it defaults to 25. This value is optional.
    :type max_results: int

    """
    return web.Response(status=200)


async def list_associated_attribute_groups(request: web.Request, application, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None, max_results=None) -> web.Response:
    """list_associated_attribute_groups

    Lists all attribute groups that are associated with specified application. Results are paginated.

    :param application: The name or ID of the application.
    :type application: str
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
    :param next_token: The token to use to get the next page of results after a previous API call. 
    :type next_token: str
    :param max_results: The upper bound of the number of results to return (cannot exceed 25). If this parameter is omitted, it defaults to 25. This value is optional.
    :type max_results: int

    """
    return web.Response(status=200)


async def list_associated_resources(request: web.Request, application, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None, max_results=None) -> web.Response:
    """list_associated_resources

    &lt;p&gt; Lists all of the resources that are associated with the specified application. Results are paginated. &lt;/p&gt; &lt;note&gt; &lt;p&gt; If you share an application, and a consumer account associates a tag query to the application, all of the users who can access the application can also view the tag values in all accounts that are associated with it using this API. &lt;/p&gt; &lt;/note&gt;

    :param application:  The name, ID, or ARN of the application. 
    :type application: str
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
    :param next_token: The token to use to get the next page of results after a previous API call. 
    :type next_token: str
    :param max_results: The upper bound of the number of results to return (cannot exceed 25). If this parameter is omitted, it defaults to 25. This value is optional.
    :type max_results: int

    """
    return web.Response(status=200)


async def list_attribute_groups(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None, max_results=None) -> web.Response:
    """list_attribute_groups

    Lists all attribute groups which you have access to. Results are paginated.

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
    :param next_token: The token to use to get the next page of results after a previous API call. 
    :type next_token: str
    :param max_results: The upper bound of the number of results to return (cannot exceed 25). If this parameter is omitted, it defaults to 25. This value is optional.
    :type max_results: int

    """
    return web.Response(status=200)


async def list_attribute_groups_for_application(request: web.Request, application, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None, max_results=None) -> web.Response:
    """list_attribute_groups_for_application

    Lists the details of all attribute groups associated with a specific application. The results display in pages.

    :param application: The name or ID of the application.
    :type application: str
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
    :param next_token: This token retrieves the next page of results after a previous API call.
    :type next_token: str
    :param max_results: The upper bound of the number of results to return. The value cannot exceed 25. If you omit this parameter, it defaults to 25. This value is optional.
    :type max_results: int

    """
    return web.Response(status=200)


async def list_tags_for_resource(request: web.Request, resource_arn, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """list_tags_for_resource

    Lists all of the tags on the resource.

    :param resource_arn: The Amazon resource name (ARN) that specifies the resource.
    :type resource_arn: str
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


async def put_configuration(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """put_configuration

     Associates a &lt;code&gt;TagKey&lt;/code&gt; configuration to an account. 

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
    body = PutConfigurationRequest.from_dict(body)
    return web.Response(status=200)


async def sync_resource(request: web.Request, resource_type, resource, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """sync_resource

    &lt;p&gt;Syncs the resource with current AppRegistry records.&lt;/p&gt; &lt;p&gt;Specifically, the resource’s AppRegistry system tags sync with its associated application. We remove the resource&#39;s AppRegistry system tags if it does not associate with the application. The caller must have permissions to read and update the resource.&lt;/p&gt;

    :param resource_type: The type of resource of which the application will be associated.
    :type resource_type: str
    :param resource: An entity you can work with and specify with a name or ID. Examples include an Amazon EC2 instance, an Amazon Web Services CloudFormation stack, or an Amazon S3 bucket.
    :type resource: str
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


async def tag_resource(request: web.Request, resource_arn, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """tag_resource

    &lt;p&gt;Assigns one or more tags (key-value pairs) to the specified resource.&lt;/p&gt; &lt;p&gt;Each tag consists of a key and an optional value. If a tag with the same key is already associated with the resource, this action updates its value.&lt;/p&gt; &lt;p&gt;This operation returns an empty response if the call was successful.&lt;/p&gt;

    :param resource_arn: The Amazon resource name (ARN) that specifies the resource.
    :type resource_arn: str
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
    body = TagResourceRequest.from_dict(body)
    return web.Response(status=200)


async def untag_resource(request: web.Request, resource_arn, tag_keys, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """untag_resource

    &lt;p&gt;Removes tags from a resource.&lt;/p&gt; &lt;p&gt;This operation returns an empty response if the call was successful.&lt;/p&gt;

    :param resource_arn: The Amazon resource name (ARN) that specifies the resource.
    :type resource_arn: str
    :param tag_keys: A list of the tag keys to remove from the specified resource.
    :type tag_keys: List[str]
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


async def update_application(request: web.Request, application, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_application

    Updates an existing application with new attributes.

    :param application:  The name, ID, or ARN of the application that will be updated. 
    :type application: str
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


async def update_attribute_group(request: web.Request, attribute_group, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_attribute_group

    Updates an existing attribute group with new details. 

    :param attribute_group:  The name, ID, or ARN of the attribute group that holds the attributes to describe the application. 
    :type attribute_group: str
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
    body = UpdateAttributeGroupRequest.from_dict(body)
    return web.Response(status=200)
