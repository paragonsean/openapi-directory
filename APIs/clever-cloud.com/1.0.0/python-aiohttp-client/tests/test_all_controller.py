# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.addon import Addon
from openapi_server.models.addon_migration import AddonMigration
from openapi_server.models.addon_provider_sso import AddonProviderSso
from openapi_server.models.app_instance import AppInstance
from openapi_server.models.application import Application
from openapi_server.models.avatar import Avatar
from openapi_server.models.body import Body
from openapi_server.models.change_password import ChangePassword
from openapi_server.models.conso import Conso
from openapi_server.models.consumer import Consumer
from openapi_server.models.country import Country
from openapi_server.models.credits import Credits
from openapi_server.models.deployment import Deployment
from openapi_server.models.deployment_summary import DeploymentSummary
from openapi_server.models.env import Env
from openapi_server.models.error import Error
from openapi_server.models.feature import Feature
from openapi_server.models.instance import Instance
from openapi_server.models.key import Key
from openapi_server.models.linked_app_env import LinkedAppEnv
from openapi_server.models.list_env import ListEnv
from openapi_server.models.organisation import Organisation
from openapi_server.models.organisations_id_addons_addon_id_migrations_post_request import OrganisationsIdAddonsAddonIdMigrationsPostRequest
from openapi_server.models.payment_data import PaymentData
from openapi_server.models.payment_provider import PaymentProvider
from openapi_server.models.plan import Plan
from openapi_server.models.provider import Provider
from openapi_server.models.rights import Rights
from openapi_server.models.schema1 import Schema1
from openapi_server.models.schema2 import Schema2
from openapi_server.models.secret import Secret
from openapi_server.models.sso import Sso
from openapi_server.models.summary import Summary
from openapi_server.models.supernova_instance_view import SupernovaInstanceView
from openapi_server.models.token import Token
from openapi_server.models.transaction_id import TransactionId
from openapi_server.models.user import User
from openapi_server.models.vhost import Vhost
from openapi_server.models.wannabe_addon import WannabeAddon
from openapi_server.models.wannabe_addon_billing import WannabeAddonBilling
from openapi_server.models.wannabe_addon_provider import WannabeAddonProvider
from openapi_server.models.wannabe_application import WannabeApplication
from openapi_server.models.wannabe_consumer import WannabeConsumer
from openapi_server.models.wannabe_env import WannabeEnv
from openapi_server.models.wannabe_feature import WannabeFeature
from openapi_server.models.wannabe_organisation import WannabeOrganisation
from openapi_server.models.wannabe_plan import WannabePlan
from openapi_server.models.wannabe_plan_feature import WannabePlanFeature
from openapi_server.models.wannabe_user import WannabeUser
from openapi_server.models.zone import Zone


pytestmark = pytest.mark.asyncio

