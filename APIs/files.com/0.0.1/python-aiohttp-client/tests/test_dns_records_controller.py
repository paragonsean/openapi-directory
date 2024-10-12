# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.dns_record_entity import DnsRecordEntity


pytestmark = pytest.mark.asyncio

async def test_get_dns_records(client):
    """Test case for get_dns_records

    Show site DNS configuration.
    """
    params = [('cursor', 'cursor_example'),
                    ('per_page', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/rest/v1/dns_records',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

