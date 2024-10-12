# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.expense_type_model import ExpenseTypeModel
from openapi_server.models.expense_types_model import ExpenseTypesModel


pytestmark = pytest.mark.asyncio

async def test_expense_types_get_by_country(client):
    """Test case for expense_types_get_by_country

    
    """
    params = [('country', 'country_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/factfinder/api/ExpenseTypes',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_expense_types_get_by_id(client):
    """Test case for expense_types_get_by_id

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/factfinder/api/ExpenseTypes/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

