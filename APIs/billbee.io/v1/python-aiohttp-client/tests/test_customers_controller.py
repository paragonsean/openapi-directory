# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.billbee_interfaces_billbee_api_model_create_customer_api_model import BillbeeInterfacesBillbeeAPIModelCreateCustomerApiModel
from openapi_server.models.billbee_interfaces_billbee_api_model_customer_address_api_model import BillbeeInterfacesBillbeeAPIModelCustomerAddressApiModel
from openapi_server.models.billbee_interfaces_billbee_api_model_customer_api_model import BillbeeInterfacesBillbeeAPIModelCustomerApiModel
from openapi_server.models.rechnungsdruck_web_app_controllers_api_api_paged_result_system_collections_generic_list_billbee_interfaces_billbee_api_model_customer_address_api_model import RechnungsdruckWebAppControllersApiApiPagedResultSystemCollectionsGenericListBillbeeInterfacesBillbeeAPIModelCustomerAddressApiModel
from openapi_server.models.rechnungsdruck_web_app_controllers_api_api_paged_result_system_collections_generic_list_billbee_interfaces_billbee_api_model_customer_api_model import RechnungsdruckWebAppControllersApiApiPagedResultSystemCollectionsGenericListBillbeeInterfacesBillbeeAPIModelCustomerApiModel
from openapi_server.models.rechnungsdruck_web_app_controllers_api_api_paged_result_system_collections_generic_list_rechnungsdruck_web_app_controllers_api_order import RechnungsdruckWebAppControllersApiApiPagedResultSystemCollectionsGenericListRechnungsdruckWebAppControllersApiOrder
from openapi_server.models.rechnungsdruck_web_app_controllers_api_api_result_billbee_interfaces_billbee_api_model_customer_address_api_model import RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelCustomerAddressApiModel
from openapi_server.models.rechnungsdruck_web_app_controllers_api_api_result_billbee_interfaces_billbee_api_model_customer_api_model import RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelCustomerApiModel
from openapi_server.models.rechnungsdruck_web_app_controllers_api_api_result_rechnungsdruck_web_app_controllers_api_search_controller_search_results_model import RechnungsdruckWebAppControllersApiApiResultRechnungsdruckWebAppControllersApiSearchControllerSearchResultsModel
from openapi_server.models.rechnungsdruck_web_app_controllers_api_search_controller_search_model import RechnungsdruckWebAppControllersApiSearchControllerSearchModel


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_customer_add_customer_address(client):
    """Test case for customer_add_customer_address

    Adds a new address to a customer
    """
    body = openapi_server.BillbeeInterfacesBillbeeAPIModelCustomerAddressApiModel()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/customers/{id}/addresses'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_customer_create(client):
    """Test case for customer_create

    Creates a new customer
    """
    body = openapi_server.BillbeeInterfacesBillbeeAPIModelCreateCustomerApiModel()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/customers',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_customer_get_all(client):
    """Test case for customer_get_all

    Get a list of all customers
    """
    params = [('page', 56),
                    ('pageSize', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/customers',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_customer_get_customer_address(client):
    """Test case for customer_get_customer_address

    Queries a single address from a customer
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/customers/addresses/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_customer_get_customer_addresses(client):
    """Test case for customer_get_customer_addresses

    Queries a list of addresses from a customer
    """
    params = [('page', 56),
                    ('pageSize', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/customers/{id}/addresses'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_customer_get_customer_orders(client):
    """Test case for customer_get_customer_orders

    Queries a list of orders from a customer
    """
    params = [('page', 56),
                    ('pageSize', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/customers/{id}/orders'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_customer_get_one(client):
    """Test case for customer_get_one

    Queries a single customer by id
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/customers/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_customer_patch_address(client):
    """Test case for customer_patch_address

    Updates one or more fields of an address
    """
    body = None
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v1/customers/addresses/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_customer_update(client):
    """Test case for customer_update

    Updates a customer by id
    """
    body = openapi_server.BillbeeInterfacesBillbeeAPIModelCustomerApiModel()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/customers/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_customer_update_address(client):
    """Test case for customer_update_address

    Updates all fields of an address
    """
    body = openapi_server.BillbeeInterfacesBillbeeAPIModelCustomerAddressApiModel()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/customers/addresses/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_search_search_0(client):
    """Test case for search_search_0

    Search for products, customers and orders.  Type can be \"order\", \"product\" and / or \"customer\"  Term can contains lucene query syntax
    """
    body = openapi_server.RechnungsdruckWebAppControllersApiSearchControllerSearchModel()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/search',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

