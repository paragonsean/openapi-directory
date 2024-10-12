# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.activity_list_public_events503_response import ActivityListPublicEvents503Response
from openapi_server.models.secret_scanning_alert import SecretScanningAlert
from openapi_server.models.secret_scanning_update_alert_request import SecretScanningUpdateAlertRequest


pytestmark = pytest.mark.asyncio

async def test_secret_scanning_get_alert(client):
    """Test case for secret_scanning_get_alert

    Get a secret scanning alert
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/repos/{owner}/{repo}/secret-scanning/alerts/{alert_number}'.format(owner='owner_example', repo='repo_example', alert_number=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_secret_scanning_list_alerts_for_repo(client):
    """Test case for secret_scanning_list_alerts_for_repo

    List secret scanning alerts for a repository
    """
    params = [('state', 'state_example'),
                    ('secret_type', 'secret_type_example'),
                    ('resolution', 'resolution_example'),
                    ('page', 1),
                    ('per_page', 30)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/repos/{owner}/{repo}/secret-scanning/alerts'.format(owner='owner_example', repo='repo_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_secret_scanning_update_alert(client):
    """Test case for secret_scanning_update_alert

    Update a secret scanning alert
    """
    body = {"resolution":"false_positive","state":"resolved"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/repos/{owner}/{repo}/secret-scanning/alerts/{alert_number}'.format(owner='owner_example', repo='repo_example', alert_number=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

