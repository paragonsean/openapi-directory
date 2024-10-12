# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.addon import Addon
from openapi_server.models.addon_migration import AddonMigration
from openapi_server.models.addon_provider_sso import AddonProviderSso
from openapi_server.models.app_instance import AppInstance
from openapi_server.models.application import Application
from openapi_server.models.body import Body
from openapi_server.models.conso import Conso
from openapi_server.models.consumer import Consumer
from openapi_server.models.credits import Credits
from openapi_server.models.deployment import Deployment
from openapi_server.models.deployment_summary import DeploymentSummary
from openapi_server.models.env import Env
from openapi_server.models.error import Error
from openapi_server.models.feature import Feature
from openapi_server.models.linked_app_env import LinkedAppEnv
from openapi_server.models.list_env import ListEnv
from openapi_server.models.organisation import Organisation
from openapi_server.models.organisations_id_addons_addon_id_migrations_post_request import OrganisationsIdAddonsAddonIdMigrationsPostRequest
from openapi_server.models.payment_data import PaymentData
from openapi_server.models.plan import Plan
from openapi_server.models.provider import Provider
from openapi_server.models.schema1 import Schema1
from openapi_server.models.schema2 import Schema2
from openapi_server.models.secret import Secret
from openapi_server.models.sso import Sso
from openapi_server.models.supernova_instance_view import SupernovaInstanceView
from openapi_server.models.vhost import Vhost
from openapi_server.models.wannabe_addon import WannabeAddon
from openapi_server.models.wannabe_addon_provider import WannabeAddonProvider
from openapi_server.models.wannabe_application import WannabeApplication
from openapi_server.models.wannabe_consumer import WannabeConsumer
from openapi_server.models.wannabe_env import WannabeEnv
from openapi_server.models.wannabe_feature import WannabeFeature
from openapi_server.models.wannabe_organisation import WannabeOrganisation
from openapi_server.models.wannabe_plan import WannabePlan
from openapi_server.models.wannabe_plan_feature import WannabePlanFeature


pytestmark = pytest.mark.asyncio

async def test_create_network_group_0(client):
    """Test case for create_network_group_0

    Create Network Group
    """
    body = None
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v2/v4/networkgroups/organisations/{owner_id}/networkgroups'.format(owner_id='owner_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_network_group_external_peer_0(client):
    """Test case for create_network_group_external_peer_0

    Add external peer
    """
    body = None
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v2/v4/networkgroups/organisations/{owner_id}/networkgroups/{network_group_id}/external-peers'.format(owner_id='owner_id_example', network_group_id='network_group_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_network_group_member_0(client):
    """Test case for create_network_group_member_0

    Add member
    """
    body = openapi_server.Schema2()
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v2/v4/networkgroups/organisations/{owner_id}/networkgroups/{network_group_id}/members'.format(owner_id='owner_id_example', network_group_id='network_group_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_delete_network_group_0(client):
    """Test case for delete_network_group_0

    Delete Network Group
    """
    body = None
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/v2/v4/networkgroups/organisations/{owner_id}/networkgroups/{network_group_id}'.format(owner_id='owner_id_example', network_group_id='network_group_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_delete_network_group_external_peer_0(client):
    """Test case for delete_network_group_external_peer_0

    Remove external peer
    """
    body = None
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/v2/v4/networkgroups/organisations/{owner_id}/networkgroups/{network_group_id}/external-peers/{peer_id}'.format(owner_id='owner_id_example', network_group_id='network_group_id_example', peer_id='peer_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_delete_network_group_member_0(client):
    """Test case for delete_network_group_member_0

    Remove member
    """
    body = None
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/v2/v4/networkgroups/organisations/{owner_id}/networkgroups/{network_group_id}/members/{member_id}'.format(owner_id='owner_id_example', network_group_id='network_group_id_example', member_id='member_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_delete_network_group_peer_0(client):
    """Test case for delete_network_group_peer_0

    Remove peer
    """
    body = None
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/v2/v4/networkgroups/organisations/{owner_id}/networkgroups/{network_group_id}/peers/{peer_id}'.format(owner_id='owner_id_example', network_group_id='network_group_id_example', peer_id='peer_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_organisations_id_0(client):
    """Test case for delete_organisations_id_0

    
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/v2/organisations/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_organisations_id_addonproviders_provider_id_features_feature_id_0(client):
    """Test case for delete_organisations_id_addonproviders_provider_id_features_feature_id_0

    
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/v2/organisations/{id}/addonproviders/{provider_id}/features/{feature_id}'.format(id='id_example', feature_id='feature_id_example', provider_id='provider_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_organisations_id_addonproviders_provider_id_plans_plan_id_0(client):
    """Test case for delete_organisations_id_addonproviders_provider_id_plans_plan_id_0

    
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/v2/organisations/{id}/addonproviders/{provider_id}/plans/{plan_id}'.format(id='id_example', provider_id='provider_id_example', plan_id='plan_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_organisations_id_addonproviders_provider_id_plans_plan_id_features_feature_name_0(client):
    """Test case for delete_organisations_id_addonproviders_provider_id_plans_plan_id_features_feature_name_0

    
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/v2/organisations/{id}/addonproviders/{provider_id}/plans/{plan_id}/features/{feature_name}'.format(id='id_example', feature_name='feature_name_example', provider_id='provider_id_example', plan_id='plan_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_organisations_id_addons_addon_id_1(client):
    """Test case for delete_organisations_id_addons_addon_id_1

    
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

async def test_delete_organisations_id_addons_addon_id_tags_tag_1(client):
    """Test case for delete_organisations_id_addons_addon_id_tags_tag_1

    
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

