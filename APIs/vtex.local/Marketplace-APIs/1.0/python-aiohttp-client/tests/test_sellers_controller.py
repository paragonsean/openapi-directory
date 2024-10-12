# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.request_body_inner import RequestBodyInner
from openapi_server.models.upsert_seller_request import UpsertSellerRequest


pytestmark = pytest.mark.asyncio

async def test_get_list_sellers(client):
    """Test case for get_list_sellers

    List Sellers
    """
    params = [('accountName', 'apiexamples'),
                    ('environment', 'vtexcommercestable'),
                    ('from', 0),
                    ('to', 100),
                    ('keyword', 'keyword'),
                    ('integration', 'vtex-seller'),
                    ('group ', 'Group'),
                    ('isActive', False),
                    ('isBetterScope', False),
                    ('isVtex', False),
                    ('sc', '1'),
                    ('sellerType', 1),
                    ('sort', 'id:asc')]
    headers = { 
        'accept': 'application/json',
        'content_type': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/seller-register/pvt/sellers',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_retrieve_seller(client):
    """Test case for get_retrieve_seller

    Get Seller data by ID
    """
    params = [('accountName', 'apiexamples'),
                    ('environment', 'vtexcommercestable'),
                    ('sc', '1')]
    headers = { 
        'accept': 'application/json',
        'content_type': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/seller-register/pvt/sellers/{seller_id}'.format(seller_id='seller123'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_seller(client):
    """Test case for update_seller

    Update Seller by Seller ID
    """
    body = [openapi_server.RequestBodyInner()]
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
        method='PATCH',
        path='/seller-register/pvt/sellers/{seller_id}'.format(seller_id='seller123'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_upsert_seller_request(client):
    """Test case for upsert_seller_request

    Configure Seller Account
    """
    body = {"CSCIdentification":"","account":"parceiro01","allowHybridPayments":False,"availableSalesChannels":[{"id":1,"isSelected":True,"name":"Loja Principal"},{"id":2,"isSelected":True,"name":"Terceira"},{"id":3,"isSelected":True,"name":"Marketplaces"}],"catalogSystemEndpoint":"https://pedrostore.vtexcommercestable.com.br/api/catalog_system/","channel":"","deliveryPolicy":"","description":"","email":"vtexqa1@vtex.com.br","exchangeReturnPolicy":"","fulfillmentEndpoint":"http://fulfillment.vtexcommerce.com.br/api/fulfillment?an=parceiro01","fulfillmentSellerId":"","groups":[{"groups":[{"id":"8d845239bf1448dc8bc3ed3121837511","name":"long tail"},{"id":"b9bcd348ab9c4cec8285ff9485c27a72","name":"franchise accounts"}]}],"id":"testeMARCUS123","isActive":True,"isBetterScope":False,"isVtex":True,"name":"qamarketplace","password":"integrationHubPassword","salesChannel":"","score":0,"securityPrivacyPolicy":null,"sellerCommissionConfiguration":{"categoriesCommissionConfiguration":[],"freightCommissionPercentage":4,"productCommissionPercentage":3},"sellerType":1,"taxCode":"34444","trustPolicy":"AllowEmailSharing","user":"integrationHubUserName"}
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
        method='POST',
        path='/seller-register/pvt/sellers',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

