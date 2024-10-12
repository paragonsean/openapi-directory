# OrganisationsApi

All URIs are relative to *https://api.clever-cloud.com/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createNetworkGroupExternalPeer_0**](OrganisationsApi.md#createNetworkGroupExternalPeer_0) | **POST** /v4/networkgroups/organisations/{ownerId}/networkgroups/{networkGroupId}/external-peers | Add external peer |
| [**createNetworkGroupMember_0**](OrganisationsApi.md#createNetworkGroupMember_0) | **POST** /v4/networkgroups/organisations/{ownerId}/networkgroups/{networkGroupId}/members | Add member |
| [**createNetworkGroup_0**](OrganisationsApi.md#createNetworkGroup_0) | **POST** /v4/networkgroups/organisations/{ownerId}/networkgroups | Create Network Group |
| [**deleteNetworkGroupExternalPeer_0**](OrganisationsApi.md#deleteNetworkGroupExternalPeer_0) | **DELETE** /v4/networkgroups/organisations/{ownerId}/networkgroups/{networkGroupId}/external-peers/{peerId} | Remove external peer |
| [**deleteNetworkGroupMember_0**](OrganisationsApi.md#deleteNetworkGroupMember_0) | **DELETE** /v4/networkgroups/organisations/{ownerId}/networkgroups/{networkGroupId}/members/{memberId} | Remove member |
| [**deleteNetworkGroupPeer_0**](OrganisationsApi.md#deleteNetworkGroupPeer_0) | **DELETE** /v4/networkgroups/organisations/{ownerId}/networkgroups/{networkGroupId}/peers/{peerId} | Remove peer |
| [**deleteNetworkGroup_0**](OrganisationsApi.md#deleteNetworkGroup_0) | **DELETE** /v4/networkgroups/organisations/{ownerId}/networkgroups/{networkGroupId} | Delete Network Group |
| [**deleteOrganisationsIdAddonprovidersProviderIdFeaturesFeatureId_0**](OrganisationsApi.md#deleteOrganisationsIdAddonprovidersProviderIdFeaturesFeatureId_0) | **DELETE** /organisations/{id}/addonproviders/{providerId}/features/{featureId} |  |
| [**deleteOrganisationsIdAddonprovidersProviderIdPlansPlanIdFeaturesFeatureName_0**](OrganisationsApi.md#deleteOrganisationsIdAddonprovidersProviderIdPlansPlanIdFeaturesFeatureName_0) | **DELETE** /organisations/{id}/addonproviders/{providerId}/plans/{planId}/features/{featureName} |  |
| [**deleteOrganisationsIdAddonprovidersProviderIdPlansPlanId_0**](OrganisationsApi.md#deleteOrganisationsIdAddonprovidersProviderIdPlansPlanId_0) | **DELETE** /organisations/{id}/addonproviders/{providerId}/plans/{planId} |  |
| [**deleteOrganisationsIdAddonsAddonIdTagsTag_1**](OrganisationsApi.md#deleteOrganisationsIdAddonsAddonIdTagsTag_1) | **DELETE** /organisations/{id}/addons/{addonId}/tags/{tag} |  |
| [**deleteOrganisationsIdAddonsAddonId_1**](OrganisationsApi.md#deleteOrganisationsIdAddonsAddonId_1) | **DELETE** /organisations/{id}/addons/{addonId} |  |
| [**deleteOrganisationsIdApplicationsAppIdAddonsAddonId_2**](OrganisationsApi.md#deleteOrganisationsIdApplicationsAppIdAddonsAddonId_2) | **DELETE** /organisations/{id}/applications/{appId}/addons/{addonId} |  |
| [**deleteOrganisationsIdApplicationsAppIdDependenciesDependencyId_1**](OrganisationsApi.md#deleteOrganisationsIdApplicationsAppIdDependenciesDependencyId_1) | **DELETE** /organisations/{id}/applications/{appId}/dependencies/{dependencyId} |  |
| [**deleteOrganisationsIdApplicationsAppIdDeploymentsDeploymentIdInstances_1**](OrganisationsApi.md#deleteOrganisationsIdApplicationsAppIdDeploymentsDeploymentIdInstances_1) | **DELETE** /organisations/{id}/applications/{appId}/deployments/{deploymentId}/instances |  |
| [**deleteOrganisationsIdApplicationsAppIdEnvEnvName_1**](OrganisationsApi.md#deleteOrganisationsIdApplicationsAppIdEnvEnvName_1) | **DELETE** /organisations/{id}/applications/{appId}/env/{envName} |  |
| [**deleteOrganisationsIdApplicationsAppIdInstances_1**](OrganisationsApi.md#deleteOrganisationsIdApplicationsAppIdInstances_1) | **DELETE** /organisations/{id}/applications/{appId}/instances |  |
| [**deleteOrganisationsIdApplicationsAppIdTagsTag_1**](OrganisationsApi.md#deleteOrganisationsIdApplicationsAppIdTagsTag_1) | **DELETE** /organisations/{id}/applications/{appId}/tags/{tag} |  |
| [**deleteOrganisationsIdApplicationsAppIdVhostsDomain_1**](OrganisationsApi.md#deleteOrganisationsIdApplicationsAppIdVhostsDomain_1) | **DELETE** /organisations/{id}/applications/{appId}/vhosts/{domain} |  |
| [**deleteOrganisationsIdApplicationsAppIdVhostsFavourite_1**](OrganisationsApi.md#deleteOrganisationsIdApplicationsAppIdVhostsFavourite_1) | **DELETE** /organisations/{id}/applications/{appId}/vhosts/favourite |  |
| [**deleteOrganisationsIdApplicationsAppId_1**](OrganisationsApi.md#deleteOrganisationsIdApplicationsAppId_1) | **DELETE** /organisations/{id}/applications/{appId} |  |
| [**deleteOrganisationsIdConsumersKey_0**](OrganisationsApi.md#deleteOrganisationsIdConsumersKey_0) | **DELETE** /organisations/{id}/consumers/{key} |  |
| [**deleteOrganisationsIdMembersUserId_0**](OrganisationsApi.md#deleteOrganisationsIdMembersUserId_0) | **DELETE** /organisations/{id}/members/{userId} |  |
| [**deleteOrganisationsIdPaymentsBillingsBid_0**](OrganisationsApi.md#deleteOrganisationsIdPaymentsBillingsBid_0) | **DELETE** /organisations/{id}/payments/billings/{bid} |  |
| [**deleteOrganisationsIdPaymentsRecurring_0**](OrganisationsApi.md#deleteOrganisationsIdPaymentsRecurring_0) | **DELETE** /organisations/{id}/payments/recurring |  |
| [**deleteOrganisationsId_0**](OrganisationsApi.md#deleteOrganisationsId_0) | **DELETE** /organisations/{id} |  |
| [**getNetworkGroupMember_0**](OrganisationsApi.md#getNetworkGroupMember_0) | **GET** /v4/networkgroups/organisations/{ownerId}/networkgroups/{networkGroupId}/members/{memberId} | Get member |
| [**getNetworkGroupPeer_0**](OrganisationsApi.md#getNetworkGroupPeer_0) | **GET** /v4/networkgroups/organisations/{ownerId}/networkgroups/{networkGroupId}/peers/{peerId} | Get peer |
| [**getNetworkGroupStream_0**](OrganisationsApi.md#getNetworkGroupStream_0) | **GET** /v4/networkgroups/organisations/{ownerId}/networkgroups/{networkGroupId}/stream | Network Group SSE |
| [**getNetworkGroupWireGuardConfigurationStream_0**](OrganisationsApi.md#getNetworkGroupWireGuardConfigurationStream_0) | **GET** /v4/networkgroups/organisations/{ownerId}/networkgroups/{networkGroupId}/peers/{peerId}/wireguard/configuration/stream | Get WireGuard® configuration |
| [**getNetworkGroupWireGuardConfiguration_0**](OrganisationsApi.md#getNetworkGroupWireGuardConfiguration_0) | **GET** /v4/networkgroups/organisations/{ownerId}/networkgroups/{networkGroupId}/peers/{peerId}/wireguard/configuration | Get WireGuard® configuration |
| [**getNetworkGroup_0**](OrganisationsApi.md#getNetworkGroup_0) | **GET** /v4/networkgroups/organisations/{ownerId}/networkgroups/{networkGroupId} | Get Network Group |
| [**getOrganisationsIdAddonprovidersProviderIdFeatures_0**](OrganisationsApi.md#getOrganisationsIdAddonprovidersProviderIdFeatures_0) | **GET** /organisations/{id}/addonproviders/{providerId}/features |  |
| [**getOrganisationsIdAddonprovidersProviderIdPlansPlanId_0**](OrganisationsApi.md#getOrganisationsIdAddonprovidersProviderIdPlansPlanId_0) | **GET** /organisations/{id}/addonproviders/{providerId}/plans/{planId} |  |
| [**getOrganisationsIdAddonprovidersProviderIdPlans_0**](OrganisationsApi.md#getOrganisationsIdAddonprovidersProviderIdPlans_0) | **GET** /organisations/{id}/addonproviders/{providerId}/plans |  |
| [**getOrganisationsIdAddonprovidersProviderIdTags_0**](OrganisationsApi.md#getOrganisationsIdAddonprovidersProviderIdTags_0) | **GET** /organisations/{id}/addonproviders/{providerId}/tags |  |
| [**getOrganisationsIdAddonprovidersProviderId_0**](OrganisationsApi.md#getOrganisationsIdAddonprovidersProviderId_0) | **GET** /organisations/{id}/addonproviders/{providerId} |  |
| [**getOrganisationsIdAddonproviders_0**](OrganisationsApi.md#getOrganisationsIdAddonproviders_0) | **GET** /organisations/{id}/addonproviders |  |
| [**getOrganisationsIdAddonsAddonIdApplications_2**](OrganisationsApi.md#getOrganisationsIdAddonsAddonIdApplications_2) | **GET** /organisations/{id}/addons/{addonId}/applications |  |
| [**getOrganisationsIdAddonsAddonIdEnv_1**](OrganisationsApi.md#getOrganisationsIdAddonsAddonIdEnv_1) | **GET** /organisations/{id}/addons/{addonId}/env |  |
| [**getOrganisationsIdAddonsAddonIdSso_0**](OrganisationsApi.md#getOrganisationsIdAddonsAddonIdSso_0) | **GET** /organisations/{id}/addonproviders/{providerId}/sso |  |
| [**getOrganisationsIdAddonsAddonIdTags_1**](OrganisationsApi.md#getOrganisationsIdAddonsAddonIdTags_1) | **GET** /organisations/{id}/addons/{addonId}/tags |  |
| [**getOrganisationsIdAddonsAddonId_1**](OrganisationsApi.md#getOrganisationsIdAddonsAddonId_1) | **GET** /organisations/{id}/addons/{addonId} |  |
| [**getOrganisationsIdAddons_1**](OrganisationsApi.md#getOrganisationsIdAddons_1) | **GET** /organisations/{id}/addons |  |
| [**getOrganisationsIdApplicationsAppIdAddonsEnv_2**](OrganisationsApi.md#getOrganisationsIdApplicationsAppIdAddonsEnv_2) | **GET** /organisations/{id}/applications/{appId}/addons/env |  |
| [**getOrganisationsIdApplicationsAppIdAddons_2**](OrganisationsApi.md#getOrganisationsIdApplicationsAppIdAddons_2) | **GET** /organisations/{id}/applications/{appId}/addons |  |
| [**getOrganisationsIdApplicationsAppIdDependencies_1**](OrganisationsApi.md#getOrganisationsIdApplicationsAppIdDependencies_1) | **GET** /organisations/{id}/applications/{appId}/dependencies |  |
| [**getOrganisationsIdApplicationsAppIdDependents_1**](OrganisationsApi.md#getOrganisationsIdApplicationsAppIdDependents_1) | **GET** /organisations/{id}/applications/{appId}/dependents |  |
| [**getOrganisationsIdApplicationsAppIdDeployments_1**](OrganisationsApi.md#getOrganisationsIdApplicationsAppIdDeployments_1) | **GET** /organisations/{id}/applications/{appId}/deployments |  |
| [**getOrganisationsIdApplicationsAppIdEnv_1**](OrganisationsApi.md#getOrganisationsIdApplicationsAppIdEnv_1) | **GET** /organisations/{id}/applications/{appId}/env |  |
| [**getOrganisationsIdApplicationsAppIdInstances_1**](OrganisationsApi.md#getOrganisationsIdApplicationsAppIdInstances_1) | **GET** /organisations/{id}/applications/{appId}/instances |  |
| [**getOrganisationsIdApplicationsAppIdTags_1**](OrganisationsApi.md#getOrganisationsIdApplicationsAppIdTags_1) | **GET** /organisations/{id}/applications/{appId}/tags |  |
| [**getOrganisationsIdApplicationsAppIdVhostsFavourite_1**](OrganisationsApi.md#getOrganisationsIdApplicationsAppIdVhostsFavourite_1) | **GET** /organisations/{id}/applications/{appId}/vhosts/favourite |  |
| [**getOrganisationsIdApplicationsAppIdVhosts_1**](OrganisationsApi.md#getOrganisationsIdApplicationsAppIdVhosts_1) | **GET** /organisations/{id}/applications/{appId}/vhosts |  |
| [**getOrganisationsIdApplicationsAppId_1**](OrganisationsApi.md#getOrganisationsIdApplicationsAppId_1) | **GET** /organisations/{id}/applications/{appId} |  |
| [**getOrganisationsIdApplications_1**](OrganisationsApi.md#getOrganisationsIdApplications_1) | **GET** /organisations/{id}/applications |  |
| [**getOrganisationsIdConsumersKeySecret_0**](OrganisationsApi.md#getOrganisationsIdConsumersKeySecret_0) | **GET** /organisations/{id}/consumers/{key}/secret |  |
| [**getOrganisationsIdConsumersKey_0**](OrganisationsApi.md#getOrganisationsIdConsumersKey_0) | **GET** /organisations/{id}/consumers/{key} |  |
| [**getOrganisationsIdConsumers_0**](OrganisationsApi.md#getOrganisationsIdConsumers_0) | **GET** /organisations/{id}/consumers |  |
| [**getOrganisationsIdConsumptions_0**](OrganisationsApi.md#getOrganisationsIdConsumptions_0) | **GET** /organisations/{id}/consumptions |  |
| [**getOrganisationsIdCredits_0**](OrganisationsApi.md#getOrganisationsIdCredits_0) | **GET** /organisations/{id}/credits |  |
| [**getOrganisationsIdDeployments_0**](OrganisationsApi.md#getOrganisationsIdDeployments_0) | **GET** /organisations/{id}/deployments |  |
| [**getOrganisationsIdInstances_0**](OrganisationsApi.md#getOrganisationsIdInstances_0) | **GET** /organisations/{id}/instances |  |
| [**getOrganisationsIdMembers_0**](OrganisationsApi.md#getOrganisationsIdMembers_0) | **GET** /organisations/{id}/members |  |
| [**getOrganisationsIdPaymentInfo_0**](OrganisationsApi.md#getOrganisationsIdPaymentInfo_0) | **GET** /organisations/{id}/payment-info |  |
| [**getOrganisationsIdPaymentsBillingsBidPdf_0**](OrganisationsApi.md#getOrganisationsIdPaymentsBillingsBidPdf_0) | **GET** /organisations/{id}/payments/billings/{bid}.pdf |  |
| [**getOrganisationsIdPaymentsBillingsBid_0**](OrganisationsApi.md#getOrganisationsIdPaymentsBillingsBid_0) | **GET** /organisations/{id}/payments/billings/{bid} |  |
| [**getOrganisationsIdPaymentsBillings_0**](OrganisationsApi.md#getOrganisationsIdPaymentsBillings_0) | **GET** /organisations/{id}/payments/billings |  |
| [**getOrganisationsIdPaymentsFullPricePrice_0**](OrganisationsApi.md#getOrganisationsIdPaymentsFullPricePrice_0) | **GET** /organisations/{id}/payments/fullprice/{price} |  |
| [**getOrganisationsId_0**](OrganisationsApi.md#getOrganisationsId_0) | **GET** /organisations/{id} |  |
| [**getOrganisations_0**](OrganisationsApi.md#getOrganisations_0) | **GET** /organisations |  |
| [**listNetworkGroupMembers_0**](OrganisationsApi.md#listNetworkGroupMembers_0) | **GET** /v4/networkgroups/organisations/{ownerId}/networkgroups/{networkGroupId}/members | List members |
| [**listNetworkGroupPeers_0**](OrganisationsApi.md#listNetworkGroupPeers_0) | **GET** /v4/networkgroups/organisations/{ownerId}/networkgroups/{networkGroupId}/peers | List peers |
| [**listNetworkGroups_0**](OrganisationsApi.md#listNetworkGroups_0) | **GET** /v4/networkgroups/organisations/{ownerId}/networkgroups | List Network Groups |
| [**organisationsIdAddonprovidersProviderIdDelete_0**](OrganisationsApi.md#organisationsIdAddonprovidersProviderIdDelete_0) | **DELETE** /organisations/{id}/addonproviders/{providerId} | Remove an add-on provider |
| [**organisationsIdAddonsAddonIdInstancesGet_1**](OrganisationsApi.md#organisationsIdAddonsAddonIdInstancesGet_1) | **GET** /organisations/{id}/addons/{addonId}/instances | List instances for this add-on. |
| [**organisationsIdAddonsAddonIdInstancesInstanceIdGet_1**](OrganisationsApi.md#organisationsIdAddonsAddonIdInstancesInstanceIdGet_1) | **GET** /organisations/{id}/addons/{addonId}/instances/{instanceId} | Get a specific instance for {addonId} |
| [**organisationsIdAddonsAddonIdMigrationsGet_1**](OrganisationsApi.md#organisationsIdAddonsAddonIdMigrationsGet_1) | **GET** /organisations/{id}/addons/{addonId}/migrations | Get past migrations from add-on. |
| [**organisationsIdAddonsAddonIdMigrationsMigrationIdGet_1**](OrganisationsApi.md#organisationsIdAddonsAddonIdMigrationsMigrationIdGet_1) | **GET** /organisations/{id}/addons/{addonId}/migrations/{migrationId} | Get a given migration |
| [**organisationsIdAddonsAddonIdMigrationsPost_1**](OrganisationsApi.md#organisationsIdAddonsAddonIdMigrationsPost_1) | **POST** /organisations/{id}/addons/{addonId}/migrations | Start a new add-on migration |
| [**organisationsIdAddonsAddonIdSsoGet_1**](OrganisationsApi.md#organisationsIdAddonsAddonIdSsoGet_1) | **GET** /organisations/{id}/addons/{addonId}/sso |  |
| [**organisationsIdAddonsPreordersPost_1**](OrganisationsApi.md#organisationsIdAddonsPreordersPost_1) | **POST** /organisations/{id}/addons/preorders |  |
| [**organisationsIdApplicationsAppIdBranchPut_1**](OrganisationsApi.md#organisationsIdApplicationsAppIdBranchPut_1) | **PUT** /organisations/{id}/applications/{appId}/branch |  |
| [**organisationsIdApplicationsAppIdBranchesGet_1**](OrganisationsApi.md#organisationsIdApplicationsAppIdBranchesGet_1) | **GET** /organisations/{id}/applications/{appId}/branches |  |
| [**organisationsIdApplicationsAppIdBuildflavorPut_1**](OrganisationsApi.md#organisationsIdApplicationsAppIdBuildflavorPut_1) | **PUT** /organisations/{id}/applications/{appId}/buildflavor |  |
| [**organisationsIdApplicationsAppIdDependenciesEnvGet_1**](OrganisationsApi.md#organisationsIdApplicationsAppIdDependenciesEnvGet_1) | **GET** /organisations/{id}/applications/{appId}/dependencies/env |  |
| [**organisationsIdApplicationsAppIdDeploymentsDeploymentIdGet_1**](OrganisationsApi.md#organisationsIdApplicationsAppIdDeploymentsDeploymentIdGet_1) | **GET** /organisations/{id}/applications/{appId}/deployments/{deploymentId} |  |
| [**organisationsIdApplicationsAppIdExposedEnvGet_1**](OrganisationsApi.md#organisationsIdApplicationsAppIdExposedEnvGet_1) | **GET** /organisations/{id}/applications/{appId}/exposed_env |  |
| [**organisationsIdApplicationsAppIdExposedEnvPut_1**](OrganisationsApi.md#organisationsIdApplicationsAppIdExposedEnvPut_1) | **PUT** /organisations/{id}/applications/{appId}/exposed_env |  |
| [**organisationsIdApplicationsAppIdInstancesInstanceIdGet_1**](OrganisationsApi.md#organisationsIdApplicationsAppIdInstancesInstanceIdGet_1) | **GET** /organisations/{id}/applications/{appId}/instances/{instanceId} |  |
| [**organisationsIdPaymentsBillingsUnpaidGet_0**](OrganisationsApi.md#organisationsIdPaymentsBillingsUnpaidGet_0) | **GET** /organisations/{id}/payments/billings/unpaid |  |
| [**organisationsIdPaymentsMethodsDefaultGet_0**](OrganisationsApi.md#organisationsIdPaymentsMethodsDefaultGet_0) | **GET** /organisations/{id}/payments/methods/default |  |
| [**organisationsIdPaymentsMethodsDefaultPut_0**](OrganisationsApi.md#organisationsIdPaymentsMethodsDefaultPut_0) | **PUT** /organisations/{id}/payments/methods/default |  |
| [**organisationsIdPaymentsMethodsGet_0**](OrganisationsApi.md#organisationsIdPaymentsMethodsGet_0) | **GET** /organisations/{id}/payments/methods |  |
| [**organisationsIdPaymentsMethodsMIdDelete_0**](OrganisationsApi.md#organisationsIdPaymentsMethodsMIdDelete_0) | **DELETE** /organisations/{id}/payments/methods/{mId} |  |
| [**organisationsIdPaymentsMethodsPost_0**](OrganisationsApi.md#organisationsIdPaymentsMethodsPost_0) | **POST** /organisations/{id}/payments/methods |  |
| [**organisationsIdPaymentsMonthlyinvoiceGet_0**](OrganisationsApi.md#organisationsIdPaymentsMonthlyinvoiceGet_0) | **GET** /organisations/{id}/payments/monthlyinvoice |  |
| [**organisationsIdPaymentsMonthlyinvoiceMaxcreditPut_0**](OrganisationsApi.md#organisationsIdPaymentsMonthlyinvoiceMaxcreditPut_0) | **PUT** /organisations/{id}/payments/monthlyinvoice/maxcredit |  |
| [**organisationsIdPaymentsRecurringGet_0**](OrganisationsApi.md#organisationsIdPaymentsRecurringGet_0) | **GET** /organisations/{id}/payments/recurring |  |
| [**postOrganisationsIdAddonprovidersProviderIdFeatures_0**](OrganisationsApi.md#postOrganisationsIdAddonprovidersProviderIdFeatures_0) | **POST** /organisations/{id}/addonproviders/{providerId}/features |  |
| [**postOrganisationsIdAddonprovidersProviderIdPlans_0**](OrganisationsApi.md#postOrganisationsIdAddonprovidersProviderIdPlans_0) | **POST** /organisations/{id}/addonproviders/{providerId}/plans |  |
| [**postOrganisationsIdAddonprovidersProviderIdTesters_0**](OrganisationsApi.md#postOrganisationsIdAddonprovidersProviderIdTesters_0) | **POST** /organisations/{id}/addonproviders/{providerId}/testers |  |
| [**postOrganisationsIdAddonproviders_0**](OrganisationsApi.md#postOrganisationsIdAddonproviders_0) | **POST** /organisations/{id}/addonproviders |  |
| [**postOrganisationsIdAddons_1**](OrganisationsApi.md#postOrganisationsIdAddons_1) | **POST** /organisations/{id}/addons |  |
| [**postOrganisationsIdApplicationsAppIdAddons_2**](OrganisationsApi.md#postOrganisationsIdApplicationsAppIdAddons_2) | **POST** /organisations/{id}/applications/{appId}/addons |  |
| [**postOrganisationsIdApplicationsAppIdInstances_1**](OrganisationsApi.md#postOrganisationsIdApplicationsAppIdInstances_1) | **POST** /organisations/{id}/applications/{appId}/instances |  |
| [**postOrganisationsIdApplications_1**](OrganisationsApi.md#postOrganisationsIdApplications_1) | **POST** /organisations/{id}/applications |  |
| [**postOrganisationsIdConsumers_0**](OrganisationsApi.md#postOrganisationsIdConsumers_0) | **POST** /organisations/{id}/consumers |  |
| [**postOrganisationsIdMembers_0**](OrganisationsApi.md#postOrganisationsIdMembers_0) | **POST** /organisations/{id}/members |  |
| [**postOrganisationsIdPaymentsBillings_0**](OrganisationsApi.md#postOrganisationsIdPaymentsBillings_0) | **POST** /organisations/{id}/payments/billings |  |
| [**postOrganisations_0**](OrganisationsApi.md#postOrganisations_0) | **POST** /organisations |  |
| [**putOrganisationsIdAddonprovidersProviderIdPlansPlanIdFeaturesFeatureName_0**](OrganisationsApi.md#putOrganisationsIdAddonprovidersProviderIdPlansPlanIdFeaturesFeatureName_0) | **PUT** /organisations/{id}/addonproviders/{providerId}/plans/{planId}/features/{featureName} |  |
| [**putOrganisationsIdAddonprovidersProviderIdPlansPlanId_0**](OrganisationsApi.md#putOrganisationsIdAddonprovidersProviderIdPlansPlanId_0) | **PUT** /organisations/{id}/addonproviders/{providerId}/plans/{planId} |  |
| [**putOrganisationsIdAddonprovidersProviderId_0**](OrganisationsApi.md#putOrganisationsIdAddonprovidersProviderId_0) | **PUT** /organisations/{id}/addonproviders/{providerId} |  |
| [**putOrganisationsIdAddonsAddonIdTagsTag_1**](OrganisationsApi.md#putOrganisationsIdAddonsAddonIdTagsTag_1) | **PUT** /organisations/{id}/addons/{addonId}/tags/{tag} |  |
| [**putOrganisationsIdAddonsAddonId_1**](OrganisationsApi.md#putOrganisationsIdAddonsAddonId_1) | **PUT** /organisations/{id}/addons/{addonId} |  |
| [**putOrganisationsIdApplicationsAppIdDependenciesDependencyId_1**](OrganisationsApi.md#putOrganisationsIdApplicationsAppIdDependenciesDependencyId_1) | **PUT** /organisations/{id}/applications/{appId}/dependencies/{dependencyId} |  |
| [**putOrganisationsIdApplicationsAppIdEnvEnvName_1**](OrganisationsApi.md#putOrganisationsIdApplicationsAppIdEnvEnvName_1) | **PUT** /organisations/{id}/applications/{appId}/env/{envName} |  |
| [**putOrganisationsIdApplicationsAppIdEnv_1**](OrganisationsApi.md#putOrganisationsIdApplicationsAppIdEnv_1) | **PUT** /organisations/{id}/applications/{appId}/env |  |
| [**putOrganisationsIdApplicationsAppIdTagsTag_1**](OrganisationsApi.md#putOrganisationsIdApplicationsAppIdTagsTag_1) | **PUT** /organisations/{id}/applications/{appId}/tags/{tag} |  |
| [**putOrganisationsIdApplicationsAppIdVhostsDomain_1**](OrganisationsApi.md#putOrganisationsIdApplicationsAppIdVhostsDomain_1) | **PUT** /organisations/{id}/applications/{appId}/vhosts/{domain} |  |
| [**putOrganisationsIdApplicationsAppIdVhostsFavourite_1**](OrganisationsApi.md#putOrganisationsIdApplicationsAppIdVhostsFavourite_1) | **PUT** /organisations/{id}/applications/{appId}/vhosts/favourite |  |
| [**putOrganisationsIdApplicationsAppId_1**](OrganisationsApi.md#putOrganisationsIdApplicationsAppId_1) | **PUT** /organisations/{id}/applications/{appId} |  |
| [**putOrganisationsIdAvatar_0**](OrganisationsApi.md#putOrganisationsIdAvatar_0) | **PUT** /organisations/{id}/avatar |  |
| [**putOrganisationsIdConsumersKey_0**](OrganisationsApi.md#putOrganisationsIdConsumersKey_0) | **PUT** /organisations/{id}/consumers/{key} |  |
| [**putOrganisationsIdMembersUserId_0**](OrganisationsApi.md#putOrganisationsIdMembersUserId_0) | **PUT** /organisations/{id}/members/{userId} |  |
| [**putOrganisationsIdPaymentsBillingsBid_0**](OrganisationsApi.md#putOrganisationsIdPaymentsBillingsBid_0) | **PUT** /organisations/{id}/payments/billings/{bid} |  |
| [**putOrganisationsId_0**](OrganisationsApi.md#putOrganisationsId_0) | **PUT** /organisations/{id} |  |


<a id="createNetworkGroupExternalPeer_0"></a>
# **createNetworkGroupExternalPeer_0**
> Object createNetworkGroupExternalPeer_0(ownerId, networkGroupId, body)

Add external peer

Adds an external peer to a Network Group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganisationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    OrganisationsApi apiInstance = new OrganisationsApi(defaultClient);
    String ownerId = "ownerId_example"; // String | Automatically added
    String networkGroupId = "networkGroupId_example"; // String | Automatically added
    Object body = null; // Object | 
    try {
      Object result = apiInstance.createNetworkGroupExternalPeer_0(ownerId, networkGroupId, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganisationsApi#createNetworkGroupExternalPeer_0");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **ownerId** | **String**| Automatically added | |
| **networkGroupId** | **String**| Automatically added | |
| **body** | **Object**|  | [optional] |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain; charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad Request |  -  |
| **401** |  |  -  |
| **404** |  |  -  |

<a id="createNetworkGroupMember_0"></a>
# **createNetworkGroupMember_0**
> createNetworkGroupMember_0(ownerId, networkGroupId, schema2)

Add member

Adds a member to a Network Group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganisationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    OrganisationsApi apiInstance = new OrganisationsApi(defaultClient);
    String ownerId = "ownerId_example"; // String | Automatically added
    String networkGroupId = "networkGroupId_example"; // String | Automatically added
    Schema2 schema2 = new Schema2(); // Schema2 | 
    try {
      apiInstance.createNetworkGroupMember_0(ownerId, networkGroupId, schema2);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganisationsApi#createNetworkGroupMember_0");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **ownerId** | **String**| Automatically added | |
| **networkGroupId** | **String**| Automatically added | |
| **schema2** | [**Schema2**](Schema2.md)|  | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** |  |  -  |
| **400** |  |  -  |
| **401** |  |  -  |
| **404** |  |  -  |

<a id="createNetworkGroup_0"></a>
# **createNetworkGroup_0**
> Object createNetworkGroup_0(ownerId, body)

Create Network Group

Creates a Network Group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganisationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    OrganisationsApi apiInstance = new OrganisationsApi(defaultClient);
    String ownerId = "ownerId_example"; // String | Automatically added
    Object body = null; // Object | 
    try {
      Object result = apiInstance.createNetworkGroup_0(ownerId, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganisationsApi#createNetworkGroup_0");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **ownerId** | **String**| Automatically added | |
| **body** | **Object**|  | [optional] |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain; charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Success |  -  |
| **400** |  |  -  |
| **401** |  |  -  |
| **409** | Conflict |  -  |

<a id="deleteNetworkGroupExternalPeer_0"></a>
# **deleteNetworkGroupExternalPeer_0**
> deleteNetworkGroupExternalPeer_0(ownerId, networkGroupId, peerId, body)

Remove external peer

Removes an external peer from a Network Group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganisationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    OrganisationsApi apiInstance = new OrganisationsApi(defaultClient);
    String ownerId = "ownerId_example"; // String | Automatically added
    String networkGroupId = "networkGroupId_example"; // String | Automatically added
    String peerId = "peerId_example"; // String | Automatically added
    Object body = null; // Object | 
    try {
      apiInstance.deleteNetworkGroupExternalPeer_0(ownerId, networkGroupId, peerId, body);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganisationsApi#deleteNetworkGroupExternalPeer_0");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **ownerId** | **String**| Automatically added | |
| **networkGroupId** | **String**| Automatically added | |
| **peerId** | **String**| Automatically added | |
| **body** | **Object**|  | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |
| **401** |  |  -  |

<a id="deleteNetworkGroupMember_0"></a>
# **deleteNetworkGroupMember_0**
> deleteNetworkGroupMember_0(ownerId, networkGroupId, memberId, body)

Remove member

Removes a member from a Network Group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganisationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    OrganisationsApi apiInstance = new OrganisationsApi(defaultClient);
    String ownerId = "ownerId_example"; // String | Automatically added
    String networkGroupId = "networkGroupId_example"; // String | Automatically added
    String memberId = "memberId_example"; // String | Automatically added
    Object body = null; // Object | 
    try {
      apiInstance.deleteNetworkGroupMember_0(ownerId, networkGroupId, memberId, body);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganisationsApi#deleteNetworkGroupMember_0");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **ownerId** | **String**| Automatically added | |
| **networkGroupId** | **String**| Automatically added | |
| **memberId** | **String**| Automatically added | |
| **body** | **Object**|  | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |
| **401** |  |  -  |

<a id="deleteNetworkGroupPeer_0"></a>
# **deleteNetworkGroupPeer_0**
> deleteNetworkGroupPeer_0(ownerId, networkGroupId, peerId, body)

Remove peer

Removes a peer from a Network Group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganisationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    OrganisationsApi apiInstance = new OrganisationsApi(defaultClient);
    String ownerId = "ownerId_example"; // String | Automatically added
    String networkGroupId = "networkGroupId_example"; // String | Automatically added
    String peerId = "peerId_example"; // String | Automatically added
    Object body = null; // Object | 
    try {
      apiInstance.deleteNetworkGroupPeer_0(ownerId, networkGroupId, peerId, body);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganisationsApi#deleteNetworkGroupPeer_0");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **ownerId** | **String**| Automatically added | |
| **networkGroupId** | **String**| Automatically added | |
| **peerId** | **String**| Automatically added | |
| **body** | **Object**|  | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |
| **401** |  |  -  |

<a id="deleteNetworkGroup_0"></a>
# **deleteNetworkGroup_0**
> deleteNetworkGroup_0(ownerId, networkGroupId, body)

Delete Network Group

Deletes a Network Group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganisationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    OrganisationsApi apiInstance = new OrganisationsApi(defaultClient);
    String ownerId = "ownerId_example"; // String | Automatically added
    String networkGroupId = "networkGroupId_example"; // String | Automatically added
    Object body = null; // Object | 
    try {
      apiInstance.deleteNetworkGroup_0(ownerId, networkGroupId, body);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganisationsApi#deleteNetworkGroup_0");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **ownerId** | **String**| Automatically added | |
| **networkGroupId** | **String**| Automatically added | |
| **body** | **Object**|  | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |
| **401** |  |  -  |
| **404** |  |  -  |

<a id="deleteOrganisationsIdAddonprovidersProviderIdFeaturesFeatureId_0"></a>
# **deleteOrganisationsIdAddonprovidersProviderIdFeaturesFeatureId_0**
> deleteOrganisationsIdAddonprovidersProviderIdFeaturesFeatureId_0(id, featureId, providerId)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganisationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    OrganisationsApi apiInstance = new OrganisationsApi(defaultClient);
    String id = "id_example"; // String | 
    String featureId = "featureId_example"; // String | 
    String providerId = "providerId_example"; // String | 
    try {
      apiInstance.deleteOrganisationsIdAddonprovidersProviderIdFeaturesFeatureId_0(id, featureId, providerId);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganisationsApi#deleteOrganisationsIdAddonprovidersProviderIdFeaturesFeatureId_0");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**|  | |
| **featureId** | **String**|  | |
| **providerId** | **String**|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | deleteProviderFeature |  -  |

<a id="deleteOrganisationsIdAddonprovidersProviderIdPlansPlanIdFeaturesFeatureName_0"></a>
# **deleteOrganisationsIdAddonprovidersProviderIdPlansPlanIdFeaturesFeatureName_0**
> deleteOrganisationsIdAddonprovidersProviderIdPlansPlanIdFeaturesFeatureName_0(id, featureName, providerId, planId)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganisationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    OrganisationsApi apiInstance = new OrganisationsApi(defaultClient);
    String id = "id_example"; // String | 
    String featureName = "featureName_example"; // String | 
    String providerId = "providerId_example"; // String | 
    String planId = "planId_example"; // String | 
    try {
      apiInstance.deleteOrganisationsIdAddonprovidersProviderIdPlansPlanIdFeaturesFeatureName_0(id, featureName, providerId, planId);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganisationsApi#deleteOrganisationsIdAddonprovidersProviderIdPlansPlanIdFeaturesFeatureName_0");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**|  | |
| **featureName** | **String**|  | |
| **providerId** | **String**|  | |
| **planId** | **String**|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | deleteProviderPlanFeature |  -  |

<a id="deleteOrganisationsIdAddonprovidersProviderIdPlansPlanId_0"></a>
# **deleteOrganisationsIdAddonprovidersProviderIdPlansPlanId_0**
> deleteOrganisationsIdAddonprovidersProviderIdPlansPlanId_0(id, providerId, planId)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganisationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    OrganisationsApi apiInstance = new OrganisationsApi(defaultClient);
    String id = "id_example"; // String | 
    String providerId = "providerId_example"; // String | 
    String planId = "planId_example"; // String | 
    try {
      apiInstance.deleteOrganisationsIdAddonprovidersProviderIdPlansPlanId_0(id, providerId, planId);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganisationsApi#deleteOrganisationsIdAddonprovidersProviderIdPlansPlanId_0");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**|  | |
| **providerId** | **String**|  | |
| **planId** | **String**|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | deleteProviderPlan |  -  |

<a id="deleteOrganisationsIdAddonsAddonIdTagsTag_1"></a>
# **deleteOrganisationsIdAddonsAddonIdTagsTag_1**
> deleteOrganisationsIdAddonsAddonIdTagsTag_1(id, tag, addonId)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganisationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    OrganisationsApi apiInstance = new OrganisationsApi(defaultClient);
    String id = "id_example"; // String | 
    String tag = "tag_example"; // String | 
    String addonId = "addonId_example"; // String | 
    try {
      apiInstance.deleteOrganisationsIdAddonsAddonIdTagsTag_1(id, tag, addonId);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganisationsApi#deleteOrganisationsIdAddonsAddonIdTagsTag_1");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**|  | |
| **tag** | **String**|  | |
| **addonId** | **String**|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | deleteAddonTag |  -  |

<a id="deleteOrganisationsIdAddonsAddonId_1"></a>
# **deleteOrganisationsIdAddonsAddonId_1**
> deleteOrganisationsIdAddonsAddonId_1(id, addonId)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganisationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    OrganisationsApi apiInstance = new OrganisationsApi(defaultClient);
    String id = "id_example"; // String | 
    String addonId = "addonId_example"; // String | 
    try {
      apiInstance.deleteOrganisationsIdAddonsAddonId_1(id, addonId);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganisationsApi#deleteOrganisationsIdAddonsAddonId_1");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**|  | |
| **addonId** | **String**|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | deprovisionAddon |  -  |

<a id="deleteOrganisationsIdApplicationsAppIdAddonsAddonId_2"></a>
# **deleteOrganisationsIdApplicationsAppIdAddonsAddonId_2**
> deleteOrganisationsIdApplicationsAppIdAddonsAddonId_2(id, appId, addonId)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganisationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    OrganisationsApi apiInstance = new OrganisationsApi(defaultClient);
    String id = "id_example"; // String | 
    String appId = "appId_example"; // String | 
    String addonId = "addonId_example"; // String | 
    try {
      apiInstance.deleteOrganisationsIdApplicationsAppIdAddonsAddonId_2(id, appId, addonId);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganisationsApi#deleteOrganisationsIdApplicationsAppIdAddonsAddonId_2");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**|  | |
| **appId** | **String**|  | |
| **addonId** | **String**|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | unlinkAddonFromApplication |  -  |

<a id="deleteOrganisationsIdApplicationsAppIdDependenciesDependencyId_1"></a>
# **deleteOrganisationsIdApplicationsAppIdDependenciesDependencyId_1**
> deleteOrganisationsIdApplicationsAppIdDependenciesDependencyId_1(dependencyId, appId, id)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganisationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    OrganisationsApi apiInstance = new OrganisationsApi(defaultClient);
    String dependencyId = "dependencyId_example"; // String | 
    String appId = "appId_example"; // String | 
    String id = "id_example"; // String | 
    try {
      apiInstance.deleteOrganisationsIdApplicationsAppIdDependenciesDependencyId_1(dependencyId, appId, id);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganisationsApi#deleteOrganisationsIdApplicationsAppIdDependenciesDependencyId_1");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **dependencyId** | **String**|  | |
| **appId** | **String**|  | |
| **id** | **String**|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | deleteApplicationDependency |  -  |

<a id="deleteOrganisationsIdApplicationsAppIdDeploymentsDeploymentIdInstances_1"></a>
# **deleteOrganisationsIdApplicationsAppIdDeploymentsDeploymentIdInstances_1**
> deleteOrganisationsIdApplicationsAppIdDeploymentsDeploymentIdInstances_1(id, appId, deploymentId)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganisationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    OrganisationsApi apiInstance = new OrganisationsApi(defaultClient);
    String id = "id_example"; // String | 
    String appId = "appId_example"; // String | 
    String deploymentId = "deploymentId_example"; // String | 
    try {
      apiInstance.deleteOrganisationsIdApplicationsAppIdDeploymentsDeploymentIdInstances_1(id, appId, deploymentId);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganisationsApi#deleteOrganisationsIdApplicationsAppIdDeploymentsDeploymentIdInstances_1");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**|  | |
| **appId** | **String**|  | |
| **deploymentId** | **String**|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | getApplicationDeploymentsForOrga |  -  |

<a id="deleteOrganisationsIdApplicationsAppIdEnvEnvName_1"></a>
# **deleteOrganisationsIdApplicationsAppIdEnvEnvName_1**
> deleteOrganisationsIdApplicationsAppIdEnvEnvName_1(id, appId, envName)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganisationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    OrganisationsApi apiInstance = new OrganisationsApi(defaultClient);
    String id = "id_example"; // String | 
    String appId = "appId_example"; // String | 
    String envName = "envName_example"; // String | 
    try {
      apiInstance.deleteOrganisationsIdApplicationsAppIdEnvEnvName_1(id, appId, envName);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganisationsApi#deleteOrganisationsIdApplicationsAppIdEnvEnvName_1");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**|  | |
| **appId** | **String**|  | |
| **envName** | **String**|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | removeApplicationEnv |  -  |

<a id="deleteOrganisationsIdApplicationsAppIdInstances_1"></a>
# **deleteOrganisationsIdApplicationsAppIdInstances_1**
> deleteOrganisationsIdApplicationsAppIdInstances_1(id, appId)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganisationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    OrganisationsApi apiInstance = new OrganisationsApi(defaultClient);
    String id = "id_example"; // String | 
    String appId = "appId_example"; // String | 
    try {
      apiInstance.deleteOrganisationsIdApplicationsAppIdInstances_1(id, appId);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganisationsApi#deleteOrganisationsIdApplicationsAppIdInstances_1");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**|  | |
| **appId** | **String**|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | undeployApplication |  -  |

<a id="deleteOrganisationsIdApplicationsAppIdTagsTag_1"></a>
# **deleteOrganisationsIdApplicationsAppIdTagsTag_1**
> deleteOrganisationsIdApplicationsAppIdTagsTag_1(id, appId, tag)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganisationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    OrganisationsApi apiInstance = new OrganisationsApi(defaultClient);
    String id = "id_example"; // String | 
    String appId = "appId_example"; // String | 
    String tag = "tag_example"; // String | 
    try {
      apiInstance.deleteOrganisationsIdApplicationsAppIdTagsTag_1(id, appId, tag);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganisationsApi#deleteOrganisationsIdApplicationsAppIdTagsTag_1");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**|  | |
| **appId** | **String**|  | |
| **tag** | **String**|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | deleteApplicationTag |  -  |

<a id="deleteOrganisationsIdApplicationsAppIdVhostsDomain_1"></a>
# **deleteOrganisationsIdApplicationsAppIdVhostsDomain_1**
> deleteOrganisationsIdApplicationsAppIdVhostsDomain_1(id, appId, domain)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganisationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    OrganisationsApi apiInstance = new OrganisationsApi(defaultClient);
    String id = "id_example"; // String | 
    String appId = "appId_example"; // String | 
    String domain = "domain_example"; // String | 
    try {
      apiInstance.deleteOrganisationsIdApplicationsAppIdVhostsDomain_1(id, appId, domain);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganisationsApi#deleteOrganisationsIdApplicationsAppIdVhostsDomain_1");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**|  | |
| **appId** | **String**|  | |
| **domain** | **String**|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | removeVhost |  -  |

<a id="deleteOrganisationsIdApplicationsAppIdVhostsFavourite_1"></a>
# **deleteOrganisationsIdApplicationsAppIdVhostsFavourite_1**
> deleteOrganisationsIdApplicationsAppIdVhostsFavourite_1(id, appId)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganisationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    OrganisationsApi apiInstance = new OrganisationsApi(defaultClient);
    String id = "id_example"; // String | 
    String appId = "appId_example"; // String | 
    try {
      apiInstance.deleteOrganisationsIdApplicationsAppIdVhostsFavourite_1(id, appId);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganisationsApi#deleteOrganisationsIdApplicationsAppIdVhostsFavourite_1");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**|  | |
| **appId** | **String**|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | unmarkFavouriteVhost |  -  |

<a id="deleteOrganisationsIdApplicationsAppId_1"></a>
# **deleteOrganisationsIdApplicationsAppId_1**
> deleteOrganisationsIdApplicationsAppId_1(id, appId)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganisationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    OrganisationsApi apiInstance = new OrganisationsApi(defaultClient);
    String id = "id_example"; // String | 
    String appId = "appId_example"; // String | 
    try {
      apiInstance.deleteOrganisationsIdApplicationsAppId_1(id, appId);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganisationsApi#deleteOrganisationsIdApplicationsAppId_1");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**|  | |
| **appId** | **String**|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | deleteApplication |  -  |

<a id="deleteOrganisationsIdConsumersKey_0"></a>
# **deleteOrganisationsIdConsumersKey_0**
> deleteOrganisationsIdConsumersKey_0(id, key)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganisationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    OrganisationsApi apiInstance = new OrganisationsApi(defaultClient);
    String id = "id_example"; // String | 
    String key = "key_example"; // String | 
    try {
      apiInstance.deleteOrganisationsIdConsumersKey_0(id, key);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganisationsApi#deleteOrganisationsIdConsumersKey_0");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**|  | |
| **key** | **String**|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | deleteConsumer |  -  |

<a id="deleteOrganisationsIdMembersUserId_0"></a>
# **deleteOrganisationsIdMembersUserId_0**
> deleteOrganisationsIdMembersUserId_0(id, userId)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganisationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    OrganisationsApi apiInstance = new OrganisationsApi(defaultClient);
    String id = "id_example"; // String | 
    String userId = "userId_example"; // String | 
    try {
      apiInstance.deleteOrganisationsIdMembersUserId_0(id, userId);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganisationsApi#deleteOrganisationsIdMembersUserId_0");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**|  | |
| **userId** | **String**|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | removeOrganisationMember |  -  |

<a id="deleteOrganisationsIdPaymentsBillingsBid_0"></a>
# **deleteOrganisationsIdPaymentsBillingsBid_0**
> deleteOrganisationsIdPaymentsBillingsBid_0(id, bid)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganisationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    OrganisationsApi apiInstance = new OrganisationsApi(defaultClient);
    String id = "id_example"; // String | 
    String bid = "bid_example"; // String | 
    try {
      apiInstance.deleteOrganisationsIdPaymentsBillingsBid_0(id, bid);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganisationsApi#deleteOrganisationsIdPaymentsBillingsBid_0");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**|  | |
| **bid** | **String**|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | deletePurchaseOrder |  -  |

<a id="deleteOrganisationsIdPaymentsRecurring_0"></a>
# **deleteOrganisationsIdPaymentsRecurring_0**
> deleteOrganisationsIdPaymentsRecurring_0(id)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganisationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    OrganisationsApi apiInstance = new OrganisationsApi(defaultClient);
    String id = "id_example"; // String | 
    try {
      apiInstance.deleteOrganisationsIdPaymentsRecurring_0(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganisationsApi#deleteOrganisationsIdPaymentsRecurring_0");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | deleteRecurrentPayment |  -  |

<a id="deleteOrganisationsId_0"></a>
# **deleteOrganisationsId_0**
> deleteOrganisationsId_0(id)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganisationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    OrganisationsApi apiInstance = new OrganisationsApi(defaultClient);
    String id = "id_example"; // String | 
    try {
      apiInstance.deleteOrganisationsId_0(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganisationsApi#deleteOrganisationsId_0");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | deleteOrganisation |  -  |

<a id="getNetworkGroupMember_0"></a>
# **getNetworkGroupMember_0**
> Schema1 getNetworkGroupMember_0(ownerId, networkGroupId, memberId, body)

Get member

Gets details of a Network Group member.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganisationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    OrganisationsApi apiInstance = new OrganisationsApi(defaultClient);
    String ownerId = "ownerId_example"; // String | Automatically added
    String networkGroupId = "networkGroupId_example"; // String | Automatically added
    String memberId = "memberId_example"; // String | Automatically added
    Object body = null; // Object | 
    try {
      Schema1 result = apiInstance.getNetworkGroupMember_0(ownerId, networkGroupId, memberId, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganisationsApi#getNetworkGroupMember_0");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **ownerId** | **String**| Automatically added | |
| **networkGroupId** | **String**| Automatically added | |
| **memberId** | **String**| Automatically added | |
| **body** | **Object**|  | [optional] |

### Return type

[**Schema1**](Schema1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **401** |  |  -  |
| **404** |  |  -  |

<a id="getNetworkGroupPeer_0"></a>
# **getNetworkGroupPeer_0**
> Object getNetworkGroupPeer_0(ownerId, networkGroupId, peerId, body)

Get peer

Gets details of a Network Group peer.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganisationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    OrganisationsApi apiInstance = new OrganisationsApi(defaultClient);
    String ownerId = "ownerId_example"; // String | Automatically added
    String networkGroupId = "networkGroupId_example"; // String | Automatically added
    String peerId = "peerId_example"; // String | Automatically added
    Object body = null; // Object | 
    try {
      Object result = apiInstance.getNetworkGroupPeer_0(ownerId, networkGroupId, peerId, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganisationsApi#getNetworkGroupPeer_0");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **ownerId** | **String**| Automatically added | |
| **networkGroupId** | **String**| Automatically added | |
| **peerId** | **String**| Automatically added | |
| **body** | **Object**|  | [optional] |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **401** |  |  -  |
| **404** |  |  -  |

<a id="getNetworkGroupStream_0"></a>
# **getNetworkGroupStream_0**
> Object getNetworkGroupStream_0(ownerId, networkGroupId, body)

Network Group SSE

Retrieves the current Network Group details as a Server Sent Event.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganisationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    OrganisationsApi apiInstance = new OrganisationsApi(defaultClient);
    String ownerId = "ownerId_example"; // String | Automatically added
    String networkGroupId = "networkGroupId_example"; // String | Automatically added
    Object body = null; // Object | 
    try {
      Object result = apiInstance.getNetworkGroupStream_0(ownerId, networkGroupId, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganisationsApi#getNetworkGroupStream_0");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **ownerId** | **String**| Automatically added | |
| **networkGroupId** | **String**| Automatically added | |
| **body** | **Object**|  | [optional] |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/event-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **401** |  |  -  |
| **404** |  |  -  |

<a id="getNetworkGroupWireGuardConfigurationStream_0"></a>
# **getNetworkGroupWireGuardConfigurationStream_0**
> Object getNetworkGroupWireGuardConfigurationStream_0(ownerId, networkGroupId, peerId, body)

Get WireGuard® configuration

Gets the current WireGuard® tunnel configuration file for a Network Group peer as a Server Sent Event.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganisationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    OrganisationsApi apiInstance = new OrganisationsApi(defaultClient);
    String ownerId = "ownerId_example"; // String | Automatically added
    String networkGroupId = "networkGroupId_example"; // String | Automatically added
    String peerId = "peerId_example"; // String | Automatically added
    Object body = null; // Object | 
    try {
      Object result = apiInstance.getNetworkGroupWireGuardConfigurationStream_0(ownerId, networkGroupId, peerId, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganisationsApi#getNetworkGroupWireGuardConfigurationStream_0");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **ownerId** | **String**| Automatically added | |
| **networkGroupId** | **String**| Automatically added | |
| **peerId** | **String**| Automatically added | |
| **body** | **Object**|  | [optional] |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/event-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **401** |  |  -  |
| **404** |  |  -  |

<a id="getNetworkGroupWireGuardConfiguration_0"></a>
# **getNetworkGroupWireGuardConfiguration_0**
> Object getNetworkGroupWireGuardConfiguration_0(ownerId, networkGroupId, peerId, body)

Get WireGuard® configuration

Gets the current WireGuard® tunnel configuration file for a Network Group peer.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganisationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    OrganisationsApi apiInstance = new OrganisationsApi(defaultClient);
    String ownerId = "ownerId_example"; // String | Automatically added
    String networkGroupId = "networkGroupId_example"; // String | Automatically added
    String peerId = "peerId_example"; // String | Automatically added
    Object body = null; // Object | 
    try {
      Object result = apiInstance.getNetworkGroupWireGuardConfiguration_0(ownerId, networkGroupId, peerId, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganisationsApi#getNetworkGroupWireGuardConfiguration_0");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **ownerId** | **String**| Automatically added | |
| **networkGroupId** | **String**| Automatically added | |
| **peerId** | **String**| Automatically added | |
| **body** | **Object**|  | [optional] |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **401** |  |  -  |
| **404** |  |  -  |

<a id="getNetworkGroup_0"></a>
# **getNetworkGroup_0**
> Object getNetworkGroup_0(ownerId, networkGroupId, body)

Get Network Group

Gets details of a Network Group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganisationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    OrganisationsApi apiInstance = new OrganisationsApi(defaultClient);
    String ownerId = "ownerId_example"; // String | Automatically added
    String networkGroupId = "networkGroupId_example"; // String | Automatically added
    Object body = null; // Object | 
    try {
      Object result = apiInstance.getNetworkGroup_0(ownerId, networkGroupId, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganisationsApi#getNetworkGroup_0");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **ownerId** | **String**| Automatically added | |
| **networkGroupId** | **String**| Automatically added | |
| **body** | **Object**|  | [optional] |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **401** |  |  -  |
| **404** |  |  -  |

<a id="getOrganisationsIdAddonprovidersProviderIdFeatures_0"></a>
# **getOrganisationsIdAddonprovidersProviderIdFeatures_0**
> List&lt;Feature&gt; getOrganisationsIdAddonprovidersProviderIdFeatures_0(id, providerId)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganisationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    OrganisationsApi apiInstance = new OrganisationsApi(defaultClient);
    String id = "id_example"; // String | 
    String providerId = "providerId_example"; // String | 
    try {
      List<Feature> result = apiInstance.getOrganisationsIdAddonprovidersProviderIdFeatures_0(id, providerId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganisationsApi#getOrganisationsIdAddonprovidersProviderIdFeatures_0");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**|  | |
| **providerId** | **String**|  | |

### Return type

[**List&lt;Feature&gt;**](Feature.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | getProviderFeatures |  -  |

<a id="getOrganisationsIdAddonprovidersProviderIdPlansPlanId_0"></a>
# **getOrganisationsIdAddonprovidersProviderIdPlansPlanId_0**
> Plan getOrganisationsIdAddonprovidersProviderIdPlansPlanId_0(id, providerId, planId)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganisationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    OrganisationsApi apiInstance = new OrganisationsApi(defaultClient);
    String id = "id_example"; // String | 
    String providerId = "providerId_example"; // String | 
    String planId = "planId_example"; // String | 
    try {
      Plan result = apiInstance.getOrganisationsIdAddonprovidersProviderIdPlansPlanId_0(id, providerId, planId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganisationsApi#getOrganisationsIdAddonprovidersProviderIdPlansPlanId_0");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**|  | |
| **providerId** | **String**|  | |
| **planId** | **String**|  | |

### Return type

[**Plan**](Plan.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | getProviderPlan |  -  |

<a id="getOrganisationsIdAddonprovidersProviderIdPlans_0"></a>
# **getOrganisationsIdAddonprovidersProviderIdPlans_0**
> List&lt;Plan&gt; getOrganisationsIdAddonprovidersProviderIdPlans_0(id, providerId)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganisationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    OrganisationsApi apiInstance = new OrganisationsApi(defaultClient);
    String id = "id_example"; // String | 
    String providerId = "providerId_example"; // String | 
    try {
      List<Plan> result = apiInstance.getOrganisationsIdAddonprovidersProviderIdPlans_0(id, providerId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganisationsApi#getOrganisationsIdAddonprovidersProviderIdPlans_0");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**|  | |
| **providerId** | **String**|  | |

### Return type

[**List&lt;Plan&gt;**](Plan.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | getProviderPlans |  -  |

<a id="getOrganisationsIdAddonprovidersProviderIdTags_0"></a>
# **getOrganisationsIdAddonprovidersProviderIdTags_0**
> List&lt;String&gt; getOrganisationsIdAddonprovidersProviderIdTags_0(id, providerId)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganisationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    OrganisationsApi apiInstance = new OrganisationsApi(defaultClient);
    String id = "id_example"; // String | 
    String providerId = "providerId_example"; // String | 
    try {
      List<String> result = apiInstance.getOrganisationsIdAddonprovidersProviderIdTags_0(id, providerId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganisationsApi#getOrganisationsIdAddonprovidersProviderIdTags_0");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**|  | |
| **providerId** | **String**|  | |

### Return type

**List&lt;String&gt;**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | getProviderTags |  -  |

<a id="getOrganisationsIdAddonprovidersProviderId_0"></a>
# **getOrganisationsIdAddonprovidersProviderId_0**
> Provider getOrganisationsIdAddonprovidersProviderId_0(id, providerId)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganisationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    OrganisationsApi apiInstance = new OrganisationsApi(defaultClient);
    String id = "id_example"; // String | 
    String providerId = "providerId_example"; // String | 
    try {
      Provider result = apiInstance.getOrganisationsIdAddonprovidersProviderId_0(id, providerId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganisationsApi#getOrganisationsIdAddonprovidersProviderId_0");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**|  | |
| **providerId** | **String**|  | |

### Return type

[**Provider**](Provider.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Get all informations about given provider. |  -  |

<a id="getOrganisationsIdAddonproviders_0"></a>
# **getOrganisationsIdAddonproviders_0**
> List&lt;Provider&gt; getOrganisationsIdAddonproviders_0(id)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganisationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    OrganisationsApi apiInstance = new OrganisationsApi(defaultClient);
    String id = "id_example"; // String | 
    try {
      List<Provider> result = apiInstance.getOrganisationsIdAddonproviders_0(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganisationsApi#getOrganisationsIdAddonproviders_0");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**|  | |

### Return type

[**List&lt;Provider&gt;**](Provider.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Get all informations about all providers. |  -  |

<a id="getOrganisationsIdAddonsAddonIdApplications_2"></a>
# **getOrganisationsIdAddonsAddonIdApplications_2**
> List&lt;Application&gt; getOrganisationsIdAddonsAddonIdApplications_2(id, addonId)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganisationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    OrganisationsApi apiInstance = new OrganisationsApi(defaultClient);
    String id = "id_example"; // String | 
    String addonId = "addonId_example"; // String | 
    try {
      List<Application> result = apiInstance.getOrganisationsIdAddonsAddonIdApplications_2(id, addonId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganisationsApi#getOrganisationsIdAddonsAddonIdApplications_2");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**|  | |
| **addonId** | **String**|  | |

### Return type

[**List&lt;Application&gt;**](Application.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | getApplicationsLinkedToAddon |  -  |

<a id="getOrganisationsIdAddonsAddonIdEnv_1"></a>
# **getOrganisationsIdAddonsAddonIdEnv_1**
> List&lt;ListEnv&gt; getOrganisationsIdAddonsAddonIdEnv_1(id, addonId)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganisationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    OrganisationsApi apiInstance = new OrganisationsApi(defaultClient);
    String id = "id_example"; // String | 
    String addonId = "addonId_example"; // String | 
    try {
      List<ListEnv> result = apiInstance.getOrganisationsIdAddonsAddonIdEnv_1(id, addonId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganisationsApi#getOrganisationsIdAddonsAddonIdEnv_1");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**|  | |
| **addonId** | **String**|  | |

### Return type

[**List&lt;ListEnv&gt;**](ListEnv.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | getAddonEnv |  -  |

<a id="getOrganisationsIdAddonsAddonIdSso_0"></a>
# **getOrganisationsIdAddonsAddonIdSso_0**
> AddonProviderSso getOrganisationsIdAddonsAddonIdSso_0(providerId, id)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganisationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    OrganisationsApi apiInstance = new OrganisationsApi(defaultClient);
    String providerId = "providerId_example"; // String | 
    String id = "id_example"; // String | 
    try {
      AddonProviderSso result = apiInstance.getOrganisationsIdAddonsAddonIdSso_0(providerId, id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganisationsApi#getOrganisationsIdAddonsAddonIdSso_0");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **providerId** | **String**|  | |
| **id** | **String**|  | |

### Return type

[**AddonProviderSso**](AddonProviderSso.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | getSSOData |  -  |

<a id="getOrganisationsIdAddonsAddonIdTags_1"></a>
# **getOrganisationsIdAddonsAddonIdTags_1**
> List&lt;String&gt; getOrganisationsIdAddonsAddonIdTags_1(id, addonId)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganisationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    OrganisationsApi apiInstance = new OrganisationsApi(defaultClient);
    String id = "id_example"; // String | 
    String addonId = "addonId_example"; // String | 
    try {
      List<String> result = apiInstance.getOrganisationsIdAddonsAddonIdTags_1(id, addonId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganisationsApi#getOrganisationsIdAddonsAddonIdTags_1");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**|  | |
| **addonId** | **String**|  | |

### Return type

**List&lt;String&gt;**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | getAddonTags |  -  |

<a id="getOrganisationsIdAddonsAddonId_1"></a>
# **getOrganisationsIdAddonsAddonId_1**
> Addon getOrganisationsIdAddonsAddonId_1(id, addonId)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganisationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    OrganisationsApi apiInstance = new OrganisationsApi(defaultClient);
    String id = "id_example"; // String | 
    String addonId = "addonId_example"; // String | 
    try {
      Addon result = apiInstance.getOrganisationsIdAddonsAddonId_1(id, addonId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganisationsApi#getOrganisationsIdAddonsAddonId_1");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**|  | |
| **addonId** | **String**|  | |

### Return type

[**Addon**](Addon.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | getAddon |  -  |

<a id="getOrganisationsIdAddons_1"></a>
# **getOrganisationsIdAddons_1**
> List&lt;Addon&gt; getOrganisationsIdAddons_1(id)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganisationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    OrganisationsApi apiInstance = new OrganisationsApi(defaultClient);
    String id = "id_example"; // String | 
    try {
      List<Addon> result = apiInstance.getOrganisationsIdAddons_1(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganisationsApi#getOrganisationsIdAddons_1");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**|  | |

### Return type

[**List&lt;Addon&gt;**](Addon.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | getAddons |  -  |

<a id="getOrganisationsIdApplicationsAppIdAddonsEnv_2"></a>
# **getOrganisationsIdApplicationsAppIdAddonsEnv_2**
> List&lt;Env&gt; getOrganisationsIdApplicationsAppIdAddonsEnv_2(id, appId)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganisationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    OrganisationsApi apiInstance = new OrganisationsApi(defaultClient);
    String id = "id_example"; // String | 
    String appId = "appId_example"; // String | 
    try {
      List<Env> result = apiInstance.getOrganisationsIdApplicationsAppIdAddonsEnv_2(id, appId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganisationsApi#getOrganisationsIdApplicationsAppIdAddonsEnv_2");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**|  | |
| **appId** | **String**|  | |

### Return type

[**List&lt;Env&gt;**](Env.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | getEnvOfAddonsLinkedToApplication |  -  |

<a id="getOrganisationsIdApplicationsAppIdAddons_2"></a>
# **getOrganisationsIdApplicationsAppIdAddons_2**
> List&lt;Addon&gt; getOrganisationsIdApplicationsAppIdAddons_2(id, appId)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganisationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    OrganisationsApi apiInstance = new OrganisationsApi(defaultClient);
    String id = "id_example"; // String | 
    String appId = "appId_example"; // String | 
    try {
      List<Addon> result = apiInstance.getOrganisationsIdApplicationsAppIdAddons_2(id, appId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganisationsApi#getOrganisationsIdApplicationsAppIdAddons_2");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**|  | |
| **appId** | **String**|  | |

### Return type

[**List&lt;Addon&gt;**](Addon.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | getAddonsLinkedToApplication |  -  |

<a id="getOrganisationsIdApplicationsAppIdDependencies_1"></a>
# **getOrganisationsIdApplicationsAppIdDependencies_1**
> List&lt;Application&gt; getOrganisationsIdApplicationsAppIdDependencies_1(appId, id)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganisationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    OrganisationsApi apiInstance = new OrganisationsApi(defaultClient);
    String appId = "appId_example"; // String | 
    String id = "id_example"; // String | 
    try {
      List<Application> result = apiInstance.getOrganisationsIdApplicationsAppIdDependencies_1(appId, id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganisationsApi#getOrganisationsIdApplicationsAppIdDependencies_1");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **appId** | **String**|  | |
| **id** | **String**|  | |

### Return type

[**List&lt;Application&gt;**](Application.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | getApplicationDependencies |  -  |

<a id="getOrganisationsIdApplicationsAppIdDependents_1"></a>
# **getOrganisationsIdApplicationsAppIdDependents_1**
> List&lt;Application&gt; getOrganisationsIdApplicationsAppIdDependents_1(appId, id)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganisationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    OrganisationsApi apiInstance = new OrganisationsApi(defaultClient);
    String appId = "appId_example"; // String | 
    String id = "id_example"; // String | 
    try {
      List<Application> result = apiInstance.getOrganisationsIdApplicationsAppIdDependents_1(appId, id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganisationsApi#getOrganisationsIdApplicationsAppIdDependents_1");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **appId** | **String**|  | |
| **id** | **String**|  | |

### Return type

[**List&lt;Application&gt;**](Application.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | getApplicationDependents |  -  |

<a id="getOrganisationsIdApplicationsAppIdDeployments_1"></a>
# **getOrganisationsIdApplicationsAppIdDeployments_1**
> List&lt;Deployment&gt; getOrganisationsIdApplicationsAppIdDeployments_1(id, appId, limit, offset, action)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganisationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    OrganisationsApi apiInstance = new OrganisationsApi(defaultClient);
    String id = "id_example"; // String | 
    String appId = "appId_example"; // String | 
    String limit = "limit_example"; // String | 
    String offset = "offset_example"; // String | 
    String action = "action_example"; // String | 
    try {
      List<Deployment> result = apiInstance.getOrganisationsIdApplicationsAppIdDeployments_1(id, appId, limit, offset, action);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganisationsApi#getOrganisationsIdApplicationsAppIdDeployments_1");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**|  | |
| **appId** | **String**|  | |
| **limit** | **String**|  | [optional] |
| **offset** | **String**|  | [optional] |
| **action** | **String**|  | [optional] |

### Return type

[**List&lt;Deployment&gt;**](Deployment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | getApplicationDeploymentsForOrga |  -  |

<a id="getOrganisationsIdApplicationsAppIdEnv_1"></a>
# **getOrganisationsIdApplicationsAppIdEnv_1**
> List&lt;ListEnv&gt; getOrganisationsIdApplicationsAppIdEnv_1(id, appId)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganisationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    OrganisationsApi apiInstance = new OrganisationsApi(defaultClient);
    String id = "id_example"; // String | 
    String appId = "appId_example"; // String | 
    try {
      List<ListEnv> result = apiInstance.getOrganisationsIdApplicationsAppIdEnv_1(id, appId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganisationsApi#getOrganisationsIdApplicationsAppIdEnv_1");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**|  | |
| **appId** | **String**|  | |

### Return type

[**List&lt;ListEnv&gt;**](ListEnv.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | getApplicationEnv |  -  |

<a id="getOrganisationsIdApplicationsAppIdInstances_1"></a>
# **getOrganisationsIdApplicationsAppIdInstances_1**
> List&lt;AppInstance&gt; getOrganisationsIdApplicationsAppIdInstances_1(id, appId)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganisationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    OrganisationsApi apiInstance = new OrganisationsApi(defaultClient);
    String id = "id_example"; // String | 
    String appId = "appId_example"; // String | 
    try {
      List<AppInstance> result = apiInstance.getOrganisationsIdApplicationsAppIdInstances_1(id, appId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganisationsApi#getOrganisationsIdApplicationsAppIdInstances_1");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**|  | |
| **appId** | **String**|  | |

### Return type

[**List&lt;AppInstance&gt;**](AppInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | getApplicationInstances |  -  |

<a id="getOrganisationsIdApplicationsAppIdTags_1"></a>
# **getOrganisationsIdApplicationsAppIdTags_1**
> List&lt;String&gt; getOrganisationsIdApplicationsAppIdTags_1(id, appId)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganisationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    OrganisationsApi apiInstance = new OrganisationsApi(defaultClient);
    String id = "id_example"; // String | 
    String appId = "appId_example"; // String | 
    try {
      List<String> result = apiInstance.getOrganisationsIdApplicationsAppIdTags_1(id, appId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganisationsApi#getOrganisationsIdApplicationsAppIdTags_1");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**|  | |
| **appId** | **String**|  | |

### Return type

**List&lt;String&gt;**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | getApplicationTags |  -  |

<a id="getOrganisationsIdApplicationsAppIdVhostsFavourite_1"></a>
# **getOrganisationsIdApplicationsAppIdVhostsFavourite_1**
> Vhost getOrganisationsIdApplicationsAppIdVhostsFavourite_1(id, appId)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganisationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    OrganisationsApi apiInstance = new OrganisationsApi(defaultClient);
    String id = "id_example"; // String | 
    String appId = "appId_example"; // String | 
    try {
      Vhost result = apiInstance.getOrganisationsIdApplicationsAppIdVhostsFavourite_1(id, appId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganisationsApi#getOrganisationsIdApplicationsAppIdVhostsFavourite_1");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**|  | |
| **appId** | **String**|  | |

### Return type

[**Vhost**](Vhost.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | getFavouriteVhost |  -  |

<a id="getOrganisationsIdApplicationsAppIdVhosts_1"></a>
# **getOrganisationsIdApplicationsAppIdVhosts_1**
> List&lt;Vhost&gt; getOrganisationsIdApplicationsAppIdVhosts_1(id, appId)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganisationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    OrganisationsApi apiInstance = new OrganisationsApi(defaultClient);
    String id = "id_example"; // String | 
    String appId = "appId_example"; // String | 
    try {
      List<Vhost> result = apiInstance.getOrganisationsIdApplicationsAppIdVhosts_1(id, appId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganisationsApi#getOrganisationsIdApplicationsAppIdVhosts_1");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**|  | |
| **appId** | **String**|  | |

### Return type

[**List&lt;Vhost&gt;**](Vhost.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | getVhosts |  -  |

<a id="getOrganisationsIdApplicationsAppId_1"></a>
# **getOrganisationsIdApplicationsAppId_1**
> Application getOrganisationsIdApplicationsAppId_1(id, appId)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganisationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    OrganisationsApi apiInstance = new OrganisationsApi(defaultClient);
    String id = "id_example"; // String | 
    String appId = "appId_example"; // String | 
    try {
      Application result = apiInstance.getOrganisationsIdApplicationsAppId_1(id, appId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganisationsApi#getOrganisationsIdApplicationsAppId_1");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**|  | |
| **appId** | **String**|  | |

### Return type

[**Application**](Application.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | getApplication |  -  |

<a id="getOrganisationsIdApplications_1"></a>
# **getOrganisationsIdApplications_1**
> List&lt;Application&gt; getOrganisationsIdApplications_1(id)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganisationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    OrganisationsApi apiInstance = new OrganisationsApi(defaultClient);
    String id = "id_example"; // String | 
    try {
      List<Application> result = apiInstance.getOrganisationsIdApplications_1(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganisationsApi#getOrganisationsIdApplications_1");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**|  | |

### Return type

[**List&lt;Application&gt;**](Application.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | getAllApplications |  -  |

<a id="getOrganisationsIdConsumersKeySecret_0"></a>
# **getOrganisationsIdConsumersKeySecret_0**
> Secret getOrganisationsIdConsumersKeySecret_0(id, key)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganisationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    OrganisationsApi apiInstance = new OrganisationsApi(defaultClient);
    String id = "id_example"; // String | 
    String key = "key_example"; // String | 
    try {
      Secret result = apiInstance.getOrganisationsIdConsumersKeySecret_0(id, key);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganisationsApi#getOrganisationsIdConsumersKeySecret_0");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**|  | |
| **key** | **String**|  | |

### Return type

[**Secret**](Secret.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | getConsumerSecret |  -  |

<a id="getOrganisationsIdConsumersKey_0"></a>
# **getOrganisationsIdConsumersKey_0**
> Consumer getOrganisationsIdConsumersKey_0(id, key)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganisationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    OrganisationsApi apiInstance = new OrganisationsApi(defaultClient);
    String id = "id_example"; // String | 
    String key = "key_example"; // String | 
    try {
      Consumer result = apiInstance.getOrganisationsIdConsumersKey_0(id, key);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganisationsApi#getOrganisationsIdConsumersKey_0");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**|  | |
| **key** | **String**|  | |

### Return type

[**Consumer**](Consumer.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | getConsumer |  -  |

<a id="getOrganisationsIdConsumers_0"></a>
# **getOrganisationsIdConsumers_0**
> List&lt;Consumer&gt; getOrganisationsIdConsumers_0(id)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganisationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    OrganisationsApi apiInstance = new OrganisationsApi(defaultClient);
    String id = "id_example"; // String | 
    try {
      List<Consumer> result = apiInstance.getOrganisationsIdConsumers_0(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganisationsApi#getOrganisationsIdConsumers_0");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**|  | |

### Return type

[**List&lt;Consumer&gt;**](Consumer.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | getConsumers |  -  |

<a id="getOrganisationsIdConsumptions_0"></a>
# **getOrganisationsIdConsumptions_0**
> Conso getOrganisationsIdConsumptions_0(id, appId, from, to)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganisationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    OrganisationsApi apiInstance = new OrganisationsApi(defaultClient);
    String id = "id_example"; // String | 
    String appId = "appId_example"; // String | 
    String from = "from_example"; // String | 
    String to = "to_example"; // String | 
    try {
      Conso result = apiInstance.getOrganisationsIdConsumptions_0(id, appId, from, to);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganisationsApi#getOrganisationsIdConsumptions_0");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**|  | |
| **appId** | **String**|  | [optional] |
| **from** | **String**|  | [optional] |
| **to** | **String**|  | [optional] |

### Return type

[**Conso**](Conso.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | getAmount |  -  |

<a id="getOrganisationsIdCredits_0"></a>
# **getOrganisationsIdCredits_0**
> Credits getOrganisationsIdCredits_0(id)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganisationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    OrganisationsApi apiInstance = new OrganisationsApi(defaultClient);
    String id = "id_example"; // String | 
    try {
      Credits result = apiInstance.getOrganisationsIdCredits_0(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganisationsApi#getOrganisationsIdCredits_0");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**|  | |

### Return type

[**Credits**](Credits.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | getAmount |  -  |

<a id="getOrganisationsIdDeployments_0"></a>
# **getOrganisationsIdDeployments_0**
> DeploymentSummary getOrganisationsIdDeployments_0(id)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganisationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    OrganisationsApi apiInstance = new OrganisationsApi(defaultClient);
    String id = "id_example"; // String | 
    try {
      DeploymentSummary result = apiInstance.getOrganisationsIdDeployments_0(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganisationsApi#getOrganisationsIdDeployments_0");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**|  | |

### Return type

[**DeploymentSummary**](DeploymentSummary.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | getDeploymentsForAllApps |  -  |

<a id="getOrganisationsIdInstances_0"></a>
# **getOrganisationsIdInstances_0**
> Object getOrganisationsIdInstances_0(id)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganisationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    OrganisationsApi apiInstance = new OrganisationsApi(defaultClient);
    String id = "id_example"; // String | 
    try {
      Object result = apiInstance.getOrganisationsIdInstances_0(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganisationsApi#getOrganisationsIdInstances_0");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**|  | |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | getInstancesForAllApps |  -  |

<a id="getOrganisationsIdMembers_0"></a>
# **getOrganisationsIdMembers_0**
> List&lt;Schema1&gt; getOrganisationsIdMembers_0(id)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganisationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    OrganisationsApi apiInstance = new OrganisationsApi(defaultClient);
    String id = "id_example"; // String | 
    try {
      List<Schema1> result = apiInstance.getOrganisationsIdMembers_0(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganisationsApi#getOrganisationsIdMembers_0");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**|  | |

### Return type

[**List&lt;Schema1&gt;**](Schema1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | getOrganisationMembers |  -  |

<a id="getOrganisationsIdPaymentInfo_0"></a>
# **getOrganisationsIdPaymentInfo_0**
> getOrganisationsIdPaymentInfo_0(id)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganisationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    OrganisationsApi apiInstance = new OrganisationsApi(defaultClient);
    String id = "id_example"; // String | 
    try {
      apiInstance.getOrganisationsIdPaymentInfo_0(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganisationsApi#getOrganisationsIdPaymentInfo_0");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | getPaymentInfo |  -  |

<a id="getOrganisationsIdPaymentsBillingsBidPdf_0"></a>
# **getOrganisationsIdPaymentsBillingsBidPdf_0**
> getOrganisationsIdPaymentsBillingsBidPdf_0(id, bid, token)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganisationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    OrganisationsApi apiInstance = new OrganisationsApi(defaultClient);
    String id = "id_example"; // String | 
    String bid = "bid_example"; // String | 
    String token = "token_example"; // String | 
    try {
      apiInstance.getOrganisationsIdPaymentsBillingsBidPdf_0(id, bid, token);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganisationsApi#getOrganisationsIdPaymentsBillingsBidPdf_0");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**|  | |
| **bid** | **String**|  | |
| **token** | **String**|  | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | getPdfInvoice |  -  |

<a id="getOrganisationsIdPaymentsBillingsBid_0"></a>
# **getOrganisationsIdPaymentsBillingsBid_0**
> getOrganisationsIdPaymentsBillingsBid_0(id, bid)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganisationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    OrganisationsApi apiInstance = new OrganisationsApi(defaultClient);
    String id = "id_example"; // String | 
    String bid = "bid_example"; // String | 
    try {
      apiInstance.getOrganisationsIdPaymentsBillingsBid_0(id, bid);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganisationsApi#getOrganisationsIdPaymentsBillingsBid_0");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**|  | |
| **bid** | **String**|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | getInvoice |  -  |

<a id="getOrganisationsIdPaymentsBillings_0"></a>
# **getOrganisationsIdPaymentsBillings_0**
> getOrganisationsIdPaymentsBillings_0(id)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganisationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    OrganisationsApi apiInstance = new OrganisationsApi(defaultClient);
    String id = "id_example"; // String | 
    try {
      apiInstance.getOrganisationsIdPaymentsBillings_0(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganisationsApi#getOrganisationsIdPaymentsBillings_0");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | getInvoices |  -  |

<a id="getOrganisationsIdPaymentsFullPricePrice_0"></a>
# **getOrganisationsIdPaymentsFullPricePrice_0**
> getOrganisationsIdPaymentsFullPricePrice_0(id, price)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganisationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    OrganisationsApi apiInstance = new OrganisationsApi(defaultClient);
    String id = "id_example"; // String | 
    String price = "price_example"; // String | 
    try {
      apiInstance.getOrganisationsIdPaymentsFullPricePrice_0(id, price);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganisationsApi#getOrganisationsIdPaymentsFullPricePrice_0");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**|  | |
| **price** | **String**|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | priceWithTax |  -  |

<a id="getOrganisationsId_0"></a>
# **getOrganisationsId_0**
> Organisation getOrganisationsId_0(id)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganisationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    OrganisationsApi apiInstance = new OrganisationsApi(defaultClient);
    String id = "id_example"; // String | 
    try {
      Organisation result = apiInstance.getOrganisationsId_0(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganisationsApi#getOrganisationsId_0");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**|  | |

### Return type

[**Organisation**](Organisation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | getOrganisation |  -  |

<a id="getOrganisations_0"></a>
# **getOrganisations_0**
> List&lt;Organisation&gt; getOrganisations_0(user)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganisationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    OrganisationsApi apiInstance = new OrganisationsApi(defaultClient);
    String user = "user_example"; // String | 
    try {
      List<Organisation> result = apiInstance.getOrganisations_0(user);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganisationsApi#getOrganisations_0");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **user** | **String**|  | [optional] |

### Return type

[**List&lt;Organisation&gt;**](Organisation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | getUserOrganisations |  -  |

<a id="listNetworkGroupMembers_0"></a>
# **listNetworkGroupMembers_0**
> List&lt;Schema1&gt; listNetworkGroupMembers_0(ownerId, networkGroupId, body)

List members

Lists members in a Network Group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganisationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    OrganisationsApi apiInstance = new OrganisationsApi(defaultClient);
    String ownerId = "ownerId_example"; // String | Automatically added
    String networkGroupId = "networkGroupId_example"; // String | Automatically added
    Object body = null; // Object | 
    try {
      List<Schema1> result = apiInstance.listNetworkGroupMembers_0(ownerId, networkGroupId, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganisationsApi#listNetworkGroupMembers_0");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **ownerId** | **String**| Automatically added | |
| **networkGroupId** | **String**| Automatically added | |
| **body** | **Object**|  | [optional] |

### Return type

[**List&lt;Schema1&gt;**](Schema1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **401** |  |  -  |
| **404** |  |  -  |

<a id="listNetworkGroupPeers_0"></a>
# **listNetworkGroupPeers_0**
> List&lt;Object&gt; listNetworkGroupPeers_0(ownerId, networkGroupId, body)

List peers

Lists peers in a Network Group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganisationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    OrganisationsApi apiInstance = new OrganisationsApi(defaultClient);
    String ownerId = "ownerId_example"; // String | Automatically added
    String networkGroupId = "networkGroupId_example"; // String | Automatically added
    Object body = null; // Object | 
    try {
      List<Object> result = apiInstance.listNetworkGroupPeers_0(ownerId, networkGroupId, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganisationsApi#listNetworkGroupPeers_0");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **ownerId** | **String**| Automatically added | |
| **networkGroupId** | **String**| Automatically added | |
| **body** | **Object**|  | [optional] |

### Return type

**List&lt;Object&gt;**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **401** |  |  -  |
| **404** |  |  -  |

<a id="listNetworkGroups_0"></a>
# **listNetworkGroups_0**
> List&lt;Object&gt; listNetworkGroups_0(ownerId, body)

List Network Groups

Lists Network Groups from an owner.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganisationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    OrganisationsApi apiInstance = new OrganisationsApi(defaultClient);
    String ownerId = "ownerId_example"; // String | Automatically added
    Object body = null; // Object | 
    try {
      List<Object> result = apiInstance.listNetworkGroups_0(ownerId, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganisationsApi#listNetworkGroups_0");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **ownerId** | **String**| Automatically added | |
| **body** | **Object**|  | [optional] |

### Return type

**List&lt;Object&gt;**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **401** |  |  -  |

<a id="organisationsIdAddonprovidersProviderIdDelete_0"></a>
# **organisationsIdAddonprovidersProviderIdDelete_0**
> organisationsIdAddonprovidersProviderIdDelete_0(id, providerId)

Remove an add-on provider

Remove a given add-on provider. providerId must be owned by organisation {id}.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganisationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    OrganisationsApi apiInstance = new OrganisationsApi(defaultClient);
    String id = "id_example"; // String | 
    String providerId = "providerId_example"; // String | 
    try {
      apiInstance.organisationsIdAddonprovidersProviderIdDelete_0(id, providerId);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganisationsApi#organisationsIdAddonprovidersProviderIdDelete_0");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**|  | |
| **providerId** | **String**|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | If the deletion was successful. |  -  |
| **403** | If user has no access to organisation {id} or provider or if there still are add-ons of this provider. |  -  |
| **404** | If no such organisation/provider exists. |  -  |

<a id="organisationsIdAddonsAddonIdInstancesGet_1"></a>
# **organisationsIdAddonsAddonIdInstancesGet_1**
> List&lt;SupernovaInstanceView&gt; organisationsIdAddonsAddonIdInstancesGet_1(id, addonId, deploymentId, withDeleted)

List instances for this add-on.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganisationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    OrganisationsApi apiInstance = new OrganisationsApi(defaultClient);
    String id = "id_example"; // String | 
    String addonId = "addonId_example"; // String | 
    String deploymentId = "deploymentId_example"; // String | 
    String withDeleted = "withDeleted_example"; // String | 
    try {
      List<SupernovaInstanceView> result = apiInstance.organisationsIdAddonsAddonIdInstancesGet_1(id, addonId, deploymentId, withDeleted);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganisationsApi#organisationsIdAddonsAddonIdInstancesGet_1");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**|  | |
| **addonId** | **String**|  | |
| **deploymentId** | **String**|  | [optional] |
| **withDeleted** | **String**|  | [optional] |

### Return type

[**List&lt;SupernovaInstanceView&gt;**](SupernovaInstanceView.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The instance list |  -  |

<a id="organisationsIdAddonsAddonIdInstancesInstanceIdGet_1"></a>
# **organisationsIdAddonsAddonIdInstancesInstanceIdGet_1**
> SupernovaInstanceView organisationsIdAddonsAddonIdInstancesInstanceIdGet_1(instanceId, id, addonId)

Get a specific instance for {addonId}

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganisationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    OrganisationsApi apiInstance = new OrganisationsApi(defaultClient);
    String instanceId = "instanceId_example"; // String | 
    String id = "id_example"; // String | 
    String addonId = "addonId_example"; // String | 
    try {
      SupernovaInstanceView result = apiInstance.organisationsIdAddonsAddonIdInstancesInstanceIdGet_1(instanceId, id, addonId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganisationsApi#organisationsIdAddonsAddonIdInstancesInstanceIdGet_1");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **instanceId** | **String**|  | |
| **id** | **String**|  | |
| **addonId** | **String**|  | |

### Return type

[**SupernovaInstanceView**](SupernovaInstanceView.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | An instance |  -  |

<a id="organisationsIdAddonsAddonIdMigrationsGet_1"></a>
# **organisationsIdAddonsAddonIdMigrationsGet_1**
> List&lt;AddonMigration&gt; organisationsIdAddonsAddonIdMigrationsGet_1(id, addonId)

Get past migrations from add-on.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganisationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    OrganisationsApi apiInstance = new OrganisationsApi(defaultClient);
    String id = "id_example"; // String | 
    String addonId = "addonId_example"; // String | 
    try {
      List<AddonMigration> result = apiInstance.organisationsIdAddonsAddonIdMigrationsGet_1(id, addonId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganisationsApi#organisationsIdAddonsAddonIdMigrationsGet_1");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**|  | |
| **addonId** | **String**|  | |

### Return type

[**List&lt;AddonMigration&gt;**](AddonMigration.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of migrations |  -  |

<a id="organisationsIdAddonsAddonIdMigrationsMigrationIdGet_1"></a>
# **organisationsIdAddonsAddonIdMigrationsMigrationIdGet_1**
> AddonMigration organisationsIdAddonsAddonIdMigrationsMigrationIdGet_1(migrationId, id, addonId)

Get a given migration

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganisationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    OrganisationsApi apiInstance = new OrganisationsApi(defaultClient);
    String migrationId = "migrationId_example"; // String | 
    String id = "id_example"; // String | 
    String addonId = "addonId_example"; // String | 
    try {
      AddonMigration result = apiInstance.organisationsIdAddonsAddonIdMigrationsMigrationIdGet_1(migrationId, id, addonId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganisationsApi#organisationsIdAddonsAddonIdMigrationsMigrationIdGet_1");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **migrationId** | **String**|  | |
| **id** | **String**|  | |
| **addonId** | **String**|  | |

### Return type

[**AddonMigration**](AddonMigration.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The migration object |  -  |

<a id="organisationsIdAddonsAddonIdMigrationsPost_1"></a>
# **organisationsIdAddonsAddonIdMigrationsPost_1**
> Object organisationsIdAddonsAddonIdMigrationsPost_1(id, addonId, organisationsIdAddonsAddonIdMigrationsPostRequest)

Start a new add-on migration

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganisationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    OrganisationsApi apiInstance = new OrganisationsApi(defaultClient);
    String id = "id_example"; // String | 
    String addonId = "addonId_example"; // String | 
    OrganisationsIdAddonsAddonIdMigrationsPostRequest organisationsIdAddonsAddonIdMigrationsPostRequest = new OrganisationsIdAddonsAddonIdMigrationsPostRequest(); // OrganisationsIdAddonsAddonIdMigrationsPostRequest | 
    try {
      Object result = apiInstance.organisationsIdAddonsAddonIdMigrationsPost_1(id, addonId, organisationsIdAddonsAddonIdMigrationsPostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganisationsApi#organisationsIdAddonsAddonIdMigrationsPost_1");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**|  | |
| **addonId** | **String**|  | |
| **organisationsIdAddonsAddonIdMigrationsPostRequest** | [**OrganisationsIdAddonsAddonIdMigrationsPostRequest**](OrganisationsIdAddonsAddonIdMigrationsPostRequest.md)|  | |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Migration has started. |  -  |

<a id="organisationsIdAddonsAddonIdSsoGet_1"></a>
# **organisationsIdAddonsAddonIdSsoGet_1**
> Sso organisationsIdAddonsAddonIdSsoGet_1(id, addonId)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganisationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    OrganisationsApi apiInstance = new OrganisationsApi(defaultClient);
    String id = "id_example"; // String | 
    String addonId = "addonId_example"; // String | 
    try {
      Sso result = apiInstance.organisationsIdAddonsAddonIdSsoGet_1(id, addonId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganisationsApi#organisationsIdAddonsAddonIdSsoGet_1");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**|  | |
| **addonId** | **String**|  | |

### Return type

[**Sso**](Sso.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | getSSOData |  -  |

<a id="organisationsIdAddonsPreordersPost_1"></a>
# **organisationsIdAddonsPreordersPost_1**
> organisationsIdAddonsPreordersPost_1(id, wannabeAddon)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganisationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    OrganisationsApi apiInstance = new OrganisationsApi(defaultClient);
    String id = "id_example"; // String | 
    WannabeAddon wannabeAddon = new WannabeAddon(); // WannabeAddon | 
    try {
      apiInstance.organisationsIdAddonsPreordersPost_1(id, wannabeAddon);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganisationsApi#organisationsIdAddonsPreordersPost_1");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**|  | |
| **wannabeAddon** | [**WannabeAddon**](WannabeAddon.md)|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Status 200 |  -  |

<a id="organisationsIdApplicationsAppIdBranchPut_1"></a>
# **organisationsIdApplicationsAppIdBranchPut_1**
> organisationsIdApplicationsAppIdBranchPut_1(appId, id)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganisationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    OrganisationsApi apiInstance = new OrganisationsApi(defaultClient);
    String appId = "appId_example"; // String | 
    String id = "id_example"; // String | 
    try {
      apiInstance.organisationsIdApplicationsAppIdBranchPut_1(appId, id);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganisationsApi#organisationsIdApplicationsAppIdBranchPut_1");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **appId** | **String**|  | |
| **id** | **String**|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Status 200 |  -  |

<a id="organisationsIdApplicationsAppIdBranchesGet_1"></a>
# **organisationsIdApplicationsAppIdBranchesGet_1**
> organisationsIdApplicationsAppIdBranchesGet_1(appId, id)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganisationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    OrganisationsApi apiInstance = new OrganisationsApi(defaultClient);
    String appId = "appId_example"; // String | 
    String id = "id_example"; // String | 
    try {
      apiInstance.organisationsIdApplicationsAppIdBranchesGet_1(appId, id);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganisationsApi#organisationsIdApplicationsAppIdBranchesGet_1");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **appId** | **String**|  | |
| **id** | **String**|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Status 200 |  -  |

<a id="organisationsIdApplicationsAppIdBuildflavorPut_1"></a>
# **organisationsIdApplicationsAppIdBuildflavorPut_1**
> organisationsIdApplicationsAppIdBuildflavorPut_1(appId, id)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganisationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    OrganisationsApi apiInstance = new OrganisationsApi(defaultClient);
    String appId = "appId_example"; // String | 
    String id = "id_example"; // String | 
    try {
      apiInstance.organisationsIdApplicationsAppIdBuildflavorPut_1(appId, id);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganisationsApi#organisationsIdApplicationsAppIdBuildflavorPut_1");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **appId** | **String**|  | |
| **id** | **String**|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Status 200 |  -  |

<a id="organisationsIdApplicationsAppIdDependenciesEnvGet_1"></a>
# **organisationsIdApplicationsAppIdDependenciesEnvGet_1**
> List&lt;LinkedAppEnv&gt; organisationsIdApplicationsAppIdDependenciesEnvGet_1(appId, id)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganisationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    OrganisationsApi apiInstance = new OrganisationsApi(defaultClient);
    String appId = "appId_example"; // String | 
    String id = "id_example"; // String | 
    try {
      List<LinkedAppEnv> result = apiInstance.organisationsIdApplicationsAppIdDependenciesEnvGet_1(appId, id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganisationsApi#organisationsIdApplicationsAppIdDependenciesEnvGet_1");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **appId** | **String**|  | |
| **id** | **String**|  | |

### Return type

[**List&lt;LinkedAppEnv&gt;**](LinkedAppEnv.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Get env variables defined by application dependencies |  -  |

<a id="organisationsIdApplicationsAppIdDeploymentsDeploymentIdGet_1"></a>
# **organisationsIdApplicationsAppIdDeploymentsDeploymentIdGet_1**
> organisationsIdApplicationsAppIdDeploymentsDeploymentIdGet_1(appId, deploymentId, id)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganisationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    OrganisationsApi apiInstance = new OrganisationsApi(defaultClient);
    String appId = "appId_example"; // String | 
    String deploymentId = "deploymentId_example"; // String | 
    String id = "id_example"; // String | 
    try {
      apiInstance.organisationsIdApplicationsAppIdDeploymentsDeploymentIdGet_1(appId, deploymentId, id);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganisationsApi#organisationsIdApplicationsAppIdDeploymentsDeploymentIdGet_1");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **appId** | **String**|  | |
| **deploymentId** | **String**|  | |
| **id** | **String**|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Status 200 |  -  |

<a id="organisationsIdApplicationsAppIdExposedEnvGet_1"></a>
# **organisationsIdApplicationsAppIdExposedEnvGet_1**
> organisationsIdApplicationsAppIdExposedEnvGet_1(appId, id)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganisationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    OrganisationsApi apiInstance = new OrganisationsApi(defaultClient);
    String appId = "appId_example"; // String | 
    String id = "id_example"; // String | 
    try {
      apiInstance.organisationsIdApplicationsAppIdExposedEnvGet_1(appId, id);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganisationsApi#organisationsIdApplicationsAppIdExposedEnvGet_1");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **appId** | **String**|  | |
| **id** | **String**|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Status 200 |  -  |

<a id="organisationsIdApplicationsAppIdExposedEnvPut_1"></a>
# **organisationsIdApplicationsAppIdExposedEnvPut_1**
> organisationsIdApplicationsAppIdExposedEnvPut_1(appId, id)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganisationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    OrganisationsApi apiInstance = new OrganisationsApi(defaultClient);
    String appId = "appId_example"; // String | 
    String id = "id_example"; // String | 
    try {
      apiInstance.organisationsIdApplicationsAppIdExposedEnvPut_1(appId, id);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganisationsApi#organisationsIdApplicationsAppIdExposedEnvPut_1");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **appId** | **String**|  | |
| **id** | **String**|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Status 200 |  -  |

<a id="organisationsIdApplicationsAppIdInstancesInstanceIdGet_1"></a>
# **organisationsIdApplicationsAppIdInstancesInstanceIdGet_1**
> organisationsIdApplicationsAppIdInstancesInstanceIdGet_1(instanceId, appId, id)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganisationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    OrganisationsApi apiInstance = new OrganisationsApi(defaultClient);
    String instanceId = "instanceId_example"; // String | 
    String appId = "appId_example"; // String | 
    String id = "id_example"; // String | 
    try {
      apiInstance.organisationsIdApplicationsAppIdInstancesInstanceIdGet_1(instanceId, appId, id);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganisationsApi#organisationsIdApplicationsAppIdInstancesInstanceIdGet_1");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **instanceId** | **String**|  | |
| **appId** | **String**|  | |
| **id** | **String**|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Status 200 |  -  |

<a id="organisationsIdPaymentsBillingsUnpaidGet_0"></a>
# **organisationsIdPaymentsBillingsUnpaidGet_0**
> organisationsIdPaymentsBillingsUnpaidGet_0(id)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganisationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    OrganisationsApi apiInstance = new OrganisationsApi(defaultClient);
    String id = "id_example"; // String | 
    try {
      apiInstance.organisationsIdPaymentsBillingsUnpaidGet_0(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganisationsApi#organisationsIdPaymentsBillingsUnpaidGet_0");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Status 200 |  -  |

<a id="organisationsIdPaymentsMethodsDefaultGet_0"></a>
# **organisationsIdPaymentsMethodsDefaultGet_0**
> organisationsIdPaymentsMethodsDefaultGet_0(id)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganisationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    OrganisationsApi apiInstance = new OrganisationsApi(defaultClient);
    String id = "id_example"; // String | 
    try {
      apiInstance.organisationsIdPaymentsMethodsDefaultGet_0(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganisationsApi#organisationsIdPaymentsMethodsDefaultGet_0");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Status 200 |  -  |

<a id="organisationsIdPaymentsMethodsDefaultPut_0"></a>
# **organisationsIdPaymentsMethodsDefaultPut_0**
> organisationsIdPaymentsMethodsDefaultPut_0(id, paymentData)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganisationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    OrganisationsApi apiInstance = new OrganisationsApi(defaultClient);
    String id = "id_example"; // String | 
    PaymentData paymentData = new PaymentData(); // PaymentData | 
    try {
      apiInstance.organisationsIdPaymentsMethodsDefaultPut_0(id, paymentData);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganisationsApi#organisationsIdPaymentsMethodsDefaultPut_0");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**|  | |
| **paymentData** | [**PaymentData**](PaymentData.md)|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Status 200 |  -  |

<a id="organisationsIdPaymentsMethodsGet_0"></a>
# **organisationsIdPaymentsMethodsGet_0**
> organisationsIdPaymentsMethodsGet_0(id)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganisationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    OrganisationsApi apiInstance = new OrganisationsApi(defaultClient);
    String id = "id_example"; // String | 
    try {
      apiInstance.organisationsIdPaymentsMethodsGet_0(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganisationsApi#organisationsIdPaymentsMethodsGet_0");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Status 200 |  -  |

<a id="organisationsIdPaymentsMethodsMIdDelete_0"></a>
# **organisationsIdPaymentsMethodsMIdDelete_0**
> organisationsIdPaymentsMethodsMIdDelete_0(mId, id)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganisationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    OrganisationsApi apiInstance = new OrganisationsApi(defaultClient);
    String mId = "mId_example"; // String | 
    String id = "id_example"; // String | 
    try {
      apiInstance.organisationsIdPaymentsMethodsMIdDelete_0(mId, id);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganisationsApi#organisationsIdPaymentsMethodsMIdDelete_0");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **mId** | **String**|  | |
| **id** | **String**|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Status 200 |  -  |

<a id="organisationsIdPaymentsMethodsPost_0"></a>
# **organisationsIdPaymentsMethodsPost_0**
> organisationsIdPaymentsMethodsPost_0(id, body)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganisationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    OrganisationsApi apiInstance = new OrganisationsApi(defaultClient);
    String id = "id_example"; // String | 
    Body body = new Body(); // Body | 
    try {
      apiInstance.organisationsIdPaymentsMethodsPost_0(id, body);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganisationsApi#organisationsIdPaymentsMethodsPost_0");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**|  | |
| **body** | [**Body**](Body.md)|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Status 200 |  -  |

<a id="organisationsIdPaymentsMonthlyinvoiceGet_0"></a>
# **organisationsIdPaymentsMonthlyinvoiceGet_0**
> organisationsIdPaymentsMonthlyinvoiceGet_0(id)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganisationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    OrganisationsApi apiInstance = new OrganisationsApi(defaultClient);
    String id = "id_example"; // String | 
    try {
      apiInstance.organisationsIdPaymentsMonthlyinvoiceGet_0(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganisationsApi#organisationsIdPaymentsMonthlyinvoiceGet_0");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Status 200 |  -  |

<a id="organisationsIdPaymentsMonthlyinvoiceMaxcreditPut_0"></a>
# **organisationsIdPaymentsMonthlyinvoiceMaxcreditPut_0**
> organisationsIdPaymentsMonthlyinvoiceMaxcreditPut_0(id)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganisationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    OrganisationsApi apiInstance = new OrganisationsApi(defaultClient);
    String id = "id_example"; // String | 
    try {
      apiInstance.organisationsIdPaymentsMonthlyinvoiceMaxcreditPut_0(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganisationsApi#organisationsIdPaymentsMonthlyinvoiceMaxcreditPut_0");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Status 200 |  -  |

<a id="organisationsIdPaymentsRecurringGet_0"></a>
# **organisationsIdPaymentsRecurringGet_0**
> organisationsIdPaymentsRecurringGet_0(id)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganisationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    OrganisationsApi apiInstance = new OrganisationsApi(defaultClient);
    String id = "id_example"; // String | 
    try {
      apiInstance.organisationsIdPaymentsRecurringGet_0(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganisationsApi#organisationsIdPaymentsRecurringGet_0");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Status 200 |  -  |

<a id="postOrganisationsIdAddonprovidersProviderIdFeatures_0"></a>
# **postOrganisationsIdAddonprovidersProviderIdFeatures_0**
> Feature postOrganisationsIdAddonprovidersProviderIdFeatures_0(id, providerId, wannabeFeature)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganisationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    OrganisationsApi apiInstance = new OrganisationsApi(defaultClient);
    String id = "id_example"; // String | 
    String providerId = "providerId_example"; // String | 
    WannabeFeature wannabeFeature = new WannabeFeature(); // WannabeFeature | 
    try {
      Feature result = apiInstance.postOrganisationsIdAddonprovidersProviderIdFeatures_0(id, providerId, wannabeFeature);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganisationsApi#postOrganisationsIdAddonprovidersProviderIdFeatures_0");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**|  | |
| **providerId** | **String**|  | |
| **wannabeFeature** | [**WannabeFeature**](WannabeFeature.md)|  | |

### Return type

[**Feature**](Feature.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | addProviderFeature |  -  |

<a id="postOrganisationsIdAddonprovidersProviderIdPlans_0"></a>
# **postOrganisationsIdAddonprovidersProviderIdPlans_0**
> Plan postOrganisationsIdAddonprovidersProviderIdPlans_0(id, providerId, wannabePlan)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganisationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    OrganisationsApi apiInstance = new OrganisationsApi(defaultClient);
    String id = "id_example"; // String | 
    String providerId = "providerId_example"; // String | 
    WannabePlan wannabePlan = new WannabePlan(); // WannabePlan | 
    try {
      Plan result = apiInstance.postOrganisationsIdAddonprovidersProviderIdPlans_0(id, providerId, wannabePlan);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganisationsApi#postOrganisationsIdAddonprovidersProviderIdPlans_0");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**|  | |
| **providerId** | **String**|  | |
| **wannabePlan** | [**WannabePlan**](WannabePlan.md)|  | |

### Return type

[**Plan**](Plan.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | addProviderPlan |  -  |

<a id="postOrganisationsIdAddonprovidersProviderIdTesters_0"></a>
# **postOrganisationsIdAddonprovidersProviderIdTesters_0**
> postOrganisationsIdAddonprovidersProviderIdTesters_0(id, providerId)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganisationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    OrganisationsApi apiInstance = new OrganisationsApi(defaultClient);
    String id = "id_example"; // String | 
    String providerId = "providerId_example"; // String | 
    try {
      apiInstance.postOrganisationsIdAddonprovidersProviderIdTesters_0(id, providerId);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganisationsApi#postOrganisationsIdAddonprovidersProviderIdTesters_0");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**|  | |
| **providerId** | **String**|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | addBetaTester |  -  |

<a id="postOrganisationsIdAddonproviders_0"></a>
# **postOrganisationsIdAddonproviders_0**
> Provider postOrganisationsIdAddonproviders_0(id, wannabeAddonProvider)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganisationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    OrganisationsApi apiInstance = new OrganisationsApi(defaultClient);
    String id = "id_example"; // String | 
    WannabeAddonProvider wannabeAddonProvider = new WannabeAddonProvider(); // WannabeAddonProvider | 
    try {
      Provider result = apiInstance.postOrganisationsIdAddonproviders_0(id, wannabeAddonProvider);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganisationsApi#postOrganisationsIdAddonproviders_0");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**|  | |
| **wannabeAddonProvider** | [**WannabeAddonProvider**](WannabeAddonProvider.md)|  | |

### Return type

[**Provider**](Provider.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | createProvider |  -  |

<a id="postOrganisationsIdAddons_1"></a>
# **postOrganisationsIdAddons_1**
> Addon postOrganisationsIdAddons_1(id, wannabeAddon)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganisationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    OrganisationsApi apiInstance = new OrganisationsApi(defaultClient);
    String id = "id_example"; // String | 
    WannabeAddon wannabeAddon = new WannabeAddon(); // WannabeAddon | 
    try {
      Addon result = apiInstance.postOrganisationsIdAddons_1(id, wannabeAddon);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganisationsApi#postOrganisationsIdAddons_1");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**|  | |
| **wannabeAddon** | [**WannabeAddon**](WannabeAddon.md)|  | |

### Return type

[**Addon**](Addon.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | provisionAddon |  -  |

<a id="postOrganisationsIdApplicationsAppIdAddons_2"></a>
# **postOrganisationsIdApplicationsAppIdAddons_2**
> postOrganisationsIdApplicationsAppIdAddons_2(id, appId, body)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganisationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    OrganisationsApi apiInstance = new OrganisationsApi(defaultClient);
    String id = "id_example"; // String | 
    String appId = "appId_example"; // String | 
    Body body = new Body(); // Body | 
    try {
      apiInstance.postOrganisationsIdApplicationsAppIdAddons_2(id, appId, body);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganisationsApi#postOrganisationsIdApplicationsAppIdAddons_2");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**|  | |
| **appId** | **String**|  | |
| **body** | [**Body**](Body.md)|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | linkAddonToApplication |  -  |

<a id="postOrganisationsIdApplicationsAppIdInstances_1"></a>
# **postOrganisationsIdApplicationsAppIdInstances_1**
> postOrganisationsIdApplicationsAppIdInstances_1(id, appId, commit)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganisationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    OrganisationsApi apiInstance = new OrganisationsApi(defaultClient);
    String id = "id_example"; // String | 
    String appId = "appId_example"; // String | 
    String commit = "commit_example"; // String | 
    try {
      apiInstance.postOrganisationsIdApplicationsAppIdInstances_1(id, appId, commit);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganisationsApi#postOrganisationsIdApplicationsAppIdInstances_1");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**|  | |
| **appId** | **String**|  | |
| **commit** | **String**|  | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | redeployApplication |  -  |

<a id="postOrganisationsIdApplications_1"></a>
# **postOrganisationsIdApplications_1**
> Application postOrganisationsIdApplications_1(id, wannabeApplication)



Creates an application. If you want to create a Github app, you need to replace the oauthApp field with what you will find here: https://github.com/CleverCloud/doc.clever-cloud.com/issues/179

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganisationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    OrganisationsApi apiInstance = new OrganisationsApi(defaultClient);
    String id = "id_example"; // String | 
    WannabeApplication wannabeApplication = new WannabeApplication(); // WannabeApplication | 
    try {
      Application result = apiInstance.postOrganisationsIdApplications_1(id, wannabeApplication);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganisationsApi#postOrganisationsIdApplications_1");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**|  | |
| **wannabeApplication** | [**WannabeApplication**](WannabeApplication.md)|  | |

### Return type

[**Application**](Application.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | addApplication |  -  |

<a id="postOrganisationsIdConsumers_0"></a>
# **postOrganisationsIdConsumers_0**
> postOrganisationsIdConsumers_0(id, wannabeConsumer)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganisationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    OrganisationsApi apiInstance = new OrganisationsApi(defaultClient);
    String id = "id_example"; // String | 
    WannabeConsumer wannabeConsumer = new WannabeConsumer(); // WannabeConsumer | 
    try {
      apiInstance.postOrganisationsIdConsumers_0(id, wannabeConsumer);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganisationsApi#postOrganisationsIdConsumers_0");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**|  | |
| **wannabeConsumer** | [**WannabeConsumer**](WannabeConsumer.md)|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | createConsumer |  -  |

<a id="postOrganisationsIdMembers_0"></a>
# **postOrganisationsIdMembers_0**
> postOrganisationsIdMembers_0(id, body, invitationKey)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganisationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    OrganisationsApi apiInstance = new OrganisationsApi(defaultClient);
    String id = "id_example"; // String | 
    Schema2 body = new Schema2(); // Schema2 | 
    String invitationKey = "invitationKey_example"; // String | 
    try {
      apiInstance.postOrganisationsIdMembers_0(id, body, invitationKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganisationsApi#postOrganisationsIdMembers_0");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**|  | |
| **body** | **Schema2**|  | |
| **invitationKey** | **String**|  | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | addOrganisationMember |  -  |

<a id="postOrganisationsIdPaymentsBillings_0"></a>
# **postOrganisationsIdPaymentsBillings_0**
> postOrganisationsIdPaymentsBillings_0(id)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganisationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    OrganisationsApi apiInstance = new OrganisationsApi(defaultClient);
    String id = "id_example"; // String | 
    try {
      apiInstance.postOrganisationsIdPaymentsBillings_0(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganisationsApi#postOrganisationsIdPaymentsBillings_0");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | buyDrops |  -  |

<a id="postOrganisations_0"></a>
# **postOrganisations_0**
> Organisation postOrganisations_0(wannabeOrganisation)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganisationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    OrganisationsApi apiInstance = new OrganisationsApi(defaultClient);
    WannabeOrganisation wannabeOrganisation = new WannabeOrganisation(); // WannabeOrganisation | 
    try {
      Organisation result = apiInstance.postOrganisations_0(wannabeOrganisation);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganisationsApi#postOrganisations_0");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **wannabeOrganisation** | [**WannabeOrganisation**](WannabeOrganisation.md)|  | |

### Return type

[**Organisation**](Organisation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | createOrganisation |  -  |

<a id="putOrganisationsIdAddonprovidersProviderIdPlansPlanIdFeaturesFeatureName_0"></a>
# **putOrganisationsIdAddonprovidersProviderIdPlansPlanIdFeaturesFeatureName_0**
> putOrganisationsIdAddonprovidersProviderIdPlansPlanIdFeaturesFeatureName_0(id, featureName, providerId, planId, wannabePlanFeature)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganisationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    OrganisationsApi apiInstance = new OrganisationsApi(defaultClient);
    String id = "id_example"; // String | 
    String featureName = "featureName_example"; // String | 
    String providerId = "providerId_example"; // String | 
    String planId = "planId_example"; // String | 
    WannabePlanFeature wannabePlanFeature = new WannabePlanFeature(); // WannabePlanFeature | 
    try {
      apiInstance.putOrganisationsIdAddonprovidersProviderIdPlansPlanIdFeaturesFeatureName_0(id, featureName, providerId, planId, wannabePlanFeature);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganisationsApi#putOrganisationsIdAddonprovidersProviderIdPlansPlanIdFeaturesFeatureName_0");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**|  | |
| **featureName** | **String**|  | |
| **providerId** | **String**|  | |
| **planId** | **String**|  | |
| **wannabePlanFeature** | [**WannabePlanFeature**](WannabePlanFeature.md)|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | editProviderPlanFeature |  -  |

<a id="putOrganisationsIdAddonprovidersProviderIdPlansPlanId_0"></a>
# **putOrganisationsIdAddonprovidersProviderIdPlansPlanId_0**
> Plan putOrganisationsIdAddonprovidersProviderIdPlansPlanId_0(id, providerId, planId, wannabePlan)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganisationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    OrganisationsApi apiInstance = new OrganisationsApi(defaultClient);
    String id = "id_example"; // String | 
    String providerId = "providerId_example"; // String | 
    String planId = "planId_example"; // String | 
    WannabePlan wannabePlan = new WannabePlan(); // WannabePlan | 
    try {
      Plan result = apiInstance.putOrganisationsIdAddonprovidersProviderIdPlansPlanId_0(id, providerId, planId, wannabePlan);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganisationsApi#putOrganisationsIdAddonprovidersProviderIdPlansPlanId_0");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**|  | |
| **providerId** | **String**|  | |
| **planId** | **String**|  | |
| **wannabePlan** | [**WannabePlan**](WannabePlan.md)|  | |

### Return type

[**Plan**](Plan.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | editProviderPlan |  -  |

<a id="putOrganisationsIdAddonprovidersProviderId_0"></a>
# **putOrganisationsIdAddonprovidersProviderId_0**
> Provider putOrganisationsIdAddonprovidersProviderId_0(id, providerId, wannabeAddonProvider)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganisationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    OrganisationsApi apiInstance = new OrganisationsApi(defaultClient);
    String id = "id_example"; // String | 
    String providerId = "providerId_example"; // String | 
    WannabeAddonProvider wannabeAddonProvider = new WannabeAddonProvider(); // WannabeAddonProvider | 
    try {
      Provider result = apiInstance.putOrganisationsIdAddonprovidersProviderId_0(id, providerId, wannabeAddonProvider);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganisationsApi#putOrganisationsIdAddonprovidersProviderId_0");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**|  | |
| **providerId** | **String**|  | |
| **wannabeAddonProvider** | [**WannabeAddonProvider**](WannabeAddonProvider.md)|  | |

### Return type

[**Provider**](Provider.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | updateProviderInfos |  -  |

<a id="putOrganisationsIdAddonsAddonIdTagsTag_1"></a>
# **putOrganisationsIdAddonsAddonIdTagsTag_1**
> putOrganisationsIdAddonsAddonIdTagsTag_1(id, tag, addonId, body)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganisationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    OrganisationsApi apiInstance = new OrganisationsApi(defaultClient);
    String id = "id_example"; // String | 
    String tag = "tag_example"; // String | 
    String addonId = "addonId_example"; // String | 
    Body body = new Body(); // Body | 
    try {
      apiInstance.putOrganisationsIdAddonsAddonIdTagsTag_1(id, tag, addonId, body);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganisationsApi#putOrganisationsIdAddonsAddonIdTagsTag_1");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**|  | |
| **tag** | **String**|  | |
| **addonId** | **String**|  | |
| **body** | [**Body**](Body.md)|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | addAddonTag |  -  |

<a id="putOrganisationsIdAddonsAddonId_1"></a>
# **putOrganisationsIdAddonsAddonId_1**
> Addon putOrganisationsIdAddonsAddonId_1(id, addonId, wannabeAddon)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganisationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    OrganisationsApi apiInstance = new OrganisationsApi(defaultClient);
    String id = "id_example"; // String | 
    String addonId = "addonId_example"; // String | 
    WannabeAddon wannabeAddon = new WannabeAddon(); // WannabeAddon | 
    try {
      Addon result = apiInstance.putOrganisationsIdAddonsAddonId_1(id, addonId, wannabeAddon);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganisationsApi#putOrganisationsIdAddonsAddonId_1");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**|  | |
| **addonId** | **String**|  | |
| **wannabeAddon** | [**WannabeAddon**](WannabeAddon.md)|  | |

### Return type

[**Addon**](Addon.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Update addon information |  -  |

<a id="putOrganisationsIdApplicationsAppIdDependenciesDependencyId_1"></a>
# **putOrganisationsIdApplicationsAppIdDependenciesDependencyId_1**
> putOrganisationsIdApplicationsAppIdDependenciesDependencyId_1(dependencyId, appId, id, body)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganisationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    OrganisationsApi apiInstance = new OrganisationsApi(defaultClient);
    String dependencyId = "dependencyId_example"; // String | 
    String appId = "appId_example"; // String | 
    String id = "id_example"; // String | 
    Body body = new Body(); // Body | 
    try {
      apiInstance.putOrganisationsIdApplicationsAppIdDependenciesDependencyId_1(dependencyId, appId, id, body);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganisationsApi#putOrganisationsIdApplicationsAppIdDependenciesDependencyId_1");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **dependencyId** | **String**|  | |
| **appId** | **String**|  | |
| **id** | **String**|  | |
| **body** | [**Body**](Body.md)|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | addApplicationDependency |  -  |

<a id="putOrganisationsIdApplicationsAppIdEnvEnvName_1"></a>
# **putOrganisationsIdApplicationsAppIdEnvEnvName_1**
> ListEnv putOrganisationsIdApplicationsAppIdEnvEnvName_1(id, appId, envName, wannabeEnv)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganisationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    OrganisationsApi apiInstance = new OrganisationsApi(defaultClient);
    String id = "id_example"; // String | 
    String appId = "appId_example"; // String | 
    String envName = "envName_example"; // String | 
    WannabeEnv wannabeEnv = new WannabeEnv(); // WannabeEnv | 
    try {
      ListEnv result = apiInstance.putOrganisationsIdApplicationsAppIdEnvEnvName_1(id, appId, envName, wannabeEnv);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganisationsApi#putOrganisationsIdApplicationsAppIdEnvEnvName_1");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**|  | |
| **appId** | **String**|  | |
| **envName** | **String**|  | |
| **wannabeEnv** | [**WannabeEnv**](WannabeEnv.md)|  | |

### Return type

[**ListEnv**](ListEnv.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | editApplicationEnv |  -  |

<a id="putOrganisationsIdApplicationsAppIdEnv_1"></a>
# **putOrganisationsIdApplicationsAppIdEnv_1**
> ListEnv putOrganisationsIdApplicationsAppIdEnv_1(id, appId, wannabeEnv)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganisationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    OrganisationsApi apiInstance = new OrganisationsApi(defaultClient);
    String id = "id_example"; // String | 
    String appId = "appId_example"; // String | 
    WannabeEnv wannabeEnv = new WannabeEnv(); // WannabeEnv | 
    try {
      ListEnv result = apiInstance.putOrganisationsIdApplicationsAppIdEnv_1(id, appId, wannabeEnv);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganisationsApi#putOrganisationsIdApplicationsAppIdEnv_1");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**|  | |
| **appId** | **String**|  | |
| **wannabeEnv** | [**WannabeEnv**](WannabeEnv.md)|  | |

### Return type

[**ListEnv**](ListEnv.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | editApplicationEnvironment |  -  |

<a id="putOrganisationsIdApplicationsAppIdTagsTag_1"></a>
# **putOrganisationsIdApplicationsAppIdTagsTag_1**
> putOrganisationsIdApplicationsAppIdTagsTag_1(id, appId, tag, body)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganisationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    OrganisationsApi apiInstance = new OrganisationsApi(defaultClient);
    String id = "id_example"; // String | 
    String appId = "appId_example"; // String | 
    String tag = "tag_example"; // String | 
    Body body = new Body(); // Body | 
    try {
      apiInstance.putOrganisationsIdApplicationsAppIdTagsTag_1(id, appId, tag, body);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganisationsApi#putOrganisationsIdApplicationsAppIdTagsTag_1");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**|  | |
| **appId** | **String**|  | |
| **tag** | **String**|  | |
| **body** | [**Body**](Body.md)|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | addApplicationTag |  -  |

<a id="putOrganisationsIdApplicationsAppIdVhostsDomain_1"></a>
# **putOrganisationsIdApplicationsAppIdVhostsDomain_1**
> putOrganisationsIdApplicationsAppIdVhostsDomain_1(id, appId, domain, vhost)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganisationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    OrganisationsApi apiInstance = new OrganisationsApi(defaultClient);
    String id = "id_example"; // String | 
    String appId = "appId_example"; // String | 
    String domain = "domain_example"; // String | 
    Vhost vhost = new Vhost(); // Vhost | 
    try {
      apiInstance.putOrganisationsIdApplicationsAppIdVhostsDomain_1(id, appId, domain, vhost);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganisationsApi#putOrganisationsIdApplicationsAppIdVhostsDomain_1");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**|  | |
| **appId** | **String**|  | |
| **domain** | **String**|  | |
| **vhost** | [**Vhost**](Vhost.md)|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | addVhost |  -  |

<a id="putOrganisationsIdApplicationsAppIdVhostsFavourite_1"></a>
# **putOrganisationsIdApplicationsAppIdVhostsFavourite_1**
> putOrganisationsIdApplicationsAppIdVhostsFavourite_1(id, appId, vhost)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganisationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    OrganisationsApi apiInstance = new OrganisationsApi(defaultClient);
    String id = "id_example"; // String | 
    String appId = "appId_example"; // String | 
    Vhost vhost = new Vhost(); // Vhost | 
    try {
      apiInstance.putOrganisationsIdApplicationsAppIdVhostsFavourite_1(id, appId, vhost);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganisationsApi#putOrganisationsIdApplicationsAppIdVhostsFavourite_1");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**|  | |
| **appId** | **String**|  | |
| **vhost** | [**Vhost**](Vhost.md)|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | markFavouriteVhost |  -  |

<a id="putOrganisationsIdApplicationsAppId_1"></a>
# **putOrganisationsIdApplicationsAppId_1**
> Application putOrganisationsIdApplicationsAppId_1(id, appId, wannabeApplication)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganisationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    OrganisationsApi apiInstance = new OrganisationsApi(defaultClient);
    String id = "id_example"; // String | 
    String appId = "appId_example"; // String | 
    WannabeApplication wannabeApplication = new WannabeApplication(); // WannabeApplication | 
    try {
      Application result = apiInstance.putOrganisationsIdApplicationsAppId_1(id, appId, wannabeApplication);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganisationsApi#putOrganisationsIdApplicationsAppId_1");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**|  | |
| **appId** | **String**|  | |
| **wannabeApplication** | [**WannabeApplication**](WannabeApplication.md)|  | |

### Return type

[**Application**](Application.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | editApplication |  -  |

<a id="putOrganisationsIdAvatar_0"></a>
# **putOrganisationsIdAvatar_0**
> putOrganisationsIdAvatar_0(id)



If you want to upload an image from your computer, send the image in the body of the request without anything else.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganisationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    OrganisationsApi apiInstance = new OrganisationsApi(defaultClient);
    String id = "id_example"; // String | 
    try {
      apiInstance.putOrganisationsIdAvatar_0(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganisationsApi#putOrganisationsIdAvatar_0");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | setOrgaAvatar setOrgaAvatarFromSource |  -  |

<a id="putOrganisationsIdConsumersKey_0"></a>
# **putOrganisationsIdConsumersKey_0**
> putOrganisationsIdConsumersKey_0(id, key, wannabeConsumer)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganisationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    OrganisationsApi apiInstance = new OrganisationsApi(defaultClient);
    String id = "id_example"; // String | 
    String key = "key_example"; // String | 
    WannabeConsumer wannabeConsumer = new WannabeConsumer(); // WannabeConsumer | 
    try {
      apiInstance.putOrganisationsIdConsumersKey_0(id, key, wannabeConsumer);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganisationsApi#putOrganisationsIdConsumersKey_0");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**|  | |
| **key** | **String**|  | |
| **wannabeConsumer** | [**WannabeConsumer**](WannabeConsumer.md)|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | PUT the same data as in POST. |  -  |

<a id="putOrganisationsIdMembersUserId_0"></a>
# **putOrganisationsIdMembersUserId_0**
> putOrganisationsIdMembersUserId_0(id, userId, body)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganisationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    OrganisationsApi apiInstance = new OrganisationsApi(defaultClient);
    String id = "id_example"; // String | 
    String userId = "userId_example"; // String | 
    Schema2 body = new Schema2(); // Schema2 | 
    try {
      apiInstance.putOrganisationsIdMembersUserId_0(id, userId, body);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganisationsApi#putOrganisationsIdMembersUserId_0");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**|  | |
| **userId** | **String**|  | |
| **body** | **Schema2**|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | editOrganisationMember |  -  |

<a id="putOrganisationsIdPaymentsBillingsBid_0"></a>
# **putOrganisationsIdPaymentsBillingsBid_0**
> putOrganisationsIdPaymentsBillingsBid_0(id, bid)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganisationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    OrganisationsApi apiInstance = new OrganisationsApi(defaultClient);
    String id = "id_example"; // String | 
    String bid = "bid_example"; // String | 
    try {
      apiInstance.putOrganisationsIdPaymentsBillingsBid_0(id, bid);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganisationsApi#putOrganisationsIdPaymentsBillingsBid_0");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**|  | |
| **bid** | **String**|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | choosePaymentProvider |  -  |

<a id="putOrganisationsId_0"></a>
# **putOrganisationsId_0**
> Organisation putOrganisationsId_0(id, wannabeOrganisation)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganisationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    OrganisationsApi apiInstance = new OrganisationsApi(defaultClient);
    String id = "id_example"; // String | 
    WannabeOrganisation wannabeOrganisation = new WannabeOrganisation(); // WannabeOrganisation | 
    try {
      Organisation result = apiInstance.putOrganisationsId_0(id, wannabeOrganisation);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganisationsApi#putOrganisationsId_0");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**|  | |
| **wannabeOrganisation** | [**WannabeOrganisation**](WannabeOrganisation.md)|  | |

### Return type

[**Organisation**](Organisation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | editOrganisation |  -  |

