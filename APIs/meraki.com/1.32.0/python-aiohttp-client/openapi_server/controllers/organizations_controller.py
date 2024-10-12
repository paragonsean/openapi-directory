from typing import List, Dict
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
from openapi_server import util


async def assign_organization_licenses_seats(request: web.Request, organization_id, body) -> web.Response:
    """Assign SM seats to a network

    Assign SM seats to a network. This will increase the managed SM device limit of the network

    :param organization_id: 
    :type organization_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = AssignOrganizationLicensesSeatsRequest.from_dict(body)
    return web.Response(status=200)


async def claim_into_organization(request: web.Request, organization_id, body=None) -> web.Response:
    """Claim a list of devices, licenses, and/or orders into an organization

    Claim a list of devices, licenses, and/or orders into an organization. When claiming by order, all devices and licenses in the order will be claimed; licenses will be added to the organization and devices will be placed in the organization&#39;s inventory.

    :param organization_id: 
    :type organization_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = ClaimIntoOrganizationRequest.from_dict(body)
    return web.Response(status=200)


async def claim_into_organization_inventory(request: web.Request, organization_id, body=None) -> web.Response:
    """Claim a list of devices, licenses, and/or orders into an organization inventory

    Claim a list of devices, licenses, and/or orders into an organization inventory. When claiming by order, all devices and licenses in the order will be claimed; licenses will be added to the organization and devices will be placed in the organization&#39;s inventory. Use /organizations/{organizationId}/inventory/release to release devices from an organization.

    :param organization_id: 
    :type organization_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = ClaimIntoOrganizationInventoryRequest.from_dict(body)
    return web.Response(status=200)


async def clone_organization(request: web.Request, organization_id, body) -> web.Response:
    """Create a new organization by cloning the addressed organization

    Create a new organization by cloning the addressed organization

    :param organization_id: 
    :type organization_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CloneOrganizationRequest.from_dict(body)
    return web.Response(status=200)


async def combine_organization_networks(request: web.Request, organization_id, body) -> web.Response:
    """Combine multiple networks into a single network

    Combine multiple networks into a single network

    :param organization_id: 
    :type organization_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CombineOrganizationNetworksRequest.from_dict(body)
    return web.Response(status=200)


async def create_organization(request: web.Request, body) -> web.Response:
    """Create a new organization

    Create a new organization

    :param body: 
    :type body: dict | bytes

    """
    body = CreateOrganizationRequest.from_dict(body)
    return web.Response(status=200)


async def create_organization_action_batch(request: web.Request, organization_id, body) -> web.Response:
    """Create an action batch

    Create an action batch

    :param organization_id: 
    :type organization_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateOrganizationActionBatchRequest.from_dict(body)
    return web.Response(status=200)


async def create_organization_adaptive_policy_acl(request: web.Request, organization_id, body) -> web.Response:
    """Creates new adaptive policy ACL

    Creates new adaptive policy ACL

    :param organization_id: 
    :type organization_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateOrganizationAdaptivePolicyAclRequest.from_dict(body)
    return web.Response(status=200)


async def create_organization_adaptive_policy_group(request: web.Request, organization_id, body) -> web.Response:
    """Creates a new adaptive policy group

    Creates a new adaptive policy group

    :param organization_id: 
    :type organization_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateOrganizationAdaptivePolicyGroupRequest.from_dict(body)
    return web.Response(status=200)


async def create_organization_adaptive_policy_policy(request: web.Request, organization_id, body) -> web.Response:
    """Add an Adaptive Policy

    Add an Adaptive Policy

    :param organization_id: 
    :type organization_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateOrganizationAdaptivePolicyPolicyRequest.from_dict(body)
    return web.Response(status=200)


async def create_organization_admin(request: web.Request, organization_id, body) -> web.Response:
    """Create a new dashboard administrator

    Create a new dashboard administrator

    :param organization_id: 
    :type organization_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateOrganizationAdminRequest.from_dict(body)
    return web.Response(status=200)


async def create_organization_alerts_profile(request: web.Request, organization_id, body) -> web.Response:
    """Create an organization-wide alert configuration

    Create an organization-wide alert configuration

    :param organization_id: 
    :type organization_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateOrganizationAlertsProfileRequest.from_dict(body)
    return web.Response(status=200)


async def create_organization_branding_policy(request: web.Request, organization_id, body=None) -> web.Response:
    """Add a new branding policy to an organization

    Add a new branding policy to an organization

    :param organization_id: 
    :type organization_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateOrganizationBrandingPolicyRequest.from_dict(body)
    return web.Response(status=200)


async def create_organization_config_template(request: web.Request, organization_id, body) -> web.Response:
    """Create a new configuration template

    Create a new configuration template

    :param organization_id: 
    :type organization_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateOrganizationConfigTemplateRequest.from_dict(body)
    return web.Response(status=200)


async def create_organization_early_access_features_opt_in(request: web.Request, organization_id, body) -> web.Response:
    """Create a new early access feature opt-in for an organization

    Create a new early access feature opt-in for an organization

    :param organization_id: 
    :type organization_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateOrganizationEarlyAccessFeaturesOptInRequest.from_dict(body)
    return web.Response(status=200)


async def create_organization_inventory_onboarding_cloud_monitoring_export_event(request: web.Request, organization_id, body) -> web.Response:
    """Imports event logs related to the onboarding app into elastisearch

    Imports event logs related to the onboarding app into elastisearch

    :param organization_id: 
    :type organization_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateOrganizationInventoryOnboardingCloudMonitoringExportEventRequest.from_dict(body)
    return web.Response(status=200)


async def create_organization_inventory_onboarding_cloud_monitoring_import(request: web.Request, organization_id, body) -> web.Response:
    """Commits the import operation to complete the onboarding of a device into Dashboard for monitoring.

    Commits the import operation to complete the onboarding of a device into Dashboard for monitoring.

    :param organization_id: 
    :type organization_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateOrganizationInventoryOnboardingCloudMonitoringImportRequest.from_dict(body)
    return web.Response(status=200)


async def create_organization_inventory_onboarding_cloud_monitoring_prepare(request: web.Request, organization_id, body) -> web.Response:
    """Initiates or updates an import session

    Initiates or updates an import session. An import ID will be generated and used when you are ready to commit the import.

    :param organization_id: 
    :type organization_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateOrganizationInventoryOnboardingCloudMonitoringPrepareRequest.from_dict(body)
    return web.Response(status=200)


async def create_organization_network(request: web.Request, organization_id, body) -> web.Response:
    """Create a network

    Create a network

    :param organization_id: 
    :type organization_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateOrganizationNetworkRequest.from_dict(body)
    return web.Response(status=200)


async def create_organization_policy_object(request: web.Request, organization_id, body) -> web.Response:
    """Creates a new Policy Object.

    Creates a new Policy Object.

    :param organization_id: 
    :type organization_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateOrganizationPolicyObjectRequest.from_dict(body)
    return web.Response(status=200)


async def create_organization_policy_objects_group(request: web.Request, organization_id, body) -> web.Response:
    """Creates a new Policy Object Group.

    Creates a new Policy Object Group.

    :param organization_id: 
    :type organization_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateOrganizationPolicyObjectsGroupRequest.from_dict(body)
    return web.Response(status=200)


async def create_organization_saml_idp(request: web.Request, organization_id, body) -> web.Response:
    """Create a SAML IdP for your organization.

    Create a SAML IdP for your organization.

    :param organization_id: 
    :type organization_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateOrganizationSamlIdpRequest.from_dict(body)
    return web.Response(status=200)


async def create_organization_saml_role(request: web.Request, organization_id, body) -> web.Response:
    """Create a SAML role

    Create a SAML role

    :param organization_id: 
    :type organization_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateOrganizationSamlRoleRequest.from_dict(body)
    return web.Response(status=200)


