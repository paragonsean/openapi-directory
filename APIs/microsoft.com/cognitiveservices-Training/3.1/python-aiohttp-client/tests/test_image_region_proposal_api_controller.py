# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.custom_vision_error import CustomVisionError
from openapi_server.models.image_region_proposal import ImageRegionProposal


pytestmark = pytest.mark.asyncio

async def test_get_image_region_proposals(client):
    """Test case for get_image_region_proposals

    Get region proposals for an image. Returns empty array if no proposals are found.
    """
    headers = { 
        'Accept': 'application/json',
        'training_key': '{API Key}',
    }
    response = await client.request(
        method='POST',
        path='/customvision/v3.1/training/projects/{project_id}/images/{image_id}/regionproposals'.format(project_id='bc3f7dad-5544-468c-8573-3ef04d55463e', image_id='4d6eb844-42ee-42bc-bd6f-c32455ef07c9'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

