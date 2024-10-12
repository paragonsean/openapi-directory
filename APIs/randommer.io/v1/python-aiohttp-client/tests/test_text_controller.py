# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.case_type import CaseType
from openapi_server.models.lorem_type import LoremType
from openapi_server.models.text_action_type import TextActionType
from openapi_server.models.text_dto import TextDto
from openapi_server.models.text_type import TextType


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_api_text_humanize_post(client):
    """Test case for api_text_humanize_post

    Humanize text
    """
    body = {"text":"text"}
    headers = { 
        'Content-Type': 'application/*+json',
        'x_api_key': 'x_api_key_example',
    }
    response = await client.request(
        method='POST',
        path='/api/Text/Humanize',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_text_lorem_ipsum_get(client):
    """Test case for api_text_lorem_ipsum_get

    Generate lorem ipsum
    """
    params = [('loremType', openapi_server.LoremType()),
                    ('type', openapi_server.TextType()),
                    ('number', 56)]
    headers = { 
        'x_api_key': 'x_api_key_example',
    }
    response = await client.request(
        method='GET',
        path='/api/Text/LoremIpsum',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_text_password_get(client):
    """Test case for api_text_password_get

    Generate password
    """
    params = [('length', 56),
                    ('hasDigits', True),
                    ('hasUppercase', True),
                    ('hasSpecial', True)]
    headers = { 
        'x_api_key': 'x_api_key_example',
    }
    response = await client.request(
        method='GET',
        path='/api/Text/Password',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_text_review_post(client):
    """Test case for api_text_review_post

    Get reviews (max quantity=500)
    """
    params = [('product', 'product_example'),
                    ('quantity', 56)]
    headers = { 
        'x_api_key': 'x_api_key_example',
    }
    response = await client.request(
        method='POST',
        path='/api/Text/Review',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_api_text_transform_post(client):
    """Test case for api_text_transform_post

    Transform text
    """
    body = {"text":"text"}
    params = [('textActionType', openapi_server.TextActionType()),
                    ('caseType', openapi_server.CaseType()),
                    ('find', 'find_example'),
                    ('replace', 'replace_example')]
    headers = { 
        'Content-Type': 'application/*+json',
        'x_api_key': 'x_api_key_example',
    }
    response = await client.request(
        method='POST',
        path='/api/Text/Transform',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

