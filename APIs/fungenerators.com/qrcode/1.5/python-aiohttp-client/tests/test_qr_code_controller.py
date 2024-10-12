# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.qrcode_decode_post_request import QrcodeDecodePostRequest


pytestmark = pytest.mark.asyncio

async def test_qrcode_business_card_get(client):
    """Test case for qrcode_business_card_get

    
    """
    params = [('firstname', 'firstname_example'),
                    ('lastname', 'lastname_example'),
                    ('middlename', 'middlename_example'),
                    ('email', 'email_example'),
                    ('company', 'company_example'),
                    ('phone_work', 'phone_work_example'),
                    ('phone_home', 'phone_home_example'),
                    ('phone_cell', 'phone_cell_example'),
                    ('street1', 'street1_example'),
                    ('street2', 'street2_example'),
                    ('city', 'city_example'),
                    ('zip', 'zip_example'),
                    ('state', 'state_example'),
                    ('country', 'country_example'),
                    ('format', 'format_example')]
    headers = { 
        'Accept': 'application/json',
        'X-Fungenerators-Api-Secret': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/qrcode/business_card',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_qrcode_decode_post(client):
    """Test case for qrcode_decode_post

    
    """
    body = openapi_server.QrcodeDecodePostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'mulitpart/form-data',
        'X-Fungenerators-Api-Secret': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/qrcode/decode',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_qrcode_email_get(client):
    """Test case for qrcode_email_get

    
    """
    params = [('email', 'email_example'),
                    ('subject', 'subject_example'),
                    ('body', 'body_example'),
                    ('format', 'format_example')]
    headers = { 
        'Accept': 'application/json',
        'X-Fungenerators-Api-Secret': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/qrcode/email',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_qrcode_phone_get(client):
    """Test case for qrcode_phone_get

    
    """
    params = [('number', 'number_example'),
                    ('format', 'format_example')]
    headers = { 
        'Accept': 'application/json',
        'X-Fungenerators-Api-Secret': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/qrcode/phone',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_qrcode_raw_get(client):
    """Test case for qrcode_raw_get

    
    """
    params = [('rawtext', 'rawtext_example'),
                    ('format', 'format_example')]
    headers = { 
        'Accept': 'application/json',
        'X-Fungenerators-Api-Secret': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/qrcode/raw',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_qrcode_skype_get(client):
    """Test case for qrcode_skype_get

    
    """
    params = [('username', 'username_example'),
                    ('format', 'format_example')]
    headers = { 
        'Accept': 'application/json',
        'X-Fungenerators-Api-Secret': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/qrcode/skype',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_qrcode_sms_get(client):
    """Test case for qrcode_sms_get

    
    """
    params = [('number', 'number_example'),
                    ('format', 'format_example')]
    headers = { 
        'Accept': 'application/json',
        'X-Fungenerators-Api-Secret': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/qrcode/sms',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_qrcode_text_get(client):
    """Test case for qrcode_text_get

    
    """
    params = [('text', 'text_example'),
                    ('format', 'format_example')]
    headers = { 
        'Accept': 'application/json',
        'X-Fungenerators-Api-Secret': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/qrcode/text',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_qrcode_url_get(client):
    """Test case for qrcode_url_get

    
    """
    params = [('url', 'url_example'),
                    ('format', 'format_example')]
    headers = { 
        'Accept': 'application/json',
        'X-Fungenerators-Api-Secret': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/qrcode/url',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

