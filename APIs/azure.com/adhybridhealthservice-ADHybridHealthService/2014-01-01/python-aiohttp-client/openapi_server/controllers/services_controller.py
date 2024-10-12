from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_counts import ErrorCounts
from openapi_server.models.export_statuses import ExportStatuses
from openapi_server.models.item import Item
from openapi_server.models.items import Items
from openapi_server.models.merged_export_errors import MergedExportErrors
from openapi_server.models.result import Result
from openapi_server.models.service_properties import ServiceProperties
from openapi_server.models.services import Services
from openapi_server import util


async def adds_services_delete(request: web.Request, service_name, api_version, confirm=None) -> web.Response:
    """adds_services_delete

    Deletes an Active Directory Domain Service which is onboarded to Azure Active Directory Connect Health.

    :param service_name: The name of the service which needs to be deleted.
    :type service_name: str
    :param api_version: The version of the API to be used with the client request.
    :type api_version: str
    :param confirm: Indicates if the service will be permanently deleted or disabled. True indicates that the service will be permanently deleted and False indicates that the service will be marked disabled and then deleted after 30 days, if it is not re-registered.
    :type confirm: bool

    """
    return web.Response(status=200)


async def adds_services_get(request: web.Request, service_name, api_version) -> web.Response:
    """adds_services_get

    Gets the details of an Active Directory Domain Service for a tenant having Azure AD Premium license and is onboarded to Azure Active Directory Connect Health.

    :param service_name: The name of the service.
    :type service_name: str
    :param api_version: The version of the API to be used with the client request.
    :type api_version: str

    """
    return web.Response(status=200)


async def adds_services_list_premium_services(request: web.Request, api_version, filter=None, service_type=None, skip_count=None, take_count=None) -> web.Response:
    """adds_services_list_premium_services

    Gets the details of Active Directory Domain Services for a tenant having Azure AD Premium license and is onboarded to Azure Active Directory Connect Health.

    :param api_version: The version of the API to be used with the client request.
    :type api_version: str
    :param filter: The service property filter to apply.
    :type filter: str
    :param service_type: The service type for the services onboarded to Azure Active Directory Connect Health. Depending on whether the service is monitoring, ADFS, Sync or ADDS roles, the service type can either be AdFederationService or AadSyncService or AdDomainService.
    :type service_type: str
    :param skip_count: The skip count, which specifies the number of elements that can be bypassed from a sequence and then return the remaining elements.
    :type skip_count: int
    :param take_count: The take count , which specifies the number of elements that can be returned from a sequence.
    :type take_count: int

    """
    return web.Response(status=200)


async def adds_services_update(request: web.Request, service_name, api_version, service) -> web.Response:
    """adds_services_update

    Updates an Active Directory Domain Service properties of an onboarded service.

    :param service_name: The name of the service which needs to be deleted.
    :type service_name: str
    :param api_version: The version of the API to be used with the client request.
    :type api_version: str
    :param service: The service object.
    :type service: dict | bytes

    """
    service = ServiceProperties.from_dict(service)
    return web.Response(status=200)


async def services_add(request: web.Request, api_version, service) -> web.Response:
    """services_add

    Onboards a service for a given tenant in Azure Active Directory Connect Health.

    :param api_version: The version of the API to be used with the client request.
    :type api_version: str
    :param service: The service object.
    :type service: dict | bytes

    """
    service = ServiceProperties.from_dict(service)
    return web.Response(status=200)


async def services_delete(request: web.Request, service_name, api_version, confirm=None) -> web.Response:
    """services_delete

    Deletes a service which is onboarded to Azure Active Directory Connect Health.

    :param service_name: The name of the service which needs to be deleted.
    :type service_name: str
    :param api_version: The version of the API to be used with the client request.
    :type api_version: str
    :param confirm: Indicates if the service will be permanently deleted or disabled. True indicates that the service will be permanently deleted and False indicates that the service will be marked disabled and then deleted after 30 days, if it is not re-registered.
    :type confirm: bool

    """
    return web.Response(status=200)


async def services_get(request: web.Request, service_name, api_version) -> web.Response:
    """services_get

    Gets the details of a service for a tenant having Azure AD Premium license and is onboarded to Azure Active Directory Connect Health.

    :param service_name: The name of the service.
    :type service_name: str
    :param api_version: The version of the API to be used with the client request.
    :type api_version: str

    """
    return web.Response(status=200)


async def services_get_feature_availibility(request: web.Request, service_name, feature_name, api_version) -> web.Response:
    """services_get_feature_availibility

    Checks if the service has all the pre-requisites met to use a feature.

    :param service_name: The name of the service.
    :type service_name: str
    :param feature_name: The name of the feature.
    :type feature_name: str
    :param api_version: The version of the API to be used with the client request.
    :type api_version: str

    """
    return web.Response(status=200)