async def test_delete_organisations_id_applications_app_id_1(client):
    """Test case for delete_organisations_id_applications_app_id_1

    
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

async def test_delete_organisations_id_applications_app_id_addons_addon_id_2(client):
    """Test case for delete_organisations_id_applications_app_id_addons_addon_id_2

    
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

async def test_delete_organisations_id_applications_app_id_dependencies_dependency_id_1(client):
    """Test case for delete_organisations_id_applications_app_id_dependencies_dependency_id_1

    
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

async def test_delete_organisations_id_applications_app_id_deployments_deployment_id_instances_1(client):
    """Test case for delete_organisations_id_applications_app_id_deployments_deployment_id_instances_1

    
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

async def test_delete_organisations_id_applications_app_id_env_env_name_1(client):
    """Test case for delete_organisations_id_applications_app_id_env_env_name_1

    
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

async def test_delete_organisations_id_applications_app_id_instances_1(client):
    """Test case for delete_organisations_id_applications_app_id_instances_1

    
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

async def test_delete_organisations_id_applications_app_id_tags_tag_1(client):
    """Test case for delete_organisations_id_applications_app_id_tags_tag_1

    
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

async def test_delete_organisations_id_applications_app_id_vhosts_domain_1(client):
    """Test case for delete_organisations_id_applications_app_id_vhosts_domain_1

    
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

