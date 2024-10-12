# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.lifecycle_many_to_one_request import LifecycleManyToOneRequest
from openapi_server.models.lifecycle_one_to_one_request import LifecycleOneToOneRequest
from openapi_server.models.planning_level_data_dto import PlanningLevelDataDto


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_lifecycle_many_to_one_post(client):
    """Test case for lifecycle_many_to_one_post

    Map from old product to new product to create artifical history
    """
    body = {"planningLevelId":"planningLevelId","data":[{"timeSeriesId":"timeSeriesId","historyValues":[0.8008281904610115,0.8008281904610115]},{"timeSeriesId":"timeSeriesId","historyValues":[0.8008281904610115,0.8008281904610115]}],"ratios":[0.8008281904610115,0.8008281904610115]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
        'token': 'token_example',
    }
    response = await client.request(
        method='POST',
        path='/lifecycle/many-to-one',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_lifecycle_one_to_one_post(client):
    """Test case for lifecycle_one_to_one_post

    Map from old product to new product to create artifical history
    """
    body = {"planningLevelId":"planningLevelId","data":{"timeSeriesId":"timeSeriesId","historyValues":[0.8008281904610115,0.8008281904610115]},"ratio":15}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
        'token': 'token_example',
    }
    response = await client.request(
        method='POST',
        path='/lifecycle/one-to-one',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

