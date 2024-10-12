# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.get_callback_url_parameters import GetCallbackUrlParameters
from openapi_server.models.integration_account_schema import IntegrationAccountSchema
from openapi_server.models.integration_account_schema_list_result import IntegrationAccountSchemaListResult
from openapi_server.models.workflow_trigger_callback_url import WorkflowTriggerCallbackUrl


pytestmark = pytest.mark.asyncio

async def test_schemas_create_or_update(client):
    """Test case for schemas_create_or_update

    
    """
    _schema = {"properties":{"fileName":"fileName","metadata":"{}","targetNamespace":"targetNamespace","schemaType":"NotSpecified","contentLink":{"metadata":"{}","contentSize":0,"contentVersion":"contentVersion","uri":"uri","contentHash":{"value":"value","algorithm":"algorithm"}},"createdTime":"2000-01-23T04:56:07.000+00:00","changedTime":"2000-01-23T04:56:07.000+00:00","documentName":"documentName","contentType":"contentType","content":"{}"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Logic/integrationAccounts/{integration_account_name}/schemas/{schema_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', integration_account_name='integration_account_name_example', schema_name='schema_name_example'),
        headers=headers,
        json=_schema,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_schemas_delete(client):
    """Test case for schemas_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Logic/integrationAccounts/{integration_account_name}/schemas/{schema_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', integration_account_name='integration_account_name_example', schema_name='schema_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_schemas_get(client):
    """Test case for schemas_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Logic/integrationAccounts/{integration_account_name}/schemas/{schema_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', integration_account_name='integration_account_name_example', schema_name='schema_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_schemas_list_by_integration_accounts(client):
    """Test case for schemas_list_by_integration_accounts

    
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
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Logic/integrationAccounts/{integration_account_name}/schemas'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', integration_account_name='integration_account_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_schemas_list_content_callback_url(client):
    """Test case for schemas_list_content_callback_url

    
    """
    list_content_callback_url = {"notAfter":"2000-01-23T04:56:07.000+00:00","keyType":"NotSpecified"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Logic/integrationAccounts/{integration_account_name}/schemas/{schema_name}/listContentCallbackUrl'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', integration_account_name='integration_account_name_example', schema_name='schema_name_example'),
        headers=headers,
        json=list_content_callback_url,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

