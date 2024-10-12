# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.company_contact import CompanyContact
from openapi_server.models.contact_list import ContactList
from openapi_server.models.new_company_contact import NewCompanyContact


pytestmark = pytest.mark.asyncio

async def test_contact_get(client):
    """Test case for contact_get

    Gets list of Contacts
    """
    params = [('UpdatedAfter', '2013-10-20T19:20:30+01:00'),
                    ('pageSize', 56),
                    ('pageNumber', 56),
                    ('Sort', 'sort_example'),
                    ('CompanyIDFK', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/Contact',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_contact_get_by_id(client):
    """Test case for contact_get_by_id

    Gets Contact by Contact ID
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/Contact/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_contact_post(client):
    """Test case for contact_post

    Create a Contact
    """
    model = {"CompanyBillingAddressCity":"CompanyBillingAddressCity","PositionTitle":"PositionTitle","CompanyBillingAddressCountryCode":"CompanyBillingAddressCountryCode","Lastname":"Lastname","UpdateExisting":True,"CompanyIDFK":0,"CompanyBillingAddress":"CompanyBillingAddress","CompanyBillingAddressLine":"CompanyBillingAddressLine","Mobile":"Mobile","CurrencyCode":"CurrencyCode","Firstname":"Firstname","CompanyName":"CompanyName","CompanyBillingAddressState":"CompanyBillingAddressState","Phone":"Phone","CompanyBillingAddressPostCode":"CompanyBillingAddressPostCode","ContactEmail":"ContactEmail"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/Contact',
        headers=headers,
        json=model,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

