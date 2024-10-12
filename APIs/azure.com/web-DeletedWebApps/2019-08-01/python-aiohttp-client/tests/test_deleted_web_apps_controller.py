# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.deleted_web_app_collection import DeletedWebAppCollection
from openapi_server.models.deleted_web_apps_get_deleted_web_app_by_location200_response import DeletedWebAppsGetDeletedWebAppByLocation200Response
from openapi_server.models.deleted_web_apps_list_default_response import DeletedWebAppsListDefaultResponse


pytestmark = pytest.mark.asyncio

async def test_deleted_web_apps_get_deleted_web_app_by_location(client):
    """Test case for deleted_web_apps_get_deleted_web_app_by_location

    Get deleted app for a subscription at location.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Web/locations/{location}/deletedSites/{deleted_site_id}'.format(location='location_example', deleted_site_id='deleted_site_id_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


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


pytestmark = pytest.mark.asyncio

async def test_deleted_web_apps_list_by_location(client):
    """Test case for deleted_web_apps_list_by_location

    Get all deleted apps for a subscription at location
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Web/locations/{location}/deletedSites'.format(location='location_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

