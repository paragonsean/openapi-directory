# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.addon import Addon
from openapi_server.models.application import Application
from openapi_server.models.avatar import Avatar
from openapi_server.models.body import Body
from openapi_server.models.change_password import ChangePassword
from openapi_server.models.conso import Conso
from openapi_server.models.consumer import Consumer
from openapi_server.models.credits import Credits
from openapi_server.models.deployment import Deployment
from openapi_server.models.env import Env
from openapi_server.models.instance import Instance
from openapi_server.models.key import Key
from openapi_server.models.linked_app_env import LinkedAppEnv
from openapi_server.models.list_env import ListEnv
from openapi_server.models.secret import Secret
from openapi_server.models.sso import Sso
from openapi_server.models.token import Token
from openapi_server.models.user import User
from openapi_server.models.vhost import Vhost
from openapi_server.models.wannabe_addon import WannabeAddon
from openapi_server.models.wannabe_application import WannabeApplication
from openapi_server.models.wannabe_consumer import WannabeConsumer
from openapi_server.models.wannabe_env import WannabeEnv
from openapi_server.models.wannabe_plan import WannabePlan
from openapi_server.models.wannabe_user import WannabeUser


pytestmark = pytest.mark.asyncio

async def test_delete_self_0(client):
    """Test case for delete_self_0

    
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

async def test_delete_self_addons_addon_id_1(client):
    """Test case for delete_self_addons_addon_id_1

    
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

async def test_delete_self_addons_addon_id_tags_tag_1(client):
    """Test case for delete_self_addons_addon_id_tags_tag_1

    
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

async def test_delete_self_applications_app_id_1(client):
    """Test case for delete_self_applications_app_id_1

    
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

async def test_delete_self_applications_app_id_addons_addon_id_2(client):
    """Test case for delete_self_applications_app_id_addons_addon_id_2

    
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

async def test_delete_self_applications_app_id_dependencies_dependency_id_1(client):
    """Test case for delete_self_applications_app_id_dependencies_dependency_id_1

    
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

async def test_delete_self_applications_app_id_deployments_deployment_id_instances_1(client):
    """Test case for delete_self_applications_app_id_deployments_deployment_id_instances_1

    
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

async def test_delete_self_applications_app_id_env_env_name_1(client):
    """Test case for delete_self_applications_app_id_env_env_name_1

    
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

async def test_delete_self_applications_app_id_instances_1(client):
    """Test case for delete_self_applications_app_id_instances_1

    
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

async def test_delete_self_applications_app_id_tags_tag_1(client):
    """Test case for delete_self_applications_app_id_tags_tag_1

    
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

async def test_delete_self_applications_app_id_vhosts_domain_1(client):
    """Test case for delete_self_applications_app_id_vhosts_domain_1

    
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

async def test_delete_self_applications_app_id_vhosts_favourite_1(client):
    """Test case for delete_self_applications_app_id_vhosts_favourite_1

    
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

async def test_delete_self_consumers_key_0(client):
    """Test case for delete_self_consumers_key_0

    
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

async def test_delete_self_emails_email_0(client):
    """Test case for delete_self_emails_email_0

    
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

async def test_delete_self_keys_key_0(client):
    """Test case for delete_self_keys_key_0

    
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

async def test_delete_self_payments_billings_bid_1(client):
    """Test case for delete_self_payments_billings_bid_1

    
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

async def test_delete_self_payments_methods_mid_1(client):
    """Test case for delete_self_payments_methods_mid_1

    
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

async def test_delete_self_payments_recurring_1(client):
    """Test case for delete_self_payments_recurring_1

    
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

async def test_delete_self_tokens_0(client):
    """Test case for delete_self_tokens_0

    
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

async def test_delete_self_tokens_token_0(client):
    """Test case for delete_self_tokens_token_0

    
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

async def test_get_self_0(client):
    """Test case for get_self_0

    
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

async def test_get_self_addons_1(client):
    """Test case for get_self_addons_1

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

async def test_get_self_addons_addon_id_1(client):
    """Test case for get_self_addons_addon_id_1

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

async def test_get_self_addons_addon_id_applications_2(client):
    """Test case for get_self_addons_addon_id_applications_2

    
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

async def test_get_self_addons_addon_id_env_1(client):
    """Test case for get_self_addons_addon_id_env_1

    
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

async def test_get_self_addons_addon_id_sso_1(client):
    """Test case for get_self_addons_addon_id_sso_1

    
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

