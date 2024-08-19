from typing import List, Dict
from aiohttp import web

from openapi_server.models.account import Account
from openapi_server.models.api_key import ApiKey
from openapi_server.models.api_key_ids import ApiKeyIds
from openapi_server.models.api_keys import ApiKeys
from openapi_server.models.authorizer import Authorizer
from openapi_server.models.authorizers import Authorizers
from openapi_server.models.base_path_mapping import BasePathMapping
from openapi_server.models.base_path_mappings import BasePathMappings
from openapi_server.models.client_certificate import ClientCertificate
from openapi_server.models.client_certificates import ClientCertificates
from openapi_server.models.create_api_key_request import CreateApiKeyRequest
from openapi_server.models.create_authorizer_request import CreateAuthorizerRequest
from openapi_server.models.create_base_path_mapping_request import CreateBasePathMappingRequest
from openapi_server.models.create_deployment_request import CreateDeploymentRequest
from openapi_server.models.create_documentation_part_request import CreateDocumentationPartRequest
from openapi_server.models.create_documentation_version_request import CreateDocumentationVersionRequest
from openapi_server.models.create_domain_name_request import CreateDomainNameRequest
from openapi_server.models.create_model_request import CreateModelRequest
from openapi_server.models.create_request_validator_request import CreateRequestValidatorRequest
from openapi_server.models.create_resource_request import CreateResourceRequest
from openapi_server.models.create_rest_api_request import CreateRestApiRequest
from openapi_server.models.create_stage_request import CreateStageRequest
from openapi_server.models.create_usage_plan_key_request import CreateUsagePlanKeyRequest
from openapi_server.models.create_usage_plan_request import CreateUsagePlanRequest
from openapi_server.models.create_vpc_link_request import CreateVpcLinkRequest
from openapi_server.models.deployment import Deployment
from openapi_server.models.deployments import Deployments
from openapi_server.models.documentation_part import DocumentationPart
from openapi_server.models.documentation_part_ids import DocumentationPartIds
from openapi_server.models.documentation_parts import DocumentationParts
from openapi_server.models.documentation_version import DocumentationVersion
from openapi_server.models.documentation_versions import DocumentationVersions
from openapi_server.models.domain_name import DomainName
from openapi_server.models.domain_names import DomainNames
from openapi_server.models.export_response import ExportResponse
from openapi_server.models.gateway_response import GatewayResponse
from openapi_server.models.gateway_responses import GatewayResponses
from openapi_server.models.generate_client_certificate_request import GenerateClientCertificateRequest
from openapi_server.models.import_api_keys_request import ImportApiKeysRequest
from openapi_server.models.import_documentation_parts_request import ImportDocumentationPartsRequest
from openapi_server.models.import_rest_api_request import ImportRestApiRequest
from openapi_server.models.integration import Integration
from openapi_server.models.integration_response import IntegrationResponse
from openapi_server.models.method import Method
from openapi_server.models.method_response import MethodResponse
from openapi_server.models.model import Model
from openapi_server.models.models import Models
from openapi_server.models.put_gateway_response_request import PutGatewayResponseRequest
from openapi_server.models.put_integration_request import PutIntegrationRequest
from openapi_server.models.put_integration_response_request import PutIntegrationResponseRequest
from openapi_server.models.put_method_request import PutMethodRequest
from openapi_server.models.put_method_response_request import PutMethodResponseRequest
from openapi_server.models.put_rest_api_request import PutRestApiRequest
from openapi_server.models.request_validator import RequestValidator
from openapi_server.models.request_validators import RequestValidators
from openapi_server.models.resource import Resource
from openapi_server.models.resources import Resources
from openapi_server.models.rest_api import RestApi
from openapi_server.models.rest_apis import RestApis
from openapi_server.models.sdk_response import SdkResponse
from openapi_server.models.sdk_type import SdkType
from openapi_server.models.sdk_types import SdkTypes
from openapi_server.models.stage import Stage
from openapi_server.models.stages import Stages
from openapi_server.models.tag_resource_request import TagResourceRequest
from openapi_server.models.tags import Tags
from openapi_server.models.template import Template
from openapi_server.models.test_invoke_authorizer_request import TestInvokeAuthorizerRequest
from openapi_server.models.test_invoke_authorizer_response import TestInvokeAuthorizerResponse
from openapi_server.models.test_invoke_method_request import TestInvokeMethodRequest
from openapi_server.models.test_invoke_method_response import TestInvokeMethodResponse
from openapi_server.models.update_api_key_request import UpdateApiKeyRequest
from openapi_server.models.usage import Usage
from openapi_server.models.usage_plan import UsagePlan
from openapi_server.models.usage_plan_key import UsagePlanKey
from openapi_server.models.usage_plan_keys import UsagePlanKeys
from openapi_server.models.usage_plans import UsagePlans
from openapi_server.models.vpc_link import VpcLink
from openapi_server.models.vpc_links import VpcLinks
from openapi_server import util


