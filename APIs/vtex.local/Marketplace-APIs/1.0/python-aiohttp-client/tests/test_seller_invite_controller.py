# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.accept_seller_lead_request import AcceptSellerLeadRequest
from openapi_server.models.create_seller_lead_request import CreateSellerLeadRequest
from openapi_server.models.resend_seller_lead_request_request import ResendSellerLeadRequestRequest


pytestmark = pytest.mark.asyncio

async def test_accept_seller_lead(client):
    """Test case for accept_seller_lead

    Accept Seller Lead
    """
    body = {"accountId":"5fb38ace-d95e-45ad-970d-ee97cce9fbcd","accountable":{"email":"email@email.com","name":"Jane Smith","phone":"1234567890"},"address":{"city":"Rio de Janeiro","complement":"Appartment 1234","neighborhood":"VTEX quarter","number":"25","postalcode":"12345678","state":"RJ","street":"VTEX street"},"affiliateId":"MKP","document":"12345671000","email":"seller@email.com","hasAcceptedLegalTerms":True,"salesChannel":"1","sellerAccountName":"seller123","sellerEmail":"selleremail@email.com","sellerName":"Seller Name","sellerType":1}
    params = [('accountName', 'apiexamples'),
                    ('environment', 'vtexcommercestable')]
    headers = { 
        'Content-Type': 'application/json',
        'accept': 'application/json',
        'content_type': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/seller-register/pvt/seller-leads/{seller_lead_id}'.format(seller_lead_id='seller_lead_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_seller_from_seller_lead(client):
    """Test case for create_seller_from_seller_lead

    Create Seller From Lead
    """
    params = [('accountName', 'apiexamples'),
                    ('environment', 'vtexcommercestable'),
                    ('isActive', False)]
    headers = { 
        'accept': 'application/json',
        'content_type': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/seller-register/pvt/seller-leads/{seller_lead_id}/seller'.format(seller_lead_id='seller_lead_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_seller_lead(client):
    """Test case for create_seller_lead

    Invite Seller Lead
    """
    body = {"accountId":"5fb38ace-d95e-45ad-970d-ee97cce9fbcd","accountable":{"phone":"1234567890","name":"Jane Smith","email":"email@email.com"},"address":{"number":"25","city":"Rio de Janeiro","postalcode":"12345678","street":"VTEX street","neighborhood":"VTEX quarter","state":"RJ","complement":"Appartment 1234"},"document":"12345671000","sellerAccountName":"seller123","sellerName":"Seller Name","hasAcceptedLegalTerms":True,"salesChannel":"1","sellerType":0,"sellerEmail":"selleremail@email.com","email":"email@email.com"}
    params = [('accountName', 'apiexample'),
                    ('environment', 'vtexcommercestable')]
    headers = { 
        'Content-Type': 'application/json',
        'accept': 'application/json',
        'content_type': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/seller-register/pvt/seller-leads',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_seller_leads(client):
    """Test case for list_seller_leads

    List Seller Leads
    """
    params = [('accountName', 'apiexamples'),
                    ('environment', 'vtexcommercestable'),
                    ('offset', 0),
                    ('limit', 15),
                    ('isConnected', ''),
                    ('search', 'user email'),
                    ('status', 'invited'),
                    ('orderBy', 'order_by_example')]
    headers = { 
        'accept': 'application/json',
        'content_type': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/seller-register/pvt/seller-leads',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_remove_seller_lead(client):
    """Test case for remove_seller_lead

    Delete Seller Lead
    """
    params = [('accountName', 'apiexamples'),
                    ('environment', 'vtexcommercestable')]
    headers = { 
        'accept': 'application/json',
        'content_type': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/seller-register/pvt/seller-leads/{seller_lead_id}'.format(seller_lead_id='seller_lead_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_resend_seller_lead_request(client):
    """Test case for resend_seller_lead_request

    Resend Seller Lead Invite
    """
    body = {"status":"accepted"}
    params = [('accountName', 'apiexamples'),
                    ('environment', 'vtexcommercestable')]
    headers = { 
        'Content-Type': 'application/json',
        'accept': 'application/json',
        'content_type': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/seller-register/pvt/seller-leads/{seller_lead_id}/status'.format(seller_lead_id='seller_lead_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_retrieve_seller_lead(client):
    """Test case for retrieve_seller_lead

    Get Seller Lead's Data by Id
    """
    params = [('accountName', 'apiexamples'),
                    ('environment', 'vtexcommercestable')]
    headers = { 
        'accept': 'application/json',
        'content_type': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/seller-register/pvt/seller-leads/{seller_lead_id}'.format(seller_lead_id='seller_lead_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

