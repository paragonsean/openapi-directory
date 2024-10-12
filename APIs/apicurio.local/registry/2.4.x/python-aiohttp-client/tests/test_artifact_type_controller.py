# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.artifact_type_info import ArtifactTypeInfo
from openapi_server.models.error import Error


pytestmark = pytest.mark.asyncio

async def test_list_artifact_types(client):
    """Test case for list_artifact_types

    List artifact types
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/admin/artifactTypes',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

