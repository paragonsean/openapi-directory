# CleverCloudApi.OrganisationsApi

All URIs are relative to *https://api.clever-cloud.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createNetworkGroupExternalPeer_0**](OrganisationsApi.md#createNetworkGroupExternalPeer_0) | **POST** /v4/networkgroups/organisations/{ownerId}/networkgroups/{networkGroupId}/external-peers | Add external peer
[**createNetworkGroupMember_0**](OrganisationsApi.md#createNetworkGroupMember_0) | **POST** /v4/networkgroups/organisations/{ownerId}/networkgroups/{networkGroupId}/members | Add member
[**createNetworkGroup_0**](OrganisationsApi.md#createNetworkGroup_0) | **POST** /v4/networkgroups/organisations/{ownerId}/networkgroups | Create Network Group
[**deleteNetworkGroupExternalPeer_0**](OrganisationsApi.md#deleteNetworkGroupExternalPeer_0) | **DELETE** /v4/networkgroups/organisations/{ownerId}/networkgroups/{networkGroupId}/external-peers/{peerId} | Remove external peer
[**deleteNetworkGroupMember_0**](OrganisationsApi.md#deleteNetworkGroupMember_0) | **DELETE** /v4/networkgroups/organisations/{ownerId}/networkgroups/{networkGroupId}/members/{memberId} | Remove member
[**deleteNetworkGroupPeer_0**](OrganisationsApi.md#deleteNetworkGroupPeer_0) | **DELETE** /v4/networkgroups/organisations/{ownerId}/networkgroups/{networkGroupId}/peers/{peerId} | Remove peer
[**deleteNetworkGroup_0**](OrganisationsApi.md#deleteNetworkGroup_0) | **DELETE** /v4/networkgroups/organisations/{ownerId}/networkgroups/{networkGroupId} | Delete Network Group
[**deleteOrganisationsIdAddonprovidersProviderIdFeaturesFeatureId_0**](OrganisationsApi.md#deleteOrganisationsIdAddonprovidersProviderIdFeaturesFeatureId_0) | **DELETE** /organisations/{id}/addonproviders/{providerId}/features/{featureId} | 
[**deleteOrganisationsIdAddonprovidersProviderIdPlansPlanIdFeaturesFeatureName_0**](OrganisationsApi.md#deleteOrganisationsIdAddonprovidersProviderIdPlansPlanIdFeaturesFeatureName_0) | **DELETE** /organisations/{id}/addonproviders/{providerId}/plans/{planId}/features/{featureName} | 
[**deleteOrganisationsIdAddonprovidersProviderIdPlansPlanId_0**](OrganisationsApi.md#deleteOrganisationsIdAddonprovidersProviderIdPlansPlanId_0) | **DELETE** /organisations/{id}/addonproviders/{providerId}/plans/{planId} | 
[**deleteOrganisationsIdAddonsAddonIdTagsTag_1**](OrganisationsApi.md#deleteOrganisationsIdAddonsAddonIdTagsTag_1) | **DELETE** /organisations/{id}/addons/{addonId}/tags/{tag} | 
[**deleteOrganisationsIdAddonsAddonId_1**](OrganisationsApi.md#deleteOrganisationsIdAddonsAddonId_1) | **DELETE** /organisations/{id}/addons/{addonId} | 
[**deleteOrganisationsIdApplicationsAppIdAddonsAddonId_2**](OrganisationsApi.md#deleteOrganisationsIdApplicationsAppIdAddonsAddonId_2) | **DELETE** /organisations/{id}/applications/{appId}/addons/{addonId} | 
[**deleteOrganisationsIdApplicationsAppIdDependenciesDependencyId_1**](OrganisationsApi.md#deleteOrganisationsIdApplicationsAppIdDependenciesDependencyId_1) | **DELETE** /organisations/{id}/applications/{appId}/dependencies/{dependencyId} | 
[**deleteOrganisationsIdApplicationsAppIdDeploymentsDeploymentIdInstances_1**](OrganisationsApi.md#deleteOrganisationsIdApplicationsAppIdDeploymentsDeploymentIdInstances_1) | **DELETE** /organisations/{id}/applications/{appId}/deployments/{deploymentId}/instances | 
[**deleteOrganisationsIdApplicationsAppIdEnvEnvName_1**](OrganisationsApi.md#deleteOrganisationsIdApplicationsAppIdEnvEnvName_1) | **DELETE** /organisations/{id}/applications/{appId}/env/{envName} | 
[**deleteOrganisationsIdApplicationsAppIdInstances_1**](OrganisationsApi.md#deleteOrganisationsIdApplicationsAppIdInstances_1) | **DELETE** /organisations/{id}/applications/{appId}/instances | 
[**deleteOrganisationsIdApplicationsAppIdTagsTag_1**](OrganisationsApi.md#deleteOrganisationsIdApplicationsAppIdTagsTag_1) | **DELETE** /organisations/{id}/applications/{appId}/tags/{tag} | 
[**deleteOrganisationsIdApplicationsAppIdVhostsDomain_1**](OrganisationsApi.md#deleteOrganisationsIdApplicationsAppIdVhostsDomain_1) | **DELETE** /organisations/{id}/applications/{appId}/vhosts/{domain} | 
[**deleteOrganisationsIdApplicationsAppIdVhostsFavourite_1**](OrganisationsApi.md#deleteOrganisationsIdApplicationsAppIdVhostsFavourite_1) | **DELETE** /organisations/{id}/applications/{appId}/vhosts/favourite | 
[**deleteOrganisationsIdApplicationsAppId_1**](OrganisationsApi.md#deleteOrganisationsIdApplicationsAppId_1) | **DELETE** /organisations/{id}/applications/{appId} | 
[**deleteOrganisationsIdConsumersKey_0**](OrganisationsApi.md#deleteOrganisationsIdConsumersKey_0) | **DELETE** /organisations/{id}/consumers/{key} | 
[**deleteOrganisationsIdMembersUserId_0**](OrganisationsApi.md#deleteOrganisationsIdMembersUserId_0) | **DELETE** /organisations/{id}/members/{userId} | 
[**deleteOrganisationsIdPaymentsBillingsBid_0**](OrganisationsApi.md#deleteOrganisationsIdPaymentsBillingsBid_0) | **DELETE** /organisations/{id}/payments/billings/{bid} | 
[**deleteOrganisationsIdPaymentsRecurring_0**](OrganisationsApi.md#deleteOrganisationsIdPaymentsRecurring_0) | **DELETE** /organisations/{id}/payments/recurring | 
[**deleteOrganisationsId_0**](OrganisationsApi.md#deleteOrganisationsId_0) | **DELETE** /organisations/{id} | 
[**getNetworkGroupMember_0**](OrganisationsApi.md#getNetworkGroupMember_0) | **GET** /v4/networkgroups/organisations/{ownerId}/networkgroups/{networkGroupId}/members/{memberId} | Get member
[**getNetworkGroupPeer_0**](OrganisationsApi.md#getNetworkGroupPeer_0) | **GET** /v4/networkgroups/organisations/{ownerId}/networkgroups/{networkGroupId}/peers/{peerId} | Get peer
[**getNetworkGroupStream_0**](OrganisationsApi.md#getNetworkGroupStream_0) | **GET** /v4/networkgroups/organisations/{ownerId}/networkgroups/{networkGroupId}/stream | Network Group SSE
[**getNetworkGroupWireGuardConfigurationStream_0**](OrganisationsApi.md#getNetworkGroupWireGuardConfigurationStream_0) | **GET** /v4/networkgroups/organisations/{ownerId}/networkgroups/{networkGroupId}/peers/{peerId}/wireguard/configuration/stream | Get WireGuard® configuration
[**getNetworkGroupWireGuardConfiguration_0**](OrganisationsApi.md#getNetworkGroupWireGuardConfiguration_0) | **GET** /v4/networkgroups/organisations/{ownerId}/networkgroups/{networkGroupId}/peers/{peerId}/wireguard/configuration | Get WireGuard® configuration
[**getNetworkGroup_0**](OrganisationsApi.md#getNetworkGroup_0) | **GET** /v4/networkgroups/organisations/{ownerId}/networkgroups/{networkGroupId} | Get Network Group
[**getOrganisationsIdAddonprovidersProviderIdFeatures_0**](OrganisationsApi.md#getOrganisationsIdAddonprovidersProviderIdFeatures_0) | **GET** /organisations/{id}/addonproviders/{providerId}/features | 
[**getOrganisationsIdAddonprovidersProviderIdPlansPlanId_0**](OrganisationsApi.md#getOrganisationsIdAddonprovidersProviderIdPlansPlanId_0) | **GET** /organisations/{id}/addonproviders/{providerId}/plans/{planId} | 
[**getOrganisationsIdAddonprovidersProviderIdPlans_0**](OrganisationsApi.md#getOrganisationsIdAddonprovidersProviderIdPlans_0) | **GET** /organisations/{id}/addonproviders/{providerId}/plans | 
[**getOrganisationsIdAddonprovidersProviderIdTags_0**](OrganisationsApi.md#getOrganisationsIdAddonprovidersProviderIdTags_0) | **GET** /organisations/{id}/addonproviders/{providerId}/tags | 
[**getOrganisationsIdAddonprovidersProviderId_0**](OrganisationsApi.md#getOrganisationsIdAddonprovidersProviderId_0) | **GET** /organisations/{id}/addonproviders/{providerId} | 
[**getOrganisationsIdAddonproviders_0**](OrganisationsApi.md#getOrganisationsIdAddonproviders_0) | **GET** /organisations/{id}/addonproviders | 
[**getOrganisationsIdAddonsAddonIdApplications_2**](OrganisationsApi.md#getOrganisationsIdAddonsAddonIdApplications_2) | **GET** /organisations/{id}/addons/{addonId}/applications | 
[**getOrganisationsIdAddonsAddonIdEnv_1**](OrganisationsApi.md#getOrganisationsIdAddonsAddonIdEnv_1) | **GET** /organisations/{id}/addons/{addonId}/env | 
[**getOrganisationsIdAddonsAddonIdSso_0**](OrganisationsApi.md#getOrganisationsIdAddonsAddonIdSso_0) | **GET** /organisations/{id}/addonproviders/{providerId}/sso | 
[**getOrganisationsIdAddonsAddonIdTags_1**](OrganisationsApi.md#getOrganisationsIdAddonsAddonIdTags_1) | **GET** /organisations/{id}/addons/{addonId}/tags | 
[**getOrganisationsIdAddonsAddonId_1**](OrganisationsApi.md#getOrganisationsIdAddonsAddonId_1) | **GET** /organisations/{id}/addons/{addonId} | 
[**getOrganisationsIdAddons_1**](OrganisationsApi.md#getOrganisationsIdAddons_1) | **GET** /organisations/{id}/addons | 
[**getOrganisationsIdApplicationsAppIdAddonsEnv_2**](OrganisationsApi.md#getOrganisationsIdApplicationsAppIdAddonsEnv_2) | **GET** /organisations/{id}/applications/{appId}/addons/env | 
[**getOrganisationsIdApplicationsAppIdAddons_2**](OrganisationsApi.md#getOrganisationsIdApplicationsAppIdAddons_2) | **GET** /organisations/{id}/applications/{appId}/addons | 
[**getOrganisationsIdApplicationsAppIdDependencies_1**](OrganisationsApi.md#getOrganisationsIdApplicationsAppIdDependencies_1) | **GET** /organisations/{id}/applications/{appId}/dependencies | 
[**getOrganisationsIdApplicationsAppIdDependents_1**](OrganisationsApi.md#getOrganisationsIdApplicationsAppIdDependents_1) | **GET** /organisations/{id}/applications/{appId}/dependents | 
[**getOrganisationsIdApplicationsAppIdDeployments_1**](OrganisationsApi.md#getOrganisationsIdApplicationsAppIdDeployments_1) | **GET** /organisations/{id}/applications/{appId}/deployments | 
[**getOrganisationsIdApplicationsAppIdEnv_1**](OrganisationsApi.md#getOrganisationsIdApplicationsAppIdEnv_1) | **GET** /organisations/{id}/applications/{appId}/env | 
[**getOrganisationsIdApplicationsAppIdInstances_1**](OrganisationsApi.md#getOrganisationsIdApplicationsAppIdInstances_1) | **GET** /organisations/{id}/applications/{appId}/instances | 
[**getOrganisationsIdApplicationsAppIdTags_1**](OrganisationsApi.md#getOrganisationsIdApplicationsAppIdTags_1) | **GET** /organisations/{id}/applications/{appId}/tags | 
[**getOrganisationsIdApplicationsAppIdVhostsFavourite_1**](OrganisationsApi.md#getOrganisationsIdApplicationsAppIdVhostsFavourite_1) | **GET** /organisations/{id}/applications/{appId}/vhosts/favourite | 
[**getOrganisationsIdApplicationsAppIdVhosts_1**](OrganisationsApi.md#getOrganisationsIdApplicationsAppIdVhosts_1) | **GET** /organisations/{id}/applications/{appId}/vhosts | 
[**getOrganisationsIdApplicationsAppId_1**](OrganisationsApi.md#getOrganisationsIdApplicationsAppId_1) | **GET** /organisations/{id}/applications/{appId} | 
[**getOrganisationsIdApplications_1**](OrganisationsApi.md#getOrganisationsIdApplications_1) | **GET** /organisations/{id}/applications | 
[**getOrganisationsIdConsumersKeySecret_0**](OrganisationsApi.md#getOrganisationsIdConsumersKeySecret_0) | **GET** /organisations/{id}/consumers/{key}/secret | 
[**getOrganisationsIdConsumersKey_0**](OrganisationsApi.md#getOrganisationsIdConsumersKey_0) | **GET** /organisations/{id}/consumers/{key} | 
[**getOrganisationsIdConsumers_0**](OrganisationsApi.md#getOrganisationsIdConsumers_0) | **GET** /organisations/{id}/consumers | 
[**getOrganisationsIdConsumptions_0**](OrganisationsApi.md#getOrganisationsIdConsumptions_0) | **GET** /organisations/{id}/consumptions | 
[**getOrganisationsIdCredits_0**](OrganisationsApi.md#getOrganisationsIdCredits_0) | **GET** /organisations/{id}/credits | 
[**getOrganisationsIdDeployments_0**](OrganisationsApi.md#getOrganisationsIdDeployments_0) | **GET** /organisations/{id}/deployments | 
[**getOrganisationsIdInstances_0**](OrganisationsApi.md#getOrganisationsIdInstances_0) | **GET** /organisations/{id}/instances | 
[**getOrganisationsIdMembers_0**](OrganisationsApi.md#getOrganisationsIdMembers_0) | **GET** /organisations/{id}/members | 
[**getOrganisationsIdPaymentInfo_0**](OrganisationsApi.md#getOrganisationsIdPaymentInfo_0) | **GET** /organisations/{id}/payment-info | 
[**getOrganisationsIdPaymentsBillingsBidPdf_0**](OrganisationsApi.md#getOrganisationsIdPaymentsBillingsBidPdf_0) | **GET** /organisations/{id}/payments/billings/{bid}.pdf | 
[**getOrganisationsIdPaymentsBillingsBid_0**](OrganisationsApi.md#getOrganisationsIdPaymentsBillingsBid_0) | **GET** /organisations/{id}/payments/billings/{bid} | 
[**getOrganisationsIdPaymentsBillings_0**](OrganisationsApi.md#getOrganisationsIdPaymentsBillings_0) | **GET** /organisations/{id}/payments/billings | 
[**getOrganisationsIdPaymentsFullPricePrice_0**](OrganisationsApi.md#getOrganisationsIdPaymentsFullPricePrice_0) | **GET** /organisations/{id}/payments/fullprice/{price} | 
[**getOrganisationsId_0**](OrganisationsApi.md#getOrganisationsId_0) | **GET** /organisations/{id} | 
[**getOrganisations_0**](OrganisationsApi.md#getOrganisations_0) | **GET** /organisations | 
[**listNetworkGroupMembers_0**](OrganisationsApi.md#listNetworkGroupMembers_0) | **GET** /v4/networkgroups/organisations/{ownerId}/networkgroups/{networkGroupId}/members | List members
[**listNetworkGroupPeers_0**](OrganisationsApi.md#listNetworkGroupPeers_0) | **GET** /v4/networkgroups/organisations/{ownerId}/networkgroups/{networkGroupId}/peers | List peers
[**listNetworkGroups_0**](OrganisationsApi.md#listNetworkGroups_0) | **GET** /v4/networkgroups/organisations/{ownerId}/networkgroups | List Network Groups
[**organisationsIdAddonprovidersProviderIdDelete_0**](OrganisationsApi.md#organisationsIdAddonprovidersProviderIdDelete_0) | **DELETE** /organisations/{id}/addonproviders/{providerId} | Remove an add-on provider
[**organisationsIdAddonsAddonIdInstancesGet_1**](OrganisationsApi.md#organisationsIdAddonsAddonIdInstancesGet_1) | **GET** /organisations/{id}/addons/{addonId}/instances | List instances for this add-on.
[**organisationsIdAddonsAddonIdInstancesInstanceIdGet_1**](OrganisationsApi.md#organisationsIdAddonsAddonIdInstancesInstanceIdGet_1) | **GET** /organisations/{id}/addons/{addonId}/instances/{instanceId} | Get a specific instance for {addonId}
[**organisationsIdAddonsAddonIdMigrationsGet_1**](OrganisationsApi.md#organisationsIdAddonsAddonIdMigrationsGet_1) | **GET** /organisations/{id}/addons/{addonId}/migrations | Get past migrations from add-on.
[**organisationsIdAddonsAddonIdMigrationsMigrationIdGet_1**](OrganisationsApi.md#organisationsIdAddonsAddonIdMigrationsMigrationIdGet_1) | **GET** /organisations/{id}/addons/{addonId}/migrations/{migrationId} | Get a given migration
[**organisationsIdAddonsAddonIdMigrationsPost_1**](OrganisationsApi.md#organisationsIdAddonsAddonIdMigrationsPost_1) | **POST** /organisations/{id}/addons/{addonId}/migrations | Start a new add-on migration
[**organisationsIdAddonsAddonIdSsoGet_1**](OrganisationsApi.md#organisationsIdAddonsAddonIdSsoGet_1) | **GET** /organisations/{id}/addons/{addonId}/sso | 
[**organisationsIdAddonsPreordersPost_1**](OrganisationsApi.md#organisationsIdAddonsPreordersPost_1) | **POST** /organisations/{id}/addons/preorders | 
[**organisationsIdApplicationsAppIdBranchPut_1**](OrganisationsApi.md#organisationsIdApplicationsAppIdBranchPut_1) | **PUT** /organisations/{id}/applications/{appId}/branch | 
[**organisationsIdApplicationsAppIdBranchesGet_1**](OrganisationsApi.md#organisationsIdApplicationsAppIdBranchesGet_1) | **GET** /organisations/{id}/applications/{appId}/branches | 
[**organisationsIdApplicationsAppIdBuildflavorPut_1**](OrganisationsApi.md#organisationsIdApplicationsAppIdBuildflavorPut_1) | **PUT** /organisations/{id}/applications/{appId}/buildflavor | 
[**organisationsIdApplicationsAppIdDependenciesEnvGet_1**](OrganisationsApi.md#organisationsIdApplicationsAppIdDependenciesEnvGet_1) | **GET** /organisations/{id}/applications/{appId}/dependencies/env | 
[**organisationsIdApplicationsAppIdDeploymentsDeploymentIdGet_1**](OrganisationsApi.md#organisationsIdApplicationsAppIdDeploymentsDeploymentIdGet_1) | **GET** /organisations/{id}/applications/{appId}/deployments/{deploymentId} | 
[**organisationsIdApplicationsAppIdExposedEnvGet_1**](OrganisationsApi.md#organisationsIdApplicationsAppIdExposedEnvGet_1) | **GET** /organisations/{id}/applications/{appId}/exposed_env | 
[**organisationsIdApplicationsAppIdExposedEnvPut_1**](OrganisationsApi.md#organisationsIdApplicationsAppIdExposedEnvPut_1) | **PUT** /organisations/{id}/applications/{appId}/exposed_env | 
[**organisationsIdApplicationsAppIdInstancesInstanceIdGet_1**](OrganisationsApi.md#organisationsIdApplicationsAppIdInstancesInstanceIdGet_1) | **GET** /organisations/{id}/applications/{appId}/instances/{instanceId} | 
[**organisationsIdPaymentsBillingsUnpaidGet_0**](OrganisationsApi.md#organisationsIdPaymentsBillingsUnpaidGet_0) | **GET** /organisations/{id}/payments/billings/unpaid | 
[**organisationsIdPaymentsMethodsDefaultGet_0**](OrganisationsApi.md#organisationsIdPaymentsMethodsDefaultGet_0) | **GET** /organisations/{id}/payments/methods/default | 
[**organisationsIdPaymentsMethodsDefaultPut_0**](OrganisationsApi.md#organisationsIdPaymentsMethodsDefaultPut_0) | **PUT** /organisations/{id}/payments/methods/default | 
[**organisationsIdPaymentsMethodsGet_0**](OrganisationsApi.md#organisationsIdPaymentsMethodsGet_0) | **GET** /organisations/{id}/payments/methods | 
[**organisationsIdPaymentsMethodsMIdDelete_0**](OrganisationsApi.md#organisationsIdPaymentsMethodsMIdDelete_0) | **DELETE** /organisations/{id}/payments/methods/{mId} | 
[**organisationsIdPaymentsMethodsPost_0**](OrganisationsApi.md#organisationsIdPaymentsMethodsPost_0) | **POST** /organisations/{id}/payments/methods | 
[**organisationsIdPaymentsMonthlyinvoiceGet_0**](OrganisationsApi.md#organisationsIdPaymentsMonthlyinvoiceGet_0) | **GET** /organisations/{id}/payments/monthlyinvoice | 
[**organisationsIdPaymentsMonthlyinvoiceMaxcreditPut_0**](OrganisationsApi.md#organisationsIdPaymentsMonthlyinvoiceMaxcreditPut_0) | **PUT** /organisations/{id}/payments/monthlyinvoice/maxcredit | 
[**organisationsIdPaymentsRecurringGet_0**](OrganisationsApi.md#organisationsIdPaymentsRecurringGet_0) | **GET** /organisations/{id}/payments/recurring | 
[**postOrganisationsIdAddonprovidersProviderIdFeatures_0**](OrganisationsApi.md#postOrganisationsIdAddonprovidersProviderIdFeatures_0) | **POST** /organisations/{id}/addonproviders/{providerId}/features | 
[**postOrganisationsIdAddonprovidersProviderIdPlans_0**](OrganisationsApi.md#postOrganisationsIdAddonprovidersProviderIdPlans_0) | **POST** /organisations/{id}/addonproviders/{providerId}/plans | 
[**postOrganisationsIdAddonprovidersProviderIdTesters_0**](OrganisationsApi.md#postOrganisationsIdAddonprovidersProviderIdTesters_0) | **POST** /organisations/{id}/addonproviders/{providerId}/testers | 
[**postOrganisationsIdAddonproviders_0**](OrganisationsApi.md#postOrganisationsIdAddonproviders_0) | **POST** /organisations/{id}/addonproviders | 
[**postOrganisationsIdAddons_1**](OrganisationsApi.md#postOrganisationsIdAddons_1) | **POST** /organisations/{id}/addons | 
[**postOrganisationsIdApplicationsAppIdAddons_2**](OrganisationsApi.md#postOrganisationsIdApplicationsAppIdAddons_2) | **POST** /organisations/{id}/applications/{appId}/addons | 
[**postOrganisationsIdApplicationsAppIdInstances_1**](OrganisationsApi.md#postOrganisationsIdApplicationsAppIdInstances_1) | **POST** /organisations/{id}/applications/{appId}/instances | 
[**postOrganisationsIdApplications_1**](OrganisationsApi.md#postOrganisationsIdApplications_1) | **POST** /organisations/{id}/applications | 
[**postOrganisationsIdConsumers_0**](OrganisationsApi.md#postOrganisationsIdConsumers_0) | **POST** /organisations/{id}/consumers | 
[**postOrganisationsIdMembers_0**](OrganisationsApi.md#postOrganisationsIdMembers_0) | **POST** /organisations/{id}/members | 
[**postOrganisationsIdPaymentsBillings_0**](OrganisationsApi.md#postOrganisationsIdPaymentsBillings_0) | **POST** /organisations/{id}/payments/billings | 
[**postOrganisations_0**](OrganisationsApi.md#postOrganisations_0) | **POST** /organisations | 
[**putOrganisationsIdAddonprovidersProviderIdPlansPlanIdFeaturesFeatureName_0**](OrganisationsApi.md#putOrganisationsIdAddonprovidersProviderIdPlansPlanIdFeaturesFeatureName_0) | **PUT** /organisations/{id}/addonproviders/{providerId}/plans/{planId}/features/{featureName} | 
[**putOrganisationsIdAddonprovidersProviderIdPlansPlanId_0**](OrganisationsApi.md#putOrganisationsIdAddonprovidersProviderIdPlansPlanId_0) | **PUT** /organisations/{id}/addonproviders/{providerId}/plans/{planId} | 
[**putOrganisationsIdAddonprovidersProviderId_0**](OrganisationsApi.md#putOrganisationsIdAddonprovidersProviderId_0) | **PUT** /organisations/{id}/addonproviders/{providerId} | 
[**putOrganisationsIdAddonsAddonIdTagsTag_1**](OrganisationsApi.md#putOrganisationsIdAddonsAddonIdTagsTag_1) | **PUT** /organisations/{id}/addons/{addonId}/tags/{tag} | 
[**putOrganisationsIdAddonsAddonId_1**](OrganisationsApi.md#putOrganisationsIdAddonsAddonId_1) | **PUT** /organisations/{id}/addons/{addonId} | 
[**putOrganisationsIdApplicationsAppIdDependenciesDependencyId_1**](OrganisationsApi.md#putOrganisationsIdApplicationsAppIdDependenciesDependencyId_1) | **PUT** /organisations/{id}/applications/{appId}/dependencies/{dependencyId} | 
[**putOrganisationsIdApplicationsAppIdEnvEnvName_1**](OrganisationsApi.md#putOrganisationsIdApplicationsAppIdEnvEnvName_1) | **PUT** /organisations/{id}/applications/{appId}/env/{envName} | 
[**putOrganisationsIdApplicationsAppIdEnv_1**](OrganisationsApi.md#putOrganisationsIdApplicationsAppIdEnv_1) | **PUT** /organisations/{id}/applications/{appId}/env | 
[**putOrganisationsIdApplicationsAppIdTagsTag_1**](OrganisationsApi.md#putOrganisationsIdApplicationsAppIdTagsTag_1) | **PUT** /organisations/{id}/applications/{appId}/tags/{tag} | 
[**putOrganisationsIdApplicationsAppIdVhostsDomain_1**](OrganisationsApi.md#putOrganisationsIdApplicationsAppIdVhostsDomain_1) | **PUT** /organisations/{id}/applications/{appId}/vhosts/{domain} | 
[**putOrganisationsIdApplicationsAppIdVhostsFavourite_1**](OrganisationsApi.md#putOrganisationsIdApplicationsAppIdVhostsFavourite_1) | **PUT** /organisations/{id}/applications/{appId}/vhosts/favourite | 
[**putOrganisationsIdApplicationsAppId_1**](OrganisationsApi.md#putOrganisationsIdApplicationsAppId_1) | **PUT** /organisations/{id}/applications/{appId} | 
[**putOrganisationsIdAvatar_0**](OrganisationsApi.md#putOrganisationsIdAvatar_0) | **PUT** /organisations/{id}/avatar | 
[**putOrganisationsIdConsumersKey_0**](OrganisationsApi.md#putOrganisationsIdConsumersKey_0) | **PUT** /organisations/{id}/consumers/{key} | 
[**putOrganisationsIdMembersUserId_0**](OrganisationsApi.md#putOrganisationsIdMembersUserId_0) | **PUT** /organisations/{id}/members/{userId} | 
[**putOrganisationsIdPaymentsBillingsBid_0**](OrganisationsApi.md#putOrganisationsIdPaymentsBillingsBid_0) | **PUT** /organisations/{id}/payments/billings/{bid} | 
[**putOrganisationsId_0**](OrganisationsApi.md#putOrganisationsId_0) | **PUT** /organisations/{id} | 



## createNetworkGroupExternalPeer_0

> Object createNetworkGroupExternalPeer_0(ownerId, networkGroupId, opts)

Add external peer

Adds an external peer to a Network Group.

### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.OrganisationsApi();
let ownerId = "ownerId_example"; // String | Automatically added
let networkGroupId = "networkGroupId_example"; // String | Automatically added
let opts = {
  'body': null // Object | 
};
apiInstance.createNetworkGroupExternalPeer_0(ownerId, networkGroupId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ownerId** | **String**| Automatically added | 
 **networkGroupId** | **String**| Automatically added | 
 **body** | **Object**|  | [optional] 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json, text/plain; charset=UTF-8


## createNetworkGroupMember_0

> createNetworkGroupMember_0(ownerId, networkGroupId, opts)

Add member

Adds a member to a Network Group.

### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.OrganisationsApi();
let ownerId = "ownerId_example"; // String | Automatically added
let networkGroupId = "networkGroupId_example"; // String | Automatically added
let opts = {
  'schema2': new CleverCloudApi.Schema2() // Schema2 | 
};
apiInstance.createNetworkGroupMember_0(ownerId, networkGroupId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ownerId** | **String**| Automatically added | 
 **networkGroupId** | **String**| Automatically added | 
 **schema2** | [**Schema2**](Schema2.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## createNetworkGroup_0

> Object createNetworkGroup_0(ownerId, opts)

Create Network Group

Creates a Network Group.

### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.OrganisationsApi();
let ownerId = "ownerId_example"; // String | Automatically added
let opts = {
  'body': null // Object | 
};
apiInstance.createNetworkGroup_0(ownerId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ownerId** | **String**| Automatically added | 
 **body** | **Object**|  | [optional] 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json, text/plain; charset=UTF-8


## deleteNetworkGroupExternalPeer_0

> deleteNetworkGroupExternalPeer_0(ownerId, networkGroupId, peerId, opts)

Remove external peer

Removes an external peer from a Network Group.

### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.OrganisationsApi();
let ownerId = "ownerId_example"; // String | Automatically added
let networkGroupId = "networkGroupId_example"; // String | Automatically added
let peerId = "peerId_example"; // String | Automatically added
let opts = {
  'body': null // Object | 
};
apiInstance.deleteNetworkGroupExternalPeer_0(ownerId, networkGroupId, peerId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ownerId** | **String**| Automatically added | 
 **networkGroupId** | **String**| Automatically added | 
 **peerId** | **String**| Automatically added | 
 **body** | **Object**|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteNetworkGroupMember_0

> deleteNetworkGroupMember_0(ownerId, networkGroupId, memberId, opts)

Remove member

Removes a member from a Network Group.

### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.OrganisationsApi();
let ownerId = "ownerId_example"; // String | Automatically added
let networkGroupId = "networkGroupId_example"; // String | Automatically added
let memberId = "memberId_example"; // String | Automatically added
let opts = {
  'body': null // Object | 
};
apiInstance.deleteNetworkGroupMember_0(ownerId, networkGroupId, memberId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ownerId** | **String**| Automatically added | 
 **networkGroupId** | **String**| Automatically added | 
 **memberId** | **String**| Automatically added | 
 **body** | **Object**|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteNetworkGroupPeer_0

> deleteNetworkGroupPeer_0(ownerId, networkGroupId, peerId, opts)

Remove peer

Removes a peer from a Network Group.

### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.OrganisationsApi();
let ownerId = "ownerId_example"; // String | Automatically added
let networkGroupId = "networkGroupId_example"; // String | Automatically added
let peerId = "peerId_example"; // String | Automatically added
let opts = {
  'body': null // Object | 
};
apiInstance.deleteNetworkGroupPeer_0(ownerId, networkGroupId, peerId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ownerId** | **String**| Automatically added | 
 **networkGroupId** | **String**| Automatically added | 
 **peerId** | **String**| Automatically added | 
 **body** | **Object**|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteNetworkGroup_0

> deleteNetworkGroup_0(ownerId, networkGroupId, opts)

Delete Network Group

Deletes a Network Group.

### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.OrganisationsApi();
let ownerId = "ownerId_example"; // String | Automatically added
let networkGroupId = "networkGroupId_example"; // String | Automatically added
let opts = {
  'body': null // Object | 
};
apiInstance.deleteNetworkGroup_0(ownerId, networkGroupId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ownerId** | **String**| Automatically added | 
 **networkGroupId** | **String**| Automatically added | 
 **body** | **Object**|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteOrganisationsIdAddonprovidersProviderIdFeaturesFeatureId_0

> deleteOrganisationsIdAddonprovidersProviderIdFeaturesFeatureId_0(id, featureId, providerId)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.OrganisationsApi();
let id = "id_example"; // String | 
let featureId = "featureId_example"; // String | 
let providerId = "providerId_example"; // String | 
apiInstance.deleteOrganisationsIdAddonprovidersProviderIdFeaturesFeatureId_0(id, featureId, providerId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**|  | 
 **featureId** | **String**|  | 
 **providerId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteOrganisationsIdAddonprovidersProviderIdPlansPlanIdFeaturesFeatureName_0

> deleteOrganisationsIdAddonprovidersProviderIdPlansPlanIdFeaturesFeatureName_0(id, featureName, providerId, planId)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.OrganisationsApi();
let id = "id_example"; // String | 
let featureName = "featureName_example"; // String | 
let providerId = "providerId_example"; // String | 
let planId = "planId_example"; // String | 
apiInstance.deleteOrganisationsIdAddonprovidersProviderIdPlansPlanIdFeaturesFeatureName_0(id, featureName, providerId, planId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**|  | 
 **featureName** | **String**|  | 
 **providerId** | **String**|  | 
 **planId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteOrganisationsIdAddonprovidersProviderIdPlansPlanId_0

> deleteOrganisationsIdAddonprovidersProviderIdPlansPlanId_0(id, providerId, planId)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.OrganisationsApi();
let id = "id_example"; // String | 
let providerId = "providerId_example"; // String | 
let planId = "planId_example"; // String | 
apiInstance.deleteOrganisationsIdAddonprovidersProviderIdPlansPlanId_0(id, providerId, planId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**|  | 
 **providerId** | **String**|  | 
 **planId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteOrganisationsIdAddonsAddonIdTagsTag_1

> deleteOrganisationsIdAddonsAddonIdTagsTag_1(id, tag, addonId)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.OrganisationsApi();
let id = "id_example"; // String | 
let tag = "tag_example"; // String | 
let addonId = "addonId_example"; // String | 
apiInstance.deleteOrganisationsIdAddonsAddonIdTagsTag_1(id, tag, addonId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**|  | 
 **tag** | **String**|  | 
 **addonId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteOrganisationsIdAddonsAddonId_1

> deleteOrganisationsIdAddonsAddonId_1(id, addonId)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.OrganisationsApi();
let id = "id_example"; // String | 
let addonId = "addonId_example"; // String | 
apiInstance.deleteOrganisationsIdAddonsAddonId_1(id, addonId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**|  | 
 **addonId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteOrganisationsIdApplicationsAppIdAddonsAddonId_2

> deleteOrganisationsIdApplicationsAppIdAddonsAddonId_2(id, appId, addonId)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.OrganisationsApi();
let id = "id_example"; // String | 
let appId = "appId_example"; // String | 
let addonId = "addonId_example"; // String | 
apiInstance.deleteOrganisationsIdApplicationsAppIdAddonsAddonId_2(id, appId, addonId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**|  | 
 **appId** | **String**|  | 
 **addonId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteOrganisationsIdApplicationsAppIdDependenciesDependencyId_1

> deleteOrganisationsIdApplicationsAppIdDependenciesDependencyId_1(dependencyId, appId, id)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.OrganisationsApi();
let dependencyId = "dependencyId_example"; // String | 
let appId = "appId_example"; // String | 
let id = "id_example"; // String | 
apiInstance.deleteOrganisationsIdApplicationsAppIdDependenciesDependencyId_1(dependencyId, appId, id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dependencyId** | **String**|  | 
 **appId** | **String**|  | 
 **id** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteOrganisationsIdApplicationsAppIdDeploymentsDeploymentIdInstances_1

> deleteOrganisationsIdApplicationsAppIdDeploymentsDeploymentIdInstances_1(id, appId, deploymentId)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.OrganisationsApi();
let id = "id_example"; // String | 
let appId = "appId_example"; // String | 
let deploymentId = "deploymentId_example"; // String | 
apiInstance.deleteOrganisationsIdApplicationsAppIdDeploymentsDeploymentIdInstances_1(id, appId, deploymentId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**|  | 
 **appId** | **String**|  | 
 **deploymentId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteOrganisationsIdApplicationsAppIdEnvEnvName_1

> deleteOrganisationsIdApplicationsAppIdEnvEnvName_1(id, appId, envName)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.OrganisationsApi();
let id = "id_example"; // String | 
let appId = "appId_example"; // String | 
let envName = "envName_example"; // String | 
apiInstance.deleteOrganisationsIdApplicationsAppIdEnvEnvName_1(id, appId, envName, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**|  | 
 **appId** | **String**|  | 
 **envName** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteOrganisationsIdApplicationsAppIdInstances_1

> deleteOrganisationsIdApplicationsAppIdInstances_1(id, appId)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.OrganisationsApi();
let id = "id_example"; // String | 
let appId = "appId_example"; // String | 
apiInstance.deleteOrganisationsIdApplicationsAppIdInstances_1(id, appId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**|  | 
 **appId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteOrganisationsIdApplicationsAppIdTagsTag_1

> deleteOrganisationsIdApplicationsAppIdTagsTag_1(id, appId, tag)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.OrganisationsApi();
let id = "id_example"; // String | 
let appId = "appId_example"; // String | 
let tag = "tag_example"; // String | 
apiInstance.deleteOrganisationsIdApplicationsAppIdTagsTag_1(id, appId, tag, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**|  | 
 **appId** | **String**|  | 
 **tag** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteOrganisationsIdApplicationsAppIdVhostsDomain_1

> deleteOrganisationsIdApplicationsAppIdVhostsDomain_1(id, appId, domain)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.OrganisationsApi();
let id = "id_example"; // String | 
let appId = "appId_example"; // String | 
let domain = "domain_example"; // String | 
apiInstance.deleteOrganisationsIdApplicationsAppIdVhostsDomain_1(id, appId, domain, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**|  | 
 **appId** | **String**|  | 
 **domain** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteOrganisationsIdApplicationsAppIdVhostsFavourite_1

> deleteOrganisationsIdApplicationsAppIdVhostsFavourite_1(id, appId)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.OrganisationsApi();
let id = "id_example"; // String | 
let appId = "appId_example"; // String | 
apiInstance.deleteOrganisationsIdApplicationsAppIdVhostsFavourite_1(id, appId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**|  | 
 **appId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteOrganisationsIdApplicationsAppId_1

> deleteOrganisationsIdApplicationsAppId_1(id, appId)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.OrganisationsApi();
let id = "id_example"; // String | 
let appId = "appId_example"; // String | 
apiInstance.deleteOrganisationsIdApplicationsAppId_1(id, appId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**|  | 
 **appId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteOrganisationsIdConsumersKey_0

> deleteOrganisationsIdConsumersKey_0(id, key)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.OrganisationsApi();
let id = "id_example"; // String | 
let key = "key_example"; // String | 
apiInstance.deleteOrganisationsIdConsumersKey_0(id, key, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**|  | 
 **key** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteOrganisationsIdMembersUserId_0

> deleteOrganisationsIdMembersUserId_0(id, userId)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.OrganisationsApi();
let id = "id_example"; // String | 
let userId = "userId_example"; // String | 
apiInstance.deleteOrganisationsIdMembersUserId_0(id, userId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**|  | 
 **userId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteOrganisationsIdPaymentsBillingsBid_0

> deleteOrganisationsIdPaymentsBillingsBid_0(id, bid)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.OrganisationsApi();
let id = "id_example"; // String | 
let bid = "bid_example"; // String | 
apiInstance.deleteOrganisationsIdPaymentsBillingsBid_0(id, bid, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**|  | 
 **bid** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteOrganisationsIdPaymentsRecurring_0

> deleteOrganisationsIdPaymentsRecurring_0(id)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.OrganisationsApi();
let id = "id_example"; // String | 
apiInstance.deleteOrganisationsIdPaymentsRecurring_0(id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteOrganisationsId_0

> deleteOrganisationsId_0(id)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.OrganisationsApi();
let id = "id_example"; // String | 
apiInstance.deleteOrganisationsId_0(id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getNetworkGroupMember_0

> Schema1 getNetworkGroupMember_0(ownerId, networkGroupId, memberId, opts)

Get member

Gets details of a Network Group member.

### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.OrganisationsApi();
let ownerId = "ownerId_example"; // String | Automatically added
let networkGroupId = "networkGroupId_example"; // String | Automatically added
let memberId = "memberId_example"; // String | Automatically added
let opts = {
  'body': null // Object | 
};
apiInstance.getNetworkGroupMember_0(ownerId, networkGroupId, memberId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ownerId** | **String**| Automatically added | 
 **networkGroupId** | **String**| Automatically added | 
 **memberId** | **String**| Automatically added | 
 **body** | **Object**|  | [optional] 

### Return type

[**Schema1**](Schema1.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkGroupPeer_0

> Object getNetworkGroupPeer_0(ownerId, networkGroupId, peerId, opts)

Get peer

Gets details of a Network Group peer.

### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.OrganisationsApi();
let ownerId = "ownerId_example"; // String | Automatically added
let networkGroupId = "networkGroupId_example"; // String | Automatically added
let peerId = "peerId_example"; // String | Automatically added
let opts = {
  'body': null // Object | 
};
apiInstance.getNetworkGroupPeer_0(ownerId, networkGroupId, peerId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ownerId** | **String**| Automatically added | 
 **networkGroupId** | **String**| Automatically added | 
 **peerId** | **String**| Automatically added | 
 **body** | **Object**|  | [optional] 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkGroupStream_0

> Object getNetworkGroupStream_0(ownerId, networkGroupId, opts)

Network Group SSE

Retrieves the current Network Group details as a Server Sent Event.

### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.OrganisationsApi();
let ownerId = "ownerId_example"; // String | Automatically added
let networkGroupId = "networkGroupId_example"; // String | Automatically added
let opts = {
  'body': null // Object | 
};
apiInstance.getNetworkGroupStream_0(ownerId, networkGroupId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ownerId** | **String**| Automatically added | 
 **networkGroupId** | **String**| Automatically added | 
 **body** | **Object**|  | [optional] 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/event-stream


## getNetworkGroupWireGuardConfigurationStream_0

> Object getNetworkGroupWireGuardConfigurationStream_0(ownerId, networkGroupId, peerId, opts)

Get WireGuard® configuration

Gets the current WireGuard® tunnel configuration file for a Network Group peer as a Server Sent Event.

### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.OrganisationsApi();
let ownerId = "ownerId_example"; // String | Automatically added
let networkGroupId = "networkGroupId_example"; // String | Automatically added
let peerId = "peerId_example"; // String | Automatically added
let opts = {
  'body': null // Object | 
};
apiInstance.getNetworkGroupWireGuardConfigurationStream_0(ownerId, networkGroupId, peerId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ownerId** | **String**| Automatically added | 
 **networkGroupId** | **String**| Automatically added | 
 **peerId** | **String**| Automatically added | 
 **body** | **Object**|  | [optional] 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/event-stream


## getNetworkGroupWireGuardConfiguration_0

> Object getNetworkGroupWireGuardConfiguration_0(ownerId, networkGroupId, peerId, opts)

Get WireGuard® configuration

Gets the current WireGuard® tunnel configuration file for a Network Group peer.

### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.OrganisationsApi();
let ownerId = "ownerId_example"; // String | Automatically added
let networkGroupId = "networkGroupId_example"; // String | Automatically added
let peerId = "peerId_example"; // String | Automatically added
let opts = {
  'body': null // Object | 
};
apiInstance.getNetworkGroupWireGuardConfiguration_0(ownerId, networkGroupId, peerId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ownerId** | **String**| Automatically added | 
 **networkGroupId** | **String**| Automatically added | 
 **peerId** | **String**| Automatically added | 
 **body** | **Object**|  | [optional] 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkGroup_0

> Object getNetworkGroup_0(ownerId, networkGroupId, opts)

Get Network Group

Gets details of a Network Group.

### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.OrganisationsApi();
let ownerId = "ownerId_example"; // String | Automatically added
let networkGroupId = "networkGroupId_example"; // String | Automatically added
let opts = {
  'body': null // Object | 
};
apiInstance.getNetworkGroup_0(ownerId, networkGroupId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ownerId** | **String**| Automatically added | 
 **networkGroupId** | **String**| Automatically added | 
 **body** | **Object**|  | [optional] 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getOrganisationsIdAddonprovidersProviderIdFeatures_0

> [Feature] getOrganisationsIdAddonprovidersProviderIdFeatures_0(id, providerId)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.OrganisationsApi();
let id = "id_example"; // String | 
let providerId = "providerId_example"; // String | 
apiInstance.getOrganisationsIdAddonprovidersProviderIdFeatures_0(id, providerId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**|  | 
 **providerId** | **String**|  | 

### Return type

[**[Feature]**](Feature.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getOrganisationsIdAddonprovidersProviderIdPlansPlanId_0

> Plan getOrganisationsIdAddonprovidersProviderIdPlansPlanId_0(id, providerId, planId)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.OrganisationsApi();
let id = "id_example"; // String | 
let providerId = "providerId_example"; // String | 
let planId = "planId_example"; // String | 
apiInstance.getOrganisationsIdAddonprovidersProviderIdPlansPlanId_0(id, providerId, planId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**|  | 
 **providerId** | **String**|  | 
 **planId** | **String**|  | 

### Return type

[**Plan**](Plan.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getOrganisationsIdAddonprovidersProviderIdPlans_0

> [Plan] getOrganisationsIdAddonprovidersProviderIdPlans_0(id, providerId)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.OrganisationsApi();
let id = "id_example"; // String | 
let providerId = "providerId_example"; // String | 
apiInstance.getOrganisationsIdAddonprovidersProviderIdPlans_0(id, providerId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**|  | 
 **providerId** | **String**|  | 

### Return type

[**[Plan]**](Plan.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getOrganisationsIdAddonprovidersProviderIdTags_0

> [String] getOrganisationsIdAddonprovidersProviderIdTags_0(id, providerId)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.OrganisationsApi();
let id = "id_example"; // String | 
let providerId = "providerId_example"; // String | 
apiInstance.getOrganisationsIdAddonprovidersProviderIdTags_0(id, providerId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**|  | 
 **providerId** | **String**|  | 

### Return type

**[String]**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## getOrganisationsIdAddonprovidersProviderId_0

> Provider getOrganisationsIdAddonprovidersProviderId_0(id, providerId)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.OrganisationsApi();
let id = "id_example"; // String | 
let providerId = "providerId_example"; // String | 
apiInstance.getOrganisationsIdAddonprovidersProviderId_0(id, providerId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**|  | 
 **providerId** | **String**|  | 

### Return type

[**Provider**](Provider.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getOrganisationsIdAddonproviders_0

> [Provider] getOrganisationsIdAddonproviders_0(id)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.OrganisationsApi();
let id = "id_example"; // String | 
apiInstance.getOrganisationsIdAddonproviders_0(id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**|  | 

### Return type

[**[Provider]**](Provider.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getOrganisationsIdAddonsAddonIdApplications_2

> [Application] getOrganisationsIdAddonsAddonIdApplications_2(id, addonId)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.OrganisationsApi();
let id = "id_example"; // String | 
let addonId = "addonId_example"; // String | 
apiInstance.getOrganisationsIdAddonsAddonIdApplications_2(id, addonId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**|  | 
 **addonId** | **String**|  | 

### Return type

[**[Application]**](Application.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getOrganisationsIdAddonsAddonIdEnv_1

> [ListEnv] getOrganisationsIdAddonsAddonIdEnv_1(id, addonId)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.OrganisationsApi();
let id = "id_example"; // String | 
let addonId = "addonId_example"; // String | 
apiInstance.getOrganisationsIdAddonsAddonIdEnv_1(id, addonId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**|  | 
 **addonId** | **String**|  | 

### Return type

[**[ListEnv]**](ListEnv.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getOrganisationsIdAddonsAddonIdSso_0

> AddonProviderSso getOrganisationsIdAddonsAddonIdSso_0(providerId, id)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.OrganisationsApi();
let providerId = "providerId_example"; // String | 
let id = "id_example"; // String | 
apiInstance.getOrganisationsIdAddonsAddonIdSso_0(providerId, id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **providerId** | **String**|  | 
 **id** | **String**|  | 

### Return type

[**AddonProviderSso**](AddonProviderSso.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getOrganisationsIdAddonsAddonIdTags_1

> [String] getOrganisationsIdAddonsAddonIdTags_1(id, addonId)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.OrganisationsApi();
let id = "id_example"; // String | 
let addonId = "addonId_example"; // String | 
apiInstance.getOrganisationsIdAddonsAddonIdTags_1(id, addonId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**|  | 
 **addonId** | **String**|  | 

### Return type

**[String]**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## getOrganisationsIdAddonsAddonId_1

> Addon getOrganisationsIdAddonsAddonId_1(id, addonId)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.OrganisationsApi();
let id = "id_example"; // String | 
let addonId = "addonId_example"; // String | 
apiInstance.getOrganisationsIdAddonsAddonId_1(id, addonId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**|  | 
 **addonId** | **String**|  | 

### Return type

[**Addon**](Addon.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getOrganisationsIdAddons_1

> [Addon] getOrganisationsIdAddons_1(id)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.OrganisationsApi();
let id = "id_example"; // String | 
apiInstance.getOrganisationsIdAddons_1(id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**|  | 

### Return type

[**[Addon]**](Addon.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getOrganisationsIdApplicationsAppIdAddonsEnv_2

> [Env] getOrganisationsIdApplicationsAppIdAddonsEnv_2(id, appId)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.OrganisationsApi();
let id = "id_example"; // String | 
let appId = "appId_example"; // String | 
apiInstance.getOrganisationsIdApplicationsAppIdAddonsEnv_2(id, appId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**|  | 
 **appId** | **String**|  | 

### Return type

[**[Env]**](Env.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getOrganisationsIdApplicationsAppIdAddons_2

> [Addon] getOrganisationsIdApplicationsAppIdAddons_2(id, appId)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.OrganisationsApi();
let id = "id_example"; // String | 
let appId = "appId_example"; // String | 
apiInstance.getOrganisationsIdApplicationsAppIdAddons_2(id, appId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**|  | 
 **appId** | **String**|  | 

### Return type

[**[Addon]**](Addon.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getOrganisationsIdApplicationsAppIdDependencies_1

> [Application] getOrganisationsIdApplicationsAppIdDependencies_1(appId, id)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.OrganisationsApi();
let appId = "appId_example"; // String | 
let id = "id_example"; // String | 
apiInstance.getOrganisationsIdApplicationsAppIdDependencies_1(appId, id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appId** | **String**|  | 
 **id** | **String**|  | 

### Return type

[**[Application]**](Application.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getOrganisationsIdApplicationsAppIdDependents_1

> [Application] getOrganisationsIdApplicationsAppIdDependents_1(appId, id)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.OrganisationsApi();
let appId = "appId_example"; // String | 
let id = "id_example"; // String | 
apiInstance.getOrganisationsIdApplicationsAppIdDependents_1(appId, id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appId** | **String**|  | 
 **id** | **String**|  | 

### Return type

[**[Application]**](Application.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getOrganisationsIdApplicationsAppIdDeployments_1

> [Deployment] getOrganisationsIdApplicationsAppIdDeployments_1(id, appId, opts)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.OrganisationsApi();
let id = "id_example"; // String | 
let appId = "appId_example"; // String | 
let opts = {
  'limit': "limit_example", // String | 
  'offset': "offset_example", // String | 
  'action': "action_example" // String | 
};
apiInstance.getOrganisationsIdApplicationsAppIdDeployments_1(id, appId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**|  | 
 **appId** | **String**|  | 
 **limit** | **String**|  | [optional] 
 **offset** | **String**|  | [optional] 
 **action** | **String**|  | [optional] 

### Return type

[**[Deployment]**](Deployment.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getOrganisationsIdApplicationsAppIdEnv_1

> [ListEnv] getOrganisationsIdApplicationsAppIdEnv_1(id, appId)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.OrganisationsApi();
let id = "id_example"; // String | 
let appId = "appId_example"; // String | 
apiInstance.getOrganisationsIdApplicationsAppIdEnv_1(id, appId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**|  | 
 **appId** | **String**|  | 

### Return type

[**[ListEnv]**](ListEnv.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getOrganisationsIdApplicationsAppIdInstances_1

> [AppInstance] getOrganisationsIdApplicationsAppIdInstances_1(id, appId)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.OrganisationsApi();
let id = "id_example"; // String | 
let appId = "appId_example"; // String | 
apiInstance.getOrganisationsIdApplicationsAppIdInstances_1(id, appId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**|  | 
 **appId** | **String**|  | 

### Return type

[**[AppInstance]**](AppInstance.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getOrganisationsIdApplicationsAppIdTags_1

> [String] getOrganisationsIdApplicationsAppIdTags_1(id, appId)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.OrganisationsApi();
let id = "id_example"; // String | 
let appId = "appId_example"; // String | 
apiInstance.getOrganisationsIdApplicationsAppIdTags_1(id, appId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**|  | 
 **appId** | **String**|  | 

### Return type

**[String]**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## getOrganisationsIdApplicationsAppIdVhostsFavourite_1

> Vhost getOrganisationsIdApplicationsAppIdVhostsFavourite_1(id, appId)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.OrganisationsApi();
let id = "id_example"; // String | 
let appId = "appId_example"; // String | 
apiInstance.getOrganisationsIdApplicationsAppIdVhostsFavourite_1(id, appId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**|  | 
 **appId** | **String**|  | 

### Return type

[**Vhost**](Vhost.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getOrganisationsIdApplicationsAppIdVhosts_1

> [Vhost] getOrganisationsIdApplicationsAppIdVhosts_1(id, appId)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.OrganisationsApi();
let id = "id_example"; // String | 
let appId = "appId_example"; // String | 
apiInstance.getOrganisationsIdApplicationsAppIdVhosts_1(id, appId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**|  | 
 **appId** | **String**|  | 

### Return type

[**[Vhost]**](Vhost.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getOrganisationsIdApplicationsAppId_1

> Application getOrganisationsIdApplicationsAppId_1(id, appId)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.OrganisationsApi();
let id = "id_example"; // String | 
let appId = "appId_example"; // String | 
apiInstance.getOrganisationsIdApplicationsAppId_1(id, appId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**|  | 
 **appId** | **String**|  | 

### Return type

[**Application**](Application.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getOrganisationsIdApplications_1

> [Application] getOrganisationsIdApplications_1(id)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.OrganisationsApi();
let id = "id_example"; // String | 
apiInstance.getOrganisationsIdApplications_1(id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**|  | 

### Return type

[**[Application]**](Application.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getOrganisationsIdConsumersKeySecret_0

> Secret getOrganisationsIdConsumersKeySecret_0(id, key)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.OrganisationsApi();
let id = "id_example"; // String | 
let key = "key_example"; // String | 
apiInstance.getOrganisationsIdConsumersKeySecret_0(id, key, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**|  | 
 **key** | **String**|  | 

### Return type

[**Secret**](Secret.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getOrganisationsIdConsumersKey_0

> Consumer getOrganisationsIdConsumersKey_0(id, key)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.OrganisationsApi();
let id = "id_example"; // String | 
let key = "key_example"; // String | 
apiInstance.getOrganisationsIdConsumersKey_0(id, key, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**|  | 
 **key** | **String**|  | 

### Return type

[**Consumer**](Consumer.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getOrganisationsIdConsumers_0

> [Consumer] getOrganisationsIdConsumers_0(id)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.OrganisationsApi();
let id = "id_example"; // String | 
apiInstance.getOrganisationsIdConsumers_0(id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**|  | 

### Return type

[**[Consumer]**](Consumer.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getOrganisationsIdConsumptions_0

> Conso getOrganisationsIdConsumptions_0(id, opts)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.OrganisationsApi();
let id = "id_example"; // String | 
let opts = {
  'appId': "appId_example", // String | 
  'from': "from_example", // String | 
  'to': "to_example" // String | 
};
apiInstance.getOrganisationsIdConsumptions_0(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**|  | 
 **appId** | **String**|  | [optional] 
 **from** | **String**|  | [optional] 
 **to** | **String**|  | [optional] 

### Return type

[**Conso**](Conso.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getOrganisationsIdCredits_0

> Credits getOrganisationsIdCredits_0(id)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.OrganisationsApi();
let id = "id_example"; // String | 
apiInstance.getOrganisationsIdCredits_0(id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**|  | 

### Return type

[**Credits**](Credits.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getOrganisationsIdDeployments_0

> DeploymentSummary getOrganisationsIdDeployments_0(id)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.OrganisationsApi();
let id = "id_example"; // String | 
apiInstance.getOrganisationsIdDeployments_0(id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**|  | 

### Return type

[**DeploymentSummary**](DeploymentSummary.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getOrganisationsIdInstances_0

> Object getOrganisationsIdInstances_0(id)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.OrganisationsApi();
let id = "id_example"; // String | 
apiInstance.getOrganisationsIdInstances_0(id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**|  | 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getOrganisationsIdMembers_0

> [Schema1] getOrganisationsIdMembers_0(id)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.OrganisationsApi();
let id = "id_example"; // String | 
apiInstance.getOrganisationsIdMembers_0(id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**|  | 

### Return type

[**[Schema1]**](Schema1.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getOrganisationsIdPaymentInfo_0

> getOrganisationsIdPaymentInfo_0(id)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.OrganisationsApi();
let id = "id_example"; // String | 
apiInstance.getOrganisationsIdPaymentInfo_0(id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getOrganisationsIdPaymentsBillingsBidPdf_0

> getOrganisationsIdPaymentsBillingsBidPdf_0(id, bid, opts)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.OrganisationsApi();
let id = "id_example"; // String | 
let bid = "bid_example"; // String | 
let opts = {
  'token': "token_example" // String | 
};
apiInstance.getOrganisationsIdPaymentsBillingsBidPdf_0(id, bid, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**|  | 
 **bid** | **String**|  | 
 **token** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getOrganisationsIdPaymentsBillingsBid_0

> getOrganisationsIdPaymentsBillingsBid_0(id, bid)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.OrganisationsApi();
let id = "id_example"; // String | 
let bid = "bid_example"; // String | 
apiInstance.getOrganisationsIdPaymentsBillingsBid_0(id, bid, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**|  | 
 **bid** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getOrganisationsIdPaymentsBillings_0

> getOrganisationsIdPaymentsBillings_0(id)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.OrganisationsApi();
let id = "id_example"; // String | 
apiInstance.getOrganisationsIdPaymentsBillings_0(id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getOrganisationsIdPaymentsFullPricePrice_0

> getOrganisationsIdPaymentsFullPricePrice_0(id, price)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.OrganisationsApi();
let id = "id_example"; // String | 
let price = "price_example"; // String | 
apiInstance.getOrganisationsIdPaymentsFullPricePrice_0(id, price, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**|  | 
 **price** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getOrganisationsId_0

> Organisation getOrganisationsId_0(id)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.OrganisationsApi();
let id = "id_example"; // String | 
apiInstance.getOrganisationsId_0(id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**|  | 

### Return type

[**Organisation**](Organisation.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getOrganisations_0

> [Organisation] getOrganisations_0(opts)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.OrganisationsApi();
let opts = {
  'user': "user_example" // String | 
};
apiInstance.getOrganisations_0(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **String**|  | [optional] 

### Return type

[**[Organisation]**](Organisation.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listNetworkGroupMembers_0

> [Schema1] listNetworkGroupMembers_0(ownerId, networkGroupId, opts)

List members

Lists members in a Network Group.

### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.OrganisationsApi();
let ownerId = "ownerId_example"; // String | Automatically added
let networkGroupId = "networkGroupId_example"; // String | Automatically added
let opts = {
  'body': null // Object | 
};
apiInstance.listNetworkGroupMembers_0(ownerId, networkGroupId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ownerId** | **String**| Automatically added | 
 **networkGroupId** | **String**| Automatically added | 
 **body** | **Object**|  | [optional] 

### Return type

[**[Schema1]**](Schema1.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listNetworkGroupPeers_0

> [Object] listNetworkGroupPeers_0(ownerId, networkGroupId, opts)

List peers

Lists peers in a Network Group.

### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.OrganisationsApi();
let ownerId = "ownerId_example"; // String | Automatically added
let networkGroupId = "networkGroupId_example"; // String | Automatically added
let opts = {
  'body': null // Object | 
};
apiInstance.listNetworkGroupPeers_0(ownerId, networkGroupId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ownerId** | **String**| Automatically added | 
 **networkGroupId** | **String**| Automatically added | 
 **body** | **Object**|  | [optional] 

### Return type

**[Object]**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listNetworkGroups_0

> [Object] listNetworkGroups_0(ownerId, opts)

List Network Groups

Lists Network Groups from an owner.

### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.OrganisationsApi();
let ownerId = "ownerId_example"; // String | Automatically added
let opts = {
  'body': null // Object | 
};
apiInstance.listNetworkGroups_0(ownerId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ownerId** | **String**| Automatically added | 
 **body** | **Object**|  | [optional] 

### Return type

**[Object]**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## organisationsIdAddonprovidersProviderIdDelete_0

> organisationsIdAddonprovidersProviderIdDelete_0(id, providerId)

Remove an add-on provider

Remove a given add-on provider. providerId must be owned by organisation {id}.

### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.OrganisationsApi();
let id = "id_example"; // String | 
let providerId = "providerId_example"; // String | 
apiInstance.organisationsIdAddonprovidersProviderIdDelete_0(id, providerId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**|  | 
 **providerId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## organisationsIdAddonsAddonIdInstancesGet_1

> [SupernovaInstanceView] organisationsIdAddonsAddonIdInstancesGet_1(id, addonId, opts)

List instances for this add-on.

### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.OrganisationsApi();
let id = "id_example"; // String | 
let addonId = "addonId_example"; // String | 
let opts = {
  'deploymentId': "deploymentId_example", // String | 
  'withDeleted': "withDeleted_example" // String | 
};
apiInstance.organisationsIdAddonsAddonIdInstancesGet_1(id, addonId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**|  | 
 **addonId** | **String**|  | 
 **deploymentId** | **String**|  | [optional] 
 **withDeleted** | **String**|  | [optional] 

### Return type

[**[SupernovaInstanceView]**](SupernovaInstanceView.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## organisationsIdAddonsAddonIdInstancesInstanceIdGet_1

> SupernovaInstanceView organisationsIdAddonsAddonIdInstancesInstanceIdGet_1(instanceId, id, addonId)

Get a specific instance for {addonId}

### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.OrganisationsApi();
let instanceId = "instanceId_example"; // String | 
let id = "id_example"; // String | 
let addonId = "addonId_example"; // String | 
apiInstance.organisationsIdAddonsAddonIdInstancesInstanceIdGet_1(instanceId, id, addonId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instanceId** | **String**|  | 
 **id** | **String**|  | 
 **addonId** | **String**|  | 

### Return type

[**SupernovaInstanceView**](SupernovaInstanceView.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## organisationsIdAddonsAddonIdMigrationsGet_1

> [AddonMigration] organisationsIdAddonsAddonIdMigrationsGet_1(id, addonId)

Get past migrations from add-on.

### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.OrganisationsApi();
let id = "id_example"; // String | 
let addonId = "addonId_example"; // String | 
apiInstance.organisationsIdAddonsAddonIdMigrationsGet_1(id, addonId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**|  | 
 **addonId** | **String**|  | 

### Return type

[**[AddonMigration]**](AddonMigration.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## organisationsIdAddonsAddonIdMigrationsMigrationIdGet_1

> AddonMigration organisationsIdAddonsAddonIdMigrationsMigrationIdGet_1(migrationId, id, addonId)

Get a given migration

### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.OrganisationsApi();
let migrationId = "migrationId_example"; // String | 
let id = "id_example"; // String | 
let addonId = "addonId_example"; // String | 
apiInstance.organisationsIdAddonsAddonIdMigrationsMigrationIdGet_1(migrationId, id, addonId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **migrationId** | **String**|  | 
 **id** | **String**|  | 
 **addonId** | **String**|  | 

### Return type

[**AddonMigration**](AddonMigration.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## organisationsIdAddonsAddonIdMigrationsPost_1

> Object organisationsIdAddonsAddonIdMigrationsPost_1(id, addonId, organisationsIdAddonsAddonIdMigrationsPostRequest)

Start a new add-on migration

### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.OrganisationsApi();
let id = "id_example"; // String | 
let addonId = "addonId_example"; // String | 
let organisationsIdAddonsAddonIdMigrationsPostRequest = new CleverCloudApi.OrganisationsIdAddonsAddonIdMigrationsPostRequest(); // OrganisationsIdAddonsAddonIdMigrationsPostRequest | 
apiInstance.organisationsIdAddonsAddonIdMigrationsPost_1(id, addonId, organisationsIdAddonsAddonIdMigrationsPostRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**|  | 
 **addonId** | **String**|  | 
 **organisationsIdAddonsAddonIdMigrationsPostRequest** | [**OrganisationsIdAddonsAddonIdMigrationsPostRequest**](OrganisationsIdAddonsAddonIdMigrationsPostRequest.md)|  | 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## organisationsIdAddonsAddonIdSsoGet_1

> Sso organisationsIdAddonsAddonIdSsoGet_1(id, addonId)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.OrganisationsApi();
let id = "id_example"; // String | 
let addonId = "addonId_example"; // String | 
apiInstance.organisationsIdAddonsAddonIdSsoGet_1(id, addonId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**|  | 
 **addonId** | **String**|  | 

### Return type

[**Sso**](Sso.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## organisationsIdAddonsPreordersPost_1

> organisationsIdAddonsPreordersPost_1(id, wannabeAddon)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.OrganisationsApi();
let id = "id_example"; // String | 
let wannabeAddon = new CleverCloudApi.WannabeAddon(); // WannabeAddon | 
apiInstance.organisationsIdAddonsPreordersPost_1(id, wannabeAddon, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**|  | 
 **wannabeAddon** | [**WannabeAddon**](WannabeAddon.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## organisationsIdApplicationsAppIdBranchPut_1

> organisationsIdApplicationsAppIdBranchPut_1(appId, id)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.OrganisationsApi();
let appId = "appId_example"; // String | 
let id = "id_example"; // String | 
apiInstance.organisationsIdApplicationsAppIdBranchPut_1(appId, id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appId** | **String**|  | 
 **id** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## organisationsIdApplicationsAppIdBranchesGet_1

> organisationsIdApplicationsAppIdBranchesGet_1(appId, id)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.OrganisationsApi();
let appId = "appId_example"; // String | 
let id = "id_example"; // String | 
apiInstance.organisationsIdApplicationsAppIdBranchesGet_1(appId, id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appId** | **String**|  | 
 **id** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## organisationsIdApplicationsAppIdBuildflavorPut_1

> organisationsIdApplicationsAppIdBuildflavorPut_1(appId, id)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.OrganisationsApi();
let appId = "appId_example"; // String | 
let id = "id_example"; // String | 
apiInstance.organisationsIdApplicationsAppIdBuildflavorPut_1(appId, id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appId** | **String**|  | 
 **id** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## organisationsIdApplicationsAppIdDependenciesEnvGet_1

> [LinkedAppEnv] organisationsIdApplicationsAppIdDependenciesEnvGet_1(appId, id)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.OrganisationsApi();
let appId = "appId_example"; // String | 
let id = "id_example"; // String | 
apiInstance.organisationsIdApplicationsAppIdDependenciesEnvGet_1(appId, id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appId** | **String**|  | 
 **id** | **String**|  | 

### Return type

[**[LinkedAppEnv]**](LinkedAppEnv.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## organisationsIdApplicationsAppIdDeploymentsDeploymentIdGet_1

> organisationsIdApplicationsAppIdDeploymentsDeploymentIdGet_1(appId, deploymentId, id)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.OrganisationsApi();
let appId = "appId_example"; // String | 
let deploymentId = "deploymentId_example"; // String | 
let id = "id_example"; // String | 
apiInstance.organisationsIdApplicationsAppIdDeploymentsDeploymentIdGet_1(appId, deploymentId, id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appId** | **String**|  | 
 **deploymentId** | **String**|  | 
 **id** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## organisationsIdApplicationsAppIdExposedEnvGet_1

> organisationsIdApplicationsAppIdExposedEnvGet_1(appId, id)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.OrganisationsApi();
let appId = "appId_example"; // String | 
let id = "id_example"; // String | 
apiInstance.organisationsIdApplicationsAppIdExposedEnvGet_1(appId, id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appId** | **String**|  | 
 **id** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## organisationsIdApplicationsAppIdExposedEnvPut_1

> organisationsIdApplicationsAppIdExposedEnvPut_1(appId, id)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.OrganisationsApi();
let appId = "appId_example"; // String | 
let id = "id_example"; // String | 
apiInstance.organisationsIdApplicationsAppIdExposedEnvPut_1(appId, id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appId** | **String**|  | 
 **id** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## organisationsIdApplicationsAppIdInstancesInstanceIdGet_1

> organisationsIdApplicationsAppIdInstancesInstanceIdGet_1(instanceId, appId, id)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.OrganisationsApi();
let instanceId = "instanceId_example"; // String | 
let appId = "appId_example"; // String | 
let id = "id_example"; // String | 
apiInstance.organisationsIdApplicationsAppIdInstancesInstanceIdGet_1(instanceId, appId, id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instanceId** | **String**|  | 
 **appId** | **String**|  | 
 **id** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## organisationsIdPaymentsBillingsUnpaidGet_0

> organisationsIdPaymentsBillingsUnpaidGet_0(id)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.OrganisationsApi();
let id = "id_example"; // String | 
apiInstance.organisationsIdPaymentsBillingsUnpaidGet_0(id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## organisationsIdPaymentsMethodsDefaultGet_0

> organisationsIdPaymentsMethodsDefaultGet_0(id)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.OrganisationsApi();
let id = "id_example"; // String | 
apiInstance.organisationsIdPaymentsMethodsDefaultGet_0(id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## organisationsIdPaymentsMethodsDefaultPut_0

> organisationsIdPaymentsMethodsDefaultPut_0(id, paymentData)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.OrganisationsApi();
let id = "id_example"; // String | 
let paymentData = new CleverCloudApi.PaymentData(); // PaymentData | 
apiInstance.organisationsIdPaymentsMethodsDefaultPut_0(id, paymentData, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**|  | 
 **paymentData** | [**PaymentData**](PaymentData.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## organisationsIdPaymentsMethodsGet_0

> organisationsIdPaymentsMethodsGet_0(id)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.OrganisationsApi();
let id = "id_example"; // String | 
apiInstance.organisationsIdPaymentsMethodsGet_0(id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## organisationsIdPaymentsMethodsMIdDelete_0

> organisationsIdPaymentsMethodsMIdDelete_0(mId, id)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.OrganisationsApi();
let mId = "mId_example"; // String | 
let id = "id_example"; // String | 
apiInstance.organisationsIdPaymentsMethodsMIdDelete_0(mId, id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mId** | **String**|  | 
 **id** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## organisationsIdPaymentsMethodsPost_0

> organisationsIdPaymentsMethodsPost_0(id, body)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.OrganisationsApi();
let id = "id_example"; // String | 
let body = new CleverCloudApi.Body(); // Body | 
apiInstance.organisationsIdPaymentsMethodsPost_0(id, body, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**|  | 
 **body** | [**Body**](Body.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## organisationsIdPaymentsMonthlyinvoiceGet_0

> organisationsIdPaymentsMonthlyinvoiceGet_0(id)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.OrganisationsApi();
let id = "id_example"; // String | 
apiInstance.organisationsIdPaymentsMonthlyinvoiceGet_0(id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## organisationsIdPaymentsMonthlyinvoiceMaxcreditPut_0

> organisationsIdPaymentsMonthlyinvoiceMaxcreditPut_0(id)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.OrganisationsApi();
let id = "id_example"; // String | 
apiInstance.organisationsIdPaymentsMonthlyinvoiceMaxcreditPut_0(id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## organisationsIdPaymentsRecurringGet_0

> organisationsIdPaymentsRecurringGet_0(id)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.OrganisationsApi();
let id = "id_example"; // String | 
apiInstance.organisationsIdPaymentsRecurringGet_0(id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## postOrganisationsIdAddonprovidersProviderIdFeatures_0

> Feature postOrganisationsIdAddonprovidersProviderIdFeatures_0(id, providerId, wannabeFeature)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.OrganisationsApi();
let id = "id_example"; // String | 
let providerId = "providerId_example"; // String | 
let wannabeFeature = new CleverCloudApi.WannabeFeature(); // WannabeFeature | 
apiInstance.postOrganisationsIdAddonprovidersProviderIdFeatures_0(id, providerId, wannabeFeature, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**|  | 
 **providerId** | **String**|  | 
 **wannabeFeature** | [**WannabeFeature**](WannabeFeature.md)|  | 

### Return type

[**Feature**](Feature.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: */*


## postOrganisationsIdAddonprovidersProviderIdPlans_0

> Plan postOrganisationsIdAddonprovidersProviderIdPlans_0(id, providerId, wannabePlan)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.OrganisationsApi();
let id = "id_example"; // String | 
let providerId = "providerId_example"; // String | 
let wannabePlan = new CleverCloudApi.WannabePlan(); // WannabePlan | 
apiInstance.postOrganisationsIdAddonprovidersProviderIdPlans_0(id, providerId, wannabePlan, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**|  | 
 **providerId** | **String**|  | 
 **wannabePlan** | [**WannabePlan**](WannabePlan.md)|  | 

### Return type

[**Plan**](Plan.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: */*


## postOrganisationsIdAddonprovidersProviderIdTesters_0

> postOrganisationsIdAddonprovidersProviderIdTesters_0(id, providerId)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.OrganisationsApi();
let id = "id_example"; // String | 
let providerId = "providerId_example"; // String | 
apiInstance.postOrganisationsIdAddonprovidersProviderIdTesters_0(id, providerId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**|  | 
 **providerId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## postOrganisationsIdAddonproviders_0

> Provider postOrganisationsIdAddonproviders_0(id, wannabeAddonProvider)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.OrganisationsApi();
let id = "id_example"; // String | 
let wannabeAddonProvider = new CleverCloudApi.WannabeAddonProvider(); // WannabeAddonProvider | 
apiInstance.postOrganisationsIdAddonproviders_0(id, wannabeAddonProvider, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**|  | 
 **wannabeAddonProvider** | [**WannabeAddonProvider**](WannabeAddonProvider.md)|  | 

### Return type

[**Provider**](Provider.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: */*


## postOrganisationsIdAddons_1

> Addon postOrganisationsIdAddons_1(id, wannabeAddon)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.OrganisationsApi();
let id = "id_example"; // String | 
let wannabeAddon = new CleverCloudApi.WannabeAddon(); // WannabeAddon | 
apiInstance.postOrganisationsIdAddons_1(id, wannabeAddon, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**|  | 
 **wannabeAddon** | [**WannabeAddon**](WannabeAddon.md)|  | 

### Return type

[**Addon**](Addon.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: */*


## postOrganisationsIdApplicationsAppIdAddons_2

> postOrganisationsIdApplicationsAppIdAddons_2(id, appId, body)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.OrganisationsApi();
let id = "id_example"; // String | 
let appId = "appId_example"; // String | 
let body = new CleverCloudApi.Body(); // Body | 
apiInstance.postOrganisationsIdApplicationsAppIdAddons_2(id, appId, body, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**|  | 
 **appId** | **String**|  | 
 **body** | [**Body**](Body.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## postOrganisationsIdApplicationsAppIdInstances_1

> postOrganisationsIdApplicationsAppIdInstances_1(id, appId, opts)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.OrganisationsApi();
let id = "id_example"; // String | 
let appId = "appId_example"; // String | 
let opts = {
  'commit': "commit_example" // String | 
};
apiInstance.postOrganisationsIdApplicationsAppIdInstances_1(id, appId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**|  | 
 **appId** | **String**|  | 
 **commit** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## postOrganisationsIdApplications_1

> Application postOrganisationsIdApplications_1(id, wannabeApplication)



Creates an application. If you want to create a Github app, you need to replace the oauthApp field with what you will find here: https://github.com/CleverCloud/doc.clever-cloud.com/issues/179

### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.OrganisationsApi();
let id = "id_example"; // String | 
let wannabeApplication = new CleverCloudApi.WannabeApplication(); // WannabeApplication | 
apiInstance.postOrganisationsIdApplications_1(id, wannabeApplication, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**|  | 
 **wannabeApplication** | [**WannabeApplication**](WannabeApplication.md)|  | 

### Return type

[**Application**](Application.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: */*


## postOrganisationsIdConsumers_0

> postOrganisationsIdConsumers_0(id, wannabeConsumer)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.OrganisationsApi();
let id = "id_example"; // String | 
let wannabeConsumer = new CleverCloudApi.WannabeConsumer(); // WannabeConsumer | 
apiInstance.postOrganisationsIdConsumers_0(id, wannabeConsumer, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**|  | 
 **wannabeConsumer** | [**WannabeConsumer**](WannabeConsumer.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## postOrganisationsIdMembers_0

> postOrganisationsIdMembers_0(id, body, opts)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.OrganisationsApi();
let id = "id_example"; // String | 
let body = new CleverCloudApi.Schema2(); // Schema2 | 
let opts = {
  'invitationKey': "invitationKey_example" // String | 
};
apiInstance.postOrganisationsIdMembers_0(id, body, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**|  | 
 **body** | **Schema2**|  | 
 **invitationKey** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## postOrganisationsIdPaymentsBillings_0

> postOrganisationsIdPaymentsBillings_0(id)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.OrganisationsApi();
let id = "id_example"; // String | 
apiInstance.postOrganisationsIdPaymentsBillings_0(id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## postOrganisations_0

> Organisation postOrganisations_0(wannabeOrganisation)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.OrganisationsApi();
let wannabeOrganisation = new CleverCloudApi.WannabeOrganisation(); // WannabeOrganisation | 
apiInstance.postOrganisations_0(wannabeOrganisation, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wannabeOrganisation** | [**WannabeOrganisation**](WannabeOrganisation.md)|  | 

### Return type

[**Organisation**](Organisation.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: */*


## putOrganisationsIdAddonprovidersProviderIdPlansPlanIdFeaturesFeatureName_0

> putOrganisationsIdAddonprovidersProviderIdPlansPlanIdFeaturesFeatureName_0(id, featureName, providerId, planId, wannabePlanFeature)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.OrganisationsApi();
let id = "id_example"; // String | 
let featureName = "featureName_example"; // String | 
let providerId = "providerId_example"; // String | 
let planId = "planId_example"; // String | 
let wannabePlanFeature = new CleverCloudApi.WannabePlanFeature(); // WannabePlanFeature | 
apiInstance.putOrganisationsIdAddonprovidersProviderIdPlansPlanIdFeaturesFeatureName_0(id, featureName, providerId, planId, wannabePlanFeature, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**|  | 
 **featureName** | **String**|  | 
 **providerId** | **String**|  | 
 **planId** | **String**|  | 
 **wannabePlanFeature** | [**WannabePlanFeature**](WannabePlanFeature.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## putOrganisationsIdAddonprovidersProviderIdPlansPlanId_0

> Plan putOrganisationsIdAddonprovidersProviderIdPlansPlanId_0(id, providerId, planId, wannabePlan)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.OrganisationsApi();
let id = "id_example"; // String | 
let providerId = "providerId_example"; // String | 
let planId = "planId_example"; // String | 
let wannabePlan = new CleverCloudApi.WannabePlan(); // WannabePlan | 
apiInstance.putOrganisationsIdAddonprovidersProviderIdPlansPlanId_0(id, providerId, planId, wannabePlan, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**|  | 
 **providerId** | **String**|  | 
 **planId** | **String**|  | 
 **wannabePlan** | [**WannabePlan**](WannabePlan.md)|  | 

### Return type

[**Plan**](Plan.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: */*


## putOrganisationsIdAddonprovidersProviderId_0

> Provider putOrganisationsIdAddonprovidersProviderId_0(id, providerId, wannabeAddonProvider)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.OrganisationsApi();
let id = "id_example"; // String | 
let providerId = "providerId_example"; // String | 
let wannabeAddonProvider = new CleverCloudApi.WannabeAddonProvider(); // WannabeAddonProvider | 
apiInstance.putOrganisationsIdAddonprovidersProviderId_0(id, providerId, wannabeAddonProvider, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**|  | 
 **providerId** | **String**|  | 
 **wannabeAddonProvider** | [**WannabeAddonProvider**](WannabeAddonProvider.md)|  | 

### Return type

[**Provider**](Provider.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: */*


## putOrganisationsIdAddonsAddonIdTagsTag_1

> putOrganisationsIdAddonsAddonIdTagsTag_1(id, tag, addonId, body)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.OrganisationsApi();
let id = "id_example"; // String | 
let tag = "tag_example"; // String | 
let addonId = "addonId_example"; // String | 
let body = new CleverCloudApi.Body(); // Body | 
apiInstance.putOrganisationsIdAddonsAddonIdTagsTag_1(id, tag, addonId, body, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**|  | 
 **tag** | **String**|  | 
 **addonId** | **String**|  | 
 **body** | [**Body**](Body.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## putOrganisationsIdAddonsAddonId_1

> Addon putOrganisationsIdAddonsAddonId_1(id, addonId, wannabeAddon)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.OrganisationsApi();
let id = "id_example"; // String | 
let addonId = "addonId_example"; // String | 
let wannabeAddon = new CleverCloudApi.WannabeAddon(); // WannabeAddon | 
apiInstance.putOrganisationsIdAddonsAddonId_1(id, addonId, wannabeAddon, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**|  | 
 **addonId** | **String**|  | 
 **wannabeAddon** | [**WannabeAddon**](WannabeAddon.md)|  | 

### Return type

[**Addon**](Addon.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: */*


## putOrganisationsIdApplicationsAppIdDependenciesDependencyId_1

> putOrganisationsIdApplicationsAppIdDependenciesDependencyId_1(dependencyId, appId, id, body)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.OrganisationsApi();
let dependencyId = "dependencyId_example"; // String | 
let appId = "appId_example"; // String | 
let id = "id_example"; // String | 
let body = new CleverCloudApi.Body(); // Body | 
apiInstance.putOrganisationsIdApplicationsAppIdDependenciesDependencyId_1(dependencyId, appId, id, body, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dependencyId** | **String**|  | 
 **appId** | **String**|  | 
 **id** | **String**|  | 
 **body** | [**Body**](Body.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## putOrganisationsIdApplicationsAppIdEnvEnvName_1

> ListEnv putOrganisationsIdApplicationsAppIdEnvEnvName_1(id, appId, envName, wannabeEnv)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.OrganisationsApi();
let id = "id_example"; // String | 
let appId = "appId_example"; // String | 
let envName = "envName_example"; // String | 
let wannabeEnv = new CleverCloudApi.WannabeEnv(); // WannabeEnv | 
apiInstance.putOrganisationsIdApplicationsAppIdEnvEnvName_1(id, appId, envName, wannabeEnv, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**|  | 
 **appId** | **String**|  | 
 **envName** | **String**|  | 
 **wannabeEnv** | [**WannabeEnv**](WannabeEnv.md)|  | 

### Return type

[**ListEnv**](ListEnv.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: */*


## putOrganisationsIdApplicationsAppIdEnv_1

> ListEnv putOrganisationsIdApplicationsAppIdEnv_1(id, appId, wannabeEnv)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.OrganisationsApi();
let id = "id_example"; // String | 
let appId = "appId_example"; // String | 
let wannabeEnv = new CleverCloudApi.WannabeEnv(); // WannabeEnv | 
apiInstance.putOrganisationsIdApplicationsAppIdEnv_1(id, appId, wannabeEnv, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**|  | 
 **appId** | **String**|  | 
 **wannabeEnv** | [**WannabeEnv**](WannabeEnv.md)|  | 

### Return type

[**ListEnv**](ListEnv.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: */*


## putOrganisationsIdApplicationsAppIdTagsTag_1

> putOrganisationsIdApplicationsAppIdTagsTag_1(id, appId, tag, body)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.OrganisationsApi();
let id = "id_example"; // String | 
let appId = "appId_example"; // String | 
let tag = "tag_example"; // String | 
let body = new CleverCloudApi.Body(); // Body | 
apiInstance.putOrganisationsIdApplicationsAppIdTagsTag_1(id, appId, tag, body, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**|  | 
 **appId** | **String**|  | 
 **tag** | **String**|  | 
 **body** | [**Body**](Body.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## putOrganisationsIdApplicationsAppIdVhostsDomain_1

> putOrganisationsIdApplicationsAppIdVhostsDomain_1(id, appId, domain, vhost)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.OrganisationsApi();
let id = "id_example"; // String | 
let appId = "appId_example"; // String | 
let domain = "domain_example"; // String | 
let vhost = new CleverCloudApi.Vhost(); // Vhost | 
apiInstance.putOrganisationsIdApplicationsAppIdVhostsDomain_1(id, appId, domain, vhost, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**|  | 
 **appId** | **String**|  | 
 **domain** | **String**|  | 
 **vhost** | [**Vhost**](Vhost.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## putOrganisationsIdApplicationsAppIdVhostsFavourite_1

> putOrganisationsIdApplicationsAppIdVhostsFavourite_1(id, appId, vhost)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.OrganisationsApi();
let id = "id_example"; // String | 
let appId = "appId_example"; // String | 
let vhost = new CleverCloudApi.Vhost(); // Vhost | 
apiInstance.putOrganisationsIdApplicationsAppIdVhostsFavourite_1(id, appId, vhost, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**|  | 
 **appId** | **String**|  | 
 **vhost** | [**Vhost**](Vhost.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## putOrganisationsIdApplicationsAppId_1

> Application putOrganisationsIdApplicationsAppId_1(id, appId, wannabeApplication)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.OrganisationsApi();
let id = "id_example"; // String | 
let appId = "appId_example"; // String | 
let wannabeApplication = new CleverCloudApi.WannabeApplication(); // WannabeApplication | 
apiInstance.putOrganisationsIdApplicationsAppId_1(id, appId, wannabeApplication, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**|  | 
 **appId** | **String**|  | 
 **wannabeApplication** | [**WannabeApplication**](WannabeApplication.md)|  | 

### Return type

[**Application**](Application.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: */*


## putOrganisationsIdAvatar_0

> putOrganisationsIdAvatar_0(id)



If you want to upload an image from your computer, send the image in the body of the request without anything else.

### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.OrganisationsApi();
let id = "id_example"; // String | 
apiInstance.putOrganisationsIdAvatar_0(id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## putOrganisationsIdConsumersKey_0

> putOrganisationsIdConsumersKey_0(id, key, wannabeConsumer)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.OrganisationsApi();
let id = "id_example"; // String | 
let key = "key_example"; // String | 
let wannabeConsumer = new CleverCloudApi.WannabeConsumer(); // WannabeConsumer | 
apiInstance.putOrganisationsIdConsumersKey_0(id, key, wannabeConsumer, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**|  | 
 **key** | **String**|  | 
 **wannabeConsumer** | [**WannabeConsumer**](WannabeConsumer.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## putOrganisationsIdMembersUserId_0

> putOrganisationsIdMembersUserId_0(id, userId, body)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.OrganisationsApi();
let id = "id_example"; // String | 
let userId = "userId_example"; // String | 
let body = new CleverCloudApi.Schema2(); // Schema2 | 
apiInstance.putOrganisationsIdMembersUserId_0(id, userId, body, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**|  | 
 **userId** | **String**|  | 
 **body** | **Schema2**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## putOrganisationsIdPaymentsBillingsBid_0

> putOrganisationsIdPaymentsBillingsBid_0(id, bid)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.OrganisationsApi();
let id = "id_example"; // String | 
let bid = "bid_example"; // String | 
apiInstance.putOrganisationsIdPaymentsBillingsBid_0(id, bid, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**|  | 
 **bid** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## putOrganisationsId_0

> Organisation putOrganisationsId_0(id, wannabeOrganisation)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.OrganisationsApi();
let id = "id_example"; // String | 
let wannabeOrganisation = new CleverCloudApi.WannabeOrganisation(); // WannabeOrganisation | 
apiInstance.putOrganisationsId_0(id, wannabeOrganisation, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**|  | 
 **wannabeOrganisation** | [**WannabeOrganisation**](WannabeOrganisation.md)|  | 

### Return type

[**Organisation**](Organisation.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: */*

