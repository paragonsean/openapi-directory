# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.subscription import Subscription


pytestmark = pytest.mark.asyncio

async def test_add_repository(client):
    """Test case for add_repository

    Add repository to watch
    """
    params = [('repository', 'repository_example'),
                    ('autosubscribe', True),
                    ('dryrun', True)]
    headers = { 
        'Accept': 'application/json',
        'x_anchore_account': 'x_anchore_account_example',
    }
    response = await client.request(
        method='POST',
        path='/repositories',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

