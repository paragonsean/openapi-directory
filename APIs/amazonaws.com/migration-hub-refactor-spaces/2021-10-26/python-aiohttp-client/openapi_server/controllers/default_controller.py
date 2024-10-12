from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_application_request import CreateApplicationRequest
from openapi_server.models.create_application_response import CreateApplicationResponse
from openapi_server.models.create_environment_request import CreateEnvironmentRequest
from openapi_server.models.create_environment_response import CreateEnvironmentResponse
from openapi_server.models.create_route_request import CreateRouteRequest
from openapi_server.models.create_route_response import CreateRouteResponse
from openapi_server.models.create_service_request import CreateServiceRequest
from openapi_server.models.create_service_response import CreateServiceResponse
from openapi_server.models.delete_application_response import DeleteApplicationResponse
from openapi_server.models.delete_environment_response import DeleteEnvironmentResponse
from openapi_server.models.delete_route_response import DeleteRouteResponse
from openapi_server.models.delete_service_response import DeleteServiceResponse
from openapi_server.models.get_application_response import GetApplicationResponse
from openapi_server.models.get_environment_response import GetEnvironmentResponse
from openapi_server.models.get_resource_policy_response import GetResourcePolicyResponse
from openapi_server.models.get_route_response import GetRouteResponse
from openapi_server.models.get_service_response import GetServiceResponse
from openapi_server.models.list_applications_response import ListApplicationsResponse
from openapi_server.models.list_environment_vpcs_response import ListEnvironmentVpcsResponse
from openapi_server.models.list_environments_response import ListEnvironmentsResponse
from openapi_server.models.list_routes_response import ListRoutesResponse
from openapi_server.models.list_services_response import ListServicesResponse
from openapi_server.models.list_tags_for_resource_response import ListTagsForResourceResponse
from openapi_server.models.put_resource_policy_request import PutResourcePolicyRequest
from openapi_server.models.tag_resource_request import TagResourceRequest
from openapi_server.models.update_route_request import UpdateRouteRequest
from openapi_server.models.update_route_response import UpdateRouteResponse
from openapi_server import util


