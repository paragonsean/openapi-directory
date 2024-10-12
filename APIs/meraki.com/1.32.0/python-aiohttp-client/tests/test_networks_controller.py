# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.bind_network_request import BindNetworkRequest
from openapi_server.models.claim_network_devices_request import ClaimNetworkDevicesRequest
from openapi_server.models.combine_organization_networks200_response import CombineOrganizationNetworks200Response
from openapi_server.models.combine_organization_networks_request import CombineOrganizationNetworksRequest
from openapi_server.models.create_network_firmware_upgrades_rollback200_response import CreateNetworkFirmwareUpgradesRollback200Response
from openapi_server.models.create_network_firmware_upgrades_rollback_request import CreateNetworkFirmwareUpgradesRollbackRequest
from openapi_server.models.create_network_firmware_upgrades_staged_event_request import CreateNetworkFirmwareUpgradesStagedEventRequest
from openapi_server.models.create_network_firmware_upgrades_staged_group_request import CreateNetworkFirmwareUpgradesStagedGroupRequest
from openapi_server.models.create_network_floor_plan_request import CreateNetworkFloorPlanRequest
from openapi_server.models.create_network_group_policy_request import CreateNetworkGroupPolicyRequest
from openapi_server.models.create_network_meraki_auth_user_request import CreateNetworkMerakiAuthUserRequest
from openapi_server.models.create_network_mqtt_broker_request import CreateNetworkMqttBrokerRequest
from openapi_server.models.create_network_pii_request_request import CreateNetworkPiiRequestRequest
from openapi_server.models.create_network_webhooks_http_server_request import CreateNetworkWebhooksHttpServerRequest
from openapi_server.models.create_network_webhooks_payload_template_request import CreateNetworkWebhooksPayloadTemplateRequest
from openapi_server.models.create_network_webhooks_webhook_test201_response import CreateNetworkWebhooksWebhookTest201Response
from openapi_server.models.create_network_webhooks_webhook_test_request import CreateNetworkWebhooksWebhookTestRequest
from openapi_server.models.create_organization_network_request import CreateOrganizationNetworkRequest
from openapi_server.models.get_network200_response import GetNetwork200Response
from openapi_server.models.get_network_alerts_history200_response_inner import GetNetworkAlertsHistory200ResponseInner
from openapi_server.models.get_network_client200_response import GetNetworkClient200Response
from openapi_server.models.get_network_clients200_response import GetNetworkClients200Response
from openapi_server.models.get_network_events200_response import GetNetworkEvents200Response
from openapi_server.models.get_network_events_event_types200_response_inner import GetNetworkEventsEventTypes200ResponseInner
from openapi_server.models.get_network_firmware_upgrades200_response import GetNetworkFirmwareUpgrades200Response
from openapi_server.models.get_network_firmware_upgrades_staged_events200_response import GetNetworkFirmwareUpgradesStagedEvents200Response
from openapi_server.models.get_network_firmware_upgrades_staged_groups200_response_inner import GetNetworkFirmwareUpgradesStagedGroups200ResponseInner
from openapi_server.models.get_network_firmware_upgrades_staged_stages200_response_inner import GetNetworkFirmwareUpgradesStagedStages200ResponseInner
from openapi_server.models.get_network_health_alerts200_response_inner import GetNetworkHealthAlerts200ResponseInner
from openapi_server.models.get_network_meraki_auth_users200_response_inner import GetNetworkMerakiAuthUsers200ResponseInner
from openapi_server.models.get_network_policies_by_client200_response_inner import GetNetworkPoliciesByClient200ResponseInner
from openapi_server.models.get_network_settings200_response import GetNetworkSettings200Response
from openapi_server.models.get_network_syslog_servers200_response import GetNetworkSyslogServers200Response
from openapi_server.models.get_network_webhooks_http_servers200_response_inner import GetNetworkWebhooksHttpServers200ResponseInner
from openapi_server.models.get_network_webhooks_payload_templates200_response_inner import GetNetworkWebhooksPayloadTemplates200ResponseInner
from openapi_server.models.provision_network_clients_request import ProvisionNetworkClientsRequest
from openapi_server.models.remove_network_devices_request import RemoveNetworkDevicesRequest
from openapi_server.models.rollbacks_network_firmware_upgrades_staged_events_request import RollbacksNetworkFirmwareUpgradesStagedEventsRequest
from openapi_server.models.split_network200_response import SplitNetwork200Response
from openapi_server.models.unbind_network_request import UnbindNetworkRequest
from openapi_server.models.update_network_alerts_settings_request import UpdateNetworkAlertsSettingsRequest
from openapi_server.models.update_network_client_policy_request import UpdateNetworkClientPolicyRequest
from openapi_server.models.update_network_client_splash_authorization_status_request import UpdateNetworkClientSplashAuthorizationStatusRequest
from openapi_server.models.update_network_firmware_upgrades_request import UpdateNetworkFirmwareUpgradesRequest
from openapi_server.models.update_network_firmware_upgrades_staged_events_request import UpdateNetworkFirmwareUpgradesStagedEventsRequest
from openapi_server.models.update_network_firmware_upgrades_staged_stages_request import UpdateNetworkFirmwareUpgradesStagedStagesRequest
from openapi_server.models.update_network_floor_plan_request import UpdateNetworkFloorPlanRequest
from openapi_server.models.update_network_group_policy_request import UpdateNetworkGroupPolicyRequest
from openapi_server.models.update_network_meraki_auth_user_request import UpdateNetworkMerakiAuthUserRequest
from openapi_server.models.update_network_mqtt_broker_request import UpdateNetworkMqttBrokerRequest
from openapi_server.models.update_network_netflow_request import UpdateNetworkNetflowRequest
from openapi_server.models.update_network_request import UpdateNetworkRequest
from openapi_server.models.update_network_settings_request import UpdateNetworkSettingsRequest
from openapi_server.models.update_network_snmp_request import UpdateNetworkSnmpRequest
from openapi_server.models.update_network_syslog_servers_request import UpdateNetworkSyslogServersRequest
from openapi_server.models.update_network_traffic_analysis_request import UpdateNetworkTrafficAnalysisRequest
from openapi_server.models.update_network_webhooks_http_server_request import UpdateNetworkWebhooksHttpServerRequest
from openapi_server.models.update_network_webhooks_payload_template_request import UpdateNetworkWebhooksPayloadTemplateRequest
from openapi_server.models.vmx_network_devices_claim_request import VmxNetworkDevicesClaimRequest