async def create_api_key(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_api_key

    Create an ApiKey resource. 

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
    body = CreateApiKeyRequest.from_dict(body)
    return web.Response(status=200)


async def create_authorizer(request: web.Request, restapi_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_authorizer

    Adds a new Authorizer resource to an existing RestApi resource.

    :param restapi_id: The string identifier of the associated RestApi.
    :type restapi_id: str
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
    body = CreateAuthorizerRequest.from_dict(body)
    return web.Response(status=200)


async def create_base_path_mapping(request: web.Request, domain_name, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_base_path_mapping

    Creates a new BasePathMapping resource.

    :param domain_name: The domain name of the BasePathMapping resource to create.
    :type domain_name: str
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
    body = CreateBasePathMappingRequest.from_dict(body)
    return web.Response(status=200)


async def create_deployment(request: web.Request, restapi_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_deployment

    Creates a Deployment resource, which makes a specified RestApi callable over the internet.

    :param restapi_id: The string identifier of the associated RestApi.
    :type restapi_id: str
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
    body = CreateDeploymentRequest.from_dict(body)
    return web.Response(status=200)


async def create_documentation_part(request: web.Request, restapi_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_documentation_part

    Creates a documentation part.

    :param restapi_id: The string identifier of the associated RestApi.
    :type restapi_id: str
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
    body = CreateDocumentationPartRequest.from_dict(body)
    return web.Response(status=200)


async def create_documentation_version(request: web.Request, restapi_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_documentation_version

    Creates a documentation version

    :param restapi_id: The string identifier of the associated RestApi.
    :type restapi_id: str
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
    body = CreateDocumentationVersionRequest.from_dict(body)
    return web.Response(status=200)


async def create_domain_name(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_domain_name

    Creates a new domain name.

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
    body = CreateDomainNameRequest.from_dict(body)
    return web.Response(status=200)


async def create_model(request: web.Request, restapi_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_model

    Adds a new Model resource to an existing RestApi resource.

    :param restapi_id: The RestApi identifier under which the Model will be created.
    :type restapi_id: str
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
    body = CreateModelRequest.from_dict(body)
    return web.Response(status=200)


async def create_request_validator(request: web.Request, restapi_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_request_validator

    Creates a RequestValidator of a given RestApi.

    :param restapi_id: The string identifier of the associated RestApi.
    :type restapi_id: str
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
    body = CreateRequestValidatorRequest.from_dict(body)
    return web.Response(status=200)


async def create_resource(request: web.Request, restapi_id, parent_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_resource

    Creates a Resource resource.

    :param restapi_id: The string identifier of the associated RestApi.
    :type restapi_id: str
    :param parent_id: The parent resource&#39;s identifier.
    :type parent_id: str
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
    body = CreateResourceRequest.from_dict(body)
    return web.Response(status=200)


async def create_rest_api(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_rest_api

    Creates a new RestApi resource.

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
    body = CreateRestApiRequest.from_dict(body)
    return web.Response(status=200)


async def create_stage(request: web.Request, restapi_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_stage

    Creates a new Stage resource that references a pre-existing Deployment for the API. 

    :param restapi_id: The string identifier of the associated RestApi.
    :type restapi_id: str
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
    body = CreateStageRequest.from_dict(body)
    return web.Response(status=200)


async def create_usage_plan(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_usage_plan

    Creates a usage plan with the throttle and quota limits, as well as the associated API stages, specified in the payload. 

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
    body = CreateUsagePlanRequest.from_dict(body)
    return web.Response(status=200)


async def create_usage_plan_key(request: web.Request, usageplan_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_usage_plan_key

    Creates a usage plan key for adding an existing API key to a usage plan.

    :param usageplan_id: The Id of the UsagePlan resource representing the usage plan containing the to-be-created UsagePlanKey resource representing a plan customer.
    :type usageplan_id: str
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
    body = CreateUsagePlanKeyRequest.from_dict(body)
    return web.Response(status=200)


async def create_vpc_link(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_vpc_link

    Creates a VPC link, under the caller&#39;s account in a selected region, in an asynchronous operation that typically takes 2-4 minutes to complete and become operational. The caller must have permissions to create and update VPC Endpoint services.

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
    body = CreateVpcLinkRequest.from_dict(body)
    return web.Response(status=200)


async def delete_api_key(request: web.Request, api_key, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_api_key

    Deletes the ApiKey resource.

    :param api_key: The identifier of the ApiKey resource to be deleted.
    :type api_key: str
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


async def delete_authorizer(request: web.Request, restapi_id, authorizer_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_authorizer

    Deletes an existing Authorizer resource.

    :param restapi_id: The string identifier of the associated RestApi.
    :type restapi_id: str
    :param authorizer_id: The identifier of the Authorizer resource.
    :type authorizer_id: str
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


async def delete_base_path_mapping(request: web.Request, domain_name, base_path, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_base_path_mapping

    Deletes the BasePathMapping resource.

    :param domain_name: The domain name of the BasePathMapping resource to delete.
    :type domain_name: str
    :param base_path: &lt;p&gt;The base path name of the BasePathMapping resource to delete.&lt;/p&gt; &lt;p&gt;To specify an empty base path, set this parameter to &lt;code&gt;&#39;(none)&#39;&lt;/code&gt;.&lt;/p&gt;
    :type base_path: str
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


async def delete_client_certificate(request: web.Request, clientcertificate_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_client_certificate

    Deletes the ClientCertificate resource.

    :param clientcertificate_id: The identifier of the ClientCertificate resource to be deleted.
    :type clientcertificate_id: str
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


async def delete_deployment(request: web.Request, restapi_id, deployment_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_deployment

    Deletes a Deployment resource. Deleting a deployment will only succeed if there are no Stage resources associated with it.

    :param restapi_id: The string identifier of the associated RestApi.
    :type restapi_id: str
    :param deployment_id: The identifier of the Deployment resource to delete.
    :type deployment_id: str
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


async def delete_documentation_part(request: web.Request, restapi_id, part_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_documentation_part

    Deletes a documentation part

    :param restapi_id: The string identifier of the associated RestApi.
    :type restapi_id: str
    :param part_id: The identifier of the to-be-deleted documentation part.
    :type part_id: str
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


async def delete_documentation_version(request: web.Request, restapi_id, doc_version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_documentation_version

    Deletes a documentation version.

    :param restapi_id: The string identifier of the associated RestApi.
    :type restapi_id: str
    :param doc_version: The version identifier of a to-be-deleted documentation snapshot.
    :type doc_version: str
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


async def delete_domain_name(request: web.Request, domain_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_domain_name

    Deletes the DomainName resource.

    :param domain_name: The name of the DomainName resource to be deleted.
    :type domain_name: str
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


async def delete_gateway_response(request: web.Request, restapi_id, response_type, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_gateway_response

    Clears any customization of a GatewayResponse of a specified response type on the given RestApi and resets it with the default settings.

    :param restapi_id: The string identifier of the associated RestApi.
    :type restapi_id: str
    :param response_type: The response type of the associated GatewayResponse.
    :type response_type: str
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


async def delete_integration(request: web.Request, restapi_id, resource_id, http_method, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_integration

    Represents a delete integration.

    :param restapi_id: The string identifier of the associated RestApi.
    :type restapi_id: str
    :param resource_id: Specifies a delete integration request&#39;s resource identifier.
    :type resource_id: str
    :param http_method: Specifies a delete integration request&#39;s HTTP method.
    :type http_method: str
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


async def delete_integration_response(request: web.Request, restapi_id, resource_id, http_method, status_code, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_integration_response

    Represents a delete integration response.

    :param restapi_id: The string identifier of the associated RestApi.
    :type restapi_id: str
    :param resource_id: Specifies a delete integration response request&#39;s resource identifier.
    :type resource_id: str
    :param http_method: Specifies a delete integration response request&#39;s HTTP method.
    :type http_method: str
    :param status_code: Specifies a delete integration response request&#39;s status code.
    :type status_code: str
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


async def delete_method(request: web.Request, restapi_id, resource_id, http_method, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_method

    Deletes an existing Method resource.

    :param restapi_id: The string identifier of the associated RestApi.
    :type restapi_id: str
    :param resource_id: The Resource identifier for the Method resource.
    :type resource_id: str
    :param http_method: The HTTP verb of the Method resource.
    :type http_method: str
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


async def delete_method_response(request: web.Request, restapi_id, resource_id, http_method, status_code, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_method_response

    Deletes an existing MethodResponse resource.

    :param restapi_id: The string identifier of the associated RestApi.
    :type restapi_id: str
    :param resource_id: The Resource identifier for the MethodResponse resource.
    :type resource_id: str
    :param http_method: The HTTP verb of the Method resource.
    :type http_method: str
    :param status_code: The status code identifier for the MethodResponse resource.
    :type status_code: str
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


async def delete_model(request: web.Request, restapi_id, model_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_model

    Deletes a model.

    :param restapi_id: The string identifier of the associated RestApi.
    :type restapi_id: str
    :param model_name: The name of the model to delete.
    :type model_name: str
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


async def delete_request_validator(request: web.Request, restapi_id, requestvalidator_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_request_validator

    Deletes a RequestValidator of a given RestApi.

    :param restapi_id: The string identifier of the associated RestApi.
    :type restapi_id: str
    :param requestvalidator_id: The identifier of the RequestValidator to be deleted.
    :type requestvalidator_id: str
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


async def delete_resource(request: web.Request, restapi_id, resource_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_resource

    Deletes a Resource resource.

    :param restapi_id: The string identifier of the associated RestApi.
    :type restapi_id: str
    :param resource_id: The identifier of the Resource resource.
    :type resource_id: str
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


async def delete_rest_api(request: web.Request, restapi_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_rest_api

    Deletes the specified API.

    :param restapi_id: The string identifier of the associated RestApi.
    :type restapi_id: str
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


async def delete_stage(request: web.Request, restapi_id, stage_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_stage

    Deletes a Stage resource.

    :param restapi_id: The string identifier of the associated RestApi.
    :type restapi_id: str
    :param stage_name: The name of the Stage resource to delete.
    :type stage_name: str
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


async def delete_usage_plan(request: web.Request, usageplan_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_usage_plan

    Deletes a usage plan of a given plan Id.

    :param usageplan_id: The Id of the to-be-deleted usage plan.
    :type usageplan_id: str
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


async def delete_usage_plan_key(request: web.Request, usageplan_id, key_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_usage_plan_key

    Deletes a usage plan key and remove the underlying API key from the associated usage plan.

    :param usageplan_id: The Id of the UsagePlan resource representing the usage plan containing the to-be-deleted UsagePlanKey resource representing a plan customer.
    :type usageplan_id: str
    :param key_id: The Id of the UsagePlanKey resource to be deleted.
    :type key_id: str
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


async def delete_vpc_link(request: web.Request, vpclink_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_vpc_link

    Deletes an existing VpcLink of a specified identifier.

    :param vpclink_id: The identifier of the VpcLink. It is used in an Integration to reference this VpcLink.
    :type vpclink_id: str
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


async def flush_stage_authorizers_cache(request: web.Request, restapi_id, stage_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """flush_stage_authorizers_cache

    Flushes all authorizer cache entries on a stage.

    :param restapi_id: The string identifier of the associated RestApi.
    :type restapi_id: str
    :param stage_name: The name of the stage to flush.
    :type stage_name: str
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


async def flush_stage_cache(request: web.Request, restapi_id, stage_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """flush_stage_cache

    Flushes a stage&#39;s cache.

    :param restapi_id: The string identifier of the associated RestApi.
    :type restapi_id: str
    :param stage_name: The name of the stage to flush its cache.
    :type stage_name: str
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


async def generate_client_certificate(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """generate_client_certificate

    Generates a ClientCertificate resource.

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
    body = GenerateClientCertificateRequest.from_dict(body)
    return web.Response(status=200)


async def get_account(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_account

    Gets information about the current Account resource.

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


async def get_api_key(request: web.Request, api_key, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, include_value=None) -> web.Response:
    """get_api_key

    Gets information about the current ApiKey resource.

    :param api_key: The identifier of the ApiKey resource.
    :type api_key: str
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
    :param include_value: A boolean flag to specify whether (&lt;code&gt;true&lt;/code&gt;) or not (&lt;code&gt;false&lt;/code&gt;) the result contains the key value.
    :type include_value: bool

    """
    return web.Response(status=200)


async def get_api_keys(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, position=None, limit=None, name=None, customer_id=None, include_values=None) -> web.Response:
    """get_api_keys

    Gets information about the current ApiKeys resource.

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
    :param position: The current pagination position in the paged result set.
    :type position: str
    :param limit: The maximum number of returned results per page. The default value is 25 and the maximum value is 500.
    :type limit: int
    :param name: The name of queried API keys.
    :type name: str
    :param customer_id: The identifier of a customer in AWS Marketplace or an external system, such as a developer portal.
    :type customer_id: str
    :param include_values: A boolean flag to specify whether (&lt;code&gt;true&lt;/code&gt;) or not (&lt;code&gt;false&lt;/code&gt;) the result contains key values.
    :type include_values: bool

    """
    return web.Response(status=200)


async def get_authorizer(request: web.Request, restapi_id, authorizer_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_authorizer

    Describe an existing Authorizer resource.

    :param restapi_id: The string identifier of the associated RestApi.
    :type restapi_id: str
    :param authorizer_id: The identifier of the Authorizer resource.
    :type authorizer_id: str
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


async def get_authorizers(request: web.Request, restapi_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, position=None, limit=None) -> web.Response:
    """get_authorizers

    Describe an existing Authorizers resource.

    :param restapi_id: The string identifier of the associated RestApi.
    :type restapi_id: str
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
    :param position: The current pagination position in the paged result set.
    :type position: str
    :param limit: The maximum number of returned results per page. The default value is 25 and the maximum value is 500.
    :type limit: int

    """
    return web.Response(status=200)


async def get_base_path_mapping(request: web.Request, domain_name, base_path, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_base_path_mapping

    Describe a BasePathMapping resource.

    :param domain_name: The domain name of the BasePathMapping resource to be described.
    :type domain_name: str
    :param base_path: The base path name that callers of the API must provide as part of the URL after the domain name. This value must be unique for all of the mappings across a single API. Specify &#39;(none)&#39; if you do not want callers to specify any base path name after the domain name.
    :type base_path: str
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


async def get_base_path_mappings(request: web.Request, domain_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, position=None, limit=None) -> web.Response:
    """get_base_path_mappings

    Represents a collection of BasePathMapping resources.

    :param domain_name: The domain name of a BasePathMapping resource.
    :type domain_name: str
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
    :param position: The current pagination position in the paged result set.
    :type position: str
    :param limit: The maximum number of returned results per page. The default value is 25 and the maximum value is 500.
    :type limit: int

    """
    return web.Response(status=200)


async def get_client_certificate(request: web.Request, clientcertificate_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_client_certificate

    Gets information about the current ClientCertificate resource.

    :param clientcertificate_id: The identifier of the ClientCertificate resource to be described.
    :type clientcertificate_id: str
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


async def get_client_certificates(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, position=None, limit=None) -> web.Response:
    """get_client_certificates

    Gets a collection of ClientCertificate resources.

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
    :param position: The current pagination position in the paged result set.
    :type position: str
    :param limit: The maximum number of returned results per page. The default value is 25 and the maximum value is 500.
    :type limit: int

    """
    return web.Response(status=200)


async def get_deployment(request: web.Request, restapi_id, deployment_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, embed=None) -> web.Response:
    """get_deployment

    Gets information about a Deployment resource.

    :param restapi_id: The string identifier of the associated RestApi.
    :type restapi_id: str
    :param deployment_id: The identifier of the Deployment resource to get information about.
    :type deployment_id: str
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
    :param embed: A query parameter to retrieve the specified embedded resources of the returned Deployment resource in the response. In a REST API call, this &lt;code&gt;embed&lt;/code&gt; parameter value is a list of comma-separated strings, as in &lt;code&gt;GET /restapis/{restapi_id}/deployments/{deployment_id}?embed&#x3D;var1,var2&lt;/code&gt;. The SDK and other platform-dependent libraries might use a different format for the list. Currently, this request supports only retrieval of the embedded API summary this way. Hence, the parameter value must be a single-valued list containing only the &lt;code&gt;\&quot;apisummary\&quot;&lt;/code&gt; string. For example, &lt;code&gt;GET /restapis/{restapi_id}/deployments/{deployment_id}?embed&#x3D;apisummary&lt;/code&gt;.
    :type embed: List[str]

    """
    return web.Response(status=200)


async def get_deployments(request: web.Request, restapi_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, position=None, limit=None) -> web.Response:
    """get_deployments

    Gets information about a Deployments collection.

    :param restapi_id: The string identifier of the associated RestApi.
    :type restapi_id: str
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
    :param position: The current pagination position in the paged result set.
    :type position: str
    :param limit: The maximum number of returned results per page. The default value is 25 and the maximum value is 500.
    :type limit: int

    """
    return web.Response(status=200)


async def get_documentation_part(request: web.Request, restapi_id, part_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_documentation_part

    Gets a documentation part.

    :param restapi_id: The string identifier of the associated RestApi.
    :type restapi_id: str
    :param part_id: The string identifier of the associated RestApi.
    :type part_id: str
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


async def get_documentation_parts(request: web.Request, restapi_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, type=None, name=None, path=None, position=None, limit=None, location_status=None) -> web.Response:
    """get_documentation_parts

    Gets documentation parts.

    :param restapi_id: The string identifier of the associated RestApi.
    :type restapi_id: str
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
    :param type: The type of API entities of the to-be-retrieved documentation parts. 
    :type type: str
    :param name: The name of API entities of the to-be-retrieved documentation parts.
    :type name: str
    :param path: The path of API entities of the to-be-retrieved documentation parts.
    :type path: str
    :param position: The current pagination position in the paged result set.
    :type position: str
    :param limit: The maximum number of returned results per page. The default value is 25 and the maximum value is 500.
    :type limit: int
    :param location_status: The status of the API documentation parts to retrieve. Valid values are &lt;code&gt;DOCUMENTED&lt;/code&gt; for retrieving DocumentationPart resources with content and &lt;code&gt;UNDOCUMENTED&lt;/code&gt; for DocumentationPart resources without content.
    :type location_status: str

    """
    return web.Response(status=200)


async def get_documentation_version(request: web.Request, restapi_id, doc_version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_documentation_version

    Gets a documentation version.

    :param restapi_id: The string identifier of the associated RestApi.
    :type restapi_id: str
    :param doc_version: The version identifier of the to-be-retrieved documentation snapshot.
    :type doc_version: str
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


async def get_documentation_versions(request: web.Request, restapi_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, position=None, limit=None) -> web.Response:
    """get_documentation_versions

    Gets documentation versions.

    :param restapi_id: The string identifier of the associated RestApi.
    :type restapi_id: str
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
    :param position: The current pagination position in the paged result set.
    :type position: str
    :param limit: The maximum number of returned results per page. The default value is 25 and the maximum value is 500.
    :type limit: int

    """
    return web.Response(status=200)


async def get_domain_name(request: web.Request, domain_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_domain_name

    Represents a domain name that is contained in a simpler, more intuitive URL that can be called.

    :param domain_name: The name of the DomainName resource.
    :type domain_name: str
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


async def get_domain_names(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, position=None, limit=None) -> web.Response:
    """get_domain_names

    Represents a collection of DomainName resources.

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
    :param position: The current pagination position in the paged result set.
    :type position: str
    :param limit: The maximum number of returned results per page. The default value is 25 and the maximum value is 500.
    :type limit: int

    """
    return web.Response(status=200)


async def get_export(request: web.Request, restapi_id, stage_name, export_type, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, parameters=None, accept=None) -> web.Response:
    """get_export

    Exports a deployed version of a RestApi in a specified format.

    :param restapi_id: The string identifier of the associated RestApi.
    :type restapi_id: str
    :param stage_name: The name of the Stage that will be exported.
    :type stage_name: str
    :param export_type: The type of export. Acceptable values are &#39;oas30&#39; for OpenAPI 3.0.x and &#39;swagger&#39; for Swagger/OpenAPI 2.0.
    :type export_type: str
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
    :param parameters: A key-value map of query string parameters that specify properties of the export, depending on the requested &lt;code&gt;exportType&lt;/code&gt;. For &lt;code&gt;exportType&lt;/code&gt; &lt;code&gt;oas30&lt;/code&gt; and &lt;code&gt;swagger&lt;/code&gt;, any combination of the following parameters are supported: &lt;code&gt;extensions&#x3D;&#39;integrations&#39;&lt;/code&gt; or &lt;code&gt;extensions&#x3D;&#39;apigateway&#39;&lt;/code&gt; will export the API with x-amazon-apigateway-integration extensions. &lt;code&gt;extensions&#x3D;&#39;authorizers&#39;&lt;/code&gt; will export the API with x-amazon-apigateway-authorizer extensions. &lt;code&gt;postman&lt;/code&gt; will export the API with Postman extensions, allowing for import to the Postman tool
    :type parameters: Dict[str, str]
    :param accept: The content-type of the export, for example &lt;code&gt;application/json&lt;/code&gt;. Currently &lt;code&gt;application/json&lt;/code&gt; and &lt;code&gt;application/yaml&lt;/code&gt; are supported for &lt;code&gt;exportType&lt;/code&gt; of&lt;code&gt;oas30&lt;/code&gt; and &lt;code&gt;swagger&lt;/code&gt;. This should be specified in the &lt;code&gt;Accept&lt;/code&gt; header for direct API requests.
    :type accept: str

    """
    return web.Response(status=200)


async def get_gateway_response(request: web.Request, restapi_id, response_type, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_gateway_response

    Gets a GatewayResponse of a specified response type on the given RestApi.

    :param restapi_id: The string identifier of the associated RestApi.
    :type restapi_id: str
    :param response_type: The response type of the associated GatewayResponse.
    :type response_type: str
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


async def get_gateway_responses(request: web.Request, restapi_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, position=None, limit=None) -> web.Response:
    """get_gateway_responses

    Gets the GatewayResponses collection on the given RestApi. If an API developer has not added any definitions for gateway responses, the result will be the API Gateway-generated default GatewayResponses collection for the supported response types.

    :param restapi_id: The string identifier of the associated RestApi.
    :type restapi_id: str
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
    :param position: The current pagination position in the paged result set. The GatewayResponse collection does not support pagination and the position does not apply here.
    :type position: str
    :param limit: The maximum number of returned results per page. The default value is 25 and the maximum value is 500. The GatewayResponses collection does not support pagination and the limit does not apply here.
    :type limit: int

    """
    return web.Response(status=200)


async def get_integration(request: web.Request, restapi_id, resource_id, http_method, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_integration

    Get the integration settings.

    :param restapi_id: The string identifier of the associated RestApi.
    :type restapi_id: str
    :param resource_id: Specifies a get integration request&#39;s resource identifier
    :type resource_id: str
    :param http_method: Specifies a get integration request&#39;s HTTP method.
    :type http_method: str
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


async def get_integration_response(request: web.Request, restapi_id, resource_id, http_method, status_code, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_integration_response

    Represents a get integration response.

    :param restapi_id: The string identifier of the associated RestApi.
    :type restapi_id: str
    :param resource_id: Specifies a get integration response request&#39;s resource identifier.
    :type resource_id: str
    :param http_method: Specifies a get integration response request&#39;s HTTP method.
    :type http_method: str
    :param status_code: Specifies a get integration response request&#39;s status code.
    :type status_code: str
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


async def get_method(request: web.Request, restapi_id, resource_id, http_method, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_method

    Describe an existing Method resource.

    :param restapi_id: The string identifier of the associated RestApi.
    :type restapi_id: str
    :param resource_id: The Resource identifier for the Method resource.
    :type resource_id: str
    :param http_method: Specifies the method request&#39;s HTTP method type.
    :type http_method: str
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


async def get_method_response(request: web.Request, restapi_id, resource_id, http_method, status_code, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_method_response

    Describes a MethodResponse resource.

    :param restapi_id: The string identifier of the associated RestApi.
    :type restapi_id: str
    :param resource_id: The Resource identifier for the MethodResponse resource.
    :type resource_id: str
    :param http_method: The HTTP verb of the Method resource.
    :type http_method: str
    :param status_code: The status code for the MethodResponse resource.
    :type status_code: str
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


async def get_model(request: web.Request, restapi_id, model_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, flatten=None) -> web.Response:
    """get_model

    Describes an existing model defined for a RestApi resource.

    :param restapi_id: The RestApi identifier under which the Model exists.
    :type restapi_id: str
    :param model_name: The name of the model as an identifier.
    :type model_name: str
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
    :param flatten: A query parameter of a Boolean value to resolve (&lt;code&gt;true&lt;/code&gt;) all external model references and returns a flattened model schema or not (&lt;code&gt;false&lt;/code&gt;) The default is &lt;code&gt;false&lt;/code&gt;.
    :type flatten: bool

    """
    return web.Response(status=200)


async def get_model_template(request: web.Request, restapi_id, model_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_model_template

    Generates a sample mapping template that can be used to transform a payload into the structure of a model.

    :param restapi_id: The string identifier of the associated RestApi.
    :type restapi_id: str
    :param model_name: The name of the model for which to generate a template.
    :type model_name: str
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


async def get_models(request: web.Request, restapi_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, position=None, limit=None) -> web.Response:
    """get_models

    Describes existing Models defined for a RestApi resource.

    :param restapi_id: The string identifier of the associated RestApi.
    :type restapi_id: str
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
    :param position: The current pagination position in the paged result set.
    :type position: str
    :param limit: The maximum number of returned results per page. The default value is 25 and the maximum value is 500.
    :type limit: int

    """
    return web.Response(status=200)


async def get_request_validator(request: web.Request, restapi_id, requestvalidator_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_request_validator

    Gets a RequestValidator of a given RestApi.

    :param restapi_id: The string identifier of the associated RestApi.
    :type restapi_id: str
    :param requestvalidator_id: The identifier of the RequestValidator to be retrieved.
    :type requestvalidator_id: str
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


async def get_request_validators(request: web.Request, restapi_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, position=None, limit=None) -> web.Response:
    """get_request_validators

    Gets the RequestValidators collection of a given RestApi.

    :param restapi_id: The string identifier of the associated RestApi.
    :type restapi_id: str
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
    :param position: The current pagination position in the paged result set.
    :type position: str
    :param limit: The maximum number of returned results per page. The default value is 25 and the maximum value is 500.
    :type limit: int

    """
    return web.Response(status=200)


async def get_resource(request: web.Request, restapi_id, resource_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, embed=None) -> web.Response:
    """get_resource

    Lists information about a resource.

    :param restapi_id: The string identifier of the associated RestApi.
    :type restapi_id: str
    :param resource_id: The identifier for the Resource resource.
    :type resource_id: str
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
    :param embed: A query parameter to retrieve the specified resources embedded in the returned Resource representation in the response. This &lt;code&gt;embed&lt;/code&gt; parameter value is a list of comma-separated strings. Currently, the request supports only retrieval of the embedded Method resources this way. The query parameter value must be a single-valued list and contain the &lt;code&gt;\&quot;methods\&quot;&lt;/code&gt; string. For example, &lt;code&gt;GET /restapis/{restapi_id}/resources/{resource_id}?embed&#x3D;methods&lt;/code&gt;.
    :type embed: List[str]

    """
    return web.Response(status=200)


async def get_resources(request: web.Request, restapi_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, position=None, limit=None, embed=None) -> web.Response:
    """get_resources

    Lists information about a collection of Resource resources.

    :param restapi_id: The string identifier of the associated RestApi.
    :type restapi_id: str
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
    :param position: The current pagination position in the paged result set.
    :type position: str
    :param limit: The maximum number of returned results per page. The default value is 25 and the maximum value is 500.
    :type limit: int
    :param embed: A query parameter used to retrieve the specified resources embedded in the returned Resources resource in the response. This &lt;code&gt;embed&lt;/code&gt; parameter value is a list of comma-separated strings. Currently, the request supports only retrieval of the embedded Method resources this way. The query parameter value must be a single-valued list and contain the &lt;code&gt;\&quot;methods\&quot;&lt;/code&gt; string. For example, &lt;code&gt;GET /restapis/{restapi_id}/resources?embed&#x3D;methods&lt;/code&gt;.
    :type embed: List[str]

    """
    return web.Response(status=200)


async def get_rest_api(request: web.Request, restapi_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_rest_api

    Lists the RestApi resource in the collection.

    :param restapi_id: The string identifier of the associated RestApi.
    :type restapi_id: str
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


async def get_rest_apis(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, position=None, limit=None) -> web.Response:
    """get_rest_apis

    Lists the RestApis resources for your collection.

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
    :param position: The current pagination position in the paged result set.
    :type position: str
    :param limit: The maximum number of returned results per page. The default value is 25 and the maximum value is 500.
    :type limit: int

    """
    return web.Response(status=200)


async def get_sdk(request: web.Request, restapi_id, stage_name, sdk_type, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, parameters=None) -> web.Response:
    """get_sdk

    Generates a client SDK for a RestApi and Stage.

    :param restapi_id: The string identifier of the associated RestApi.
    :type restapi_id: str
    :param stage_name: The name of the Stage that the SDK will use.
    :type stage_name: str
    :param sdk_type: The language for the generated SDK. Currently &lt;code&gt;java&lt;/code&gt;, &lt;code&gt;javascript&lt;/code&gt;, &lt;code&gt;android&lt;/code&gt;, &lt;code&gt;objectivec&lt;/code&gt; (for iOS), &lt;code&gt;swift&lt;/code&gt; (for iOS), and &lt;code&gt;ruby&lt;/code&gt; are supported.
    :type sdk_type: str
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
    :param parameters: A string-to-string key-value map of query parameters &lt;code&gt;sdkType&lt;/code&gt;-dependent properties of the SDK. For &lt;code&gt;sdkType&lt;/code&gt; of &lt;code&gt;objectivec&lt;/code&gt; or &lt;code&gt;swift&lt;/code&gt;, a parameter named &lt;code&gt;classPrefix&lt;/code&gt; is required. For &lt;code&gt;sdkType&lt;/code&gt; of &lt;code&gt;android&lt;/code&gt;, parameters named &lt;code&gt;groupId&lt;/code&gt;, &lt;code&gt;artifactId&lt;/code&gt;, &lt;code&gt;artifactVersion&lt;/code&gt;, and &lt;code&gt;invokerPackage&lt;/code&gt; are required. For &lt;code&gt;sdkType&lt;/code&gt; of &lt;code&gt;java&lt;/code&gt;, parameters named &lt;code&gt;serviceName&lt;/code&gt; and &lt;code&gt;javaPackageName&lt;/code&gt; are required. 
    :type parameters: Dict[str, str]

    """
    return web.Response(status=200)


async def get_sdk_type(request: web.Request, sdktype_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_sdk_type

    Gets an SDK type.

    :param sdktype_id: The identifier of the queried SdkType instance.
    :type sdktype_id: str
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


async def get_sdk_types(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, position=None, limit=None) -> web.Response:
    """get_sdk_types

    Gets SDK types

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
    :param position: The current pagination position in the paged result set.
    :type position: str
    :param limit: The maximum number of returned results per page. The default value is 25 and the maximum value is 500.
    :type limit: int

    """
    return web.Response(status=200)


async def get_stage(request: web.Request, restapi_id, stage_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_stage

    Gets information about a Stage resource.

    :param restapi_id: The string identifier of the associated RestApi.
    :type restapi_id: str
    :param stage_name: The name of the Stage resource to get information about.
    :type stage_name: str
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


async def get_stages(request: web.Request, restapi_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, deployment_id=None) -> web.Response:
    """get_stages

    Gets information about one or more Stage resources.

    :param restapi_id: The string identifier of the associated RestApi.
    :type restapi_id: str
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
    :param deployment_id: The stages&#39; deployment identifiers.
    :type deployment_id: str

    """
    return web.Response(status=200)


async def get_tags(request: web.Request, resource_arn, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, position=None, limit=None) -> web.Response:
    """get_tags

    Gets the Tags collection for a given resource.

    :param resource_arn: The ARN of a resource that can be tagged.
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
    :param position: (Not currently supported) The current pagination position in the paged result set.
    :type position: str
    :param limit: (Not currently supported) The maximum number of returned results per page. The default value is 25 and the maximum value is 500.
    :type limit: int

    """
    return web.Response(status=200)


async def get_usage(request: web.Request, usageplan_id, start_date, end_date, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, key_id=None, position=None, limit=None) -> web.Response:
    """get_usage

    Gets the usage data of a usage plan in a specified time interval.

    :param usageplan_id: The Id of the usage plan associated with the usage data.
    :type usageplan_id: str
    :param start_date: The starting date (e.g., 2016-01-01) of the usage data.
    :type start_date: str
    :param end_date: The ending date (e.g., 2016-12-31) of the usage data.
    :type end_date: str
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
    :param key_id: The Id of the API key associated with the resultant usage data.
    :type key_id: str
    :param position: The current pagination position in the paged result set.
    :type position: str
    :param limit: The maximum number of returned results per page. The default value is 25 and the maximum value is 500.
    :type limit: int

    """
    return web.Response(status=200)


async def get_usage_plan(request: web.Request, usageplan_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_usage_plan

    Gets a usage plan of a given plan identifier.

    :param usageplan_id: The identifier of the UsagePlan resource to be retrieved.
    :type usageplan_id: str
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


async def get_usage_plan_key(request: web.Request, usageplan_id, key_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_usage_plan_key

    Gets a usage plan key of a given key identifier.

    :param usageplan_id: The Id of the UsagePlan resource representing the usage plan containing the to-be-retrieved UsagePlanKey resource representing a plan customer.
    :type usageplan_id: str
    :param key_id: The key Id of the to-be-retrieved UsagePlanKey resource representing a plan customer.
    :type key_id: str
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


async def get_usage_plan_keys(request: web.Request, usageplan_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, position=None, limit=None, name=None) -> web.Response:
    """get_usage_plan_keys

    Gets all the usage plan keys representing the API keys added to a specified usage plan.

    :param usageplan_id: The Id of the UsagePlan resource representing the usage plan containing the to-be-retrieved UsagePlanKey resource representing a plan customer.
    :type usageplan_id: str
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
    :param position: The current pagination position in the paged result set.
    :type position: str
    :param limit: The maximum number of returned results per page. The default value is 25 and the maximum value is 500.
    :type limit: int
    :param name: A query parameter specifying the name of the to-be-returned usage plan keys.
    :type name: str

    """
    return web.Response(status=200)


async def get_usage_plans(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, position=None, key_id=None, limit=None) -> web.Response:
    """get_usage_plans

    Gets all the usage plans of the caller&#39;s account.

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
    :param position: The current pagination position in the paged result set.
    :type position: str
    :param key_id: The identifier of the API key associated with the usage plans.
    :type key_id: str
    :param limit: The maximum number of returned results per page. The default value is 25 and the maximum value is 500.
    :type limit: int

    """
    return web.Response(status=200)


async def get_vpc_link(request: web.Request, vpclink_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_vpc_link

    Gets a specified VPC link under the caller&#39;s account in a region.

    :param vpclink_id: The identifier of the VpcLink. It is used in an Integration to reference this VpcLink.
    :type vpclink_id: str
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


async def get_vpc_links(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, position=None, limit=None) -> web.Response:
    """get_vpc_links

    Gets the VpcLinks collection under the caller&#39;s account in a selected region.

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
    :param position: The current pagination position in the paged result set.
    :type position: str
    :param limit: The maximum number of returned results per page. The default value is 25 and the maximum value is 500.
    :type limit: int

    """
    return web.Response(status=200)


async def import_api_keys(request: web.Request, format, mode, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, failonwarnings=None) -> web.Response:
    """import_api_keys

    Import API keys from an external source, such as a CSV-formatted file.

    :param format: A query parameter to specify the input format to imported API keys. Currently, only the &lt;code&gt;csv&lt;/code&gt; format is supported.
    :type format: str
    :param mode: 
    :type mode: str
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
    :param failonwarnings: A query parameter to indicate whether to rollback ApiKey importation (&lt;code&gt;true&lt;/code&gt;) or not (&lt;code&gt;false&lt;/code&gt;) when error is encountered.
    :type failonwarnings: bool

    """
    body = ImportApiKeysRequest.from_dict(body)
    return web.Response(status=200)


async def import_documentation_parts(request: web.Request, restapi_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, mode=None, failonwarnings=None) -> web.Response:
    """import_documentation_parts

    Imports documentation parts

    :param restapi_id: The string identifier of the associated RestApi.
    :type restapi_id: str
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
    :param mode: A query parameter to indicate whether to overwrite (&lt;code&gt;OVERWRITE&lt;/code&gt;) any existing DocumentationParts definition or to merge (&lt;code&gt;MERGE&lt;/code&gt;) the new definition into the existing one. The default value is &lt;code&gt;MERGE&lt;/code&gt;.
    :type mode: str
    :param failonwarnings: A query parameter to specify whether to rollback the documentation importation (&lt;code&gt;true&lt;/code&gt;) or not (&lt;code&gt;false&lt;/code&gt;) when a warning is encountered. The default value is &lt;code&gt;false&lt;/code&gt;.
    :type failonwarnings: bool

    """
    body = ImportDocumentationPartsRequest.from_dict(body)
    return web.Response(status=200)


async def import_rest_api(request: web.Request, mode, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, failonwarnings=None, parameters=None) -> web.Response:
    """import_rest_api

    A feature of the API Gateway control service for creating a new API from an external API definition file.

    :param mode: 
    :type mode: str
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
    :param failonwarnings: A query parameter to indicate whether to rollback the API creation (&lt;code&gt;true&lt;/code&gt;) or not (&lt;code&gt;false&lt;/code&gt;) when a warning is encountered. The default value is &lt;code&gt;false&lt;/code&gt;.
    :type failonwarnings: bool
    :param parameters: &lt;p&gt;A key-value map of context-specific query string parameters specifying the behavior of different API importing operations. The following shows operation-specific parameters and their supported values.&lt;/p&gt; &lt;p&gt; To exclude DocumentationParts from the import, set &lt;code&gt;parameters&lt;/code&gt; as &lt;code&gt;ignore&#x3D;documentation&lt;/code&gt;.&lt;/p&gt; &lt;p&gt; To configure the endpoint type, set &lt;code&gt;parameters&lt;/code&gt; as &lt;code&gt;endpointConfigurationTypes&#x3D;EDGE&lt;/code&gt;, &lt;code&gt;endpointConfigurationTypes&#x3D;REGIONAL&lt;/code&gt;, or &lt;code&gt;endpointConfigurationTypes&#x3D;PRIVATE&lt;/code&gt;. The default endpoint type is &lt;code&gt;EDGE&lt;/code&gt;.&lt;/p&gt; &lt;p&gt; To handle imported &lt;code&gt;basepath&lt;/code&gt;, set &lt;code&gt;parameters&lt;/code&gt; as &lt;code&gt;basepath&#x3D;ignore&lt;/code&gt;, &lt;code&gt;basepath&#x3D;prepend&lt;/code&gt; or &lt;code&gt;basepath&#x3D;split&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;For example, the AWS CLI command to exclude documentation from the imported API is:&lt;/p&gt; &lt;p&gt;The AWS CLI command to set the regional endpoint on the imported API is:&lt;/p&gt;
    :type parameters: Dict[str, str]

    """
    body = ImportRestApiRequest.from_dict(body)
    return web.Response(status=200)


async def put_gateway_response(request: web.Request, restapi_id, response_type, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """put_gateway_response

    Creates a customization of a GatewayResponse of a specified response type and status code on the given RestApi.

    :param restapi_id: The string identifier of the associated RestApi.
    :type restapi_id: str
    :param response_type: The response type of the associated GatewayResponse
    :type response_type: str
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
    body = PutGatewayResponseRequest.from_dict(body)
    return web.Response(status=200)


async def put_integration(request: web.Request, restapi_id, resource_id, http_method, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """put_integration

    Sets up a method&#39;s integration.

    :param restapi_id: The string identifier of the associated RestApi.
    :type restapi_id: str
    :param resource_id: Specifies a put integration request&#39;s resource ID.
    :type resource_id: str
    :param http_method: Specifies the HTTP method for the integration.
    :type http_method: str
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
    body = PutIntegrationRequest.from_dict(body)
    return web.Response(status=200)


async def put_integration_response(request: web.Request, restapi_id, resource_id, http_method, status_code, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """put_integration_response

    Represents a put integration.

    :param restapi_id: The string identifier of the associated RestApi.
    :type restapi_id: str
    :param resource_id: Specifies a put integration response request&#39;s resource identifier.
    :type resource_id: str
    :param http_method: Specifies a put integration response request&#39;s HTTP method.
    :type http_method: str
    :param status_code: Specifies the status code that is used to map the integration response to an existing MethodResponse.
    :type status_code: str
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
    body = PutIntegrationResponseRequest.from_dict(body)
    return web.Response(status=200)


async def put_method(request: web.Request, restapi_id, resource_id, http_method, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """put_method

    Add a method to an existing Resource resource.

    :param restapi_id: The string identifier of the associated RestApi.
    :type restapi_id: str
    :param resource_id: The Resource identifier for the new Method resource.
    :type resource_id: str
    :param http_method: Specifies the method request&#39;s HTTP method type.
    :type http_method: str
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
    body = PutMethodRequest.from_dict(body)
    return web.Response(status=200)


async def put_method_response(request: web.Request, restapi_id, resource_id, http_method, status_code, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """put_method_response

    Adds a MethodResponse to an existing Method resource.

    :param restapi_id: The string identifier of the associated RestApi.
    :type restapi_id: str
    :param resource_id: The Resource identifier for the Method resource.
    :type resource_id: str
    :param http_method: The HTTP verb of the Method resource.
    :type http_method: str
    :param status_code: The method response&#39;s status code.
    :type status_code: str
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
    body = PutMethodResponseRequest.from_dict(body)
    return web.Response(status=200)


async def put_rest_api(request: web.Request, restapi_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, mode=None, failonwarnings=None, parameters=None) -> web.Response:
    """put_rest_api

    A feature of the API Gateway control service for updating an existing API with an input of external API definitions. The update can take the form of merging the supplied definition into the existing API or overwriting the existing API.

    :param restapi_id: The string identifier of the associated RestApi.
    :type restapi_id: str
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
    :param mode: The &lt;code&gt;mode&lt;/code&gt; query parameter to specify the update mode. Valid values are \&quot;merge\&quot; and \&quot;overwrite\&quot;. By default, the update mode is \&quot;merge\&quot;.
    :type mode: str
    :param failonwarnings: A query parameter to indicate whether to rollback the API update (&lt;code&gt;true&lt;/code&gt;) or not (&lt;code&gt;false&lt;/code&gt;) when a warning is encountered. The default value is &lt;code&gt;false&lt;/code&gt;.
    :type failonwarnings: bool
    :param parameters: Custom header parameters as part of the request. For example, to exclude DocumentationParts from an imported API, set &lt;code&gt;ignore&#x3D;documentation&lt;/code&gt; as a &lt;code&gt;parameters&lt;/code&gt; value, as in the AWS CLI command of &lt;code&gt;aws apigateway import-rest-api --parameters ignore&#x3D;documentation --body &#39;file:///path/to/imported-api-body.json&#39;&lt;/code&gt;.
    :type parameters: Dict[str, str]

    """
    body = PutRestApiRequest.from_dict(body)
    return web.Response(status=200)


async def tag_resource(request: web.Request, resource_arn, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """tag_resource

    Adds or updates a tag on a given resource.

    :param resource_arn: The ARN of a resource that can be tagged.
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


async def test_invoke_authorizer(request: web.Request, restapi_id, authorizer_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """test_invoke_authorizer

    Simulate the execution of an Authorizer in your RestApi with headers, parameters, and an incoming request body.

    :param restapi_id: The string identifier of the associated RestApi.
    :type restapi_id: str
    :param authorizer_id: Specifies a test invoke authorizer request&#39;s Authorizer ID.
    :type authorizer_id: str
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
    body = TestInvokeAuthorizerRequest.from_dict(body)
    return web.Response(status=200)


async def test_invoke_method(request: web.Request, restapi_id, resource_id, http_method, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """test_invoke_method

    Simulate the invocation of a Method in your RestApi with headers, parameters, and an incoming request body.

    :param restapi_id: The string identifier of the associated RestApi.
    :type restapi_id: str
    :param resource_id: Specifies a test invoke method request&#39;s resource ID.
    :type resource_id: str
    :param http_method: Specifies a test invoke method request&#39;s HTTP method.
    :type http_method: str
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
    body = TestInvokeMethodRequest.from_dict(body)
    return web.Response(status=200)


async def untag_resource(request: web.Request, resource_arn, tag_keys, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """untag_resource

    Removes a tag from a given resource.

    :param resource_arn: The ARN of a resource that can be tagged.
    :type resource_arn: str
    :param tag_keys: The Tag keys to delete.
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


async def update_account(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_account

    Changes information about the current Account resource.

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
    body = UpdateApiKeyRequest.from_dict(body)
    return web.Response(status=200)


async def update_api_key(request: web.Request, api_key, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_api_key

    Changes information about an ApiKey resource.

    :param api_key: The identifier of the ApiKey resource to be updated.
    :type api_key: str
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
    body = UpdateApiKeyRequest.from_dict(body)
    return web.Response(status=200)


async def update_authorizer(request: web.Request, restapi_id, authorizer_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_authorizer

    Updates an existing Authorizer resource.

    :param restapi_id: The string identifier of the associated RestApi.
    :type restapi_id: str
    :param authorizer_id: The identifier of the Authorizer resource.
    :type authorizer_id: str
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
    body = UpdateApiKeyRequest.from_dict(body)
    return web.Response(status=200)


async def update_base_path_mapping(request: web.Request, domain_name, base_path, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_base_path_mapping

    Changes information about the BasePathMapping resource.

    :param domain_name: The domain name of the BasePathMapping resource to change.
    :type domain_name: str
    :param base_path: &lt;p&gt;The base path of the BasePathMapping resource to change.&lt;/p&gt; &lt;p&gt;To specify an empty base path, set this parameter to &lt;code&gt;&#39;(none)&#39;&lt;/code&gt;.&lt;/p&gt;
    :type base_path: str
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
    body = UpdateApiKeyRequest.from_dict(body)
    return web.Response(status=200)


async def update_client_certificate(request: web.Request, clientcertificate_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_client_certificate

    Changes information about an ClientCertificate resource.

    :param clientcertificate_id: The identifier of the ClientCertificate resource to be updated.
    :type clientcertificate_id: str
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
    body = UpdateApiKeyRequest.from_dict(body)
    return web.Response(status=200)


async def update_deployment(request: web.Request, restapi_id, deployment_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_deployment

    Changes information about a Deployment resource.

    :param restapi_id: The string identifier of the associated RestApi.
    :type restapi_id: str
    :param deployment_id: The replacement identifier for the Deployment resource to change information about.
    :type deployment_id: str
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
    body = UpdateApiKeyRequest.from_dict(body)
    return web.Response(status=200)


async def update_documentation_part(request: web.Request, restapi_id, part_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_documentation_part

    Updates a documentation part.

    :param restapi_id: The string identifier of the associated RestApi.
    :type restapi_id: str
    :param part_id: The identifier of the to-be-updated documentation part.
    :type part_id: str
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
    body = UpdateApiKeyRequest.from_dict(body)
    return web.Response(status=200)


async def update_documentation_version(request: web.Request, restapi_id, doc_version, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_documentation_version

    Updates a documentation version.

    :param restapi_id: The string identifier of the associated RestApi..
    :type restapi_id: str
    :param doc_version: The version identifier of the to-be-updated documentation version.
    :type doc_version: str
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
    body = UpdateApiKeyRequest.from_dict(body)
    return web.Response(status=200)


async def update_domain_name(request: web.Request, domain_name, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_domain_name

    Changes information about the DomainName resource.

    :param domain_name: The name of the DomainName resource to be changed.
    :type domain_name: str
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
    body = UpdateApiKeyRequest.from_dict(body)
    return web.Response(status=200)


async def update_gateway_response(request: web.Request, restapi_id, response_type, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_gateway_response

    Updates a GatewayResponse of a specified response type on the given RestApi.

    :param restapi_id: The string identifier of the associated RestApi.
    :type restapi_id: str
    :param response_type: The response type of the associated GatewayResponse.
    :type response_type: str
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
    body = UpdateApiKeyRequest.from_dict(body)
    return web.Response(status=200)


async def update_integration(request: web.Request, restapi_id, resource_id, http_method, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_integration

    Represents an update integration.

    :param restapi_id: The string identifier of the associated RestApi.
    :type restapi_id: str
    :param resource_id: Represents an update integration request&#39;s resource identifier.
    :type resource_id: str
    :param http_method: Represents an update integration request&#39;s HTTP method.
    :type http_method: str
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
    body = UpdateApiKeyRequest.from_dict(body)
    return web.Response(status=200)


async def update_integration_response(request: web.Request, restapi_id, resource_id, http_method, status_code, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_integration_response

    Represents an update integration response.

    :param restapi_id: The string identifier of the associated RestApi.
    :type restapi_id: str
    :param resource_id: Specifies an update integration response request&#39;s resource identifier.
    :type resource_id: str
    :param http_method: Specifies an update integration response request&#39;s HTTP method.
    :type http_method: str
    :param status_code: Specifies an update integration response request&#39;s status code.
    :type status_code: str
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
    body = UpdateApiKeyRequest.from_dict(body)
    return web.Response(status=200)


async def update_method(request: web.Request, restapi_id, resource_id, http_method, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_method

    Updates an existing Method resource.

    :param restapi_id: The string identifier of the associated RestApi.
    :type restapi_id: str
    :param resource_id: The Resource identifier for the Method resource.
    :type resource_id: str
    :param http_method: The HTTP verb of the Method resource.
    :type http_method: str
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
    body = UpdateApiKeyRequest.from_dict(body)
    return web.Response(status=200)


async def update_method_response(request: web.Request, restapi_id, resource_id, http_method, status_code, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_method_response

    Updates an existing MethodResponse resource.

    :param restapi_id: The string identifier of the associated RestApi.
    :type restapi_id: str
    :param resource_id: The Resource identifier for the MethodResponse resource.
    :type resource_id: str
    :param http_method: The HTTP verb of the Method resource.
    :type http_method: str
    :param status_code: The status code for the MethodResponse resource.
    :type status_code: str
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
    body = UpdateApiKeyRequest.from_dict(body)
    return web.Response(status=200)


async def update_model(request: web.Request, restapi_id, model_name, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_model

    Changes information about a model.

    :param restapi_id: The string identifier of the associated RestApi.
    :type restapi_id: str
    :param model_name: The name of the model to update.
    :type model_name: str
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
    body = UpdateApiKeyRequest.from_dict(body)
    return web.Response(status=200)


async def update_request_validator(request: web.Request, restapi_id, requestvalidator_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_request_validator

    Updates a RequestValidator of a given RestApi.

    :param restapi_id: The string identifier of the associated RestApi.
    :type restapi_id: str
    :param requestvalidator_id: The identifier of RequestValidator to be updated.
    :type requestvalidator_id: str
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
    body = UpdateApiKeyRequest.from_dict(body)
    return web.Response(status=200)


async def update_resource(request: web.Request, restapi_id, resource_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_resource

    Changes information about a Resource resource.

    :param restapi_id: The string identifier of the associated RestApi.
    :type restapi_id: str
    :param resource_id: The identifier of the Resource resource.
    :type resource_id: str
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
    body = UpdateApiKeyRequest.from_dict(body)
    return web.Response(status=200)


async def update_rest_api(request: web.Request, restapi_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_rest_api

    Changes information about the specified API.

    :param restapi_id: The string identifier of the associated RestApi.
    :type restapi_id: str
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
    body = UpdateApiKeyRequest.from_dict(body)
    return web.Response(status=200)


async def update_stage(request: web.Request, restapi_id, stage_name, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_stage

    Changes information about a Stage resource.

    :param restapi_id: The string identifier of the associated RestApi.
    :type restapi_id: str
    :param stage_name: The name of the Stage resource to change information about.
    :type stage_name: str
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
    body = UpdateApiKeyRequest.from_dict(body)
    return web.Response(status=200)


async def update_usage(request: web.Request, usageplan_id, key_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_usage

    Grants a temporary extension to the remaining quota of a usage plan associated with a specified API key.

    :param usageplan_id: The Id of the usage plan associated with the usage data.
    :type usageplan_id: str
    :param key_id: The identifier of the API key associated with the usage plan in which a temporary extension is granted to the remaining quota.
    :type key_id: str
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
    body = UpdateApiKeyRequest.from_dict(body)
    return web.Response(status=200)


async def update_usage_plan(request: web.Request, usageplan_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_usage_plan

    Updates a usage plan of a given plan Id.

    :param usageplan_id: The Id of the to-be-updated usage plan.
    :type usageplan_id: str
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
    body = UpdateApiKeyRequest.from_dict(body)
    return web.Response(status=200)


async def update_vpc_link(request: web.Request, vpclink_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_vpc_link

    Updates an existing VpcLink of a specified identifier.

    :param vpclink_id: The identifier of the VpcLink. It is used in an Integration to reference this VpcLink.
    :type vpclink_id: str
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
    body = UpdateApiKeyRequest.from_dict(body)
    return web.Response(status=200)