async def services_get_tenant_whitelisting(request: web.Request, service_name, feature_name, api_version) -> web.Response:
    """services_get_tenant_whitelisting

    Checks if the tenant, to which a service is registered, is whitelisted to use a feature.

    :param service_name: The name of the service.
    :type service_name: str
    :param feature_name: The name of the feature.
    :type feature_name: str
    :param api_version: The version of the API to be used with the client request.
    :type api_version: str

    """
    return web.Response(status=200)


async def services_list(request: web.Request, api_version, filter=None, service_type=None, skip_count=None, take_count=None) -> web.Response:
    """services_list

    Gets the details of services, for a tenant, that are onboarded to Azure Active Directory Connect Health.

    :param api_version: The version of the API to be used with the client request.
    :type api_version: str
    :param filter: The service property filter to apply.
    :type filter: str
    :param service_type: The service type for the services onboarded to Azure Active Directory Connect Health. Depending on whether the service is monitoring, ADFS, Sync or ADDS roles, the service type can either be AdFederationService or AadSyncService or AdDomainService.
    :type service_type: str
    :param skip_count: The skip count, which specifies the number of elements that can be bypassed from a sequence and then return the remaining elements.
    :type skip_count: int
    :param take_count: The take count , which specifies the number of elements that can be returned from a sequence.
    :type take_count: int

    """
    return web.Response(status=200)


async def services_list_export_errors(request: web.Request, service_name, api_version) -> web.Response:
    """services_list_export_errors

    Gets the count of latest AAD export errors.

    :param service_name: The name of the service.
    :type service_name: str
    :param api_version: The version of the API to be used with the client request.
    :type api_version: str

    """
    return web.Response(status=200)


async def services_list_export_errors_v2(request: web.Request, service_name, error_bucket, api_version) -> web.Response:
    """services_list_export_errors_v2

     Gets the categorized export errors.

    :param service_name: The name of the service.
    :type service_name: str
    :param error_bucket: The error category to query for.
    :type error_bucket: str
    :param api_version: The version of the API to be used with the client request.
    :type api_version: str

    """
    return web.Response(status=200)


async def services_list_export_status(request: web.Request, service_name, api_version) -> web.Response:
    """services_list_export_status

    Gets the export status.

    :param service_name: The name of the service.
    :type service_name: str
    :param api_version: The version of the API to be used with the client request.
    :type api_version: str

    """
    return web.Response(status=200)


async def services_list_monitoring_configurations(request: web.Request, service_name, api_version) -> web.Response:
    """services_list_monitoring_configurations

    Gets the service level monitoring configurations.

    :param service_name: The name of the service.
    :type service_name: str
    :param api_version: The version of the API to be used with the client request.
    :type api_version: str

    """
    return web.Response(status=200)


async def services_list_premium(request: web.Request, api_version, filter=None, service_type=None, skip_count=None, take_count=None) -> web.Response:
    """services_list_premium

    Gets the details of services for a tenant having Azure AD Premium license and is onboarded to Azure Active Directory Connect Health.

    :param api_version: The version of the API to be used with the client request.
    :type api_version: str
    :param filter: The service property filter to apply.
    :type filter: str
    :param service_type: The service type for the services onboarded to Azure Active Directory Connect Health. Depending on whether the service is monitoring, ADFS, Sync or ADDS roles, the service type can either be AdFederationService or AadSyncService or AdDomainService.
    :type service_type: str
    :param skip_count: The skip count, which specifies the number of elements that can be bypassed from a sequence and then return the remaining elements.
    :type skip_count: int
    :param take_count: The take count , which specifies the number of elements that can be returned from a sequence.
    :type take_count: int

    """
    return web.Response(status=200)


async def services_update(request: web.Request, service_name, api_version, service) -> web.Response:
    """services_update

    Updates the service properties of an onboarded service.

    :param service_name: The name of the service which needs to be deleted.
    :type service_name: str
    :param api_version: The version of the API to be used with the client request.
    :type api_version: str
    :param service: The service object.
    :type service: dict | bytes

    """
    service = ServiceProperties.from_dict(service)
    return web.Response(status=200)


async def services_update_monitoring_configuration(request: web.Request, service_name, api_version, configuration_setting) -> web.Response:
    """services_update_monitoring_configuration

    Updates the service level monitoring configuration.

    :param service_name: The name of the service.
    :type service_name: str
    :param api_version: The version of the API to be used with the client request.
    :type api_version: str
    :param configuration_setting: The monitoring configuration to update
    :type configuration_setting: dict | bytes

    """
    configuration_setting = Item.from_dict(configuration_setting)
    return web.Response(status=200)
