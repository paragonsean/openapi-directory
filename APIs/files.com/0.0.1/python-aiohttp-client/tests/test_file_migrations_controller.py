# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.file_migration_entity import FileMigrationEntity


pytestmark = pytest.mark.asyncio

async def test_get_file_migrations_id(client):
    """Test case for get_file_migrations_id

    Show File Migration
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/rest/v1/file_migrations/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

