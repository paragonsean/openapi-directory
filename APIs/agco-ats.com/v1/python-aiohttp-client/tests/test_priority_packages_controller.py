# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_models_api_error import APIModelsApiError
from openapi_server.models.api_paged_response_update_system_models_priority_package import APIPagedResponseUpdateSystemModelsPriorityPackage
from openapi_server.models.update_system_models_priority_package import UpdateSystemModelsPriorityPackage


pytestmark = pytest.mark.asyncio

async def test_priority_packages_delete_priority_packages(client):
    """Test case for priority_packages_delete_priority_packages

    Delete a Priority Package for a Client.
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v2/PriorityPackages/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_priority_packages_get_priority_package(client):
    """Test case for priority_packages_get_priority_package

    Get a Priority Packages for a Client.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/PriorityPackages/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_priority_packages_get_priority_packages(client):
    """Test case for priority_packages_get_priority_packages

    Get a list of Priority Packages by Client.
    """
    params = [('ClientID', 'client_id_example'),
                    ('Status', 'status_example'),
                    ('limit', 56),
                    ('offset', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/PriorityPackages',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_priority_packages_post_priority_packages(client):
    """Test case for priority_packages_post_priority_packages

    Add a Priority Package for a Client.
    """
    body = openapi_server.UpdateSystemModelsPriorityPackage()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v2/PriorityPackages',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