async def test_delete_organisations_id_applications_app_id_vhosts_favourite_1(client):
    """Test case for delete_organisations_id_applications_app_id_vhosts_favourite_1

    
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

async def test_delete_organisations_id_consumers_key_0(client):
    """Test case for delete_organisations_id_consumers_key_0

    
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/v2/organisations/{id}/consumers/{key}'.format(id='id_example', key='key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_organisations_id_members_user_id_0(client):
    """Test case for delete_organisations_id_members_user_id_0

    
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/v2/organisations/{id}/members/{user_id}'.format(id='id_example', user_id='user_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_organisations_id_payments_billings_bid_0(client):
    """Test case for delete_organisations_id_payments_billings_bid_0

    
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/v2/organisations/{id}/payments/billings/{bid}'.format(id='id_example', bid='bid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_organisations_id_payments_recurring_0(client):
    """Test case for delete_organisations_id_payments_recurring_0

    
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/v2/organisations/{id}/payments/recurring'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_get_network_group_0(client):
    """Test case for get_network_group_0

    Get Network Group
    """
    body = None
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/v4/networkgroups/organisations/{owner_id}/networkgroups/{network_group_id}'.format(owner_id='owner_id_example', network_group_id='network_group_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_get_network_group_member_0(client):
    """Test case for get_network_group_member_0

    Get member
    """
    body = None
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/v4/networkgroups/organisations/{owner_id}/networkgroups/{network_group_id}/members/{member_id}'.format(owner_id='owner_id_example', network_group_id='network_group_id_example', member_id='member_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_get_network_group_peer_0(client):
    """Test case for get_network_group_peer_0

    Get peer
    """
    body = None
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/v4/networkgroups/organisations/{owner_id}/networkgroups/{network_group_id}/peers/{peer_id}'.format(owner_id='owner_id_example', network_group_id='network_group_id_example', peer_id='peer_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_get_network_group_stream_0(client):
    """Test case for get_network_group_stream_0

    Network Group SSE
    """
    body = None
    headers = { 
        'Accept': 'text/event-stream',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/v4/networkgroups/organisations/{owner_id}/networkgroups/{network_group_id}/stream'.format(owner_id='owner_id_example', network_group_id='network_group_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_get_network_group_wire_guard_configuration_0(client):
    """Test case for get_network_group_wire_guard_configuration_0

    Get WireGuard® configuration
    """
    body = None
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/v4/networkgroups/organisations/{owner_id}/networkgroups/{network_group_id}/peers/{peer_id}/wireguard/configuration'.format(owner_id='owner_id_example', network_group_id='network_group_id_example', peer_id='peer_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_get_network_group_wire_guard_configuration_stream_0(client):
    """Test case for get_network_group_wire_guard_configuration_stream_0

    Get WireGuard® configuration
    """
    body = None
    headers = { 
        'Accept': 'text/event-stream',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/v4/networkgroups/organisations/{owner_id}/networkgroups/{network_group_id}/peers/{peer_id}/wireguard/configuration/stream'.format(owner_id='owner_id_example', network_group_id='network_group_id_example', peer_id='peer_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organisations_0(client):
    """Test case for get_organisations_0

    
    """
    params = [('user', 'user_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/organisations',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organisations_id_0(client):
    """Test case for get_organisations_id_0

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/organisations/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organisations_id_addonproviders_0(client):
    """Test case for get_organisations_id_addonproviders_0

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/organisations/{id}/addonproviders'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organisations_id_addonproviders_provider_id_0(client):
    """Test case for get_organisations_id_addonproviders_provider_id_0

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/organisations/{id}/addonproviders/{provider_id}'.format(id='id_example', provider_id='provider_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organisations_id_addonproviders_provider_id_features_0(client):
    """Test case for get_organisations_id_addonproviders_provider_id_features_0

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/organisations/{id}/addonproviders/{provider_id}/features'.format(id='id_example', provider_id='provider_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organisations_id_addonproviders_provider_id_plans_0(client):
    """Test case for get_organisations_id_addonproviders_provider_id_plans_0

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/organisations/{id}/addonproviders/{provider_id}/plans'.format(id='id_example', provider_id='provider_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organisations_id_addonproviders_provider_id_plans_plan_id_0(client):
    """Test case for get_organisations_id_addonproviders_provider_id_plans_plan_id_0

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/organisations/{id}/addonproviders/{provider_id}/plans/{plan_id}'.format(id='id_example', provider_id='provider_id_example', plan_id='plan_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organisations_id_addonproviders_provider_id_tags_0(client):
    """Test case for get_organisations_id_addonproviders_provider_id_tags_0

    
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/v2/organisations/{id}/addonproviders/{provider_id}/tags'.format(id='id_example', provider_id='provider_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organisations_id_addons_1(client):
    """Test case for get_organisations_id_addons_1

    
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

async def test_get_organisations_id_addons_addon_id_1(client):
    """Test case for get_organisations_id_addons_addon_id_1

    
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

async def test_get_organisations_id_addons_addon_id_applications_2(client):
    """Test case for get_organisations_id_addons_addon_id_applications_2

    
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

async def test_get_organisations_id_addons_addon_id_env_1(client):
    """Test case for get_organisations_id_addons_addon_id_env_1

    
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

async def test_get_organisations_id_addons_addon_id_sso_0(client):
    """Test case for get_organisations_id_addons_addon_id_sso_0

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/organisations/{id}/addonproviders/{provider_id}/sso'.format(provider_id='provider_id_example', id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organisations_id_addons_addon_id_tags_1(client):
    """Test case for get_organisations_id_addons_addon_id_tags_1

    
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

