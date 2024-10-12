# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.addon import Addon
from openapi_server.models.addon_migration import AddonMigration
from openapi_server.models.application import Application
from openapi_server.models.body import Body
from openapi_server.models.env import Env
from openapi_server.models.list_env import ListEnv
from openapi_server.models.organisations_id_addons_addon_id_migrations_post_request import OrganisationsIdAddonsAddonIdMigrationsPostRequest
from openapi_server.models.sso import Sso
from openapi_server.models.supernova_instance_view import SupernovaInstanceView
from openapi_server.models.wannabe_addon import WannabeAddon
from openapi_server.models.wannabe_plan import WannabePlan


pytestmark = pytest.mark.asyncio

async def test_delete_organisations_id_addons_addon_id_0(client):
    """Test case for delete_organisations_id_addons_addon_id_0

    
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/v2/organisations/{id}/addons/{addon_id}'.format(id='id_example', addon_id='addon_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_organisations_id_addons_addon_id_tags_tag_0(client):
    """Test case for delete_organisations_id_addons_addon_id_tags_tag_0

    
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/v2/organisations/{id}/addons/{addon_id}/tags/{tag}'.format(id='id_example', tag='tag_example', addon_id='addon_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_organisations_id_applications_app_id_addons_addon_id_0(client):
    """Test case for delete_organisations_id_applications_app_id_addons_addon_id_0

    
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

async def test_delete_self_addons_addon_id_0(client):
    """Test case for delete_self_addons_addon_id_0

    
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/v2/self/addons/{addon_id}'.format(addon_id='addon_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_self_addons_addon_id_tags_tag_0(client):
    """Test case for delete_self_addons_addon_id_tags_tag_0

    
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/v2/self/addons/{addon_id}/tags/{tag}'.format(tag='tag_example', addon_id='addon_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_self_applications_app_id_addons_addon_id_0(client):
    """Test case for delete_self_applications_app_id_addons_addon_id_0

    
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

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_get_config_provider_0(client):
    """Test case for get_config_provider_0

    Get Addon provider configuration
    """
    body = 'body_example'
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/v4/addon-providers/config-provider/addons/{configuration_provider_id}'.format(configuration_provider_id='configuration_provider_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_get_config_provider_env_0(client):
    """Test case for get_config_provider_env_0

    Get provider's addon environment
    """
    body = 'body_example'
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/v4/addon-providers/config-provider/addons/{configuration_provider_id}/env'.format(configuration_provider_id='configuration_provider_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_get_matomo_0(client):
    """Test case for get_matomo_0

    Get Matomo addon
    """
    body = 'body_example'
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/v4/addon-providers/addon-matomo/addons/{matomo_id}'.format(matomo_id='matomo_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organisations_id_addons_0(client):
    """Test case for get_organisations_id_addons_0

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/organisations/{id}/addons'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organisations_id_addons_addon_id_0(client):
    """Test case for get_organisations_id_addons_addon_id_0

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/organisations/{id}/addons/{addon_id}'.format(id='id_example', addon_id='addon_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organisations_id_addons_addon_id_applications_0(client):
    """Test case for get_organisations_id_addons_addon_id_applications_0

    
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

async def test_get_organisations_id_addons_addon_id_env_0(client):
    """Test case for get_organisations_id_addons_addon_id_env_0

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/organisations/{id}/addons/{addon_id}/env'.format(id='id_example', addon_id='addon_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organisations_id_addons_addon_id_tags_0(client):
    """Test case for get_organisations_id_addons_addon_id_tags_0

    
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/v2/organisations/{id}/addons/{addon_id}/tags'.format(id='id_example', addon_id='addon_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organisations_id_applications_app_id_addons_0(client):
    """Test case for get_organisations_id_applications_app_id_addons_0

    
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

async def test_get_organisations_id_applications_app_id_addons_env_0(client):
    """Test case for get_organisations_id_applications_app_id_addons_env_0

    
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

async def test_get_self_addons_0(client):
    """Test case for get_self_addons_0

    Addon
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/self/addons',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_self_addons_addon_id_0(client):
    """Test case for get_self_addons_addon_id_0

    Specific addon
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/self/addons/{addon_id}'.format(addon_id='addon_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_self_addons_addon_id_applications_0(client):
    """Test case for get_self_addons_addon_id_applications_0

    
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

async def test_get_self_addons_addon_id_env_0(client):
    """Test case for get_self_addons_addon_id_env_0

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/self/addons/{addon_id}/env'.format(addon_id='addon_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_self_addons_addon_id_sso_0(client):
    """Test case for get_self_addons_addon_id_sso_0

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/self/addons/{addon_id}/sso'.format(addon_id='addon_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_self_addons_addon_id_tags_0(client):
    """Test case for get_self_addons_addon_id_tags_0

    
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/v2/self/addons/{addon_id}/tags'.format(addon_id='addon_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_self_applications_app_id_addons_0(client):
    """Test case for get_self_applications_app_id_addons_0

    
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

