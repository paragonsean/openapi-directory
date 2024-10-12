# coding: utf-8

import pytest
import json
from aiohttp import web
from aiohttp import FormData
from aiohttp import FormData
from aiohttp import FormData



pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_api_v1_vendors_create(client):
    """Test case for api_v1_vendors_create

    Creates a new Vendor
    """
    headers = { 
        'Content-Type': 'multipart/form-data',
    }
    data = FormData()
    data.add_field('vendor_name', 'vendor_name_example')
    data.add_field('vendor_info', 'vendor_info_example')
    data.add_field('vendor_url', 'vendor_url_example')
    data.add_field('vendor_mac', 'vendor_mac_example')
    response = await client.request(
        method='POST',
        path='/api/v1/vendors.json',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_api_v1_vendors_id_json_patch(client):
    """Test case for api_v1_vendors_id_json_patch

    Updates an existing Vendor
    """
    headers = { 
        'Content-Type': 'multipart/form-data',
    }
    data = FormData()
    data.add_field('vendor_name', 'vendor_name_example')
    data.add_field('vendor_info', 'vendor_info_example')
    data.add_field('vendor_url', 'vendor_url_example')
    data.add_field('vendor_mac', 'vendor_mac_example')
    response = await client.request(
        method='PATCH',
        path='/api/v1/vendors/{id_jso}'.format(id='id_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_api_v1_vendors_id_json_put(client):
    """Test case for api_v1_vendors_id_json_put

    Updates an existing Vendor
    """
    headers = { 
        'Content-Type': 'multipart/form-data',
    }
    data = FormData()
    data.add_field('vendor_name', 'vendor_name_example')
    data.add_field('vendor_info', 'vendor_info_example')
    data.add_field('vendor_url', 'vendor_url_example')
    data.add_field('vendor_mac', 'vendor_mac_example')
    response = await client.request(
        method='PUT',
        path='/api/v1/vendors/{id_jso}'.format(id='id_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_v1_vendors_index(client):
    """Test case for api_v1_vendors_index

    Fetches all Vendors
    """
    params = [('page', 56),
                    ('order', 'order_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/v1/vendors.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_v1_vendors_show(client):
    """Test case for api_v1_vendors_show

    Fetches a single Vendor
    """
    params = [('order', 'order_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/v1/vendors/{id_jso}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

