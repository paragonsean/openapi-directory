# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.default_error_template import DefaultErrorTemplate
from openapi_server.models.default_success_template import DefaultSuccessTemplate
from openapi_server.models.team_access_logs_error_schema import TeamAccessLogsErrorSchema
from openapi_server.models.team_access_logs_schema import TeamAccessLogsSchema
from openapi_server.models.team_info_error_schema import TeamInfoErrorSchema
from openapi_server.models.team_info_schema import TeamInfoSchema
from openapi_server.models.team_integration_logs_error_schema import TeamIntegrationLogsErrorSchema
from openapi_server.models.team_integration_logs_schema import TeamIntegrationLogsSchema
from openapi_server.models.team_profile_get_error_schema import TeamProfileGetErrorSchema
from openapi_server.models.team_profile_get_success_schema import TeamProfileGetSuccessSchema


pytestmark = pytest.mark.asyncio

async def test_team_access_logs(client):
    """Test case for team_access_logs

    
    """
    params = [('token', 'token_example'),
                    ('before', 'before_example'),
                    ('count', 'count_example'),
                    ('page', 'page_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/team.accessLogs',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_team_billable_info(client):
    """Test case for team_billable_info

    
    """
    params = [('token', 'token_example'),
                    ('user', 'user_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/team.billableInfo',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_team_info(client):
    """Test case for team_info

    
    """
    params = [('token', 'token_example'),
                    ('team', 'team_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/team.info',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_team_integration_logs(client):
    """Test case for team_integration_logs

    
    """
    params = [('token', 'token_example'),
                    ('app_id', 'app_id_example'),
                    ('change_type', 'change_type_example'),
                    ('count', 'count_example'),
                    ('page', 'page_example'),
                    ('service_id', 'service_id_example'),
                    ('user', 'user_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/team.integrationLogs',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_team_profile_get_0(client):
    """Test case for team_profile_get_0

    
    """
    params = [('token', 'token_example'),
                    ('visibility', 'visibility_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/team.profile.get',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

