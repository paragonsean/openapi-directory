# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.custom_vision_error import CustomVisionError
from openapi_server.models.suggested_tag_and_region import SuggestedTagAndRegion


pytestmark = pytest.mark.asyncio

async def test_suggest_tags_and_regions(client):
    """Test case for suggest_tags_and_regions

    Suggest tags and regions for an array/batch of untagged images. Returns empty array if no tags are found.
    """
    params = [('iterationId', '4d6eb844-42ee-42bc-bd6f-c32455ef07c9'),
                    ('imageIds', ['[\"e7f08c23-9e54-49f7-b609-69a0240ba306\",\"ce632666-4b66-4adb-aa0a-ad8b7c32df06\"]'])]
    headers = { 
        'Accept': 'application/json',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/customvision/v3.2/training/projects/{project_id}/tagsandregions/suggestions'.format(project_id='bc3f7dad-5544-468c-8573-3ef04d55463e'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

