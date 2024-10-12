# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_response import ApiResponse
from openapi_server.models.findings_inner import FindingsInner
from openapi_server.models.scan_definition import ScanDefinition


pytestmark = pytest.mark.asyncio

async def test_clean_scan_page(client):
    """Test case for clean_scan_page

    Clean scan
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/clean/{scan_id}'.format(scan_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_clean_scans_page(client):
    """Test case for clean_scans_page

    Clean all scans
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/clean',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_default_page(client):
    """Test case for get_default_page

    Index page
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_finding_page(client):
    """Test case for get_finding_page

    Get findings on finished scans
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/getfindings/{scan_id}'.format(scan_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_info_page(client):
    """Test case for get_info_page

    Engine info page
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/info',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_liveness_page(client):
    """Test case for get_liveness_page

    Liveness page
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/liveness',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_readiness_page(client):
    """Test case for get_readiness_page

    Readiness page
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/readiness',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_test_page(client):
    """Test case for get_test_page

    Test page
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/test',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_reload_configuration_page(client):
    """Test case for reload_configuration_page

    Configuration reloading page
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/reloadconfig',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_start_scan_page(client):
    """Test case for start_scan_page

    Start a new scan
    """
    body = {"assets":[{"datatype":"ip","criticity":"low","id":"3","value":"8.8.8.8"},{"datatype":"ip","criticity":"low","id":"3","value":"8.8.8.8"}],"options":"{}","scan_id":1}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/startscan',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_status_scan_page(client):
    """Test case for status_scan_page

    Status of a scan
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/status/{scan_id}'.format(scan_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_status_scans_page(client):
    """Test case for status_scans_page

    Status on all scans
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/status',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stop_scan_page(client):
    """Test case for stop_scan_page

    Stop a scan
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/stop/{scan_id}'.format(scan_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stop_scans_page(client):
    """Test case for stop_scans_page

    Stop all scans
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/stopscans',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

