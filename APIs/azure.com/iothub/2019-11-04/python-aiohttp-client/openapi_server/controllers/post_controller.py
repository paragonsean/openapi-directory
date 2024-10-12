from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_details import ErrorDetails
from openapi_server.models.export_devices_request import ExportDevicesRequest
from openapi_server.models.failover_input import FailoverInput
from openapi_server.models.import_devices_request import ImportDevicesRequest
from openapi_server.models.iot_hub_name_availability_info import IotHubNameAvailabilityInfo
from openapi_server.models.job_response import JobResponse
from openapi_server.models.operation_inputs import OperationInputs
from openapi_server.models.shared_access_signature_authorization_rule import SharedAccessSignatureAuthorizationRule
from openapi_server.models.shared_access_signature_authorization_rule_list_result import SharedAccessSignatureAuthorizationRuleListResult
from openapi_server.models.test_all_routes_input import TestAllRoutesInput
from openapi_server.models.test_all_routes_result import TestAllRoutesResult
from openapi_server.models.test_route_input import TestRouteInput
from openapi_server.models.test_route_result import TestRouteResult
from openapi_server import util


async def iot_hub_manual_failover(request: web.Request, iot_hub_name, subscription_id, resource_group_name, api_version, failover_input) -> web.Response:
    """Manually initiate a failover for the IoT Hub to its secondary region

    Manually initiate a failover for the IoT Hub to its secondary region. To learn more, see https://aka.ms/manualfailover

    :param iot_hub_name: Name of the IoT hub to failover
    :type iot_hub_name: str
    :param subscription_id: The subscription identifier.
    :type subscription_id: str
    :param resource_group_name: Name of the resource group containing the IoT hub resource
    :type resource_group_name: str
    :param api_version: The version of the API.
    :type api_version: str
    :param failover_input: Region to failover to. Must be the Azure paired region. Get the value from the secondary location in the locations property. To learn more, see https://aka.ms/manualfailover/region
    :type failover_input: dict | bytes

    """
    failover_input = FailoverInput.from_dict(failover_input)
    return web.Response(status=200)


async def iot_hub_resource_check_name_availability(request: web.Request, api_version, subscription_id, operation_inputs) -> web.Response:
    """Check if an IoT hub name is available

    Check if an IoT hub name is available.

    :param api_version: The version of the API.
    :type api_version: str
    :param subscription_id: The subscription identifier.
    :type subscription_id: str
    :param operation_inputs: Set the name parameter in the OperationInputs structure to the name of the IoT hub to check.
    :type operation_inputs: dict | bytes

    """
    operation_inputs = OperationInputs.from_dict(operation_inputs)
    return web.Response(status=200)


async def iot_hub_resource_export_devices(request: web.Request, api_version, subscription_id, resource_group_name, resource_name, export_devices_parameters) -> web.Response:
    """Exports all the device identities in the IoT hub identity registry to an Azure Storage blob container. For more information, see: https://docs.microsoft.com/azure/iot-hub/iot-hub-devguide-identity-registry#import-and-export-device-identities

    Exports all the device identities in the IoT hub identity registry to an Azure Storage blob container. For more information, see: https://docs.microsoft.com/azure/iot-hub/iot-hub-devguide-identity-registry#import-and-export-device-identities.

    :param api_version: The version of the API.
    :type api_version: str
    :param subscription_id: The subscription identifier.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group that contains the IoT hub.
    :type resource_group_name: str
    :param resource_name: The name of the IoT hub.
    :type resource_name: str
    :param export_devices_parameters: The parameters that specify the export devices operation.
    :type export_devices_parameters: dict | bytes

    """
    export_devices_parameters = ExportDevicesRequest.from_dict(export_devices_parameters)
    return web.Response(status=200)


async def iot_hub_resource_get_keys_for_key_name(request: web.Request, api_version, subscription_id, resource_group_name, resource_name, key_name) -> web.Response:
    """Get a shared access policy by name from an IoT hub. For more information, see: https://docs.microsoft.com/azure/iot-hub/iot-hub-devguide-security

    Get a shared access policy by name from an IoT hub. For more information, see: https://docs.microsoft.com/azure/iot-hub/iot-hub-devguide-security.

    :param api_version: The version of the API.
    :type api_version: str
    :param subscription_id: The subscription identifier.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group that contains the IoT hub.
    :type resource_group_name: str
    :param resource_name: The name of the IoT hub.
    :type resource_name: str
    :param key_name: The name of the shared access policy.
    :type key_name: str

    """
    return web.Response(status=200)


async def iot_hub_resource_import_devices(request: web.Request, api_version, subscription_id, resource_group_name, resource_name, import_devices_parameters) -> web.Response:
    """Import, update, or delete device identities in the IoT hub identity registry from a blob. For more information, see: https://docs.microsoft.com/azure/iot-hub/iot-hub-devguide-identity-registry#import-and-export-device-identities

    Import, update, or delete device identities in the IoT hub identity registry from a blob. For more information, see: https://docs.microsoft.com/azure/iot-hub/iot-hub-devguide-identity-registry#import-and-export-device-identities.

    :param api_version: The version of the API.
    :type api_version: str
    :param subscription_id: The subscription identifier.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group that contains the IoT hub.
    :type resource_group_name: str
    :param resource_name: The name of the IoT hub.
    :type resource_name: str
    :param import_devices_parameters: The parameters that specify the import devices operation.
    :type import_devices_parameters: dict | bytes

    """
    import_devices_parameters = ImportDevicesRequest.from_dict(import_devices_parameters)
    return web.Response(status=200)


async def iot_hub_resource_list_keys(request: web.Request, api_version, subscription_id, resource_group_name, resource_name) -> web.Response:
    """Get the security metadata for an IoT hub. For more information, see: https://docs.microsoft.com/azure/iot-hub/iot-hub-devguide-security

    Get the security metadata for an IoT hub. For more information, see: https://docs.microsoft.com/azure/iot-hub/iot-hub-devguide-security.

    :param api_version: The version of the API.
    :type api_version: str
    :param subscription_id: The subscription identifier.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group that contains the IoT hub.
    :type resource_group_name: str
    :param resource_name: The name of the IoT hub.
    :type resource_name: str

    """
    return web.Response(status=200)


async def iot_hub_resource_test_all_routes(request: web.Request, iot_hub_name, subscription_id, resource_group_name, api_version, input) -> web.Response:
    """Test all routes

    Test all routes configured in this Iot Hub

    :param iot_hub_name: IotHub to be tested
    :type iot_hub_name: str
    :param subscription_id: The subscription identifier.
    :type subscription_id: str
    :param resource_group_name: resource group which Iot Hub belongs to
    :type resource_group_name: str
    :param api_version: The version of the API.
    :type api_version: str
    :param input: Input for testing all routes
    :type input: dict | bytes

    """
    input = TestAllRoutesInput.from_dict(input)
    return web.Response(status=200)


async def iot_hub_resource_test_route(request: web.Request, iot_hub_name, subscription_id, resource_group_name, api_version, input) -> web.Response:
    """Test the new route

    Test the new route for this Iot Hub

    :param iot_hub_name: IotHub to be tested
    :type iot_hub_name: str
    :param subscription_id: The subscription identifier.
    :type subscription_id: str
    :param resource_group_name: resource group which Iot Hub belongs to
    :type resource_group_name: str
    :param api_version: The version of the API.
    :type api_version: str
    :param input: Route that needs to be tested
    :type input: dict | bytes

    """
    input = TestRouteInput.from_dict(input)
    return web.Response(status=200)
