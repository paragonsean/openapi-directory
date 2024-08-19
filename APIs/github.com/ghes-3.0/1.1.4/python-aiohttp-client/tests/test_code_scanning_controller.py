# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.activity_list_public_events503_response import ActivityListPublicEvents503Response
from openapi_server.models.basic_error import BasicError
from openapi_server.models.code_scanning_alert import CodeScanningAlert
from openapi_server.models.code_scanning_alert_items import CodeScanningAlertItems
from openapi_server.models.code_scanning_alert_state import CodeScanningAlertState
from openapi_server.models.code_scanning_analysis import CodeScanningAnalysis
from openapi_server.models.code_scanning_sarifs_receipt import CodeScanningSarifsReceipt
from openapi_server.models.code_scanning_update_alert_request import CodeScanningUpdateAlertRequest
from openapi_server.models.code_scanning_upload_sarif_request import CodeScanningUploadSarifRequest


pytestmark = pytest.mark.asyncio

async def test_code_scanning_get_alert(client):
    """Test case for code_scanning_get_alert

    Get a code scanning alert
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/repos/{owner}/{repo}/code-scanning/alerts/{alert_number}'.format(owner='owner_example', repo='repo_example', alert_number=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_code_scanning_list_alerts_for_repo(client):
    """Test case for code_scanning_list_alerts_for_repo

    List code scanning alerts for a repository
    """
    params = [('tool_name', 'tool_name_example'),
                    ('tool_guid', 'tool_guid_example'),
                    ('page', 1),
                    ('per_page', 30),
                    ('ref', 'ref_example'),
                    ('state', openapi_server.CodeScanningAlertState())]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/repos/{owner}/{repo}/code-scanning/alerts'.format(owner='owner_example', repo='repo_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_code_scanning_list_recent_analyses(client):
    """Test case for code_scanning_list_recent_analyses

    List code scanning analyses for a repository
    """
    params = [('tool_name', 'tool_name_example'),
                    ('tool_guid', 'tool_guid_example'),
                    ('page', 1),
                    ('per_page', 30),
                    ('ref', 'ref_example'),
                    ('sarif_id', 'sarif_id_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/repos/{owner}/{repo}/code-scanning/analyses'.format(owner='owner_example', repo='repo_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_code_scanning_update_alert(client):
    """Test case for code_scanning_update_alert

    Update a code scanning alert
    """
    body = {"dismissed_reason":"false positive","state":"dismissed"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v3/repos/{owner}/{repo}/code-scanning/alerts/{alert_number}'.format(owner='owner_example', repo='repo_example', alert_number=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_code_scanning_upload_sarif(client):
    """Test case for code_scanning_upload_sarif

    Upload an analysis as SARIF data
    """
    body = openapi_server.CodeScanningUploadSarifRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/repos/{owner}/{repo}/code-scanning/sarifs'.format(owner='owner_example', repo='repo_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

