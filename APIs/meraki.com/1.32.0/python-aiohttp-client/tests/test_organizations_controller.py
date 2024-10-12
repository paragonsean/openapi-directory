# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.assign_organization_licenses_seats200_response import AssignOrganizationLicensesSeats200Response
from openapi_server.models.assign_organization_licenses_seats_request import AssignOrganizationLicensesSeatsRequest
from openapi_server.models.claim_into_organization_inventory_request import ClaimIntoOrganizationInventoryRequest
from openapi_server.models.claim_into_organization_request import ClaimIntoOrganizationRequest
from openapi_server.models.clone_organization_request import CloneOrganizationRequest
from openapi_server.models.combine_organization_networks200_response import CombineOrganizationNetworks200Response
from openapi_server.models.combine_organization_networks_request import CombineOrganizationNetworksRequest
from openapi_server.models.create_organization_action_batch201_response import CreateOrganizationActionBatch201Response
from openapi_server.models.create_organization_action_batch_request import CreateOrganizationActionBatchRequest
from openapi_server.models.create_organization_adaptive_policy_acl_request import CreateOrganizationAdaptivePolicyAclRequest
from openapi_server.models.create_organization_adaptive_policy_group_request import CreateOrganizationAdaptivePolicyGroupRequest
from openapi_server.models.create_organization_adaptive_policy_policy_request import CreateOrganizationAdaptivePolicyPolicyRequest
from openapi_server.models.create_organization_admin_request import CreateOrganizationAdminRequest
from openapi_server.models.create_organization_alerts_profile_request import CreateOrganizationAlertsProfileRequest
from openapi_server.models.create_organization_branding_policy201_response import CreateOrganizationBrandingPolicy201Response
from openapi_server.models.create_organization_branding_policy_request import CreateOrganizationBrandingPolicyRequest
from openapi_server.models.create_organization_config_template_request import CreateOrganizationConfigTemplateRequest
from openapi_server.models.create_organization_early_access_features_opt_in_request import CreateOrganizationEarlyAccessFeaturesOptInRequest
from openapi_server.models.create_organization_inventory_onboarding_cloud_monitoring_export_event_request import CreateOrganizationInventoryOnboardingCloudMonitoringExportEventRequest
from openapi_server.models.create_organization_inventory_onboarding_cloud_monitoring_import201_response_inner import CreateOrganizationInventoryOnboardingCloudMonitoringImport201ResponseInner
from openapi_server.models.create_organization_inventory_onboarding_cloud_monitoring_import_request import CreateOrganizationInventoryOnboardingCloudMonitoringImportRequest
from openapi_server.models.create_organization_inventory_onboarding_cloud_monitoring_prepare201_response_inner import CreateOrganizationInventoryOnboardingCloudMonitoringPrepare201ResponseInner
from openapi_server.models.create_organization_inventory_onboarding_cloud_monitoring_prepare_request import CreateOrganizationInventoryOnboardingCloudMonitoringPrepareRequest
from openapi_server.models.create_organization_network_request import CreateOrganizationNetworkRequest
from openapi_server.models.create_organization_policy_object_request import CreateOrganizationPolicyObjectRequest
from openapi_server.models.create_organization_policy_objects_group_request import CreateOrganizationPolicyObjectsGroupRequest
from openapi_server.models.create_organization_request import CreateOrganizationRequest
from openapi_server.models.create_organization_saml_idp_request import CreateOrganizationSamlIdpRequest
from openapi_server.models.create_organization_saml_role_request import CreateOrganizationSamlRoleRequest
from openapi_server.models.get_network200_response import GetNetwork200Response
from openapi_server.models.get_organization_adaptive_policy_overview200_response import GetOrganizationAdaptivePolicyOverview200Response
from openapi_server.models.get_organization_api_requests200_response_inner import GetOrganizationApiRequests200ResponseInner
from openapi_server.models.get_organization_api_requests_overview_response_codes_by_interval200_response_inner import GetOrganizationApiRequestsOverviewResponseCodesByInterval200ResponseInner
from openapi_server.models.get_organization_branding_policies200_response_inner import GetOrganizationBrandingPolicies200ResponseInner
from openapi_server.models.get_organization_branding_policies_priorities200_response import GetOrganizationBrandingPoliciesPriorities200Response
from openapi_server.models.get_organization_clients_bandwidth_usage_history200_response_inner import GetOrganizationClientsBandwidthUsageHistory200ResponseInner
from openapi_server.models.get_organization_clients_overview200_response import GetOrganizationClientsOverview200Response
from openapi_server.models.get_organization_devices200_response_inner import GetOrganizationDevices200ResponseInner
from openapi_server.models.get_organization_devices_availabilities200_response_inner import GetOrganizationDevicesAvailabilities200ResponseInner
from openapi_server.models.get_organization_devices_power_modules_statuses_by_device200_response_inner import GetOrganizationDevicesPowerModulesStatusesByDevice200ResponseInner
from openapi_server.models.get_organization_devices_statuses200_response import GetOrganizationDevicesStatuses200Response
from openapi_server.models.get_organization_devices_statuses_overview200_response import GetOrganizationDevicesStatusesOverview200Response
from openapi_server.models.get_organization_devices_uplinks_addresses_by_device200_response_inner import GetOrganizationDevicesUplinksAddressesByDevice200ResponseInner
from openapi_server.models.get_organization_devices_uplinks_loss_and_latency200_response_inner import GetOrganizationDevicesUplinksLossAndLatency200ResponseInner
from openapi_server.models.get_organization_firmware_upgrades200_response_inner import GetOrganizationFirmwareUpgrades200ResponseInner
from openapi_server.models.get_organization_firmware_upgrades_by_device200_response_inner import GetOrganizationFirmwareUpgradesByDevice200ResponseInner
from openapi_server.models.get_organization_inventory_devices200_response_inner import GetOrganizationInventoryDevices200ResponseInner
from openapi_server.models.get_organization_inventory_onboarding_cloud_monitoring_imports200_response_inner import GetOrganizationInventoryOnboardingCloudMonitoringImports200ResponseInner
from openapi_server.models.get_organization_licenses200_response_inner import GetOrganizationLicenses200ResponseInner
from openapi_server.models.get_organization_login_security200_response import GetOrganizationLoginSecurity200Response
from openapi_server.models.get_organization_saml200_response import GetOrganizationSaml200Response
from openapi_server.models.get_organization_saml_idps200_response_inner import GetOrganizationSamlIdps200ResponseInner
from openapi_server.models.get_organization_summary_top_appliances_by_utilization200_response_inner import GetOrganizationSummaryTopAppliancesByUtilization200ResponseInner
from openapi_server.models.get_organization_summary_top_clients_by_usage200_response_inner import GetOrganizationSummaryTopClientsByUsage200ResponseInner
from openapi_server.models.get_organization_summary_top_clients_manufacturers_by_usage200_response_inner import GetOrganizationSummaryTopClientsManufacturersByUsage200ResponseInner
from openapi_server.models.get_organization_summary_top_devices_by_usage200_response_inner import GetOrganizationSummaryTopDevicesByUsage200ResponseInner
from openapi_server.models.get_organization_summary_top_devices_models_by_usage200_response_inner import GetOrganizationSummaryTopDevicesModelsByUsage200ResponseInner
from openapi_server.models.get_organization_summary_top_ssids_by_usage200_response_inner import GetOrganizationSummaryTopSsidsByUsage200ResponseInner
from openapi_server.models.get_organization_summary_top_switches_by_energy_usage200_response_inner import GetOrganizationSummaryTopSwitchesByEnergyUsage200ResponseInner
from openapi_server.models.get_organization_uplinks_statuses200_response_inner import GetOrganizationUplinksStatuses200ResponseInner
from openapi_server.models.get_organization_webhooks_logs200_response_inner import GetOrganizationWebhooksLogs200ResponseInner
from openapi_server.models.get_organizations200_response_inner import GetOrganizations200ResponseInner
from openapi_server.models.move_organization_licenses200_response import MoveOrganizationLicenses200Response
from openapi_server.models.move_organization_licenses_request import MoveOrganizationLicensesRequest
from openapi_server.models.move_organization_licenses_seats200_response import MoveOrganizationLicensesSeats200Response
from openapi_server.models.move_organization_licenses_seats_request import MoveOrganizationLicensesSeatsRequest
from openapi_server.models.release_from_organization_inventory_request import ReleaseFromOrganizationInventoryRequest
from openapi_server.models.renew_organization_licenses_seats_request import RenewOrganizationLicensesSeatsRequest
from openapi_server.models.update_organization_action_batch_request import UpdateOrganizationActionBatchRequest
from openapi_server.models.update_organization_adaptive_policy_acl_request import UpdateOrganizationAdaptivePolicyAclRequest
from openapi_server.models.update_organization_adaptive_policy_group_request import UpdateOrganizationAdaptivePolicyGroupRequest
from openapi_server.models.update_organization_adaptive_policy_policy_request import UpdateOrganizationAdaptivePolicyPolicyRequest
from openapi_server.models.update_organization_adaptive_policy_settings_request import UpdateOrganizationAdaptivePolicySettingsRequest
from openapi_server.models.update_organization_admin_request import UpdateOrganizationAdminRequest
from openapi_server.models.update_organization_alerts_profile_request import UpdateOrganizationAlertsProfileRequest
from openapi_server.models.update_organization_branding_policies_priorities_request import UpdateOrganizationBrandingPoliciesPrioritiesRequest
from openapi_server.models.update_organization_branding_policy_request import UpdateOrganizationBrandingPolicyRequest
from openapi_server.models.update_organization_config_template_request import UpdateOrganizationConfigTemplateRequest
from openapi_server.models.update_organization_early_access_features_opt_in_request import UpdateOrganizationEarlyAccessFeaturesOptInRequest
from openapi_server.models.update_organization_license_request import UpdateOrganizationLicenseRequest
from openapi_server.models.update_organization_login_security_request import UpdateOrganizationLoginSecurityRequest
from openapi_server.models.update_organization_policy_object_request import UpdateOrganizationPolicyObjectRequest
from openapi_server.models.update_organization_policy_objects_group_request import UpdateOrganizationPolicyObjectsGroupRequest
from openapi_server.models.update_organization_request import UpdateOrganizationRequest
from openapi_server.models.update_organization_saml_idp_request import UpdateOrganizationSamlIdpRequest
from openapi_server.models.update_organization_saml_request import UpdateOrganizationSamlRequest
from openapi_server.models.update_organization_saml_role200_response import UpdateOrganizationSamlRole200Response
from openapi_server.models.update_organization_saml_role_request import UpdateOrganizationSamlRoleRequest
from openapi_server.models.update_organization_snmp_request import UpdateOrganizationSnmpRequest