async def test_get_self_addons_addon_id_tags_1(client):
    """Test case for get_self_addons_addon_id_tags_1

    
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

async def test_get_self_applications_1(client):
    """Test case for get_self_applications_1

    
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

async def test_get_self_applications_app_id_1(client):
    """Test case for get_self_applications_app_id_1

    
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

async def test_get_self_applications_app_id_addons_2(client):
    """Test case for get_self_applications_app_id_addons_2

    
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

async def test_get_self_applications_app_id_addons_env_2(client):
    """Test case for get_self_applications_app_id_addons_env_2

    
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

async def test_get_self_applications_app_id_dependencies_1(client):
    """Test case for get_self_applications_app_id_dependencies_1

    
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

async def test_get_self_applications_app_id_dependencies_dependency_id_1(client):
    """Test case for get_self_applications_app_id_dependencies_dependency_id_1

    
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

async def test_get_self_applications_app_id_dependents_1(client):
    """Test case for get_self_applications_app_id_dependents_1

    
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

async def test_get_self_applications_app_id_deployments_1(client):
    """Test case for get_self_applications_app_id_deployments_1

    
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

async def test_get_self_applications_app_id_env_1(client):
    """Test case for get_self_applications_app_id_env_1

    
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

async def test_get_self_applications_app_id_instances_1(client):
    """Test case for get_self_applications_app_id_instances_1

    
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

async def test_get_self_applications_app_id_tags_1(client):
    """Test case for get_self_applications_app_id_tags_1

    
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

async def test_get_self_applications_app_id_vhosts_1(client):
    """Test case for get_self_applications_app_id_vhosts_1

    
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

async def test_get_self_applications_app_id_vhosts_favourite_1(client):
    """Test case for get_self_applications_app_id_vhosts_favourite_1

    
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

async def test_get_self_confirmation_email_0(client):
    """Test case for get_self_confirmation_email_0

    
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

async def test_get_self_consumers_0(client):
    """Test case for get_self_consumers_0

    
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

async def test_get_self_consumers_key_0(client):
    """Test case for get_self_consumers_key_0

    
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

async def test_get_self_consumers_key_secret_0(client):
    """Test case for get_self_consumers_key_secret_0

    
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

async def test_get_self_consumptions_0(client):
    """Test case for get_self_consumptions_0

    
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

async def test_get_self_credits_0(client):
    """Test case for get_self_credits_0

    
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

async def test_get_self_emails_0(client):
    """Test case for get_self_emails_0

    
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

async def test_get_self_id_0(client):
    """Test case for get_self_id_0

    
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

async def test_get_self_instances_0(client):
    """Test case for get_self_instances_0

    
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

async def test_get_self_keys_0(client):
    """Test case for get_self_keys_0

    
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

async def test_get_self_payment_info_0(client):
    """Test case for get_self_payment_info_0

    
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

async def test_get_self_payments_billings_1(client):
    """Test case for get_self_payments_billings_1

    
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

async def test_get_self_payments_billings_bid_1(client):
    """Test case for get_self_payments_billings_bid_1

    
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

async def test_get_self_payments_billings_bid_pdf_1(client):
    """Test case for get_self_payments_billings_bid_pdf_1

    
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

async def test_get_self_payments_fullprice_price_1(client):
    """Test case for get_self_payments_fullprice_price_1

    
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

async def test_get_self_payments_methods_1(client):
    """Test case for get_self_payments_methods_1

    
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

async def test_get_self_tokens_0(client):
    """Test case for get_self_tokens_0

    
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

async def test_get_self_validate_email_0(client):
    """Test case for get_self_validate_email_0

    
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

async def test_post_self_addons_1(client):
    """Test case for post_self_addons_1

    
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

async def test_post_self_applications_1(client):
    """Test case for post_self_applications_1

    
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

async def test_post_self_applications_app_id_addons_2(client):
    """Test case for post_self_applications_app_id_addons_2

    
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

async def test_post_self_applications_app_id_instances_1(client):
    """Test case for post_self_applications_app_id_instances_1

    
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

async def test_post_self_consumers_0(client):
    """Test case for post_self_consumers_0

    
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

async def test_post_self_payments_billings_1(client):
    """Test case for post_self_payments_billings_1

    
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

async def test_post_self_payments_methods_1(client):
    """Test case for post_self_payments_methods_1

    
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

async def test_put_self_0(client):
    """Test case for put_self_0

    
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