async def test_application_app_id_environment_get(client):
    """Test case for application_app_id_environment_get

    
    """
    params = [('token', 'token_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/v2/application/{app_id}/environment'.format(app_id='app_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_application_app_id_environment_put(client):
    """Test case for application_app_id_environment_put

    
    """
    params = [('token', 'token_example')]
    headers = { 
    }
    response = await client.request(
        method='PUT',
        path='/v2/application/{app_id}/environment'.format(app_id='app_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_create_matomo(client):
    """Test case for create_matomo

    Create Matomo addon
    """
    body = None
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v2/v2/providers/addon-matomo/resources',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_network_group(client):
    """Test case for create_network_group

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

async def test_create_network_group_external_peer(client):
    """Test case for create_network_group_external_peer

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

async def test_create_network_group_member(client):
    """Test case for create_network_group_member

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

async def test_delete_github_link(client):
    """Test case for delete_github_link

    
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/v2/github/link',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_delete_matomo(client):
    """Test case for delete_matomo

    Delete Matomo addon
    """
    body = 'body_example'
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/v2/v2/providers/addon-matomo/resources/{matomo_id}'.format(matomo_id='matomo_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_delete_network_group(client):
    """Test case for delete_network_group

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
async def test_delete_network_group_external_peer(client):
    """Test case for delete_network_group_external_peer

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
async def test_delete_network_group_member(client):
    """Test case for delete_network_group_member

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
async def test_delete_network_group_peer(client):
    """Test case for delete_network_group_peer

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

async def test_delete_organisations_id(client):
    """Test case for delete_organisations_id

    
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

async def test_delete_organisations_id_addonproviders_provider_id_features_feature_id(client):
    """Test case for delete_organisations_id_addonproviders_provider_id_features_feature_id

    
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

async def test_delete_organisations_id_addonproviders_provider_id_plans_plan_id(client):
    """Test case for delete_organisations_id_addonproviders_provider_id_plans_plan_id

    
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

async def test_delete_organisations_id_addonproviders_provider_id_plans_plan_id_features_feature_name(client):
    """Test case for delete_organisations_id_addonproviders_provider_id_plans_plan_id_features_feature_name

    
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

async def test_delete_organisations_id_addons_addon_id(client):
    """Test case for delete_organisations_id_addons_addon_id

    
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

async def test_delete_organisations_id_addons_addon_id_tags_tag(client):
    """Test case for delete_organisations_id_addons_addon_id_tags_tag

    
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

async def test_delete_organisations_id_applications_app_id(client):
    """Test case for delete_organisations_id_applications_app_id

    
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

async def test_delete_organisations_id_applications_app_id_addons_addon_id(client):
    """Test case for delete_organisations_id_applications_app_id_addons_addon_id

    
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

async def test_delete_organisations_id_applications_app_id_dependencies_dependency_id(client):
    """Test case for delete_organisations_id_applications_app_id_dependencies_dependency_id

    
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

async def test_delete_organisations_id_applications_app_id_deployments_deployment_id_instances(client):
    """Test case for delete_organisations_id_applications_app_id_deployments_deployment_id_instances

    
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

async def test_delete_organisations_id_applications_app_id_env_env_name(client):
    """Test case for delete_organisations_id_applications_app_id_env_env_name

    
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

async def test_delete_organisations_id_applications_app_id_instances(client):
    """Test case for delete_organisations_id_applications_app_id_instances

    
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

async def test_delete_organisations_id_applications_app_id_tags_tag(client):
    """Test case for delete_organisations_id_applications_app_id_tags_tag

    
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

async def test_delete_organisations_id_applications_app_id_vhosts_domain(client):
    """Test case for delete_organisations_id_applications_app_id_vhosts_domain

    
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

async def test_delete_organisations_id_applications_app_id_vhosts_favourite(client):
    """Test case for delete_organisations_id_applications_app_id_vhosts_favourite

    
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

async def test_delete_organisations_id_consumers_key(client):
    """Test case for delete_organisations_id_consumers_key

    
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

async def test_delete_organisations_id_members_user_id(client):
    """Test case for delete_organisations_id_members_user_id

    
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

async def test_delete_organisations_id_payments_billings_bid(client):
    """Test case for delete_organisations_id_payments_billings_bid

    
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

async def test_delete_organisations_id_payments_recurring(client):
    """Test case for delete_organisations_id_payments_recurring

    
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

async def test_delete_self(client):
    """Test case for delete_self

    
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/v2/self',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_self_addons_addon_id(client):
    """Test case for delete_self_addons_addon_id

    
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

async def test_delete_self_addons_addon_id_tags_tag(client):
    """Test case for delete_self_addons_addon_id_tags_tag

    
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

async def test_delete_self_applications_app_id(client):
    """Test case for delete_self_applications_app_id

    
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

async def test_delete_self_applications_app_id_addons_addon_id(client):
    """Test case for delete_self_applications_app_id_addons_addon_id

    
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

async def test_delete_self_applications_app_id_dependencies_dependency_id(client):
    """Test case for delete_self_applications_app_id_dependencies_dependency_id

    
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

async def test_delete_self_applications_app_id_deployments_deployment_id_instances(client):
    """Test case for delete_self_applications_app_id_deployments_deployment_id_instances

    
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

async def test_delete_self_applications_app_id_env_env_name(client):
    """Test case for delete_self_applications_app_id_env_env_name

    
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

async def test_delete_self_applications_app_id_instances(client):
    """Test case for delete_self_applications_app_id_instances

    
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

async def test_delete_self_applications_app_id_tags_tag(client):
    """Test case for delete_self_applications_app_id_tags_tag

    
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

async def test_delete_self_applications_app_id_vhosts_domain(client):
    """Test case for delete_self_applications_app_id_vhosts_domain

    
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

async def test_delete_self_applications_app_id_vhosts_favourite(client):
    """Test case for delete_self_applications_app_id_vhosts_favourite

    
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

async def test_delete_self_consumers_key(client):
    """Test case for delete_self_consumers_key

    
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/v2/self/consumers/{key}'.format(key='key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_self_emails_email(client):
    """Test case for delete_self_emails_email

    
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/v2/self/emails/{email}'.format(email='email_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_self_keys_key(client):
    """Test case for delete_self_keys_key

    
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/v2/self/keys/{key}'.format(key='key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_self_payments_billings_bid(client):
    """Test case for delete_self_payments_billings_bid

    
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/v2/self/payments/billings/{bid}'.format(bid='bid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_self_payments_methods_mid(client):
    """Test case for delete_self_payments_methods_mid

    
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/v2/self/payments/methods/{m_id}'.format(m_id='m_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_self_payments_recurring(client):
    """Test case for delete_self_payments_recurring

    
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/v2/self/payments/recurring',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_self_tokens(client):
    """Test case for delete_self_tokens

    
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/v2/self/tokens',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_self_tokens_token(client):
    """Test case for delete_self_tokens_token

    
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/v2/self/tokens/{token}'.format(token='token_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_events_event_socket_get(client):
    """Test case for events_event_socket_get

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/v2/events/event-socket',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_get_config_provider(client):
    """Test case for get_config_provider

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
async def test_get_config_provider_env(client):
    """Test case for get_config_provider_env

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

async def test_get_github(client):
    """Test case for get_github

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/github',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_github_applications(client):
    """Test case for get_github_applications

    
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

async def test_get_github_callback(client):
    """Test case for get_github_callback

    
    """
    params = [('code', 'code_example'),
                    ('state', 'state_example'),
                    ('error', 'error_example'),
                    ('error_description', 'error_description_example'),
                    ('error_uri', 'error_uri_example')]
    headers = { 
        'cookie': 'cookie_example',
    }
    response = await client.request(
        method='GET',
        path='/v2/github/callback',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_github_emails(client):
    """Test case for get_github_emails

    
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/v2/github/emails',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_github_keys(client):
    """Test case for get_github_keys

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/github/keys',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_github_link(client):
    """Test case for get_github_link

    
    """
    params = [('transactionId', 'transaction_id_example'),
                    ('redirectUrl', 'redirect_url_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/v2/github/link',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_github_login(client):
    """Test case for get_github_login

    
    """
    params = [('redirectUrl', 'redirect_url_example'),
                    ('fromAuthorize', 'from_authorize_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/v2/github/login',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_github_signup(client):
    """Test case for get_github_signup

    
    """
    params = [('redirectUrl', 'redirect_url_example'),
                    ('fromAuthorize', 'from_authorize_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/v2/github/signup',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_github_username(client):
    """Test case for get_github_username

    
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/v2/github/username',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_get_matomo(client):
    """Test case for get_matomo

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

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_get_matomo_k_token_validation(client):
    """Test case for get_matomo_k_token_validation

    Validate a keycloak token
    """
    body = 'body_example'
    params = [('keycloakToken', 'keycloak_token_example')]
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/v4/addon-providers/addon-matomo/token/validate',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_get_network_group(client):
    """Test case for get_network_group

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
async def test_get_network_group_member(client):
    """Test case for get_network_group_member

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
async def test_get_network_group_peer(client):
    """Test case for get_network_group_peer

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
async def test_get_network_group_stream(client):
    """Test case for get_network_group_stream

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
async def test_get_network_group_wire_guard_configuration(client):
    """Test case for get_network_group_wire_guard_configuration

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
async def test_get_network_group_wire_guard_configuration_stream(client):
    """Test case for get_network_group_wire_guard_configuration_stream

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

async def test_get_newsfeed_engineering(client):
    """Test case for get_newsfeed_engineering

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/v2/newsfeeds/engineering',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_newsfeeds_blog(client):
    """Test case for get_newsfeeds_blog

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/v2/newsfeeds/blog',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_oauth_authorize(client):
    """Test case for get_oauth_authorize

    
    """
    params = [('oauth_token', 'oauth_token_example')]
    headers = { 
        'cookie': 'cookie_example',
    }
    response = await client.request(
        method='GET',
        path='/v2/oauth/authorize',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_oauth_rights(client):
    """Test case for get_oauth_rights

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/oauth/rights',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organisations(client):
    """Test case for get_organisations

    
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

async def test_get_organisations_id(client):
    """Test case for get_organisations_id

    
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

async def test_get_organisations_id_addonproviders(client):
    """Test case for get_organisations_id_addonproviders

    
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

async def test_get_organisations_id_addonproviders_provider_id(client):
    """Test case for get_organisations_id_addonproviders_provider_id

    
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

async def test_get_organisations_id_addonproviders_provider_id_features(client):
    """Test case for get_organisations_id_addonproviders_provider_id_features

    
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

async def test_get_organisations_id_addonproviders_provider_id_plans(client):
    """Test case for get_organisations_id_addonproviders_provider_id_plans

    
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

async def test_get_organisations_id_addonproviders_provider_id_plans_plan_id(client):
    """Test case for get_organisations_id_addonproviders_provider_id_plans_plan_id

    
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

async def test_get_organisations_id_addonproviders_provider_id_tags(client):
    """Test case for get_organisations_id_addonproviders_provider_id_tags

    
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

async def test_get_organisations_id_addons(client):
    """Test case for get_organisations_id_addons

    
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

async def test_get_organisations_id_addons_addon_id(client):
    """Test case for get_organisations_id_addons_addon_id

    
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

async def test_get_organisations_id_addons_addon_id_applications(client):
    """Test case for get_organisations_id_addons_addon_id_applications

    
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

async def test_get_organisations_id_addons_addon_id_env(client):
    """Test case for get_organisations_id_addons_addon_id_env

    
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

async def test_get_organisations_id_addons_addon_id_sso(client):
    """Test case for get_organisations_id_addons_addon_id_sso

    
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

async def test_get_organisations_id_addons_addon_id_tags(client):
    """Test case for get_organisations_id_addons_addon_id_tags

    
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

async def test_get_organisations_id_applications(client):
    """Test case for get_organisations_id_applications

    
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

async def test_get_organisations_id_applications_app_id(client):
    """Test case for get_organisations_id_applications_app_id

    
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

async def test_get_organisations_id_applications_app_id_addons(client):
    """Test case for get_organisations_id_applications_app_id_addons

    
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

async def test_get_organisations_id_applications_app_id_addons_env(client):
    """Test case for get_organisations_id_applications_app_id_addons_env

    
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

async def test_get_organisations_id_applications_app_id_dependencies(client):
    """Test case for get_organisations_id_applications_app_id_dependencies

    
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

async def test_get_organisations_id_applications_app_id_dependents(client):
    """Test case for get_organisations_id_applications_app_id_dependents

    
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

async def test_get_organisations_id_applications_app_id_deployments(client):
    """Test case for get_organisations_id_applications_app_id_deployments

    
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

async def test_get_organisations_id_applications_app_id_env(client):
    """Test case for get_organisations_id_applications_app_id_env

    
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

async def test_get_organisations_id_applications_app_id_instances(client):
    """Test case for get_organisations_id_applications_app_id_instances

    
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

async def test_get_organisations_id_applications_app_id_tags(client):
    """Test case for get_organisations_id_applications_app_id_tags

    
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

async def test_get_organisations_id_applications_app_id_vhosts(client):
    """Test case for get_organisations_id_applications_app_id_vhosts

    
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

async def test_get_organisations_id_applications_app_id_vhosts_favourite(client):
    """Test case for get_organisations_id_applications_app_id_vhosts_favourite

    
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

async def test_get_organisations_id_consumers(client):
    """Test case for get_organisations_id_consumers

    
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

async def test_get_organisations_id_consumers_key(client):
    """Test case for get_organisations_id_consumers_key

    
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

async def test_get_organisations_id_consumers_key_secret(client):
    """Test case for get_organisations_id_consumers_key_secret

    
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

async def test_get_organisations_id_consumptions(client):
    """Test case for get_organisations_id_consumptions

    
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

async def test_get_organisations_id_credits(client):
    """Test case for get_organisations_id_credits

    
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

async def test_get_organisations_id_deployments(client):
    """Test case for get_organisations_id_deployments

    
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

async def test_get_organisations_id_instances(client):
    """Test case for get_organisations_id_instances

    
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

async def test_get_organisations_id_members(client):
    """Test case for get_organisations_id_members

    
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

async def test_get_organisations_id_payment_info(client):
    """Test case for get_organisations_id_payment_info

    
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

async def test_get_organisations_id_payments_billings(client):
    """Test case for get_organisations_id_payments_billings

    
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

async def test_get_organisations_id_payments_billings_bid(client):
    """Test case for get_organisations_id_payments_billings_bid

    
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

async def test_get_organisations_id_payments_billings_bid_pdf(client):
    """Test case for get_organisations_id_payments_billings_bid_pdf

    
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

async def test_get_organisations_id_payments_full_price_price(client):
    """Test case for get_organisations_id_payments_full_price_price

    
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

async def test_get_password_forgotten(client):
    """Test case for get_password_forgotten

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/v2/password_forgotten',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_password_forgotten_key(client):
    """Test case for get_password_forgotten_key

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/v2/password_forgotten/{key}'.format(key='key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_payments_coupons_name(client):
    """Test case for get_payments_coupons_name

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/v2/payments/coupons/{name}'.format(name='name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_payments_providers(client):
    """Test case for get_payments_providers

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/payments/providers',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_payments_tokens_stripe(client):
    """Test case for get_payments_tokens_stripe

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/v2/payments/tokens/stripe',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_products_addon_providers(client):
    """Test case for get_products_addon_providers

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/products/addonproviders',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_products_addon_providers_provider_id(client):
    """Test case for get_products_addon_providers_provider_id

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/products/addonproviders/{provider_id}'.format(provider_id='provider_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_products_countries(client):
    """Test case for get_products_countries

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/products/countries',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_products_countrycodes(client):
    """Test case for get_products_countrycodes

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/products/countrycodes',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_products_instances(client):
    """Test case for get_products_instances

    
    """
    params = [('for', '_for_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/products/instances',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_products_instances_type_version(client):
    """Test case for get_products_instances_type_version

    
    """
    params = [('for', '_for_example'),
                    ('app', 'app_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/products/instances/{type_version}'.format(type='type_example', version='version_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_products_packages(client):
    """Test case for get_products_packages

    
    """
    params = [('coupon', 'coupon_example'),
                    ('orgaId', 'orga_id_example'),
                    ('currency', 'currency_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/v2/products/packages',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_products_prices(client):
    """Test case for get_products_prices

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/v2/products/prices',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_products_zones(client):
    """Test case for get_products_zones

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/products/zones',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_self(client):
    """Test case for get_self

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/self',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_self_addons(client):
    """Test case for get_self_addons

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

async def test_get_self_addons_addon_id(client):
    """Test case for get_self_addons_addon_id

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

async def test_get_self_addons_addon_id_applications(client):
    """Test case for get_self_addons_addon_id_applications

    
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

async def test_get_self_addons_addon_id_env(client):
    """Test case for get_self_addons_addon_id_env

    
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

async def test_get_self_addons_addon_id_sso(client):
    """Test case for get_self_addons_addon_id_sso

    
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

async def test_get_self_addons_addon_id_tags(client):
    """Test case for get_self_addons_addon_id_tags

    
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

async def test_get_self_applications(client):
    """Test case for get_self_applications

    
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

async def test_get_self_applications_app_id(client):
    """Test case for get_self_applications_app_id

    
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

async def test_get_self_applications_app_id_addons(client):
    """Test case for get_self_applications_app_id_addons

    
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

async def test_get_self_applications_app_id_addons_env(client):
    """Test case for get_self_applications_app_id_addons_env

    
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

async def test_get_self_applications_app_id_dependencies(client):
    """Test case for get_self_applications_app_id_dependencies

    
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

async def test_get_self_applications_app_id_dependencies_dependency_id(client):
    """Test case for get_self_applications_app_id_dependencies_dependency_id

    
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

async def test_get_self_applications_app_id_dependents(client):
    """Test case for get_self_applications_app_id_dependents

    
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

async def test_get_self_applications_app_id_deployments(client):
    """Test case for get_self_applications_app_id_deployments

    
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

async def test_get_self_applications_app_id_env(client):
    """Test case for get_self_applications_app_id_env

    
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

async def test_get_self_applications_app_id_instances(client):
    """Test case for get_self_applications_app_id_instances

    
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

async def test_get_self_applications_app_id_tags(client):
    """Test case for get_self_applications_app_id_tags

    
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

async def test_get_self_applications_app_id_vhosts(client):
    """Test case for get_self_applications_app_id_vhosts

    
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

async def test_get_self_applications_app_id_vhosts_favourite(client):
    """Test case for get_self_applications_app_id_vhosts_favourite

    
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

async def test_get_self_confirmation_email(client):
    """Test case for get_self_confirmation_email

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/v2/self/confirmation_email',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_self_consumers(client):
    """Test case for get_self_consumers

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/self/consumers',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_self_consumers_key(client):
    """Test case for get_self_consumers_key

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/self/consumers/{key}'.format(key='key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_self_consumers_key_secret(client):
    """Test case for get_self_consumers_key_secret

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/self/consumers/{key}/secret'.format(key='key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_self_consumptions(client):
    """Test case for get_self_consumptions

    
    """
    params = [('appId', 'app_id_example'),
                    ('from', '_from_example'),
                    ('to', 'to_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/self/consumptions',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_self_credits(client):
    """Test case for get_self_credits

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/self/credits',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_self_emails(client):
    """Test case for get_self_emails

    
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/v2/self/emails',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_self_id(client):
    """Test case for get_self_id

    
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/v2/self/id',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_self_instances(client):
    """Test case for get_self_instances

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/self/instances',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_self_keys(client):
    """Test case for get_self_keys

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/self/keys',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_self_payment_info(client):
    """Test case for get_self_payment_info

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/v2/self/payment-info',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_self_payments_billings(client):
    """Test case for get_self_payments_billings

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/v2/self/payments/billings',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_self_payments_billings_bid(client):
    """Test case for get_self_payments_billings_bid

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/v2/self/payments/billings/{bid}'.format(bid='bid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_self_payments_billings_bid_pdf(client):
    """Test case for get_self_payments_billings_bid_pdf

    
    """
    params = [('token', 'token_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/v2/self/payments/billings/{bid_pd}'.format(bid='bid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_self_payments_fullprice_price(client):
    """Test case for get_self_payments_fullprice_price

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/v2/self/payments/fullprice/{price}'.format(price='price_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_self_payments_methods(client):
    """Test case for get_self_payments_methods

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/v2/self/payments/methods',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_self_tokens(client):
    """Test case for get_self_tokens

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/self/tokens',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_self_validate_email(client):
    """Test case for get_self_validate_email

    
    """
    params = [('validationKey', 'validation_key_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/v2/self/validate_email',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_summary(client):
    """Test case for get_summary

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/summary',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_users_id(client):
    """Test case for get_users_id

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/users/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_users_id_applications(client):
    """Test case for get_users_id_applications

    
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

async def test_get_users_user_id_git_info(client):
    """Test case for get_users_user_id_git_info

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/v2/users/{user_id}/git-info'.format(user_id='user_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_vendor_apps(client):
    """Test case for get_vendor_apps

    
    """
    params = [('offset', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/vendor/apps',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_vendor_apps_addon_id(client):
    """Test case for get_vendor_apps_addon_id

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/v2/vendor/apps/{addon_id}'.format(addon_id='addon_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_list_network_group_members(client):
    """Test case for list_network_group_members

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
async def test_list_network_group_peers(client):
    """Test case for list_network_group_peers

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
async def test_list_network_groups(client):
    """Test case for list_network_groups

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

async def test_logs_app_id_drains_get(client):
    """Test case for logs_app_id_drains_get

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/v2/logs/{app_id}/drains'.format(app_id='app_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_logs_app_id_drains_id_or_url_delete(client):
    """Test case for logs_app_id_drains_id_or_url_delete

    
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/v2/logs/{app_id}/drains/:idOrUrl'.format(app_id='app_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_logs_app_id_drains_id_or_url_get(client):
    """Test case for logs_app_id_drains_id_or_url_get

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/v2/logs/{app_id}/drains/:idOrUrl'.format(app_id='app_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_logs_app_id_drains_post(client):
    """Test case for logs_app_id_drains_post

    
    """
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/v2/logs/{app_id}/drains'.format(app_id='app_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_logs_app_id_get(client):
    """Test case for logs_app_id_get

    
    """
    params = [('limit', 56),
                    ('order', desc),
                    ('after', '2013-10-20T19:20:30+01:00'),
                    ('before', '2013-10-20T19:20:30+01:00'),
                    ('filter', 'filter_example'),
                    ('deployment_id', 'deployment_id_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/v2/logs/{app_id}'.format(app_id='app_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_logs_app_id_sse_get(client):
    """Test case for logs_app_id_sse_get

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/v2/logs/{app_id}/sse'.format(app_id='app_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_logs_drains_drain_id_put(client):
    """Test case for logs_drains_drain_id_put

    
    """
    headers = { 
    }
    response = await client.request(
        method='PUT',
        path='/v2/logs/drains/{drain_id}'.format(drain_id='drain_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_logs_drains_get(client):
    """Test case for logs_drains_get

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/v2/logs/drains',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_logs_logs_chunked_app_id_get(client):
    """Test case for logs_logs_chunked_app_id_get

    
    """
    params = [('download', True)]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/v2/logs/logs-chunked/{app_id}'.format(app_id='app_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_logs_logs_socket_app_id_get(client):
    """Test case for logs_logs_socket_app_id_get

    
    """
    params = [('since', '2013-10-20T19:20:30+01:00'),
                    ('filter', 'filter_example'),
                    ('deployment_id', 'deployment_id_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/v2/logs/logs-socket/{app_id}'.format(app_id='app_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_logs_socket_app_id_get(client):
    """Test case for logs_socket_app_id_get

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/v2/logs-socket/{app_id}'.format(app_id='app_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_notifications_emailhooks_owner_id_get(client):
    """Test case for notifications_emailhooks_owner_id_get

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/v2/notifications/emailhooks/{owner_id}'.format(owner_id='owner_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_notifications_emailhooks_owner_id_id_delete(client):
    """Test case for notifications_emailhooks_owner_id_id_delete

    
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/v2/notifications/emailhooks/{owner_id}/:id'.format(owner_id='owner_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_notifications_emailhooks_owner_id_id_put(client):
    """Test case for notifications_emailhooks_owner_id_id_put

    
    """
    headers = { 
    }
    response = await client.request(
        method='PUT',
        path='/v2/notifications/emailhooks/{owner_id}/:id'.format(owner_id='owner_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_notifications_emailhooks_owner_id_post(client):
    """Test case for notifications_emailhooks_owner_id_post

    
    """
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/v2/notifications/emailhooks/{owner_id}'.format(owner_id='owner_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_notifications_info_events_get(client):
    """Test case for notifications_info_events_get

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/v2/notifications/info/events',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_notifications_info_webhookformats_get(client):
    """Test case for notifications_info_webhookformats_get

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/v2/notifications/info/webhookformats',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_notifications_webhooks_owner_id_get(client):
    """Test case for notifications_webhooks_owner_id_get

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/v2/notifications/webhooks/{owner_id}'.format(owner_id='owner_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_notifications_webhooks_owner_id_id_delete(client):
    """Test case for notifications_webhooks_owner_id_id_delete

    
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/v2/notifications/webhooks/{owner_id}/:id'.format(owner_id='owner_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_notifications_webhooks_owner_id_id_put(client):
    """Test case for notifications_webhooks_owner_id_id_put

    
    """
    headers = { 
    }
    response = await client.request(
        method='PUT',
        path='/v2/notifications/webhooks/{owner_id}/:id'.format(owner_id='owner_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_notifications_webhooks_owner_id_post(client):
    """Test case for notifications_webhooks_owner_id_post

    
    """
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/v2/notifications/webhooks/{owner_id}'.format(owner_id='owner_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_oauth_access_token_query_post(client):
    """Test case for oauth_access_token_query_post

    
    """
    params = [('oauth_consumer_key', 'oauth_consumer_key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('oauth_signature_method', 'oauth_signature_method_example'),
                    ('oauth_signature', 'oauth_signature_example'),
                    ('oauth_timestamp', 'oauth_timestamp_example'),
                    ('oauth_nonce', 'oauth_nonce_example'),
                    ('oauth_version', 'oauth_version_example'),
                    ('oauth_verifier', 'oauth_verifier_example'),
                    ('oauth_callback', 'oauth_callback_example'),
                    ('oauth_token_secret', 'oauth_token_secret_example'),
                    ('oauth_callback_confirmed', 'oauth_callback_confirmed_example')]
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/v2/oauth/access_token_query',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_oauth_request_token_query_post(client):
    """Test case for oauth_request_token_query_post

    
    """
    params = [('oauth_consumer_key', 'oauth_consumer_key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('oauth_signature_method', 'oauth_signature_method_example'),
                    ('oauth_signature', 'oauth_signature_example'),
                    ('oauth_timestamp', 'oauth_timestamp_example'),
                    ('oauth_nonce', 'oauth_nonce_example'),
                    ('oauth_version', 'oauth_version_example'),
                    ('oauth_verifier', 'oauth_verifier_example'),
                    ('oauth_callback', 'oauth_callback_example'),
                    ('oauth_token_secret', 'oauth_token_secret_example'),
                    ('oauth_callback_confirmed', 'oauth_callback_confirmed_example')]
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/v2/oauth/request_token_query',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_openapi_get(client):
    """Test case for openapi_get

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/v2//openapi',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_openapi_type_get(client):
    """Test case for openapi_type_get

    Get the swagger for this API as {type}
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/v2/openapi.{type}'.format(type='type_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_organisations_id_addonproviders_provider_id_delete(client):
    """Test case for organisations_id_addonproviders_provider_id_delete

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

async def test_organisations_id_addons_addon_id_instances_get(client):
    """Test case for organisations_id_addons_addon_id_instances_get

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

async def test_organisations_id_addons_addon_id_instances_instance_id_get(client):
    """Test case for organisations_id_addons_addon_id_instances_instance_id_get

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

async def test_organisations_id_addons_addon_id_migrations_get(client):
    """Test case for organisations_id_addons_addon_id_migrations_get

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

async def test_organisations_id_addons_addon_id_migrations_migration_id_get(client):
    """Test case for organisations_id_addons_addon_id_migrations_migration_id_get

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

async def test_organisations_id_addons_addon_id_migrations_post(client):
    """Test case for organisations_id_addons_addon_id_migrations_post

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

async def test_organisations_id_addons_addon_id_sso_get(client):
    """Test case for organisations_id_addons_addon_id_sso_get

    
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

async def test_organisations_id_addons_preorders_post(client):
    """Test case for organisations_id_addons_preorders_post

    
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

async def test_organisations_id_applications_app_id_branch_put(client):
    """Test case for organisations_id_applications_app_id_branch_put

    
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

async def test_organisations_id_applications_app_id_branches_get(client):
    """Test case for organisations_id_applications_app_id_branches_get

    
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

async def test_organisations_id_applications_app_id_buildflavor_put(client):
    """Test case for organisations_id_applications_app_id_buildflavor_put

    
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

async def test_organisations_id_applications_app_id_dependencies_env_get(client):
    """Test case for organisations_id_applications_app_id_dependencies_env_get

    
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

async def test_organisations_id_applications_app_id_deployments_deployment_id_get(client):
    """Test case for organisations_id_applications_app_id_deployments_deployment_id_get

    
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

async def test_organisations_id_applications_app_id_exposed_env_get(client):
    """Test case for organisations_id_applications_app_id_exposed_env_get

    
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

async def test_organisations_id_applications_app_id_exposed_env_put(client):
    """Test case for organisations_id_applications_app_id_exposed_env_put

    
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

async def test_organisations_id_applications_app_id_instances_instance_id_get(client):
    """Test case for organisations_id_applications_app_id_instances_instance_id_get

    
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

async def test_organisations_id_payments_billings_unpaid_get(client):
    """Test case for organisations_id_payments_billings_unpaid_get

    
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

async def test_organisations_id_payments_methods_default_get(client):
    """Test case for organisations_id_payments_methods_default_get

    
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

async def test_organisations_id_payments_methods_default_put(client):
    """Test case for organisations_id_payments_methods_default_put

    
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

async def test_organisations_id_payments_methods_get(client):
    """Test case for organisations_id_payments_methods_get

    
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

async def test_organisations_id_payments_methods_mid_delete(client):
    """Test case for organisations_id_payments_methods_mid_delete

    
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

async def test_organisations_id_payments_methods_post(client):
    """Test case for organisations_id_payments_methods_post

    
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

async def test_organisations_id_payments_monthlyinvoice_get(client):
    """Test case for organisations_id_payments_monthlyinvoice_get

    
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

async def test_organisations_id_payments_monthlyinvoice_maxcredit_put(client):
    """Test case for organisations_id_payments_monthlyinvoice_maxcredit_put

    
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

async def test_organisations_id_payments_recurring_get(client):
    """Test case for organisations_id_payments_recurring_get

    
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

async def test_payments_assets_pay_button_token_button_png_get(client):
    """Test case for payments_assets_pay_button_token_button_png_get

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/v2/payments/assets/pay_button/{token}/button.png'.format(token='token_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_payments_bid_end_stripe_post(client):
    """Test case for payments_bid_end_stripe_post

    
    """
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/v2/payments/{bid}/end/stripe'.format(bid='bid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_authorize(client):
    """Test case for post_authorize

    
    """
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/v2/authorize',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_github_redeploy(client):
    """Test case for post_github_redeploy

    
    """
    headers = { 
        'user_agent': 'user_agent_example',
        'x_github_event': 'x_github_event_example',
        'x_hub_signature': 'x_hub_signature_example',
    }
    response = await client.request(
        method='POST',
        path='/v2/github/redeploy',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_github_signup(client):
    """Test case for post_github_signup

    
    """
    params = [('transactionId', 'transaction_id_example'),
                    ('name', 'name_example'),
                    ('otherId', 'other_id_example'),
                    ('otherEmail', 'other_email_example'),
                    ('password', 'password_example'),
                    ('autoLink', 'auto_link_example'),
                    ('terms', 'terms_example')]
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/v2/github/signup',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_oauth_access_token(client):
    """Test case for post_oauth_access_token

    
    """
    params = [('oauth_consumer_key', 'oauth_consumer_key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('oauth_signature_method', 'oauth_signature_method_example'),
                    ('oauth_signature', 'oauth_signature_example'),
                    ('oauth_timestamp', 'oauth_timestamp_example'),
                    ('oauth_nonce', 'oauth_nonce_example'),
                    ('oauth_version', 'oauth_version_example'),
                    ('oauth_verifier', 'oauth_verifier_example'),
                    ('oauth_callback', 'oauth_callback_example'),
                    ('oauth_token_secret', 'oauth_token_secret_example'),
                    ('oauth_callback_confirmed', 'oauth_callback_confirmed_example')]
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/v2/oauth/access_token',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_oauth_authorize(client):
    """Test case for post_oauth_authorize

    
    """
    params = [('almighty', 'almighty_example'),
                    ('access_organisations', 'access_organisations_example'),
                    ('manage_organisations', 'manage_organisations_example'),
                    ('manage_organisations_services', 'manage_organisations_services_example'),
                    ('manage_organisations_applications', 'manage_organisations_applications_example'),
                    ('manage_organisations_members', 'manage_organisations_members_example'),
                    ('access_organisations_bills', 'access_organisations_bills_example'),
                    ('access_organisations_credit_count', 'access_organisations_credit_count_example'),
                    ('access_organisations_consumption_statistics', 'access_organisations_consumption_statistics_example'),
                    ('access_personal_information', 'access_personal_information_example'),
                    ('manage_personal_information', 'manage_personal_information_example'),
                    ('manage_ssh_keys', 'manage_ssh_keys_example'),
                    ('manage_services', 'manage_services_example'),
                    ('manage_applications', 'manage_applications_example'),
                    ('access_bills', 'access_bills_example'),
                    ('access_credit_count', 'access_credit_count_example'),
                    ('access_consumption_statistics', 'access_consumption_statistics_example')]
    headers = { 
        'cookie': 'cookie_example',
    }
    response = await client.request(
        method='POST',
        path='/v2/oauth/authorize',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_oauth_request_token(client):
    """Test case for post_oauth_request_token

    
    """
    params = [('oauth_consumer_key', 'oauth_consumer_key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('oauth_signature_method', 'oauth_signature_method_example'),
                    ('oauth_signature', 'oauth_signature_example'),
                    ('oauth_timestamp', 'oauth_timestamp_example'),
                    ('oauth_nonce', 'oauth_nonce_example'),
                    ('oauth_version', 'oauth_version_example'),
                    ('oauth_verifier', 'oauth_verifier_example'),
                    ('oauth_callback', 'oauth_callback_example'),
                    ('oauth_token_secret', 'oauth_token_secret_example'),
                    ('oauth_callback_confirmed', 'oauth_callback_confirmed_example')]
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/v2/oauth/request_token',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_organisations(client):
    """Test case for post_organisations

    
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

async def test_post_organisations_id_addonproviders(client):
    """Test case for post_organisations_id_addonproviders

    
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

async def test_post_organisations_id_addonproviders_provider_id_features(client):
    """Test case for post_organisations_id_addonproviders_provider_id_features

    
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

async def test_post_organisations_id_addonproviders_provider_id_plans(client):
    """Test case for post_organisations_id_addonproviders_provider_id_plans

    
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

async def test_post_organisations_id_addonproviders_provider_id_testers(client):
    """Test case for post_organisations_id_addonproviders_provider_id_testers

    
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

async def test_post_organisations_id_addons(client):
    """Test case for post_organisations_id_addons

    
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

async def test_post_organisations_id_applications(client):
    """Test case for post_organisations_id_applications

    
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

async def test_post_organisations_id_applications_app_id_addons(client):
    """Test case for post_organisations_id_applications_app_id_addons

    
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

async def test_post_organisations_id_applications_app_id_instances(client):
    """Test case for post_organisations_id_applications_app_id_instances

    
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

async def test_post_organisations_id_consumers(client):
    """Test case for post_organisations_id_consumers

    
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

async def test_post_organisations_id_members(client):
    """Test case for post_organisations_id_members

    
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

async def test_post_organisations_id_payments_billings(client):
    """Test case for post_organisations_id_payments_billings

    
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

async def test_post_password_forgotten(client):
    """Test case for post_password_forgotten

    
    """
    params = [('login', 'login_example'),
                    ('drop_tokens', 'drop_tokens_example')]
    headers = { 
        'tester_pass': 'tester_pass_example',
    }
    response = await client.request(
        method='POST',
        path='/v2/password_forgotten',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_password_forgotten_key(client):
    """Test case for post_password_forgotten_key

    
    """
    params = [('pass', '_pass_example'),
                    ('pass2', 'pass2_example')]
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/v2/password_forgotten/{key}'.format(key='key_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_self_addons(client):
    """Test case for post_self_addons

    
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

async def test_post_self_applications(client):
    """Test case for post_self_applications

    
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

async def test_post_self_applications_app_id_addons(client):
    """Test case for post_self_applications_app_id_addons

    
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

async def test_post_self_applications_app_id_instances(client):
    """Test case for post_self_applications_app_id_instances

    
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

async def test_post_self_consumers(client):
    """Test case for post_self_consumers

    
    """
    body = {"baseUrl":{"url":"url"},"rights":{"right":"right","activated":False},"name":"name","description":"description","picture":"picture","url":{"url":"url"}}
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v2/self/consumers',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_self_payments_billings(client):
    """Test case for post_self_payments_billings

    
    """
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/v2/self/payments/billings',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_self_payments_methods(client):
    """Test case for post_self_payments_methods

    
    """
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/v2/self/payments/methods',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_users(client):
    """Test case for post_users

    
    """
    body = {"zipcode":"zipcode","country":"country","password":"password","address":"address","city":"city","phone":"phone","terms":False,"name":"name","lang":"lang","email":"email"}
    params = [('invitationKey', 'invitation_key_example'),
                    ('addonBetaInvitationKey', 'addon_beta_invitation_key_example'),
                    ('email', 'email_example'),
                    ('pass', '_pass_example'),
                    ('url_next', 'url_next_example'),
                    ('terms', 'terms_example')]
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v2/users',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_vendor_billing_owner_id(client):
    """Test case for post_vendor_billing_owner_id

    
    """
    body = {"cost":0.8008281904610115}
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v2/vendor/apps/{addon_id}/consumptions'.format(addon_id='addon_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_products_addonproviders_provider_id_versions_get(client):
    """Test case for products_addonproviders_provider_id_versions_get

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/v2/products/addonproviders/{provider_id}/versions'.format(provider_id='provider_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_products_mfa_kinds_get(client):
    """Test case for products_mfa_kinds_get

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/v2/products/mfa_kinds',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_put_organisations_id(client):
    """Test case for put_organisations_id

    
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

async def test_put_organisations_id_addonproviders_provider_id(client):
    """Test case for put_organisations_id_addonproviders_provider_id

    
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

async def test_put_organisations_id_addonproviders_provider_id_plans_plan_id(client):
    """Test case for put_organisations_id_addonproviders_provider_id_plans_plan_id

    
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

async def test_put_organisations_id_addonproviders_provider_id_plans_plan_id_features_feature_name(client):
    """Test case for put_organisations_id_addonproviders_provider_id_plans_plan_id_features_feature_name

    
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

async def test_put_organisations_id_addons_addon_id(client):
    """Test case for put_organisations_id_addons_addon_id

    
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

async def test_put_organisations_id_addons_addon_id_tags_tag(client):
    """Test case for put_organisations_id_addons_addon_id_tags_tag

    
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

async def test_put_organisations_id_applications_app_id(client):
    """Test case for put_organisations_id_applications_app_id

    
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

async def test_put_organisations_id_applications_app_id_dependencies_dependency_id(client):
    """Test case for put_organisations_id_applications_app_id_dependencies_dependency_id

    
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

async def test_put_organisations_id_applications_app_id_env(client):
    """Test case for put_organisations_id_applications_app_id_env

    
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

async def test_put_organisations_id_applications_app_id_env_env_name(client):
    """Test case for put_organisations_id_applications_app_id_env_env_name

    
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

async def test_put_organisations_id_applications_app_id_tags_tag(client):
    """Test case for put_organisations_id_applications_app_id_tags_tag

    
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

async def test_put_organisations_id_applications_app_id_vhosts_domain(client):
    """Test case for put_organisations_id_applications_app_id_vhosts_domain

    
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

async def test_put_organisations_id_applications_app_id_vhosts_favourite(client):
    """Test case for put_organisations_id_applications_app_id_vhosts_favourite

    
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

async def test_put_organisations_id_avatar(client):
    """Test case for put_organisations_id_avatar

    
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

async def test_put_organisations_id_consumers_key(client):
    """Test case for put_organisations_id_consumers_key

    
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

async def test_put_organisations_id_members_user_id(client):
    """Test case for put_organisations_id_members_user_id

    
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

async def test_put_organisations_id_payments_billings_bid(client):
    """Test case for put_organisations_id_payments_billings_bid

    
    """
    headers = { 
    }
    response = await client.request(
        method='PUT',
        path='/v2/organisations/{id}/payments/billings/{bid}'.format(id='id_example', bid='bid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_put_self(client):
    """Test case for put_self

    
    """
    body = {"zipcode":"zipcode","country":"country","password":"password","address":"address","city":"city","phone":"phone","terms":False,"name":"name","lang":"lang","email":"email"}
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/v2/self',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_put_self_addons_addon_id(client):
    """Test case for put_self_addons_addon_id

    
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

async def test_put_self_addons_addon_id_plan(client):
    """Test case for put_self_addons_addon_id_plan

    
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

async def test_put_self_addons_addon_id_tags_tag(client):
    """Test case for put_self_addons_addon_id_tags_tag

    
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

async def test_put_self_applications_app_id(client):
    """Test case for put_self_applications_app_id

    
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

async def test_put_self_applications_app_id_env(client):
    """Test case for put_self_applications_app_id_env

    
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

async def test_put_self_applications_app_id_env_env_name(client):
    """Test case for put_self_applications_app_id_env_env_name

    
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

async def test_put_self_applications_app_id_tags_tag(client):
    """Test case for put_self_applications_app_id_tags_tag

    
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

async def test_put_self_applications_app_id_vhosts_domain(client):
    """Test case for put_self_applications_app_id_vhosts_domain

    
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

async def test_put_self_applications_app_id_vhosts_favourite(client):
    """Test case for put_self_applications_app_id_vhosts_favourite

    
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

async def test_put_self_avatar(client):
    """Test case for put_self_avatar

    
    """
    body = {"source":{"source":"source","value":{"url":"url"}}}
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/v2/self/avatar',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_put_self_change_password(client):
    """Test case for put_self_change_password

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/v2/self/change_password',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_put_self_consumers_key(client):
    """Test case for put_self_consumers_key

    
    """
    body = {"baseUrl":{"url":"url"},"rights":{"right":"right","activated":False},"name":"name","description":"description","picture":"picture","url":{"url":"url"}}
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/v2/self/consumers/{key}'.format(key='key_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_put_self_emails_email(client):
    """Test case for put_self_emails_email

    
    """
    body = {"body":"body"}
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/v2/self/emails/{email}'.format(email='email_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_put_self_keys_key(client):
    """Test case for put_self_keys_key

    
    """
    body = {"body":"body"}
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/v2/self/keys/{key}'.format(key='key_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_put_self_payments_billings_bid(client):
    """Test case for put_self_payments_billings_bid

    
    """
    headers = { 
    }
    response = await client.request(
        method='PUT',
        path='/v2/self/payments/billings/{bid}'.format(bid='bid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_put_vendor_apps_addon_id(client):
    """Test case for put_vendor_apps_addon_id

    
    """
    headers = { 
    }
    response = await client.request(
        method='PUT',
        path='/v2/vendor/apps/{addon_id}'.format(addon_id='addon_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_self_addons_preorders_post(client):
    """Test case for self_addons_preorders_post

    
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

async def test_self_applications_app_id_branch_put(client):
    """Test case for self_applications_app_id_branch_put

    
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

async def test_self_applications_app_id_branches_get(client):
    """Test case for self_applications_app_id_branches_get

    
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

async def test_self_applications_app_id_buildflavor_put(client):
    """Test case for self_applications_app_id_buildflavor_put

    
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

async def test_self_applications_app_id_dependencies_env_get(client):
    """Test case for self_applications_app_id_dependencies_env_get

    
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

async def test_self_applications_app_id_deployments_deployment_id_get(client):
    """Test case for self_applications_app_id_deployments_deployment_id_get

    
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

async def test_self_applications_app_id_exposed_env_get(client):
    """Test case for self_applications_app_id_exposed_env_get

    
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

async def test_self_applications_app_id_exposed_env_put(client):
    """Test case for self_applications_app_id_exposed_env_put

    
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

async def test_self_applications_app_id_instances_instance_id_get(client):
    """Test case for self_applications_app_id_instances_instance_id_get

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/v2/self/applications/{app_id}/instances/{instance_id}'.format(instance_id='instance_id_example', app_id='app_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_self_cli_tokens_get(client):
    """Test case for self_cli_tokens_get

    
    """
    params = [('cli_token', 'cli_token_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/v2/self/cli_tokens',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_self_mfa_kind_backupcodes_get(client):
    """Test case for self_mfa_kind_backupcodes_get

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/v2/self/mfa/{kind}/backupcodes'.format(kind='kind_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_self_mfa_kind_confirmation_post(client):
    """Test case for self_mfa_kind_confirmation_post

    
    """
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/v2/self/mfa/{kind}/confirmation'.format(kind='kind_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_self_mfa_kind_delete(client):
    """Test case for self_mfa_kind_delete

    
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/v2/self/mfa/{kind}'.format(kind='kind_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_self_mfa_kind_post(client):
    """Test case for self_mfa_kind_post

    
    """
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/v2/self/mfa/{kind}'.format(kind='kind_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_self_mfa_kind_put(client):
    """Test case for self_mfa_kind_put

    
    """
    headers = { 
    }
    response = await client.request(
        method='PUT',
        path='/v2/self/mfa/{kind}'.format(kind='kind_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_self_payments_methods_default_get(client):
    """Test case for self_payments_methods_default_get

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/v2/self/payments/methods/default',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_self_payments_methods_default_put(client):
    """Test case for self_payments_methods_default_put

    
    """
    headers = { 
    }
    response = await client.request(
        method='PUT',
        path='/v2/self/payments/methods/default',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_self_payments_monthlyinvoice_get(client):
    """Test case for self_payments_monthlyinvoice_get

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/v2/self/payments/monthlyinvoice',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_self_payments_monthlyinvoice_maxcredit_put(client):
    """Test case for self_payments_monthlyinvoice_maxcredit_put

    
    """
    headers = { 
    }
    response = await client.request(
        method='PUT',
        path='/v2/self/payments/monthlyinvoice/maxcredit',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_self_payments_recurring_get(client):
    """Test case for self_payments_recurring_get

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/v2/self/payments/recurring',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_self_payments_tokens_stripe_get(client):
    """Test case for self_payments_tokens_stripe_get

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/v2/self/payments/tokens/stripe',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_config_provider_env(client):
    """Test case for update_config_provider_env

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

async def test_v3_logs_app_id_drains_get(client):
    """Test case for v3_logs_app_id_drains_get

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/v2/v3/logs/{app_id}/drains'.format(app_id='app_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_v3_logs_app_id_drains_id_or_url_delete(client):
    """Test case for v3_logs_app_id_drains_id_or_url_delete

    
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/v2/v3/logs/{app_id}/drains/:idOrUrl'.format(app_id='app_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_v3_logs_app_id_drains_id_or_url_get(client):
    """Test case for v3_logs_app_id_drains_id_or_url_get

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/v2/v3/logs/{app_id}/drains/:idOrUrl'.format(app_id='app_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_v3_logs_app_id_drains_post(client):
    """Test case for v3_logs_app_id_drains_post

    
    """
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/v2/v3/logs/{app_id}/drains'.format(app_id='app_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_v3_logs_app_id_get(client):
    """Test case for v3_logs_app_id_get

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/v2/v3/logs/{app_id}'.format(app_id='app_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_v3_logs_app_id_logs_chunked_get(client):
    """Test case for v3_logs_app_id_logs_chunked_get

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/v2/v3/logs/{app_id}/logs-chunked'.format(app_id='app_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_v3_logs_app_id_logs_socket_get(client):
    """Test case for v3_logs_app_id_logs_socket_get

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/v2/v3/logs/{app_id}/logs-socket'.format(app_id='app_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_vendor_addons_post(client):
    """Test case for vendor_addons_post

    
    """
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/v2/vendor//addons',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_vendor_apps_addon_id_logscollector_get(client):
    """Test case for vendor_apps_addon_id_logscollector_get

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/v2/vendor//apps/{addon_id}/logscollector'.format(addon_id='addon_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_vendor_apps_addon_id_migration_callback_put(client):
    """Test case for vendor_apps_addon_id_migration_callback_put

    
    """
    params = [('plan_id', 'plan_id_example'),
                    ('region', 'region_example')]
    headers = { 
    }
    response = await client.request(
        method='PUT',
        path='/v2/vendor/apps/{addon_id}/migration_callback'.format(addon_id='addon_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

