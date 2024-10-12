# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_organization_action_batch201_response import CreateOrganizationActionBatch201Response
from openapi_server.models.create_organization_action_batch_request import CreateOrganizationActionBatchRequest
from openapi_server.models.update_organization_action_batch_request import UpdateOrganizationActionBatchRequest


pytestmark = pytest.mark.asyncio

async def test_create_organization_action_batch_1(client):
    """Test case for create_organization_action_batch_1

    Create an action batch
    """
    body = openapi_server.CreateOrganizationActionBatchRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/organizations/{organization_id}/actionBatches'.format(organization_id='organization_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_organization_action_batch_1(client):
    """Test case for delete_organization_action_batch_1

    Delete an action batch
    """
    headers = { 
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/organizations/{organization_id}/actionBatches/{action_batch_id}'.format(organization_id='organization_id_example', action_batch_id='action_batch_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organization_action_batch_1(client):
    """Test case for get_organization_action_batch_1

    Return an action batch
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/organizations/{organization_id}/actionBatches/{action_batch_id}'.format(organization_id='organization_id_example', action_batch_id='action_batch_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organization_action_batches_1(client):
    """Test case for get_organization_action_batches_1

    Return the list of action batches in the organization
    """
    params = [('status', 'status_example')]
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/organizations/{organization_id}/actionBatches'.format(organization_id='organization_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_organization_action_batch_1(client):
    """Test case for update_organization_action_batch_1

    Update an action batch
    """
    body = openapi_server.UpdateOrganizationActionBatchRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/organizations/{organization_id}/actionBatches/{action_batch_id}'.format(organization_id='organization_id_example', action_batch_id='action_batch_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