async def delete_organization(request: web.Request, organization_id) -> web.Response:
    """Delete an organization

    Delete an organization

    :param organization_id: 
    :type organization_id: str

    """
    return web.Response(status=200)


async def delete_organization_action_batch(request: web.Request, organization_id, action_batch_id) -> web.Response:
    """Delete an action batch

    Delete an action batch

    :param organization_id: 
    :type organization_id: str
    :param action_batch_id: 
    :type action_batch_id: str

    """
    return web.Response(status=200)


async def delete_organization_adaptive_policy_acl(request: web.Request, organization_id, acl_id) -> web.Response:
    """Deletes the specified adaptive policy ACL

    Deletes the specified adaptive policy ACL. Note this adaptive policy ACL will also be removed from policies using it.

    :param organization_id: 
    :type organization_id: str
    :param acl_id: 
    :type acl_id: str

    """
    return web.Response(status=200)


async def delete_organization_adaptive_policy_group(request: web.Request, organization_id, id) -> web.Response:
    """Deletes the specified adaptive policy group and any associated policies and references

    Deletes the specified adaptive policy group and any associated policies and references

    :param organization_id: 
    :type organization_id: str
    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def delete_organization_adaptive_policy_policy(request: web.Request, organization_id, id) -> web.Response:
    """Delete an Adaptive Policy

    Delete an Adaptive Policy

    :param organization_id: 
    :type organization_id: str
    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def delete_organization_admin(request: web.Request, organization_id, admin_id) -> web.Response:
    """Revoke all access for a dashboard administrator within this organization

    Revoke all access for a dashboard administrator within this organization

    :param organization_id: 
    :type organization_id: str
    :param admin_id: 
    :type admin_id: str

    """
    return web.Response(status=200)


async def delete_organization_alerts_profile(request: web.Request, organization_id, alert_config_id) -> web.Response:
    """Removes an organization-wide alert config

    Removes an organization-wide alert config

    :param organization_id: 
    :type organization_id: str
    :param alert_config_id: 
    :type alert_config_id: str

    """
    return web.Response(status=200)


async def delete_organization_branding_policy(request: web.Request, organization_id, branding_policy_id) -> web.Response:
    """Delete a branding policy

    Delete a branding policy

    :param organization_id: 
    :type organization_id: str
    :param branding_policy_id: 
    :type branding_policy_id: str

    """
    return web.Response(status=200)


async def delete_organization_config_template(request: web.Request, organization_id, config_template_id) -> web.Response:
    """Remove a configuration template

    Remove a configuration template

    :param organization_id: 
    :type organization_id: str
    :param config_template_id: 
    :type config_template_id: str

    """
    return web.Response(status=200)


async def delete_organization_early_access_features_opt_in(request: web.Request, organization_id, opt_in_id) -> web.Response:
    """Delete an early access feature opt-in

    Delete an early access feature opt-in

    :param organization_id: 
    :type organization_id: str
    :param opt_in_id: 
    :type opt_in_id: str

    """
    return web.Response(status=200)


async def delete_organization_policy_object(request: web.Request, organization_id, policy_object_id) -> web.Response:
    """Deletes a Policy Object.

    Deletes a Policy Object.

    :param organization_id: 
    :type organization_id: str
    :param policy_object_id: 
    :type policy_object_id: str

    """
    return web.Response(status=200)


async def delete_organization_policy_objects_group(request: web.Request, organization_id, policy_object_group_id) -> web.Response:
    """Deletes a Policy Object Group.

    Deletes a Policy Object Group.

    :param organization_id: 
    :type organization_id: str
    :param policy_object_group_id: 
    :type policy_object_group_id: str

    """
    return web.Response(status=200)


async def delete_organization_saml_idp(request: web.Request, organization_id, idp_id) -> web.Response:
    """Remove a SAML IdP in your organization.

    Remove a SAML IdP in your organization.

    :param organization_id: 
    :type organization_id: str
    :param idp_id: 
    :type idp_id: str

    """
    return web.Response(status=200)


async def delete_organization_saml_role(request: web.Request, organization_id, saml_role_id) -> web.Response:
    """Remove a SAML role

    Remove a SAML role

    :param organization_id: 
    :type organization_id: str
    :param saml_role_id: 
    :type saml_role_id: str

    """
    return web.Response(status=200)


async def delete_organization_user(request: web.Request, organization_id, user_id) -> web.Response:
    """Delete a user and all of its authentication methods.

    Delete a user and all of its authentication methods.

    :param organization_id: 
    :type organization_id: str
    :param user_id: 
    :type user_id: str

    """
    return web.Response(status=200)


async def get_organization(request: web.Request, organization_id) -> web.Response:
    """Return an organization

    Return an organization

    :param organization_id: 
    :type organization_id: str

    """
    return web.Response(status=200)


async def get_organization_action_batch(request: web.Request, organization_id, action_batch_id) -> web.Response:
    """Return an action batch

    Return an action batch

    :param organization_id: 
    :type organization_id: str
    :param action_batch_id: 
    :type action_batch_id: str

    """
    return web.Response(status=200)


async def get_organization_action_batches(request: web.Request, organization_id, status=None) -> web.Response:
    """Return the list of action batches in the organization

    Return the list of action batches in the organization

    :param organization_id: 
    :type organization_id: str
    :param status: Filter batches by status. Valid types are pending, completed, and failed.
    :type status: str

    """
    return web.Response(status=200)


async def get_organization_adaptive_policy_acl(request: web.Request, organization_id, acl_id) -> web.Response:
    """Returns the adaptive policy ACL information

    Returns the adaptive policy ACL information

    :param organization_id: 
    :type organization_id: str
    :param acl_id: 
    :type acl_id: str

    """
    return web.Response(status=200)


async def get_organization_adaptive_policy_acls(request: web.Request, organization_id) -> web.Response:
    """List adaptive policy ACLs in a organization

    List adaptive policy ACLs in a organization

    :param organization_id: 
    :type organization_id: str

    """
    return web.Response(status=200)


async def get_organization_adaptive_policy_group(request: web.Request, organization_id, id) -> web.Response:
    """Returns an adaptive policy group

    Returns an adaptive policy group

    :param organization_id: 
    :type organization_id: str
    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def get_organization_adaptive_policy_groups(request: web.Request, organization_id) -> web.Response:
    """List adaptive policy groups in a organization

    List adaptive policy groups in a organization

    :param organization_id: 
    :type organization_id: str

    """
    return web.Response(status=200)


async def get_organization_adaptive_policy_overview(request: web.Request, organization_id) -> web.Response:
    """Returns adaptive policy aggregate statistics for an organization

    Returns adaptive policy aggregate statistics for an organization

    :param organization_id: 
    :type organization_id: str

    """
    return web.Response(status=200)


async def get_organization_adaptive_policy_policies(request: web.Request, organization_id) -> web.Response:
    """List adaptive policies in an organization

    List adaptive policies in an organization

    :param organization_id: 
    :type organization_id: str

    """
    return web.Response(status=200)


async def get_organization_adaptive_policy_policy(request: web.Request, organization_id, id) -> web.Response:
    """Return an adaptive policy

    Return an adaptive policy

    :param organization_id: 
    :type organization_id: str
    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def get_organization_adaptive_policy_settings(request: web.Request, organization_id) -> web.Response:
    """Returns global adaptive policy settings in an organization

    Returns global adaptive policy settings in an organization

    :param organization_id: 
    :type organization_id: str

    """
    return web.Response(status=200)


