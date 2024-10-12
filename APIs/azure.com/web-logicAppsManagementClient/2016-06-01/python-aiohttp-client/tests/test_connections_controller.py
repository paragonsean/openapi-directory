# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_connection_definition import ApiConnectionDefinition
from openapi_server.models.api_connection_definition_collection import ApiConnectionDefinitionCollection
from openapi_server.models.confirm_consent_code_definition import ConfirmConsentCodeDefinition
from openapi_server.models.consent_link_collection import ConsentLinkCollection
from openapi_server.models.list_consent_links_definition import ListConsentLinksDefinition


pytestmark = pytest.mark.asyncio

async def test_connections_confirm_consent_code(client):
    """Test case for connections_confirm_consent_code

    Confirms the consent code for a connection
    """
    confirm_consent_code = {"code":"code","tenantId":"tenantId","objectId":"objectId"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/connections/{connection_name}/confirmConsentCode'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', connection_name='connection_name_example'),
        headers=headers,
        json=confirm_consent_code,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_connections_create_or_update(client):
    """Test case for connections_create_or_update

    Replace an existing connection
    """
    connection = {"properties":"{}"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/connections/{connection_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', connection_name='connection_name_example'),
        headers=headers,
        json=connection,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_connections_delete(client):
    """Test case for connections_delete

    Delete an existing connection
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/connections/{connection_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', connection_name='connection_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_connections_get(client):
    """Test case for connections_get

    Get a connection
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/connections/{connection_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', connection_name='connection_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_connections_list(client):
    """Test case for connections_list

    Get all connections
    """
    params = [('$top', 56),
                    ('$filter', 'filter_example'),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/connections'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_connections_list_consent_links(client):
    """Test case for connections_list_consent_links

    Lists consent links for a connection
    """
    list_consent_link = {"parameters":[{"redirectUrl":"redirectUrl","tenantId":"tenantId","parameterName":"parameterName","objectId":"objectId"},{"redirectUrl":"redirectUrl","tenantId":"tenantId","parameterName":"parameterName","objectId":"objectId"}]}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/connections/{connection_name}/listConsentLinks'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', connection_name='connection_name_example'),
        headers=headers,
        json=list_consent_link,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_connections_update(client):
    """Test case for connections_update

    Update an existing connection
    """
    connection = {"properties":"{}"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/connections/{connection_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', connection_name='connection_name_example'),
        headers=headers,
        json=connection,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

