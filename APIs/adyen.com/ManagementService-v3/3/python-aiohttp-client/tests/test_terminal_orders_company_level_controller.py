# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.billing_entities_response import BillingEntitiesResponse
from openapi_server.models.rest_service_error import RestServiceError
from openapi_server.models.shipping_location import ShippingLocation
from openapi_server.models.shipping_locations_response import ShippingLocationsResponse
from openapi_server.models.terminal_models_response import TerminalModelsResponse
from openapi_server.models.terminal_order import TerminalOrder
from openapi_server.models.terminal_order_request import TerminalOrderRequest
from openapi_server.models.terminal_orders_response import TerminalOrdersResponse
from openapi_server.models.terminal_products_response import TerminalProductsResponse


pytestmark = pytest.mark.asyncio

async def test_get_companies_company_id_billing_entities(client):
    """Test case for get_companies_company_id_billing_entities

    Get a list of billing entities
    """
    params = [('name', 'name_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v3/companies/{company_id}/billingEntities'.format(company_id='company_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_companies_company_id_shipping_locations(client):
    """Test case for get_companies_company_id_shipping_locations

    Get a list of shipping locations
    """
    params = [('name', 'name_example'),
                    ('offset', 56),
                    ('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v3/companies/{company_id}/shippingLocations'.format(company_id='company_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_companies_company_id_terminal_models(client):
    """Test case for get_companies_company_id_terminal_models

    Get a list of terminal models
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v3/companies/{company_id}/terminalModels'.format(company_id='company_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_companies_company_id_terminal_orders(client):
    """Test case for get_companies_company_id_terminal_orders

    Get a list of orders
    """
    params = [('customerOrderReference', 'customer_order_reference_example'),
                    ('status', 'status_example'),
                    ('offset', 56),
                    ('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v3/companies/{company_id}/terminalOrders'.format(company_id='company_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_companies_company_id_terminal_orders_order_id(client):
    """Test case for get_companies_company_id_terminal_orders_order_id

    Get an order
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v3/companies/{company_id}/terminalOrders/{order_id}'.format(company_id='company_id_example', order_id='order_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_companies_company_id_terminal_products(client):
    """Test case for get_companies_company_id_terminal_products

    Get a list of terminal products
    """
    params = [('country', 'country_example'),
                    ('terminalModelId', 'terminal_model_id_example'),
                    ('offset', 56),
                    ('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v3/companies/{company_id}/terminalProducts'.format(company_id='company_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_patch_companies_company_id_terminal_orders_order_id(client):
    """Test case for patch_companies_company_id_terminal_orders_order_id

    Update an order
    """
    body = {"orderType":"orderType","customerOrderReference":"customerOrderReference","taxId":"taxId","shippingLocationId":"shippingLocationId","billingEntityId":"billingEntityId","items":[{"quantity":6,"installments":0,"name":"name","id":"id"},{"quantity":6,"installments":0,"name":"name","id":"id"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/v3/companies/{company_id}/terminalOrders/{order_id}'.format(company_id='company_id_example', order_id='order_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_companies_company_id_shipping_locations(client):
    """Test case for post_companies_company_id_shipping_locations

    Create a shipping location
    """
    body = {"address":{"country":"country","stateOrProvince":"stateOrProvince","city":"city","streetAddress":"streetAddress","companyName":"companyName","postalCode":"postalCode","streetAddress2":"streetAddress2"},"contact":{"firstName":"firstName","lastName":"lastName","phoneNumber":"phoneNumber","infix":"infix","email":"email"},"name":"name","id":"id"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v3/companies/{company_id}/shippingLocations'.format(company_id='company_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_companies_company_id_terminal_orders(client):
    """Test case for post_companies_company_id_terminal_orders

    Create an order
    """
    body = {"orderType":"orderType","customerOrderReference":"customerOrderReference","taxId":"taxId","shippingLocationId":"shippingLocationId","billingEntityId":"billingEntityId","items":[{"quantity":6,"installments":0,"name":"name","id":"id"},{"quantity":6,"installments":0,"name":"name","id":"id"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v3/companies/{company_id}/terminalOrders'.format(company_id='company_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_companies_company_id_terminal_orders_order_id_cancel(client):
    """Test case for post_companies_company_id_terminal_orders_order_id_cancel

    Cancel an order
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v3/companies/{company_id}/terminalOrders/{order_id}/cancel'.format(company_id='company_id_example', order_id='order_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