async def get_organization_admins(request: web.Request, organization_id) -> web.Response:
    """List the dashboard administrators in this organization

    List the dashboard administrators in this organization

    :param organization_id: 
    :type organization_id: str

    """
    return web.Response(status=200)


async def get_organization_alerts_profiles(request: web.Request, organization_id) -> web.Response:
    """List all organization-wide alert configurations

    List all organization-wide alert configurations

    :param organization_id: 
    :type organization_id: str

    """
    return web.Response(status=200)


async def get_organization_api_requests(request: web.Request, organization_id, t0=None, t1=None, timespan=None, per_page=None, starting_after=None, ending_before=None, admin_id=None, path=None, method=None, response_code=None, source_ip=None, user_agent=None, version=None, operation_ids=None) -> web.Response:
    """List the API requests made by an organization

    List the API requests made by an organization

    :param organization_id: 
    :type organization_id: str
    :param t0: The beginning of the timespan for the data. The maximum lookback period is 31 days from today.
    :type t0: str
    :param t1: The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
    :type t1: str
    :param timespan: The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 31 days.
    :type timespan: float
    :param per_page: The number of entries per page returned. Acceptable range is 3 - 1000. Default is 50.
    :type per_page: int
    :param starting_after: A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type starting_after: str
    :param ending_before: A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type ending_before: str
    :param admin_id: Filter the results by the ID of the admin who made the API requests
    :type admin_id: str
    :param path: Filter the results by the path of the API requests
    :type path: str
    :param method: Filter the results by the method of the API requests (must be &#39;GET&#39;, &#39;PUT&#39;, &#39;POST&#39; or &#39;DELETE&#39;)
    :type method: str
    :param response_code: Filter the results by the response code of the API requests
    :type response_code: int
    :param source_ip: Filter the results by the IP address of the originating API request
    :type source_ip: str
    :param user_agent: Filter the results by the user agent string of the API request
    :type user_agent: str
    :param version: Filter the results by the API version of the API request
    :type version: int
    :param operation_ids: Filter the results by one or more operation IDs for the API request
    :type operation_ids: List[str]

    """
    return web.Response(status=200)


async def get_organization_api_requests_overview(request: web.Request, organization_id, t0=None, t1=None, timespan=None) -> web.Response:
    """Return an aggregated overview of API requests data

    Return an aggregated overview of API requests data

    :param organization_id: 
    :type organization_id: str
    :param t0: The beginning of the timespan for the data. The maximum lookback period is 31 days from today.
    :type t0: str
    :param t1: The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
    :type t1: str
    :param timespan: The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 31 days.
    :type timespan: float

    """
    return web.Response(status=200)


async def get_organization_api_requests_overview_response_codes_by_interval(request: web.Request, organization_id, t0=None, t1=None, timespan=None, interval=None, version=None, operation_ids=None, source_ips=None, admin_ids=None, user_agent=None) -> web.Response:
    """Tracks organizations&#39; API requests by response code across a given time period

    Tracks organizations&#39; API requests by response code across a given time period

    :param organization_id: 
    :type organization_id: str
    :param t0: The beginning of the timespan for the data. The maximum lookback period is 31 days from today.
    :type t0: str
    :param t1: The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
    :type t1: str
    :param timespan: The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 31 days. If interval is provided, the timespan will be autocalculated.
    :type timespan: float
    :param interval: The time interval in seconds for returned data. The valid intervals are: 120, 3600, 14400, 21600. The default is 21600. Interval is calculated if time params are provided.
    :type interval: int
    :param version: Filter by API version of the endpoint. Allowable values are: [0, 1]
    :type version: int
    :param operation_ids: Filter by operation ID of the endpoint
    :type operation_ids: List[str]
    :param source_ips: Filter by source IP that made the API request
    :type source_ips: List[str]
    :param admin_ids: Filter by admin ID of user that made the API request
    :type admin_ids: List[str]
    :param user_agent: Filter by user agent string for API request. This will filter by a complete or partial match.
    :type user_agent: str

    """
    return web.Response(status=200)


async def get_organization_branding_policies(request: web.Request, organization_id) -> web.Response:
    """List the branding policies of an organization

    List the branding policies of an organization

    :param organization_id: 
    :type organization_id: str

    """
    return web.Response(status=200)


async def get_organization_branding_policies_priorities(request: web.Request, organization_id) -> web.Response:
    """Return the branding policy IDs of an organization in priority order

    Return the branding policy IDs of an organization in priority order. IDs are ordered in ascending order of priority (IDs later in the array have higher priority).

    :param organization_id: 
    :type organization_id: str

    """
    return web.Response(status=200)


async def get_organization_branding_policy(request: web.Request, organization_id, branding_policy_id) -> web.Response:
    """Return a branding policy

    Return a branding policy

    :param organization_id: 
    :type organization_id: str
    :param branding_policy_id: 
    :type branding_policy_id: str

    """
    return web.Response(status=200)


async def get_organization_clients_bandwidth_usage_history(request: web.Request, organization_id, t0=None, t1=None, timespan=None) -> web.Response:
    """Return data usage (in megabits per second) over time for all clients in the given organization within a given time range.

    Return data usage (in megabits per second) over time for all clients in the given organization within a given time range.

    :param organization_id: 
    :type organization_id: str
    :param t0: The beginning of the timespan for the data.
    :type t0: str
    :param t1: The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
    :type t1: str
    :param timespan: The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 1 day.
    :type timespan: float

    """
    return web.Response(status=200)


async def get_organization_clients_overview(request: web.Request, organization_id, t0=None, t1=None, timespan=None) -> web.Response:
    """Return summary information around client data usage (in mb) across the given organization.

    Return summary information around client data usage (in mb) across the given organization.

    :param organization_id: 
    :type organization_id: str
    :param t0: The beginning of the timespan for the data.
    :type t0: str
    :param t1: The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
    :type t1: str
    :param timespan: The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 1 day.
    :type timespan: float

    """
    return web.Response(status=200)


async def get_organization_clients_search(request: web.Request, organization_id, mac, per_page=None, starting_after=None, ending_before=None) -> web.Response:
    """Return the client details in an organization

    Return the client details in an organization

    :param organization_id: 
    :type organization_id: str
    :param mac: The MAC address of the client. Required.
    :type mac: str
    :param per_page: The number of entries per page returned. Acceptable range is 3 - 5. Default is 5.
    :type per_page: int
    :param starting_after: A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type starting_after: str
    :param ending_before: A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type ending_before: str

    """
    return web.Response(status=200)


async def get_organization_config_template(request: web.Request, organization_id, config_template_id) -> web.Response:
    """Return a single configuration template

    Return a single configuration template

    :param organization_id: 
    :type organization_id: str
    :param config_template_id: 
    :type config_template_id: str

    """
    return web.Response(status=200)


async def get_organization_config_templates(request: web.Request, organization_id) -> web.Response:
    """List the configuration templates for this organization

    List the configuration templates for this organization

    :param organization_id: 
    :type organization_id: str

    """
    return web.Response(status=200)


