# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.container_for_project_features import ContainerForProjectFeatures
from openapi_server.models.project_feature_state import ProjectFeatureState


pytestmark = pytest.mark.asyncio

async def test_get_features_for_project(client):
    """Test case for get_features_for_project

    Get project features
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/rest/api/3/project/{project_id_or_key}/features'.format(project_id_or_key='project_id_or_key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_toggle_feature_for_project(client):
    """Test case for toggle_feature_for_project

    Set project feature state
    """
    body = {"state":"ENABLED"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='PUT',
        path='/rest/api/3/project/{project_id_or_key}/features/{feature_key}'.format(project_id_or_key='project_id_or_key_example', feature_key='feature_key_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

