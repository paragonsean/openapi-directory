# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.migration_exchange_error_schema import MigrationExchangeErrorSchema
from openapi_server.models.migration_exchange_success_schema import MigrationExchangeSuccessSchema


pytestmark = pytest.mark.asyncio

async def test_migration_exchange(client):
    """Test case for migration_exchange

    
    """
    params = [('token', 'token_example'),
                    ('users', 'users_example'),
                    ('team_id', 'team_id_example'),
                    ('to_old', True)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/migration.exchange',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

