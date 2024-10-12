# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.controller import Controller
from openapi_server.models.controller_connection_details_list import ControllerConnectionDetailsList
from openapi_server.models.controller_list import ControllerList
from openapi_server.models.controller_update_parameters import ControllerUpdateParameters
from openapi_server.models.dev_spaces_error_response import DevSpacesErrorResponse
from openapi_server.models.list_connection_details_parameters import ListConnectionDetailsParameters


pytestmark = pytest.mark.asyncio

async def test_controllers_create(client):
    """Test case for controllers_create

    Creates an Azure Dev Spaces Controller.
    """
    controller = {"sku":{"tier":"Standard","name":"S1"},"properties":{"dataPlaneFqdn":"dataPlaneFqdn","targetContainerHostCredentialsBase64":"targetContainerHostCredentialsBase64","hostSuffix":"hostSuffix","targetContainerHostResourceId":"targetContainerHostResourceId","provisioningState":"Succeeded"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DevSpaces/controllers/{name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', name='name_example'),
        headers=headers,
        json=controller,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_controllers_delete(client):
    """Test case for controllers_delete

    Deletes an Azure Dev Spaces Controller.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DevSpaces/controllers/{name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_controllers_get(client):
    """Test case for controllers_get

    Gets an Azure Dev Spaces Controller.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DevSpaces/controllers/{name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_controllers_list(client):
    """Test case for controllers_list

    Lists the Azure Dev Spaces Controllers in a subscription.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.DevSpaces/controllers'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_controllers_list_by_resource_group(client):
    """Test case for controllers_list_by_resource_group

    Lists the Azure Dev Spaces Controllers in a resource group.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DevSpaces/controllers'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_controllers_list_connection_details(client):
    """Test case for controllers_list_connection_details

    Lists connection details for an Azure Dev Spaces Controller.
    """
    list_connection_details_parameters = {"targetContainerHostResourceId":"targetContainerHostResourceId"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DevSpaces/controllers/{name}/listConnectionDetails'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', name='name_example'),
        headers=headers,
        json=list_connection_details_parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_controllers_update(client):
    """Test case for controllers_update

    Updates an Azure Dev Spaces Controller.
    """
    controller_update_parameters = {"properties":{"targetContainerHostCredentialsBase64":"targetContainerHostCredentialsBase64"},"tags":"{}"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DevSpaces/controllers/{name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', name='name_example'),
        headers=headers,
        json=controller_update_parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

