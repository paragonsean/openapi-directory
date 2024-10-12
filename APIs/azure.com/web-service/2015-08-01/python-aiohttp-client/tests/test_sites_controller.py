# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.backup_item import BackupItem
from openapi_server.models.backup_item_collection import BackupItemCollection
from openapi_server.models.backup_request import BackupRequest
from openapi_server.models.connection_string_dictionary import ConnectionStringDictionary
from openapi_server.models.csm_publishing_profile_options import CsmPublishingProfileOptions
from openapi_server.models.csm_site_recovery_entity import CsmSiteRecoveryEntity
from openapi_server.models.csm_slot_entity import CsmSlotEntity
from openapi_server.models.csm_usage_quota_collection import CsmUsageQuotaCollection
from openapi_server.models.deleted_site_collection import DeletedSiteCollection
from openapi_server.models.deployment import Deployment
from openapi_server.models.deployment_collection import DeploymentCollection
from openapi_server.models.host_name_binding import HostNameBinding
from openapi_server.models.host_name_binding_collection import HostNameBindingCollection
from openapi_server.models.metric_definition_collection import MetricDefinitionCollection
from openapi_server.models.network_features import NetworkFeatures
from openapi_server.models.premier_add_on_request import PremierAddOnRequest
from openapi_server.models.relay_service_connection_entity import RelayServiceConnectionEntity
from openapi_server.models.resource_metric_collection import ResourceMetricCollection
from openapi_server.models.restore_request import RestoreRequest
from openapi_server.models.restore_response import RestoreResponse
from openapi_server.models.site import Site
from openapi_server.models.site_auth_settings import SiteAuthSettings
from openapi_server.models.site_cloneability import SiteCloneability
from openapi_server.models.site_collection import SiteCollection
from openapi_server.models.site_config import SiteConfig
from openapi_server.models.site_instance_collection import SiteInstanceCollection
from openapi_server.models.site_logs_config import SiteLogsConfig
from openapi_server.models.site_source_control import SiteSourceControl
from openapi_server.models.slot_config_names_resource import SlotConfigNamesResource
from openapi_server.models.slot_difference_collection import SlotDifferenceCollection
from openapi_server.models.string_dictionary import StringDictionary
from openapi_server.models.user import User
from openapi_server.models.vnet_gateway import VnetGateway
from openapi_server.models.vnet_info import VnetInfo


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_sites_add_site_premier_add_on(client):
    """Test case for sites_add_site_premier_add_on

    
    """
    premier_add_on = {"location":"location","sku":{"size":"size","tier":"tier","name":"name","family":"family","capacity":0},"plan":{"product":"product","name":"name","promotionCode":"promotionCode","publisher":"publisher","version":"version"},"properties":"{}","tags":{"key":"tags"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/premieraddons/{premier_add_on_name}'.format(resource_group_name='resource_group_name_example', name='name_example', premier_add_on_name='premier_add_on_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=premier_add_on,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_sites_add_site_premier_add_on_slot(client):
    """Test case for sites_add_site_premier_add_on_slot

    
    """
    premier_add_on = {"location":"location","sku":{"size":"size","tier":"tier","name":"name","family":"family","capacity":0},"plan":{"product":"product","name":"name","promotionCode":"promotionCode","publisher":"publisher","version":"version"},"properties":"{}","tags":{"key":"tags"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/premieraddons/{premier_add_on_name}'.format(resource_group_name='resource_group_name_example', name='name_example', premier_add_on_name='premier_add_on_name_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=premier_add_on,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_sites_apply_slot_config_slot(client):
    """Test case for sites_apply_slot_config_slot

    Applies the configuration settings from the target slot onto the current slot
    """
    slot_swap_entity = {"preserveVnet":True,"targetSlot":"targetSlot"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/applySlotConfig'.format(resource_group_name='resource_group_name_example', name='name_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=slot_swap_entity,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_sites_apply_slot_config_to_production(client):
    """Test case for sites_apply_slot_config_to_production

    Applies the configuration settings from the target slot onto the current slot
    """
    slot_swap_entity = {"preserveVnet":True,"targetSlot":"targetSlot"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/applySlotConfig'.format(resource_group_name='resource_group_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=slot_swap_entity,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_sites_backup_site(client):
    """Test case for sites_backup_site

    Creates web app backup
    """
    request = {"properties":"{}"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/backup'.format(resource_group_name='resource_group_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=request,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_sites_backup_site_slot(client):
    """Test case for sites_backup_site_slot

    Creates web app backup
    """
    request = {"properties":"{}"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/backup'.format(resource_group_name='resource_group_name_example', name='name_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=request,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_sites_create_deployment(client):
    """Test case for sites_create_deployment

    Create a deployment
    """
    deployment = {"properties":"{}"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/deployments/{id}'.format(resource_group_name='resource_group_name_example', name='name_example', id='id_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=deployment,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_sites_create_deployment_slot(client):
    """Test case for sites_create_deployment_slot

    Create a deployment
    """
    deployment = {"properties":"{}"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/deployments/{id}'.format(resource_group_name='resource_group_name_example', name='name_example', id='id_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=deployment,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_sites_create_instance_deployment(client):
    """Test case for sites_create_instance_deployment

    Create a deployment
    """
    deployment = {"properties":"{}"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/instances/{instance_id}/deployments/{id}'.format(resource_group_name='resource_group_name_example', name='name_example', id='id_example', instance_id='instance_id_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=deployment,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_sites_create_instance_deployment_slot(client):
    """Test case for sites_create_instance_deployment_slot

    Create a deployment
    """
    deployment = {"properties":"{}"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/instances/{instance_id}/deployments/{id}'.format(resource_group_name='resource_group_name_example', name='name_example', id='id_example', slot='slot_example', instance_id='instance_id_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=deployment,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_sites_create_or_update_site(client):
    """Test case for sites_create_or_update_site

    Creates a new web app or modifies an existing web app.
    """
    site_envelope = {"properties":"{}"}
    params = [('skipDnsRegistration', 'skip_dns_registration_example'),
                    ('skipCustomDomainVerification', 'skip_custom_domain_verification_example'),
                    ('forceDnsRegistration', 'force_dns_registration_example'),
                    ('ttlInSeconds', 'ttl_in_seconds_example'),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}'.format(resource_group_name='resource_group_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=site_envelope,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_sites_create_or_update_site_config(client):
    """Test case for sites_create_or_update_site_config

    Update the configuration of web app
    """
    site_config = {"properties":"{}"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/config/web'.format(resource_group_name='resource_group_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=site_config,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_sites_create_or_update_site_config_slot(client):
    """Test case for sites_create_or_update_site_config_slot

    Update the configuration of web app
    """
    site_config = {"properties":"{}"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/config/web'.format(resource_group_name='resource_group_name_example', name='name_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=site_config,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_sites_create_or_update_site_host_name_binding(client):
    """Test case for sites_create_or_update_site_host_name_binding

    Creates a web app hostname binding
    """
    host_name_binding = {"properties":"{}"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/hostNameBindings/{host_name}'.format(resource_group_name='resource_group_name_example', name='name_example', host_name='host_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=host_name_binding,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_sites_create_or_update_site_host_name_binding_slot(client):
    """Test case for sites_create_or_update_site_host_name_binding_slot

    Creates a web app hostname binding
    """
    host_name_binding = {"properties":"{}"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/hostNameBindings/{host_name}'.format(resource_group_name='resource_group_name_example', name='name_example', host_name='host_name_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=host_name_binding,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_sites_create_or_update_site_relay_service_connection(client):
    """Test case for sites_create_or_update_site_relay_service_connection

    Creates a new association to a BizTalk Hybrid Connection, or updates an existing one.
    """
    connection_envelope = {"properties":"{}"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/hybridconnection/{entity_name}'.format(resource_group_name='resource_group_name_example', name='name_example', entity_name='entity_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=connection_envelope,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_sites_create_or_update_site_relay_service_connection_slot(client):
    """Test case for sites_create_or_update_site_relay_service_connection_slot

    Creates a new association to a BizTalk Hybrid Connection, or updates an existing one.
    """
    connection_envelope = {"properties":"{}"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/hybridconnection/{entity_name}'.format(resource_group_name='resource_group_name_example', name='name_example', entity_name='entity_name_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=connection_envelope,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_sites_create_or_update_site_slot(client):
    """Test case for sites_create_or_update_site_slot

    Creates a new web app or modifies an existing web app.
    """
    site_envelope = {"properties":"{}"}
    params = [('skipDnsRegistration', 'skip_dns_registration_example'),
                    ('skipCustomDomainVerification', 'skip_custom_domain_verification_example'),
                    ('forceDnsRegistration', 'force_dns_registration_example'),
                    ('ttlInSeconds', 'ttl_in_seconds_example'),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}'.format(resource_group_name='resource_group_name_example', name='name_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=site_envelope,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_sites_create_or_update_site_source_control(client):
    """Test case for sites_create_or_update_site_source_control

    Update the source control configuration of web app
    """
    site_source_control = {"properties":"{}"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/sourcecontrols/web'.format(resource_group_name='resource_group_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=site_source_control,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_sites_create_or_update_site_source_control_slot(client):
    """Test case for sites_create_or_update_site_source_control_slot

    Update the source control configuration of web app
    """
    site_source_control = {"properties":"{}"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/sourcecontrols/web'.format(resource_group_name='resource_group_name_example', name='name_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=site_source_control,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_sites_create_or_update_site_vnet_connection(client):
    """Test case for sites_create_or_update_site_vnet_connection

    Adds a Virtual Network Connection or updates it's properties.
    """
    connection_envelope = {"properties":"{}"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/virtualNetworkConnections/{vnet_name}'.format(resource_group_name='resource_group_name_example', name='name_example', vnet_name='vnet_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=connection_envelope,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_sites_create_or_update_site_vnet_connection_gateway(client):
    """Test case for sites_create_or_update_site_vnet_connection_gateway

    Updates the Virtual Network Gateway.
    """
    connection_envelope = {"properties":"{}"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/virtualNetworkConnections/{vnet_name}/gateways/{gateway_name}'.format(resource_group_name='resource_group_name_example', name='name_example', vnet_name='vnet_name_example', gateway_name='gateway_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=connection_envelope,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_sites_create_or_update_site_vnet_connection_gateway_slot(client):
    """Test case for sites_create_or_update_site_vnet_connection_gateway_slot

    Updates the Virtual Network Gateway.
    """
    connection_envelope = {"properties":"{}"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/virtualNetworkConnections/{vnet_name}/gateways/{gateway_name}'.format(resource_group_name='resource_group_name_example', name='name_example', vnet_name='vnet_name_example', gateway_name='gateway_name_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=connection_envelope,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_sites_create_or_update_site_vnet_connection_slot(client):
    """Test case for sites_create_or_update_site_vnet_connection_slot

    Adds a Virtual Network Connection or updates it's properties.
    """
    connection_envelope = {"properties":"{}"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/virtualNetworkConnections/{vnet_name}'.format(resource_group_name='resource_group_name_example', name='name_example', vnet_name='vnet_name_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=connection_envelope,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sites_delete_backup(client):
    """Test case for sites_delete_backup

    Deletes a backup from Azure Storage
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/backups/{backup_id}'.format(resource_group_name='resource_group_name_example', name='name_example', backup_id='backup_id_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sites_delete_backup_slot(client):
    """Test case for sites_delete_backup_slot

    Deletes a backup from Azure Storage
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/backups/{backup_id}'.format(resource_group_name='resource_group_name_example', name='name_example', backup_id='backup_id_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sites_delete_deployment(client):
    """Test case for sites_delete_deployment

    Delete the deployment
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/deployments/{id}'.format(resource_group_name='resource_group_name_example', name='name_example', id='id_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sites_delete_deployment_slot(client):
    """Test case for sites_delete_deployment_slot

    Delete the deployment
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/deployments/{id}'.format(resource_group_name='resource_group_name_example', name='name_example', id='id_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sites_delete_instance_deployment(client):
    """Test case for sites_delete_instance_deployment

    Delete the deployment
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/instances/{instance_id}/deployments/{id}'.format(resource_group_name='resource_group_name_example', name='name_example', id='id_example', instance_id='instance_id_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sites_delete_instance_deployment_slot(client):
    """Test case for sites_delete_instance_deployment_slot

    Delete the deployment
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/instances/{instance_id}/deployments/{id}'.format(resource_group_name='resource_group_name_example', name='name_example', id='id_example', slot='slot_example', instance_id='instance_id_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sites_delete_site(client):
    """Test case for sites_delete_site

    Deletes a web app
    """
    params = [('deleteMetrics', 'delete_metrics_example'),
                    ('deleteEmptyServerFarm', 'delete_empty_server_farm_example'),
                    ('skipDnsRegistration', 'skip_dns_registration_example'),
                    ('deleteAllSlots', 'delete_all_slots_example'),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}'.format(resource_group_name='resource_group_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sites_delete_site_host_name_binding(client):
    """Test case for sites_delete_site_host_name_binding

    Deletes a host name binding
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/hostNameBindings/{host_name}'.format(resource_group_name='resource_group_name_example', name='name_example', host_name='host_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sites_delete_site_host_name_binding_slot(client):
    """Test case for sites_delete_site_host_name_binding_slot

    Deletes a host name binding
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/hostNameBindings/{host_name}'.format(resource_group_name='resource_group_name_example', name='name_example', slot='slot_example', host_name='host_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sites_delete_site_premier_add_on(client):
    """Test case for sites_delete_site_premier_add_on

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/premieraddons/{premier_add_on_name}'.format(resource_group_name='resource_group_name_example', name='name_example', premier_add_on_name='premier_add_on_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sites_delete_site_premier_add_on_slot(client):
    """Test case for sites_delete_site_premier_add_on_slot

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/premieraddons/{premier_add_on_name}'.format(resource_group_name='resource_group_name_example', name='name_example', premier_add_on_name='premier_add_on_name_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sites_delete_site_relay_service_connection(client):
    """Test case for sites_delete_site_relay_service_connection

    Removes the association to a BizTalk Hybrid Connection, identified by its entity name.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/hybridconnection/{entity_name}'.format(resource_group_name='resource_group_name_example', name='name_example', entity_name='entity_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sites_delete_site_relay_service_connection_slot(client):
    """Test case for sites_delete_site_relay_service_connection_slot

    Removes the association to a BizTalk Hybrid Connection, identified by its entity name.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/hybridconnection/{entity_name}'.format(resource_group_name='resource_group_name_example', name='name_example', entity_name='entity_name_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sites_delete_site_slot(client):
    """Test case for sites_delete_site_slot

    Deletes a web app
    """
    params = [('deleteMetrics', 'delete_metrics_example'),
                    ('deleteEmptyServerFarm', 'delete_empty_server_farm_example'),
                    ('skipDnsRegistration', 'skip_dns_registration_example'),
                    ('deleteAllSlots', 'delete_all_slots_example'),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}'.format(resource_group_name='resource_group_name_example', name='name_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sites_delete_site_source_control(client):
    """Test case for sites_delete_site_source_control

    Delete source control configuration of web app
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/sourcecontrols/web'.format(resource_group_name='resource_group_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sites_delete_site_source_control_slot(client):
    """Test case for sites_delete_site_source_control_slot

    Delete source control configuration of web app
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/sourcecontrols/web'.format(resource_group_name='resource_group_name_example', name='name_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sites_delete_site_vnet_connection(client):
    """Test case for sites_delete_site_vnet_connection

    Removes the specified Virtual Network Connection association from this web app.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/virtualNetworkConnections/{vnet_name}'.format(resource_group_name='resource_group_name_example', name='name_example', vnet_name='vnet_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sites_delete_site_vnet_connection_slot(client):
    """Test case for sites_delete_site_vnet_connection_slot

    Removes the specified Virtual Network Connection association from this web app.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/virtualNetworkConnections/{vnet_name}'.format(resource_group_name='resource_group_name_example', name='name_example', vnet_name='vnet_name_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_sites_discover_site_restore(client):
    """Test case for sites_discover_site_restore

    Discovers existing web app backups that can be restored
    """
    request = {"properties":"{}"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/backups/discover'.format(resource_group_name='resource_group_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=request,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_sites_discover_site_restore_slot(client):
    """Test case for sites_discover_site_restore_slot

    Discovers existing web app backups that can be restored
    """
    request = {"properties":"{}"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/backups/discover'.format(resource_group_name='resource_group_name_example', name='name_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=request,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sites_generate_new_site_publishing_password(client):
    """Test case for sites_generate_new_site_publishing_password

    Generates new random app publishing password
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/newpassword'.format(resource_group_name='resource_group_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sites_generate_new_site_publishing_password_slot(client):
    """Test case for sites_generate_new_site_publishing_password_slot

    Generates new random app publishing password
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/newpassword'.format(resource_group_name='resource_group_name_example', name='name_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sites_get_deleted_sites(client):
    """Test case for sites_get_deleted_sites

    Gets deleted web apps in subscription
    """
    params = [('propertiesToInclude', 'properties_to_include_example'),
                    ('includeSiteTypes', 'include_site_types_example'),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/deletedSites'.format(resource_group_name='resource_group_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sites_get_deployment(client):
    """Test case for sites_get_deployment

    Get the deployment
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/deployments/{id}'.format(resource_group_name='resource_group_name_example', name='name_example', id='id_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sites_get_deployment_slot(client):
    """Test case for sites_get_deployment_slot

    Get the deployment
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/deployments/{id}'.format(resource_group_name='resource_group_name_example', name='name_example', id='id_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sites_get_deployments(client):
    """Test case for sites_get_deployments

    List deployments
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/deployments'.format(resource_group_name='resource_group_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sites_get_deployments_slot(client):
    """Test case for sites_get_deployments_slot

    List deployments
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/deployments'.format(resource_group_name='resource_group_name_example', name='name_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sites_get_instance_deployment(client):
    """Test case for sites_get_instance_deployment

    Get the deployment
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/instances/{instance_id}/deployments/{id}'.format(resource_group_name='resource_group_name_example', name='name_example', id='id_example', instance_id='instance_id_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sites_get_instance_deployment_slot(client):
    """Test case for sites_get_instance_deployment_slot

    Get the deployment
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/instances/{instance_id}/deployments/{id}'.format(resource_group_name='resource_group_name_example', name='name_example', id='id_example', slot='slot_example', instance_id='instance_id_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sites_get_instance_deployments(client):
    """Test case for sites_get_instance_deployments

    List deployments
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/instances/{instance_id}/deployments'.format(resource_group_name='resource_group_name_example', name='name_example', instance_id='instance_id_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sites_get_instance_deployments_slot(client):
    """Test case for sites_get_instance_deployments_slot

    List deployments
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/instances/{instance_id}/deployments'.format(resource_group_name='resource_group_name_example', name='name_example', slot='slot_example', instance_id='instance_id_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sites_get_site(client):
    """Test case for sites_get_site

    Get details of a web app
    """
    params = [('propertiesToInclude', 'properties_to_include_example'),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}'.format(resource_group_name='resource_group_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sites_get_site_backup_configuration(client):
    """Test case for sites_get_site_backup_configuration

    Gets the backup configuration for a web app
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/config/backup/list'.format(resource_group_name='resource_group_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sites_get_site_backup_configuration_slot(client):
    """Test case for sites_get_site_backup_configuration_slot

    Gets the backup configuration for a web app
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/config/backup/list'.format(resource_group_name='resource_group_name_example', name='name_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sites_get_site_backup_status(client):
    """Test case for sites_get_site_backup_status

    Gets status of a web app backup that may be in progress.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/backups/{backup_id}'.format(resource_group_name='resource_group_name_example', name='name_example', backup_id='backup_id_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_sites_get_site_backup_status_secrets(client):
    """Test case for sites_get_site_backup_status_secrets

    Gets status of a web app backup that may be in progress, including secrets associated with the backup, such as the Azure Storage SAS URL. Also can be used to update the SAS URL for the backup if a new URL is passed in the request body.
    """
    request = {"properties":"{}"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/backups/{backup_id}/list'.format(resource_group_name='resource_group_name_example', name='name_example', backup_id='backup_id_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=request,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_sites_get_site_backup_status_secrets_slot(client):
    """Test case for sites_get_site_backup_status_secrets_slot

    Gets status of a web app backup that may be in progress, including secrets associated with the backup, such as the Azure Storage SAS URL. Also can be used to update the SAS URL for the backup if a new URL is passed in the request body.
    """
    request = {"properties":"{}"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/backups/{backup_id}/list'.format(resource_group_name='resource_group_name_example', name='name_example', backup_id='backup_id_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=request,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sites_get_site_backup_status_slot(client):
    """Test case for sites_get_site_backup_status_slot

    Gets status of a web app backup that may be in progress.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/backups/{backup_id}'.format(resource_group_name='resource_group_name_example', name='name_example', backup_id='backup_id_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sites_get_site_config(client):
    """Test case for sites_get_site_config

    Gets the configuration of the web app
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/config/web'.format(resource_group_name='resource_group_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sites_get_site_config_slot(client):
    """Test case for sites_get_site_config_slot

    Gets the configuration of the web app
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/config/web'.format(resource_group_name='resource_group_name_example', name='name_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sites_get_site_host_name_binding(client):
    """Test case for sites_get_site_host_name_binding

    Get web app binding for a hostname
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/hostNameBindings/{host_name}'.format(resource_group_name='resource_group_name_example', name='name_example', host_name='host_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sites_get_site_host_name_binding_slot(client):
    """Test case for sites_get_site_host_name_binding_slot

    Get web app binding for a hostname
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/hostNameBindings/{host_name}'.format(resource_group_name='resource_group_name_example', name='name_example', slot='slot_example', host_name='host_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sites_get_site_host_name_bindings(client):
    """Test case for sites_get_site_host_name_bindings

    Get web app hostname bindings
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/hostNameBindings'.format(resource_group_name='resource_group_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sites_get_site_host_name_bindings_slot(client):
    """Test case for sites_get_site_host_name_bindings_slot

    Get web app hostname bindings
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/hostNameBindings'.format(resource_group_name='resource_group_name_example', name='name_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sites_get_site_instance_identifiers(client):
    """Test case for sites_get_site_instance_identifiers

    Gets all instance of a web app
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/instances'.format(resource_group_name='resource_group_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sites_get_site_instance_identifiers_slot(client):
    """Test case for sites_get_site_instance_identifiers_slot

    Gets all instance of a web app
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/instances'.format(resource_group_name='resource_group_name_example', name='name_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sites_get_site_logs_config(client):
    """Test case for sites_get_site_logs_config

    Gets the web app logs configuration
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/config/logs'.format(resource_group_name='resource_group_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sites_get_site_logs_config_slot(client):
    """Test case for sites_get_site_logs_config_slot

    Gets the web app logs configuration
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/config/logs'.format(resource_group_name='resource_group_name_example', name='name_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sites_get_site_metric_definitions(client):
    """Test case for sites_get_site_metric_definitions

    Gets metric definitions for web app
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/metricdefinitions'.format(resource_group_name='resource_group_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sites_get_site_metric_definitions_slot(client):
    """Test case for sites_get_site_metric_definitions_slot

    Gets metric definitions for web app
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/metricdefinitions'.format(resource_group_name='resource_group_name_example', name='name_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sites_get_site_metrics(client):
    """Test case for sites_get_site_metrics

    Gets metrics for web app
    """
    params = [('details', True),
                    ('$filter', 'filter_example'),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/metrics'.format(resource_group_name='resource_group_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sites_get_site_metrics_slot(client):
    """Test case for sites_get_site_metrics_slot

    Gets metrics for web app
    """
    params = [('details', True),
                    ('$filter', 'filter_example'),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/metrics'.format(resource_group_name='resource_group_name_example', name='name_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sites_get_site_network_features(client):
    """Test case for sites_get_site_network_features

    Retrieves a view of all network features in use on this web app.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/networkFeatures/{view}'.format(resource_group_name='resource_group_name_example', name='name_example', view='view_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sites_get_site_network_features_slot(client):
    """Test case for sites_get_site_network_features_slot

    Retrieves a view of all network features in use on this web app.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/networkFeatures/{view}'.format(resource_group_name='resource_group_name_example', name='name_example', view='view_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sites_get_site_operation(client):
    """Test case for sites_get_site_operation

    Gets the operation for a web app
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/operationresults/{operation_id}'.format(resource_group_name='resource_group_name_example', name='name_example', operation_id='operation_id_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sites_get_site_operation_slot(client):
    """Test case for sites_get_site_operation_slot

    Gets the operation for a web app
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/operationresults/{operation_id}'.format(resource_group_name='resource_group_name_example', name='name_example', operation_id='operation_id_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sites_get_site_premier_add_on(client):
    """Test case for sites_get_site_premier_add_on

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/premieraddons/{premier_add_on_name}'.format(resource_group_name='resource_group_name_example', name='name_example', premier_add_on_name='premier_add_on_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sites_get_site_premier_add_on_slot(client):
    """Test case for sites_get_site_premier_add_on_slot

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/premieraddons/{premier_add_on_name}'.format(resource_group_name='resource_group_name_example', name='name_example', premier_add_on_name='premier_add_on_name_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sites_get_site_relay_service_connection(client):
    """Test case for sites_get_site_relay_service_connection

    Retrieves a BizTalk Hybrid Connection identified by its entity name.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/hybridconnection/{entity_name}'.format(resource_group_name='resource_group_name_example', name='name_example', entity_name='entity_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sites_get_site_relay_service_connection_slot(client):
    """Test case for sites_get_site_relay_service_connection_slot

    Retrieves a BizTalk Hybrid Connection identified by its entity name.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/hybridconnection/{entity_name}'.format(resource_group_name='resource_group_name_example', name='name_example', entity_name='entity_name_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sites_get_site_slot(client):
    """Test case for sites_get_site_slot

    Get details of a web app
    """
    params = [('propertiesToInclude', 'properties_to_include_example'),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}'.format(resource_group_name='resource_group_name_example', name='name_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sites_get_site_slots(client):
    """Test case for sites_get_site_slots

    Gets all the slots for a web apps
    """
    params = [('propertiesToInclude', 'properties_to_include_example'),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots'.format(resource_group_name='resource_group_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sites_get_site_snapshots(client):
    """Test case for sites_get_site_snapshots

    Returns all Snapshots to the user.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/snapshots'.format(resource_group_name='resource_group_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sites_get_site_snapshots_slot(client):
    """Test case for sites_get_site_snapshots_slot

    Returns all Snapshots to the user.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/snapshots'.format(resource_group_name='resource_group_name_example', name='name_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sites_get_site_source_control(client):
    """Test case for sites_get_site_source_control

    Get the source control configuration of web app
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/sourcecontrols/web'.format(resource_group_name='resource_group_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sites_get_site_source_control_slot(client):
    """Test case for sites_get_site_source_control_slot

    Get the source control configuration of web app
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/sourcecontrols/web'.format(resource_group_name='resource_group_name_example', name='name_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sites_get_site_usages(client):
    """Test case for sites_get_site_usages

    Gets the quota usage numbers for web app
    """
    params = [('$filter', 'filter_example'),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/usages'.format(resource_group_name='resource_group_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sites_get_site_usages_slot(client):
    """Test case for sites_get_site_usages_slot

    Gets the quota usage numbers for web app
    """
    params = [('$filter', 'filter_example'),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/usages'.format(resource_group_name='resource_group_name_example', name='name_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sites_get_site_vnet_connection(client):
    """Test case for sites_get_site_vnet_connection

    Retrieves a specific Virtual Network Connection associated with this web app.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/virtualNetworkConnections/{vnet_name}'.format(resource_group_name='resource_group_name_example', name='name_example', vnet_name='vnet_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sites_get_site_vnet_connection_slot(client):
    """Test case for sites_get_site_vnet_connection_slot

    Retrieves a specific Virtual Network Connection associated with this web app.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/virtualNetworkConnections/{vnet_name}'.format(resource_group_name='resource_group_name_example', name='name_example', vnet_name='vnet_name_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sites_get_site_vnet_connections(client):
    """Test case for sites_get_site_vnet_connections

    Retrieves a list of all Virtual Network Connections associated with this web app.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/virtualNetworkConnections'.format(resource_group_name='resource_group_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sites_get_site_vnet_connections_slot(client):
    """Test case for sites_get_site_vnet_connections_slot

    Retrieves a list of all Virtual Network Connections associated with this web app.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/virtualNetworkConnections'.format(resource_group_name='resource_group_name_example', name='name_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sites_get_site_vnet_gateway(client):
    """Test case for sites_get_site_vnet_gateway

    Retrieves a Virtual Network connection gateway associated with this web app and virtual network.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/virtualNetworkConnections/{vnet_name}/gateways/{gateway_name}'.format(resource_group_name='resource_group_name_example', name='name_example', vnet_name='vnet_name_example', gateway_name='gateway_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sites_get_site_vnet_gateway_slot(client):
    """Test case for sites_get_site_vnet_gateway_slot

    Retrieves a Virtual Network connection gateway associated with this web app and virtual network.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/virtualNetworkConnections/{vnet_name}/gateways/{gateway_name}'.format(resource_group_name='resource_group_name_example', name='name_example', vnet_name='vnet_name_example', gateway_name='gateway_name_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sites_get_sites(client):
    """Test case for sites_get_sites

    Gets the web apps for a subscription in the specified resource group
    """
    params = [('propertiesToInclude', 'properties_to_include_example'),
                    ('includeSiteTypes', 'include_site_types_example'),
                    ('includeSlots', True),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites'.format(resource_group_name='resource_group_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sites_get_slot_config_names(client):
    """Test case for sites_get_slot_config_names

    Gets the names of application settings and connection string that remain with the slot during swap operation
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/config/slotConfigNames'.format(resource_group_name='resource_group_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_sites_get_slots_differences_from_production(client):
    """Test case for sites_get_slots_differences_from_production

    Get the difference in configuration settings between two web app slots
    """
    slot_swap_entity = {"preserveVnet":True,"targetSlot":"targetSlot"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slotsdiffs'.format(resource_group_name='resource_group_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=slot_swap_entity,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_sites_get_slots_differences_slot(client):
    """Test case for sites_get_slots_differences_slot

    Get the difference in configuration settings between two web app slots
    """
    slot_swap_entity = {"preserveVnet":True,"targetSlot":"targetSlot"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/slotsdiffs'.format(resource_group_name='resource_group_name_example', name='name_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=slot_swap_entity,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sites_is_site_cloneable(client):
    """Test case for sites_is_site_cloneable

    Creates a new web app or modifies an existing web app.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/iscloneable'.format(resource_group_name='resource_group_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sites_is_site_cloneable_slot(client):
    """Test case for sites_is_site_cloneable_slot

    Creates a new web app or modifies an existing web app.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/iscloneable'.format(resource_group_name='resource_group_name_example', name='name_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sites_list_site_app_settings(client):
    """Test case for sites_list_site_app_settings

    Gets the application settings of web app
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/config/appsettings/list'.format(resource_group_name='resource_group_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sites_list_site_app_settings_slot(client):
    """Test case for sites_list_site_app_settings_slot

    Gets the application settings of web app
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/config/appsettings/list'.format(resource_group_name='resource_group_name_example', name='name_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sites_list_site_auth_settings(client):
    """Test case for sites_list_site_auth_settings

    Gets the Authentication / Authorization settings associated with web app
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/config/authsettings/list'.format(resource_group_name='resource_group_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sites_list_site_auth_settings_slot(client):
    """Test case for sites_list_site_auth_settings_slot

    Gets the Authentication / Authorization settings associated with web app
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/config/authsettings/list'.format(resource_group_name='resource_group_name_example', name='name_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sites_list_site_backups(client):
    """Test case for sites_list_site_backups

    Lists all available backups for web app
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/backups'.format(resource_group_name='resource_group_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sites_list_site_backups_slot(client):
    """Test case for sites_list_site_backups_slot

    Lists all available backups for web app
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/backups'.format(resource_group_name='resource_group_name_example', name='name_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sites_list_site_connection_strings(client):
    """Test case for sites_list_site_connection_strings

    Gets the connection strings associated with web app
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/config/connectionstrings/list'.format(resource_group_name='resource_group_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sites_list_site_connection_strings_slot(client):
    """Test case for sites_list_site_connection_strings_slot

    Gets the connection strings associated with web app
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/config/connectionstrings/list'.format(resource_group_name='resource_group_name_example', name='name_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sites_list_site_metadata(client):
    """Test case for sites_list_site_metadata

    Gets the web app meta data.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/config/metadata/list'.format(resource_group_name='resource_group_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sites_list_site_metadata_slot(client):
    """Test case for sites_list_site_metadata_slot

    Gets the web app meta data.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/config/metadata/list'.format(resource_group_name='resource_group_name_example', name='name_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sites_list_site_premier_add_ons(client):
    """Test case for sites_list_site_premier_add_ons

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/premieraddons'.format(resource_group_name='resource_group_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sites_list_site_premier_add_ons_slot(client):
    """Test case for sites_list_site_premier_add_ons_slot

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/premieraddons'.format(resource_group_name='resource_group_name_example', name='name_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sites_list_site_publishing_credentials(client):
    """Test case for sites_list_site_publishing_credentials

    Gets the web app publishing credentials
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/config/publishingcredentials/list'.format(resource_group_name='resource_group_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sites_list_site_publishing_credentials_slot(client):
    """Test case for sites_list_site_publishing_credentials_slot

    Gets the web app publishing credentials
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/config/publishingcredentials/list'.format(resource_group_name='resource_group_name_example', name='name_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_sites_list_site_publishing_profile_xml(client):
    """Test case for sites_list_site_publishing_profile_xml

    Gets the publishing profile for web app
    """
    options = {"format":"format"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/publishxml'.format(resource_group_name='resource_group_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=options,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_sites_list_site_publishing_profile_xml_slot(client):
    """Test case for sites_list_site_publishing_profile_xml_slot

    Gets the publishing profile for web app
    """
    options = {"format":"format"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/publishxml'.format(resource_group_name='resource_group_name_example', name='name_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=options,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sites_list_site_relay_service_connections(client):
    """Test case for sites_list_site_relay_service_connections

    Retrieves all BizTalk Hybrid Connections associated with this web app.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/hybridconnection'.format(resource_group_name='resource_group_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sites_list_site_relay_service_connections_slot(client):
    """Test case for sites_list_site_relay_service_connections_slot

    Retrieves all BizTalk Hybrid Connections associated with this web app.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/hybridconnection'.format(resource_group_name='resource_group_name_example', name='name_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_sites_recover_site(client):
    """Test case for sites_recover_site

    Recovers a deleted web app
    """
    recovery_entity = {"slotName":"slotName","recoverConfig":True,"siteName":"siteName","snapshotTime":"2000-01-23T04:56:07.000+00:00"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/recover'.format(resource_group_name='resource_group_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=recovery_entity,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_sites_recover_site_slot(client):
    """Test case for sites_recover_site_slot

    Recovers a deleted web app
    """
    recovery_entity = {"slotName":"slotName","recoverConfig":True,"siteName":"siteName","snapshotTime":"2000-01-23T04:56:07.000+00:00"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/recover'.format(resource_group_name='resource_group_name_example', name='name_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=recovery_entity,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sites_reset_production_slot_config(client):
    """Test case for sites_reset_production_slot_config

    Resets the configuration settings of the current slot if they were previously modified by calling ApplySlotConfig API
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/resetSlotConfig'.format(resource_group_name='resource_group_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sites_reset_slot_config_slot(client):
    """Test case for sites_reset_slot_config_slot

    Resets the configuration settings of the current slot if they were previously modified by calling ApplySlotConfig API
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/resetSlotConfig'.format(resource_group_name='resource_group_name_example', name='name_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sites_restart_site(client):
    """Test case for sites_restart_site

    Restarts web app
    """
    params = [('softRestart', True),
                    ('synchronous', True),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/restart'.format(resource_group_name='resource_group_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sites_restart_site_slot(client):
    """Test case for sites_restart_site_slot

    Restarts web app
    """
    params = [('softRestart', True),
                    ('synchronous', True),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/restart'.format(resource_group_name='resource_group_name_example', name='name_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_sites_restore_site(client):
    """Test case for sites_restore_site

    Restores a web app
    """
    request = {"properties":"{}"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/backups/{backup_id}/restore'.format(resource_group_name='resource_group_name_example', name='name_example', backup_id='backup_id_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=request,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_sites_restore_site_slot(client):
    """Test case for sites_restore_site_slot

    Restores a web app
    """
    request = {"properties":"{}"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/backups/{backup_id}/restore'.format(resource_group_name='resource_group_name_example', name='name_example', backup_id='backup_id_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=request,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sites_start_site(client):
    """Test case for sites_start_site

    Starts web app
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/start'.format(resource_group_name='resource_group_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sites_start_site_slot(client):
    """Test case for sites_start_site_slot

    Starts web app
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/start'.format(resource_group_name='resource_group_name_example', name='name_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sites_stop_site(client):
    """Test case for sites_stop_site

    Stops web app
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/stop'.format(resource_group_name='resource_group_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sites_stop_site_slot(client):
    """Test case for sites_stop_site_slot

    Stops web app
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/stop'.format(resource_group_name='resource_group_name_example', name='name_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_sites_swap_slot_with_production(client):
    """Test case for sites_swap_slot_with_production

    Swaps web app slots
    """
    slot_swap_entity = {"preserveVnet":True,"targetSlot":"targetSlot"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slotsswap'.format(resource_group_name='resource_group_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=slot_swap_entity,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_sites_swap_slots_slot(client):
    """Test case for sites_swap_slots_slot

    Swaps web app slots
    """
    slot_swap_entity = {"preserveVnet":True,"targetSlot":"targetSlot"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/slotsswap'.format(resource_group_name='resource_group_name_example', name='name_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=slot_swap_entity,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sites_sync_site_repository(client):
    """Test case for sites_sync_site_repository

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/sync'.format(resource_group_name='resource_group_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sites_sync_site_repository_slot(client):
    """Test case for sites_sync_site_repository_slot

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/sync'.format(resource_group_name='resource_group_name_example', name='name_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_sites_update_site_app_settings(client):
    """Test case for sites_update_site_app_settings

    Updates the application settings of web app
    """
    app_settings = {"properties":{"key":"properties"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/config/appsettings'.format(resource_group_name='resource_group_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=app_settings,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_sites_update_site_app_settings_slot(client):
    """Test case for sites_update_site_app_settings_slot

    Updates the application settings of web app
    """
    app_settings = {"properties":{"key":"properties"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/config/appsettings'.format(resource_group_name='resource_group_name_example', name='name_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=app_settings,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_sites_update_site_auth_settings(client):
    """Test case for sites_update_site_auth_settings

    Updates the Authentication / Authorization settings associated with web app
    """
    site_auth_settings = {"facebookAppId":"facebookAppId","googleClientSecret":"googleClientSecret","twitterConsumerSecret":"twitterConsumerSecret","unauthenticatedClientAction":"RedirectToLoginPage","twitterConsumerKey":"twitterConsumerKey","enabled":True,"googleClientId":"googleClientId","issuer":"issuer","googleOAuthScopes":["googleOAuthScopes","googleOAuthScopes"],"microsoftAccountClientId":"microsoftAccountClientId","tokenRefreshExtensionHours":0.8008281904610115,"clientSecret":"clientSecret","aadClientId":"aadClientId","facebookAppSecret":"facebookAppSecret","tokenStoreEnabled":True,"clientId":"clientId","facebookOAuthScopes":["facebookOAuthScopes","facebookOAuthScopes"],"openIdIssuer":"openIdIssuer","additionalLoginParams":["additionalLoginParams","additionalLoginParams"],"defaultProvider":"AzureActiveDirectory","httpApiPrefixPath":"httpApiPrefixPath","microsoftAccountOAuthScopes":["microsoftAccountOAuthScopes","microsoftAccountOAuthScopes"],"allowedExternalRedirectUrls":["allowedExternalRedirectUrls","allowedExternalRedirectUrls"],"microsoftAccountClientSecret":"microsoftAccountClientSecret","allowedAudiences":["allowedAudiences","allowedAudiences"]}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/config/authsettings'.format(resource_group_name='resource_group_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=site_auth_settings,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_sites_update_site_auth_settings_slot(client):
    """Test case for sites_update_site_auth_settings_slot

    Updates the Authentication / Authorization settings associated with web app
    """
    site_auth_settings = {"facebookAppId":"facebookAppId","googleClientSecret":"googleClientSecret","twitterConsumerSecret":"twitterConsumerSecret","unauthenticatedClientAction":"RedirectToLoginPage","twitterConsumerKey":"twitterConsumerKey","enabled":True,"googleClientId":"googleClientId","issuer":"issuer","googleOAuthScopes":["googleOAuthScopes","googleOAuthScopes"],"microsoftAccountClientId":"microsoftAccountClientId","tokenRefreshExtensionHours":0.8008281904610115,"clientSecret":"clientSecret","aadClientId":"aadClientId","facebookAppSecret":"facebookAppSecret","tokenStoreEnabled":True,"clientId":"clientId","facebookOAuthScopes":["facebookOAuthScopes","facebookOAuthScopes"],"openIdIssuer":"openIdIssuer","additionalLoginParams":["additionalLoginParams","additionalLoginParams"],"defaultProvider":"AzureActiveDirectory","httpApiPrefixPath":"httpApiPrefixPath","microsoftAccountOAuthScopes":["microsoftAccountOAuthScopes","microsoftAccountOAuthScopes"],"allowedExternalRedirectUrls":["allowedExternalRedirectUrls","allowedExternalRedirectUrls"],"microsoftAccountClientSecret":"microsoftAccountClientSecret","allowedAudiences":["allowedAudiences","allowedAudiences"]}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/config/authsettings'.format(resource_group_name='resource_group_name_example', name='name_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=site_auth_settings,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_sites_update_site_backup_configuration(client):
    """Test case for sites_update_site_backup_configuration

    Updates backup configuration of web app
    """
    request = {"properties":"{}"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/config/backup'.format(resource_group_name='resource_group_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=request,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_sites_update_site_backup_configuration_slot(client):
    """Test case for sites_update_site_backup_configuration_slot

    Updates backup configuration of web app
    """
    request = {"properties":"{}"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/config/backup'.format(resource_group_name='resource_group_name_example', name='name_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=request,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_sites_update_site_config(client):
    """Test case for sites_update_site_config

    Update the configuration of web app
    """
    site_config = {"properties":"{}"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/config/web'.format(resource_group_name='resource_group_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=site_config,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_sites_update_site_config_slot(client):
    """Test case for sites_update_site_config_slot

    Update the configuration of web app
    """
    site_config = {"properties":"{}"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/config/web'.format(resource_group_name='resource_group_name_example', name='name_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=site_config,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_sites_update_site_connection_strings(client):
    """Test case for sites_update_site_connection_strings

    Updates the connection strings associated with web app
    """
    connection_strings = {"properties":{"key":{"type":"MySql","value":"value"}}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/config/connectionstrings'.format(resource_group_name='resource_group_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=connection_strings,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_sites_update_site_connection_strings_slot(client):
    """Test case for sites_update_site_connection_strings_slot

    Updates the connection strings associated with web app
    """
    connection_strings = {"properties":{"key":{"type":"MySql","value":"value"}}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/config/connectionstrings'.format(resource_group_name='resource_group_name_example', name='name_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=connection_strings,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_sites_update_site_logs_config(client):
    """Test case for sites_update_site_logs_config

    Updates the meta data for web app
    """
    site_logs_config = {"properties":"{}"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/config/logs'.format(resource_group_name='resource_group_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=site_logs_config,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_sites_update_site_logs_config_slot(client):
    """Test case for sites_update_site_logs_config_slot

    Updates the meta data for web app
    """
    site_logs_config = {"properties":"{}"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/config/logs'.format(resource_group_name='resource_group_name_example', name='name_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=site_logs_config,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_sites_update_site_metadata(client):
    """Test case for sites_update_site_metadata

    Updates the meta data for web app
    """
    metadata = {"properties":{"key":"properties"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/config/metadata'.format(resource_group_name='resource_group_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=metadata,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_sites_update_site_metadata_slot(client):
    """Test case for sites_update_site_metadata_slot

    Updates the meta data for web app
    """
    metadata = {"properties":{"key":"properties"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/config/metadata'.format(resource_group_name='resource_group_name_example', name='name_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=metadata,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_sites_update_site_relay_service_connection(client):
    """Test case for sites_update_site_relay_service_connection

    Creates a new association to a BizTalk Hybrid Connection, or updates an existing one.
    """
    connection_envelope = {"properties":"{}"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/hybridconnection/{entity_name}'.format(resource_group_name='resource_group_name_example', name='name_example', entity_name='entity_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=connection_envelope,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_sites_update_site_relay_service_connection_slot(client):
    """Test case for sites_update_site_relay_service_connection_slot

    Creates a new association to a BizTalk Hybrid Connection, or updates an existing one.
    """
    connection_envelope = {"properties":"{}"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/hybridconnection/{entity_name}'.format(resource_group_name='resource_group_name_example', name='name_example', entity_name='entity_name_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=connection_envelope,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_sites_update_site_source_control(client):
    """Test case for sites_update_site_source_control

    Update the source control configuration of web app
    """
    site_source_control = {"properties":"{}"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/sourcecontrols/web'.format(resource_group_name='resource_group_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=site_source_control,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_sites_update_site_source_control_slot(client):
    """Test case for sites_update_site_source_control_slot

    Update the source control configuration of web app
    """
    site_source_control = {"properties":"{}"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/sourcecontrols/web'.format(resource_group_name='resource_group_name_example', name='name_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=site_source_control,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_sites_update_site_vnet_connection(client):
    """Test case for sites_update_site_vnet_connection

    Adds a Virtual Network Connection or updates it's properties.
    """
    connection_envelope = {"properties":"{}"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/virtualNetworkConnections/{vnet_name}'.format(resource_group_name='resource_group_name_example', name='name_example', vnet_name='vnet_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=connection_envelope,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_sites_update_site_vnet_connection_gateway(client):
    """Test case for sites_update_site_vnet_connection_gateway

    Updates the Virtual Network Gateway.
    """
    connection_envelope = {"properties":"{}"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/virtualNetworkConnections/{vnet_name}/gateways/{gateway_name}'.format(resource_group_name='resource_group_name_example', name='name_example', vnet_name='vnet_name_example', gateway_name='gateway_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=connection_envelope,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_sites_update_site_vnet_connection_gateway_slot(client):
    """Test case for sites_update_site_vnet_connection_gateway_slot

    Updates the Virtual Network Gateway.
    """
    connection_envelope = {"properties":"{}"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/virtualNetworkConnections/{vnet_name}/gateways/{gateway_name}'.format(resource_group_name='resource_group_name_example', name='name_example', vnet_name='vnet_name_example', gateway_name='gateway_name_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=connection_envelope,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_sites_update_site_vnet_connection_slot(client):
    """Test case for sites_update_site_vnet_connection_slot

    Adds a Virtual Network Connection or updates it's properties.
    """
    connection_envelope = {"properties":"{}"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/slots/{slot}/virtualNetworkConnections/{vnet_name}'.format(resource_group_name='resource_group_name_example', name='name_example', vnet_name='vnet_name_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=connection_envelope,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_sites_update_slot_config_names(client):
    """Test case for sites_update_slot_config_names

    Updates the names of application settings and connection string that remain with the slot during swap operation
    """
    slot_config_names = {"properties":"{}"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{name}/config/slotConfigNames'.format(resource_group_name='resource_group_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=slot_config_names,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

