from typing import List, Dict
from aiohttp import web

from openapi_server.models.application_type_manifest import ApplicationTypeManifest
from openapi_server.models.fabric_error import FabricError
from openapi_server.models.paged_application_type_info_list import PagedApplicationTypeInfoList
from openapi_server.models.provision_application_type_description_base import ProvisionApplicationTypeDescriptionBase
from openapi_server.models.unprovision_application_type_description_info import UnprovisionApplicationTypeDescriptionInfo
from openapi_server import util


async def get_application_manifest(request: web.Request, api_version, application_type_name, application_type_version, timeout=None) -> web.Response:
    """Gets the manifest describing an application type.

    Gets the manifest describing an application type. The response contains the application manifest XML as a string.

    :param api_version: The version of this API. This is a required parameter and its value must be \&quot;6.0\&quot;.  Service Fabric REST API version is based on the runtime version in which the API was introduced or was changed. Service Fabric runtime supports more than one version of the API. This is the latest supported version of the API. If a lower API version is passed, the returned response may be different from the one documented in this specification.  Additionally the runtime accept any version that is higher than the latest supported version up to the current version of the runtime. So if the latest API version is 6.0, but if the runtime is 6.1, in order to make it easier to write the clients, the runtime will accept version 6.1 for that API. However the behavior of the API will be as per the documented 6.0 version. 
    :type api_version: str
    :param application_type_name: The name of the application type.
    :type application_type_name: str
    :param application_type_version: The version of the application type.
    :type application_type_version: str
    :param timeout: The server timeout for performing the operation in seconds. This specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    :type timeout: int

    """
    return web.Response(status=200)


async def get_application_type_info_list(request: web.Request, api_version, application_type_definition_kind_filter=None, exclude_application_parameters=None, continuation_token=None, max_results=None, timeout=None) -> web.Response:
    """Gets the list of application types in the Service Fabric cluster.

    Returns the information about the application types that are provisioned or in the process of being provisioned in the Service Fabric cluster. Each version of an application type is returned as one application type. The response includes the name, version, status and other details about the application type. This is a paged query, meaning that if not all of the application types fit in a page, one page of results is returned as well as a continuation token which can be used to get the next page. For example, if there are 10 application types but a page only fits the first 3 application types, or if max results is set to 3, then 3 is returned. To access the rest of the results, retrieve subsequent pages by using the returned continuation token in the next query. An empty continuation token is returned if there are no subsequent pages.

    :param api_version: The version of this API. This is a required parameter and its value must be \&quot;6.0\&quot;.  Service Fabric REST API version is based on the runtime version in which the API was introduced or was changed. Service Fabric runtime supports more than one version of the API. This is the latest supported version of the API. If a lower API version is passed, the returned response may be different from the one documented in this specification.  Additionally the runtime accept any version that is higher than the latest supported version up to the current version of the runtime. So if the latest API version is 6.0, but if the runtime is 6.1, in order to make it easier to write the clients, the runtime will accept version 6.1 for that API. However the behavior of the API will be as per the documented 6.0 version. 
    :type api_version: str
    :param application_type_definition_kind_filter: Used to filter on ApplicationTypeDefinitionKind which is the mechanism used to define a Service Fabric application type. - Default - Default value, which performs the same function as selecting \&quot;All\&quot;. The value is 0. - All - Filter that matches input with any ApplicationTypeDefinitionKind value. The value is 65535. - ServiceFabricApplicationPackage - Filter that matches input with ApplicationTypeDefinitionKind value ServiceFabricApplicationPackage. The value is 1. - Compose - Filter that matches input with ApplicationTypeDefinitionKind value Compose. The value is 2. 
    :type application_type_definition_kind_filter: int
    :param exclude_application_parameters: The flag that specifies whether application parameters will be excluded from the result.
    :type exclude_application_parameters: bool
    :param continuation_token: The continuation token parameter is used to obtain next set of results. A continuation token with a non empty value is included in the response of the API when the results from the system do not fit in a single response. When this value is passed to the next API call, the API returns next set of results. If there are no further results then the continuation token does not contain a value. The value of this parameter should not be URL encoded.
    :type continuation_token: str
    :param max_results: The maximum number of results to be returned as part of the paged queries. This parameter defines the upper bound on the number of results returned. The results returned can be less than the specified maximum results if they do not fit in the message as per the max message size restrictions defined in the configuration. If this parameter is zero or not specified, the paged queries includes as much results as possible that fit in the return message.
    :type max_results: int
    :param timeout: The server timeout for performing the operation in seconds. This specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    :type timeout: int

    """
    return web.Response(status=200)


