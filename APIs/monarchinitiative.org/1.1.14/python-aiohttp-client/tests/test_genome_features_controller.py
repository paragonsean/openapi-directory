# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.sequence_feature import SequenceFeature


pytestmark = pytest.mark.asyncio

async def test_get_features_within_resource(client):
    """Test case for get_features_within_resource

    Returns list of matches
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/genome/features/within/{build}/{reference}/{begin}/{end}'.format(build='build_example', reference='reference_example', begin='begin_example', end='end_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

