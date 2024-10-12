# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.id_type import IdType
from openapi_server.models.number_validation import NumberValidation


pytestmark = pytest.mark.asyncio

async def test_api_social_number_get(client):
    """Test case for api_social_number_get

    Generate a social security number
    """
    headers = { 
        'x_api_key': 'x_api_key_example',
    }
    response = await client.request(
        method='GET',
        path='/api/SocialNumber',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_api_social_number_post(client):
    """Test case for api_social_number_post

    Validate VAT/identity numbers
    """
    body = {"country":"country","number":"number"}
    params = [('idType', openapi_server.IdType())]
    headers = { 
        'Content-Type': 'application/*+json',
        'x_api_key': 'x_api_key_example',
    }
    response = await client.request(
        method='POST',
        path='/api/SocialNumber',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