async def get_application_type_info_list_by_name(request: web.Request, api_version, application_type_name, application_type_version=None, exclude_application_parameters=None, continuation_token=None, max_results=None, timeout=None) -> web.Response:
    """Gets the list of application types in the Service Fabric cluster matching exactly the specified name.

    Returns the information about the application types that are provisioned or in the process of being provisioned in the Service Fabric cluster. These results are of application types whose name match exactly the one specified as the parameter, and which comply with the given query parameters. All versions of the application type matching the application type name are returned, with each version returned as one application type. The response includes the name, version, status and other details about the application type. This is a paged query, meaning that if not all of the application types fit in a page, one page of results is returned as well as a continuation token which can be used to get the next page. For example, if there are 10 application types but a page only fits the first 3 application types, or if max results is set to 3, then 3 is returned. To access the rest of the results, retrieve subsequent pages by using the returned continuation token in the next query. An empty continuation token is returned if there are no subsequent pages.

    :param api_version: The version of this API. This is a required parameter and its value must be \&quot;6.0\&quot;.  Service Fabric REST API version is based on the runtime version in which the API was introduced or was changed. Service Fabric runtime supports more than one version of the API. This is the latest supported version of the API. If a lower API version is passed, the returned response may be different from the one documented in this specification.  Additionally the runtime accept any version that is higher than the latest supported version up to the current version of the runtime. So if the latest API version is 6.0, but if the runtime is 6.1, in order to make it easier to write the clients, the runtime will accept version 6.1 for that API. However the behavior of the API will be as per the documented 6.0 version. 
    :type api_version: str
    :param application_type_name: The name of the application type.
    :type application_type_name: str
    :param application_type_version: The version of the application type.
    :type application_type_version: str
    :param exclude_application_parameters: The flag that specifies whether application parameters will be excluded from the result.
    :type exclude_application_parameters: bool
    :param continuation_token: The continuation token parameter is used to obtain next set of results. A continuation token with a non empty value is included in the response of the API when the results from the system do not fit in a single response. When this value is passed to the next API call, the API returns next set of results. If there are no further results then the continuation token does not contain a value. The value of this parameter should not be URL encoded.
    :type continuation_token: str
    :param max_results: The maximum number of results to be returned as part of the paged queries. This parameter defines the upper bound on the number of results returned. The results returned can be less than the specified maximum results if they do not fit in the message as per the max message size restrictions defined in the configuration. If this parameter is zero or not specified, the paged queries includes as much results as possible that fit in the return message.
    :type max_results: int
    :param timeout: The server timeout for performing the operation in seconds. This specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    :type timeout: int

    """
    return web.Response(status=200)


async def provision_application_type(request: web.Request, api_version, provision_application_type_description_base_required_body_param, timeout=None) -> web.Response:
    """Provisions or registers a Service Fabric application type with the cluster using the .sfpkg package in the external store or using the application package in the image store.

    Provisions a Service Fabric application type with the cluster. This is required before any new applications can be instantiated. The provision operation can be performed either on the application package specified by the relativePathInImageStore, or by using the URI of the external .sfpkg. 

    :param api_version: The version of this API. This is a required parameter and its value must be \&quot;6.1\&quot;.  Service Fabric REST API version is based on the runtime version in which the API was introduced or was changed. Service Fabric runtime supports more than one version of the API. This is the latest supported version of the API. If a lower API version is passed, the returned response may be different from the one documented in this specification.  Additionally the runtime accept any version that is higher than the latest supported version up to the current version of the runtime. So if the latest API version is 6.0, but if the runtime is 6.1, in order to make it easier to write the clients, the runtime will accept version 6.1 for that API. However the behavior of the API will be as per the documented 6.0 version. 
    :type api_version: str
    :param provision_application_type_description_base_required_body_param: The base type of provision application type description which supports either image store based provision or external store based provision.
    :type provision_application_type_description_base_required_body_param: dict | bytes
    :param timeout: The server timeout for performing the operation in seconds. This specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    :type timeout: int

    """
    provision_application_type_description_base_required_body_param = ProvisionApplicationTypeDescriptionBase.from_dict(provision_application_type_description_base_required_body_param)
    return web.Response(status=200)


async def unprovision_application_type(request: web.Request, api_version, application_type_name, unprovision_application_type_description_info, timeout=None) -> web.Response:
    """Removes or unregisters a Service Fabric application type from the cluster.

    Removes or unregisters a Service Fabric application type from the cluster. This operation can only be performed if all application instances of the application type has been deleted. Once the application type is unregistered, no new application instances can be created for this particular application type.

    :param api_version: The version of this API. This is a required parameter and its value must be \&quot;6.0\&quot;.  Service Fabric REST API version is based on the runtime version in which the API was introduced or was changed. Service Fabric runtime supports more than one version of the API. This is the latest supported version of the API. If a lower API version is passed, the returned response may be different from the one documented in this specification.  Additionally the runtime accept any version that is higher than the latest supported version up to the current version of the runtime. So if the latest API version is 6.0, but if the runtime is 6.1, in order to make it easier to write the clients, the runtime will accept version 6.1 for that API. However the behavior of the API will be as per the documented 6.0 version. 
    :type api_version: str
    :param application_type_name: The name of the application type.
    :type application_type_name: str
    :param unprovision_application_type_description_info: The relative path for the application package in the image store specified during the prior copy operation.
    :type unprovision_application_type_description_info: dict | bytes
    :param timeout: The server timeout for performing the operation in seconds. This specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    :type timeout: int

    """
    unprovision_application_type_description_info = UnprovisionApplicationTypeDescriptionInfo.from_dict(unprovision_application_type_description_info)
    return web.Response(status=200)
