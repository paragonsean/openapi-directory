# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.billbee_interfaces_billbee_api_model_customer_address_api_model import BillbeeInterfacesBillbeeAPIModelCustomerAddressApiModel
from openapi_server.models.rechnungsdruck_web_app_controllers_api_api_paged_result_system_collections_generic_list_billbee_interfaces_billbee_api_model_customer_address_api_model import RechnungsdruckWebAppControllersApiApiPagedResultSystemCollectionsGenericListBillbeeInterfacesBillbeeAPIModelCustomerAddressApiModel
from openapi_server.models.rechnungsdruck_web_app_controllers_api_api_result_billbee_interfaces_billbee_api_model_customer_address_api_model import RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelCustomerAddressApiModel


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_customer_addresses_create(client):
    """Test case for customer_addresses_create

    Creates a new customer address
    """
    body = openapi_server.BillbeeInterfacesBillbeeAPIModelCustomerAddressApiModel()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/customer-addresses',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_customer_addresses_get_all(client):
    """Test case for customer_addresses_get_all

    Get a list of all customer addresses
    """
    params = [('page', 56),
                    ('pageSize', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/customer-addresses',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_customer_addresses_get_one(client):
    """Test case for customer_addresses_get_one

    Queries a single customer address by id
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/customer-addresses/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_customer_addresses_update(client):
    """Test case for customer_addresses_update

    Updates a customer address by id
    """
    body = openapi_server.BillbeeInterfacesBillbeeAPIModelCustomerAddressApiModel()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/customer-addresses/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

