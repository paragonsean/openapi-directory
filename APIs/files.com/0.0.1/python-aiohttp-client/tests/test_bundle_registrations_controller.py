# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.bundle_registration_entity import BundleRegistrationEntity


pytestmark = pytest.mark.asyncio

async def test_get_bundle_registrations(client):
    """Test case for get_bundle_registrations

    List Bundle Registrations
    """
    params = [('user_id', 56),
                    ('cursor', 'cursor_example'),
                    ('per_page', 56),
                    ('bundle_id', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/rest/v1/bundle_registrations',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

