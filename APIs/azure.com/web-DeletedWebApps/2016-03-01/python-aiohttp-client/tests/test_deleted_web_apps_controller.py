# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.deleted_web_app_collection import DeletedWebAppCollection


pytestmark = pytest.mark.asyncio

async def test_deleted_web_apps_list(client):
    """Test case for deleted_web_apps_list

    Get all deleted apps for a subscription.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Web/deletedSites'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