async def test_get_organisations_id_applications_1(client):
    """Test case for get_organisations_id_applications_1

    
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

async def test_get_organisations_id_applications_app_id_1(client):
    """Test case for get_organisations_id_applications_app_id_1

    
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

async def test_get_organisations_id_applications_app_id_addons_2(client):
    """Test case for get_organisations_id_applications_app_id_addons_2

    
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

async def test_get_organisations_id_applications_app_id_addons_env_2(client):
    """Test case for get_organisations_id_applications_app_id_addons_env_2

    
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

async def test_get_organisations_id_applications_app_id_dependencies_1(client):
    """Test case for get_organisations_id_applications_app_id_dependencies_1

    
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

async def test_get_organisations_id_applications_app_id_dependents_1(client):
    """Test case for get_organisations_id_applications_app_id_dependents_1

    
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

async def test_get_organisations_id_applications_app_id_deployments_1(client):
    """Test case for get_organisations_id_applications_app_id_deployments_1

    
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

async def test_get_organisations_id_applications_app_id_env_1(client):
    """Test case for get_organisations_id_applications_app_id_env_1

    
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

async def test_get_organisations_id_applications_app_id_instances_1(client):
    """Test case for get_organisations_id_applications_app_id_instances_1

    
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

async def test_get_organisations_id_applications_app_id_tags_1(client):
    """Test case for get_organisations_id_applications_app_id_tags_1

    
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

async def test_get_organisations_id_applications_app_id_vhosts_1(client):
    """Test case for get_organisations_id_applications_app_id_vhosts_1

    
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

async def test_get_organisations_id_applications_app_id_vhosts_favourite_1(client):
    """Test case for get_organisations_id_applications_app_id_vhosts_favourite_1

    
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

