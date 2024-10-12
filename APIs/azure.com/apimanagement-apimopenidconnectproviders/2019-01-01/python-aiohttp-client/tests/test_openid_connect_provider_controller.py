# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.open_id_connect_provider_get200_response import OpenIdConnectProviderGet200Response
from openapi_server.models.open_id_connect_provider_list_by_service200_response import OpenIdConnectProviderListByService200Response
from openapi_server.models.open_id_connect_provider_list_by_service_default_response import OpenIdConnectProviderListByServiceDefaultResponse
from openapi_server.models.open_id_connect_provider_update_request import OpenIdConnectProviderUpdateRequest


pytestmark = pytest.mark.asyncio

async def test_open_id_connect_provider_create_or_update(client):
    """Test case for open_id_connect_provider_create_or_update

    
    """
    parameters = openapi_server.OpenIdConnectProviderGet200Response()
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'if_match': 'if_match_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ApiManagement/service/{service_name}/openidConnectProviders/{opid}'.format(resource_group_name='resource_group_name_example', service_name='service_name_example', opid='opid_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_open_id_connect_provider_delete(client):
    """Test case for open_id_connect_provider_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'if_match': 'if_match_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ApiManagement/service/{service_name}/openidConnectProviders/{opid}'.format(resource_group_name='resource_group_name_example', service_name='service_name_example', opid='opid_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_open_id_connect_provider_get(client):
    """Test case for open_id_connect_provider_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ApiManagement/service/{service_name}/openidConnectProviders/{opid}'.format(resource_group_name='resource_group_name_example', service_name='service_name_example', opid='opid_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_open_id_connect_provider_get_entity_tag(client):
    """Test case for open_id_connect_provider_get_entity_tag

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='HEAD',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ApiManagement/service/{service_name}/openidConnectProviders/{opid}'.format(resource_group_name='resource_group_name_example', service_name='service_name_example', opid='opid_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_open_id_connect_provider_list_by_service(client):
    """Test case for open_id_connect_provider_list_by_service

    
    """
    params = [('$filter', 'filter_example'),
                    ('$top', 56),
                    ('$skip', 56),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ApiManagement/service/{service_name}/openidConnectProviders'.format(resource_group_name='resource_group_name_example', service_name='service_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_open_id_connect_provider_update(client):
    """Test case for open_id_connect_provider_update

    
    """
    parameters = openapi_server.OpenIdConnectProviderUpdateRequest()
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'if_match': 'if_match_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ApiManagement/service/{service_name}/openidConnectProviders/{opid}'.format(resource_group_name='resource_group_name_example', service_name='service_name_example', opid='opid_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