pytestmark = pytest.mark.asyncio

async def test_bind_network(client):
    """Test case for bind_network

    Bind a network to a template.
    """
    body = openapi_server.BindNetworkRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/networks/{network_id}/bind'.format(network_id='network_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_claim_network_devices(client):
    """Test case for claim_network_devices

    Claim devices into a network. (Note: for recently claimed devices, it may take a few minutes for API requsts against that device to succeed)
    """
    body = openapi_server.ClaimNetworkDevicesRequest()
    headers = { 
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/networks/{network_id}/devices/claim'.format(network_id='network_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_combine_organization_networks_1(client):
    """Test case for combine_organization_networks_1

    Combine multiple networks into a single network
    """
    body = openapi_server.CombineOrganizationNetworksRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/organizations/{organization_id}/networks/combine'.format(organization_id='organization_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_network_firmware_upgrades_rollback(client):
    """Test case for create_network_firmware_upgrades_rollback

    Rollback a Firmware Upgrade For A Network
    """
    body = openapi_server.CreateNetworkFirmwareUpgradesRollbackRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/networks/{network_id}/firmwareUpgrades/rollbacks'.format(network_id='network_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_network_firmware_upgrades_staged_event(client):
    """Test case for create_network_firmware_upgrades_staged_event

    Create a Staged Upgrade Event for a network
    """
    body = openapi_server.CreateNetworkFirmwareUpgradesStagedEventRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/networks/{network_id}/firmwareUpgrades/staged/events'.format(network_id='network_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_network_firmware_upgrades_staged_group(client):
    """Test case for create_network_firmware_upgrades_staged_group

    Create a Staged Upgrade Group for a network
    """
    body = openapi_server.CreateNetworkFirmwareUpgradesStagedGroupRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/networks/{network_id}/firmwareUpgrades/staged/groups'.format(network_id='network_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_network_floor_plan(client):
    """Test case for create_network_floor_plan

    Upload a floor plan
    """
    body = openapi_server.CreateNetworkFloorPlanRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/networks/{network_id}/floorPlans'.format(network_id='network_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_network_group_policy(client):
    """Test case for create_network_group_policy

    Create a group policy
    """
    body = openapi_server.CreateNetworkGroupPolicyRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/networks/{network_id}/groupPolicies'.format(network_id='network_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_network_meraki_auth_user(client):
    """Test case for create_network_meraki_auth_user

    Authorize a user configured with Meraki Authentication for a network (currently supports 802.1X, splash guest, and client VPN users, and currently, organizations have a 50,000 user cap)
    """
    body = openapi_server.CreateNetworkMerakiAuthUserRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/networks/{network_id}/merakiAuthUsers'.format(network_id='network_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_network_mqtt_broker(client):
    """Test case for create_network_mqtt_broker

    Add an MQTT broker
    """
    body = openapi_server.CreateNetworkMqttBrokerRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/networks/{network_id}/mqttBrokers'.format(network_id='network_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_network_pii_request(client):
    """Test case for create_network_pii_request

    Submit a new delete or restrict processing PII request
    """
    body = openapi_server.CreateNetworkPiiRequestRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/networks/{network_id}/pii/requests'.format(network_id='network_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_network_webhooks_http_server(client):
    """Test case for create_network_webhooks_http_server

    Add an HTTP server to a network
    """
    body = openapi_server.CreateNetworkWebhooksHttpServerRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/networks/{network_id}/webhooks/httpServers'.format(network_id='network_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_network_webhooks_payload_template(client):
    """Test case for create_network_webhooks_payload_template

    Create a webhook payload template for a network
    """
    body = openapi_server.CreateNetworkWebhooksPayloadTemplateRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/networks/{network_id}/webhooks/payloadTemplates'.format(network_id='network_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_network_webhooks_webhook_test(client):
    """Test case for create_network_webhooks_webhook_test

    Send a test webhook for a network
    """
    body = openapi_server.CreateNetworkWebhooksWebhookTestRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/networks/{network_id}/webhooks/webhookTests'.format(network_id='network_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_organization_network_1(client):
    """Test case for create_organization_network_1

    Create a network
    """
    body = openapi_server.CreateOrganizationNetworkRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/organizations/{organization_id}/networks'.format(organization_id='organization_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_defer_network_firmware_upgrades_staged_events(client):
    """Test case for defer_network_firmware_upgrades_staged_events

    Postpone by 1 week all pending staged upgrade stages for a network
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/networks/{network_id}/firmwareUpgrades/staged/events/defer'.format(network_id='network_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_network(client):
    """Test case for delete_network

    Delete a network
    """
    headers = { 
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/networks/{network_id}'.format(network_id='network_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_network_firmware_upgrades_staged_group(client):
    """Test case for delete_network_firmware_upgrades_staged_group

    Delete a Staged Upgrade Group
    """
    headers = { 
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/networks/{network_id}/firmwareUpgrades/staged/groups/{group_id}'.format(network_id='network_id_example', group_id='group_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_network_floor_plan(client):
    """Test case for delete_network_floor_plan

    Destroy a floor plan
    """
    headers = { 
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/networks/{network_id}/floorPlans/{floor_plan_id}'.format(network_id='network_id_example', floor_plan_id='floor_plan_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_network_group_policy(client):
    """Test case for delete_network_group_policy

    Delete a group policy
    """
    headers = { 
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/networks/{network_id}/groupPolicies/{group_policy_id}'.format(network_id='network_id_example', group_policy_id='group_policy_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_network_meraki_auth_user(client):
    """Test case for delete_network_meraki_auth_user

    Deauthorize a user
    """
    headers = { 
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/networks/{network_id}/merakiAuthUsers/{meraki_auth_user_id}'.format(network_id='network_id_example', meraki_auth_user_id='meraki_auth_user_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_network_mqtt_broker(client):
    """Test case for delete_network_mqtt_broker

    Delete an MQTT broker
    """
    headers = { 
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/networks/{network_id}/mqttBrokers/{mqtt_broker_id}'.format(network_id='network_id_example', mqtt_broker_id='mqtt_broker_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_network_pii_request(client):
    """Test case for delete_network_pii_request

    Delete a restrict processing PII request
    """
    headers = { 
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/networks/{network_id}/pii/requests/{request_id}'.format(network_id='network_id_example', request_id='request_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_network_webhooks_http_server(client):
    """Test case for delete_network_webhooks_http_server

    Delete an HTTP server from a network
    """
    headers = { 
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/networks/{network_id}/webhooks/httpServers/{http_server_id}'.format(network_id='network_id_example', http_server_id='http_server_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_network_webhooks_payload_template(client):
    """Test case for delete_network_webhooks_payload_template

    Destroy a webhook payload template for a network
    """
    headers = { 
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/networks/{network_id}/webhooks/payloadTemplates/{payload_template_id}'.format(network_id='network_id_example', payload_template_id='payload_template_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network(client):
    """Test case for get_network

    Return a network
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}'.format(network_id='network_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_alerts_history(client):
    """Test case for get_network_alerts_history

    Return the alert history for this network
    """
    params = [('perPage', 56),
                    ('startingAfter', 'starting_after_example'),
                    ('endingBefore', 'ending_before_example')]
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/alerts/history'.format(network_id='network_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_alerts_settings(client):
    """Test case for get_network_alerts_settings

    Return the alert configuration for this network
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/alerts/settings'.format(network_id='network_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_bluetooth_client(client):
    """Test case for get_network_bluetooth_client

    Return a Bluetooth client
    """
    params = [('includeConnectivityHistory', True),
                    ('connectivityHistoryTimespan', 56)]
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/bluetoothClients/{bluetooth_client_id}'.format(network_id='network_id_example', bluetooth_client_id='bluetooth_client_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_bluetooth_clients(client):
    """Test case for get_network_bluetooth_clients

    List the Bluetooth clients seen by APs in this network
    """
    params = [('t0', 't0_example'),
                    ('timespan', 3.4),
                    ('perPage', 56),
                    ('startingAfter', 'starting_after_example'),
                    ('endingBefore', 'ending_before_example'),
                    ('includeConnectivityHistory', True)]
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/bluetoothClients'.format(network_id='network_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_client(client):
    """Test case for get_network_client

    Return the client associated with the given identifier
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/clients/{client_id}'.format(network_id='network_id_example', client_id='client_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_client_policy(client):
    """Test case for get_network_client_policy

    Return the policy assigned to a client on the network
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/clients/{client_id}/policy'.format(network_id='network_id_example', client_id='client_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_client_splash_authorization_status(client):
    """Test case for get_network_client_splash_authorization_status

    Return the splash authorization for a client, for each SSID they've associated with through splash
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/clients/{client_id}/splashAuthorizationStatus'.format(network_id='network_id_example', client_id='client_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_client_traffic_history(client):
    """Test case for get_network_client_traffic_history

    Return the client's network traffic data over time
    """
    params = [('perPage', 56),
                    ('startingAfter', 'starting_after_example'),
                    ('endingBefore', 'ending_before_example')]
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/clients/{client_id}/trafficHistory'.format(network_id='network_id_example', client_id='client_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_client_usage_history(client):
    """Test case for get_network_client_usage_history

    Return the client's daily usage history
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/clients/{client_id}/usageHistory'.format(network_id='network_id_example', client_id='client_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_clients(client):
    """Test case for get_network_clients

    List the clients that have used this network in the timespan
    """
    params = [('t0', 't0_example'),
                    ('timespan', 3.4),
                    ('perPage', 56),
                    ('startingAfter', 'starting_after_example'),
                    ('endingBefore', 'ending_before_example'),
                    ('statuses', ['statuses_example']),
                    ('ip', 'ip_example'),
                    ('ip6', 'ip6_example'),
                    ('ip6Local', 'ip6_local_example'),
                    ('mac', 'mac_example'),
                    ('os', 'os_example'),
                    ('description', 'description_example'),
                    ('vlan', 'vlan_example'),
                    ('recentDeviceConnections', ['recent_device_connections_example'])]
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/clients'.format(network_id='network_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_clients_application_usage(client):
    """Test case for get_network_clients_application_usage

    Return the application usage data for clients
    """
    params = [('clients', 'clients_example'),
                    ('ssidNumber', 56),
                    ('perPage', 56),
                    ('startingAfter', 'starting_after_example'),
                    ('endingBefore', 'ending_before_example'),
                    ('t0', 't0_example'),
                    ('t1', 't1_example'),
                    ('timespan', 3.4)]
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/clients/applicationUsage'.format(network_id='network_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_clients_bandwidth_usage_history(client):
    """Test case for get_network_clients_bandwidth_usage_history

    Returns a timeseries of total traffic consumption rates for all clients on a network within a given timespan, in megabits per second.
    """
    params = [('t0', 't0_example'),
                    ('t1', 't1_example'),
                    ('timespan', 3.4),
                    ('perPage', 56),
                    ('startingAfter', 'starting_after_example'),
                    ('endingBefore', 'ending_before_example')]
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/clients/bandwidthUsageHistory'.format(network_id='network_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_clients_overview(client):
    """Test case for get_network_clients_overview

    Return overview statistics for network clients
    """
    params = [('t0', 't0_example'),
                    ('t1', 't1_example'),
                    ('timespan', 3.4),
                    ('resolution', 56)]
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/clients/overview'.format(network_id='network_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_clients_usage_histories(client):
    """Test case for get_network_clients_usage_histories

    Return the usage histories for clients
    """
    params = [('clients', 'clients_example'),
                    ('ssidNumber', 56),
                    ('perPage', 56),
                    ('startingAfter', 'starting_after_example'),
                    ('endingBefore', 'ending_before_example'),
                    ('t0', 't0_example'),
                    ('t1', 't1_example'),
                    ('timespan', 3.4)]
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/clients/usageHistories'.format(network_id='network_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_devices(client):
    """Test case for get_network_devices

    List the devices in a network
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/devices'.format(network_id='network_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_events(client):
    """Test case for get_network_events

    List the events for the network
    """
    params = [('productType', 'product_type_example'),
                    ('includedEventTypes', ['included_event_types_example']),
                    ('excludedEventTypes', ['excluded_event_types_example']),
                    ('deviceMac', 'device_mac_example'),
                    ('deviceSerial', 'device_serial_example'),
                    ('deviceName', 'device_name_example'),
                    ('clientIp', 'client_ip_example'),
                    ('clientMac', 'client_mac_example'),
                    ('clientName', 'client_name_example'),
                    ('smDeviceMac', 'sm_device_mac_example'),
                    ('smDeviceName', 'sm_device_name_example'),
                    ('perPage', 56),
                    ('startingAfter', 'starting_after_example'),
                    ('endingBefore', 'ending_before_example')]
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/events'.format(network_id='network_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_events_event_types(client):
    """Test case for get_network_events_event_types

    List the event type to human-readable description
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/events/eventTypes'.format(network_id='network_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_firmware_upgrades(client):
    """Test case for get_network_firmware_upgrades

    Get firmware upgrade information for a network
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/firmwareUpgrades'.format(network_id='network_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_firmware_upgrades_staged_events(client):
    """Test case for get_network_firmware_upgrades_staged_events

    Get the Staged Upgrade Event from a network
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/firmwareUpgrades/staged/events'.format(network_id='network_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_firmware_upgrades_staged_group(client):
    """Test case for get_network_firmware_upgrades_staged_group

    Get a Staged Upgrade Group from a network
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/firmwareUpgrades/staged/groups/{group_id}'.format(network_id='network_id_example', group_id='group_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_firmware_upgrades_staged_groups(client):
    """Test case for get_network_firmware_upgrades_staged_groups

    List of Staged Upgrade Groups in a network
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/firmwareUpgrades/staged/groups'.format(network_id='network_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_firmware_upgrades_staged_stages(client):
    """Test case for get_network_firmware_upgrades_staged_stages

    Order of Staged Upgrade Groups in a network
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/firmwareUpgrades/staged/stages'.format(network_id='network_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_floor_plan(client):
    """Test case for get_network_floor_plan

    Find a floor plan by ID
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/floorPlans/{floor_plan_id}'.format(network_id='network_id_example', floor_plan_id='floor_plan_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_floor_plans(client):
    """Test case for get_network_floor_plans

    List the floor plans that belong to your network
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/floorPlans'.format(network_id='network_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_group_policies(client):
    """Test case for get_network_group_policies

    List the group policies in a network
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/groupPolicies'.format(network_id='network_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_group_policy(client):
    """Test case for get_network_group_policy

    Display a group policy
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/groupPolicies/{group_policy_id}'.format(network_id='network_id_example', group_policy_id='group_policy_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_health_alerts(client):
    """Test case for get_network_health_alerts

    Return all global alerts on this network
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/health/alerts'.format(network_id='network_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_meraki_auth_user(client):
    """Test case for get_network_meraki_auth_user

    Return the Meraki Auth splash guest, RADIUS, or client VPN user
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/merakiAuthUsers/{meraki_auth_user_id}'.format(network_id='network_id_example', meraki_auth_user_id='meraki_auth_user_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_meraki_auth_users(client):
    """Test case for get_network_meraki_auth_users

    List the users configured under Meraki Authentication for a network (splash guest or RADIUS users for a wireless network, or client VPN users for a wired network)
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/merakiAuthUsers'.format(network_id='network_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_mqtt_broker(client):
    """Test case for get_network_mqtt_broker

    Return an MQTT broker
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/mqttBrokers/{mqtt_broker_id}'.format(network_id='network_id_example', mqtt_broker_id='mqtt_broker_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_mqtt_brokers(client):
    """Test case for get_network_mqtt_brokers

    List the MQTT brokers for this network
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/mqttBrokers'.format(network_id='network_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_netflow(client):
    """Test case for get_network_netflow

    Return the NetFlow traffic reporting settings for a network
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/netflow'.format(network_id='network_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_network_health_channel_utilization(client):
    """Test case for get_network_network_health_channel_utilization

    Get the channel utilization over each radio for all APs in a network.
    """
    params = [('t0', 't0_example'),
                    ('t1', 't1_example'),
                    ('timespan', 3.4),
                    ('resolution', 56),
                    ('perPage', 56),
                    ('startingAfter', 'starting_after_example'),
                    ('endingBefore', 'ending_before_example')]
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/networkHealth/channelUtilization'.format(network_id='network_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_pii_pii_keys(client):
    """Test case for get_network_pii_pii_keys

    List the keys required to access Personally Identifiable Information (PII) for a given identifier
    """
    params = [('username', 'username_example'),
                    ('email', 'email_example'),
                    ('mac', 'mac_example'),
                    ('serial', 'serial_example'),
                    ('imei', 'imei_example'),
                    ('bluetoothMac', 'bluetooth_mac_example')]
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/pii/piiKeys'.format(network_id='network_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_pii_request(client):
    """Test case for get_network_pii_request

    Return a PII request
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/pii/requests/{request_id}'.format(network_id='network_id_example', request_id='request_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_pii_requests(client):
    """Test case for get_network_pii_requests

    List the PII requests for this network or organization
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/pii/requests'.format(network_id='network_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_pii_sm_devices_for_key(client):
    """Test case for get_network_pii_sm_devices_for_key

    Given a piece of Personally Identifiable Information (PII), return the Systems Manager device ID(s) associated with that identifier
    """
    params = [('username', 'username_example'),
                    ('email', 'email_example'),
                    ('mac', 'mac_example'),
                    ('serial', 'serial_example'),
                    ('imei', 'imei_example'),
                    ('bluetoothMac', 'bluetooth_mac_example')]
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/pii/smDevicesForKey'.format(network_id='network_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_pii_sm_owners_for_key(client):
    """Test case for get_network_pii_sm_owners_for_key

    Given a piece of Personally Identifiable Information (PII), return the Systems Manager owner ID(s) associated with that identifier
    """
    params = [('username', 'username_example'),
                    ('email', 'email_example'),
                    ('mac', 'mac_example'),
                    ('serial', 'serial_example'),
                    ('imei', 'imei_example'),
                    ('bluetoothMac', 'bluetooth_mac_example')]
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/pii/smOwnersForKey'.format(network_id='network_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_policies_by_client(client):
    """Test case for get_network_policies_by_client

    Get policies for all clients with policies
    """
    params = [('perPage', 56),
                    ('startingAfter', 'starting_after_example'),
                    ('endingBefore', 'ending_before_example'),
                    ('t0', 't0_example'),
                    ('timespan', 3.4)]
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/policies/byClient'.format(network_id='network_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_settings(client):
    """Test case for get_network_settings

    Return the settings for a network
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/settings'.format(network_id='network_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_snmp(client):
    """Test case for get_network_snmp

    Return the SNMP settings for a network
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/snmp'.format(network_id='network_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_splash_login_attempts(client):
    """Test case for get_network_splash_login_attempts

    List the splash login attempts for a network
    """
    params = [('ssidNumber', 56),
                    ('loginIdentifier', 'login_identifier_example'),
                    ('timespan', 56)]
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/splashLoginAttempts'.format(network_id='network_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_syslog_servers(client):
    """Test case for get_network_syslog_servers

    List the syslog servers for a network
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/syslogServers'.format(network_id='network_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_topology_link_layer(client):
    """Test case for get_network_topology_link_layer

    List the LLDP and CDP information for all discovered devices and connections in a network.
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/topology/linkLayer'.format(network_id='network_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_traffic(client):
    """Test case for get_network_traffic

    Return the traffic analysis data for this network
    """
    params = [('t0', 't0_example'),
                    ('timespan', 3.4),
                    ('deviceType', 'device_type_example')]
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/traffic'.format(network_id='network_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_traffic_analysis(client):
    """Test case for get_network_traffic_analysis

    Return the traffic analysis settings for a network
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/trafficAnalysis'.format(network_id='network_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_traffic_shaping_application_categories(client):
    """Test case for get_network_traffic_shaping_application_categories

    Returns the application categories for traffic shaping rules.
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/trafficShaping/applicationCategories'.format(network_id='network_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_traffic_shaping_dscp_tagging_options(client):
    """Test case for get_network_traffic_shaping_dscp_tagging_options

    Returns the available DSCP tagging options for your traffic shaping rules.
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/trafficShaping/dscpTaggingOptions'.format(network_id='network_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_webhooks_http_server(client):
    """Test case for get_network_webhooks_http_server

    Return an HTTP server for a network
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/webhooks/httpServers/{http_server_id}'.format(network_id='network_id_example', http_server_id='http_server_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_webhooks_http_servers(client):
    """Test case for get_network_webhooks_http_servers

    List the HTTP servers for a network
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/webhooks/httpServers'.format(network_id='network_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_webhooks_payload_template(client):
    """Test case for get_network_webhooks_payload_template

    Get the webhook payload template for a network
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/webhooks/payloadTemplates/{payload_template_id}'.format(network_id='network_id_example', payload_template_id='payload_template_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_webhooks_payload_templates(client):
    """Test case for get_network_webhooks_payload_templates

    List the webhook payload templates for a network
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/webhooks/payloadTemplates'.format(network_id='network_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_webhooks_webhook_test(client):
    """Test case for get_network_webhooks_webhook_test

    Return the status of a webhook test for a network
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/webhooks/webhookTests/{webhook_test_id}'.format(network_id='network_id_example', webhook_test_id='webhook_test_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organization_inventory_onboarding_cloud_monitoring_networks_4(client):
    """Test case for get_organization_inventory_onboarding_cloud_monitoring_networks_4

    Returns list of networks eligible for adding cloud monitored device
    """
    params = [('deviceType', 'device_type_example'),
                    ('perPage', 56),
                    ('startingAfter', 'starting_after_example'),
                    ('endingBefore', 'ending_before_example')]
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/organizations/{organization_id}/inventory/onboarding/cloudMonitoring/networks'.format(organization_id='organization_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organization_networks_1(client):
    """Test case for get_organization_networks_1

    List the networks that the user has privileges on in an organization
    """
    params = [('configTemplateId', 'config_template_id_example'),
                    ('isBoundToConfigTemplate', True),
                    ('tags', ['tags_example']),
                    ('tagsFilterType', 'tags_filter_type_example'),
                    ('perPage', 56),
                    ('startingAfter', 'starting_after_example'),
                    ('endingBefore', 'ending_before_example')]
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/organizations/{organization_id}/networks'.format(organization_id='organization_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_provision_network_clients(client):
    """Test case for provision_network_clients

    Provisions a client with a name and policy
    """
    body = openapi_server.ProvisionNetworkClientsRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/networks/{network_id}/clients/provision'.format(network_id='network_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_remove_network_devices(client):
    """Test case for remove_network_devices

    Remove a single device
    """
    body = openapi_server.RemoveNetworkDevicesRequest()
    headers = { 
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/networks/{network_id}/devices/remove'.format(network_id='network_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_rollbacks_network_firmware_upgrades_staged_events(client):
    """Test case for rollbacks_network_firmware_upgrades_staged_events

    Rollback a Staged Upgrade Event for a network
    """
    body = openapi_server.RollbacksNetworkFirmwareUpgradesStagedEventsRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/networks/{network_id}/firmwareUpgrades/staged/events/rollbacks'.format(network_id='network_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_split_network(client):
    """Test case for split_network

    Split a combined network into individual networks for each type of device
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/networks/{network_id}/split'.format(network_id='network_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_unbind_network(client):
    """Test case for unbind_network

    Unbind a network from a template.
    """
    body = openapi_server.UnbindNetworkRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/networks/{network_id}/unbind'.format(network_id='network_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_network(client):
    """Test case for update_network

    Update a network
    """
    body = openapi_server.UpdateNetworkRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/networks/{network_id}'.format(network_id='network_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_network_alerts_settings(client):
    """Test case for update_network_alerts_settings

    Update the alert configuration for this network
    """
    body = openapi_server.UpdateNetworkAlertsSettingsRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/networks/{network_id}/alerts/settings'.format(network_id='network_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_network_client_policy(client):
    """Test case for update_network_client_policy

    Update the policy assigned to a client on the network
    """
    body = openapi_server.UpdateNetworkClientPolicyRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/networks/{network_id}/clients/{client_id}/policy'.format(network_id='network_id_example', client_id='client_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_network_client_splash_authorization_status(client):
    """Test case for update_network_client_splash_authorization_status

    Update a client's splash authorization
    """
    body = openapi_server.UpdateNetworkClientSplashAuthorizationStatusRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/networks/{network_id}/clients/{client_id}/splashAuthorizationStatus'.format(network_id='network_id_example', client_id='client_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_network_firmware_upgrades(client):
    """Test case for update_network_firmware_upgrades

    Update firmware upgrade information for a network
    """
    body = openapi_server.UpdateNetworkFirmwareUpgradesRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/networks/{network_id}/firmwareUpgrades'.format(network_id='network_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_network_firmware_upgrades_staged_events(client):
    """Test case for update_network_firmware_upgrades_staged_events

    Update the Staged Upgrade Event for a network
    """
    body = openapi_server.UpdateNetworkFirmwareUpgradesStagedEventsRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/networks/{network_id}/firmwareUpgrades/staged/events'.format(network_id='network_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_network_firmware_upgrades_staged_group(client):
    """Test case for update_network_firmware_upgrades_staged_group

    Update a Staged Upgrade Group for a network
    """
    body = openapi_server.CreateNetworkFirmwareUpgradesStagedGroupRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/networks/{network_id}/firmwareUpgrades/staged/groups/{group_id}'.format(network_id='network_id_example', group_id='group_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_network_firmware_upgrades_staged_stages(client):
    """Test case for update_network_firmware_upgrades_staged_stages

    Assign Staged Upgrade Group order in the sequence.
    """
    body = openapi_server.UpdateNetworkFirmwareUpgradesStagedStagesRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/networks/{network_id}/firmwareUpgrades/staged/stages'.format(network_id='network_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_network_floor_plan(client):
    """Test case for update_network_floor_plan

    Update a floor plan's geolocation and other meta data
    """
    body = openapi_server.UpdateNetworkFloorPlanRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/networks/{network_id}/floorPlans/{floor_plan_id}'.format(network_id='network_id_example', floor_plan_id='floor_plan_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_network_group_policy(client):
    """Test case for update_network_group_policy

    Update a group policy
    """
    body = openapi_server.UpdateNetworkGroupPolicyRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/networks/{network_id}/groupPolicies/{group_policy_id}'.format(network_id='network_id_example', group_policy_id='group_policy_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_network_meraki_auth_user(client):
    """Test case for update_network_meraki_auth_user

    Update a user configured with Meraki Authentication (currently, 802.1X RADIUS, splash guest, and client VPN users can be updated)
    """
    body = openapi_server.UpdateNetworkMerakiAuthUserRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/networks/{network_id}/merakiAuthUsers/{meraki_auth_user_id}'.format(network_id='network_id_example', meraki_auth_user_id='meraki_auth_user_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_network_mqtt_broker(client):
    """Test case for update_network_mqtt_broker

    Update an MQTT broker
    """
    body = openapi_server.UpdateNetworkMqttBrokerRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/networks/{network_id}/mqttBrokers/{mqtt_broker_id}'.format(network_id='network_id_example', mqtt_broker_id='mqtt_broker_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_network_netflow(client):
    """Test case for update_network_netflow

    Update the NetFlow traffic reporting settings for a network
    """
    body = openapi_server.UpdateNetworkNetflowRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/networks/{network_id}/netflow'.format(network_id='network_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_network_settings(client):
    """Test case for update_network_settings

    Update the settings for a network
    """
    body = openapi_server.UpdateNetworkSettingsRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/networks/{network_id}/settings'.format(network_id='network_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_network_snmp(client):
    """Test case for update_network_snmp

    Update the SNMP settings for a network
    """
    body = openapi_server.UpdateNetworkSnmpRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/networks/{network_id}/snmp'.format(network_id='network_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_network_syslog_servers(client):
    """Test case for update_network_syslog_servers

    Update the syslog servers for a network
    """
    body = openapi_server.UpdateNetworkSyslogServersRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/networks/{network_id}/syslogServers'.format(network_id='network_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_network_traffic_analysis(client):
    """Test case for update_network_traffic_analysis

    Update the traffic analysis settings for a network
    """
    body = openapi_server.UpdateNetworkTrafficAnalysisRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/networks/{network_id}/trafficAnalysis'.format(network_id='network_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_network_webhooks_http_server(client):
    """Test case for update_network_webhooks_http_server

    Update an HTTP server
    """
    body = openapi_server.UpdateNetworkWebhooksHttpServerRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/networks/{network_id}/webhooks/httpServers/{http_server_id}'.format(network_id='network_id_example', http_server_id='http_server_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_network_webhooks_payload_template(client):
    """Test case for update_network_webhooks_payload_template

    Update a webhook payload template for a network
    """
    body = openapi_server.UpdateNetworkWebhooksPayloadTemplateRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/networks/{network_id}/webhooks/payloadTemplates/{payload_template_id}'.format(network_id='network_id_example', payload_template_id='payload_template_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_vmx_network_devices_claim(client):
    """Test case for vmx_network_devices_claim

    Claim a vMX into a network
    """
    body = openapi_server.VmxNetworkDevicesClaimRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/networks/{network_id}/devices/claim/vmx'.format(network_id='network_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

