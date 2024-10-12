from typing import List, Dict
from aiohttp import web

from openapi_server.models.add_tenant_project_request import AddTenantProjectRequest
from openapi_server.models.apply_tenant_project_config_request import ApplyTenantProjectConfigRequest
from openapi_server.models.attach_tenant_project_request import AttachTenantProjectRequest
from openapi_server.models.create_tenancy_unit_request import CreateTenancyUnitRequest
from openapi_server.models.delete_tenant_project_request import DeleteTenantProjectRequest
from openapi_server.models.list_tenancy_units_response import ListTenancyUnitsResponse
from openapi_server.models.operation import Operation
from openapi_server.models.remove_tenant_project_request import RemoveTenantProjectRequest
from openapi_server.models.search_tenancy_units_response import SearchTenancyUnitsResponse
from openapi_server.models.tenancy_unit import TenancyUnit
from openapi_server.models.undelete_tenant_project_request import UndeleteTenantProjectRequest
from openapi_server import util


async def serviceconsumermanagement_services_search(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, page_size=None, page_token=None, query=None) -> web.Response:
    """serviceconsumermanagement_services_search

    Search tenancy units for a managed service.

    :param parent: Required. Service for which search is performed. services/{service} {service} the name of a service, for example &#39;service.googleapis.com&#39;.
    :type parent: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param page_size: Optional. The maximum number of results returned by this request. Currently, the default maximum is set to 1000. If &#x60;page_size&#x60; isn&#39;t provided or the size provided is a number larger than 1000, it&#39;s automatically set to 1000.
    :type page_size: int
    :param page_token: Optional. The continuation token, which is used to page through large result sets. To get the next page of results, set this parameter to the value of &#x60;nextPageToken&#x60; from the previous response.
    :type page_token: str
    :param query: Optional. Set a query &#x60;{expression}&#x60; for querying tenancy units. Your &#x60;{expression}&#x60; must be in the format: &#x60;field_name&#x3D;literal_string&#x60;. The &#x60;field_name&#x60; is the name of the field you want to compare. Supported fields are &#x60;tenant_resources.tag&#x60; and &#x60;tenant_resources.resource&#x60;. For example, to search tenancy units that contain at least one tenant resource with a given tag &#39;xyz&#39;, use the query &#x60;tenant_resources.tag&#x3D;xyz&#x60;. To search tenancy units that contain at least one tenant resource with a given resource name &#39;projects/123456&#39;, use the query &#x60;tenant_resources.resource&#x3D;projects/123456&#x60;. Multiple expressions can be joined with &#x60;AND&#x60;s. Tenancy units must match all expressions to be included in the result set. For example, &#x60;tenant_resources.tag&#x3D;xyz AND tenant_resources.resource&#x3D;projects/123456&#x60;
    :type query: str

    """
    return web.Response(status=200)


