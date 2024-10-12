# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.address_autocomplete_post_request import AddressAutocompletePostRequest
from openapi_server.models.contact_enrich_post_request import ContactEnrichPostRequest
from openapi_server.models.email_enrich_post_request import EmailEnrichPostRequest
from openapi_server.models.phone_enrich_post_request import PhoneEnrichPostRequest


pytestmark = pytest.mark.asyncio

async def test_address_autocomplete_post(client):
    """Test case for address_autocomplete_post

    Search
    """
    body = openapi_server.AddressAutocompletePostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'galaxy_ap_name': 'Key',
        'galaxy_ap_password': 'Secret',
        'galaxy_search_type': 'DevAPIAddressAutoComplete',
    }
    response = await client.request(
        method='POST',
        path='/address/autocomplete',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_contact_enrich_post(client):
    """Test case for contact_enrich_post

    Search
    """
    body = openapi_server.ContactEnrichPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'galaxy_ap_name': 'Key',
        'galaxy_ap_password': 'Secret',
        'galaxy_search_type': 'DevAPIContactEnrich',
    }
    response = await client.request(
        method='POST',
        path='/contact/enrich',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_email_enrich_post(client):
    """Test case for email_enrich_post

    Search
    """
    body = openapi_server.EmailEnrichPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'galaxy_ap_name': 'Key',
        'galaxy_ap_password': 'Secret',
        'galaxy_search_type': 'DevAPIEmailID',
    }
    response = await client.request(
        method='POST',
        path='/email/enrich',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_phone_enrich_post(client):
    """Test case for phone_enrich_post

    Search
    """
    body = openapi_server.PhoneEnrichPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'galaxy_ap_name': 'Key',
        'galaxy_ap_password': 'Secret',
        'galaxy_search_type': 'DevAPICallerID',
    }
    response = await client.request(
        method='POST',
        path='/phone/enrich',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_search(client):
    """Test case for search

    Search
    """
    body = openapi_server.ContactEnrichPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'galaxy_ap_name': 'Key',
        'galaxy_ap_password': 'Secret',
        'galaxy_search_type': 'DevAPIIDVerification',
    }
    response = await client.request(
        method='POST',
        path='/identity/verify_id',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

