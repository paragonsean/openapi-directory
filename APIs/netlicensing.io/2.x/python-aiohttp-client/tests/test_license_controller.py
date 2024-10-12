# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.netlicensing import Netlicensing


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_create_license(client):
    """Test case for create_license

    Create License
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'active': True,
        'currency': 'currency_example',
        'hidden': True,
        'license_template_number': 'license_template_number_example',
        'licensee_number': 'licensee_number_example',
        'name': 'name_example',
        'number': 'number_example',
        'parentfeature': 'parentfeature_example',
        'price': 3.4,
        'quantity': 'quantity_example',
        'start_date': '2013-10-20T19:20:30+01:00',
        'time_volume': 'time_volume_example',
        'time_volume_period': 'time_volume_period_example',
        'used_quantity': 'used_quantity_example'
        }
    response = await client.request(
        method='POST',
        path='/core/v2/rest/license',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_license(client):
    """Test case for delete_license

    Delete License
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/core/v2/rest/license/{license_number}'.format(license_number='license_number_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_license(client):
    """Test case for get_license

    Get License
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/core/v2/rest/license/{license_number}'.format(license_number='license_number_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_licenses(client):
    """Test case for list_licenses

    List Licenses
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/core/v2/rest/license',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_update_license(client):
    """Test case for update_license

    Update License
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'active': True,
        'currency': 'currency_example',
        'hidden': True,
        'name': 'name_example',
        'number': 'number_example',
        'parentfeature': 'parentfeature_example',
        'price': 3.4,
        'quantity': 'quantity_example',
        'start_date': '2013-10-20T19:20:30+01:00',
        'time_volume': 'time_volume_example',
        'time_volume_period': 'time_volume_period_example',
        'used_quantity': 'used_quantity_example'
        }
    response = await client.request(
        method='POST',
        path='/core/v2/rest/license/{license_number}'.format(license_number='license_number_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

