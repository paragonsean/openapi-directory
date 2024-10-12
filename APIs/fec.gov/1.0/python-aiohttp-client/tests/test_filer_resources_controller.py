# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.rad_analyst_page import RadAnalystPage
from openapi_server.models.state_election_office_info_page import StateElectionOfficeInfoPage


pytestmark = pytest.mark.asyncio

async def test_rad_analyst_get(client):
    """Test case for rad_analyst_get

    
    """
    params = [('api_key', 'DEMO_KEY'),
                    ('min_assignment_update_date', '2013-10-20'),
                    ('telephone_ext', [56]),
                    ('analyst_id', [56]),
                    ('sort_null_only', False),
                    ('page', 1),
                    ('committee_id', ['committee_id_example']),
                    ('sort_nulls_last', False),
                    ('sort_hide_null', False),
                    ('name', ['name_example']),
                    ('per_page', 20),
                    ('email', ['email_example']),
                    ('title', ['title_example']),
                    ('sort', 'sort_example'),
                    ('max_assignment_update_date', '2013-10-20'),
                    ('analyst_short_id', [56])]
    headers = { 
        'Accept': 'application/json',
        'ApiKeyHeaderAuth': 'special-key',
        'ApiKeyQueryAuth': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/rad-analyst/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_state_election_office_get(client):
    """Test case for state_election_office_get

    
    """
    params = [('page', 1),
                    ('state', 'state_example'),
                    ('api_key', 'DEMO_KEY'),
                    ('sort_hide_null', False),
                    ('per_page', 20),
                    ('sort_null_only', False),
                    ('sort', 'sort_example'),
                    ('sort_nulls_last', False)]
    headers = { 
        'Accept': 'application/json',
        'ApiKeyHeaderAuth': 'special-key',
        'ApiKeyQueryAuth': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/state-election-office/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

