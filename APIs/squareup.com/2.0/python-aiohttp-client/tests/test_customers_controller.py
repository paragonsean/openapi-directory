# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.add_group_to_customer_response import AddGroupToCustomerResponse
from openapi_server.models.create_customer_card_request import CreateCustomerCardRequest
from openapi_server.models.create_customer_card_response import CreateCustomerCardResponse
from openapi_server.models.create_customer_request import CreateCustomerRequest
from openapi_server.models.create_customer_response import CreateCustomerResponse
from openapi_server.models.delete_customer_card_response import DeleteCustomerCardResponse
from openapi_server.models.delete_customer_response import DeleteCustomerResponse
from openapi_server.models.list_customers_response import ListCustomersResponse
from openapi_server.models.remove_group_from_customer_response import RemoveGroupFromCustomerResponse
from openapi_server.models.retrieve_customer_response import RetrieveCustomerResponse
from openapi_server.models.search_customers_request import SearchCustomersRequest
from openapi_server.models.search_customers_response import SearchCustomersResponse
from openapi_server.models.update_customer_request import UpdateCustomerRequest
from openapi_server.models.update_customer_response import UpdateCustomerResponse


pytestmark = pytest.mark.asyncio

async def test_add_group_to_customer(client):
    """Test case for add_group_to_customer

    AddGroupToCustomer
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v2/customers/{customer_id}/groups/{group_id}'.format(customer_id='customer_id_example', group_id='group_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_customer(client):
    """Test case for create_customer

    CreateCustomer
    """
    body = {"request_body":{"address":{"address_line_1":"500 Electric Ave","address_line_2":"Suite 600","administrative_district_level_1":"NY","country":"US","locality":"New York","postal_code":"10003"},"email_address":"Amelia.Earhart@example.com","family_name":"Earhart","given_name":"Amelia","note":"a customer","phone_number":"1-212-555-4240","reference_id":"YOUR_REFERENCE_ID"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/customers',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_customer_card(client):
    """Test case for create_customer_card

    CreateCustomerCard
    """
    body = {"request_body":{"billing_address":{"address_line_1":"500 Electric Ave","address_line_2":"Suite 600","administrative_district_level_1":"NY","country":"US","locality":"New York","postal_code":"10003"},"card_nonce":"YOUR_CARD_NONCE","cardholder_name":"Amelia Earhart"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/customers/{customer_id}/cards'.format(customer_id='customer_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_customer(client):
    """Test case for delete_customer

    DeleteCustomer
    """
    params = [('version', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v2/customers/{customer_id}'.format(customer_id='customer_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_customer_card(client):
    """Test case for delete_customer_card

    DeleteCustomerCard
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v2/customers/{customer_id}/cards/{card_id}'.format(customer_id='customer_id_example', card_id='card_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_customers(client):
    """Test case for list_customers

    ListCustomers
    """
    params = [('cursor', 'cursor_example'),
                    ('limit', 56),
                    ('sort_field', 'sort_field_example'),
                    ('sort_order', 'sort_order_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/customers',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_remove_group_from_customer(client):
    """Test case for remove_group_from_customer

    RemoveGroupFromCustomer
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v2/customers/{customer_id}/groups/{group_id}'.format(customer_id='customer_id_example', group_id='group_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_retrieve_customer(client):
    """Test case for retrieve_customer

    RetrieveCustomer
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/customers/{customer_id}'.format(customer_id='customer_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_search_customers(client):
    """Test case for search_customers

    SearchCustomers
    """
    body = {"request_body":{"limit":2,"query":{"filter":{"created_at":{"end_at":"2018-02-01T00:00:00-00:00","start_at":"2018-01-01T00:00:00-00:00"},"creation_source":{"rule":"INCLUDE","values":["THIRD_PARTY"]},"email_address":{"fuzzy":"example.com"},"group_ids":{"all":["545AXB44B4XXWMVQ4W8SBT3HHF"]}},"sort":{"field":"CREATED_AT","order":"ASC"}}}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/customers/search',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_customer(client):
    """Test case for update_customer

    UpdateCustomer
    """
    body = {"request_body":{"email_address":"New.Amelia.Earhart@example.com","note":"updated customer note","phone_number":"","version":2}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v2/customers/{customer_id}'.format(customer_id='customer_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

