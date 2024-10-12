# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.report_metadata import ReportMetadata
from openapi_server.models.report_metadatas import ReportMetadatas


pytestmark = pytest.mark.asyncio

async def test_get_report_metadata(client):
    """Test case for get_report_metadata

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/sell/marketing/v1/ad_report_metadata',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_report_metadata_for_report_type(client):
    """Test case for get_report_metadata_for_report_type

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/sell/marketing/v1/ad_report_metadata/{report_type}'.format(report_type='report_type_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

