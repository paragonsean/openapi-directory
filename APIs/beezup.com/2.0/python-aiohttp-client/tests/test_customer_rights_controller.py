# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.beez_up_common_error_response_message import BeezUPCommonErrorResponseMessage
from openapi_server.models.functionality_right_info import FunctionalityRightInfo


pytestmark = pytest.mark.asyncio

async def test_get_rights(client):
    """Test case for get_rights

    Get store's rights
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/user/customer/stores/{store_id}/rights'.format(store_id='store_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

