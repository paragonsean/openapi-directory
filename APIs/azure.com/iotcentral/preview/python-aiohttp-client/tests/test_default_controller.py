# coding: utf-8

import pytest
import json
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


pytestmark = pytest.mark.asyncio

async def test_api_tokens_get(client):
    """Test case for api_tokens_get

    Get an API token by ID.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/preview/apiTokens/{token_id}'.format(token_id='token_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_tokens_list(client):
    """Test case for api_tokens_list

    Get the list of API tokens in an application.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/preview/apiTokens',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_tokens_remove(client):
    """Test case for api_tokens_remove

    Delete an API token.
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/api/preview/apiTokens/{token_id}'.format(token_id='token_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_tokens_set(client):
    """Test case for api_tokens_set

    Create a new API token in the application.
    """
    body = {"roles":["roles"],"expiry":"2000-01-23T04:56:07.000+00:00","id":"id","token":"token"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/api/preview/apiTokens/{token_id}'.format(token_id='token_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_continuous_data_exports_get(client):
    """Test case for continuous_data_exports_get

    Get a continuous data export by ID.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/preview/continuousDataExports/{export_id}'.format(export_id='export_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_continuous_data_exports_list(client):
    """Test case for continuous_data_exports_list

    Get the list of continuous data exports in an application.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/preview/continuousDataExports',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_continuous_data_exports_remove(client):
    """Test case for continuous_data_exports_remove

    Delete a continuous data export.
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/api/preview/continuousDataExports/{export_id}'.format(export_id='export_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_continuous_data_exports_set(client):
    """Test case for continuous_data_exports_set

    Create a new continuous data export or update an existing one by ID.
    """
    body = {"endpoint":{"connectionString":"connectionString","name":"name","type":"type"},"sources":["devices","devices"],"displayName":"displayName","etag":"etag","id":"id","enabled":True,"status":"status"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/api/preview/continuousDataExports/{export_id}'.format(export_id='export_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_device_templates_get(client):
    """Test case for device_templates_get

    Get a device template by ID
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/preview/deviceTemplates/{device_template_id}'.format(device_template_id='device_template_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_device_templates_get_merged(client):
    """Test case for device_templates_get_merged

    Get a merged device template by ID
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/preview/deviceTemplates/{device_template_id}/merged'.format(device_template_id='device_template_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_device_templates_list(client):
    """Test case for device_templates_list

    Get the list of device templates in an application
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/preview/deviceTemplates',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_device_templates_list_devices(client):
    """Test case for device_templates_list_devices

    Get devices for a template
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/preview/deviceTemplates/{device_template_id}/devices'.format(device_template_id='device_template_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_device_templates_remove(client):
    """Test case for device_templates_remove

    Delete a device template
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/api/preview/deviceTemplates/{device_template_id}'.format(device_template_id='device_template_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_device_templates_set(client):
    """Test case for device_templates_set

    Create or update a device template by ID
    """
    body = {"types":["types","types"],"displayName":"displayName","solutionModel":{"initialValues":[{"capability":{"reference":"reference","component":"component","@type":["@type","@type"],"displayName":"displayName","description":"description","comment":"comment","@id":"@id","@context":"{}"},"@type":["@type","@type"],"displayName":"displayName","description":"description","comment":"comment","@id":"@id","@context":"{}"},{"capability":{"reference":"reference","component":"component","@type":["@type","@type"],"displayName":"displayName","description":"description","comment":"comment","@id":"@id","@context":"{}"},"@type":["@type","@type"],"displayName":"displayName","description":"description","comment":"comment","@id":"@id","@context":"{}"}],"@type":["@type","@type"],"displayName":"displayName","cloudProperties":[{"@type":["@type","@type"],"displayName":"displayName","name":"name","description":"description","comment":"comment","@id":"@id","@context":"{}"},{"@type":["@type","@type"],"displayName":"displayName","name":"name","description":"description","comment":"comment","@id":"@id","@context":"{}"}],"description":"description","comment":"comment","@id":"@id","overrides":[{"capability":{"reference":"reference","component":"component","@type":["@type","@type"],"displayName":"displayName","description":"description","comment":"comment","@id":"@id","@context":"{}"},"unit":"unit","@type":["@type","@type"],"displayName":"displayName","semanticType":"semanticType","valueDetail":{"@type":["@type","@type"],"displayName":"displayName","description":"description","comment":"comment","@id":"@id","@context":"{}"},"description":"description","displayUnit":"displayUnit","comment":"comment","@id":"@id","@context":"{}"},{"capability":{"reference":"reference","component":"component","@type":["@type","@type"],"displayName":"displayName","description":"description","comment":"comment","@id":"@id","@context":"{}"},"unit":"unit","@type":["@type","@type"],"displayName":"displayName","semanticType":"semanticType","valueDetail":{"@type":["@type","@type"],"displayName":"displayName","description":"description","comment":"comment","@id":"@id","@context":"{}"},"description":"description","displayUnit":"displayUnit","comment":"comment","@id":"@id","@context":"{}"}],"@context":"{}"},"description":"description","etag":"etag","capabilityModel":{"implements":[{"schema":{"contents":[{"@type":["@type","@type"],"displayName":"displayName","name":"name","description":"description","comment":"comment","@id":"@id","@context":"{}"},{"@type":["@type","@type"],"displayName":"displayName","name":"name","description":"description","comment":"comment","@id":"@id","@context":"{}"}],"@type":["@type","@type"],"displayName":"displayName","description":"description","comment":"comment","@id":"@id","@context":"{}"},"@type":["@type","@type"],"displayName":"displayName","name":"name","description":"description","comment":"comment","@id":"@id","@context":"{}"},{"schema":{"contents":[{"@type":["@type","@type"],"displayName":"displayName","name":"name","description":"description","comment":"comment","@id":"@id","@context":"{}"},{"@type":["@type","@type"],"displayName":"displayName","name":"name","description":"description","comment":"comment","@id":"@id","@context":"{}"}],"@type":["@type","@type"],"displayName":"displayName","description":"description","comment":"comment","@id":"@id","@context":"{}"},"@type":["@type","@type"],"displayName":"displayName","name":"name","description":"description","comment":"comment","@id":"@id","@context":"{}"}],"contents":[{"@type":["@type","@type"],"displayName":"displayName","name":"name","description":"description","comment":"comment","@id":"@id","@context":"{}"},{"@type":["@type","@type"],"displayName":"displayName","name":"name","description":"description","comment":"comment","@id":"@id","@context":"{}"}],"@type":["@type","@type"],"displayName":"displayName","description":"description","comment":"comment","@id":"@id","@context":"{}"},"id":"id"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/api/preview/deviceTemplates/{device_template_id}'.format(device_template_id='device_template_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_devices_execute_command(client):
    """Test case for devices_execute_command

    Execute a device command
    """
    body = {"request":"{}","response":"{}","id":"id","responseCode":0.8008281904610115}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/preview/devices/{device_id}/components/{component_name}/commands/{command_name}'.format(device_id='device_id_example', component_name='component_name_example', command_name='command_name_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_devices_get(client):
    """Test case for devices_get

    Get a device by ID
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/preview/devices/{device_id}'.format(device_id='device_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_devices_get_cloud_properties(client):
    """Test case for devices_get_cloud_properties

    Get device cloud properties
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/preview/devices/{device_id}/cloudProperties'.format(device_id='device_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_devices_get_command_history(client):
    """Test case for devices_get_command_history

    Get device command history
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/preview/devices/{device_id}/components/{component_name}/commands/{command_name}'.format(device_id='device_id_example', component_name='component_name_example', command_name='command_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_devices_get_component_properties(client):
    """Test case for devices_get_component_properties

    Get device properties for a specific component
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/preview/devices/{device_id}/components/{component_name}/properties'.format(device_id='device_id_example', component_name='component_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_devices_get_credentials(client):
    """Test case for devices_get_credentials

    Get device credentials
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/preview/devices/{device_id}/credentials'.format(device_id='device_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_devices_get_properties(client):
    """Test case for devices_get_properties

    Get device properties
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/preview/devices/{device_id}/properties'.format(device_id='device_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_devices_get_telemetry_value(client):
    """Test case for devices_get_telemetry_value

    Get device telemetry value
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/preview/devices/{device_id}/components/{component_name}/telemetry/{telemetry_name}'.format(device_id='device_id_example', component_name='component_name_example', telemetry_name='telemetry_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_devices_list(client):
    """Test case for devices_list

    Get the list of devices in an application
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/preview/devices',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_devices_remove(client):
    """Test case for devices_remove

    Delete a device
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/api/preview/devices/{device_id}'.format(device_id='device_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_devices_set(client):
    """Test case for devices_set

    Create or update a device
    """
    body = {"approved":True,"provisioned":True,"displayName":"displayName","simulated":True,"description":"description","etag":"etag","id":"id","instanceOf":"instanceOf"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/api/preview/devices/{device_id}'.format(device_id='device_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_devices_update_cloud_properties(client):
    """Test case for devices_update_cloud_properties

    Update device cloud properties
    """
    body = None
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/api/preview/devices/{device_id}/cloudProperties'.format(device_id='device_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_devices_update_component_properties(client):
    """Test case for devices_update_component_properties

    Update device properties for a specific component
    """
    body = None
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/api/preview/devices/{device_id}/components/{component_name}/properties'.format(device_id='device_id_example', component_name='component_name_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_devices_update_properties(client):
    """Test case for devices_update_properties

    Update device properties
    """
    body = None
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/api/preview/devices/{device_id}/properties'.format(device_id='device_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_roles_get(client):
    """Test case for roles_get

    Get a role by ID.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/preview/roles/{role_id}'.format(role_id='role_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_roles_list(client):
    """Test case for roles_list

    Get the list of roles in an application.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/preview/roles',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

