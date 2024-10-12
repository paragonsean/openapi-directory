# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.account_type_model import AccountTypeModel
from openapi_server.models.account_types_model import AccountTypesModel


pytestmark = pytest.mark.asyncio

async def test_account_types_get_by_country(client):
    """Test case for account_types_get_by_country

    
    """
    params = [('country', 'country_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/factfinder/api/AccountTypes',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_account_types_get_by_id(client):
    """Test case for account_types_get_by_id

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/factfinder/api/AccountTypes/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