async def test_put_self_addons_addon_id_1(client):
    """Test case for put_self_addons_addon_id_1

    
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

async def test_put_self_addons_addon_id_plan_1(client):
    """Test case for put_self_addons_addon_id_plan_1

    
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

async def test_put_self_addons_addon_id_tags_tag_1(client):
    """Test case for put_self_addons_addon_id_tags_tag_1

    
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

async def test_put_self_applications_app_id_1(client):
    """Test case for put_self_applications_app_id_1

    
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

async def test_put_self_applications_app_id_env_1(client):
    """Test case for put_self_applications_app_id_env_1

    
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

async def test_put_self_applications_app_id_env_env_name_1(client):
    """Test case for put_self_applications_app_id_env_env_name_1

    
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

async def test_put_self_applications_app_id_tags_tag_1(client):
    """Test case for put_self_applications_app_id_tags_tag_1

    
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

async def test_put_self_applications_app_id_vhosts_domain_1(client):
    """Test case for put_self_applications_app_id_vhosts_domain_1

    
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

async def test_put_self_applications_app_id_vhosts_favourite_1(client):
    """Test case for put_self_applications_app_id_vhosts_favourite_1

    
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

async def test_put_self_avatar_0(client):
    """Test case for put_self_avatar_0

    
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

async def test_put_self_change_password_0(client):
    """Test case for put_self_change_password_0

    
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

async def test_put_self_consumers_key_0(client):
    """Test case for put_self_consumers_key_0

    
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

async def test_put_self_emails_email_0(client):
    """Test case for put_self_emails_email_0

    
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

async def test_put_self_keys_key_0(client):
    """Test case for put_self_keys_key_0

    
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

async def test_put_self_payments_billings_bid_1(client):
    """Test case for put_self_payments_billings_bid_1

    
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

async def test_self_addons_preorders_post_1(client):
    """Test case for self_addons_preorders_post_1

    
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

async def test_self_applications_app_id_branch_put_1(client):
    """Test case for self_applications_app_id_branch_put_1

    
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

async def test_self_applications_app_id_branches_get_1(client):
    """Test case for self_applications_app_id_branches_get_1

    
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

async def test_self_applications_app_id_buildflavor_put_1(client):
    """Test case for self_applications_app_id_buildflavor_put_1

    
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

async def test_self_applications_app_id_dependencies_env_get_1(client):
    """Test case for self_applications_app_id_dependencies_env_get_1

    
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

async def test_self_applications_app_id_deployments_deployment_id_get_1(client):
    """Test case for self_applications_app_id_deployments_deployment_id_get_1

    
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

async def test_self_applications_app_id_exposed_env_get_1(client):
    """Test case for self_applications_app_id_exposed_env_get_1

    
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

async def test_self_applications_app_id_exposed_env_put_1(client):
    """Test case for self_applications_app_id_exposed_env_put_1

    
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

async def test_self_applications_app_id_instances_instance_id_get_1(client):
    """Test case for self_applications_app_id_instances_instance_id_get_1

    
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

async def test_self_cli_tokens_get_0(client):
    """Test case for self_cli_tokens_get_0

    
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

async def test_self_mfa_kind_backupcodes_get_0(client):
    """Test case for self_mfa_kind_backupcodes_get_0

    
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

async def test_self_mfa_kind_confirmation_post_0(client):
    """Test case for self_mfa_kind_confirmation_post_0

    
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

async def test_self_mfa_kind_delete_0(client):
    """Test case for self_mfa_kind_delete_0

    
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

async def test_self_mfa_kind_post_0(client):
    """Test case for self_mfa_kind_post_0

    
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

async def test_self_mfa_kind_put_0(client):
    """Test case for self_mfa_kind_put_0

    
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

async def test_self_payments_methods_default_get_1(client):
    """Test case for self_payments_methods_default_get_1

    
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

async def test_self_payments_methods_default_put_1(client):
    """Test case for self_payments_methods_default_put_1

    
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

async def test_self_payments_monthlyinvoice_get_1(client):
    """Test case for self_payments_monthlyinvoice_get_1

    
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

async def test_self_payments_monthlyinvoice_maxcredit_put_1(client):
    """Test case for self_payments_monthlyinvoice_maxcredit_put_1

    
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

async def test_self_payments_recurring_get_1(client):
    """Test case for self_payments_recurring_get_1

    
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

async def test_self_payments_tokens_stripe_get_1(client):
    """Test case for self_payments_tokens_stripe_get_1

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/v2/self/payments/tokens/stripe',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

