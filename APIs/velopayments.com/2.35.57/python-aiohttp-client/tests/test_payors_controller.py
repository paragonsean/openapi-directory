# coding: utf-8

import pytest
import json
from aiohttp import web
from aiohttp import FormData

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.inline_response400 import InlineResponse400
from openapi_server.models.inline_response403 import InlineResponse403
from openapi_server.models.inline_response404 import InlineResponse404
from openapi_server.models.inline_response409 import InlineResponse409
from openapi_server.models.payor_branding_response import PayorBrandingResponse
from openapi_server.models.payor_create_api_key_request import PayorCreateApiKeyRequest
from openapi_server.models.payor_create_api_key_response import PayorCreateApiKeyResponse
from openapi_server.models.payor_create_application_request import PayorCreateApplicationRequest
from openapi_server.models.payor_email_opt_out_request import PayorEmailOptOutRequest
from openapi_server.models.payor_v1 import PayorV1
from openapi_server.models.payor_v2 import PayorV2


pytestmark = pytest.mark.asyncio

async def test_get_payor_by_id_v1(client):
    """Test case for get_payor_by_id_v1

    Get Payor
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/payors/{payor_id}'.format(payor_id='payor_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_payor_by_id_v2(client):
    """Test case for get_payor_by_id_v2

    Get Payor
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/payors/{payor_id}'.format(payor_id='payor_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_payor_add_payor_logo_v1(client):
    """Test case for payor_add_payor_logo_v1

    Add Logo
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
        'Authorization': 'Bearer special-key',
    }
    data = FormData()
    data.add_field('logo', '/path/to/file')
    response = await client.request(
        method='POST',
        path='/v1/payors/{payor_id}/branding/logos'.format(payor_id='payor_id_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_payor_create_api_key_v1(client):
    """Test case for payor_create_api_key_v1

    Create API Key
    """
    body = {"description":"Key for iOS mobile application","name":"iOS Key","roles":["velo.payor.admin"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/payors/{payor_id}/applications/{application_id}/keys'.format(payor_id='payor_id_example', application_id='application_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_payor_create_application_v1(client):
    """Test case for payor_create_application_v1

    Create Application
    """
    body = {"description":"SAP Application integration","name":"SAP"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/payors/{payor_id}/applications'.format(payor_id='payor_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_payor_email_opt_out(client):
    """Test case for payor_email_opt_out

    Reminder Email Opt-Out
    """
    body = {"reminderEmailsOptOut":True}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/payors/{payor_id}/reminderEmailsUpdate'.format(payor_id='payor_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_payor_get_branding(client):
    """Test case for payor_get_branding

    Get Branding
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/payors/{payor_id}/branding'.format(payor_id='payor_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