async def get_organization_configuration_changes(request: web.Request, organization_id, t0=None, t1=None, timespan=None, per_page=None, starting_after=None, ending_before=None, network_id=None, admin_id=None) -> web.Response:
    """View the Change Log for your organization

    View the Change Log for your organization

    :param organization_id: 
    :type organization_id: str
    :param t0: The beginning of the timespan for the data. The maximum lookback period is 365 days from today.
    :type t0: str
    :param t1: The end of the timespan for the data. t1 can be a maximum of 365 days after t0.
    :type t1: str
    :param timespan: The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 365 days. The default is 365 days.
    :type timespan: float
    :param per_page: The number of entries per page returned. Acceptable range is 3 - 5000. Default is 5000.
    :type per_page: int
    :param starting_after: A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type starting_after: str
    :param ending_before: A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type ending_before: str
    :param network_id: Filters on the given network
    :type network_id: str
    :param admin_id: Filters on the given Admin
    :type admin_id: str

    """
    return web.Response(status=200)


async def get_organization_devices(request: web.Request, organization_id, per_page=None, starting_after=None, ending_before=None, configuration_updated_after=None, network_ids=None, product_types=None, tags=None, tags_filter_type=None, name=None, mac=None, serial=None, model=None, macs=None, serials=None, sensor_metrics=None, sensor_alert_profile_ids=None, models=None) -> web.Response:
    """List the devices in an organization

    List the devices in an organization

    :param organization_id: 
    :type organization_id: str
    :param per_page: The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
    :type per_page: int
    :param starting_after: A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type starting_after: str
    :param ending_before: A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type ending_before: str
    :param configuration_updated_after: Filter results by whether or not the device&#39;s configuration has been updated after the given timestamp
    :type configuration_updated_after: str
    :param network_ids: Optional parameter to filter devices by network.
    :type network_ids: List[str]
    :param product_types: Optional parameter to filter devices by product type. Valid types are wireless, appliance, switch, systemsManager, camera, cellularGateway, and sensor.
    :type product_types: List[str]
    :param tags: Optional parameter to filter devices by tags.
    :type tags: List[str]
    :param tags_filter_type: Optional parameter of value &#39;withAnyTags&#39; or &#39;withAllTags&#39; to indicate whether to return networks which contain ANY or ALL of the included tags. If no type is included, &#39;withAnyTags&#39; will be selected.
    :type tags_filter_type: str
    :param name: Optional parameter to filter devices by name. All returned devices will have a name that contains the search term or is an exact match.
    :type name: str
    :param mac: Optional parameter to filter devices by MAC address. All returned devices will have a MAC address that contains the search term or is an exact match.
    :type mac: str
    :param serial: Optional parameter to filter devices by serial number. All returned devices will have a serial number that contains the search term or is an exact match.
    :type serial: str
    :param model: Optional parameter to filter devices by model. All returned devices will have a model that contains the search term or is an exact match.
    :type model: str
    :param macs: Optional parameter to filter devices by one or more MAC addresses. All returned devices will have a MAC address that is an exact match.
    :type macs: List[str]
    :param serials: Optional parameter to filter devices by one or more serial numbers. All returned devices will have a serial number that is an exact match.
    :type serials: List[str]
    :param sensor_metrics: Optional parameter to filter devices by the metrics that they provide. Only applies to sensor devices.
    :type sensor_metrics: List[str]
    :param sensor_alert_profile_ids: Optional parameter to filter devices by the alert profiles that are bound to them. Only applies to sensor devices.
    :type sensor_alert_profile_ids: List[str]
    :param models: Optional parameter to filter devices by one or more models. All returned devices will have a model that is an exact match.
    :type models: List[str]

    """
    return web.Response(status=200)


async def get_organization_devices_availabilities(request: web.Request, organization_id, per_page=None, starting_after=None, ending_before=None, network_ids=None, product_types=None, serials=None, tags=None, tags_filter_type=None) -> web.Response:
    """List the availability information for devices in an organization

    List the availability information for devices in an organization. The data returned by this endpoint is updated every 5 minutes.

    :param organization_id: 
    :type organization_id: str
    :param per_page: The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
    :type per_page: int
    :param starting_after: A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type starting_after: str
    :param ending_before: A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type ending_before: str
    :param network_ids: Optional parameter to filter device availabilities by network ID. This filter uses multiple exact matches.
    :type network_ids: List[str]
    :param product_types: Optional parameter to filter device availabilities by device product types. This filter uses multiple exact matches.
    :type product_types: List[str]
    :param serials: Optional parameter to filter device availabilities by device serial numbers. This filter uses multiple exact matches.
    :type serials: List[str]
    :param tags: An optional parameter to filter devices by tags. The filtering is case-sensitive. If tags are included, &#39;tagsFilterType&#39; should also be included (see below). This filter uses multiple exact matches.
    :type tags: List[str]
    :param tags_filter_type: An optional parameter of value &#39;withAnyTags&#39; or &#39;withAllTags&#39; to indicate whether to return devices which contain ANY or ALL of the included tags. If no type is included, &#39;withAnyTags&#39; will be selected.
    :type tags_filter_type: str

    """
    return web.Response(status=200)


async def get_organization_devices_power_modules_statuses_by_device(request: web.Request, organization_id, per_page=None, starting_after=None, ending_before=None, network_ids=None, product_types=None, serials=None, tags=None, tags_filter_type=None) -> web.Response:
    """List the power status information for devices in an organization

    List the power status information for devices in an organization. The data returned by this endpoint is updated every 5 minutes.

    :param organization_id: 
    :type organization_id: str
    :param per_page: The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
    :type per_page: int
    :param starting_after: A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type starting_after: str
    :param ending_before: A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type ending_before: str
    :param network_ids: Optional parameter to filter device availabilities by network ID. This filter uses multiple exact matches.
    :type network_ids: List[str]
    :param product_types: Optional parameter to filter device availabilities by device product types. This filter uses multiple exact matches.
    :type product_types: List[str]
    :param serials: Optional parameter to filter device availabilities by device serial numbers. This filter uses multiple exact matches.
    :type serials: List[str]
    :param tags: An optional parameter to filter devices by tags. The filtering is case-sensitive. If tags are included, &#39;tagsFilterType&#39; should also be included (see below). This filter uses multiple exact matches.
    :type tags: List[str]
    :param tags_filter_type: An optional parameter of value &#39;withAnyTags&#39; or &#39;withAllTags&#39; to indicate whether to return devices which contain ANY or ALL of the included tags. If no type is included, &#39;withAnyTags&#39; will be selected.
    :type tags_filter_type: str

    """
    return web.Response(status=200)


async def get_organization_devices_statuses(request: web.Request, organization_id, per_page=None, starting_after=None, ending_before=None, network_ids=None, serials=None, statuses=None, product_types=None, models=None, tags=None, tags_filter_type=None) -> web.Response:
    """List the status of every Meraki device in the organization

    List the status of every Meraki device in the organization

    :param organization_id: 
    :type organization_id: str
    :param per_page: The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
    :type per_page: int
    :param starting_after: A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type starting_after: str
    :param ending_before: A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type ending_before: str
    :param network_ids: Optional parameter to filter devices by network ids.
    :type network_ids: List[str]
    :param serials: Optional parameter to filter devices by serials.
    :type serials: List[str]
    :param statuses: Optional parameter to filter devices by statuses. Valid statuses are [\&quot;online\&quot;, \&quot;alerting\&quot;, \&quot;offline\&quot;, \&quot;dormant\&quot;].
    :type statuses: List[str]
    :param product_types: An optional parameter to filter device statuses by product type. Valid types are wireless, appliance, switch, systemsManager, camera, cellularGateway, and sensor.
    :type product_types: List[str]
    :param models: Optional parameter to filter devices by models.
    :type models: List[str]
    :param tags: An optional parameter to filter devices by tags. The filtering is case-sensitive. If tags are included, &#39;tagsFilterType&#39; should also be included (see below).
    :type tags: List[str]
    :param tags_filter_type: An optional parameter of value &#39;withAnyTags&#39; or &#39;withAllTags&#39; to indicate whether to return devices which contain ANY or ALL of the included tags. If no type is included, &#39;withAnyTags&#39; will be selected.
    :type tags_filter_type: str

    """
    return web.Response(status=200)