pytestmark = pytest.mark.asyncio

async def test_assign_organization_licenses_seats(client):
    """Test case for assign_organization_licenses_seats

    Assign SM seats to a network
    """
    body = openapi_server.AssignOrganizationLicensesSeatsRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/organizations/{organization_id}/licenses/assignSeats'.format(organization_id='organization_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_claim_into_organization(client):
    """Test case for claim_into_organization

    Claim a list of devices, licenses, and/or orders into an organization
    """
    body = openapi_server.ClaimIntoOrganizationRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/organizations/{organization_id}/claim'.format(organization_id='organization_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_claim_into_organization_inventory(client):
    """Test case for claim_into_organization_inventory

    Claim a list of devices, licenses, and/or orders into an organization inventory
    """
    body = openapi_server.ClaimIntoOrganizationInventoryRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/organizations/{organization_id}/inventory/claim'.format(organization_id='organization_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_clone_organization(client):
    """Test case for clone_organization

    Create a new organization by cloning the addressed organization
    """
    body = openapi_server.CloneOrganizationRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/organizations/{organization_id}/clone'.format(organization_id='organization_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_combine_organization_networks(client):
    """Test case for combine_organization_networks

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

async def test_create_organization(client):
    """Test case for create_organization

    Create a new organization
    """
    body = openapi_server.CreateOrganizationRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/organizations',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_organization_action_batch(client):
    """Test case for create_organization_action_batch

    Create an action batch
    """
    body = openapi_server.CreateOrganizationActionBatchRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/organizations/{organization_id}/actionBatches'.format(organization_id='organization_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_organization_adaptive_policy_acl(client):
    """Test case for create_organization_adaptive_policy_acl

    Creates new adaptive policy ACL
    """
    body = openapi_server.CreateOrganizationAdaptivePolicyAclRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/organizations/{organization_id}/adaptivePolicy/acls'.format(organization_id='organization_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_organization_adaptive_policy_group(client):
    """Test case for create_organization_adaptive_policy_group

    Creates a new adaptive policy group
    """
    body = openapi_server.CreateOrganizationAdaptivePolicyGroupRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/organizations/{organization_id}/adaptivePolicy/groups'.format(organization_id='organization_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_organization_adaptive_policy_policy(client):
    """Test case for create_organization_adaptive_policy_policy

    Add an Adaptive Policy
    """
    body = openapi_server.CreateOrganizationAdaptivePolicyPolicyRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/organizations/{organization_id}/adaptivePolicy/policies'.format(organization_id='organization_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_organization_admin(client):
    """Test case for create_organization_admin

    Create a new dashboard administrator
    """
    body = openapi_server.CreateOrganizationAdminRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/organizations/{organization_id}/admins'.format(organization_id='organization_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_organization_alerts_profile(client):
    """Test case for create_organization_alerts_profile

    Create an organization-wide alert configuration
    """
    body = openapi_server.CreateOrganizationAlertsProfileRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/organizations/{organization_id}/alerts/profiles'.format(organization_id='organization_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_organization_branding_policy(client):
    """Test case for create_organization_branding_policy

    Add a new branding policy to an organization
    """
    body = openapi_server.CreateOrganizationBrandingPolicyRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/organizations/{organization_id}/brandingPolicies'.format(organization_id='organization_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_organization_config_template(client):
    """Test case for create_organization_config_template

    Create a new configuration template
    """
    body = openapi_server.CreateOrganizationConfigTemplateRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/organizations/{organization_id}/configTemplates'.format(organization_id='organization_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_organization_early_access_features_opt_in(client):
    """Test case for create_organization_early_access_features_opt_in

    Create a new early access feature opt-in for an organization
    """
    body = openapi_server.CreateOrganizationEarlyAccessFeaturesOptInRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/organizations/{organization_id}/earlyAccess/features/optIns'.format(organization_id='organization_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_organization_inventory_onboarding_cloud_monitoring_export_event(client):
    """Test case for create_organization_inventory_onboarding_cloud_monitoring_export_event

    Imports event logs related to the onboarding app into elastisearch
    """
    body = openapi_server.CreateOrganizationInventoryOnboardingCloudMonitoringExportEventRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/organizations/{organization_id}/inventory/onboarding/cloudMonitoring/exportEvents'.format(organization_id='organization_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_organization_inventory_onboarding_cloud_monitoring_import(client):
    """Test case for create_organization_inventory_onboarding_cloud_monitoring_import

    Commits the import operation to complete the onboarding of a device into Dashboard for monitoring.
    """
    body = openapi_server.CreateOrganizationInventoryOnboardingCloudMonitoringImportRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/organizations/{organization_id}/inventory/onboarding/cloudMonitoring/imports'.format(organization_id='organization_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_organization_inventory_onboarding_cloud_monitoring_prepare(client):
    """Test case for create_organization_inventory_onboarding_cloud_monitoring_prepare

    Initiates or updates an import session
    """
    body = openapi_server.CreateOrganizationInventoryOnboardingCloudMonitoringPrepareRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/organizations/{organization_id}/inventory/onboarding/cloudMonitoring/prepare'.format(organization_id='organization_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_organization_network(client):
    """Test case for create_organization_network

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

