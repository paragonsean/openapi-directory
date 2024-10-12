# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.deploy import Deploy
from openapi_server.models.deploy_files import DeployFiles
from openapi_server.models.error import Error


pytestmark = pytest.mark.asyncio

async def test_cancel_site_deploy(client):
    """Test case for cancel_site_deploy

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/deploys/{deploy_id}/cancel'.format(deploy_id='deploy_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_site_deploy(client):
    """Test case for create_site_deploy

    
    """
    deploy = openapi_server.DeployFiles()
    params = [('deploy-previews', True),
                    ('production', True),
                    ('state', 'state_example'),
                    ('branch', 'branch_example'),
                    ('latest-published', True),
                    ('title', 'title_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/sites/{site_id}/deploys'.format(site_id='site_id_example'),
        headers=headers,
        json=deploy,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_deploy(client):
    """Test case for delete_deploy

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/deploys/{deploy_id}'.format(deploy_id='deploy_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_site_deploy(client):
    """Test case for delete_site_deploy

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/sites/{site_id}/deploys/{deploy_id}'.format(deploy_id='deploy_id_example', site_id='site_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_deploy(client):
    """Test case for get_deploy

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/deploys/{deploy_id}'.format(deploy_id='deploy_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_site_deploy(client):
    """Test case for get_site_deploy

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/sites/{site_id}/deploys/{deploy_id}'.format(site_id='site_id_example', deploy_id='deploy_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_site_deploys(client):
    """Test case for list_site_deploys

    
    """
    params = [('deploy-previews', True),
                    ('production', True),
                    ('state', 'state_example'),
                    ('branch', 'branch_example'),
                    ('latest-published', True),
                    ('page', 56),
                    ('per_page', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/sites/{site_id}/deploys'.format(site_id='site_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_lock_deploy(client):
    """Test case for lock_deploy

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/deploys/{deploy_id}/lock'.format(deploy_id='deploy_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_restore_site_deploy(client):
    """Test case for restore_site_deploy

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/sites/{site_id}/deploys/{deploy_id}/restore'.format(site_id='site_id_example', deploy_id='deploy_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_rollback_site_deploy(client):
    """Test case for rollback_site_deploy

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/sites/{site_id}/rollback'.format(site_id='site_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_unlock_deploy(client):
    """Test case for unlock_deploy

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/deploys/{deploy_id}/unlock'.format(deploy_id='deploy_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_site_deploy(client):
    """Test case for update_site_deploy

    
    """
    deploy = openapi_server.DeployFiles()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/sites/{site_id}/deploys/{deploy_id}'.format(site_id='site_id_example', deploy_id='deploy_id_example'),
        headers=headers,
        json=deploy,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