async def create_application(request: web.Request, environment_identifier, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_application

    &lt;p&gt;Creates an Amazon Web Services Migration Hub Refactor Spaces application. The account that owns the environment also owns the applications created inside the environment, regardless of the account that creates the application. Refactor Spaces provisions an Amazon API Gateway, API Gateway VPC link, and Network Load Balancer for the application proxy inside your account.&lt;/p&gt; &lt;p&gt;In environments created with a &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/migrationhub-refactor-spaces/latest/APIReference/API_CreateEnvironment.html#migrationhubrefactorspaces-CreateEnvironment-request-NetworkFabricType\&quot;&gt;CreateEnvironment:NetworkFabricType&lt;/a&gt; of &lt;code&gt;NONE&lt;/code&gt; you need to configure &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/whitepapers/latest/aws-vpc-connectivity-options/amazon-vpc-to-amazon-vpc-connectivity-options.html\&quot;&gt; VPC to VPC connectivity&lt;/a&gt; between your service VPC and the application proxy VPC to route traffic through the application proxy to a service with a private URL endpoint. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/migrationhub-refactor-spaces/latest/userguide/getting-started-create-application.html\&quot;&gt; Create an application&lt;/a&gt; in the &lt;i&gt;Refactor Spaces User Guide&lt;/i&gt;. &lt;/p&gt;

    :param environment_identifier: The unique identifier of the environment.
    :type environment_identifier: str
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


async def create_environment(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_environment

    &lt;p&gt;Creates an Amazon Web Services Migration Hub Refactor Spaces environment. The caller owns the environment resource, and all Refactor Spaces applications, services, and routes created within the environment. They are referred to as the &lt;i&gt;environment owner&lt;/i&gt;. The environment owner has cross-account visibility and control of Refactor Spaces resources that are added to the environment by other accounts that the environment is shared with.&lt;/p&gt; &lt;p&gt;When creating an environment with a &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/migrationhub-refactor-spaces/latest/APIReference/API_CreateEnvironment.html#migrationhubrefactorspaces-CreateEnvironment-request-NetworkFabricType\&quot;&gt;CreateEnvironment:NetworkFabricType&lt;/a&gt; of &lt;code&gt;TRANSIT_GATEWAY&lt;/code&gt;, Refactor Spaces provisions a transit gateway to enable services in VPCs to communicate directly across accounts. If &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/migrationhub-refactor-spaces/latest/APIReference/API_CreateEnvironment.html#migrationhubrefactorspaces-CreateEnvironment-request-NetworkFabricType\&quot;&gt;CreateEnvironment:NetworkFabricType&lt;/a&gt; is &lt;code&gt;NONE&lt;/code&gt;, Refactor Spaces does not create a transit gateway and you must use your network infrastructure to route traffic to services with private URL endpoints.&lt;/p&gt;

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
    body = CreateEnvironmentRequest.from_dict(body)
    return web.Response(status=200)


async def create_route(request: web.Request, application_identifier, environment_identifier, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_route

    &lt;p&gt;Creates an Amazon Web Services Migration Hub Refactor Spaces route. The account owner of the service resource is always the environment owner, regardless of which account creates the route. Routes target a service in the application. If an application does not have any routes, then the first route must be created as a &lt;code&gt;DEFAULT&lt;/code&gt; &lt;code&gt;RouteType&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;When created, the default route defaults to an active state so state is not a required input. However, like all other state values the state of the default route can be updated after creation, but only when all other routes are also inactive. Conversely, no route can be active without the default route also being active.&lt;/p&gt; &lt;p&gt;When you create a route, Refactor Spaces configures the Amazon API Gateway to send traffic to the target service as follows:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;URL Endpoints&lt;/b&gt; &lt;/p&gt; &lt;p&gt;If the service has a URL endpoint, and the endpoint resolves to a private IP address, Refactor Spaces routes traffic using the API Gateway VPC link. If a service endpoint resolves to a public IP address, Refactor Spaces routes traffic over the public internet. Services can have HTTP or HTTPS URL endpoints. For HTTPS URLs, publicly-signed certificates are supported. Private Certificate Authorities (CAs) are permitted only if the CA&#39;s domain is also publicly resolvable. &lt;/p&gt; &lt;p&gt;Refactor Spaces automatically resolves the public Domain Name System (DNS) names that are set in &lt;code&gt;CreateService:UrlEndpoint &lt;/code&gt;when you create a service. The DNS names resolve when the DNS time-to-live (TTL) expires, or every 60 seconds for TTLs less than 60 seconds. This periodic DNS resolution ensures that the route configuration remains up-to-date. &lt;/p&gt; &lt;p/&gt; &lt;p&gt; &lt;b&gt;One-time health check&lt;/b&gt; &lt;/p&gt; &lt;p&gt;A one-time health check is performed on the service when either the route is updated from inactive to active, or when it is created with an active state. If the health check fails, the route transitions the route state to &lt;code&gt;FAILED&lt;/code&gt;, an error code of &lt;code&gt;SERVICE_ENDPOINT_HEALTH_CHECK_FAILURE&lt;/code&gt; is provided, and no traffic is sent to the service.&lt;/p&gt; &lt;p&gt;For private URLs, a target group is created on the Network Load Balancer and the load balancer target group runs default target health checks. By default, the health check is run against the service endpoint URL. Optionally, the health check can be performed against a different protocol, port, and/or path using the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/migrationhub-refactor-spaces/latest/APIReference/API_CreateService.html#migrationhubrefactorspaces-CreateService-request-UrlEndpoint\&quot;&gt;CreateService:UrlEndpoint&lt;/a&gt; parameter. All other health check settings for the load balancer use the default values described in the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/elasticloadbalancing/latest/application/target-group-health-checks.html\&quot;&gt;Health checks for your target groups&lt;/a&gt; in the &lt;i&gt;Elastic Load Balancing guide&lt;/i&gt;. The health check is considered successful if at least one target within the target group transitions to a healthy state.&lt;/p&gt; &lt;p/&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;Lambda function endpoints&lt;/b&gt; &lt;/p&gt; &lt;p&gt;If the service has an Lambda function endpoint, then Refactor Spaces configures the Lambda function&#39;s resource policy to allow the application&#39;s API Gateway to invoke the function.&lt;/p&gt; &lt;p&gt;The Lambda function state is checked. If the function is not active, the function configuration is updated so that Lambda resources are provisioned. If the Lambda state is &lt;code&gt;Failed&lt;/code&gt;, then the route creation fails. For more information, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/lambda/latest/dg/API_GetFunctionConfiguration.html#SSS-GetFunctionConfiguration-response-State\&quot;&gt;GetFunctionConfiguration&#39;s State response parameter&lt;/a&gt; in the &lt;i&gt;Lambda Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;A check is performed to determine that a Lambda function with the specified ARN exists. If it does not exist, the health check fails. For public URLs, a connection is opened to the public endpoint. If the URL is not reachable, the health check fails. &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt; &lt;b&gt;Environments without a network bridge&lt;/b&gt; &lt;/p&gt; &lt;p&gt;When you create environments without a network bridge (&lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/migrationhub-refactor-spaces/latest/APIReference/API_CreateEnvironment.html#migrationhubrefactorspaces-CreateEnvironment-request-NetworkFabricType\&quot;&gt;CreateEnvironment:NetworkFabricType&lt;/a&gt; is &lt;code&gt;NONE)&lt;/code&gt; and you use your own networking infrastructure, you need to configure &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/whitepapers/latest/aws-vpc-connectivity-options/amazon-vpc-to-amazon-vpc-connectivity-options.html\&quot;&gt;VPC to VPC connectivity&lt;/a&gt; between your network and the application proxy VPC. Route creation from the application proxy to service endpoints will fail if your network is not configured to connect to the application proxy VPC. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/migrationhub-refactor-spaces/latest/userguide/getting-started-create-role.html\&quot;&gt; Create a route&lt;/a&gt; in the &lt;i&gt;Refactor Spaces User Guide&lt;/i&gt;.&lt;/p&gt; &lt;p/&gt;

    :param application_identifier: The ID of the application within which the route is being created.
    :type application_identifier: str
    :param environment_identifier: The ID of the environment in which the route is created.
    :type environment_identifier: str
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
    body = CreateRouteRequest.from_dict(body)
    return web.Response(status=200)


async def create_service(request: web.Request, application_identifier, environment_identifier, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_service

    &lt;p&gt;Creates an Amazon Web Services Migration Hub Refactor Spaces service. The account owner of the service is always the environment owner, regardless of which account in the environment creates the service. Services have either a URL endpoint in a virtual private cloud (VPC), or a Lambda function endpoint.&lt;/p&gt; &lt;important&gt; &lt;p&gt;If an Amazon Web Services resource is launched in a service VPC, and you want it to be accessible to all of an environment’s services with VPCs and routes, apply the &lt;code&gt;RefactorSpacesSecurityGroup&lt;/code&gt; to the resource. Alternatively, to add more cross-account constraints, apply your own security group.&lt;/p&gt; &lt;/important&gt;

    :param application_identifier: The ID of the application which the service is created.
    :type application_identifier: str
    :param environment_identifier: The ID of the environment in which the service is created.
    :type environment_identifier: str
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
    body = CreateServiceRequest.from_dict(body)
    return web.Response(status=200)


async def delete_application(request: web.Request, application_identifier, environment_identifier, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_application

    Deletes an Amazon Web Services Migration Hub Refactor Spaces application. Before you can delete an application, you must first delete any services or routes within the application.

    :param application_identifier: The ID of the application.
    :type application_identifier: str
    :param environment_identifier: The ID of the environment. 
    :type environment_identifier: str
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


async def delete_environment(request: web.Request, environment_identifier, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_environment

    Deletes an Amazon Web Services Migration Hub Refactor Spaces environment. Before you can delete an environment, you must first delete any applications and services within the environment.

    :param environment_identifier: The ID of the environment. 
    :type environment_identifier: str
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


async def delete_resource_policy(request: web.Request, identifier, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_resource_policy

    Deletes the resource policy set for the environment. 

    :param identifier: Amazon Resource Name (ARN) of the resource associated with the policy. 
    :type identifier: str
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


async def delete_route(request: web.Request, application_identifier, environment_identifier, route_identifier, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_route

    Deletes an Amazon Web Services Migration Hub Refactor Spaces route.

    :param application_identifier: The ID of the application to delete the route from.
    :type application_identifier: str
    :param environment_identifier: The ID of the environment to delete the route from.
    :type environment_identifier: str
    :param route_identifier: The ID of the route to delete.
    :type route_identifier: str
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


async def delete_service(request: web.Request, application_identifier, environment_identifier, service_identifier, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_service

    Deletes an Amazon Web Services Migration Hub Refactor Spaces service. 

    :param application_identifier: &lt;p&gt;Deletes a Refactor Spaces service.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The &lt;code&gt;RefactorSpacesSecurityGroup&lt;/code&gt; security group must be removed from all Amazon Web Services resources in the virtual private cloud (VPC) prior to deleting a service with a URL endpoint in a VPC.&lt;/p&gt; &lt;/note&gt;
    :type application_identifier: str
    :param environment_identifier: The ID of the environment that the service is in.
    :type environment_identifier: str
    :param service_identifier: The ID of the service to delete.
    :type service_identifier: str
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


async def get_application(request: web.Request, application_identifier, environment_identifier, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_application

    Gets an Amazon Web Services Migration Hub Refactor Spaces application.

    :param application_identifier: The ID of the application.
    :type application_identifier: str
    :param environment_identifier: The ID of the environment. 
    :type environment_identifier: str
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


async def get_environment(request: web.Request, environment_identifier, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_environment

    Gets an Amazon Web Services Migration Hub Refactor Spaces environment.

    :param environment_identifier: The ID of the environment.
    :type environment_identifier: str
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


async def get_resource_policy(request: web.Request, identifier, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_resource_policy

    Gets the resource-based permission policy that is set for the given environment. 

    :param identifier: The Amazon Resource Name (ARN) of the resource associated with the policy. 
    :type identifier: str
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


async def get_route(request: web.Request, application_identifier, environment_identifier, route_identifier, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_route

    Gets an Amazon Web Services Migration Hub Refactor Spaces route.

    :param application_identifier: The ID of the application. 
    :type application_identifier: str
    :param environment_identifier: The ID of the environment.
    :type environment_identifier: str
    :param route_identifier: The ID of the route.
    :type route_identifier: str
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


async def get_service(request: web.Request, application_identifier, environment_identifier, service_identifier, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_service

    Gets an Amazon Web Services Migration Hub Refactor Spaces service. 

    :param application_identifier: The ID of the application.
    :type application_identifier: str
    :param environment_identifier: The ID of the environment.
    :type environment_identifier: str
    :param service_identifier: The ID of the service.
    :type service_identifier: str
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


async def list_applications(request: web.Request, environment_identifier, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None, max_results2=None, next_token2=None) -> web.Response:
    """list_applications

    Lists all the Amazon Web Services Migration Hub Refactor Spaces applications within an environment. 

    :param environment_identifier: The ID of the environment. 
    :type environment_identifier: str
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
    :param max_results: The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned &lt;code&gt;nextToken&lt;/code&gt; value.
    :type max_results: int
    :param next_token: The token for the next page of results.
    :type next_token: str
    :param max_results2: Pagination limit
    :type max_results2: str
    :param next_token2: Pagination token
    :type next_token2: str

    """
    return web.Response(status=200)


async def list_environment_vpcs(request: web.Request, environment_identifier, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None, max_results2=None, next_token2=None) -> web.Response:
    """list_environment_vpcs

    Lists all Amazon Web Services Migration Hub Refactor Spaces service virtual private clouds (VPCs) that are part of the environment. 

    :param environment_identifier: The ID of the environment. 
    :type environment_identifier: str
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
    :param max_results: The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned &lt;code&gt;nextToken&lt;/code&gt; value.
    :type max_results: int
    :param next_token: The token for the next page of results.
    :type next_token: str
    :param max_results2: Pagination limit
    :type max_results2: str
    :param next_token2: Pagination token
    :type next_token2: str

    """
    return web.Response(status=200)


async def list_environments(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None, max_results2=None, next_token2=None) -> web.Response:
    """list_environments

    Lists Amazon Web Services Migration Hub Refactor Spaces environments owned by a caller account or shared with the caller account. 

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
    :param max_results: The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned &lt;code&gt;nextToken&lt;/code&gt; value.
    :type max_results: int
    :param next_token: The token for the next page of results.
    :type next_token: str
    :param max_results2: Pagination limit
    :type max_results2: str
    :param next_token2: Pagination token
    :type next_token2: str

    """
    return web.Response(status=200)


async def list_routes(request: web.Request, application_identifier, environment_identifier, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None, max_results2=None, next_token2=None) -> web.Response:
    """list_routes

    Lists all the Amazon Web Services Migration Hub Refactor Spaces routes within an application. 

    :param application_identifier: The ID of the application. 
    :type application_identifier: str
    :param environment_identifier: The ID of the environment. 
    :type environment_identifier: str
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
    :param max_results: The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned &lt;code&gt;nextToken&lt;/code&gt; value.
    :type max_results: int
    :param next_token: The token for the next page of results.
    :type next_token: str
    :param max_results2: Pagination limit
    :type max_results2: str
    :param next_token2: Pagination token
    :type next_token2: str

    """
    return web.Response(status=200)


async def list_services(request: web.Request, application_identifier, environment_identifier, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None, max_results2=None, next_token2=None) -> web.Response:
    """list_services

    Lists all the Amazon Web Services Migration Hub Refactor Spaces services within an application. 

    :param application_identifier: The ID of the application. 
    :type application_identifier: str
    :param environment_identifier: The ID of the environment. 
    :type environment_identifier: str
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
    :param max_results: The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned &lt;code&gt;nextToken&lt;/code&gt; value.
    :type max_results: int
    :param next_token: The token for the next page of results.
    :type next_token: str
    :param max_results2: Pagination limit
    :type max_results2: str
    :param next_token2: Pagination token
    :type next_token2: str

    """
    return web.Response(status=200)


async def list_tags_for_resource(request: web.Request, resource_arn, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """list_tags_for_resource

    Lists the tags of a resource. The caller account must be the same as the resource’s &lt;code&gt;OwnerAccountId&lt;/code&gt;. Listing tags in other accounts is not supported. 

    :param resource_arn: The Amazon Resource Name (ARN) of the resource. 
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


async def put_resource_policy(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """put_resource_policy

    Attaches a resource-based permission policy to the Amazon Web Services Migration Hub Refactor Spaces environment. The policy must contain the same actions and condition statements as the &lt;code&gt;arn:aws:ram::aws:permission/AWSRAMDefaultPermissionRefactorSpacesEnvironment&lt;/code&gt; permission in Resource Access Manager. The policy must not contain new lines or blank lines. 

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
    body = PutResourcePolicyRequest.from_dict(body)
    return web.Response(status=200)


async def tag_resource(request: web.Request, resource_arn, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """tag_resource

    &lt;p&gt;Removes the tags of a given resource. Tags are metadata which can be used to manage a resource. To tag a resource, the caller account must be the same as the resource’s &lt;code&gt;OwnerAccountId&lt;/code&gt;. Tagging resources in other accounts is not supported.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Amazon Web Services Migration Hub Refactor Spaces does not propagate tags to orchestrated resources, such as an environment’s transit gateway.&lt;/p&gt; &lt;/note&gt;

    :param resource_arn: The Amazon Resource Name (ARN) of the resource.
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

    Adds to or modifies the tags of the given resource. Tags are metadata which can be used to manage a resource. To untag a resource, the caller account must be the same as the resource’s &lt;code&gt;OwnerAccountId&lt;/code&gt;. Untagging resources across accounts is not supported. 

    :param resource_arn: The Amazon Resource Name (ARN) of the resource. 
    :type resource_arn: str
    :param tag_keys: The list of keys of the tags to be removed from the resource. 
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


async def update_route(request: web.Request, application_identifier, environment_identifier, route_identifier, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_route

     Updates an Amazon Web Services Migration Hub Refactor Spaces route. 

    :param application_identifier:  The ID of the application within which the route is being updated. 
    :type application_identifier: str
    :param environment_identifier:  The ID of the environment in which the route is being updated. 
    :type environment_identifier: str
    :param route_identifier:  The unique identifier of the route to update. 
    :type route_identifier: str
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
    body = UpdateRouteRequest.from_dict(body)
    return web.Response(status=200)
