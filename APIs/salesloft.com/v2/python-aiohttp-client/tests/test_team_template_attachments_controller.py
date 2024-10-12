# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.team_template_attachment import TeamTemplateAttachment


pytestmark = pytest.mark.asyncio

async def test_v2_team_template_attachments_json_get(client):
    """Test case for v2_team_template_attachments_json_get

    List team template attachments
    """
    params = [('ids', [56]),
                    ('team_template_id', [56]),
                    ('per_page', 56),
                    ('page', 56),
                    ('include_paging_counts', True),
                    ('limit_paging_counts', True)]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/v2/team_template_attachments.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

