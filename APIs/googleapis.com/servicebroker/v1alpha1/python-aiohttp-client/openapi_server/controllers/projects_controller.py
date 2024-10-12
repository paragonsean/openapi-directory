from typing import List, Dict
from aiohttp import web

from openapi_server.models.google_cloud_servicebroker_v1alpha1_binding import GoogleCloudServicebrokerV1alpha1Binding
from openapi_server.models.google_cloud_servicebroker_v1alpha1_create_binding_response import GoogleCloudServicebrokerV1alpha1CreateBindingResponse
from openapi_server.models.google_cloud_servicebroker_v1alpha1_delete_service_instance_response import GoogleCloudServicebrokerV1alpha1DeleteServiceInstanceResponse
from openapi_server.models.google_cloud_servicebroker_v1alpha1_list_bindings_response import GoogleCloudServicebrokerV1alpha1ListBindingsResponse
from openapi_server.models.google_cloud_servicebroker_v1alpha1_list_catalog_response import GoogleCloudServicebrokerV1alpha1ListCatalogResponse
from openapi_server.models.google_cloud_servicebroker_v1alpha1_list_service_instances_response import GoogleCloudServicebrokerV1alpha1ListServiceInstancesResponse
from openapi_server.models.google_cloud_servicebroker_v1alpha1_operation import GoogleCloudServicebrokerV1alpha1Operation
from openapi_server.models.google_cloud_servicebroker_v1alpha1_service_instance import GoogleCloudServicebrokerV1alpha1ServiceInstance
from openapi_server import util


async def servicebroker_projects_brokers_instances_service_bindings_list(request: web.Request, parent, upload_protocol=None, quota_user=None, pretty_print=None, upload_type=None, fields=None, param_callback=None, oauth_token=None, xgafv=None, alt=None, key=None, access_token=None, page_size=None, page_token=None) -> web.Response:
    """servicebroker_projects_brokers_instances_service_bindings_list

    Lists all the bindings in the instance

    :param parent: Parent must match &#x60;projects/[PROJECT_ID]/brokers/[BROKER_ID]/instances/[INSTANCE_ID]&#x60;.
    :type parent: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param param_callback: JSONP
    :type param_callback: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param alt: Data format for response.
    :type alt: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param page_size: Specifies the number of results to return per page. If there are fewer elements than the specified number, returns all elements. Optional. If unset or 0, all the results will be returned.
    :type page_size: int
    :param page_token: Specifies a page token to use. Set &#x60;pageToken&#x60; to a &#x60;nextPageToken&#x60; returned by a previous list request to get the next page of results.
    :type page_token: str

    """
    return web.Response(status=200)


async def servicebroker_projects_brokers_service_instances_list(request: web.Request, parent, upload_protocol=None, quota_user=None, pretty_print=None, upload_type=None, fields=None, param_callback=None, oauth_token=None, xgafv=None, alt=None, key=None, access_token=None, page_size=None, page_token=None) -> web.Response:
    """servicebroker_projects_brokers_service_instances_list

    Lists all the instances in the brokers This API is an extension and not part of the OSB spec. Hence the path is a standard Google API URL.

    :param parent: Parent must match &#x60;projects/[PROJECT_ID]/brokers/[BROKER_ID]&#x60;.
    :type parent: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param param_callback: JSONP
    :type param_callback: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param alt: Data format for response.
    :type alt: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param page_size: Specifies the number of results to return per page. If there are fewer elements than the specified number, returns all elements. Optional. If unset or 0, all the results will be returned.
    :type page_size: int
    :param page_token: Specifies a page token to use. Set &#x60;pageToken&#x60; to a &#x60;nextPageToken&#x60; returned by a previous list request to get the next page of results.
    :type page_token: str

    """
    return web.Response(status=200)


async def servicebroker_projects_brokers_v2_catalog_list(request: web.Request, parent, upload_protocol=None, quota_user=None, pretty_print=None, upload_type=None, fields=None, param_callback=None, oauth_token=None, xgafv=None, alt=None, key=None, access_token=None, page_size=None, page_token=None) -> web.Response:
    """servicebroker_projects_brokers_v2_catalog_list

    Lists all the Services registered with this broker for consumption for given service registry broker, which contains an set of services. Note, that Service producer API is separate from Broker API.

    :param parent: Parent must match &#x60;projects/[PROJECT_ID]/brokers/[BROKER_ID]&#x60;.
    :type parent: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param param_callback: JSONP
    :type param_callback: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param alt: Data format for response.
    :type alt: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param page_size: Specifies the number of results to return per page. If there are fewer elements than the specified number, returns all elements. Optional. If unset or 0, all the results will be returned.
    :type page_size: int
    :param page_token: Specifies a page token to use. Set &#x60;pageToken&#x60; to a &#x60;nextPageToken&#x60; returned by a previous list request to get the next page of results.
    :type page_token: str

    """
    return web.Response(status=200)


