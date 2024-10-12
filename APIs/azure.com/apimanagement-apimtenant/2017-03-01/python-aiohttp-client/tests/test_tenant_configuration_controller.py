# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.deploy_configuration_parameters import DeployConfigurationParameters
from openapi_server.models.operation_result_contract import OperationResultContract
from openapi_server.models.save_configuration_parameter import SaveConfigurationParameter
from openapi_server.models.tenant_access_update_default_response import TenantAccessUpdateDefaultResponse


pytestmark = pytest.mark.asyncio

async def test_tenant_configuration_deploy(client):
    """Test case for tenant_configuration_deploy

    
    """
    parameters = {"force":True,"branch":"branch"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/tenant/{configuration_name}/deploy'.format(configuration_name='configuration_name_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tenant_configuration_save(client):
    """Test case for tenant_configuration_save

    
    """
    parameters = {"force":True,"branch":"branch"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/tenant/{configuration_name}/save'.format(configuration_name='configuration_name_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tenant_configuration_validate(client):
    """Test case for tenant_configuration_validate

    
    """
    parameters = {"force":True,"branch":"branch"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/tenant/{configuration_name}/validate'.format(configuration_name='configuration_name_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

