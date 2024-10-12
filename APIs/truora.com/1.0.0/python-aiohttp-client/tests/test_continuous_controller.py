# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.continuous_check import ContinuousCheck
from openapi_server.models.error import Error
from openapi_server.models.get_contiuous_check_history_output import GetContiuousCheckHistoryOutput
from openapi_server.models.list_continuous_checks_output import ListContinuousChecksOutput


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_create_continuous_check(client):
    """Test case for create_continuous_check

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'api-key': 'special-key',
    }
    data = {
        'check_id': 'check_id_example',
        'frequency': 'frequency_example',
        'status': 'status_example'
        }
    response = await client.request(
        method='POST',
        path='/v1/continuous-checks',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_continuous_check(client):
    """Test case for get_continuous_check

    
    """
    headers = { 
        'Accept': 'application/json',
        'api-key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/continuous-checks/{continuous_check_id}'.format(continuous_check_id=3.4),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_continuous_checks(client):
    """Test case for list_continuous_checks

    
    """
    headers = { 
        'Accept': 'application/json',
        'api-key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/continuous-checks',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_update_continuous_check(client):
    """Test case for update_continuous_check

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'api-key': 'special-key',
    }
    data = {
        'frequency': 'frequency_example',
        'status': 'status_example'
        }
    response = await client.request(
        method='PUT',
        path='/v1/continuous-checks/{continuous_check_id}'.format(continuous_check_id=3.4),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_v1_continuous_checks_continuous_check_id_history_get(client):
    """Test case for v1_continuous_checks_continuous_check_id_history_get

    
    """
    headers = { 
        'Accept': 'application/json',
        'api-key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/continuous-checks/{continuous_check_id}/history'.format(continuous_check_id='continuous_check_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