async def get_organization_devices_statuses_overview(request: web.Request, organization_id, product_types=None, network_ids=None) -> web.Response:
    """Return an overview of current device statuses

    Return an overview of current device statuses

    :param organization_id: 
    :type organization_id: str
    :param product_types: An optional parameter to filter device statuses by product type. Valid types are wireless, appliance, switch, systemsManager, camera, cellularGateway, and sensor.
    :type product_types: List[str]
    :param network_ids: An optional parameter to filter device statuses by network.
    :type network_ids: List[str]

    """
    return web.Response(status=200)


async def get_organization_devices_uplinks_addresses_by_device(request: web.Request, organization_id, per_page=None, starting_after=None, ending_before=None, network_ids=None, product_types=None, serials=None, tags=None, tags_filter_type=None) -> web.Response:
    """List the current uplink addresses for devices in an organization.

    List the current uplink addresses for devices in an organization.

    :param organization_id: 
    :type organization_id: str
    :param per_page: The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
    :type per_page: int
    :param starting_after: A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type starting_after: str
    :param ending_before: A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type ending_before: str
    :param network_ids: Optional parameter to filter device uplinks by network ID. This filter uses multiple exact matches.
    :type network_ids: List[str]
    :param product_types: Optional parameter to filter device uplinks by device product types. This filter uses multiple exact matches.
    :type product_types: List[str]
    :param serials: Optional parameter to filter device availabilities by device serial numbers. This filter uses multiple exact matches.
    :type serials: List[str]
    :param tags: An optional parameter to filter devices by tags. The filtering is case-sensitive. If tags are included, &#39;tagsFilterType&#39; should also be included (see below). This filter uses multiple exact matches.
    :type tags: List[str]
    :param tags_filter_type: An optional parameter of value &#39;withAnyTags&#39; or &#39;withAllTags&#39; to indicate whether to return devices which contain ANY or ALL of the included tags. If no type is included, &#39;withAnyTags&#39; will be selected.
    :type tags_filter_type: str

    """
    return web.Response(status=200)


async def get_organization_devices_uplinks_loss_and_latency(request: web.Request, organization_id, t0=None, t1=None, timespan=None, uplink=None, ip=None) -> web.Response:
    """Return the uplink loss and latency for every MX in the organization from at latest 2 minutes ago

    Return the uplink loss and latency for every MX in the organization from at latest 2 minutes ago

    :param organization_id: 
    :type organization_id: str
    :param t0: The beginning of the timespan for the data. The maximum lookback period is 60 days from today.
    :type t0: str
    :param t1: The end of the timespan for the data. t1 can be a maximum of 5 minutes after t0. The latest possible time that t1 can be is 2 minutes into the past.
    :type t1: str
    :param timespan: The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 5 minutes. The default is 5 minutes.
    :type timespan: float
    :param uplink: Optional filter for a specific WAN uplink. Valid uplinks are wan1, wan2, cellular. Default will return all uplinks.
    :type uplink: str
    :param ip: Optional filter for a specific destination IP. Default will return all destination IPs.
    :type ip: str

    """
    return web.Response(status=200)


async def get_organization_early_access_features(request: web.Request, organization_id) -> web.Response:
    """List the available early access features for organization

    List the available early access features for organization

    :param organization_id: 
    :type organization_id: str

    """
    return web.Response(status=200)


async def get_organization_early_access_features_opt_in(request: web.Request, organization_id, opt_in_id) -> web.Response:
    """Show an early access feature opt-in for an organization

    Show an early access feature opt-in for an organization

    :param organization_id: 
    :type organization_id: str
    :param opt_in_id: 
    :type opt_in_id: str

    """
    return web.Response(status=200)


async def get_organization_early_access_features_opt_ins(request: web.Request, organization_id) -> web.Response:
    """List the early access feature opt-ins for an organization

    List the early access feature opt-ins for an organization

    :param organization_id: 
    :type organization_id: str

    """
    return web.Response(status=200)


async def get_organization_firmware_upgrades(request: web.Request, organization_id, status=None, product_type=None) -> web.Response:
    """Get firmware upgrade information for an organization

    Get firmware upgrade information for an organization

    :param organization_id: 
    :type organization_id: str
    :param status: The status of an upgrade 
    :type status: List[str]
    :param product_type: The product type in a given upgrade ID
    :type product_type: List[str]

    """
    return web.Response(status=200)


async def get_organization_firmware_upgrades_by_device(request: web.Request, organization_id, per_page=None, starting_after=None, ending_before=None, network_ids=None, serials=None, macs=None, firmware_upgrade_ids=None, firmware_upgrade_batch_ids=None) -> web.Response:
    """Get firmware upgrade status for the filtered devices

    Get firmware upgrade status for the filtered devices

    :param organization_id: 
    :type organization_id: str
    :param per_page: The number of entries per page returned. Acceptable range is 3 - 50. Default is 50.
    :type per_page: int
    :param starting_after: A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type starting_after: str
    :param ending_before: A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type ending_before: str
    :param network_ids: Optional parameter to filter by network
    :type network_ids: List[str]
    :param serials: Optional parameter to filter by serial number.  All returned devices will have a serial number that is an exact match.
    :type serials: List[str]
    :param macs: Optional parameter to filter by one or more MAC addresses belonging to devices. All devices returned belong to MAC addresses that are an exact match.
    :type macs: List[str]
    :param firmware_upgrade_ids: Optional parameter to filter by firmware upgrade ids.
    :type firmware_upgrade_ids: List[str]
    :param firmware_upgrade_batch_ids: Optional parameter to filter by firmware upgrade batch ids.
    :type firmware_upgrade_batch_ids: List[str]

    """
    return web.Response(status=200)


async def get_organization_inventory_device(request: web.Request, organization_id, serial) -> web.Response:
    """Return a single device from the inventory of an organization

    Return a single device from the inventory of an organization

    :param organization_id: 
    :type organization_id: str
    :param serial: 
    :type serial: str

    """
    return web.Response(status=200)


async def get_organization_inventory_devices(request: web.Request, organization_id, per_page=None, starting_after=None, ending_before=None, used_state=None, search=None, macs=None, network_ids=None, serials=None, models=None, order_numbers=None, tags=None, tags_filter_type=None, product_types=None) -> web.Response:
    """Return the device inventory for an organization

    Return the device inventory for an organization

    :param organization_id: 
    :type organization_id: str
    :param per_page: The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
    :type per_page: int
    :param starting_after: A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type starting_after: str
    :param ending_before: A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type ending_before: str
    :param used_state: Filter results by used or unused inventory. Accepted values are &#39;used&#39; or &#39;unused&#39;.
    :type used_state: str
    :param search: Search for devices in inventory based on serial number, mac address, or model.
    :type search: str
    :param macs: Search for devices in inventory based on mac addresses.
    :type macs: List[str]
    :param network_ids: Search for devices in inventory based on network ids.
    :type network_ids: List[str]
    :param serials: Search for devices in inventory based on serials.
    :type serials: List[str]
    :param models: Search for devices in inventory based on model.
    :type models: List[str]
    :param order_numbers: Search for devices in inventory based on order numbers.
    :type order_numbers: List[str]
    :param tags: Filter devices by tags. The filtering is case-sensitive. If tags are included, &#39;tagsFilterType&#39; should also be included (see below).
    :type tags: List[str]
    :param tags_filter_type: To use with &#39;tags&#39; parameter, to filter devices which contain ANY or ALL given tags. Accepted values are &#39;withAnyTags&#39; or &#39;withAllTags&#39;, default is &#39;withAnyTags&#39;.
    :type tags_filter_type: str
    :param product_types: Filter devices by product type. Accepted values are appliance, camera, cellularGateway, sensor, switch, systemsManager, and wireless.
    :type product_types: List[str]

    """
    return web.Response(status=200)


