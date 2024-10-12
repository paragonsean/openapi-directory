# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.grafana import Grafana
from openapi_server.models.grafana_board import GrafanaBoard
from openapi_server.models.grafana_config_params import GrafanaConfigParams
from openapi_server.models.service import Service


pytestmark = pytest.mark.asyncio

async def test_id_delete_grafana_config(client):
    """Test case for id_delete_grafana_config

    Handle DELETE request for Grafana configuration
    """
    headers = { 
        'token': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/telemetry/metrics/grafana/config',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_id_get_grafana(client):
    """Test case for id_get_grafana

    Handle GET request for Grafana
    """
    headers = { 
        'Accept': 'application/json',
        'token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/telemetry/metrics/grafana/scan',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_id_get_grafana_boards(client):
    """Test case for id_get_grafana_boards

    Handle GET request for Grafana boards
    """
    params = [('dashboardSearch', 'dashboard_search_example')]
    headers = { 
        'Accept': 'application/json',
        'token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/telemetry/metrics/grafana/boards',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_id_get_grafana_config(client):
    """Test case for id_get_grafana_config

    Handle GET request for Grafana configuration
    """
    headers = { 
        'Accept': 'application/json',
        'token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/telemetry/metrics/grafana/config',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_id_get_grafana_ping(client):
    """Test case for id_get_grafana_ping

    Handle GET request for Grafana ping
    """
    headers = { 
        'token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/telemetry/metrics/grafana/ping',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_id_get_grafana_query(client):
    """Test case for id_get_grafana_query

    Handle GET request for Grafana queries
    """
    headers = { 
        'token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/telemetry/metrics/grafana/query',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_id_post_grafana_boards(client):
    """Test case for id_post_grafana_boards

    Handle POST request for Grafana boards
    """
    headers = { 
        'token': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/telemetry/metrics/grafana/boards',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_id_post_grafana_config(client):
    """Test case for id_post_grafana_config

    Handle POST request for Grafana configuration
    """
    body = {"grafanaAPIKey":"grafanaAPIKey","grafanaURL":"grafanaURL"}
    headers = { 
        'Content-Type': 'application/json',
        'token': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/telemetry/metrics/grafana/config',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

