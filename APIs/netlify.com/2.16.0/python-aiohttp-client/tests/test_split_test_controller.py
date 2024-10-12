# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.split_test import SplitTest
from openapi_server.models.split_test_setup import SplitTestSetup


pytestmark = pytest.mark.asyncio

async def test_create_split_test(client):
    """Test case for create_split_test

    
    """
    branch_tests = openapi_server.SplitTestSetup()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/sites/{site_id}/traffic_splits'.format(site_id='site_id_example'),
        headers=headers,
        json=branch_tests,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_disable_split_test(client):
    """Test case for disable_split_test

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/sites/{site_id}/traffic_splits/{split_test_id}/unpublish'.format(site_id='site_id_example', split_test_id='split_test_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_enable_split_test(client):
    """Test case for enable_split_test

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/sites/{site_id}/traffic_splits/{split_test_id}/publish'.format(site_id='site_id_example', split_test_id='split_test_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_split_test(client):
    """Test case for get_split_test

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/sites/{site_id}/traffic_splits/{split_test_id}'.format(site_id='site_id_example', split_test_id='split_test_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_split_tests(client):
    """Test case for get_split_tests

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/sites/{site_id}/traffic_splits'.format(site_id='site_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_split_test(client):
    """Test case for update_split_test

    
    """
    branch_tests = openapi_server.SplitTestSetup()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/sites/{site_id}/traffic_splits/{split_test_id}'.format(site_id='site_id_example', split_test_id='split_test_id_example'),
        headers=headers,
        json=branch_tests,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

