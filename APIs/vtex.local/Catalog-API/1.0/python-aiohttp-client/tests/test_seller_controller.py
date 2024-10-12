# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_seller200_response import CreateSeller200Response
from openapi_server.models.create_seller_request import CreateSellerRequest
from openapi_server.models.get_sellerby_id200_response import GetSellerbyId200Response
from openapi_server.models.get_sellersby_id200_response import GetSellersbyId200Response
from openapi_server.models.update_seller200_response import UpdateSeller200Response
from openapi_server.models.update_seller_request import UpdateSellerRequest


pytestmark = pytest.mark.asyncio

async def test_create_seller(client):
    """Test case for create_seller

    Create Seller
    """
    body = {"FulfillmentEndpoint":"http://pedrostore.vtexcommercestable.com.br/api/fulfillment?affiliateid=LDB&sc=1","Description":"Brief description","Email":"breno@breno.com","IsActive":True,"UrlLogo":"/myseller","FulfillmentSellerId":1,"SellerType":1,"Name":"My pedrostore","CSCIdentification":"pedrostore","MerchantName":"pedrostore","IsBetterScope":False,"TrustPolicy":"Default","SellerId":"pedrostore","Password":"passoword","ProductCommissionPercentage":0,"UserName":"myseller","CategoryCommissionPercentage":"[{\"CategoryId\":14,\"ProductCommission\":15.0,\"FreightCommission\":0.0}]","UseHybridPaymentOptions":False,"CatalogSystemEndpoint":"http://pedrostore.vtexcommercestable.com.br/api/catalog_system/","SecutityPrivacyPolicy":"Secutity privacy policy text","ArchiveId":1,"DeliveryPolicy":"Delivery policy text","CNPJ":"12035072751","ExchangeReturnPolicy":"Exchange return policy text","FreightCommissionPercentage":0}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/catalog_system/pvt/seller',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_sellerby_id(client):
    """Test case for get_sellerby_id

    Get Seller by ID
    """
    headers = { 
        'Accept': 'application/json',
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/catalog_system/pvt/seller/{seller_id}'.format(seller_id='pedrostore'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_sellersby_id(client):
    """Test case for get_sellersby_id

    Get Seller by ID
    """
    headers = { 
        'Accept': 'application/json',
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/catalog_system/pvt/sellers/{seller_id}'.format(seller_id='pedrostore'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_seller_list(client):
    """Test case for seller_list

    Get Seller List
    """
    params = [('sc', 1),
                    ('sellerType', 1),
                    ('isBetterScope', false)]
    headers = { 
        'Accept': 'application/json',
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/catalog_system/pvt/seller/list',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_seller(client):
    """Test case for update_seller

    Update Seller
    """
    body = {"FulfillmentEndpoint":"http://pedrostore.vtexcommercestable.com.br/api/fulfillment?affiliateid=LDB&sc=1","Description":"Brief description","Email":"breno@breno.com","IsActive":True,"UrlLogo":"/myseller","FulfillmentSellerId":1,"SellerType":1,"Name":"My pedrostore","CSCIdentification":"pedrostore","MerchantName":"pedrostore","IsBetterScope":False,"TrustPolicy":"Default","SellerId":"pedrostore","Password":"passoword","ProductCommissionPercentage":0,"UserName":"myseller","CategoryCommissionPercentage":"[{\"CategoryId\":14,\"ProductCommission\":15.0,\"FreightCommission\":0.0}]","UseHybridPaymentOptions":False,"CatalogSystemEndpoint":"http://pedrostore.vtexcommercestable.com.br/api/catalog_system/","SecutityPrivacyPolicy":"Secutity privacy policy text","ArchiveId":1,"DeliveryPolicy":"Delivery policy text","CNPJ":"12035072751","ExchangeReturnPolicy":"Exchange return policy text","FreightCommissionPercentage":0}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/catalog_system/pvt/seller',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

