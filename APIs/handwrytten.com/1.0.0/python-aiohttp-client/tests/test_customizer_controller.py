# coding: utf-8

import pytest
import json
from aiohttp import web
from aiohttp import FormData

from openapi_server.models.card import Card
from openapi_server.models.create_custom_card_request import CreateCustomCardRequest
from openapi_server.models.font_for_customizer import FontForCustomizer
from openapi_server.models.upload_custom_logo200_response import UploadCustomLogo200Response


pytestmark = pytest.mark.asyncio

async def test_create_custom_card(client):
    """Test case for create_custom_card

    Create a new custom card
    """
    body = openapi_server.CreateCustomCardRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/cards/createCustomCard',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fonts_list_for_customizer(client):
    """Test case for fonts_list_for_customizer

    Lists fonts available for use with the card customizer
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/fonts/listForCustomizer',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_upload_custom_logo(client):
    """Test case for upload_custom_logo

    upload logo or cover image for card
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
    }
    data = FormData()
    data.add_field('file', '/path/to/file')
    data.add_field('type', 'type_example')
    data.add_field('uid', 'uid_example')
    response = await client.request(
        method='POST',
        path='/v1/cards/uploadCustomLogo',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

