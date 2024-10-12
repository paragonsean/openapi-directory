# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.gift_wrapping_data_wrapping_interface import GiftWrappingDataWrappingInterface
from openapi_server.models.gift_wrapping_wrapping_repository_v1_save_post_request import GiftWrappingWrappingRepositoryV1SavePostRequest


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_gift_wrapping_wrapping_repository_v1_save_put(client):
    """Test case for gift_wrapping_wrapping_repository_v1_save_put

    gift-wrappings/{wrappingId}
    """
    body = openapi_server.GiftWrappingWrappingRepositoryV1SavePostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/rest/default/V1/gift-wrappings/{wrapping_id}'.format(wrapping_id='wrapping_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

