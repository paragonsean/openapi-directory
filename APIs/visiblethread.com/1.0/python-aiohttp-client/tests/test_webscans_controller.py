# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.new_scan import NewScan
from openapi_server.models.new_scan_response import NewScanResponse
from openapi_server.models.scan_response_detailed import ScanResponseDetailed
from openapi_server.models.scan_response_summary import ScanResponseSummary
from openapi_server.models.web_response_not_ready import WebResponseNotReady
from openapi_server.models.web_url_detail import WebUrlDetail


pytestmark = pytest.mark.asyncio

async def test_get_scan_by_id(client):
    """Test case for get_scan_by_id

    Get data from a previously run scan
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/webscans/{scan_id}'.format(scan_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_scan_url_by_id(client):
    """Test case for get_scan_url_by_id

    Gets data for a particular scan/webUrl
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/webscans/{scan_id}/webUrls/{url_id}'.format(scan_id=56, url_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_run_scan(client):
    """Test case for run_scan

    Run a new scan
    """
    body = {"webUrls":[{"url":"http://visiblethread.com"},{"url":"http://visiblethread.com"}],"scanSettings":{"longSentenceWordCount":20,"veryLongSentenceWordCount":30},"title":"My fancy scan title"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/webscans',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_webscans_get(client):
    """Test case for webscans_get

    Get your list of scans
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/webscans',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

