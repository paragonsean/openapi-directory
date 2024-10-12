# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.configuration_summary_list_response import ConfigurationSummaryListResponse
from openapi_server.models.configuration_update_summary_list_response import ConfigurationUpdateSummaryListResponse


pytestmark = pytest.mark.asyncio

async def test_query_configuration_history_updates(client):
    """Test case for query_configuration_history_updates

    View a list of filtered configuration updates
    """
    params = [('limit', 56),
                    ('offset', 56),
                    ('api_user', 'api_user_example'),
                    ('node_id', 'node_id_example'),
                    ('namespace', 'namespace_example'),
                    ('name', 'name_example'),
                    ('source', 'source_example'),
                    ('after_time', '2013-10-20T19:20:30+01:00'),
                    ('before_time', '2013-10-20T19:20:30+01:00')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/config/history/list_updates',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_retrieve_configuration_values(client):
    """Test case for retrieve_configuration_values

    View a list of configurations and their values on a given date
    """
    params = [('limit', 56),
                    ('offset', 56),
                    ('node_id', 'node_id_example'),
                    ('namespace', 'namespace_example'),
                    ('name', 'name_example'),
                    ('on_date', '2013-10-20T19:20:30+01:00')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/config/history/ondate',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

