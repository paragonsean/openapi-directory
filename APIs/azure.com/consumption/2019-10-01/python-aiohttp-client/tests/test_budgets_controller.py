# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.budget import Budget
from openapi_server.models.budgets_list_result import BudgetsListResult
from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

async def test_budgets_create_or_update(client):
    """Test case for budgets_create_or_update

    
    """
    parameters = {"properties":{"amount":0.8008281904610115,"timeGrain":"Monthly","currentSpend":{"amount":6.027456183070403,"unit":"unit"},"timePeriod":{"endDate":"2000-01-23T04:56:07.000+00:00","startDate":"2000-01-23T04:56:07.000+00:00"},"filters":{"resourceGroups":["resourceGroups","resourceGroups","resourceGroups","resourceGroups","resourceGroups"],"resources":["resources","resources","resources","resources","resources"],"meters":["046b6c7f-0b8a-43b9-b35d-6489e6daee91","046b6c7f-0b8a-43b9-b35d-6489e6daee91","046b6c7f-0b8a-43b9-b35d-6489e6daee91","046b6c7f-0b8a-43b9-b35d-6489e6daee91","046b6c7f-0b8a-43b9-b35d-6489e6daee91"],"tags":{"key":["tags","tags"]}},"category":"Cost","notifications":{"key":{"contactGroups":["contactGroups","contactGroups","contactGroups","contactGroups","contactGroups"],"contactEmails":["contactEmails","contactEmails","contactEmails","contactEmails","contactEmails"],"threshold":1.4658129805029452,"enabled":True,"operator":"EqualTo","contactRoles":["contactRoles","contactRoles"]}}}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/{scope}/providers/Microsoft.Consumption/budgets/{budget_name}'.format(scope='scope_example', budget_name='budget_name_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_budgets_delete(client):
    """Test case for budgets_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/{scope}/providers/Microsoft.Consumption/budgets/{budget_name}'.format(scope='scope_example', budget_name='budget_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_budgets_get(client):
    """Test case for budgets_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{scope}/providers/Microsoft.Consumption/budgets/{budget_name}'.format(scope='scope_example', budget_name='budget_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_budgets_list(client):
    """Test case for budgets_list

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{scope}/providers/Microsoft.Consumption/budgets'.format(scope='scope_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

