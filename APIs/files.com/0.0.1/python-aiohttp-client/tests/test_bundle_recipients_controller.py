# coding: utf-8

import pytest
import json
from aiohttp import web
from aiohttp import FormData

from openapi_server.models.bundle_recipient_entity import BundleRecipientEntity


pytestmark = pytest.mark.asyncio

async def test_get_bundle_recipients(client):
    """Test case for get_bundle_recipients

    List Bundle Recipients
    """
    params = [('user_id', 56),
                    ('cursor', 'cursor_example'),
                    ('per_page', 56),
                    ('sort_by', None),
                    ('filter', None),
                    ('bundle_id', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/rest/v1/bundle_recipients',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_post_bundle_recipients(client):
    """Test case for post_bundle_recipients

    Create Bundle Recipient
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
    }
    data = FormData()
    data.add_field('bundle_id', 56)
    data.add_field('company', 'company_example')
    data.add_field('name', 'name_example')
    data.add_field('note', 'note_example')
    data.add_field('recipient', 'recipient_example')
    data.add_field('share_after_create', True)
    data.add_field('user_id', 56)
    response = await client.request(
        method='POST',
        path='/api/rest/v1/bundle_recipients',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