async def test_get_organisations_id_consumers_0(client):
    """Test case for get_organisations_id_consumers_0

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/organisations/{id}/consumers'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organisations_id_consumers_key_0(client):
    """Test case for get_organisations_id_consumers_key_0

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/organisations/{id}/consumers/{key}'.format(id='id_example', key='key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organisations_id_consumers_key_secret_0(client):
    """Test case for get_organisations_id_consumers_key_secret_0

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/organisations/{id}/consumers/{key}/secret'.format(id='id_example', key='key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organisations_id_consumptions_0(client):
    """Test case for get_organisations_id_consumptions_0

    
    """
    params = [('appId', 'app_id_example'),
                    ('from', '_from_example'),
                    ('to', 'to_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/organisations/{id}/consumptions'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organisations_id_credits_0(client):
    """Test case for get_organisations_id_credits_0

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/organisations/{id}/credits'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organisations_id_deployments_0(client):
    """Test case for get_organisations_id_deployments_0

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/organisations/{id}/deployments'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organisations_id_instances_0(client):
    """Test case for get_organisations_id_instances_0

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/organisations/{id}/instances'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organisations_id_members_0(client):
    """Test case for get_organisations_id_members_0

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/organisations/{id}/members'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organisations_id_payment_info_0(client):
    """Test case for get_organisations_id_payment_info_0

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/v2/organisations/{id}/payment-info'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organisations_id_payments_billings_0(client):
    """Test case for get_organisations_id_payments_billings_0

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/v2/organisations/{id}/payments/billings'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organisations_id_payments_billings_bid_0(client):
    """Test case for get_organisations_id_payments_billings_bid_0

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/v2/organisations/{id}/payments/billings/{bid}'.format(id='id_example', bid='bid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organisations_id_payments_billings_bid_pdf_0(client):
    """Test case for get_organisations_id_payments_billings_bid_pdf_0

    
    """
    params = [('token', 'token_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/v2/organisations/{id}/payments/billings/{bid_pd}'.format(id='id_example', bid='bid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organisations_id_payments_full_price_price_0(client):
    """Test case for get_organisations_id_payments_full_price_price_0

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/v2/organisations/{id}/payments/fullprice/{price}'.format(id='id_example', price='price_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_list_network_group_members_0(client):
    """Test case for list_network_group_members_0

    List members
    """
    body = None
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/v4/networkgroups/organisations/{owner_id}/networkgroups/{network_group_id}/members'.format(owner_id='owner_id_example', network_group_id='network_group_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_list_network_group_peers_0(client):
    """Test case for list_network_group_peers_0

    List peers
    """
    body = None
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/v4/networkgroups/organisations/{owner_id}/networkgroups/{network_group_id}/peers'.format(owner_id='owner_id_example', network_group_id='network_group_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_list_network_groups_0(client):
    """Test case for list_network_groups_0

    List Network Groups
    """
    body = None
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/v4/networkgroups/organisations/{owner_id}/networkgroups'.format(owner_id='owner_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_organisations_id_addonproviders_provider_id_delete_0(client):
    """Test case for organisations_id_addonproviders_provider_id_delete_0

    Remove an add-on provider
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/v2/organisations/{id}/addonproviders/{provider_id}'.format(id='id_example', provider_id='provider_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_organisations_id_addons_addon_id_instances_get_1(client):
    """Test case for organisations_id_addons_addon_id_instances_get_1

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

async def test_organisations_id_addons_addon_id_instances_instance_id_get_1(client):
    """Test case for organisations_id_addons_addon_id_instances_instance_id_get_1

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

async def test_organisations_id_addons_addon_id_migrations_get_1(client):
    """Test case for organisations_id_addons_addon_id_migrations_get_1

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

async def test_organisations_id_addons_addon_id_migrations_migration_id_get_1(client):
    """Test case for organisations_id_addons_addon_id_migrations_migration_id_get_1

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

async def test_organisations_id_addons_addon_id_migrations_post_1(client):
    """Test case for organisations_id_addons_addon_id_migrations_post_1

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

async def test_organisations_id_addons_addon_id_sso_get_1(client):
    """Test case for organisations_id_addons_addon_id_sso_get_1

    
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

async def test_organisations_id_addons_preorders_post_1(client):
    """Test case for organisations_id_addons_preorders_post_1

    
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

async def test_organisations_id_applications_app_id_branch_put_1(client):
    """Test case for organisations_id_applications_app_id_branch_put_1

    
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

async def test_organisations_id_applications_app_id_branches_get_1(client):
    """Test case for organisations_id_applications_app_id_branches_get_1

    
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

async def test_organisations_id_applications_app_id_buildflavor_put_1(client):
    """Test case for organisations_id_applications_app_id_buildflavor_put_1

    
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

async def test_organisations_id_applications_app_id_dependencies_env_get_1(client):
    """Test case for organisations_id_applications_app_id_dependencies_env_get_1

    
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

async def test_organisations_id_applications_app_id_deployments_deployment_id_get_1(client):
    """Test case for organisations_id_applications_app_id_deployments_deployment_id_get_1

    
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

async def test_organisations_id_applications_app_id_exposed_env_get_1(client):
    """Test case for organisations_id_applications_app_id_exposed_env_get_1

    
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

async def test_organisations_id_applications_app_id_exposed_env_put_1(client):
    """Test case for organisations_id_applications_app_id_exposed_env_put_1

    
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

async def test_organisations_id_applications_app_id_instances_instance_id_get_1(client):
    """Test case for organisations_id_applications_app_id_instances_instance_id_get_1

    
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

async def test_organisations_id_payments_billings_unpaid_get_0(client):
    """Test case for organisations_id_payments_billings_unpaid_get_0

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/v2/organisations/{id}/payments/billings/unpaid'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_organisations_id_payments_methods_default_get_0(client):
    """Test case for organisations_id_payments_methods_default_get_0

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/v2/organisations/{id}/payments/methods/default'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_organisations_id_payments_methods_default_put_0(client):
    """Test case for organisations_id_payments_methods_default_put_0

    
    """
    body = {"deviceData":"deviceData","type":"NEW_CARD","token":"token"}
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/v2/organisations/{id}/payments/methods/default'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_organisations_id_payments_methods_get_0(client):
    """Test case for organisations_id_payments_methods_get_0

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/v2/organisations/{id}/payments/methods'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_organisations_id_payments_methods_mid_delete_0(client):
    """Test case for organisations_id_payments_methods_mid_delete_0

    
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/v2/organisations/{id}/payments/methods/{m_id}'.format(m_id='m_id_example', id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_organisations_id_payments_methods_post_0(client):
    """Test case for organisations_id_payments_methods_post_0

    
    """
    body = {"body":"body"}
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v2/organisations/{id}/payments/methods'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_organisations_id_payments_monthlyinvoice_get_0(client):
    """Test case for organisations_id_payments_monthlyinvoice_get_0

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/v2/organisations/{id}/payments/monthlyinvoice'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_organisations_id_payments_monthlyinvoice_maxcredit_put_0(client):
    """Test case for organisations_id_payments_monthlyinvoice_maxcredit_put_0

    
    """
    headers = { 
    }
    response = await client.request(
        method='PUT',
        path='/v2/organisations/{id}/payments/monthlyinvoice/maxcredit'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_organisations_id_payments_recurring_get_0(client):
    """Test case for organisations_id_payments_recurring_get_0

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/v2/organisations/{id}/payments/recurring'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_organisations_0(client):
    """Test case for post_organisations_0

    
    """
    body = {"zipcode":"zipcode","country":"country","address":"address","city":"city","VAT":"VAT","name":"name","description":"description","company":"company"}
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v2/organisations',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_organisations_id_addonproviders_0(client):
    """Test case for post_organisations_id_addonproviders_0

    
    """
    body = {"name":"name","api":{"password":"password","regions":["regions","regions"],"test":{"base_url":"base_url","sso_url":"sso_url"},"config_vars":["config_vars","config_vars"],"production":{"base_url":"base_url","sso_url":"sso_url"},"sso_salt":"sso_salt"},"id":"id"}
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v2/organisations/{id}/addonproviders'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_organisations_id_addonproviders_provider_id_features_0(client):
    """Test case for post_organisations_id_addonproviders_provider_id_features_0

    
    """
    body = {"name":"name","type":"type"}
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v2/organisations/{id}/addonproviders/{provider_id}/features'.format(id='id_example', provider_id='provider_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_organisations_id_addonproviders_provider_id_plans_0(client):
    """Test case for post_organisations_id_addonproviders_provider_id_plans_0

    
    """
    body = {"features":[{"name":"name","type":"type","value":"value"},{"name":"name","type":"type","value":"value"}],"price":0,"name":"name","slug":"slug"}
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v2/organisations/{id}/addonproviders/{provider_id}/plans'.format(id='id_example', provider_id='provider_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_organisations_id_addonproviders_provider_id_testers_0(client):
    """Test case for post_organisations_id_addonproviders_provider_id_testers_0

    
    """
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/v2/organisations/{id}/addonproviders/{provider_id}/testers'.format(id='id_example', provider_id='provider_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_organisations_id_addons_1(client):
    """Test case for post_organisations_id_addons_1

    
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

async def test_post_organisations_id_applications_1(client):
    """Test case for post_organisations_id_applications_1

    
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

async def test_post_organisations_id_applications_app_id_addons_2(client):
    """Test case for post_organisations_id_applications_app_id_addons_2

    
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

async def test_post_organisations_id_applications_app_id_instances_1(client):
    """Test case for post_organisations_id_applications_app_id_instances_1

    
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

async def test_post_organisations_id_consumers_0(client):
    """Test case for post_organisations_id_consumers_0

    
    """
    body = {"baseUrl":{"url":"url"},"rights":{"right":"right","activated":False},"name":"name","description":"description","picture":"picture","url":{"url":"url"}}
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v2/organisations/{id}/consumers'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_organisations_id_members_0(client):
    """Test case for post_organisations_id_members_0

    
    """
    body = openapi_server.Schema2()
    params = [('invitationKey', 'invitation_key_example')]
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v2/organisations/{id}/members'.format(id='id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_organisations_id_payments_billings_0(client):
    """Test case for post_organisations_id_payments_billings_0

    
    """
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/v2/organisations/{id}/payments/billings'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_put_organisations_id_0(client):
    """Test case for put_organisations_id_0

    
    """
    body = {"zipcode":"zipcode","country":"country","address":"address","city":"city","VAT":"VAT","name":"name","description":"description","company":"company"}
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/v2/organisations/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_put_organisations_id_addonproviders_provider_id_0(client):
    """Test case for put_organisations_id_addonproviders_provider_id_0

    
    """
    body = {"name":"name","api":{"password":"password","regions":["regions","regions"],"test":{"base_url":"base_url","sso_url":"sso_url"},"config_vars":["config_vars","config_vars"],"production":{"base_url":"base_url","sso_url":"sso_url"},"sso_salt":"sso_salt"},"id":"id"}
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/v2/organisations/{id}/addonproviders/{provider_id}'.format(id='id_example', provider_id='provider_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_put_organisations_id_addonproviders_provider_id_plans_plan_id_0(client):
    """Test case for put_organisations_id_addonproviders_provider_id_plans_plan_id_0

    
    """
    body = {"features":[{"name":"name","type":"type","value":"value"},{"name":"name","type":"type","value":"value"}],"price":0,"name":"name","slug":"slug"}
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/v2/organisations/{id}/addonproviders/{provider_id}/plans/{plan_id}'.format(id='id_example', provider_id='provider_id_example', plan_id='plan_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_put_organisations_id_addonproviders_provider_id_plans_plan_id_features_feature_name_0(client):
    """Test case for put_organisations_id_addonproviders_provider_id_plans_plan_id_features_feature_name_0

    
    """
    body = {"name":"name","type":"type","value":"value"}
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/v2/organisations/{id}/addonproviders/{provider_id}/plans/{plan_id}/features/{feature_name}'.format(id='id_example', feature_name='feature_name_example', provider_id='provider_id_example', plan_id='plan_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_put_organisations_id_addons_addon_id_1(client):
    """Test case for put_organisations_id_addons_addon_id_1

    
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

async def test_put_organisations_id_addons_addon_id_tags_tag_1(client):
    """Test case for put_organisations_id_addons_addon_id_tags_tag_1

    
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

async def test_put_organisations_id_applications_app_id_1(client):
    """Test case for put_organisations_id_applications_app_id_1

    
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

async def test_put_organisations_id_applications_app_id_dependencies_dependency_id_1(client):
    """Test case for put_organisations_id_applications_app_id_dependencies_dependency_id_1

    
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

async def test_put_organisations_id_applications_app_id_env_1(client):
    """Test case for put_organisations_id_applications_app_id_env_1

    
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

async def test_put_organisations_id_applications_app_id_env_env_name_1(client):
    """Test case for put_organisations_id_applications_app_id_env_env_name_1

    
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

async def test_put_organisations_id_applications_app_id_tags_tag_1(client):
    """Test case for put_organisations_id_applications_app_id_tags_tag_1

    
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

async def test_put_organisations_id_applications_app_id_vhosts_domain_1(client):
    """Test case for put_organisations_id_applications_app_id_vhosts_domain_1

    
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

async def test_put_organisations_id_applications_app_id_vhosts_favourite_1(client):
    """Test case for put_organisations_id_applications_app_id_vhosts_favourite_1

    
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

async def test_put_organisations_id_avatar_0(client):
    """Test case for put_organisations_id_avatar_0

    
    """
    headers = { 
    }
    response = await client.request(
        method='PUT',
        path='/v2/organisations/{id}/avatar'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_put_organisations_id_consumers_key_0(client):
    """Test case for put_organisations_id_consumers_key_0

    
    """
    body = {"baseUrl":{"url":"url"},"rights":{"right":"right","activated":False},"name":"name","description":"description","picture":"picture","url":{"url":"url"}}
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/v2/organisations/{id}/consumers/{key}'.format(id='id_example', key='key_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_put_organisations_id_members_user_id_0(client):
    """Test case for put_organisations_id_members_user_id_0

    
    """
    body = openapi_server.Schema2()
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/v2/organisations/{id}/members/{user_id}'.format(id='id_example', user_id='user_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_put_organisations_id_payments_billings_bid_0(client):
    """Test case for put_organisations_id_payments_billings_bid_0

    
    """
    headers = { 
    }
    response = await client.request(
        method='PUT',
        path='/v2/organisations/{id}/payments/billings/{bid}'.format(id='id_example', bid='bid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

