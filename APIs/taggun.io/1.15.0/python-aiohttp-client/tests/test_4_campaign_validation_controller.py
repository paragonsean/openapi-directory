# coding: utf-8

import pytest
import json
from aiohttp import web
from aiohttp import FormData
from aiohttp import FormData

from openapi_server.models.bad_request_error import BadRequestError
from openapi_server.models.model9 import Model9


pytestmark = pytest.mark.asyncio

async def test_delete_api_validation_v1_campaign_settings_delete_campaignid(client):
    """Test case for delete_api_validation_v1_campaign_settings_delete_campaignid

    delete campaign settings for a client
    """
    headers = { 
        'Accept': '*/*',
        'apikey': 'apikey_example',
    }
    response = await client.request(
        method='DELETE',
        path='/api/validation/v1/campaign/settings/delete/{campaign_id}'.format(campaign_id='campaign_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_api_validation_v1_campaign_settings_campaignid(client):
    """Test case for get_api_validation_v1_campaign_settings_campaignid

    get campaign settings for a client
    """
    headers = { 
        'Accept': '*/*',
        'apikey': 'apikey_example',
    }
    response = await client.request(
        method='GET',
        path='/api/validation/v1/campaign/settings/{campaign_id}'.format(campaign_id='campaign_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_api_validation_v1_campaign_settings_list(client):
    """Test case for get_api_validation_v1_campaign_settings_list

    list all campaign setting IDs for a client
    """
    headers = { 
        'Accept': '*/*',
        'apikey': 'apikey_example',
    }
    response = await client.request(
        method='GET',
        path='/api/validation/v1/campaign/settings/list',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_post_api_validation_v1_campaign_file(client):
    """Test case for post_api_validation_v1_campaign_file

    validate and match a receipt against a campaign validation settings by uploading an image file
    """
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'multipart/form-data',
        'apikey': 'apikey_example',
    }
    data = FormData()
    data.add_field('file', '/path/to/file')
    data.add_field('incognito', False)
    data.add_field('ip_address', 'ip_address_example')
    data.add_field('near', 'near_example')
    data.add_field('campaign_id', 'campaign_id_example')
    data.add_field('reference_id', 'reference_id_example')
    response = await client.request(
        method='POST',
        path='/api/validation/v1/campaign/file',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_post_api_validation_v1_campaign_productvalidation_file(client):
    """Test case for post_api_validation_v1_campaign_productvalidation_file

    validate if user-submitted info like serial number are detected an image file
    """
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'multipart/form-data',
        'apikey': 'apikey_example',
    }
    data = FormData()
    data.add_field('file', '/path/to/file')
    data.add_field('product_verification_number', 'product_verification_number_example')
    data.add_field('incognito', False)
    data.add_field('sub_account_id', 'sub_account_id_example')
    data.add_field('reference_id', 'reference_id_example')
    response = await client.request(
        method='POST',
        path='/api/validation/v1/campaign/product-validation/file',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_post_api_validation_v1_campaign_settings_create_campaignid(client):
    """Test case for post_api_validation_v1_campaign_settings_create_campaignid

    create campaign settings for a client
    """
    body = openapi_server.Model9()
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
        'apikey': 'apikey_example',
    }
    response = await client.request(
        method='POST',
        path='/api/validation/v1/campaign/settings/create/{campaign_id}'.format(campaign_id='campaign_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_put_api_validation_v1_campaign_settings_update_campaignid(client):
    """Test case for put_api_validation_v1_campaign_settings_update_campaignid

    update campaign settings for a client
    """
    body = openapi_server.Model9()
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
        'apikey': 'apikey_example',
    }
    response = await client.request(
        method='PUT',
        path='/api/validation/v1/campaign/settings/update/{campaign_id}'.format(campaign_id='campaign_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

