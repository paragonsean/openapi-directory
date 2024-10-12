# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.operative_deed import OperativeDeed


pytestmark = pytest.mark.asyncio

async def test_deed_deed_reference_get(client):
    """Test case for deed_deed_reference_get

    Deed
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/deed/{deed_reference}'.format(deed_reference='deed_reference_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