async def servicebroker_projects_brokers_v2_service_instances_delete(request: web.Request, parent, instance_id, upload_protocol=None, quota_user=None, pretty_print=None, upload_type=None, fields=None, param_callback=None, oauth_token=None, xgafv=None, alt=None, key=None, access_token=None, accepts_incomplete=None, plan_id=None, service_id=None) -> web.Response:
    """servicebroker_projects_brokers_v2_service_instances_delete

    Deprovisions a service instance. For synchronous/asynchronous request details see CreateServiceInstance method. If service instance does not exist HTTP 410 status will be returned.

    :param parent: Parent must match &#x60;projects/[PROJECT_ID]/brokers/[BROKER_ID]&#x60;.
    :type parent: str
    :param instance_id: The instance id to deprovision.
    :type instance_id: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param param_callback: JSONP
    :type param_callback: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param alt: Data format for response.
    :type alt: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param accepts_incomplete: See CreateServiceInstanceRequest for details.
    :type accepts_incomplete: bool
    :param plan_id: The plan id of the service instance.
    :type plan_id: str
    :param service_id: The service id of the service instance.
    :type service_id: str

    """
    return web.Response(status=200)


async def servicebroker_projects_brokers_v2_service_instances_get(request: web.Request, name, upload_protocol=None, quota_user=None, pretty_print=None, upload_type=None, fields=None, param_callback=None, oauth_token=None, xgafv=None, alt=None, key=None, access_token=None) -> web.Response:
    """servicebroker_projects_brokers_v2_service_instances_get

    Gets the given service instance from the system. This API is an extension and not part of the OSB spec. Hence the path is a standard Google API URL.

    :param name: The resource name of the instance to return.
    :type name: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param param_callback: JSONP
    :type param_callback: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param alt: Data format for response.
    :type alt: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param access_token: OAuth access token.
    :type access_token: str

    """
    return web.Response(status=200)


async def servicebroker_projects_brokers_v2_service_instances_get_last_operation(request: web.Request, parent, instance_id, upload_protocol=None, quota_user=None, pretty_print=None, upload_type=None, fields=None, param_callback=None, oauth_token=None, xgafv=None, alt=None, key=None, access_token=None, operation=None, plan_id=None, service_id=None) -> web.Response:
    """servicebroker_projects_brokers_v2_service_instances_get_last_operation

    Returns the state of the last operation for the service instance. Only last (or current) operation can be polled.

    :param parent: Parent must match &#x60;projects/[PROJECT_ID]/brokers/[BROKER_ID]&#x60;.
    :type parent: str
    :param instance_id: The instance id for which to return the last operation status.
    :type instance_id: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param param_callback: JSONP
    :type param_callback: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param alt: Data format for response.
    :type alt: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param operation: If &#x60;operation&#x60; was returned during mutation operation, this field must be populated with the provided value.
    :type operation: str
    :param plan_id: Plan id.
    :type plan_id: str
    :param service_id: Service id.
    :type service_id: str

    """
    return web.Response(status=200)


async def servicebroker_projects_brokers_v2_service_instances_service_bindings_create(request: web.Request, parent, instance_id, binding_id, upload_protocol=None, quota_user=None, pretty_print=None, upload_type=None, fields=None, param_callback=None, oauth_token=None, xgafv=None, alt=None, key=None, access_token=None, accepts_incomplete=None, body=None) -> web.Response:
    """servicebroker_projects_brokers_v2_service_instances_service_bindings_create

    CreateBinding generates a service binding to an existing service instance. See ProviServiceInstance for async operation details.

    :param parent: The GCP container. Must match &#x60;projects/[PROJECT_ID]/brokers/[BROKER_ID]&#x60;.
    :type parent: str
    :param instance_id: The service instance to which to bind.
    :type instance_id: str
    :param binding_id: The id of the binding. Must be unique within GCP project. Maximum length is 64, GUID recommended. Required.
    :type binding_id: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param param_callback: JSONP
    :type param_callback: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param alt: Data format for response.
    :type alt: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param accepts_incomplete: See CreateServiceInstanceRequest for details.
    :type accepts_incomplete: bool
    :param body: 
    :type body: dict | bytes

    """
    body = GoogleCloudServicebrokerV1alpha1Binding.from_dict(body)
    return web.Response(status=200)


async def servicebroker_projects_brokers_v2_service_instances_service_bindings_get_last_operation(request: web.Request, parent, instance_id, binding_id, upload_protocol=None, quota_user=None, pretty_print=None, upload_type=None, fields=None, param_callback=None, oauth_token=None, xgafv=None, alt=None, key=None, access_token=None, operation=None, plan_id=None, service_id=None) -> web.Response:
    """servicebroker_projects_brokers_v2_service_instances_service_bindings_get_last_operation

    Returns the state of the last operation for the binding. Only last (or current) operation can be polled.

    :param parent: Parent must match &#x60;projects/[PROJECT_ID]/brokers/[BROKER_ID]&#x60;.
    :type parent: str
    :param instance_id: The instance id that the binding is bound to.
    :type instance_id: str
    :param binding_id: The binding id for which to return the last operation
    :type binding_id: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param param_callback: JSONP
    :type param_callback: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param alt: Data format for response.
    :type alt: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param operation: If &#x60;operation&#x60; was returned during mutation operation, this field must be populated with the provided value.
    :type operation: str
    :param plan_id: Plan id.
    :type plan_id: str
    :param service_id: Service id.
    :type service_id: str

    """
    return web.Response(status=200)
