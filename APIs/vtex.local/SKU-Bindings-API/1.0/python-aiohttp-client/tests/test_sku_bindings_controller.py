# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.bindtoanothersku_request import BindtoanotherskuRequest
from openapi_server.models.get_sk_useller200_response import GetSKUseller200Response
from openapi_server.models.getallby_seller_id200_response_inner import GetallbySellerId200ResponseInner
from openapi_server.models.getby_sku_id200_response_inner import GetbySkuId200ResponseInner
from openapi_server.models.getpagedadmin200_response import Getpagedadmin200Response
from openapi_server.models.insert_sku_binding_request import InsertSKUBindingRequest


pytestmark = pytest.mark.asyncio

async def test_activate_sku_binding(client):
    """Test case for activate_sku_binding

    Activate SKU Binding
    """
    headers = { 
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/sku-binding/pvt/skuseller/activate/{seller_id}/{sku_seller_id}'.format(seller_id='vtxkfj7352', sku_seller_id='71'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_bindtoanothersku(client):
    """Test case for bindtoanothersku

    Bind a seller's SKU to another SKU
    """
    body = openapi_server.BindtoanotherskuRequest()
    headers = { 
        'Content-Type': 'application/json',
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/sku-binding/pvt/skuseller/{seller_id}/{seller_sku_id}'.format(seller_id='101', seller_sku_id='1'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_change_notification(client):
    """Test case for change_notification

    Change Notification with SKU ID
    """
    headers = { 
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/sku-binding/pvt/skuseller/changenotification/{sku_id}'.format(sku_id='10'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_deactivate_sku_binding(client):
    """Test case for deactivate_sku_binding

    Deactivate SKU Binding
    """
    headers = { 
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/sku-binding/pvt/skuseller/inactivate/{seller_id}/{sku_seller_id}'.format(seller_id='vtxkfj7352', sku_seller_id='71'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_sk_usellerassociation(client):
    """Test case for delete_sk_usellerassociation

    Remove a seller's SKU Binding
    """
    headers = { 
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/sku-binding/pvt/skuseller/remove/{seller_id}/{seller_sku_id}'.format(seller_id='vtxkfj7352', seller_sku_id='71'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_sk_useller(client):
    """Test case for get_sk_useller

    Get details of a seller's SKU
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
        path='/sku-binding/pvt/skuseller/{seller_id}/{seller_sku_id}'.format(seller_id='101', seller_sku_id='1'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_getallby_seller_id(client):
    """Test case for getallby_seller_id

    Get all SKU Bindings by Seller ID
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
        path='/sku-binding/pvt/skuseller/list/bysellerId/{seller_id}'.format(seller_id='vtxkfj7352'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_getby_sku_id(client):
    """Test case for getby_sku_id

    Get SKU Bindings by SKU ID
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
        path='/catalog/pvt/skusellers/{sku_id}'.format(sku_id='1'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_getpagedadmin(client):
    """Test case for getpagedadmin

    Get SKU Bindings information
    """
    params = [('sellerId', 'vtxkfj7352'),
                    ('skuId', '1'),
                    ('sellerSkuId', '71'),
                    ('isActive', true),
                    ('size', '1')]
    headers = { 
        'Accept': 'application/json',
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/sku-binding/pvt/skuseller/admin',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_getpagedby_seller_id(client):
    """Test case for getpagedby_seller_id

    Get paged SKU Bindings by Seller ID
    """
    params = [('page', '1'),
                    ('size', '2')]
    headers = { 
        'Accept': 'application/json',
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/sku-binding/pvt/skuseller/paged/sellerid/{seller_id}'.format(seller_id='vtxkfj7352'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_insert_sku_binding(client):
    """Test case for insert_sku_binding

    Insert SKU Binding
    """
    body = {"IsActive":true,"SellerId":"vtxkfj7352","SellerStockKeepingUnitId":"71","StockKeepingUnitId":1}
    headers = { 
        'Content-Type': 'application/json',
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/sku-binding/pvt/skuseller/insertion',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sku_binding_pvt_skuseller_changenotification_seller_id_seller_sku_id_post(client):
    """Test case for sku_binding_pvt_skuseller_changenotification_seller_id_seller_sku_id_post

    Change Notification with Seller ID and Seller SKU ID
    """
    headers = { 
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/sku-binding/pvt/skuseller/changenotification/{seller_id}/{seller_sku_id}'.format(seller_id='101', seller_sku_id='1'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

