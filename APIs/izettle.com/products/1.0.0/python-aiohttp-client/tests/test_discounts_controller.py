# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.discount_request import DiscountRequest
from openapi_server.models.discount_response import DiscountResponse
from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

async def test_create_discount(client):
    """Test case for create_discount

    Create a discount
    """
    body = {"externalReference":"externalReference","amount":{"amount":0,"currencyId":"AED"},"percentage":8.008281904610115,"name":"name","description":"description","imageLookupKeys":["imageLookupKeys","imageLookupKeys"],"uuid":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/organizations/{organization_uuid}/discounts'.format(organization_uuid='organization_uuid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_discount(client):
    """Test case for delete_discount

    Delete a single discount 
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/organizations/{organization_uuid}/discounts/{discount_uuid}'.format(organization_uuid='organization_uuid_example', discount_uuid='discount_uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_all_discounts(client):
    """Test case for get_all_discounts

    Retrieve all discounts
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/organizations/{organization_uuid}/discounts'.format(organization_uuid='organization_uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_discount(client):
    """Test case for get_discount

    Retrieve a single discount
    """
    headers = { 
        'Accept': 'application/json',
        'if_none_match': 'if_none_match_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/organizations/{organization_uuid}/discounts/{discount_uuid}'.format(organization_uuid='organization_uuid_example', discount_uuid='discount_uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_discount(client):
    """Test case for update_discount

    Update a single discount
    """
    body = {"externalReference":"externalReference","amount":{"amount":0,"currencyId":"AED"},"percentage":8.008281904610115,"name":"name","description":"description","imageLookupKeys":["imageLookupKeys","imageLookupKeys"],"uuid":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'if_match': 'if_match_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/organizations/{organization_uuid}/discounts/{discount_uuid}'.format(organization_uuid='organization_uuid_example', discount_uuid='discount_uuid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

