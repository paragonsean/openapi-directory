# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.category_jo import CategoryJO
from openapi_server.models.error_jo import ErrorJO


pytestmark = pytest.mark.asyncio

async def test_get_category(client):
    """Test case for get_category

    Get a Category by UID
    """
    params = [('expand', 'expand_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/flinkster-api-ng/v1/providernetworks/{providernetwork_uid}/categories/{category_uid}'.format(providernetwork_uid='providernetwork_uid_example', category_uid='category_uid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_categories(client):
    """Test case for list_categories

    Lists all categories
    """
    params = [('expand', 'expand_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/flinkster-api-ng/v1/providernetworks/{providernetwork_uid}/categories'.format(providernetwork_uid='providernetwork_uid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