async def test_create_organization_policy_object(client):
    """Test case for create_organization_policy_object

    Creates a new Policy Object.
    """
    body = openapi_server.CreateOrganizationPolicyObjectRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/organizations/{organization_id}/policyObjects'.format(organization_id='organization_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_organization_policy_objects_group(client):
    """Test case for create_organization_policy_objects_group

    Creates a new Policy Object Group.
    """
    body = openapi_server.CreateOrganizationPolicyObjectsGroupRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/organizations/{organization_id}/policyObjects/groups'.format(organization_id='organization_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_organization_saml_idp(client):
    """Test case for create_organization_saml_idp

    Create a SAML IdP for your organization.
    """
    body = openapi_server.CreateOrganizationSamlIdpRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/organizations/{organization_id}/saml/idps'.format(organization_id='organization_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_organization_saml_role(client):
    """Test case for create_organization_saml_role

    Create a SAML role
    """
    body = openapi_server.CreateOrganizationSamlRoleRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/organizations/{organization_id}/samlRoles'.format(organization_id='organization_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_organization(client):
    """Test case for delete_organization

    Delete an organization
    """
    headers = { 
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/organizations/{organization_id}'.format(organization_id='organization_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_organization_action_batch(client):
    """Test case for delete_organization_action_batch

    Delete an action batch
    """
    headers = { 
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/organizations/{organization_id}/actionBatches/{action_batch_id}'.format(organization_id='organization_id_example', action_batch_id='action_batch_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_organization_adaptive_policy_acl(client):
    """Test case for delete_organization_adaptive_policy_acl

    Deletes the specified adaptive policy ACL
    """
    headers = { 
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/organizations/{organization_id}/adaptivePolicy/acls/{acl_id}'.format(organization_id='organization_id_example', acl_id='acl_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_organization_adaptive_policy_group(client):
    """Test case for delete_organization_adaptive_policy_group

    Deletes the specified adaptive policy group and any associated policies and references
    """
    headers = { 
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/organizations/{organization_id}/adaptivePolicy/groups/{id}'.format(organization_id='organization_id_example', id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_organization_adaptive_policy_policy(client):
    """Test case for delete_organization_adaptive_policy_policy

    Delete an Adaptive Policy
    """
    headers = { 
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/organizations/{organization_id}/adaptivePolicy/policies/{id}'.format(organization_id='organization_id_example', id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_organization_admin(client):
    """Test case for delete_organization_admin

    Revoke all access for a dashboard administrator within this organization
    """
    headers = { 
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/organizations/{organization_id}/admins/{admin_id}'.format(organization_id='organization_id_example', admin_id='admin_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_organization_alerts_profile(client):
    """Test case for delete_organization_alerts_profile

    Removes an organization-wide alert config
    """
    headers = { 
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/organizations/{organization_id}/alerts/profiles/{alert_config_id}'.format(organization_id='organization_id_example', alert_config_id='alert_config_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_organization_branding_policy(client):
    """Test case for delete_organization_branding_policy

    Delete a branding policy
    """
    headers = { 
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/organizations/{organization_id}/brandingPolicies/{branding_policy_id}'.format(organization_id='organization_id_example', branding_policy_id='branding_policy_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_organization_config_template(client):
    """Test case for delete_organization_config_template

    Remove a configuration template
    """
    headers = { 
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/organizations/{organization_id}/configTemplates/{config_template_id}'.format(organization_id='organization_id_example', config_template_id='config_template_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_organization_early_access_features_opt_in(client):
    """Test case for delete_organization_early_access_features_opt_in

    Delete an early access feature opt-in
    """
    headers = { 
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/organizations/{organization_id}/earlyAccess/features/optIns/{opt_in_id}'.format(organization_id='organization_id_example', opt_in_id='opt_in_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_organization_policy_object(client):
    """Test case for delete_organization_policy_object

    Deletes a Policy Object.
    """
    headers = { 
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/organizations/{organization_id}/policyObjects/{policy_object_id}'.format(organization_id='organization_id_example', policy_object_id='policy_object_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_organization_policy_objects_group(client):
    """Test case for delete_organization_policy_objects_group

    Deletes a Policy Object Group.
    """
    headers = { 
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/organizations/{organization_id}/policyObjects/groups/{policy_object_group_id}'.format(organization_id='organization_id_example', policy_object_group_id='policy_object_group_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_organization_saml_idp(client):
    """Test case for delete_organization_saml_idp

    Remove a SAML IdP in your organization.
    """
    headers = { 
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/organizations/{organization_id}/saml/idps/{idp_id}'.format(organization_id='organization_id_example', idp_id='idp_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_organization_saml_role(client):
    """Test case for delete_organization_saml_role

    Remove a SAML role
    """
    headers = { 
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/organizations/{organization_id}/samlRoles/{saml_role_id}'.format(organization_id='organization_id_example', saml_role_id='saml_role_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_organization_user(client):
    """Test case for delete_organization_user

    Delete a user and all of its authentication methods.
    """
    headers = { 
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/organizations/{organization_id}/users/{user_id}'.format(organization_id='organization_id_example', user_id='user_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organization(client):
    """Test case for get_organization

    Return an organization
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/organizations/{organization_id}'.format(organization_id='organization_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organization_action_batch(client):
    """Test case for get_organization_action_batch

    Return an action batch
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/organizations/{organization_id}/actionBatches/{action_batch_id}'.format(organization_id='organization_id_example', action_batch_id='action_batch_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organization_action_batches(client):
    """Test case for get_organization_action_batches

    Return the list of action batches in the organization
    """
    params = [('status', 'status_example')]
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/organizations/{organization_id}/actionBatches'.format(organization_id='organization_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organization_adaptive_policy_acl(client):
    """Test case for get_organization_adaptive_policy_acl

    Returns the adaptive policy ACL information
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/organizations/{organization_id}/adaptivePolicy/acls/{acl_id}'.format(organization_id='organization_id_example', acl_id='acl_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organization_adaptive_policy_acls(client):
    """Test case for get_organization_adaptive_policy_acls

    List adaptive policy ACLs in a organization
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/organizations/{organization_id}/adaptivePolicy/acls'.format(organization_id='organization_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organization_adaptive_policy_group(client):
    """Test case for get_organization_adaptive_policy_group

    Returns an adaptive policy group
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/organizations/{organization_id}/adaptivePolicy/groups/{id}'.format(organization_id='organization_id_example', id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organization_adaptive_policy_groups(client):
    """Test case for get_organization_adaptive_policy_groups

    List adaptive policy groups in a organization
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/organizations/{organization_id}/adaptivePolicy/groups'.format(organization_id='organization_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organization_adaptive_policy_overview(client):
    """Test case for get_organization_adaptive_policy_overview

    Returns adaptive policy aggregate statistics for an organization
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/organizations/{organization_id}/adaptivePolicy/overview'.format(organization_id='organization_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organization_adaptive_policy_policies(client):
    """Test case for get_organization_adaptive_policy_policies

    List adaptive policies in an organization
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/organizations/{organization_id}/adaptivePolicy/policies'.format(organization_id='organization_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organization_adaptive_policy_policy(client):
    """Test case for get_organization_adaptive_policy_policy

    Return an adaptive policy
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/organizations/{organization_id}/adaptivePolicy/policies/{id}'.format(organization_id='organization_id_example', id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organization_adaptive_policy_settings(client):
    """Test case for get_organization_adaptive_policy_settings

    Returns global adaptive policy settings in an organization
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/organizations/{organization_id}/adaptivePolicy/settings'.format(organization_id='organization_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organization_admins(client):
    """Test case for get_organization_admins

    List the dashboard administrators in this organization
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/organizations/{organization_id}/admins'.format(organization_id='organization_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organization_alerts_profiles(client):
    """Test case for get_organization_alerts_profiles

    List all organization-wide alert configurations
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/organizations/{organization_id}/alerts/profiles'.format(organization_id='organization_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organization_api_requests(client):
    """Test case for get_organization_api_requests

    List the API requests made by an organization
    """
    params = [('t0', 't0_example'),
                    ('t1', 't1_example'),
                    ('timespan', 3.4),
                    ('perPage', 56),
                    ('startingAfter', 'starting_after_example'),
                    ('endingBefore', 'ending_before_example'),
                    ('adminId', 'admin_id_example'),
                    ('path', 'path_example'),
                    ('method', 'method_example'),
                    ('responseCode', 56),
                    ('sourceIp', 'source_ip_example'),
                    ('userAgent', 'user_agent_example'),
                    ('version', 56),
                    ('operationIds', ['operation_ids_example'])]
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/organizations/{organization_id}/apiRequests'.format(organization_id='organization_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organization_api_requests_overview(client):
    """Test case for get_organization_api_requests_overview

    Return an aggregated overview of API requests data
    """
    params = [('t0', 't0_example'),
                    ('t1', 't1_example'),
                    ('timespan', 3.4)]
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/organizations/{organization_id}/apiRequests/overview'.format(organization_id='organization_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organization_api_requests_overview_response_codes_by_interval(client):
    """Test case for get_organization_api_requests_overview_response_codes_by_interval

    Tracks organizations' API requests by response code across a given time period
    """
    params = [('t0', 't0_example'),
                    ('t1', 't1_example'),
                    ('timespan', 3.4),
                    ('interval', 56),
                    ('version', 56),
                    ('operationIds', ['operation_ids_example']),
                    ('sourceIps', ['source_ips_example']),
                    ('adminIds', ['admin_ids_example']),
                    ('userAgent', 'user_agent_example')]
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/organizations/{organization_id}/apiRequests/overview/responseCodes/byInterval'.format(organization_id='organization_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organization_branding_policies(client):
    """Test case for get_organization_branding_policies

    List the branding policies of an organization
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/organizations/{organization_id}/brandingPolicies'.format(organization_id='organization_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organization_branding_policies_priorities(client):
    """Test case for get_organization_branding_policies_priorities

    Return the branding policy IDs of an organization in priority order
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/organizations/{organization_id}/brandingPolicies/priorities'.format(organization_id='organization_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organization_branding_policy(client):
    """Test case for get_organization_branding_policy

    Return a branding policy
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/organizations/{organization_id}/brandingPolicies/{branding_policy_id}'.format(organization_id='organization_id_example', branding_policy_id='branding_policy_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organization_clients_bandwidth_usage_history(client):
    """Test case for get_organization_clients_bandwidth_usage_history

    Return data usage (in megabits per second) over time for all clients in the given organization within a given time range.
    """
    params = [('t0', 't0_example'),
                    ('t1', 't1_example'),
                    ('timespan', 3.4)]
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/organizations/{organization_id}/clients/bandwidthUsageHistory'.format(organization_id='organization_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organization_clients_overview(client):
    """Test case for get_organization_clients_overview

    Return summary information around client data usage (in mb) across the given organization.
    """
    params = [('t0', 't0_example'),
                    ('t1', 't1_example'),
                    ('timespan', 3.4)]
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/organizations/{organization_id}/clients/overview'.format(organization_id='organization_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organization_clients_search(client):
    """Test case for get_organization_clients_search

    Return the client details in an organization
    """
    params = [('mac', 'mac_example'),
                    ('perPage', 56),
                    ('startingAfter', 'starting_after_example'),
                    ('endingBefore', 'ending_before_example')]
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/organizations/{organization_id}/clients/search'.format(organization_id='organization_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organization_config_template(client):
    """Test case for get_organization_config_template

    Return a single configuration template
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/organizations/{organization_id}/configTemplates/{config_template_id}'.format(organization_id='organization_id_example', config_template_id='config_template_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organization_config_templates(client):
    """Test case for get_organization_config_templates

    List the configuration templates for this organization
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/organizations/{organization_id}/configTemplates'.format(organization_id='organization_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organization_configuration_changes(client):
    """Test case for get_organization_configuration_changes

    View the Change Log for your organization
    """
    params = [('t0', 't0_example'),
                    ('t1', 't1_example'),
                    ('timespan', 3.4),
                    ('perPage', 56),
                    ('startingAfter', 'starting_after_example'),
                    ('endingBefore', 'ending_before_example'),
                    ('networkId', 'network_id_example'),
                    ('adminId', 'admin_id_example')]
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/organizations/{organization_id}/configurationChanges'.format(organization_id='organization_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organization_devices(client):
    """Test case for get_organization_devices

    List the devices in an organization
    """
    params = [('perPage', 56),
                    ('startingAfter', 'starting_after_example'),
                    ('endingBefore', 'ending_before_example'),
                    ('configurationUpdatedAfter', 'configuration_updated_after_example'),
                    ('networkIds', ['network_ids_example']),
                    ('productTypes', ['product_types_example']),
                    ('tags', ['tags_example']),
                    ('tagsFilterType', 'tags_filter_type_example'),
                    ('name', 'name_example'),
                    ('mac', 'mac_example'),
                    ('serial', 'serial_example'),
                    ('model', 'model_example'),
                    ('macs', ['macs_example']),
                    ('serials', ['serials_example']),
                    ('sensorMetrics', ['sensor_metrics_example']),
                    ('sensorAlertProfileIds', ['sensor_alert_profile_ids_example']),
                    ('models', ['models_example'])]
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/organizations/{organization_id}/devices'.format(organization_id='organization_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organization_devices_availabilities(client):
    """Test case for get_organization_devices_availabilities

    List the availability information for devices in an organization
    """
    params = [('perPage', 56),
                    ('startingAfter', 'starting_after_example'),
                    ('endingBefore', 'ending_before_example'),
                    ('networkIds', ['network_ids_example']),
                    ('productTypes', ['product_types_example']),
                    ('serials', ['serials_example']),
                    ('tags', ['tags_example']),
                    ('tagsFilterType', 'tags_filter_type_example')]
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/organizations/{organization_id}/devices/availabilities'.format(organization_id='organization_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organization_devices_power_modules_statuses_by_device(client):
    """Test case for get_organization_devices_power_modules_statuses_by_device

    List the power status information for devices in an organization
    """
    params = [('perPage', 56),
                    ('startingAfter', 'starting_after_example'),
                    ('endingBefore', 'ending_before_example'),
                    ('networkIds', ['network_ids_example']),
                    ('productTypes', ['product_types_example']),
                    ('serials', ['serials_example']),
                    ('tags', ['tags_example']),
                    ('tagsFilterType', 'tags_filter_type_example')]
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/organizations/{organization_id}/devices/powerModules/statuses/byDevice'.format(organization_id='organization_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organization_devices_statuses(client):
    """Test case for get_organization_devices_statuses

    List the status of every Meraki device in the organization
    """
    params = [('perPage', 56),
                    ('startingAfter', 'starting_after_example'),
                    ('endingBefore', 'ending_before_example'),
                    ('networkIds', ['network_ids_example']),
                    ('serials', ['serials_example']),
                    ('statuses', ['statuses_example']),
                    ('productTypes', ['product_types_example']),
                    ('models', ['models_example']),
                    ('tags', ['tags_example']),
                    ('tagsFilterType', 'tags_filter_type_example')]
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/organizations/{organization_id}/devices/statuses'.format(organization_id='organization_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organization_devices_statuses_overview(client):
    """Test case for get_organization_devices_statuses_overview

    Return an overview of current device statuses
    """
    params = [('productTypes', ['product_types_example']),
                    ('networkIds', ['network_ids_example'])]
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/organizations/{organization_id}/devices/statuses/overview'.format(organization_id='organization_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organization_devices_uplinks_addresses_by_device(client):
    """Test case for get_organization_devices_uplinks_addresses_by_device

    List the current uplink addresses for devices in an organization.
    """
    params = [('perPage', 56),
                    ('startingAfter', 'starting_after_example'),
                    ('endingBefore', 'ending_before_example'),
                    ('networkIds', ['network_ids_example']),
                    ('productTypes', ['product_types_example']),
                    ('serials', ['serials_example']),
                    ('tags', ['tags_example']),
                    ('tagsFilterType', 'tags_filter_type_example')]
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/organizations/{organization_id}/devices/uplinks/addresses/byDevice'.format(organization_id='organization_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organization_devices_uplinks_loss_and_latency(client):
    """Test case for get_organization_devices_uplinks_loss_and_latency

    Return the uplink loss and latency for every MX in the organization from at latest 2 minutes ago
    """
    params = [('t0', 't0_example'),
                    ('t1', 't1_example'),
                    ('timespan', 3.4),
                    ('uplink', 'uplink_example'),
                    ('ip', 'ip_example')]
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/organizations/{organization_id}/devices/uplinksLossAndLatency'.format(organization_id='organization_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organization_early_access_features(client):
    """Test case for get_organization_early_access_features

    List the available early access features for organization
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/organizations/{organization_id}/earlyAccess/features'.format(organization_id='organization_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organization_early_access_features_opt_in(client):
    """Test case for get_organization_early_access_features_opt_in

    Show an early access feature opt-in for an organization
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/organizations/{organization_id}/earlyAccess/features/optIns/{opt_in_id}'.format(organization_id='organization_id_example', opt_in_id='opt_in_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organization_early_access_features_opt_ins(client):
    """Test case for get_organization_early_access_features_opt_ins

    List the early access feature opt-ins for an organization
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/organizations/{organization_id}/earlyAccess/features/optIns'.format(organization_id='organization_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organization_firmware_upgrades(client):
    """Test case for get_organization_firmware_upgrades

    Get firmware upgrade information for an organization
    """
    params = [('status', ['status_example']),
                    ('productType', ['product_type_example'])]
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/organizations/{organization_id}/firmware/upgrades'.format(organization_id='organization_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organization_firmware_upgrades_by_device(client):
    """Test case for get_organization_firmware_upgrades_by_device

    Get firmware upgrade status for the filtered devices
    """
    params = [('perPage', 56),
                    ('startingAfter', 'starting_after_example'),
                    ('endingBefore', 'ending_before_example'),
                    ('networkIds', ['network_ids_example']),
                    ('serials', ['serials_example']),
                    ('macs', ['macs_example']),
                    ('firmwareUpgradeIds', ['firmware_upgrade_ids_example']),
                    ('firmwareUpgradeBatchIds', ['firmware_upgrade_batch_ids_example'])]
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/organizations/{organization_id}/firmware/upgrades/byDevice'.format(organization_id='organization_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organization_inventory_device(client):
    """Test case for get_organization_inventory_device

    Return a single device from the inventory of an organization
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/organizations/{organization_id}/inventory/devices/{serial}'.format(organization_id='organization_id_example', serial='serial_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organization_inventory_devices(client):
    """Test case for get_organization_inventory_devices

    Return the device inventory for an organization
    """
    params = [('perPage', 56),
                    ('startingAfter', 'starting_after_example'),
                    ('endingBefore', 'ending_before_example'),
                    ('usedState', 'used_state_example'),
                    ('search', 'search_example'),
                    ('macs', ['macs_example']),
                    ('networkIds', ['network_ids_example']),
                    ('serials', ['serials_example']),
                    ('models', ['models_example']),
                    ('orderNumbers', ['order_numbers_example']),
                    ('tags', ['tags_example']),
                    ('tagsFilterType', 'tags_filter_type_example'),
                    ('productTypes', ['product_types_example'])]
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/organizations/{organization_id}/inventory/devices'.format(organization_id='organization_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organization_inventory_onboarding_cloud_monitoring_imports(client):
    """Test case for get_organization_inventory_onboarding_cloud_monitoring_imports

    Check the status of a committed Import operation
    """
    params = [('importIds', ['import_ids_example'])]
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/organizations/{organization_id}/inventory/onboarding/cloudMonitoring/imports'.format(organization_id='organization_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organization_inventory_onboarding_cloud_monitoring_networks(client):
    """Test case for get_organization_inventory_onboarding_cloud_monitoring_networks

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

async def test_get_organization_license(client):
    """Test case for get_organization_license

    Display a license
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/organizations/{organization_id}/licenses/{license_id}'.format(organization_id='organization_id_example', license_id='license_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organization_licenses(client):
    """Test case for get_organization_licenses

    List the licenses for an organization
    """
    params = [('perPage', 56),
                    ('startingAfter', 'starting_after_example'),
                    ('endingBefore', 'ending_before_example'),
                    ('deviceSerial', 'device_serial_example'),
                    ('networkId', 'network_id_example'),
                    ('state', 'state_example')]
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/organizations/{organization_id}/licenses'.format(organization_id='organization_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organization_licenses_overview(client):
    """Test case for get_organization_licenses_overview

    Return an overview of the license state for an organization
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/organizations/{organization_id}/licenses/overview'.format(organization_id='organization_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organization_login_security(client):
    """Test case for get_organization_login_security

    Returns the login security settings for an organization.
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/organizations/{organization_id}/loginSecurity'.format(organization_id='organization_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organization_networks(client):
    """Test case for get_organization_networks

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

async def test_get_organization_openapi_spec(client):
    """Test case for get_organization_openapi_spec

    Return the OpenAPI 2.0 Specification of the organization's API documentation in JSON
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/organizations/{organization_id}/openapiSpec'.format(organization_id='organization_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organization_policy_object(client):
    """Test case for get_organization_policy_object

    Shows details of a Policy Object.
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/organizations/{organization_id}/policyObjects/{policy_object_id}'.format(organization_id='organization_id_example', policy_object_id='policy_object_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organization_policy_objects(client):
    """Test case for get_organization_policy_objects

    Lists Policy Objects belonging to the organization.
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
        path='/api/v1/organizations/{organization_id}/policyObjects'.format(organization_id='organization_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organization_policy_objects_group(client):
    """Test case for get_organization_policy_objects_group

    Shows details of a Policy Object Group.
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/organizations/{organization_id}/policyObjects/groups/{policy_object_group_id}'.format(organization_id='organization_id_example', policy_object_group_id='policy_object_group_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organization_policy_objects_groups(client):
    """Test case for get_organization_policy_objects_groups

    Lists Policy Object Groups belonging to the organization.
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
        path='/api/v1/organizations/{organization_id}/policyObjects/groups'.format(organization_id='organization_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organization_saml(client):
    """Test case for get_organization_saml

    Returns the SAML SSO enabled settings for an organization.
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/organizations/{organization_id}/saml'.format(organization_id='organization_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organization_saml_idp(client):
    """Test case for get_organization_saml_idp

    Get a SAML IdP from your organization.
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/organizations/{organization_id}/saml/idps/{idp_id}'.format(organization_id='organization_id_example', idp_id='idp_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organization_saml_idps(client):
    """Test case for get_organization_saml_idps

    List the SAML IdPs in your organization.
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/organizations/{organization_id}/saml/idps'.format(organization_id='organization_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organization_saml_role(client):
    """Test case for get_organization_saml_role

    Return a SAML role
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/organizations/{organization_id}/samlRoles/{saml_role_id}'.format(organization_id='organization_id_example', saml_role_id='saml_role_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organization_saml_roles(client):
    """Test case for get_organization_saml_roles

    List the SAML roles for this organization
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/organizations/{organization_id}/samlRoles'.format(organization_id='organization_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organization_snmp(client):
    """Test case for get_organization_snmp

    Return the SNMP settings for an organization
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/organizations/{organization_id}/snmp'.format(organization_id='organization_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organization_summary_top_appliances_by_utilization(client):
    """Test case for get_organization_summary_top_appliances_by_utilization

    Return the top 10 appliances sorted by utilization over given time range.
    """
    params = [('t0', 't0_example'),
                    ('t1', 't1_example'),
                    ('timespan', 3.4)]
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/organizations/{organization_id}/summary/top/appliances/byUtilization'.format(organization_id='organization_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organization_summary_top_clients_by_usage(client):
    """Test case for get_organization_summary_top_clients_by_usage

    Return metrics for organization's top 10 clients by data usage (in mb) over given time range.
    """
    params = [('t0', 't0_example'),
                    ('t1', 't1_example'),
                    ('timespan', 3.4)]
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/organizations/{organization_id}/summary/top/clients/byUsage'.format(organization_id='organization_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organization_summary_top_clients_manufacturers_by_usage(client):
    """Test case for get_organization_summary_top_clients_manufacturers_by_usage

    Return metrics for organization's top clients by data usage (in mb) over given time range, grouped by manufacturer.
    """
    params = [('t0', 't0_example'),
                    ('t1', 't1_example'),
                    ('timespan', 3.4)]
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/organizations/{organization_id}/summary/top/clients/manufacturers/byUsage'.format(organization_id='organization_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organization_summary_top_devices_by_usage(client):
    """Test case for get_organization_summary_top_devices_by_usage

    Return metrics for organization's top 10 devices sorted by data usage over given time range
    """
    params = [('t0', 't0_example'),
                    ('t1', 't1_example'),
                    ('timespan', 3.4)]
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/organizations/{organization_id}/summary/top/devices/byUsage'.format(organization_id='organization_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organization_summary_top_devices_models_by_usage(client):
    """Test case for get_organization_summary_top_devices_models_by_usage

    Return metrics for organization's top 10 device models sorted by data usage over given time range
    """
    params = [('t0', 't0_example'),
                    ('t1', 't1_example'),
                    ('timespan', 3.4)]
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/organizations/{organization_id}/summary/top/devices/models/byUsage'.format(organization_id='organization_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organization_summary_top_ssids_by_usage(client):
    """Test case for get_organization_summary_top_ssids_by_usage

    Return metrics for organization's top 10 ssids by data usage over given time range
    """
    params = [('t0', 't0_example'),
                    ('t1', 't1_example'),
                    ('timespan', 3.4)]
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/organizations/{organization_id}/summary/top/ssids/byUsage'.format(organization_id='organization_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organization_summary_top_switches_by_energy_usage(client):
    """Test case for get_organization_summary_top_switches_by_energy_usage

    Return metrics for organization's top 10 switches by energy usage over given time range
    """
    params = [('t0', 't0_example'),
                    ('t1', 't1_example'),
                    ('timespan', 3.4)]
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/organizations/{organization_id}/summary/top/switches/byEnergyUsage'.format(organization_id='organization_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organization_uplinks_statuses(client):
    """Test case for get_organization_uplinks_statuses

    List the uplink status of every Meraki MX, MG and Z series devices in the organization
    """
    params = [('perPage', 56),
                    ('startingAfter', 'starting_after_example'),
                    ('endingBefore', 'ending_before_example'),
                    ('networkIds', ['network_ids_example']),
                    ('serials', ['serials_example']),
                    ('iccids', ['iccids_example'])]
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/organizations/{organization_id}/uplinks/statuses'.format(organization_id='organization_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organization_webhooks_alert_types(client):
    """Test case for get_organization_webhooks_alert_types

    Return a list of alert types to be used with managing webhook alerts
    """
    params = [('productType', 'product_type_example')]
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/organizations/{organization_id}/webhooks/alertTypes'.format(organization_id='organization_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organization_webhooks_logs(client):
    """Test case for get_organization_webhooks_logs

    Return the log of webhook POSTs sent
    """
    params = [('t0', 't0_example'),
                    ('t1', 't1_example'),
                    ('timespan', 3.4),
                    ('perPage', 56),
                    ('startingAfter', 'starting_after_example'),
                    ('endingBefore', 'ending_before_example'),
                    ('url', 'url_example')]
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/organizations/{organization_id}/webhooks/logs'.format(organization_id='organization_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organizations(client):
    """Test case for get_organizations

    List the organizations that the user has privileges on
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/organizations',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_move_organization_licenses(client):
    """Test case for move_organization_licenses

    Move licenses to another organization
    """
    body = openapi_server.MoveOrganizationLicensesRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/organizations/{organization_id}/licenses/move'.format(organization_id='organization_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_move_organization_licenses_seats(client):
    """Test case for move_organization_licenses_seats

    Move SM seats to another organization
    """
    body = openapi_server.MoveOrganizationLicensesSeatsRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/organizations/{organization_id}/licenses/moveSeats'.format(organization_id='organization_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_release_from_organization_inventory(client):
    """Test case for release_from_organization_inventory

    Release a list of claimed devices from an organization.
    """
    body = openapi_server.ReleaseFromOrganizationInventoryRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/organizations/{organization_id}/inventory/release'.format(organization_id='organization_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_renew_organization_licenses_seats(client):
    """Test case for renew_organization_licenses_seats

    Renew SM seats of a license
    """
    body = openapi_server.RenewOrganizationLicensesSeatsRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/organizations/{organization_id}/licenses/renewSeats'.format(organization_id='organization_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_organization(client):
    """Test case for update_organization

    Update an organization
    """
    body = openapi_server.UpdateOrganizationRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/organizations/{organization_id}'.format(organization_id='organization_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_organization_action_batch(client):
    """Test case for update_organization_action_batch

    Update an action batch
    """
    body = openapi_server.UpdateOrganizationActionBatchRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/organizations/{organization_id}/actionBatches/{action_batch_id}'.format(organization_id='organization_id_example', action_batch_id='action_batch_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_organization_adaptive_policy_acl(client):
    """Test case for update_organization_adaptive_policy_acl

    Updates an adaptive policy ACL
    """
    body = openapi_server.UpdateOrganizationAdaptivePolicyAclRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/organizations/{organization_id}/adaptivePolicy/acls/{acl_id}'.format(organization_id='organization_id_example', acl_id='acl_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_organization_adaptive_policy_group(client):
    """Test case for update_organization_adaptive_policy_group

    Updates an adaptive policy group
    """
    body = openapi_server.UpdateOrganizationAdaptivePolicyGroupRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/organizations/{organization_id}/adaptivePolicy/groups/{id}'.format(organization_id='organization_id_example', id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_organization_adaptive_policy_policy(client):
    """Test case for update_organization_adaptive_policy_policy

    Update an Adaptive Policy
    """
    body = openapi_server.UpdateOrganizationAdaptivePolicyPolicyRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/organizations/{organization_id}/adaptivePolicy/policies/{id}'.format(organization_id='organization_id_example', id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_organization_adaptive_policy_settings(client):
    """Test case for update_organization_adaptive_policy_settings

    Update global adaptive policy settings
    """
    body = openapi_server.UpdateOrganizationAdaptivePolicySettingsRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/organizations/{organization_id}/adaptivePolicy/settings'.format(organization_id='organization_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_organization_admin(client):
    """Test case for update_organization_admin

    Update an administrator
    """
    body = openapi_server.UpdateOrganizationAdminRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/organizations/{organization_id}/admins/{admin_id}'.format(organization_id='organization_id_example', admin_id='admin_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_organization_alerts_profile(client):
    """Test case for update_organization_alerts_profile

    Update an organization-wide alert config
    """
    body = openapi_server.UpdateOrganizationAlertsProfileRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/organizations/{organization_id}/alerts/profiles/{alert_config_id}'.format(organization_id='organization_id_example', alert_config_id='alert_config_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_organization_branding_policies_priorities(client):
    """Test case for update_organization_branding_policies_priorities

    Update the priority ordering of an organization's branding policies.
    """
    body = openapi_server.UpdateOrganizationBrandingPoliciesPrioritiesRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/organizations/{organization_id}/brandingPolicies/priorities'.format(organization_id='organization_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_organization_branding_policy(client):
    """Test case for update_organization_branding_policy

    Update a branding policy
    """
    body = openapi_server.UpdateOrganizationBrandingPolicyRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/organizations/{organization_id}/brandingPolicies/{branding_policy_id}'.format(organization_id='organization_id_example', branding_policy_id='branding_policy_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_organization_config_template(client):
    """Test case for update_organization_config_template

    Update a configuration template
    """
    body = openapi_server.UpdateOrganizationConfigTemplateRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/organizations/{organization_id}/configTemplates/{config_template_id}'.format(organization_id='organization_id_example', config_template_id='config_template_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_organization_early_access_features_opt_in(client):
    """Test case for update_organization_early_access_features_opt_in

    Update an early access feature opt-in for an organization
    """
    body = openapi_server.UpdateOrganizationEarlyAccessFeaturesOptInRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/organizations/{organization_id}/earlyAccess/features/optIns/{opt_in_id}'.format(organization_id='organization_id_example', opt_in_id='opt_in_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_organization_license(client):
    """Test case for update_organization_license

    Update a license
    """
    body = openapi_server.UpdateOrganizationLicenseRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/organizations/{organization_id}/licenses/{license_id}'.format(organization_id='organization_id_example', license_id='license_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_organization_login_security(client):
    """Test case for update_organization_login_security

    Update the login security settings for an organization
    """
    body = openapi_server.UpdateOrganizationLoginSecurityRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/organizations/{organization_id}/loginSecurity'.format(organization_id='organization_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_organization_policy_object(client):
    """Test case for update_organization_policy_object

    Updates a Policy Object.
    """
    body = openapi_server.UpdateOrganizationPolicyObjectRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/organizations/{organization_id}/policyObjects/{policy_object_id}'.format(organization_id='organization_id_example', policy_object_id='policy_object_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_organization_policy_objects_group(client):
    """Test case for update_organization_policy_objects_group

    Updates a Policy Object Group.
    """
    body = openapi_server.UpdateOrganizationPolicyObjectsGroupRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/organizations/{organization_id}/policyObjects/groups/{policy_object_group_id}'.format(organization_id='organization_id_example', policy_object_group_id='policy_object_group_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_organization_saml(client):
    """Test case for update_organization_saml

    Updates the SAML SSO enabled settings for an organization.
    """
    body = openapi_server.UpdateOrganizationSamlRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/organizations/{organization_id}/saml'.format(organization_id='organization_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_organization_saml_idp(client):
    """Test case for update_organization_saml_idp

    Update a SAML IdP in your organization
    """
    body = openapi_server.UpdateOrganizationSamlIdpRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/organizations/{organization_id}/saml/idps/{idp_id}'.format(organization_id='organization_id_example', idp_id='idp_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_organization_saml_role(client):
    """Test case for update_organization_saml_role

    Update a SAML role
    """
    body = openapi_server.UpdateOrganizationSamlRoleRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/organizations/{organization_id}/samlRoles/{saml_role_id}'.format(organization_id='organization_id_example', saml_role_id='saml_role_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_organization_snmp(client):
    """Test case for update_organization_snmp

    Update the SNMP settings for an organization
    """
    body = openapi_server.UpdateOrganizationSnmpRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/organizations/{organization_id}/snmp'.format(organization_id='organization_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

