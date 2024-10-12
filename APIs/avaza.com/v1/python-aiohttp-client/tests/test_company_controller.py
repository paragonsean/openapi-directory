# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.company import Company
from openapi_server.models.company_dropdown_list import CompanyDropdownList
from openapi_server.models.company_list import CompanyList
from openapi_server.models.new_company import NewCompany
from openapi_server.models.update_company import UpdateCompany


pytestmark = pytest.mark.asyncio

async def test_company_get(client):
    """Test case for company_get

    Gets list of Companies
    """
    params = [('UpdatedAfter', '2013-10-20T19:20:30+01:00'),
                    ('pageSize', 56),
                    ('pageNumber', 56),
                    ('Sort', 'sort_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/Company',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_company_get_by_id(client):
    """Test case for company_get_by_id

    Gets Company by Company ID
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/Company/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_company_lookup(client):
    """Test case for company_lookup

    Gets minimal list of Companies.
    """
    params = [('pageSize', 56),
                    ('pageNumber', 56),
                    ('search', 'search_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/Company/Lookup',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_company_post(client):
    """Test case for company_post

    Create a Company
    """
    model = {"BillingAddressLine":"BillingAddressLine","website":"website","BillingAddressState":"BillingAddressState","Comments":"Comments","BillingCountryCode":"BillingCountryCode","BillingAddressPostCode":"BillingAddressPostCode","BillingAddressCity":"BillingAddressCity","BillingAddress":"BillingAddress","CurrencyCode":"CurrencyCode","CompanyName":"CompanyName","Phone":"Phone","TaxNumber":"TaxNumber","Fax":"Fax"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/Company',
        headers=headers,
        json=model,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_company_put(client):
    """Test case for company_put

    Update a Company record.
    """
    model = {"BillingAddressLine":"BillingAddressLine","website":"website","BillingAddressState":"BillingAddressState","FieldsToUpdate":["FieldsToUpdate","FieldsToUpdate"],"CompanyID":0,"Comments":"Comments","BillingCountryCode":"BillingCountryCode","BillingAddressPostCode":"BillingAddressPostCode","BillingAddressCity":"BillingAddressCity","BillingAddress":"BillingAddress","CompanyName":"CompanyName","Phone":"Phone","TaxNumber":"TaxNumber","Fax":"Fax"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/Company',
        headers=headers,
        json=model,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

