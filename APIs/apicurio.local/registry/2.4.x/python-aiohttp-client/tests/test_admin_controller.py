# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.artifact_type_info import ArtifactTypeInfo
from openapi_server.models.configuration_property import ConfigurationProperty
from openapi_server.models.download_ref import DownloadRef
from openapi_server.models.error import Error
from openapi_server.models.log_configuration import LogConfiguration
from openapi_server.models.named_log_configuration import NamedLogConfiguration
from openapi_server.models.role_mapping import RoleMapping
from openapi_server.models.rule import Rule
from openapi_server.models.rule_type import RuleType
from openapi_server.models.update_configuration_property import UpdateConfigurationProperty
from openapi_server.models.update_role import UpdateRole


pytestmark = pytest.mark.asyncio

async def test_create_global_rule_0(client):
    """Test case for create_global_rule_0

    Create global rule
    """
    body = {"config":"FULL","type":"VALIDITY"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/admin/rules',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_role_mapping(client):
    """Test case for create_role_mapping

    Create a new role mapping
    """
    body = {"principalId":"svc_account_84874587_123484","principalName":"famartin-svc-account","role":"READ_ONLY"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/admin/roleMappings',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_all_global_rules_0(client):
    """Test case for delete_all_global_rules_0

    Delete all global rules
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/admin/rules',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_global_rule_0(client):
    """Test case for delete_global_rule_0

    Delete global rule
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/admin/rules/{rule}'.format(rule=openapi_server.RuleType()),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_role_mapping(client):
    """Test case for delete_role_mapping

    Delete a role mapping
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/admin/roleMappings/{principal_id}'.format(principal_id='principal_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_export_data(client):
    """Test case for export_data

    Export registry data
    """
    params = [('forBrowser', True)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/admin/export',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_config_property(client):
    """Test case for get_config_property

    Get configuration property value
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/admin/config/properties/{property_name}'.format(property_name='property_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_global_rule_config_0(client):
    """Test case for get_global_rule_config_0

    Get global rule configuration
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/admin/rules/{rule}'.format(rule=openapi_server.RuleType()),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_log_configuration(client):
    """Test case for get_log_configuration

    Get a single logger configuration
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/admin/loggers/{logger}'.format(logger='logger_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_role_mapping(client):
    """Test case for get_role_mapping

    Return a single role mapping
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/admin/roleMappings/{principal_id}'.format(principal_id='principal_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/zip not supported by Connexion")
async def test_import_data(client):
    """Test case for import_data

    Import registry data
    """
    body = '/path/to/file'
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/zip',
        'x_registry_preserve_global_id': True,
        'x_registry_preserve_content_id': True,
    }
    response = await client.request(
        method='POST',
        path='/admin/import',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_artifact_types_0(client):
    """Test case for list_artifact_types_0

    List artifact types
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/admin/artifactTypes',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_config_properties(client):
    """Test case for list_config_properties

    List all configuration properties
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/admin/config/properties',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_global_rules_0(client):
    """Test case for list_global_rules_0

    List global rules
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/admin/rules',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_log_configurations(client):
    """Test case for list_log_configurations

    List logging configurations
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/admin/loggers',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_role_mappings(client):
    """Test case for list_role_mappings

    List all role mappings
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/admin/roleMappings',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_remove_log_configuration(client):
    """Test case for remove_log_configuration

    Removes logger configuration
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/admin/loggers/{logger}'.format(logger='logger_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_reset_config_property(client):
    """Test case for reset_config_property

    Reset a configuration property
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/admin/config/properties/{property_name}'.format(property_name='property_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_set_log_configuration(client):
    """Test case for set_log_configuration

    Set a logger's configuration
    """
    body = {"level":"DEBUG"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/admin/loggers/{logger}'.format(logger='logger_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_config_property(client):
    """Test case for update_config_property

    Update a configuration property
    """
    body = {"value":"true"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/admin/config/properties/{property_name}'.format(property_name='property_name_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_global_rule_config_0(client):
    """Test case for update_global_rule_config_0

    Update global rule configuration
    """
    body = {"config":"FULL","type":"VALIDITY"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/admin/rules/{rule}'.format(rule=openapi_server.RuleType()),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_role_mapping(client):
    """Test case for update_role_mapping

    Update a role mapping
    """
    body = {"role":"READ_ONLY"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/admin/roleMappings/{principal_id}'.format(principal_id='principal_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

