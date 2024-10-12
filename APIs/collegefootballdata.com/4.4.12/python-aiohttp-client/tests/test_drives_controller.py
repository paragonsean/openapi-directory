# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.drive import Drive


pytestmark = pytest.mark.asyncio

async def test_get_drives(client):
    """Test case for get_drives

    Drive data and results
    """
    params = [('seasonType', 'regular'),
                    ('year', 56),
                    ('week', 56),
                    ('team', 'team_example'),
                    ('offense', 'offense_example'),
                    ('defense', 'defense_example'),
                    ('conference', 'conference_example'),
                    ('offenseConference', 'offense_conference_example'),
                    ('defenseConference', 'defense_conference_example'),
                    ('classification', 'classification_example')]
    headers = { 
        'Accept': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/drives',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

