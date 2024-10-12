from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_token import ApiToken
from openapi_server.models.api_token_collection import ApiTokenCollection
from openapi_server.models.continuous_data_export import ContinuousDataExport
from openapi_server.models.continuous_data_export_collection import ContinuousDataExportCollection
from openapi_server.models.device import Device
from openapi_server.models.device_collection import DeviceCollection
from openapi_server.models.device_command import DeviceCommand
from openapi_server.models.device_command_collection import DeviceCommandCollection
from openapi_server.models.device_credentials import DeviceCredentials
from openapi_server.models.device_template import DeviceTemplate
from openapi_server.models.device_template_collection import DeviceTemplateCollection
from openapi_server.models.role import Role
from openapi_server.models.role_collection import RoleCollection
from openapi_server.models.value import Value
from openapi_server import util


async def api_tokens_get(request: web.Request, token_id) -> web.Response:
    """Get an API token by ID.

    

    :param token_id: Unique ID for the API token.
    :type token_id: str

    """
    return web.Response(status=200)


async def api_tokens_list(request: web.Request, ) -> web.Response:
    """Get the list of API tokens in an application.

    


    """
    return web.Response(status=200)


async def api_tokens_remove(request: web.Request, token_id) -> web.Response:
    """Delete an API token.

    

    :param token_id: Unique ID for the API token.
    :type token_id: str

    """
    return web.Response(status=200)


async def api_tokens_set(request: web.Request, token_id, body) -> web.Response:
    """Create a new API token in the application.

    

    :param token_id: Unique ID for the API token.
    :type token_id: str
    :param body: API token body.
    :type body: dict | bytes

    """
    body = ApiToken.from_dict(body)
    return web.Response(status=200)


async def continuous_data_exports_get(request: web.Request, export_id) -> web.Response:
    """Get a continuous data export by ID.

    

    :param export_id: Unique ID for the continuous data export.
    :type export_id: str

    """
    return web.Response(status=200)


async def continuous_data_exports_list(request: web.Request, ) -> web.Response:
    """Get the list of continuous data exports in an application.

    


    """
    return web.Response(status=200)


async def continuous_data_exports_remove(request: web.Request, export_id) -> web.Response:
    """Delete a continuous data export.

    

    :param export_id: Unique ID for the continuous data export.
    :type export_id: str

    """
    return web.Response(status=200)


async def continuous_data_exports_set(request: web.Request, export_id, body) -> web.Response:
    """Create a new continuous data export or update an existing one by ID.

    

    :param export_id: Unique ID for the continuous data export.
    :type export_id: str
    :param body: Data export body.
    :type body: dict | bytes

    """
    body = ContinuousDataExport.from_dict(body)
    return web.Response(status=200)


async def device_templates_get(request: web.Request, device_template_id) -> web.Response:
    """Get a device template by ID

    

    :param device_template_id: Unique ID of the device template.
    :type device_template_id: str

    """
    return web.Response(status=200)


async def device_templates_get_merged(request: web.Request, device_template_id) -> web.Response:
    """Get a merged device template by ID

    

    :param device_template_id: Unique ID of the device template.
    :type device_template_id: str

    """
    return web.Response(status=200)


async def device_templates_list(request: web.Request, ) -> web.Response:
    """Get the list of device templates in an application

    


    """
    return web.Response(status=200)


async def device_templates_list_devices(request: web.Request, device_template_id) -> web.Response:
    """Get devices for a template

    

    :param device_template_id: Unique ID of the device template.
    :type device_template_id: str

    """
    return web.Response(status=200)


async def device_templates_remove(request: web.Request, device_template_id) -> web.Response:
    """Delete a device template

    Delete an existing device template by device ID.

    :param device_template_id: Unique ID of the device template.
    :type device_template_id: str

    """
    return web.Response(status=200)


async def device_templates_set(request: web.Request, device_template_id, body) -> web.Response:
    """Create or update a device template by ID

    

    :param device_template_id: Unique ID of the device template.
    :type device_template_id: str
    :param body: Device template body.
    :type body: dict | bytes

    """
    body = DeviceTemplate.from_dict(body)
    return web.Response(status=200)


