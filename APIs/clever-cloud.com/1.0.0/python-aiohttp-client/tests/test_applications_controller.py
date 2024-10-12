# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.addon import Addon
from openapi_server.models.app_instance import AppInstance
from openapi_server.models.application import Application
from openapi_server.models.body import Body
from openapi_server.models.deployment import Deployment
from openapi_server.models.env import Env
from openapi_server.models.instance import Instance
from openapi_server.models.linked_app_env import LinkedAppEnv
from openapi_server.models.list_env import ListEnv
from openapi_server.models.vhost import Vhost
from openapi_server.models.wannabe_application import WannabeApplication
from openapi_server.models.wannabe_env import WannabeEnv


pytestmark = pytest.mark.asyncio

async def test_delete_organisations_id_applications_app_id_0(client):
    """Test case for delete_organisations_id_applications_app_id_0

    
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/v2/organisations/{id}/applications/{app_id}'.format(id='id_example', app_id='app_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_organisations_id_applications_app_id_addons_addon_id_1(client):
    """Test case for delete_organisations_id_applications_app_id_addons_addon_id_1

    
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/v2/organisations/{id}/applications/{app_id}/addons/{addon_id}'.format(id='id_example', app_id='app_id_example', addon_id='addon_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_organisations_id_applications_app_id_dependencies_dependency_id_0(client):
    """Test case for delete_organisations_id_applications_app_id_dependencies_dependency_id_0

    
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/v2/organisations/{id}/applications/{app_id}/dependencies/{dependency_id}'.format(dependency_id='dependency_id_example', app_id='app_id_example', id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_organisations_id_applications_app_id_deployments_deployment_id_instances_0(client):
    """Test case for delete_organisations_id_applications_app_id_deployments_deployment_id_instances_0

    
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/v2/organisations/{id}/applications/{app_id}/deployments/{deployment_id}/instances'.format(id='id_example', app_id='app_id_example', deployment_id='deployment_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_organisations_id_applications_app_id_env_env_name_0(client):
    """Test case for delete_organisations_id_applications_app_id_env_env_name_0

    
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/v2/organisations/{id}/applications/{app_id}/env/{env_name}'.format(id='id_example', app_id='app_id_example', env_name='env_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_organisations_id_applications_app_id_instances_0(client):
    """Test case for delete_organisations_id_applications_app_id_instances_0

    
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/v2/organisations/{id}/applications/{app_id}/instances'.format(id='id_example', app_id='app_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_organisations_id_applications_app_id_tags_tag_0(client):
    """Test case for delete_organisations_id_applications_app_id_tags_tag_0

    
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/v2/organisations/{id}/applications/{app_id}/tags/{tag}'.format(id='id_example', app_id='app_id_example', tag='tag_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_organisations_id_applications_app_id_vhosts_domain_0(client):
    """Test case for delete_organisations_id_applications_app_id_vhosts_domain_0

    
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/v2/organisations/{id}/applications/{app_id}/vhosts/{domain}'.format(id='id_example', app_id='app_id_example', domain='domain_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_organisations_id_applications_app_id_vhosts_favourite_0(client):
    """Test case for delete_organisations_id_applications_app_id_vhosts_favourite_0

    
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/v2/organisations/{id}/applications/{app_id}/vhosts/favourite'.format(id='id_example', app_id='app_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_self_applications_app_id_0(client):
    """Test case for delete_self_applications_app_id_0

    
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/v2/self/applications/{app_id}'.format(app_id='app_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_self_applications_app_id_addons_addon_id_1(client):
    """Test case for delete_self_applications_app_id_addons_addon_id_1

    
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/v2/self/applications/{app_id}/addons/{addon_id}'.format(app_id='app_id_example', addon_id='addon_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_self_applications_app_id_dependencies_dependency_id_0(client):
    """Test case for delete_self_applications_app_id_dependencies_dependency_id_0

    
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/v2/self/applications/{app_id}/dependencies/{dependency_id}'.format(dependency_id='dependency_id_example', app_id='app_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_self_applications_app_id_deployments_deployment_id_instances_0(client):
    """Test case for delete_self_applications_app_id_deployments_deployment_id_instances_0

    
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/v2/self/applications/{app_id}/deployments/{deployment_id}/instances'.format(app_id='app_id_example', deployment_id='deployment_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_self_applications_app_id_env_env_name_0(client):
    """Test case for delete_self_applications_app_id_env_env_name_0

    
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/v2/self/applications/{app_id}/env/{env_name}'.format(app_id='app_id_example', env_name='env_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_self_applications_app_id_instances_0(client):
    """Test case for delete_self_applications_app_id_instances_0

    
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/v2/self/applications/{app_id}/instances'.format(app_id='app_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_self_applications_app_id_tags_tag_0(client):
    """Test case for delete_self_applications_app_id_tags_tag_0

    
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/v2/self/applications/{app_id}/tags/{tag}'.format(app_id='app_id_example', tag='tag_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_self_applications_app_id_vhosts_domain_0(client):
    """Test case for delete_self_applications_app_id_vhosts_domain_0

    
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/v2/self/applications/{app_id}/vhosts/{domain}'.format(app_id='app_id_example', domain='domain_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_self_applications_app_id_vhosts_favourite_0(client):
    """Test case for delete_self_applications_app_id_vhosts_favourite_0

    
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/v2/self/applications/{app_id}/vhosts/favourite'.format(app_id='app_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_github_applications_0(client):
    """Test case for get_github_applications_0

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/github/applications',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organisations_id_addons_addon_id_applications_1(client):
    """Test case for get_organisations_id_addons_addon_id_applications_1

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/organisations/{id}/addons/{addon_id}/applications'.format(id='id_example', addon_id='addon_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organisations_id_applications_0(client):
    """Test case for get_organisations_id_applications_0

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/organisations/{id}/applications'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organisations_id_applications_app_id_0(client):
    """Test case for get_organisations_id_applications_app_id_0

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/organisations/{id}/applications/{app_id}'.format(id='id_example', app_id='app_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organisations_id_applications_app_id_addons_1(client):
    """Test case for get_organisations_id_applications_app_id_addons_1

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/organisations/{id}/applications/{app_id}/addons'.format(id='id_example', app_id='app_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organisations_id_applications_app_id_addons_env_1(client):
    """Test case for get_organisations_id_applications_app_id_addons_env_1

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/organisations/{id}/applications/{app_id}/addons/env'.format(id='id_example', app_id='app_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organisations_id_applications_app_id_dependencies_0(client):
    """Test case for get_organisations_id_applications_app_id_dependencies_0

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/organisations/{id}/applications/{app_id}/dependencies'.format(app_id='app_id_example', id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organisations_id_applications_app_id_dependents_0(client):
    """Test case for get_organisations_id_applications_app_id_dependents_0

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/organisations/{id}/applications/{app_id}/dependents'.format(app_id='app_id_example', id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organisations_id_applications_app_id_deployments_0(client):
    """Test case for get_organisations_id_applications_app_id_deployments_0

    
    """
    params = [('limit', 'limit_example'),
                    ('offset', 'offset_example'),
                    ('action', 'action_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/organisations/{id}/applications/{app_id}/deployments'.format(id='id_example', app_id='app_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organisations_id_applications_app_id_env_0(client):
    """Test case for get_organisations_id_applications_app_id_env_0

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/organisations/{id}/applications/{app_id}/env'.format(id='id_example', app_id='app_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organisations_id_applications_app_id_instances_0(client):
    """Test case for get_organisations_id_applications_app_id_instances_0

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/organisations/{id}/applications/{app_id}/instances'.format(id='id_example', app_id='app_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organisations_id_applications_app_id_tags_0(client):
    """Test case for get_organisations_id_applications_app_id_tags_0

    
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/v2/organisations/{id}/applications/{app_id}/tags'.format(id='id_example', app_id='app_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organisations_id_applications_app_id_vhosts_0(client):
    """Test case for get_organisations_id_applications_app_id_vhosts_0

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/organisations/{id}/applications/{app_id}/vhosts'.format(id='id_example', app_id='app_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organisations_id_applications_app_id_vhosts_favourite_0(client):
    """Test case for get_organisations_id_applications_app_id_vhosts_favourite_0

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/organisations/{id}/applications/{app_id}/vhosts/favourite'.format(id='id_example', app_id='app_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_self_addons_addon_id_applications_1(client):
    """Test case for get_self_addons_addon_id_applications_1

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/self/addons/{addon_id}/applications'.format(addon_id='addon_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_self_applications_0(client):
    """Test case for get_self_applications_0

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/self/applications',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_self_applications_app_id_0(client):
    """Test case for get_self_applications_app_id_0

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/self/applications/{app_id}'.format(app_id='app_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_self_applications_app_id_addons_1(client):
    """Test case for get_self_applications_app_id_addons_1

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/self/applications/{app_id}/addons'.format(app_id='app_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_self_applications_app_id_addons_env_1(client):
    """Test case for get_self_applications_app_id_addons_env_1

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/self/applications/{app_id}/addons/env'.format(app_id='app_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_self_applications_app_id_dependencies_0(client):
    """Test case for get_self_applications_app_id_dependencies_0

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/self/applications/{app_id}/dependencies'.format(app_id='app_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_self_applications_app_id_dependencies_dependency_id_0(client):
    """Test case for get_self_applications_app_id_dependencies_dependency_id_0

    
    """
    body = {"minInstances":6,"oauthAppId":"oauthAppId","oauthService":"oauthService","instanceType":"instanceType","cancelOnPush":False,"description":"description","favourite":False,"enabled":False,"shutdownable":False,"deploy":"deploy","instanceVariant":"instanceVariant","minFlavor":"minFlavor","separateBuild":False,"tags":["tags","tags"],"homogeneous":False,"archived":False,"oauthApp":{"owner":"owner","name":"name"},"instanceVersion":"instanceVersion","stickySessions":False,"zone":"zone","maxFlavor":"maxFlavor","name":"name","maxInstances":0}
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/v2/self/applications/{app_id}/dependencies/{dependency_id}'.format(dependency_id='dependency_id_example', app_id='app_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_self_applications_app_id_dependents_0(client):
    """Test case for get_self_applications_app_id_dependents_0

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/self/applications/{app_id}/dependents'.format(app_id='app_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_self_applications_app_id_deployments_0(client):
    """Test case for get_self_applications_app_id_deployments_0

    
    """
    params = [('limit', 'limit_example'),
                    ('offset', 'offset_example'),
                    ('action', 'action_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/self/applications/{app_id}/deployments'.format(app_id='app_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_self_applications_app_id_env_0(client):
    """Test case for get_self_applications_app_id_env_0

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/self/applications/{app_id}/env'.format(app_id='app_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_self_applications_app_id_instances_0(client):
    """Test case for get_self_applications_app_id_instances_0

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/self/applications/{app_id}/instances'.format(app_id='app_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_self_applications_app_id_tags_0(client):
    """Test case for get_self_applications_app_id_tags_0

    
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/v2/self/applications/{app_id}/tags'.format(app_id='app_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_self_applications_app_id_vhosts_0(client):
    """Test case for get_self_applications_app_id_vhosts_0

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/self/applications/{app_id}/vhosts'.format(app_id='app_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_self_applications_app_id_vhosts_favourite_0(client):
    """Test case for get_self_applications_app_id_vhosts_favourite_0

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/self/applications/{app_id}/vhosts/favourite'.format(app_id='app_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_users_id_applications_0(client):
    """Test case for get_users_id_applications_0

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/users/{id}/applications'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_organisations_id_applications_app_id_branch_put_0(client):
    """Test case for organisations_id_applications_app_id_branch_put_0

    
    """
    headers = { 
    }
    response = await client.request(
        method='PUT',
        path='/v2/organisations/{id}/applications/{app_id}/branch'.format(app_id='app_id_example', id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_organisations_id_applications_app_id_branches_get_0(client):
    """Test case for organisations_id_applications_app_id_branches_get_0

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/v2/organisations/{id}/applications/{app_id}/branches'.format(app_id='app_id_example', id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_organisations_id_applications_app_id_buildflavor_put_0(client):
    """Test case for organisations_id_applications_app_id_buildflavor_put_0

    
    """
    headers = { 
    }
    response = await client.request(
        method='PUT',
        path='/v2/organisations/{id}/applications/{app_id}/buildflavor'.format(app_id='app_id_example', id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_organisations_id_applications_app_id_dependencies_env_get_0(client):
    """Test case for organisations_id_applications_app_id_dependencies_env_get_0

    
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/v2/organisations/{id}/applications/{app_id}/dependencies/env'.format(app_id='app_id_example', id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_organisations_id_applications_app_id_deployments_deployment_id_get_0(client):
    """Test case for organisations_id_applications_app_id_deployments_deployment_id_get_0

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/v2/organisations/{id}/applications/{app_id}/deployments/{deployment_id}'.format(app_id='app_id_example', deployment_id='deployment_id_example', id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_organisations_id_applications_app_id_exposed_env_get_0(client):
    """Test case for organisations_id_applications_app_id_exposed_env_get_0

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/v2/organisations/{id}/applications/{app_id}/exposed_env'.format(app_id='app_id_example', id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_organisations_id_applications_app_id_exposed_env_put_0(client):
    """Test case for organisations_id_applications_app_id_exposed_env_put_0

    
    """
    headers = { 
    }
    response = await client.request(
        method='PUT',
        path='/v2/organisations/{id}/applications/{app_id}/exposed_env'.format(app_id='app_id_example', id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_organisations_id_applications_app_id_instances_instance_id_get_0(client):
    """Test case for organisations_id_applications_app_id_instances_instance_id_get_0

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/v2/organisations/{id}/applications/{app_id}/instances/{instance_id}'.format(instance_id='instance_id_example', app_id='app_id_example', id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_organisations_id_applications_0(client):
    """Test case for post_organisations_id_applications_0

    
    """
    body = {"minInstances":6,"oauthAppId":"oauthAppId","oauthService":"oauthService","instanceType":"instanceType","cancelOnPush":False,"description":"description","favourite":False,"enabled":False,"shutdownable":False,"deploy":"deploy","instanceVariant":"instanceVariant","minFlavor":"minFlavor","separateBuild":False,"tags":["tags","tags"],"homogeneous":False,"archived":False,"oauthApp":{"owner":"owner","name":"name"},"instanceVersion":"instanceVersion","stickySessions":False,"zone":"zone","maxFlavor":"maxFlavor","name":"name","maxInstances":0}
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v2/organisations/{id}/applications'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_organisations_id_applications_app_id_addons_1(client):
    """Test case for post_organisations_id_applications_app_id_addons_1

    
    """
    body = {"body":"body"}
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v2/organisations/{id}/applications/{app_id}/addons'.format(id='id_example', app_id='app_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_organisations_id_applications_app_id_instances_0(client):
    """Test case for post_organisations_id_applications_app_id_instances_0

    
    """
    params = [('commit', 'commit_example')]
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/v2/organisations/{id}/applications/{app_id}/instances'.format(id='id_example', app_id='app_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_self_applications_0(client):
    """Test case for post_self_applications_0

    
    """
    body = {"minInstances":6,"oauthAppId":"oauthAppId","oauthService":"oauthService","instanceType":"instanceType","cancelOnPush":False,"description":"description","favourite":False,"enabled":False,"shutdownable":False,"deploy":"deploy","instanceVariant":"instanceVariant","minFlavor":"minFlavor","separateBuild":False,"tags":["tags","tags"],"homogeneous":False,"archived":False,"oauthApp":{"owner":"owner","name":"name"},"instanceVersion":"instanceVersion","stickySessions":False,"zone":"zone","maxFlavor":"maxFlavor","name":"name","maxInstances":0}
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v2/self/applications',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_self_applications_app_id_addons_1(client):
    """Test case for post_self_applications_app_id_addons_1

    
    """
    body = {"body":"body"}
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v2/self/applications/{app_id}/addons'.format(app_id='app_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_self_applications_app_id_instances_0(client):
    """Test case for post_self_applications_app_id_instances_0

    
    """
    params = [('commit', 'commit_example')]
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/v2/self/applications/{app_id}/instances'.format(app_id='app_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_put_organisations_id_applications_app_id_0(client):
    """Test case for put_organisations_id_applications_app_id_0

    
    """
    body = {"minInstances":6,"oauthAppId":"oauthAppId","oauthService":"oauthService","instanceType":"instanceType","cancelOnPush":False,"description":"description","favourite":False,"enabled":False,"shutdownable":False,"deploy":"deploy","instanceVariant":"instanceVariant","minFlavor":"minFlavor","separateBuild":False,"tags":["tags","tags"],"homogeneous":False,"archived":False,"oauthApp":{"owner":"owner","name":"name"},"instanceVersion":"instanceVersion","stickySessions":False,"zone":"zone","maxFlavor":"maxFlavor","name":"name","maxInstances":0}
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/v2/organisations/{id}/applications/{app_id}'.format(id='id_example', app_id='app_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_put_organisations_id_applications_app_id_dependencies_dependency_id_0(client):
    """Test case for put_organisations_id_applications_app_id_dependencies_dependency_id_0

    
    """
    body = {"body":"body"}
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/v2/organisations/{id}/applications/{app_id}/dependencies/{dependency_id}'.format(dependency_id='dependency_id_example', app_id='app_id_example', id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_put_organisations_id_applications_app_id_env_0(client):
    """Test case for put_organisations_id_applications_app_id_env_0

    
    """
    body = {"name":"name","value":"value"}
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/v2/organisations/{id}/applications/{app_id}/env'.format(id='id_example', app_id='app_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_put_organisations_id_applications_app_id_env_env_name_0(client):
    """Test case for put_organisations_id_applications_app_id_env_env_name_0

    
    """
    body = {"name":"name","value":"value"}
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/v2/organisations/{id}/applications/{app_id}/env/{env_name}'.format(id='id_example', app_id='app_id_example', env_name='env_name_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_put_organisations_id_applications_app_id_tags_tag_0(client):
    """Test case for put_organisations_id_applications_app_id_tags_tag_0

    
    """
    body = {"body":"body"}
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/v2/organisations/{id}/applications/{app_id}/tags/{tag}'.format(id='id_example', app_id='app_id_example', tag='tag_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_put_organisations_id_applications_app_id_vhosts_domain_0(client):
    """Test case for put_organisations_id_applications_app_id_vhosts_domain_0

    
    """
    body = {"fqdn":"fqdn"}
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/v2/organisations/{id}/applications/{app_id}/vhosts/{domain}'.format(id='id_example', app_id='app_id_example', domain='domain_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_put_organisations_id_applications_app_id_vhosts_favourite_0(client):
    """Test case for put_organisations_id_applications_app_id_vhosts_favourite_0

    
    """
    body = {"fqdn":"fqdn"}
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/v2/organisations/{id}/applications/{app_id}/vhosts/favourite'.format(id='id_example', app_id='app_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_put_self_applications_app_id_0(client):
    """Test case for put_self_applications_app_id_0

    
    """
    body = {"minInstances":6,"oauthAppId":"oauthAppId","oauthService":"oauthService","instanceType":"instanceType","cancelOnPush":False,"description":"description","favourite":False,"enabled":False,"shutdownable":False,"deploy":"deploy","instanceVariant":"instanceVariant","minFlavor":"minFlavor","separateBuild":False,"tags":["tags","tags"],"homogeneous":False,"archived":False,"oauthApp":{"owner":"owner","name":"name"},"instanceVersion":"instanceVersion","stickySessions":False,"zone":"zone","maxFlavor":"maxFlavor","name":"name","maxInstances":0}
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/v2/self/applications/{app_id}'.format(app_id='app_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_put_self_applications_app_id_env_0(client):
    """Test case for put_self_applications_app_id_env_0

    
    """
    body = {"name":"name","value":"value"}
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/v2/self/applications/{app_id}/env'.format(app_id='app_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_put_self_applications_app_id_env_env_name_0(client):
    """Test case for put_self_applications_app_id_env_env_name_0

    
    """
    body = {"name":"name","value":"value"}
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/v2/self/applications/{app_id}/env/{env_name}'.format(app_id='app_id_example', env_name='env_name_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_put_self_applications_app_id_tags_tag_0(client):
    """Test case for put_self_applications_app_id_tags_tag_0

    
    """
    body = {"body":"body"}
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/v2/self/applications/{app_id}/tags/{tag}'.format(app_id='app_id_example', tag='tag_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_put_self_applications_app_id_vhosts_domain_0(client):
    """Test case for put_self_applications_app_id_vhosts_domain_0

    
    """
    body = {"fqdn":"fqdn"}
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/v2/self/applications/{app_id}/vhosts/{domain}'.format(app_id='app_id_example', domain='domain_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_put_self_applications_app_id_vhosts_favourite_0(client):
    """Test case for put_self_applications_app_id_vhosts_favourite_0

    
    """
    body = {"fqdn":"fqdn"}
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/v2/self/applications/{app_id}/vhosts/favourite'.format(app_id='app_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_self_applications_app_id_branch_put_0(client):
    """Test case for self_applications_app_id_branch_put_0

    
    """
    headers = { 
    }
    response = await client.request(
        method='PUT',
        path='/v2/self/applications/{app_id}/branch'.format(app_id='app_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_self_applications_app_id_branches_get_0(client):
    """Test case for self_applications_app_id_branches_get_0

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/v2/self/applications/{app_id}/branches'.format(app_id='app_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_self_applications_app_id_buildflavor_put_0(client):
    """Test case for self_applications_app_id_buildflavor_put_0

    
    """
    headers = { 
    }
    response = await client.request(
        method='PUT',
        path='/v2/self/applications/{app_id}/buildflavor'.format(app_id='app_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_self_applications_app_id_dependencies_env_get_0(client):
    """Test case for self_applications_app_id_dependencies_env_get_0

    
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/v2/self/applications/{app_id}/dependencies/env'.format(app_id='app_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_self_applications_app_id_deployments_deployment_id_get_0(client):
    """Test case for self_applications_app_id_deployments_deployment_id_get_0

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/v2/self/applications/{app_id}/deployments/{deployment_id}'.format(app_id='app_id_example', deployment_id='deployment_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_self_applications_app_id_exposed_env_get_0(client):
    """Test case for self_applications_app_id_exposed_env_get_0

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/v2/self/applications/{app_id}/exposed_env'.format(app_id='app_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_self_applications_app_id_exposed_env_put_0(client):
    """Test case for self_applications_app_id_exposed_env_put_0

    
    """
    headers = { 
    }
    response = await client.request(
        method='PUT',
        path='/v2/self/applications/{app_id}/exposed_env'.format(app_id='app_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_self_applications_app_id_instances_instance_id_get_0(client):
    """Test case for self_applications_app_id_instances_instance_id_get_0

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/v2/self/applications/{app_id}/instances/{instance_id}'.format(instance_id='instance_id_example', app_id='app_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

