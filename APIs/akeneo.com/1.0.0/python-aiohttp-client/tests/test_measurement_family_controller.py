# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.measurement_families_get_list200_response import MeasurementFamiliesGetList200Response
from openapi_server.models.patch_measurement_families200_response_inner import PatchMeasurementFamilies200ResponseInner
from openapi_server.models.post_token400_response import PostToken400Response


pytestmark = pytest.mark.asyncio

async def test_measurement_families_get_list(client):
    """Test case for measurement_families_get_list

    Get list of measurement families
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/rest/v1/measurement-families',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_patch_measurement_families(client):
    """Test case for patch_measurement_families

    Update/create several measurement families
    """
    body = [openapi_server.MeasurementFamiliesGetList200Response()]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/api/rest/v1/measurement-families',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

