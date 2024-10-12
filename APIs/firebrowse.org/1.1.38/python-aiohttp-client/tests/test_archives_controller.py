# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_standard_data(client):
    """Test case for standard_data

    Retrieve standard data archives.
    """
    params = [('format', json),
                    ('date', ['2013-10-20']),
                    ('cohort', ['cohort_example']),
                    ('data_type', ['data_type_example']),
                    ('tool', ['tool_example']),
                    ('platform', ['platform_example']),
                    ('center', ['center_example']),
                    ('level', [56]),
                    ('protocol', ['protocol_example']),
                    ('page', [56]),
                    ('page_size', [56]),
                    ('sort_by', cohort)]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/v1/Archives/StandardData',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