async def devices_execute_command(request: web.Request, device_id, component_name, command_name, body) -> web.Response:
    """Execute a device command

    Execute a command on a device.

    :param device_id: Unique ID of the device.
    :type device_id: str
    :param component_name: Name of the device component.
    :type component_name: str
    :param command_name: Name of this device command.
    :type command_name: str
    :param body: Device command body.
    :type body: dict | bytes

    """
    body = DeviceCommand.from_dict(body)
    return web.Response(status=200)


async def devices_get(request: web.Request, device_id) -> web.Response:
    """Get a device by ID

    Get details about an existing device by device ID.

    :param device_id: Unique ID of the device.
    :type device_id: str

    """
    return web.Response(status=200)


async def devices_get_cloud_properties(request: web.Request, device_id) -> web.Response:
    """Get device cloud properties

    Get all cloud property values of a device by device ID.

    :param device_id: Unique ID of the device.
    :type device_id: str

    """
    return web.Response(status=200)


async def devices_get_command_history(request: web.Request, device_id, component_name, command_name) -> web.Response:
    """Get device command history

    

    :param device_id: Unique ID of the device.
    :type device_id: str
    :param component_name: Name of the device component.
    :type component_name: str
    :param command_name: Name of this device command.
    :type command_name: str

    """
    return web.Response(status=200)


async def devices_get_component_properties(request: web.Request, device_id, component_name) -> web.Response:
    """Get device properties for a specific component

    

    :param device_id: Unique ID of the device.
    :type device_id: str
    :param component_name: Name of the device component.
    :type component_name: str

    """
    return web.Response(status=200)


async def devices_get_credentials(request: web.Request, device_id) -> web.Response:
    """Get device credentials

    

    :param device_id: Unique ID of the device.
    :type device_id: str

    """
    return web.Response(status=200)


async def devices_get_properties(request: web.Request, device_id) -> web.Response:
    """Get device properties

    Get all property values of a device by device ID.

    :param device_id: Unique ID of the device.
    :type device_id: str

    """
    return web.Response(status=200)


async def devices_get_telemetry_value(request: web.Request, device_id, component_name, telemetry_name) -> web.Response:
    """Get device telemetry value

    

    :param device_id: Unique ID of the device.
    :type device_id: str
    :param component_name: Name of the device component.
    :type component_name: str
    :param telemetry_name: Name of this device telemetry.
    :type telemetry_name: str

    """
    return web.Response(status=200)


async def devices_list(request: web.Request, ) -> web.Response:
    """Get the list of devices in an application

    


    """
    return web.Response(status=200)


async def devices_remove(request: web.Request, device_id) -> web.Response:
    """Delete a device

    Delete an existing device by device ID.

    :param device_id: Unique ID of the device.
    :type device_id: str

    """
    return web.Response(status=200)


async def devices_set(request: web.Request, device_id, body) -> web.Response:
    """Create or update a device

    Create a new device or update an existing one by device ID.

    :param device_id: Unique ID of the device.
    :type device_id: str
    :param body: Device body.
    :type body: dict | bytes

    """
    body = Device.from_dict(body)
    return web.Response(status=200)


async def devices_update_cloud_properties(request: web.Request, device_id, body) -> web.Response:
    """Update device cloud properties

    Update all cloud property values of a device by device ID.

    :param device_id: Unique ID of the device.
    :type device_id: str
    :param body: Device properties.
    :type body: Dict[str, ]

    """
    return web.Response(status=200)


async def devices_update_component_properties(request: web.Request, device_id, component_name, body) -> web.Response:
    """Update device properties for a specific component

    

    :param device_id: Unique ID of the device.
    :type device_id: str
    :param component_name: Name of the device component.
    :type component_name: str
    :param body: Device properties.
    :type body: Dict[str, ]

    """
    return web.Response(status=200)


async def devices_update_properties(request: web.Request, device_id, body) -> web.Response:
    """Update device properties

    Update all property values of a device by device ID.

    :param device_id: Unique ID of the device.
    :type device_id: str
    :param body: Device properties.
    :type body: Dict[str, ]

    """
    return web.Response(status=200)


async def roles_get(request: web.Request, role_id) -> web.Response:
    """Get a role by ID.

    

    :param role_id: Unique ID for the role.
    :type role_id: str

    """
    return web.Response(status=200)


async def roles_list(request: web.Request, ) -> web.Response:
    """Get the list of roles in an application.

    


    """
    return web.Response(status=200)