async def get_organization_inventory_onboarding_cloud_monitoring_imports(request: web.Request, organization_id, import_ids) -> web.Response:
    """Check the status of a committed Import operation

    Check the status of a committed Import operation

    :param organization_id: 
    :type organization_id: str
    :param import_ids: import ids from an imports
    :type import_ids: List[str]

    """
    return web.Response(status=200)


async def get_organization_inventory_onboarding_cloud_monitoring_networks(request: web.Request, organization_id, device_type, per_page=None, starting_after=None, ending_before=None) -> web.Response:
    """Returns list of networks eligible for adding cloud monitored device

    Returns list of networks eligible for adding cloud monitored device

    :param organization_id: 
    :type organization_id: str
    :param device_type: Device Type switch or wireless controller
    :type device_type: str
    :param per_page: The number of entries per page returned. Acceptable range is 3 - 100000. Default is 1000.
    :type per_page: int
    :param starting_after: A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type starting_after: str
    :param ending_before: A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type ending_before: str

    """
    return web.Response(status=200)


async def get_organization_license(request: web.Request, organization_id, license_id) -> web.Response:
    """Display a license

    Display a license

    :param organization_id: 
    :type organization_id: str
    :param license_id: 
    :type license_id: str

    """
    return web.Response(status=200)


async def get_organization_licenses(request: web.Request, organization_id, per_page=None, starting_after=None, ending_before=None, device_serial=None, network_id=None, state=None) -> web.Response:
    """List the licenses for an organization

    List the licenses for an organization

    :param organization_id: 
    :type organization_id: str
    :param per_page: The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
    :type per_page: int
    :param starting_after: A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type starting_after: str
    :param ending_before: A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type ending_before: str
    :param device_serial: Filter the licenses to those assigned to a particular device. Returned in the same order that they are queued to the device.
    :type device_serial: str
    :param network_id: Filter the licenses to those assigned in a particular network
    :type network_id: str
    :param state: Filter the licenses to those in a particular state. Can be one of &#39;active&#39;, &#39;expired&#39;, &#39;expiring&#39;, &#39;recentlyQueued&#39;, &#39;unused&#39; or &#39;unusedActive&#39;
    :type state: str

    """
    return web.Response(status=200)


async def get_organization_licenses_overview(request: web.Request, organization_id) -> web.Response:
    """Return an overview of the license state for an organization

    Return an overview of the license state for an organization

    :param organization_id: 
    :type organization_id: str

    """
    return web.Response(status=200)


async def get_organization_login_security(request: web.Request, organization_id) -> web.Response:
    """Returns the login security settings for an organization.

    Returns the login security settings for an organization.

    :param organization_id: 
    :type organization_id: str

    """
    return web.Response(status=200)


async def get_organization_networks(request: web.Request, organization_id, config_template_id=None, is_bound_to_config_template=None, tags=None, tags_filter_type=None, per_page=None, starting_after=None, ending_before=None) -> web.Response:
    """List the networks that the user has privileges on in an organization

    List the networks that the user has privileges on in an organization

    :param organization_id: 
    :type organization_id: str
    :param config_template_id: An optional parameter that is the ID of a config template. Will return all networks bound to that template.
    :type config_template_id: str
    :param is_bound_to_config_template: An optional parameter to filter config template bound networks. If configTemplateId is set, this cannot be false.
    :type is_bound_to_config_template: bool
    :param tags: An optional parameter to filter networks by tags. The filtering is case-sensitive. If tags are included, &#39;tagsFilterType&#39; should also be included (see below).
    :type tags: List[str]
    :param tags_filter_type: An optional parameter of value &#39;withAnyTags&#39; or &#39;withAllTags&#39; to indicate whether to return networks which contain ANY or ALL of the included tags. If no type is included, &#39;withAnyTags&#39; will be selected.
    :type tags_filter_type: str
    :param per_page: The number of entries per page returned. Acceptable range is 3 - 100000. Default is 1000.
    :type per_page: int
    :param starting_after: A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type starting_after: str
    :param ending_before: A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type ending_before: str

    """
    return web.Response(status=200)


async def get_organization_openapi_spec(request: web.Request, organization_id) -> web.Response:
    """Return the OpenAPI 2.0 Specification of the organization&#39;s API documentation in JSON

    Return the OpenAPI 2.0 Specification of the organization&#39;s API documentation in JSON

    :param organization_id: 
    :type organization_id: str

    """
    return web.Response(status=200)


async def get_organization_policy_object(request: web.Request, organization_id, policy_object_id) -> web.Response:
    """Shows details of a Policy Object.

    Shows details of a Policy Object.

    :param organization_id: 
    :type organization_id: str
    :param policy_object_id: 
    :type policy_object_id: str

    """
    return web.Response(status=200)


async def get_organization_policy_objects(request: web.Request, organization_id, per_page=None, starting_after=None, ending_before=None) -> web.Response:
    """Lists Policy Objects belonging to the organization.

    Lists Policy Objects belonging to the organization.

    :param organization_id: 
    :type organization_id: str
    :param per_page: The number of entries per page returned. Acceptable range is 10 - 5000. Default is 5000.
    :type per_page: int
    :param starting_after: A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type starting_after: str
    :param ending_before: A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type ending_before: str

    """
    return web.Response(status=200)


async def get_organization_policy_objects_group(request: web.Request, organization_id, policy_object_group_id) -> web.Response:
    """Shows details of a Policy Object Group.

    Shows details of a Policy Object Group.

    :param organization_id: 
    :type organization_id: str
    :param policy_object_group_id: 
    :type policy_object_group_id: str

    """
    return web.Response(status=200)


async def get_organization_policy_objects_groups(request: web.Request, organization_id, per_page=None, starting_after=None, ending_before=None) -> web.Response:
    """Lists Policy Object Groups belonging to the organization.

    Lists Policy Object Groups belonging to the organization.

    :param organization_id: 
    :type organization_id: str
    :param per_page: The number of entries per page returned. Acceptable range is 10 - 1000. Default is 1000.
    :type per_page: int
    :param starting_after: A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type starting_after: str
    :param ending_before: A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type ending_before: str

    """
    return web.Response(status=200)


async def get_organization_saml(request: web.Request, organization_id) -> web.Response:
    """Returns the SAML SSO enabled settings for an organization.

    Returns the SAML SSO enabled settings for an organization.

    :param organization_id: 
    :type organization_id: str

    """
    return web.Response(status=200)


async def get_organization_saml_idp(request: web.Request, organization_id, idp_id) -> web.Response:
    """Get a SAML IdP from your organization.

    Get a SAML IdP from your organization.

    :param organization_id: 
    :type organization_id: str
    :param idp_id: 
    :type idp_id: str

    """
    return web.Response(status=200)


async def get_organization_saml_idps(request: web.Request, organization_id) -> web.Response:
    """List the SAML IdPs in your organization.

    List the SAML IdPs in your organization.

    :param organization_id: 
    :type organization_id: str

    """
    return web.Response(status=200)


async def get_organization_saml_role(request: web.Request, organization_id, saml_role_id) -> web.Response:
    """Return a SAML role

    Return a SAML role

    :param organization_id: 
    :type organization_id: str
    :param saml_role_id: 
    :type saml_role_id: str

    """
    return web.Response(status=200)


