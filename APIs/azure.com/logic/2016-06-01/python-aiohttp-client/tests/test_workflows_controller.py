# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.generate_upgraded_definition_parameters import GenerateUpgradedDefinitionParameters
from openapi_server.models.get_callback_url_parameters import GetCallbackUrlParameters
from openapi_server.models.regenerate_action_parameter import RegenerateActionParameter
from openapi_server.models.workflow import Workflow
from openapi_server.models.workflow_list_result import WorkflowListResult
from openapi_server.models.workflow_trigger_callback_url import WorkflowTriggerCallbackUrl


pytestmark = pytest.mark.asyncio

async def test_workflows_create_or_update(client):
    """Test case for workflows_create_or_update

    
    """
    workflow = {"properties":{"integrationAccount":{"name":"name","id":"id","type":"type"},"accessEndpoint":"accessEndpoint","createdTime":"2000-01-23T04:56:07.000+00:00","definition":"{}","changedTime":"2000-01-23T04:56:07.000+00:00","provisioningState":"NotSpecified","state":"NotSpecified","sku":{"name":"NotSpecified","plan":{"name":"name","id":"id","type":"type"}},"parameters":{"key":{"metadata":"{}","description":"description","type":"NotSpecified","value":"{}"}},"version":"version"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Logic/workflows/{workflow_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', workflow_name='workflow_name_example'),
        headers=headers,
        json=workflow,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_workflows_delete(client):
    """Test case for workflows_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Logic/workflows/{workflow_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', workflow_name='workflow_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_workflows_disable(client):
    """Test case for workflows_disable

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Logic/workflows/{workflow_name}/disable'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', workflow_name='workflow_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_workflows_enable(client):
    """Test case for workflows_enable

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Logic/workflows/{workflow_name}/enable'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', workflow_name='workflow_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_workflows_generate_upgraded_definition(client):
    """Test case for workflows_generate_upgraded_definition

    
    """
    parameters = {"targetSchemaVersion":"targetSchemaVersion"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Logic/workflows/{workflow_name}/generateUpgradedDefinition'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', workflow_name='workflow_name_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_workflows_get(client):
    """Test case for workflows_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Logic/workflows/{workflow_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', workflow_name='workflow_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_workflows_list_by_resource_group(client):
    """Test case for workflows_list_by_resource_group

    
    """
    params = [('api-version', 'api_version_example'),
                    ('$top', 56),
                    ('$filter', 'filter_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Logic/workflows'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_workflows_list_by_subscription(client):
    """Test case for workflows_list_by_subscription

    
    """
    params = [('api-version', 'api_version_example'),
                    ('$top', 56),
                    ('$filter', 'filter_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Logic/workflows'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_workflows_list_callback_url(client):
    """Test case for workflows_list_callback_url

    
    """
    list_callback_url = {"notAfter":"2000-01-23T04:56:07.000+00:00","keyType":"NotSpecified"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Logic/workflows/{workflow_name}/listCallbackUrl'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', workflow_name='workflow_name_example'),
        headers=headers,
        json=list_callback_url,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_workflows_list_swagger(client):
    """Test case for workflows_list_swagger

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Logic/workflows/{workflow_name}/listSwagger'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', workflow_name='workflow_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_workflows_move(client):
    """Test case for workflows_move

    
    """
    move = {"properties":{"integrationAccount":{"name":"name","id":"id","type":"type"},"accessEndpoint":"accessEndpoint","createdTime":"2000-01-23T04:56:07.000+00:00","definition":"{}","changedTime":"2000-01-23T04:56:07.000+00:00","provisioningState":"NotSpecified","state":"NotSpecified","sku":{"name":"NotSpecified","plan":{"name":"name","id":"id","type":"type"}},"parameters":{"key":{"metadata":"{}","description":"description","type":"NotSpecified","value":"{}"}},"version":"version"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Logic/workflows/{workflow_name}/move'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', workflow_name='workflow_name_example'),
        headers=headers,
        json=move,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_workflows_regenerate_access_key(client):
    """Test case for workflows_regenerate_access_key

    
    """
    key_type = {"keyType":"NotSpecified"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Logic/workflows/{workflow_name}/regenerateAccessKey'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', workflow_name='workflow_name_example'),
        headers=headers,
        json=key_type,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_workflows_update(client):
    """Test case for workflows_update

    
    """
    workflow = {"properties":{"integrationAccount":{"name":"name","id":"id","type":"type"},"accessEndpoint":"accessEndpoint","createdTime":"2000-01-23T04:56:07.000+00:00","definition":"{}","changedTime":"2000-01-23T04:56:07.000+00:00","provisioningState":"NotSpecified","state":"NotSpecified","sku":{"name":"NotSpecified","plan":{"name":"name","id":"id","type":"type"}},"parameters":{"key":{"metadata":"{}","description":"description","type":"NotSpecified","value":"{}"}},"version":"version"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Logic/workflows/{workflow_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', workflow_name='workflow_name_example'),
        headers=headers,
        json=workflow,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_workflows_validate(client):
    """Test case for workflows_validate

    
    """
    workflow = {"properties":{"integrationAccount":{"name":"name","id":"id","type":"type"},"accessEndpoint":"accessEndpoint","createdTime":"2000-01-23T04:56:07.000+00:00","definition":"{}","changedTime":"2000-01-23T04:56:07.000+00:00","provisioningState":"NotSpecified","state":"NotSpecified","sku":{"name":"NotSpecified","plan":{"name":"name","id":"id","type":"type"}},"parameters":{"key":{"metadata":"{}","description":"description","type":"NotSpecified","value":"{}"}},"version":"version"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Logic/locations/{location}/workflows/{workflow_name}/validate'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', location='location_example', workflow_name='workflow_name_example'),
        headers=headers,
        json=workflow,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_workflows_validate_workflow(client):
    """Test case for workflows_validate_workflow

    
    """
    validate = {"properties":{"integrationAccount":{"name":"name","id":"id","type":"type"},"accessEndpoint":"accessEndpoint","createdTime":"2000-01-23T04:56:07.000+00:00","definition":"{}","changedTime":"2000-01-23T04:56:07.000+00:00","provisioningState":"NotSpecified","state":"NotSpecified","sku":{"name":"NotSpecified","plan":{"name":"name","id":"id","type":"type"}},"parameters":{"key":{"metadata":"{}","description":"description","type":"NotSpecified","value":"{}"}},"version":"version"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Logic/workflows/{workflow_name}/validate'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', workflow_name='workflow_name_example'),
        headers=headers,
        json=validate,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