async def test_get_self_applications_app_id_addons_env_0(client):
    """Test case for get_self_applications_app_id_addons_env_0

    
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

async def test_organisations_id_addons_addon_id_instances_get_0(client):
    """Test case for organisations_id_addons_addon_id_instances_get_0

    List instances for this add-on.
    """
    params = [('deploymentId', 'deployment_id_example'),
                    ('withDeleted', 'with_deleted_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/organisations/{id}/addons/{addon_id}/instances'.format(id='id_example', addon_id='addon_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_organisations_id_addons_addon_id_instances_instance_id_get_0(client):
    """Test case for organisations_id_addons_addon_id_instances_instance_id_get_0

    Get a specific instance for {addonId}
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/organisations/{id}/addons/{addon_id}/instances/{instance_id}'.format(instance_id='instance_id_example', id='id_example', addon_id='addon_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_organisations_id_addons_addon_id_migrations_get_0(client):
    """Test case for organisations_id_addons_addon_id_migrations_get_0

    Get past migrations from add-on.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/organisations/{id}/addons/{addon_id}/migrations'.format(id='id_example', addon_id='addon_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_organisations_id_addons_addon_id_migrations_migration_id_get_0(client):
    """Test case for organisations_id_addons_addon_id_migrations_migration_id_get_0

    Get a given migration
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/organisations/{id}/addons/{addon_id}/migrations/{migration_id}'.format(migration_id='migration_id_example', id='id_example', addon_id='addon_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_organisations_id_addons_addon_id_migrations_post_0(client):
    """Test case for organisations_id_addons_addon_id_migrations_post_0

    Start a new add-on migration
    """
    body = openapi_server.OrganisationsIdAddonsAddonIdMigrationsPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v2/organisations/{id}/addons/{addon_id}/migrations'.format(id='id_example', addon_id='addon_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_organisations_id_addons_addon_id_sso_get_0(client):
    """Test case for organisations_id_addons_addon_id_sso_get_0

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/organisations/{id}/addons/{addon_id}/sso'.format(id='id_example', addon_id='addon_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_organisations_id_addons_preorders_post_0(client):
    """Test case for organisations_id_addons_preorders_post_0

    
    """
    body = {"providerId":"providerId","name":"name","payment":{"deviceData":"deviceData","type":"NEW_CARD","token":"token"},"region":"region","plan":"plan"}
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v2/organisations/{id}/addons/preorders'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_organisations_id_addons_0(client):
    """Test case for post_organisations_id_addons_0

    
    """
    body = {"providerId":"providerId","name":"name","payment":{"deviceData":"deviceData","type":"NEW_CARD","token":"token"},"region":"region","plan":"plan"}
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v2/organisations/{id}/addons'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_organisations_id_applications_app_id_addons_0(client):
    """Test case for post_organisations_id_applications_app_id_addons_0

    
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

async def test_post_self_addons_0(client):
    """Test case for post_self_addons_0

    
    """
    body = {"providerId":"providerId","name":"name","payment":{"deviceData":"deviceData","type":"NEW_CARD","token":"token"},"region":"region","plan":"plan"}
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v2/self/addons',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_self_applications_app_id_addons_0(client):
    """Test case for post_self_applications_app_id_addons_0

    
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

async def test_put_organisations_id_addons_addon_id_0(client):
    """Test case for put_organisations_id_addons_addon_id_0

    
    """
    body = {"providerId":"providerId","name":"name","payment":{"deviceData":"deviceData","type":"NEW_CARD","token":"token"},"region":"region","plan":"plan"}
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/v2/organisations/{id}/addons/{addon_id}'.format(id='id_example', addon_id='addon_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_put_organisations_id_addons_addon_id_tags_tag_0(client):
    """Test case for put_organisations_id_addons_addon_id_tags_tag_0

    
    """
    body = {"body":"body"}
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/v2/organisations/{id}/addons/{addon_id}/tags/{tag}'.format(id='id_example', tag='tag_example', addon_id='addon_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_put_self_addons_addon_id_0(client):
    """Test case for put_self_addons_addon_id_0

    
    """
    body = {"providerId":"providerId","name":"name","payment":{"deviceData":"deviceData","type":"NEW_CARD","token":"token"},"region":"region","plan":"plan"}
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/v2/self/addons/{addon_id}'.format(addon_id='addon_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_put_self_addons_addon_id_plan_0(client):
    """Test case for put_self_addons_addon_id_plan_0

    
    """
    body = {"features":[{"name":"name","type":"type","value":"value"},{"name":"name","type":"type","value":"value"}],"price":0,"name":"name","slug":"slug"}
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/v2/self/addons/{addon_id}/plan'.format(addon_id='addon_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_put_self_addons_addon_id_tags_tag_0(client):
    """Test case for put_self_addons_addon_id_tags_tag_0

    
    """
    body = {"body":"body"}
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/v2/self/addons/{addon_id}/tags/{tag}'.format(tag='tag_example', addon_id='addon_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_self_addons_preorders_post_0(client):
    """Test case for self_addons_preorders_post_0

    
    """
    body = {"providerId":"providerId","name":"name","payment":{"deviceData":"deviceData","type":"NEW_CARD","token":"token"},"region":"region","plan":"plan"}
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v2/self/addons/preorders',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_config_provider_env_0(client):
    """Test case for update_config_provider_env_0

    Update provider's addon environment
    """
    body = None
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/v2/v4/addon-providers/config-provider/addons/{configuration_provider_id}/env'.format(configuration_provider_id='configuration_provider_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_vendor_addons_post_0(client):
    """Test case for vendor_addons_post_0

    
    """
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/v2/vendor//addons',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

