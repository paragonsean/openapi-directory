# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.bad_request_response import BadRequestResponse
from openapi_server.models.get_integrations_list200_response import GetIntegrationsList200Response
from openapi_server.models.integrations_billys_authenticate_post200_response import IntegrationsBillysAuthenticatePost200Response
from openapi_server.models.integrations_products_sync_get200_response import IntegrationsProductsSyncGet200Response


pytestmark = pytest.mark.asyncio

async def test_get_integrations_contacts_sync(client):
    """Test case for get_integrations_contacts_sync

    Force Synchronization with ERP systems
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/integrations/contactsSync',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_integrations_list(client):
    """Test case for get_integrations_list

    Get integrations list
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/integrations',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_integrations_view(client):
    """Test case for get_integrations_view

    View integration details
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/integrations/{integration_id}'.format(integration_id='integration_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_integrations_billys_authenticate_post(client):
    """Test case for integrations_billys_authenticate_post

    Authenticate to Billys
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/integrations/billysAuthenticate',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_integrations_products_sync_get(client):
    """Test case for integrations_products_sync_get

    Sync products from erp integration
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/integrations/productsSync',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

