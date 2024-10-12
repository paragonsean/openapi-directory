# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_error import APIError


pytestmark = pytest.mark.asyncio

async def test_extractor_extractor_id_csv_latest_get(client):
    """Test case for extractor_extractor_id_csv_latest_get

    Get the latest crawl run results as a csv
    """
    headers = { 
        'Accept': 'text/csv',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/extractor/{extractor_id}/csv/latest'.format(extractor_id='extractor_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_extractor_extractor_id_json_latest_get(client):
    """Test case for extractor_extractor_id_json_latest_get

    Get the latest crawl run results as json
    """
    headers = { 
        'Accept': 'application/json; boundary=NL',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/extractor/{extractor_id}/json/latest'.format(extractor_id='extractor_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

