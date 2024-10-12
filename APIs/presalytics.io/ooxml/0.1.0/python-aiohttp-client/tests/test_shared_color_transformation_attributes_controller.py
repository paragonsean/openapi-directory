# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.shared_color_transformation_attributes import SharedColorTransformationAttributes


pytestmark = pytest.mark.asyncio

async def test_shared_colortransformationattributes_get_id(client):
    """Test case for shared_colortransformationattributes_get_id

    ColorTransformationAttributes: Get by Id
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/ooxml-automation/Shared/ColorTransformationAttributes/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