async def get_organization_saml_roles(request: web.Request, organization_id) -> web.Response:
    """List the SAML roles for this organization

    List the SAML roles for this organization

    :param organization_id: 
    :type organization_id: str

    """
    return web.Response(status=200)


async def get_organization_snmp(request: web.Request, organization_id) -> web.Response:
    """Return the SNMP settings for an organization

    Return the SNMP settings for an organization

    :param organization_id: 
    :type organization_id: str

    """
    return web.Response(status=200)


async def get_organization_summary_top_appliances_by_utilization(request: web.Request, organization_id, t0=None, t1=None, timespan=None) -> web.Response:
    """Return the top 10 appliances sorted by utilization over given time range.

    Return the top 10 appliances sorted by utilization over given time range.

    :param organization_id: 
    :type organization_id: str
    :param t0: The beginning of the timespan for the data.
    :type t0: str
    :param t1: The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
    :type t1: str
    :param timespan: The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 1 day.
    :type timespan: float

    """
    return web.Response(status=200)


async def get_organization_summary_top_clients_by_usage(request: web.Request, organization_id, t0=None, t1=None, timespan=None) -> web.Response:
    """Return metrics for organization&#39;s top 10 clients by data usage (in mb) over given time range.

    Return metrics for organization&#39;s top 10 clients by data usage (in mb) over given time range.

    :param organization_id: 
    :type organization_id: str
    :param t0: The beginning of the timespan for the data.
    :type t0: str
    :param t1: The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
    :type t1: str
    :param timespan: The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 1 day.
    :type timespan: float

    """
    return web.Response(status=200)


async def get_organization_summary_top_clients_manufacturers_by_usage(request: web.Request, organization_id, t0=None, t1=None, timespan=None) -> web.Response:
    """Return metrics for organization&#39;s top clients by data usage (in mb) over given time range, grouped by manufacturer.

    Return metrics for organization&#39;s top clients by data usage (in mb) over given time range, grouped by manufacturer.

    :param organization_id: 
    :type organization_id: str
    :param t0: The beginning of the timespan for the data.
    :type t0: str
    :param t1: The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
    :type t1: str
    :param timespan: The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 1 day.
    :type timespan: float

    """
    return web.Response(status=200)


async def get_organization_summary_top_devices_by_usage(request: web.Request, organization_id, t0=None, t1=None, timespan=None) -> web.Response:
    """Return metrics for organization&#39;s top 10 devices sorted by data usage over given time range

    Return metrics for organization&#39;s top 10 devices sorted by data usage over given time range. Default unit is megabytes.

    :param organization_id: 
    :type organization_id: str
    :param t0: The beginning of the timespan for the data.
    :type t0: str
    :param t1: The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
    :type t1: str
    :param timespan: The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 1 day.
    :type timespan: float

    """
    return web.Response(status=200)


async def get_organization_summary_top_devices_models_by_usage(request: web.Request, organization_id, t0=None, t1=None, timespan=None) -> web.Response:
    """Return metrics for organization&#39;s top 10 device models sorted by data usage over given time range

    Return metrics for organization&#39;s top 10 device models sorted by data usage over given time range. Default unit is megabytes.

    :param organization_id: 
    :type organization_id: str
    :param t0: The beginning of the timespan for the data.
    :type t0: str
    :param t1: The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
    :type t1: str
    :param timespan: The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 1 day.
    :type timespan: float

    """
    return web.Response(status=200)


async def get_organization_summary_top_ssids_by_usage(request: web.Request, organization_id, t0=None, t1=None, timespan=None) -> web.Response:
    """Return metrics for organization&#39;s top 10 ssids by data usage over given time range

    Return metrics for organization&#39;s top 10 ssids by data usage over given time range. Default unit is megabytes.

    :param organization_id: 
    :type organization_id: str
    :param t0: The beginning of the timespan for the data.
    :type t0: str
    :param t1: The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
    :type t1: str
    :param timespan: The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 1 day.
    :type timespan: float

    """
    return web.Response(status=200)


async def get_organization_summary_top_switches_by_energy_usage(request: web.Request, organization_id, t0=None, t1=None, timespan=None) -> web.Response:
    """Return metrics for organization&#39;s top 10 switches by energy usage over given time range

    Return metrics for organization&#39;s top 10 switches by energy usage over given time range. Default unit is joules.

    :param organization_id: 
    :type organization_id: str
    :param t0: The beginning of the timespan for the data.
    :type t0: str
    :param t1: The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
    :type t1: str
    :param timespan: The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 1 day.
    :type timespan: float

    """
    return web.Response(status=200)


async def get_organization_uplinks_statuses(request: web.Request, organization_id, per_page=None, starting_after=None, ending_before=None, network_ids=None, serials=None, iccids=None) -> web.Response:
    """List the uplink status of every Meraki MX, MG and Z series devices in the organization

    List the uplink status of every Meraki MX, MG and Z series devices in the organization

    :param organization_id: 
    :type organization_id: str
    :param per_page: The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
    :type per_page: int
    :param starting_after: A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type starting_after: str
    :param ending_before: A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type ending_before: str
    :param network_ids: A list of network IDs. The returned devices will be filtered to only include these networks.
    :type network_ids: List[str]
    :param serials: A list of serial numbers. The returned devices will be filtered to only include these serials.
    :type serials: List[str]
    :param iccids: A list of ICCIDs. The returned devices will be filtered to only include these ICCIDs.
    :type iccids: List[str]

    """
    return web.Response(status=200)


async def get_organization_webhooks_alert_types(request: web.Request, organization_id, product_type=None) -> web.Response:
    """Return a list of alert types to be used with managing webhook alerts

    Return a list of alert types to be used with managing webhook alerts

    :param organization_id: 
    :type organization_id: str
    :param product_type: Filter sample alerts to a specific product type
    :type product_type: str

    """
    return web.Response(status=200)


async def get_organization_webhooks_logs(request: web.Request, organization_id, t0=None, t1=None, timespan=None, per_page=None, starting_after=None, ending_before=None, url=None) -> web.Response:
    """Return the log of webhook POSTs sent

    Return the log of webhook POSTs sent

    :param organization_id: 
    :type organization_id: str
    :param t0: The beginning of the timespan for the data. The maximum lookback period is 90 days from today.
    :type t0: str
    :param t1: The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
    :type t1: str
    :param timespan: The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 1 day.
    :type timespan: float
    :param per_page: The number of entries per page returned. Acceptable range is 3 - 1000. Default is 50.
    :type per_page: int
    :param starting_after: A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type starting_after: str
    :param ending_before: A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type ending_before: str
    :param url: The URL the webhook was sent to
    :type url: str

    """
    return web.Response(status=200)


async def get_organizations(request: web.Request, ) -> web.Response:
    """List the organizations that the user has privileges on

    List the organizations that the user has privileges on


    """
    return web.Response(status=200)


async def move_organization_licenses(request: web.Request, organization_id, body) -> web.Response:
    """Move licenses to another organization

    Move licenses to another organization. This will also move any devices that the licenses are assigned to

    :param organization_id: 
    :type organization_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = MoveOrganizationLicensesRequest.from_dict(body)
    return web.Response(status=200)


async def move_organization_licenses_seats(request: web.Request, organization_id, body) -> web.Response:
    """Move SM seats to another organization

    Move SM seats to another organization

    :param organization_id: 
    :type organization_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = MoveOrganizationLicensesSeatsRequest.from_dict(body)
    return web.Response(status=200)


