# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.netlicensing import Netlicensing


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_create_license_template(client):
    """Test case for create_license_template

    Create License Template
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'active': True,
        'automatic': True,
        'currency': 'currency_example',
        'hidden': True,
        'hide_licenses': True,
        'license_type': 'license_type_example',
        'max_sessions': 'max_sessions_example',
        'name': 'name_example',
        'number': 'number_example',
        'price': 3.4,
        'product_module_number': 'product_module_number_example',
        'quantity': 'quantity_example',
        'quota': 'quota_example',
        'time_volume': 'time_volume_example',
        'time_volume_period': 'time_volume_period_example'
        }
    response = await client.request(
        method='POST',
        path='/core/v2/rest/licensetemplate',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_license_template(client):
    """Test case for delete_license_template

    Delete License Template
    """
    params = [('forceCascade', True)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/core/v2/rest/licensetemplate/{license_template_number}'.format(license_template_number='license_template_number_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_license_template(client):
    """Test case for get_license_template

    Get License Template
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/core/v2/rest/licensetemplate/{license_template_number}'.format(license_template_number='license_template_number_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_license_templates(client):
    """Test case for list_license_templates

    List License Templates
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/core/v2/rest/licensetemplate',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_update_license_template(client):
    """Test case for update_license_template

    Update License Template
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'active': True,
        'automatic': True,
        'currency': 'currency_example',
        'hidden': True,
        'hide_licenses': True,
        'license_type': 'license_type_example',
        'max_sessions': 'max_sessions_example',
        'name': 'name_example',
        'number': 'number_example',
        'price': 3.4,
        'quantity': 'quantity_example',
        'quota': 'quota_example',
        'time_volume': 'time_volume_example',
        'time_volume_period': 'time_volume_period_example'
        }
    response = await client.request(
        method='POST',
        path='/core/v2/rest/licensetemplate/{license_template_number}'.format(license_template_number='license_template_number_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