async def serviceconsumermanagement_services_tenancy_units_add_project(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """serviceconsumermanagement_services_tenancy_units_add_project

    Add a new tenant project to the tenancy unit. There can be a maximum of 1024 tenant projects in a tenancy unit. If there are previously failed &#x60;AddTenantProject&#x60; calls, you might need to call &#x60;RemoveTenantProject&#x60; first to resolve them before you can make another call to &#x60;AddTenantProject&#x60; with the same tag. Operation.

    :param parent: Required. Name of the tenancy unit. Such as &#39;services/service.googleapis.com/projects/12345/tenancyUnits/abcd&#39;.
    :type parent: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = AddTenantProjectRequest.from_dict(body)
    return web.Response(status=200)


async def serviceconsumermanagement_services_tenancy_units_apply_project_config(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """serviceconsumermanagement_services_tenancy_units_apply_project_config

    Apply a configuration to an existing tenant project. This project must exist in an active state and have the original owner account. The caller must have permission to add a project to the given tenancy unit. The configuration is applied, but any existing settings on the project aren&#39;t modified. Specified policy bindings are applied. Existing bindings aren&#39;t modified. Specified services are activated. No service is deactivated. If specified, new billing configuration is applied. Omit a billing configuration to keep the existing one. A service account in the project is created if previously non existed. Specified labels will be appended to tenant project, note that the value of existing label key will be updated if the same label key is requested. The specified folder is ignored, as moving a tenant project to a different folder isn&#39;t supported. The operation fails if any of the steps fail, but no rollback of already applied configuration changes is attempted. Operation.

    :param name: Required. Name of the tenancy unit. Such as &#39;services/service.googleapis.com/projects/12345/tenancyUnits/abcd&#39;.
    :type name: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = ApplyTenantProjectConfigRequest.from_dict(body)
    return web.Response(status=200)


async def serviceconsumermanagement_services_tenancy_units_attach_project(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """serviceconsumermanagement_services_tenancy_units_attach_project

    Attach an existing project to the tenancy unit as a new tenant resource. The project could either be the tenant project reserved by calling &#x60;AddTenantProject&#x60; under a tenancy unit of a service producer&#39;s project of a managed service, or from a separate project. The caller is checked against a set of permissions as if calling &#x60;AddTenantProject&#x60; on the same service consumer. To trigger the attachment, the targeted tenant project must be in a folder. Make sure the ServiceConsumerManagement service account is the owner of that project. These two requirements are already met if the project is reserved by calling &#x60;AddTenantProject&#x60;. Operation.

    :param name: Required. Name of the tenancy unit that the project will be attached to. Such as &#39;services/service.googleapis.com/projects/12345/tenancyUnits/abcd&#39;.
    :type name: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = AttachTenantProjectRequest.from_dict(body)
    return web.Response(status=200)


async def serviceconsumermanagement_services_tenancy_units_create(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """serviceconsumermanagement_services_tenancy_units_create

    Creates a tenancy unit with no tenant resources. If tenancy unit already exists, it will be returned, however, in this case, returned TenancyUnit does not have tenant_resources field set and ListTenancyUnits has to be used to get a complete TenancyUnit with all fields populated.

    :param parent: Required. services/{service}/{collection id}/{resource id} {collection id} is the cloud resource collection type representing the service consumer, for example &#39;projects&#39;, or &#39;organizations&#39;. {resource id} is the consumer numeric id, such as project number: &#39;123456&#39;. {service} the name of a managed service, such as &#39;service.googleapis.com&#39;. Enables service binding using the new tenancy unit.
    :type parent: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateTenancyUnitRequest.from_dict(body)
    return web.Response(status=200)


async def serviceconsumermanagement_services_tenancy_units_delete(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None) -> web.Response:
    """serviceconsumermanagement_services_tenancy_units_delete

    Delete a tenancy unit. Before you delete the tenancy unit, there should be no tenant resources in it that aren&#39;t in a DELETED state. Operation.

    :param name: Required. Name of the tenancy unit to be deleted.
    :type name: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str

    """
    return web.Response(status=200)


async def serviceconsumermanagement_services_tenancy_units_delete_project(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """serviceconsumermanagement_services_tenancy_units_delete_project

    Deletes the specified project resource identified by a tenant resource tag. The mothod removes a project lien with a &#39;TenantManager&#39; origin if that was added. It will then attempt to delete the project. If that operation fails, this method also fails. After the project has been deleted, the tenant resource state is set to DELETED. To permanently remove resource metadata, call the &#x60;RemoveTenantProject&#x60; method. New resources with the same tag can&#39;t be added if there are existing resources in a DELETED state. Operation.

    :param name: Required. Name of the tenancy unit. Such as &#39;services/service.googleapis.com/projects/12345/tenancyUnits/abcd&#39;.
    :type name: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = DeleteTenantProjectRequest.from_dict(body)
    return web.Response(status=200)


async def serviceconsumermanagement_services_tenancy_units_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, filter=None, page_size=None, page_token=None) -> web.Response:
    """serviceconsumermanagement_services_tenancy_units_list

    Find the tenancy unit for a managed service and service consumer. This method shouldn&#39;t be used in a service producer&#39;s runtime path, for example to find the tenant project number when creating VMs. Service producers must persist the tenant project&#39;s information after the project is created.

    :param parent: Required. Managed service and service consumer. Required. services/{service}/{collection id}/{resource id} {collection id} is the cloud resource collection type representing the service consumer, for example &#39;projects&#39;, or &#39;organizations&#39;. {resource id} is the consumer numeric id, such as project number: &#39;123456&#39;. {service} the name of a service, such as &#39;service.googleapis.com&#39;.
    :type parent: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param filter: Optional. Filter expression over tenancy resources field. Optional.
    :type filter: str
    :param page_size: Optional. The maximum number of results returned by this request.
    :type page_size: int
    :param page_token: Optional. The continuation token, which is used to page through large result sets. To get the next page of results, set this parameter to the value of &#x60;nextPageToken&#x60; from the previous response.
    :type page_token: str

    """
    return web.Response(status=200)


async def serviceconsumermanagement_services_tenancy_units_remove_project(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """serviceconsumermanagement_services_tenancy_units_remove_project

    Removes the specified project resource identified by a tenant resource tag. The method removes the project lien with &#39;TenantManager&#39; origin if that was added. It then attempts to delete the project. If that operation fails, this method also fails. Calls to remove already removed or non-existent tenant project succeed. After the project has been deleted, or if was already in a DELETED state, resource metadata is permanently removed from the tenancy unit. Operation.

    :param name: Required. Name of the tenancy unit. Such as &#39;services/service.googleapis.com/projects/12345/tenancyUnits/abcd&#39;.
    :type name: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = RemoveTenantProjectRequest.from_dict(body)
    return web.Response(status=200)


async def serviceconsumermanagement_services_tenancy_units_undelete_project(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """serviceconsumermanagement_services_tenancy_units_undelete_project

    Attempts to undelete a previously deleted tenant project. The project must be in a DELETED state. There are no guarantees that an undeleted project will be in a fully restored and functional state. Call the &#x60;ApplyTenantProjectConfig&#x60; method to update its configuration and then validate all managed service resources. Operation.

    :param name: Required. Name of the tenancy unit. Such as &#39;services/service.googleapis.com/projects/12345/tenancyUnits/abcd&#39;.
    :type name: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = UndeleteTenantProjectRequest.from_dict(body)
    return web.Response(status=200)
