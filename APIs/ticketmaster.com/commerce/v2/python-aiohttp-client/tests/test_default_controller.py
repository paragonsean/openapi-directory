# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.offering_response import OfferingResponse


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_get_event_offers(client):
    """Test case for get_event_offers

    Event Offers
    """
    body = 'body_example'
    params = [('access_token', 'access_token_example'),
                    ('api-key', 'api_key_example')]
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
        'x_ssl_cert_uid': 'x_ssl_cert_uid_example',
        'x_tm_access_token': 'x_tm_access_token_example',
    }
    response = await client.request(
        method='GET',
        path='/commerce/v2/commerce/v2/events/{event_id}/offers'.format(event_id='event_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

