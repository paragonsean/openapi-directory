# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.factory import Factory
from openapi_server.models.factory_repo_update import FactoryRepoUpdate


pytestmark = pytest.mark.asyncio

async def test_factories_configure_factory_repo(client):
    """Test case for factories_configure_factory_repo

    
    """
    factory_repo_update = {"resourceGroupName":"resourceGroupName","vstsConfiguration":{"accountName":"accountName","collaborationBranch":"collaborationBranch","lastCommitId":"lastCommitId","rootFolder":"rootFolder","tenantId":"tenantId","projectName":"projectName","repositoryName":"repositoryName"},"factoryResourceId":"factoryResourceId"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/providers/Microsoft.DataFactory/locations/{location_id}/configureFactoryRepo'.format(subscription_id='subscription_id_example', location_id='location_id_example'),
        headers=headers,
        json=factory_repo_update,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

