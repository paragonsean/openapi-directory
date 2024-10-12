# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.netlicensing import Netlicensing


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_create_licensee(client):
    """Test case for create_licensee

    Create Licensee
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'active': True,
        'marked_for_transfer': True,
        'name': 'name_example',
        'number': 'number_example',
        'product_number': 'product_number_example'
        }
    response = await client.request(
        method='POST',
        path='/core/v2/rest/licensee',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_licensee(client):
    """Test case for delete_licensee

    Delete Licensee
    """
    params = [('forceCascade', True)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/core/v2/rest/licensee/{licensee_number}'.format(licensee_number='licensee_number_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_licensee(client):
    """Test case for get_licensee

    Get Licensee
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/core/v2/rest/licensee/{licensee_number}'.format(licensee_number='licensee_number_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_licensees(client):
    """Test case for list_licensees

    List Licensees
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/core/v2/rest/licensee',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_transfer_licenses(client):
    """Test case for transfer_licenses

    Transfer Licenses
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'source_licensee_number': 'source_licensee_number_example'
        }
    response = await client.request(
        method='POST',
        path='/core/v2/rest/licensee/{licensee_number}/transfer'.format(licensee_number='licensee_number_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_update_licensee(client):
    """Test case for update_licensee

    Update Licensee
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'active': True,
        'marked_for_transfer': True,
        'name': 'name_example',
        'number': 'number_example'
        }
    response = await client.request(
        method='POST',
        path='/core/v2/rest/licensee/{licensee_number}'.format(licensee_number='licensee_number_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_validate_licensee(client):
    """Test case for validate_licensee

    Validate Licensee
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'action': 'action_example',
        'licensee_name': 'licensee_name_example',
        'node_secret': 'node_secret_example',
        'product_module_number': 'product_module_number_example',
        'product_number': 'product_number_example',
        'session_id': 'session_id_example'
        }
    response = await client.request(
        method='POST',
        path='/core/v2/rest/licensee/{licensee_number}/validate'.format(licensee_number='licensee_number_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