async def release_from_organization_inventory(request: web.Request, organization_id, body=None) -> web.Response:
    """Release a list of claimed devices from an organization.

    Release a list of claimed devices from an organization.

    :param organization_id: 
    :type organization_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = ReleaseFromOrganizationInventoryRequest.from_dict(body)
    return web.Response(status=200)


async def renew_organization_licenses_seats(request: web.Request, organization_id, body) -> web.Response:
    """Renew SM seats of a license

    Renew SM seats of a license. This will extend the license expiration date of managed SM devices covered by this license

    :param organization_id: 
    :type organization_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = RenewOrganizationLicensesSeatsRequest.from_dict(body)
    return web.Response(status=200)


async def update_organization(request: web.Request, organization_id, body=None) -> web.Response:
    """Update an organization

    Update an organization

    :param organization_id: 
    :type organization_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateOrganizationRequest.from_dict(body)
    return web.Response(status=200)


async def update_organization_action_batch(request: web.Request, organization_id, action_batch_id, body=None) -> web.Response:
    """Update an action batch

    Update an action batch

    :param organization_id: 
    :type organization_id: str
    :param action_batch_id: 
    :type action_batch_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateOrganizationActionBatchRequest.from_dict(body)
    return web.Response(status=200)


async def update_organization_adaptive_policy_acl(request: web.Request, organization_id, acl_id, body=None) -> web.Response:
    """Updates an adaptive policy ACL

    Updates an adaptive policy ACL

    :param organization_id: 
    :type organization_id: str
    :param acl_id: 
    :type acl_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateOrganizationAdaptivePolicyAclRequest.from_dict(body)
    return web.Response(status=200)


async def update_organization_adaptive_policy_group(request: web.Request, organization_id, id, body=None) -> web.Response:
    """Updates an adaptive policy group

    Updates an adaptive policy group. If updating \&quot;Infrastructure\&quot;, only the SGT is allowed. Cannot update \&quot;Unknown\&quot;.

    :param organization_id: 
    :type organization_id: str
    :param id: 
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateOrganizationAdaptivePolicyGroupRequest.from_dict(body)
    return web.Response(status=200)


async def update_organization_adaptive_policy_policy(request: web.Request, organization_id, id, body=None) -> web.Response:
    """Update an Adaptive Policy

    Update an Adaptive Policy

    :param organization_id: 
    :type organization_id: str
    :param id: 
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateOrganizationAdaptivePolicyPolicyRequest.from_dict(body)
    return web.Response(status=200)


async def update_organization_adaptive_policy_settings(request: web.Request, organization_id, body=None) -> web.Response:
    """Update global adaptive policy settings

    Update global adaptive policy settings

    :param organization_id: 
    :type organization_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateOrganizationAdaptivePolicySettingsRequest.from_dict(body)
    return web.Response(status=200)


async def update_organization_admin(request: web.Request, organization_id, admin_id, body=None) -> web.Response:
    """Update an administrator

    Update an administrator

    :param organization_id: 
    :type organization_id: str
    :param admin_id: 
    :type admin_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateOrganizationAdminRequest.from_dict(body)
    return web.Response(status=200)


async def update_organization_alerts_profile(request: web.Request, organization_id, alert_config_id, body=None) -> web.Response:
    """Update an organization-wide alert config

    Update an organization-wide alert config

    :param organization_id: 
    :type organization_id: str
    :param alert_config_id: 
    :type alert_config_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateOrganizationAlertsProfileRequest.from_dict(body)
    return web.Response(status=200)


async def update_organization_branding_policies_priorities(request: web.Request, organization_id, body=None) -> web.Response:
    """Update the priority ordering of an organization&#39;s branding policies.

    Update the priority ordering of an organization&#39;s branding policies.

    :param organization_id: 
    :type organization_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateOrganizationBrandingPoliciesPrioritiesRequest.from_dict(body)
    return web.Response(status=200)


async def update_organization_branding_policy(request: web.Request, organization_id, branding_policy_id, body=None) -> web.Response:
    """Update a branding policy

    Update a branding policy

    :param organization_id: 
    :type organization_id: str
    :param branding_policy_id: 
    :type branding_policy_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateOrganizationBrandingPolicyRequest.from_dict(body)
    return web.Response(status=200)


async def update_organization_config_template(request: web.Request, organization_id, config_template_id, body=None) -> web.Response:
    """Update a configuration template

    Update a configuration template

    :param organization_id: 
    :type organization_id: str
    :param config_template_id: 
    :type config_template_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateOrganizationConfigTemplateRequest.from_dict(body)
    return web.Response(status=200)


async def update_organization_early_access_features_opt_in(request: web.Request, organization_id, opt_in_id, body=None) -> web.Response:
    """Update an early access feature opt-in for an organization

    Update an early access feature opt-in for an organization

    :param organization_id: 
    :type organization_id: str
    :param opt_in_id: 
    :type opt_in_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateOrganizationEarlyAccessFeaturesOptInRequest.from_dict(body)
    return web.Response(status=200)


async def update_organization_license(request: web.Request, organization_id, license_id, body=None) -> web.Response:
    """Update a license

    Update a license

    :param organization_id: 
    :type organization_id: str
    :param license_id: 
    :type license_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateOrganizationLicenseRequest.from_dict(body)
    return web.Response(status=200)


async def update_organization_login_security(request: web.Request, organization_id, body=None) -> web.Response:
    """Update the login security settings for an organization

    Update the login security settings for an organization

    :param organization_id: 
    :type organization_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateOrganizationLoginSecurityRequest.from_dict(body)
    return web.Response(status=200)


async def update_organization_policy_object(request: web.Request, organization_id, policy_object_id, body=None) -> web.Response:
    """Updates a Policy Object.

    Updates a Policy Object.

    :param organization_id: 
    :type organization_id: str
    :param policy_object_id: 
    :type policy_object_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateOrganizationPolicyObjectRequest.from_dict(body)
    return web.Response(status=200)


async def update_organization_policy_objects_group(request: web.Request, organization_id, policy_object_group_id, body=None) -> web.Response:
    """Updates a Policy Object Group.

    Updates a Policy Object Group.

    :param organization_id: 
    :type organization_id: str
    :param policy_object_group_id: 
    :type policy_object_group_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateOrganizationPolicyObjectsGroupRequest.from_dict(body)
    return web.Response(status=200)


async def update_organization_saml(request: web.Request, organization_id, body=None) -> web.Response:
    """Updates the SAML SSO enabled settings for an organization.

    Updates the SAML SSO enabled settings for an organization.

    :param organization_id: 
    :type organization_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateOrganizationSamlRequest.from_dict(body)
    return web.Response(status=200)


async def update_organization_saml_idp(request: web.Request, organization_id, idp_id, body=None) -> web.Response:
    """Update a SAML IdP in your organization

    Update a SAML IdP in your organization

    :param organization_id: 
    :type organization_id: str
    :param idp_id: 
    :type idp_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateOrganizationSamlIdpRequest.from_dict(body)
    return web.Response(status=200)


async def update_organization_saml_role(request: web.Request, organization_id, saml_role_id, body=None) -> web.Response:
    """Update a SAML role

    Update a SAML role

    :param organization_id: 
    :type organization_id: str
    :param saml_role_id: 
    :type saml_role_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateOrganizationSamlRoleRequest.from_dict(body)
    return web.Response(status=200)


async def update_organization_snmp(request: web.Request, organization_id, body=None) -> web.Response:
    """Update the SNMP settings for an organization

    Update the SNMP settings for an organization

    :param organization_id: 
    :type organization_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateOrganizationSnmpRequest.from_dict(body)
    return web.Response(status=200)
