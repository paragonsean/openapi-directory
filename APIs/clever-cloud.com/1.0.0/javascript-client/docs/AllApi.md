# CleverCloudApi.AllApi

All URIs are relative to *https://api.clever-cloud.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**applicationAppIdEnvironmentGet**](AllApi.md#applicationAppIdEnvironmentGet) | **GET** /application/{appId}/environment | 
[**applicationAppIdEnvironmentPut**](AllApi.md#applicationAppIdEnvironmentPut) | **PUT** /application/{appId}/environment | 
[**createMatomo**](AllApi.md#createMatomo) | **POST** /v2/providers/addon-matomo/resources | Create Matomo addon
[**createNetworkGroup**](AllApi.md#createNetworkGroup) | **POST** /v4/networkgroups/organisations/{ownerId}/networkgroups | Create Network Group
[**createNetworkGroupExternalPeer**](AllApi.md#createNetworkGroupExternalPeer) | **POST** /v4/networkgroups/organisations/{ownerId}/networkgroups/{networkGroupId}/external-peers | Add external peer
[**createNetworkGroupMember**](AllApi.md#createNetworkGroupMember) | **POST** /v4/networkgroups/organisations/{ownerId}/networkgroups/{networkGroupId}/members | Add member
[**deleteGithubLink**](AllApi.md#deleteGithubLink) | **DELETE** /github/link | 
[**deleteMatomo**](AllApi.md#deleteMatomo) | **DELETE** /v2/providers/addon-matomo/resources/{matomoId} | Delete Matomo addon
[**deleteNetworkGroup**](AllApi.md#deleteNetworkGroup) | **DELETE** /v4/networkgroups/organisations/{ownerId}/networkgroups/{networkGroupId} | Delete Network Group
[**deleteNetworkGroupExternalPeer**](AllApi.md#deleteNetworkGroupExternalPeer) | **DELETE** /v4/networkgroups/organisations/{ownerId}/networkgroups/{networkGroupId}/external-peers/{peerId} | Remove external peer
[**deleteNetworkGroupMember**](AllApi.md#deleteNetworkGroupMember) | **DELETE** /v4/networkgroups/organisations/{ownerId}/networkgroups/{networkGroupId}/members/{memberId} | Remove member
[**deleteNetworkGroupPeer**](AllApi.md#deleteNetworkGroupPeer) | **DELETE** /v4/networkgroups/organisations/{ownerId}/networkgroups/{networkGroupId}/peers/{peerId} | Remove peer
[**deleteOrganisationsId**](AllApi.md#deleteOrganisationsId) | **DELETE** /organisations/{id} | 
[**deleteOrganisationsIdAddonprovidersProviderIdFeaturesFeatureId**](AllApi.md#deleteOrganisationsIdAddonprovidersProviderIdFeaturesFeatureId) | **DELETE** /organisations/{id}/addonproviders/{providerId}/features/{featureId} | 
[**deleteOrganisationsIdAddonprovidersProviderIdPlansPlanId**](AllApi.md#deleteOrganisationsIdAddonprovidersProviderIdPlansPlanId) | **DELETE** /organisations/{id}/addonproviders/{providerId}/plans/{planId} | 
[**deleteOrganisationsIdAddonprovidersProviderIdPlansPlanIdFeaturesFeatureName**](AllApi.md#deleteOrganisationsIdAddonprovidersProviderIdPlansPlanIdFeaturesFeatureName) | **DELETE** /organisations/{id}/addonproviders/{providerId}/plans/{planId}/features/{featureName} | 
[**deleteOrganisationsIdAddonsAddonId**](AllApi.md#deleteOrganisationsIdAddonsAddonId) | **DELETE** /organisations/{id}/addons/{addonId} | 
[**deleteOrganisationsIdAddonsAddonIdTagsTag**](AllApi.md#deleteOrganisationsIdAddonsAddonIdTagsTag) | **DELETE** /organisations/{id}/addons/{addonId}/tags/{tag} | 
[**deleteOrganisationsIdApplicationsAppId**](AllApi.md#deleteOrganisationsIdApplicationsAppId) | **DELETE** /organisations/{id}/applications/{appId} | 
[**deleteOrganisationsIdApplicationsAppIdAddonsAddonId**](AllApi.md#deleteOrganisationsIdApplicationsAppIdAddonsAddonId) | **DELETE** /organisations/{id}/applications/{appId}/addons/{addonId} | 
[**deleteOrganisationsIdApplicationsAppIdDependenciesDependencyId**](AllApi.md#deleteOrganisationsIdApplicationsAppIdDependenciesDependencyId) | **DELETE** /organisations/{id}/applications/{appId}/dependencies/{dependencyId} | 
[**deleteOrganisationsIdApplicationsAppIdDeploymentsDeploymentIdInstances**](AllApi.md#deleteOrganisationsIdApplicationsAppIdDeploymentsDeploymentIdInstances) | **DELETE** /organisations/{id}/applications/{appId}/deployments/{deploymentId}/instances | 
[**deleteOrganisationsIdApplicationsAppIdEnvEnvName**](AllApi.md#deleteOrganisationsIdApplicationsAppIdEnvEnvName) | **DELETE** /organisations/{id}/applications/{appId}/env/{envName} | 
[**deleteOrganisationsIdApplicationsAppIdInstances**](AllApi.md#deleteOrganisationsIdApplicationsAppIdInstances) | **DELETE** /organisations/{id}/applications/{appId}/instances | 
[**deleteOrganisationsIdApplicationsAppIdTagsTag**](AllApi.md#deleteOrganisationsIdApplicationsAppIdTagsTag) | **DELETE** /organisations/{id}/applications/{appId}/tags/{tag} | 
[**deleteOrganisationsIdApplicationsAppIdVhostsDomain**](AllApi.md#deleteOrganisationsIdApplicationsAppIdVhostsDomain) | **DELETE** /organisations/{id}/applications/{appId}/vhosts/{domain} | 
[**deleteOrganisationsIdApplicationsAppIdVhostsFavourite**](AllApi.md#deleteOrganisationsIdApplicationsAppIdVhostsFavourite) | **DELETE** /organisations/{id}/applications/{appId}/vhosts/favourite | 
[**deleteOrganisationsIdConsumersKey**](AllApi.md#deleteOrganisationsIdConsumersKey) | **DELETE** /organisations/{id}/consumers/{key} | 
[**deleteOrganisationsIdMembersUserId**](AllApi.md#deleteOrganisationsIdMembersUserId) | **DELETE** /organisations/{id}/members/{userId} | 
[**deleteOrganisationsIdPaymentsBillingsBid**](AllApi.md#deleteOrganisationsIdPaymentsBillingsBid) | **DELETE** /organisations/{id}/payments/billings/{bid} | 
[**deleteOrganisationsIdPaymentsRecurring**](AllApi.md#deleteOrganisationsIdPaymentsRecurring) | **DELETE** /organisations/{id}/payments/recurring | 
[**deleteSelf**](AllApi.md#deleteSelf) | **DELETE** /self | 
[**deleteSelfAddonsAddonId**](AllApi.md#deleteSelfAddonsAddonId) | **DELETE** /self/addons/{addonId} | 
[**deleteSelfAddonsAddonIdTagsTag**](AllApi.md#deleteSelfAddonsAddonIdTagsTag) | **DELETE** /self/addons/{addonId}/tags/{tag} | 
[**deleteSelfApplicationsAppId**](AllApi.md#deleteSelfApplicationsAppId) | **DELETE** /self/applications/{appId} | 
[**deleteSelfApplicationsAppIdAddonsAddonId**](AllApi.md#deleteSelfApplicationsAppIdAddonsAddonId) | **DELETE** /self/applications/{appId}/addons/{addonId} | 
[**deleteSelfApplicationsAppIdDependenciesDependencyId**](AllApi.md#deleteSelfApplicationsAppIdDependenciesDependencyId) | **DELETE** /self/applications/{appId}/dependencies/{dependencyId} | 
[**deleteSelfApplicationsAppIdDeploymentsDeploymentIdInstances**](AllApi.md#deleteSelfApplicationsAppIdDeploymentsDeploymentIdInstances) | **DELETE** /self/applications/{appId}/deployments/{deploymentId}/instances | 
[**deleteSelfApplicationsAppIdEnvEnvName**](AllApi.md#deleteSelfApplicationsAppIdEnvEnvName) | **DELETE** /self/applications/{appId}/env/{envName} | 
[**deleteSelfApplicationsAppIdInstances**](AllApi.md#deleteSelfApplicationsAppIdInstances) | **DELETE** /self/applications/{appId}/instances | 
[**deleteSelfApplicationsAppIdTagsTag**](AllApi.md#deleteSelfApplicationsAppIdTagsTag) | **DELETE** /self/applications/{appId}/tags/{tag} | 
[**deleteSelfApplicationsAppIdVhostsDomain**](AllApi.md#deleteSelfApplicationsAppIdVhostsDomain) | **DELETE** /self/applications/{appId}/vhosts/{domain} | 
[**deleteSelfApplicationsAppIdVhostsFavourite**](AllApi.md#deleteSelfApplicationsAppIdVhostsFavourite) | **DELETE** /self/applications/{appId}/vhosts/favourite | 
[**deleteSelfConsumersKey**](AllApi.md#deleteSelfConsumersKey) | **DELETE** /self/consumers/{key} | 
[**deleteSelfEmailsEmail**](AllApi.md#deleteSelfEmailsEmail) | **DELETE** /self/emails/{email} | 
[**deleteSelfKeysKey**](AllApi.md#deleteSelfKeysKey) | **DELETE** /self/keys/{key} | 
[**deleteSelfPaymentsBillingsBid**](AllApi.md#deleteSelfPaymentsBillingsBid) | **DELETE** /self/payments/billings/{bid} | 
[**deleteSelfPaymentsMethodsMId**](AllApi.md#deleteSelfPaymentsMethodsMId) | **DELETE** /self/payments/methods/{mId} | 
[**deleteSelfPaymentsRecurring**](AllApi.md#deleteSelfPaymentsRecurring) | **DELETE** /self/payments/recurring | 
[**deleteSelfTokens**](AllApi.md#deleteSelfTokens) | **DELETE** /self/tokens | 
[**deleteSelfTokensToken**](AllApi.md#deleteSelfTokensToken) | **DELETE** /self/tokens/{token} | 
[**eventsEventSocketGet**](AllApi.md#eventsEventSocketGet) | **GET** /events/event-socket | 
[**getConfigProvider**](AllApi.md#getConfigProvider) | **GET** /v4/addon-providers/config-provider/addons/{configurationProviderId} | Get Addon provider configuration
[**getConfigProviderEnv**](AllApi.md#getConfigProviderEnv) | **GET** /v4/addon-providers/config-provider/addons/{configurationProviderId}/env | Get provider&#39;s addon environment
[**getGithub**](AllApi.md#getGithub) | **GET** /github | 
[**getGithubApplications**](AllApi.md#getGithubApplications) | **GET** /github/applications | 
[**getGithubCallback**](AllApi.md#getGithubCallback) | **GET** /github/callback | 
[**getGithubEmails**](AllApi.md#getGithubEmails) | **GET** /github/emails | 
[**getGithubKeys**](AllApi.md#getGithubKeys) | **GET** /github/keys | 
[**getGithubLink**](AllApi.md#getGithubLink) | **GET** /github/link | 
[**getGithubLogin**](AllApi.md#getGithubLogin) | **GET** /github/login | 
[**getGithubSignup**](AllApi.md#getGithubSignup) | **GET** /github/signup | 
[**getGithubUsername**](AllApi.md#getGithubUsername) | **GET** /github/username | 
[**getMatomo**](AllApi.md#getMatomo) | **GET** /v4/addon-providers/addon-matomo/addons/{matomoId} | Get Matomo addon
[**getMatomoKTokenValidation**](AllApi.md#getMatomoKTokenValidation) | **GET** /v4/addon-providers/addon-matomo/token/validate | Validate a keycloak token
[**getNetworkGroup**](AllApi.md#getNetworkGroup) | **GET** /v4/networkgroups/organisations/{ownerId}/networkgroups/{networkGroupId} | Get Network Group
[**getNetworkGroupMember**](AllApi.md#getNetworkGroupMember) | **GET** /v4/networkgroups/organisations/{ownerId}/networkgroups/{networkGroupId}/members/{memberId} | Get member
[**getNetworkGroupPeer**](AllApi.md#getNetworkGroupPeer) | **GET** /v4/networkgroups/organisations/{ownerId}/networkgroups/{networkGroupId}/peers/{peerId} | Get peer
[**getNetworkGroupStream**](AllApi.md#getNetworkGroupStream) | **GET** /v4/networkgroups/organisations/{ownerId}/networkgroups/{networkGroupId}/stream | Network Group SSE
[**getNetworkGroupWireGuardConfiguration**](AllApi.md#getNetworkGroupWireGuardConfiguration) | **GET** /v4/networkgroups/organisations/{ownerId}/networkgroups/{networkGroupId}/peers/{peerId}/wireguard/configuration | Get WireGuard® configuration
[**getNetworkGroupWireGuardConfigurationStream**](AllApi.md#getNetworkGroupWireGuardConfigurationStream) | **GET** /v4/networkgroups/organisations/{ownerId}/networkgroups/{networkGroupId}/peers/{peerId}/wireguard/configuration/stream | Get WireGuard® configuration
[**getNewsfeedEngineering**](AllApi.md#getNewsfeedEngineering) | **GET** /newsfeeds/engineering | 
[**getNewsfeedsBlog**](AllApi.md#getNewsfeedsBlog) | **GET** /newsfeeds/blog | 
[**getOauthAuthorize**](AllApi.md#getOauthAuthorize) | **GET** /oauth/authorize | 
[**getOauthRights**](AllApi.md#getOauthRights) | **GET** /oauth/rights | 
[**getOrganisations**](AllApi.md#getOrganisations) | **GET** /organisations | 
[**getOrganisationsId**](AllApi.md#getOrganisationsId) | **GET** /organisations/{id} | 
[**getOrganisationsIdAddonproviders**](AllApi.md#getOrganisationsIdAddonproviders) | **GET** /organisations/{id}/addonproviders | 
[**getOrganisationsIdAddonprovidersProviderId**](AllApi.md#getOrganisationsIdAddonprovidersProviderId) | **GET** /organisations/{id}/addonproviders/{providerId} | 
[**getOrganisationsIdAddonprovidersProviderIdFeatures**](AllApi.md#getOrganisationsIdAddonprovidersProviderIdFeatures) | **GET** /organisations/{id}/addonproviders/{providerId}/features | 
[**getOrganisationsIdAddonprovidersProviderIdPlans**](AllApi.md#getOrganisationsIdAddonprovidersProviderIdPlans) | **GET** /organisations/{id}/addonproviders/{providerId}/plans | 
[**getOrganisationsIdAddonprovidersProviderIdPlansPlanId**](AllApi.md#getOrganisationsIdAddonprovidersProviderIdPlansPlanId) | **GET** /organisations/{id}/addonproviders/{providerId}/plans/{planId} | 
[**getOrganisationsIdAddonprovidersProviderIdTags**](AllApi.md#getOrganisationsIdAddonprovidersProviderIdTags) | **GET** /organisations/{id}/addonproviders/{providerId}/tags | 
[**getOrganisationsIdAddons**](AllApi.md#getOrganisationsIdAddons) | **GET** /organisations/{id}/addons | 
[**getOrganisationsIdAddonsAddonId**](AllApi.md#getOrganisationsIdAddonsAddonId) | **GET** /organisations/{id}/addons/{addonId} | 
[**getOrganisationsIdAddonsAddonIdApplications**](AllApi.md#getOrganisationsIdAddonsAddonIdApplications) | **GET** /organisations/{id}/addons/{addonId}/applications | 
[**getOrganisationsIdAddonsAddonIdEnv**](AllApi.md#getOrganisationsIdAddonsAddonIdEnv) | **GET** /organisations/{id}/addons/{addonId}/env | 
[**getOrganisationsIdAddonsAddonIdSso**](AllApi.md#getOrganisationsIdAddonsAddonIdSso) | **GET** /organisations/{id}/addonproviders/{providerId}/sso | 
[**getOrganisationsIdAddonsAddonIdTags**](AllApi.md#getOrganisationsIdAddonsAddonIdTags) | **GET** /organisations/{id}/addons/{addonId}/tags | 
[**getOrganisationsIdApplications**](AllApi.md#getOrganisationsIdApplications) | **GET** /organisations/{id}/applications | 
[**getOrganisationsIdApplicationsAppId**](AllApi.md#getOrganisationsIdApplicationsAppId) | **GET** /organisations/{id}/applications/{appId} | 
[**getOrganisationsIdApplicationsAppIdAddons**](AllApi.md#getOrganisationsIdApplicationsAppIdAddons) | **GET** /organisations/{id}/applications/{appId}/addons | 
[**getOrganisationsIdApplicationsAppIdAddonsEnv**](AllApi.md#getOrganisationsIdApplicationsAppIdAddonsEnv) | **GET** /organisations/{id}/applications/{appId}/addons/env | 
[**getOrganisationsIdApplicationsAppIdDependencies**](AllApi.md#getOrganisationsIdApplicationsAppIdDependencies) | **GET** /organisations/{id}/applications/{appId}/dependencies | 
[**getOrganisationsIdApplicationsAppIdDependents**](AllApi.md#getOrganisationsIdApplicationsAppIdDependents) | **GET** /organisations/{id}/applications/{appId}/dependents | 
[**getOrganisationsIdApplicationsAppIdDeployments**](AllApi.md#getOrganisationsIdApplicationsAppIdDeployments) | **GET** /organisations/{id}/applications/{appId}/deployments | 
[**getOrganisationsIdApplicationsAppIdEnv**](AllApi.md#getOrganisationsIdApplicationsAppIdEnv) | **GET** /organisations/{id}/applications/{appId}/env | 
[**getOrganisationsIdApplicationsAppIdInstances**](AllApi.md#getOrganisationsIdApplicationsAppIdInstances) | **GET** /organisations/{id}/applications/{appId}/instances | 
[**getOrganisationsIdApplicationsAppIdTags**](AllApi.md#getOrganisationsIdApplicationsAppIdTags) | **GET** /organisations/{id}/applications/{appId}/tags | 
[**getOrganisationsIdApplicationsAppIdVhosts**](AllApi.md#getOrganisationsIdApplicationsAppIdVhosts) | **GET** /organisations/{id}/applications/{appId}/vhosts | 
[**getOrganisationsIdApplicationsAppIdVhostsFavourite**](AllApi.md#getOrganisationsIdApplicationsAppIdVhostsFavourite) | **GET** /organisations/{id}/applications/{appId}/vhosts/favourite | 
[**getOrganisationsIdConsumers**](AllApi.md#getOrganisationsIdConsumers) | **GET** /organisations/{id}/consumers | 
[**getOrganisationsIdConsumersKey**](AllApi.md#getOrganisationsIdConsumersKey) | **GET** /organisations/{id}/consumers/{key} | 
[**getOrganisationsIdConsumersKeySecret**](AllApi.md#getOrganisationsIdConsumersKeySecret) | **GET** /organisations/{id}/consumers/{key}/secret | 
[**getOrganisationsIdConsumptions**](AllApi.md#getOrganisationsIdConsumptions) | **GET** /organisations/{id}/consumptions | 
[**getOrganisationsIdCredits**](AllApi.md#getOrganisationsIdCredits) | **GET** /organisations/{id}/credits | 
[**getOrganisationsIdDeployments**](AllApi.md#getOrganisationsIdDeployments) | **GET** /organisations/{id}/deployments | 
[**getOrganisationsIdInstances**](AllApi.md#getOrganisationsIdInstances) | **GET** /organisations/{id}/instances | 
[**getOrganisationsIdMembers**](AllApi.md#getOrganisationsIdMembers) | **GET** /organisations/{id}/members | 
[**getOrganisationsIdPaymentInfo**](AllApi.md#getOrganisationsIdPaymentInfo) | **GET** /organisations/{id}/payment-info | 
[**getOrganisationsIdPaymentsBillings**](AllApi.md#getOrganisationsIdPaymentsBillings) | **GET** /organisations/{id}/payments/billings | 
[**getOrganisationsIdPaymentsBillingsBid**](AllApi.md#getOrganisationsIdPaymentsBillingsBid) | **GET** /organisations/{id}/payments/billings/{bid} | 
[**getOrganisationsIdPaymentsBillingsBidPdf**](AllApi.md#getOrganisationsIdPaymentsBillingsBidPdf) | **GET** /organisations/{id}/payments/billings/{bid}.pdf | 
[**getOrganisationsIdPaymentsFullPricePrice**](AllApi.md#getOrganisationsIdPaymentsFullPricePrice) | **GET** /organisations/{id}/payments/fullprice/{price} | 
[**getPasswordForgotten**](AllApi.md#getPasswordForgotten) | **GET** /password_forgotten | 
[**getPasswordForgottenKey**](AllApi.md#getPasswordForgottenKey) | **GET** /password_forgotten/{key} | 
[**getPaymentsCouponsName**](AllApi.md#getPaymentsCouponsName) | **GET** /payments/coupons/{name} | 
[**getPaymentsProviders**](AllApi.md#getPaymentsProviders) | **GET** /payments/providers | 
[**getPaymentsTokensStripe**](AllApi.md#getPaymentsTokensStripe) | **GET** /payments/tokens/stripe | 
[**getProductsAddonProviders**](AllApi.md#getProductsAddonProviders) | **GET** /products/addonproviders | 
[**getProductsAddonProvidersProviderId**](AllApi.md#getProductsAddonProvidersProviderId) | **GET** /products/addonproviders/{provider_id} | 
[**getProductsCountries**](AllApi.md#getProductsCountries) | **GET** /products/countries | 
[**getProductsCountrycodes**](AllApi.md#getProductsCountrycodes) | **GET** /products/countrycodes | 
[**getProductsInstances**](AllApi.md#getProductsInstances) | **GET** /products/instances | 
[**getProductsInstancesTypeVersion**](AllApi.md#getProductsInstancesTypeVersion) | **GET** /products/instances/{type}-{version} | 
[**getProductsPackages**](AllApi.md#getProductsPackages) | **GET** /products/packages | 
[**getProductsPrices**](AllApi.md#getProductsPrices) | **GET** /products/prices | 
[**getProductsZones**](AllApi.md#getProductsZones) | **GET** /products/zones | 
[**getSelf**](AllApi.md#getSelf) | **GET** /self | 
[**getSelfAddons**](AllApi.md#getSelfAddons) | **GET** /self/addons | Addon
[**getSelfAddonsAddonId**](AllApi.md#getSelfAddonsAddonId) | **GET** /self/addons/{addonId} | Specific addon
[**getSelfAddonsAddonIdApplications**](AllApi.md#getSelfAddonsAddonIdApplications) | **GET** /self/addons/{addonId}/applications | 
[**getSelfAddonsAddonIdEnv**](AllApi.md#getSelfAddonsAddonIdEnv) | **GET** /self/addons/{addonId}/env | 
[**getSelfAddonsAddonIdSso**](AllApi.md#getSelfAddonsAddonIdSso) | **GET** /self/addons/{addonId}/sso | 
[**getSelfAddonsAddonIdTags**](AllApi.md#getSelfAddonsAddonIdTags) | **GET** /self/addons/{addonId}/tags | 
[**getSelfApplications**](AllApi.md#getSelfApplications) | **GET** /self/applications | 
[**getSelfApplicationsAppId**](AllApi.md#getSelfApplicationsAppId) | **GET** /self/applications/{appId} | 
[**getSelfApplicationsAppIdAddons**](AllApi.md#getSelfApplicationsAppIdAddons) | **GET** /self/applications/{appId}/addons | 
[**getSelfApplicationsAppIdAddonsEnv**](AllApi.md#getSelfApplicationsAppIdAddonsEnv) | **GET** /self/applications/{appId}/addons/env | 
[**getSelfApplicationsAppIdDependencies**](AllApi.md#getSelfApplicationsAppIdDependencies) | **GET** /self/applications/{appId}/dependencies | 
[**getSelfApplicationsAppIdDependenciesDependencyId**](AllApi.md#getSelfApplicationsAppIdDependenciesDependencyId) | **PUT** /self/applications/{appId}/dependencies/{dependencyId} | 
[**getSelfApplicationsAppIdDependents**](AllApi.md#getSelfApplicationsAppIdDependents) | **GET** /self/applications/{appId}/dependents | 
[**getSelfApplicationsAppIdDeployments**](AllApi.md#getSelfApplicationsAppIdDeployments) | **GET** /self/applications/{appId}/deployments | 
[**getSelfApplicationsAppIdEnv**](AllApi.md#getSelfApplicationsAppIdEnv) | **GET** /self/applications/{appId}/env | 
[**getSelfApplicationsAppIdInstances**](AllApi.md#getSelfApplicationsAppIdInstances) | **GET** /self/applications/{appId}/instances | 
[**getSelfApplicationsAppIdTags**](AllApi.md#getSelfApplicationsAppIdTags) | **GET** /self/applications/{appId}/tags | 
[**getSelfApplicationsAppIdVhosts**](AllApi.md#getSelfApplicationsAppIdVhosts) | **GET** /self/applications/{appId}/vhosts | 
[**getSelfApplicationsAppIdVhostsFavourite**](AllApi.md#getSelfApplicationsAppIdVhostsFavourite) | **GET** /self/applications/{appId}/vhosts/favourite | 
[**getSelfConfirmationEmail**](AllApi.md#getSelfConfirmationEmail) | **GET** /self/confirmation_email | 
[**getSelfConsumers**](AllApi.md#getSelfConsumers) | **GET** /self/consumers | 
[**getSelfConsumersKey**](AllApi.md#getSelfConsumersKey) | **GET** /self/consumers/{key} | 
[**getSelfConsumersKeySecret**](AllApi.md#getSelfConsumersKeySecret) | **GET** /self/consumers/{key}/secret | 
[**getSelfConsumptions**](AllApi.md#getSelfConsumptions) | **GET** /self/consumptions | 
[**getSelfCredits**](AllApi.md#getSelfCredits) | **GET** /self/credits | 
[**getSelfEmails**](AllApi.md#getSelfEmails) | **GET** /self/emails | 
[**getSelfId**](AllApi.md#getSelfId) | **GET** /self/id | 
[**getSelfInstances**](AllApi.md#getSelfInstances) | **GET** /self/instances | 
[**getSelfKeys**](AllApi.md#getSelfKeys) | **GET** /self/keys | 
[**getSelfPaymentInfo**](AllApi.md#getSelfPaymentInfo) | **GET** /self/payment-info | 
[**getSelfPaymentsBillings**](AllApi.md#getSelfPaymentsBillings) | **GET** /self/payments/billings | 
[**getSelfPaymentsBillingsBid**](AllApi.md#getSelfPaymentsBillingsBid) | **GET** /self/payments/billings/{bid} | 
[**getSelfPaymentsBillingsBidPdf**](AllApi.md#getSelfPaymentsBillingsBidPdf) | **GET** /self/payments/billings/{bid}.pdf | 
[**getSelfPaymentsFullpricePrice**](AllApi.md#getSelfPaymentsFullpricePrice) | **GET** /self/payments/fullprice/{price} | 
[**getSelfPaymentsMethods**](AllApi.md#getSelfPaymentsMethods) | **GET** /self/payments/methods | 
[**getSelfTokens**](AllApi.md#getSelfTokens) | **GET** /self/tokens | 
[**getSelfValidateEmail**](AllApi.md#getSelfValidateEmail) | **GET** /self/validate_email | 
[**getSummary**](AllApi.md#getSummary) | **GET** /summary | 
[**getUsersId**](AllApi.md#getUsersId) | **GET** /users/{id} | 
[**getUsersIdApplications**](AllApi.md#getUsersIdApplications) | **GET** /users/{id}/applications | 
[**getUsersUserIdGitInfo**](AllApi.md#getUsersUserIdGitInfo) | **GET** /users/{userId}/git-info | 
[**getVendorApps**](AllApi.md#getVendorApps) | **GET** /vendor/apps | 
[**getVendorAppsAddonId**](AllApi.md#getVendorAppsAddonId) | **GET** /vendor/apps/{addonId} | 
[**listNetworkGroupMembers**](AllApi.md#listNetworkGroupMembers) | **GET** /v4/networkgroups/organisations/{ownerId}/networkgroups/{networkGroupId}/members | List members
[**listNetworkGroupPeers**](AllApi.md#listNetworkGroupPeers) | **GET** /v4/networkgroups/organisations/{ownerId}/networkgroups/{networkGroupId}/peers | List peers
[**listNetworkGroups**](AllApi.md#listNetworkGroups) | **GET** /v4/networkgroups/organisations/{ownerId}/networkgroups | List Network Groups
[**logsAppIdDrainsGet**](AllApi.md#logsAppIdDrainsGet) | **GET** /logs/{appId}/drains | 
[**logsAppIdDrainsIdOrUrlDelete**](AllApi.md#logsAppIdDrainsIdOrUrlDelete) | **DELETE** /logs/{appId}/drains/:idOrUrl | 
[**logsAppIdDrainsIdOrUrlGet**](AllApi.md#logsAppIdDrainsIdOrUrlGet) | **GET** /logs/{appId}/drains/:idOrUrl | 
[**logsAppIdDrainsPost**](AllApi.md#logsAppIdDrainsPost) | **POST** /logs/{appId}/drains | 
[**logsAppIdGet**](AllApi.md#logsAppIdGet) | **GET** /logs/{appId} | 
[**logsAppIdSseGet**](AllApi.md#logsAppIdSseGet) | **GET** /logs/{appId}/sse | 
[**logsDrainsDrainIdPut**](AllApi.md#logsDrainsDrainIdPut) | **PUT** /logs/drains/{drainId} | 
[**logsDrainsGet**](AllApi.md#logsDrainsGet) | **GET** /logs/drains | 
[**logsLogsChunkedAppIdGet**](AllApi.md#logsLogsChunkedAppIdGet) | **GET** /logs/logs-chunked/{appId} | 
[**logsLogsSocketAppIdGet**](AllApi.md#logsLogsSocketAppIdGet) | **GET** /logs/logs-socket/{appId} | 
[**logsSocketAppIdGet**](AllApi.md#logsSocketAppIdGet) | **GET** /logs-socket/{appId} | 
[**notificationsEmailhooksOwnerIdGet**](AllApi.md#notificationsEmailhooksOwnerIdGet) | **GET** /notifications/emailhooks/{ownerId} | 
[**notificationsEmailhooksOwnerIdIdDelete**](AllApi.md#notificationsEmailhooksOwnerIdIdDelete) | **DELETE** /notifications/emailhooks/{ownerId}/:id | 
[**notificationsEmailhooksOwnerIdIdPut**](AllApi.md#notificationsEmailhooksOwnerIdIdPut) | **PUT** /notifications/emailhooks/{ownerId}/:id | 
[**notificationsEmailhooksOwnerIdPost**](AllApi.md#notificationsEmailhooksOwnerIdPost) | **POST** /notifications/emailhooks/{ownerId} | 
[**notificationsInfoEventsGet**](AllApi.md#notificationsInfoEventsGet) | **GET** /notifications/info/events | 
[**notificationsInfoWebhookformatsGet**](AllApi.md#notificationsInfoWebhookformatsGet) | **GET** /notifications/info/webhookformats | 
[**notificationsWebhooksOwnerIdGet**](AllApi.md#notificationsWebhooksOwnerIdGet) | **GET** /notifications/webhooks/{ownerId} | 
[**notificationsWebhooksOwnerIdIdDelete**](AllApi.md#notificationsWebhooksOwnerIdIdDelete) | **DELETE** /notifications/webhooks/{ownerId}/:id | 
[**notificationsWebhooksOwnerIdIdPut**](AllApi.md#notificationsWebhooksOwnerIdIdPut) | **PUT** /notifications/webhooks/{ownerId}/:id | 
[**notificationsWebhooksOwnerIdPost**](AllApi.md#notificationsWebhooksOwnerIdPost) | **POST** /notifications/webhooks/{ownerId} | 
[**oauthAccessTokenQueryPost**](AllApi.md#oauthAccessTokenQueryPost) | **POST** /oauth/access_token_query | 
[**oauthRequestTokenQueryPost**](AllApi.md#oauthRequestTokenQueryPost) | **POST** /oauth/request_token_query | 
[**openapiGet**](AllApi.md#openapiGet) | **GET** //openapi | 
[**openapiTypeGet**](AllApi.md#openapiTypeGet) | **GET** /openapi.{type} | Get the swagger for this API as {type}
[**organisationsIdAddonprovidersProviderIdDelete**](AllApi.md#organisationsIdAddonprovidersProviderIdDelete) | **DELETE** /organisations/{id}/addonproviders/{providerId} | Remove an add-on provider
[**organisationsIdAddonsAddonIdInstancesGet**](AllApi.md#organisationsIdAddonsAddonIdInstancesGet) | **GET** /organisations/{id}/addons/{addonId}/instances | List instances for this add-on.
[**organisationsIdAddonsAddonIdInstancesInstanceIdGet**](AllApi.md#organisationsIdAddonsAddonIdInstancesInstanceIdGet) | **GET** /organisations/{id}/addons/{addonId}/instances/{instanceId} | Get a specific instance for {addonId}
[**organisationsIdAddonsAddonIdMigrationsGet**](AllApi.md#organisationsIdAddonsAddonIdMigrationsGet) | **GET** /organisations/{id}/addons/{addonId}/migrations | Get past migrations from add-on.
[**organisationsIdAddonsAddonIdMigrationsMigrationIdGet**](AllApi.md#organisationsIdAddonsAddonIdMigrationsMigrationIdGet) | **GET** /organisations/{id}/addons/{addonId}/migrations/{migrationId} | Get a given migration
[**organisationsIdAddonsAddonIdMigrationsPost**](AllApi.md#organisationsIdAddonsAddonIdMigrationsPost) | **POST** /organisations/{id}/addons/{addonId}/migrations | Start a new add-on migration
[**organisationsIdAddonsAddonIdSsoGet**](AllApi.md#organisationsIdAddonsAddonIdSsoGet) | **GET** /organisations/{id}/addons/{addonId}/sso | 
[**organisationsIdAddonsPreordersPost**](AllApi.md#organisationsIdAddonsPreordersPost) | **POST** /organisations/{id}/addons/preorders | 
[**organisationsIdApplicationsAppIdBranchPut**](AllApi.md#organisationsIdApplicationsAppIdBranchPut) | **PUT** /organisations/{id}/applications/{appId}/branch | 
[**organisationsIdApplicationsAppIdBranchesGet**](AllApi.md#organisationsIdApplicationsAppIdBranchesGet) | **GET** /organisations/{id}/applications/{appId}/branches | 
[**organisationsIdApplicationsAppIdBuildflavorPut**](AllApi.md#organisationsIdApplicationsAppIdBuildflavorPut) | **PUT** /organisations/{id}/applications/{appId}/buildflavor | 
[**organisationsIdApplicationsAppIdDependenciesEnvGet**](AllApi.md#organisationsIdApplicationsAppIdDependenciesEnvGet) | **GET** /organisations/{id}/applications/{appId}/dependencies/env | 
[**organisationsIdApplicationsAppIdDeploymentsDeploymentIdGet**](AllApi.md#organisationsIdApplicationsAppIdDeploymentsDeploymentIdGet) | **GET** /organisations/{id}/applications/{appId}/deployments/{deploymentId} | 
[**organisationsIdApplicationsAppIdExposedEnvGet**](AllApi.md#organisationsIdApplicationsAppIdExposedEnvGet) | **GET** /organisations/{id}/applications/{appId}/exposed_env | 
[**organisationsIdApplicationsAppIdExposedEnvPut**](AllApi.md#organisationsIdApplicationsAppIdExposedEnvPut) | **PUT** /organisations/{id}/applications/{appId}/exposed_env | 
[**organisationsIdApplicationsAppIdInstancesInstanceIdGet**](AllApi.md#organisationsIdApplicationsAppIdInstancesInstanceIdGet) | **GET** /organisations/{id}/applications/{appId}/instances/{instanceId} | 
[**organisationsIdPaymentsBillingsUnpaidGet**](AllApi.md#organisationsIdPaymentsBillingsUnpaidGet) | **GET** /organisations/{id}/payments/billings/unpaid | 
[**organisationsIdPaymentsMethodsDefaultGet**](AllApi.md#organisationsIdPaymentsMethodsDefaultGet) | **GET** /organisations/{id}/payments/methods/default | 
[**organisationsIdPaymentsMethodsDefaultPut**](AllApi.md#organisationsIdPaymentsMethodsDefaultPut) | **PUT** /organisations/{id}/payments/methods/default | 
[**organisationsIdPaymentsMethodsGet**](AllApi.md#organisationsIdPaymentsMethodsGet) | **GET** /organisations/{id}/payments/methods | 
[**organisationsIdPaymentsMethodsMIdDelete**](AllApi.md#organisationsIdPaymentsMethodsMIdDelete) | **DELETE** /organisations/{id}/payments/methods/{mId} | 
[**organisationsIdPaymentsMethodsPost**](AllApi.md#organisationsIdPaymentsMethodsPost) | **POST** /organisations/{id}/payments/methods | 
[**organisationsIdPaymentsMonthlyinvoiceGet**](AllApi.md#organisationsIdPaymentsMonthlyinvoiceGet) | **GET** /organisations/{id}/payments/monthlyinvoice | 
[**organisationsIdPaymentsMonthlyinvoiceMaxcreditPut**](AllApi.md#organisationsIdPaymentsMonthlyinvoiceMaxcreditPut) | **PUT** /organisations/{id}/payments/monthlyinvoice/maxcredit | 
[**organisationsIdPaymentsRecurringGet**](AllApi.md#organisationsIdPaymentsRecurringGet) | **GET** /organisations/{id}/payments/recurring | 
[**paymentsAssetsPayButtonTokenButtonPngGet**](AllApi.md#paymentsAssetsPayButtonTokenButtonPngGet) | **GET** /payments/assets/pay_button/{token}/button.png | 
[**paymentsBidEndStripePost**](AllApi.md#paymentsBidEndStripePost) | **POST** /payments/{bid}/end/stripe | 
[**postAuthorize**](AllApi.md#postAuthorize) | **POST** /authorize | 
[**postGithubRedeploy**](AllApi.md#postGithubRedeploy) | **POST** /github/redeploy | 
[**postGithubSignup**](AllApi.md#postGithubSignup) | **POST** /github/signup | 
[**postOauthAccessToken**](AllApi.md#postOauthAccessToken) | **POST** /oauth/access_token | 
[**postOauthAuthorize**](AllApi.md#postOauthAuthorize) | **POST** /oauth/authorize | 
[**postOauthRequestToken**](AllApi.md#postOauthRequestToken) | **POST** /oauth/request_token | 
[**postOrganisations**](AllApi.md#postOrganisations) | **POST** /organisations | 
[**postOrganisationsIdAddonproviders**](AllApi.md#postOrganisationsIdAddonproviders) | **POST** /organisations/{id}/addonproviders | 
[**postOrganisationsIdAddonprovidersProviderIdFeatures**](AllApi.md#postOrganisationsIdAddonprovidersProviderIdFeatures) | **POST** /organisations/{id}/addonproviders/{providerId}/features | 
[**postOrganisationsIdAddonprovidersProviderIdPlans**](AllApi.md#postOrganisationsIdAddonprovidersProviderIdPlans) | **POST** /organisations/{id}/addonproviders/{providerId}/plans | 
[**postOrganisationsIdAddonprovidersProviderIdTesters**](AllApi.md#postOrganisationsIdAddonprovidersProviderIdTesters) | **POST** /organisations/{id}/addonproviders/{providerId}/testers | 
[**postOrganisationsIdAddons**](AllApi.md#postOrganisationsIdAddons) | **POST** /organisations/{id}/addons | 
[**postOrganisationsIdApplications**](AllApi.md#postOrganisationsIdApplications) | **POST** /organisations/{id}/applications | 
[**postOrganisationsIdApplicationsAppIdAddons**](AllApi.md#postOrganisationsIdApplicationsAppIdAddons) | **POST** /organisations/{id}/applications/{appId}/addons | 
[**postOrganisationsIdApplicationsAppIdInstances**](AllApi.md#postOrganisationsIdApplicationsAppIdInstances) | **POST** /organisations/{id}/applications/{appId}/instances | 
[**postOrganisationsIdConsumers**](AllApi.md#postOrganisationsIdConsumers) | **POST** /organisations/{id}/consumers | 
[**postOrganisationsIdMembers**](AllApi.md#postOrganisationsIdMembers) | **POST** /organisations/{id}/members | 
[**postOrganisationsIdPaymentsBillings**](AllApi.md#postOrganisationsIdPaymentsBillings) | **POST** /organisations/{id}/payments/billings | 
[**postPasswordForgotten**](AllApi.md#postPasswordForgotten) | **POST** /password_forgotten | 
[**postPasswordForgottenKey**](AllApi.md#postPasswordForgottenKey) | **POST** /password_forgotten/{key} | 
[**postSelfAddons**](AllApi.md#postSelfAddons) | **POST** /self/addons | 
[**postSelfApplications**](AllApi.md#postSelfApplications) | **POST** /self/applications | 
[**postSelfApplicationsAppIdAddons**](AllApi.md#postSelfApplicationsAppIdAddons) | **POST** /self/applications/{appId}/addons | 
[**postSelfApplicationsAppIdInstances**](AllApi.md#postSelfApplicationsAppIdInstances) | **POST** /self/applications/{appId}/instances | 
[**postSelfConsumers**](AllApi.md#postSelfConsumers) | **POST** /self/consumers | 
[**postSelfPaymentsBillings**](AllApi.md#postSelfPaymentsBillings) | **POST** /self/payments/billings | 
[**postSelfPaymentsMethods**](AllApi.md#postSelfPaymentsMethods) | **POST** /self/payments/methods | 
[**postUsers**](AllApi.md#postUsers) | **POST** /users | 
[**postVendorBillingOwnerId**](AllApi.md#postVendorBillingOwnerId) | **POST** /vendor/apps/{addonId}/consumptions | 
[**productsAddonprovidersProviderIdVersionsGet**](AllApi.md#productsAddonprovidersProviderIdVersionsGet) | **GET** /products/addonproviders/{provider_id}/versions | 
[**productsMfaKindsGet**](AllApi.md#productsMfaKindsGet) | **GET** /products/mfa_kinds | 
[**putOrganisationsId**](AllApi.md#putOrganisationsId) | **PUT** /organisations/{id} | 
[**putOrganisationsIdAddonprovidersProviderId**](AllApi.md#putOrganisationsIdAddonprovidersProviderId) | **PUT** /organisations/{id}/addonproviders/{providerId} | 
[**putOrganisationsIdAddonprovidersProviderIdPlansPlanId**](AllApi.md#putOrganisationsIdAddonprovidersProviderIdPlansPlanId) | **PUT** /organisations/{id}/addonproviders/{providerId}/plans/{planId} | 
[**putOrganisationsIdAddonprovidersProviderIdPlansPlanIdFeaturesFeatureName**](AllApi.md#putOrganisationsIdAddonprovidersProviderIdPlansPlanIdFeaturesFeatureName) | **PUT** /organisations/{id}/addonproviders/{providerId}/plans/{planId}/features/{featureName} | 
[**putOrganisationsIdAddonsAddonId**](AllApi.md#putOrganisationsIdAddonsAddonId) | **PUT** /organisations/{id}/addons/{addonId} | 
[**putOrganisationsIdAddonsAddonIdTagsTag**](AllApi.md#putOrganisationsIdAddonsAddonIdTagsTag) | **PUT** /organisations/{id}/addons/{addonId}/tags/{tag} | 
[**putOrganisationsIdApplicationsAppId**](AllApi.md#putOrganisationsIdApplicationsAppId) | **PUT** /organisations/{id}/applications/{appId} | 
[**putOrganisationsIdApplicationsAppIdDependenciesDependencyId**](AllApi.md#putOrganisationsIdApplicationsAppIdDependenciesDependencyId) | **PUT** /organisations/{id}/applications/{appId}/dependencies/{dependencyId} | 
[**putOrganisationsIdApplicationsAppIdEnv**](AllApi.md#putOrganisationsIdApplicationsAppIdEnv) | **PUT** /organisations/{id}/applications/{appId}/env | 
[**putOrganisationsIdApplicationsAppIdEnvEnvName**](AllApi.md#putOrganisationsIdApplicationsAppIdEnvEnvName) | **PUT** /organisations/{id}/applications/{appId}/env/{envName} | 
[**putOrganisationsIdApplicationsAppIdTagsTag**](AllApi.md#putOrganisationsIdApplicationsAppIdTagsTag) | **PUT** /organisations/{id}/applications/{appId}/tags/{tag} | 
[**putOrganisationsIdApplicationsAppIdVhostsDomain**](AllApi.md#putOrganisationsIdApplicationsAppIdVhostsDomain) | **PUT** /organisations/{id}/applications/{appId}/vhosts/{domain} | 
[**putOrganisationsIdApplicationsAppIdVhostsFavourite**](AllApi.md#putOrganisationsIdApplicationsAppIdVhostsFavourite) | **PUT** /organisations/{id}/applications/{appId}/vhosts/favourite | 
[**putOrganisationsIdAvatar**](AllApi.md#putOrganisationsIdAvatar) | **PUT** /organisations/{id}/avatar | 
[**putOrganisationsIdConsumersKey**](AllApi.md#putOrganisationsIdConsumersKey) | **PUT** /organisations/{id}/consumers/{key} | 
[**putOrganisationsIdMembersUserId**](AllApi.md#putOrganisationsIdMembersUserId) | **PUT** /organisations/{id}/members/{userId} | 
[**putOrganisationsIdPaymentsBillingsBid**](AllApi.md#putOrganisationsIdPaymentsBillingsBid) | **PUT** /organisations/{id}/payments/billings/{bid} | 
[**putSelf**](AllApi.md#putSelf) | **PUT** /self | 
[**putSelfAddonsAddonId**](AllApi.md#putSelfAddonsAddonId) | **PUT** /self/addons/{addonId} | 
[**putSelfAddonsAddonIdPlan**](AllApi.md#putSelfAddonsAddonIdPlan) | **PUT** /self/addons/{addonId}/plan | 
[**putSelfAddonsAddonIdTagsTag**](AllApi.md#putSelfAddonsAddonIdTagsTag) | **PUT** /self/addons/{addonId}/tags/{tag} | 
[**putSelfApplicationsAppId**](AllApi.md#putSelfApplicationsAppId) | **PUT** /self/applications/{appId} | 
[**putSelfApplicationsAppIdEnv**](AllApi.md#putSelfApplicationsAppIdEnv) | **PUT** /self/applications/{appId}/env | 
[**putSelfApplicationsAppIdEnvEnvName**](AllApi.md#putSelfApplicationsAppIdEnvEnvName) | **PUT** /self/applications/{appId}/env/{envName} | 
[**putSelfApplicationsAppIdTagsTag**](AllApi.md#putSelfApplicationsAppIdTagsTag) | **PUT** /self/applications/{appId}/tags/{tag} | 
[**putSelfApplicationsAppIdVhostsDomain**](AllApi.md#putSelfApplicationsAppIdVhostsDomain) | **PUT** /self/applications/{appId}/vhosts/{domain} | 
[**putSelfApplicationsAppIdVhostsFavourite**](AllApi.md#putSelfApplicationsAppIdVhostsFavourite) | **PUT** /self/applications/{appId}/vhosts/favourite | 
[**putSelfAvatar**](AllApi.md#putSelfAvatar) | **PUT** /self/avatar | 
[**putSelfChangePassword**](AllApi.md#putSelfChangePassword) | **PUT** /self/change_password | 
[**putSelfConsumersKey**](AllApi.md#putSelfConsumersKey) | **PUT** /self/consumers/{key} | 
[**putSelfEmailsEmail**](AllApi.md#putSelfEmailsEmail) | **PUT** /self/emails/{email} | 
[**putSelfKeysKey**](AllApi.md#putSelfKeysKey) | **PUT** /self/keys/{key} | 
[**putSelfPaymentsBillingsBid**](AllApi.md#putSelfPaymentsBillingsBid) | **PUT** /self/payments/billings/{bid} | 
[**putVendorAppsAddonId**](AllApi.md#putVendorAppsAddonId) | **PUT** /vendor/apps/{addonId} | 
[**selfAddonsPreordersPost**](AllApi.md#selfAddonsPreordersPost) | **POST** /self/addons/preorders | 
[**selfApplicationsAppIdBranchPut**](AllApi.md#selfApplicationsAppIdBranchPut) | **PUT** /self/applications/{appId}/branch | 
[**selfApplicationsAppIdBranchesGet**](AllApi.md#selfApplicationsAppIdBranchesGet) | **GET** /self/applications/{appId}/branches | 
[**selfApplicationsAppIdBuildflavorPut**](AllApi.md#selfApplicationsAppIdBuildflavorPut) | **PUT** /self/applications/{appId}/buildflavor | 
[**selfApplicationsAppIdDependenciesEnvGet**](AllApi.md#selfApplicationsAppIdDependenciesEnvGet) | **GET** /self/applications/{appId}/dependencies/env | 
[**selfApplicationsAppIdDeploymentsDeploymentIdGet**](AllApi.md#selfApplicationsAppIdDeploymentsDeploymentIdGet) | **GET** /self/applications/{appId}/deployments/{deploymentId} | 
[**selfApplicationsAppIdExposedEnvGet**](AllApi.md#selfApplicationsAppIdExposedEnvGet) | **GET** /self/applications/{appId}/exposed_env | 
[**selfApplicationsAppIdExposedEnvPut**](AllApi.md#selfApplicationsAppIdExposedEnvPut) | **PUT** /self/applications/{appId}/exposed_env | 
[**selfApplicationsAppIdInstancesInstanceIdGet**](AllApi.md#selfApplicationsAppIdInstancesInstanceIdGet) | **GET** /self/applications/{appId}/instances/{instanceId} | 
[**selfCliTokensGet**](AllApi.md#selfCliTokensGet) | **GET** /self/cli_tokens | 
[**selfMfaKindBackupcodesGet**](AllApi.md#selfMfaKindBackupcodesGet) | **GET** /self/mfa/{kind}/backupcodes | 
[**selfMfaKindConfirmationPost**](AllApi.md#selfMfaKindConfirmationPost) | **POST** /self/mfa/{kind}/confirmation | 
[**selfMfaKindDelete**](AllApi.md#selfMfaKindDelete) | **DELETE** /self/mfa/{kind} | 
[**selfMfaKindPost**](AllApi.md#selfMfaKindPost) | **POST** /self/mfa/{kind} | 
[**selfMfaKindPut**](AllApi.md#selfMfaKindPut) | **PUT** /self/mfa/{kind} | 
[**selfPaymentsMethodsDefaultGet**](AllApi.md#selfPaymentsMethodsDefaultGet) | **GET** /self/payments/methods/default | 
[**selfPaymentsMethodsDefaultPut**](AllApi.md#selfPaymentsMethodsDefaultPut) | **PUT** /self/payments/methods/default | 
[**selfPaymentsMonthlyinvoiceGet**](AllApi.md#selfPaymentsMonthlyinvoiceGet) | **GET** /self/payments/monthlyinvoice | 
[**selfPaymentsMonthlyinvoiceMaxcreditPut**](AllApi.md#selfPaymentsMonthlyinvoiceMaxcreditPut) | **PUT** /self/payments/monthlyinvoice/maxcredit | 
[**selfPaymentsRecurringGet**](AllApi.md#selfPaymentsRecurringGet) | **GET** /self/payments/recurring | 
[**selfPaymentsTokensStripeGet**](AllApi.md#selfPaymentsTokensStripeGet) | **GET** /self/payments/tokens/stripe | 
[**updateConfigProviderEnv**](AllApi.md#updateConfigProviderEnv) | **PUT** /v4/addon-providers/config-provider/addons/{configurationProviderId}/env | Update provider&#39;s addon environment
[**v3LogsAppIdDrainsGet**](AllApi.md#v3LogsAppIdDrainsGet) | **GET** /v3/logs/{appId}/drains | 
[**v3LogsAppIdDrainsIdOrUrlDelete**](AllApi.md#v3LogsAppIdDrainsIdOrUrlDelete) | **DELETE** /v3/logs/{appId}/drains/:idOrUrl | 
[**v3LogsAppIdDrainsIdOrUrlGet**](AllApi.md#v3LogsAppIdDrainsIdOrUrlGet) | **GET** /v3/logs/{appId}/drains/:idOrUrl | 
[**v3LogsAppIdDrainsPost**](AllApi.md#v3LogsAppIdDrainsPost) | **POST** /v3/logs/{appId}/drains | 
[**v3LogsAppIdGet**](AllApi.md#v3LogsAppIdGet) | **GET** /v3/logs/{appId} | 
[**v3LogsAppIdLogsChunkedGet**](AllApi.md#v3LogsAppIdLogsChunkedGet) | **GET** /v3/logs/{appId}/logs-chunked | 
[**v3LogsAppIdLogsSocketGet**](AllApi.md#v3LogsAppIdLogsSocketGet) | **GET** /v3/logs/{appId}/logs-socket | 
[**vendorAddonsPost**](AllApi.md#vendorAddonsPost) | **POST** /vendor//addons | 
[**vendorAppsAddonIdLogscollectorGet**](AllApi.md#vendorAppsAddonIdLogscollectorGet) | **GET** /vendor//apps/{addonId}/logscollector | 
[**vendorAppsAddonIdMigrationCallbackPut**](AllApi.md#vendorAppsAddonIdMigrationCallbackPut) | **PUT** /vendor/apps/{addonId}/migration_callback | 



## applicationAppIdEnvironmentGet

> applicationAppIdEnvironmentGet(appId, opts)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let appId = "appId_example"; // String | 
let opts = {
  'token': "token_example" // String | 
};
apiInstance.applicationAppIdEnvironmentGet(appId, opts, (error, data, response) => {
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
 **token** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## applicationAppIdEnvironmentPut

> applicationAppIdEnvironmentPut(appId, opts)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let appId = "appId_example"; // String | 
let opts = {
  'token': "token_example" // String | 
};
apiInstance.applicationAppIdEnvironmentPut(appId, opts, (error, data, response) => {
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
 **token** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## createMatomo

> Object createMatomo(opts)

Create Matomo addon

### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let opts = {
  'body': null // Object | 
};
apiInstance.createMatomo(opts, (error, data, response) => {
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
 **body** | **Object**|  | [optional] 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## createNetworkGroup

> Object createNetworkGroup(ownerId, opts)

Create Network Group

Creates a Network Group.

### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let ownerId = "ownerId_example"; // String | Automatically added
let opts = {
  'body': null // Object | 
};
apiInstance.createNetworkGroup(ownerId, opts, (error, data, response) => {
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


## createNetworkGroupExternalPeer

> Object createNetworkGroupExternalPeer(ownerId, networkGroupId, opts)

Add external peer

Adds an external peer to a Network Group.

### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let ownerId = "ownerId_example"; // String | Automatically added
let networkGroupId = "networkGroupId_example"; // String | Automatically added
let opts = {
  'body': null // Object | 
};
apiInstance.createNetworkGroupExternalPeer(ownerId, networkGroupId, opts, (error, data, response) => {
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


## createNetworkGroupMember

> createNetworkGroupMember(ownerId, networkGroupId, opts)

Add member

Adds a member to a Network Group.

### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let ownerId = "ownerId_example"; // String | Automatically added
let networkGroupId = "networkGroupId_example"; // String | Automatically added
let opts = {
  'schema2': new CleverCloudApi.Schema2() // Schema2 | 
};
apiInstance.createNetworkGroupMember(ownerId, networkGroupId, opts, (error, data, response) => {
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


## deleteGithubLink

> deleteGithubLink()



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
apiInstance.deleteGithubLink((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteMatomo

> Object deleteMatomo(matomoId, opts)

Delete Matomo addon

### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let matomoId = "matomoId_example"; // String | Automatically added
let opts = {
  'body': "body_example" // String | 
};
apiInstance.deleteMatomo(matomoId, opts, (error, data, response) => {
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
 **matomoId** | **String**| Automatically added | 
 **body** | **String**|  | [optional] 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## deleteNetworkGroup

> deleteNetworkGroup(ownerId, networkGroupId, opts)

Delete Network Group

Deletes a Network Group.

### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let ownerId = "ownerId_example"; // String | Automatically added
let networkGroupId = "networkGroupId_example"; // String | Automatically added
let opts = {
  'body': null // Object | 
};
apiInstance.deleteNetworkGroup(ownerId, networkGroupId, opts, (error, data, response) => {
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


## deleteNetworkGroupExternalPeer

> deleteNetworkGroupExternalPeer(ownerId, networkGroupId, peerId, opts)

Remove external peer

Removes an external peer from a Network Group.

### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let ownerId = "ownerId_example"; // String | Automatically added
let networkGroupId = "networkGroupId_example"; // String | Automatically added
let peerId = "peerId_example"; // String | Automatically added
let opts = {
  'body': null // Object | 
};
apiInstance.deleteNetworkGroupExternalPeer(ownerId, networkGroupId, peerId, opts, (error, data, response) => {
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


## deleteNetworkGroupMember

> deleteNetworkGroupMember(ownerId, networkGroupId, memberId, opts)

Remove member

Removes a member from a Network Group.

### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let ownerId = "ownerId_example"; // String | Automatically added
let networkGroupId = "networkGroupId_example"; // String | Automatically added
let memberId = "memberId_example"; // String | Automatically added
let opts = {
  'body': null // Object | 
};
apiInstance.deleteNetworkGroupMember(ownerId, networkGroupId, memberId, opts, (error, data, response) => {
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


## deleteNetworkGroupPeer

> deleteNetworkGroupPeer(ownerId, networkGroupId, peerId, opts)

Remove peer

Removes a peer from a Network Group.

### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let ownerId = "ownerId_example"; // String | Automatically added
let networkGroupId = "networkGroupId_example"; // String | Automatically added
let peerId = "peerId_example"; // String | Automatically added
let opts = {
  'body': null // Object | 
};
apiInstance.deleteNetworkGroupPeer(ownerId, networkGroupId, peerId, opts, (error, data, response) => {
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


## deleteOrganisationsId

> deleteOrganisationsId(id)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let id = "id_example"; // String | 
apiInstance.deleteOrganisationsId(id, (error, data, response) => {
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


## deleteOrganisationsIdAddonprovidersProviderIdFeaturesFeatureId

> deleteOrganisationsIdAddonprovidersProviderIdFeaturesFeatureId(id, featureId, providerId)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let id = "id_example"; // String | 
let featureId = "featureId_example"; // String | 
let providerId = "providerId_example"; // String | 
apiInstance.deleteOrganisationsIdAddonprovidersProviderIdFeaturesFeatureId(id, featureId, providerId, (error, data, response) => {
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


## deleteOrganisationsIdAddonprovidersProviderIdPlansPlanId

> deleteOrganisationsIdAddonprovidersProviderIdPlansPlanId(id, providerId, planId)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let id = "id_example"; // String | 
let providerId = "providerId_example"; // String | 
let planId = "planId_example"; // String | 
apiInstance.deleteOrganisationsIdAddonprovidersProviderIdPlansPlanId(id, providerId, planId, (error, data, response) => {
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


## deleteOrganisationsIdAddonprovidersProviderIdPlansPlanIdFeaturesFeatureName

> deleteOrganisationsIdAddonprovidersProviderIdPlansPlanIdFeaturesFeatureName(id, featureName, providerId, planId)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let id = "id_example"; // String | 
let featureName = "featureName_example"; // String | 
let providerId = "providerId_example"; // String | 
let planId = "planId_example"; // String | 
apiInstance.deleteOrganisationsIdAddonprovidersProviderIdPlansPlanIdFeaturesFeatureName(id, featureName, providerId, planId, (error, data, response) => {
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


## deleteOrganisationsIdAddonsAddonId

> deleteOrganisationsIdAddonsAddonId(id, addonId)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let id = "id_example"; // String | 
let addonId = "addonId_example"; // String | 
apiInstance.deleteOrganisationsIdAddonsAddonId(id, addonId, (error, data, response) => {
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


## deleteOrganisationsIdAddonsAddonIdTagsTag

> deleteOrganisationsIdAddonsAddonIdTagsTag(id, tag, addonId)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let id = "id_example"; // String | 
let tag = "tag_example"; // String | 
let addonId = "addonId_example"; // String | 
apiInstance.deleteOrganisationsIdAddonsAddonIdTagsTag(id, tag, addonId, (error, data, response) => {
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


## deleteOrganisationsIdApplicationsAppId

> deleteOrganisationsIdApplicationsAppId(id, appId)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let id = "id_example"; // String | 
let appId = "appId_example"; // String | 
apiInstance.deleteOrganisationsIdApplicationsAppId(id, appId, (error, data, response) => {
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


## deleteOrganisationsIdApplicationsAppIdAddonsAddonId

> deleteOrganisationsIdApplicationsAppIdAddonsAddonId(id, appId, addonId)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let id = "id_example"; // String | 
let appId = "appId_example"; // String | 
let addonId = "addonId_example"; // String | 
apiInstance.deleteOrganisationsIdApplicationsAppIdAddonsAddonId(id, appId, addonId, (error, data, response) => {
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


## deleteOrganisationsIdApplicationsAppIdDependenciesDependencyId

> deleteOrganisationsIdApplicationsAppIdDependenciesDependencyId(dependencyId, appId, id)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let dependencyId = "dependencyId_example"; // String | 
let appId = "appId_example"; // String | 
let id = "id_example"; // String | 
apiInstance.deleteOrganisationsIdApplicationsAppIdDependenciesDependencyId(dependencyId, appId, id, (error, data, response) => {
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


## deleteOrganisationsIdApplicationsAppIdDeploymentsDeploymentIdInstances

> deleteOrganisationsIdApplicationsAppIdDeploymentsDeploymentIdInstances(id, appId, deploymentId)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let id = "id_example"; // String | 
let appId = "appId_example"; // String | 
let deploymentId = "deploymentId_example"; // String | 
apiInstance.deleteOrganisationsIdApplicationsAppIdDeploymentsDeploymentIdInstances(id, appId, deploymentId, (error, data, response) => {
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


## deleteOrganisationsIdApplicationsAppIdEnvEnvName

> deleteOrganisationsIdApplicationsAppIdEnvEnvName(id, appId, envName)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let id = "id_example"; // String | 
let appId = "appId_example"; // String | 
let envName = "envName_example"; // String | 
apiInstance.deleteOrganisationsIdApplicationsAppIdEnvEnvName(id, appId, envName, (error, data, response) => {
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


## deleteOrganisationsIdApplicationsAppIdInstances

> deleteOrganisationsIdApplicationsAppIdInstances(id, appId)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let id = "id_example"; // String | 
let appId = "appId_example"; // String | 
apiInstance.deleteOrganisationsIdApplicationsAppIdInstances(id, appId, (error, data, response) => {
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


## deleteOrganisationsIdApplicationsAppIdTagsTag

> deleteOrganisationsIdApplicationsAppIdTagsTag(id, appId, tag)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let id = "id_example"; // String | 
let appId = "appId_example"; // String | 
let tag = "tag_example"; // String | 
apiInstance.deleteOrganisationsIdApplicationsAppIdTagsTag(id, appId, tag, (error, data, response) => {
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


## deleteOrganisationsIdApplicationsAppIdVhostsDomain

> deleteOrganisationsIdApplicationsAppIdVhostsDomain(id, appId, domain)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let id = "id_example"; // String | 
let appId = "appId_example"; // String | 
let domain = "domain_example"; // String | 
apiInstance.deleteOrganisationsIdApplicationsAppIdVhostsDomain(id, appId, domain, (error, data, response) => {
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


## deleteOrganisationsIdApplicationsAppIdVhostsFavourite

> deleteOrganisationsIdApplicationsAppIdVhostsFavourite(id, appId)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let id = "id_example"; // String | 
let appId = "appId_example"; // String | 
apiInstance.deleteOrganisationsIdApplicationsAppIdVhostsFavourite(id, appId, (error, data, response) => {
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


## deleteOrganisationsIdConsumersKey

> deleteOrganisationsIdConsumersKey(id, key)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let id = "id_example"; // String | 
let key = "key_example"; // String | 
apiInstance.deleteOrganisationsIdConsumersKey(id, key, (error, data, response) => {
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


## deleteOrganisationsIdMembersUserId

> deleteOrganisationsIdMembersUserId(id, userId)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let id = "id_example"; // String | 
let userId = "userId_example"; // String | 
apiInstance.deleteOrganisationsIdMembersUserId(id, userId, (error, data, response) => {
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


## deleteOrganisationsIdPaymentsBillingsBid

> deleteOrganisationsIdPaymentsBillingsBid(id, bid)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let id = "id_example"; // String | 
let bid = "bid_example"; // String | 
apiInstance.deleteOrganisationsIdPaymentsBillingsBid(id, bid, (error, data, response) => {
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


## deleteOrganisationsIdPaymentsRecurring

> deleteOrganisationsIdPaymentsRecurring(id)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let id = "id_example"; // String | 
apiInstance.deleteOrganisationsIdPaymentsRecurring(id, (error, data, response) => {
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


## deleteSelf

> deleteSelf()



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
apiInstance.deleteSelf((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteSelfAddonsAddonId

> deleteSelfAddonsAddonId(addonId)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let addonId = "addonId_example"; // String | 
apiInstance.deleteSelfAddonsAddonId(addonId, (error, data, response) => {
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
 **addonId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteSelfAddonsAddonIdTagsTag

> deleteSelfAddonsAddonIdTagsTag(tag, addonId)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let tag = "tag_example"; // String | 
let addonId = "addonId_example"; // String | 
apiInstance.deleteSelfAddonsAddonIdTagsTag(tag, addonId, (error, data, response) => {
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
 **tag** | **String**|  | 
 **addonId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteSelfApplicationsAppId

> deleteSelfApplicationsAppId(appId)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let appId = "appId_example"; // String | 
apiInstance.deleteSelfApplicationsAppId(appId, (error, data, response) => {
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

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteSelfApplicationsAppIdAddonsAddonId

> deleteSelfApplicationsAppIdAddonsAddonId(appId, addonId)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let appId = "appId_example"; // String | 
let addonId = "addonId_example"; // String | 
apiInstance.deleteSelfApplicationsAppIdAddonsAddonId(appId, addonId, (error, data, response) => {
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
 **addonId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteSelfApplicationsAppIdDependenciesDependencyId

> deleteSelfApplicationsAppIdDependenciesDependencyId(dependencyId, appId)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let dependencyId = "dependencyId_example"; // String | 
let appId = "appId_example"; // String | 
apiInstance.deleteSelfApplicationsAppIdDependenciesDependencyId(dependencyId, appId, (error, data, response) => {
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

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteSelfApplicationsAppIdDeploymentsDeploymentIdInstances

> deleteSelfApplicationsAppIdDeploymentsDeploymentIdInstances(appId, deploymentId)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let appId = "appId_example"; // String | 
let deploymentId = "deploymentId_example"; // String | 
apiInstance.deleteSelfApplicationsAppIdDeploymentsDeploymentIdInstances(appId, deploymentId, (error, data, response) => {
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

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteSelfApplicationsAppIdEnvEnvName

> deleteSelfApplicationsAppIdEnvEnvName(appId, envName)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let appId = "appId_example"; // String | 
let envName = "envName_example"; // String | 
apiInstance.deleteSelfApplicationsAppIdEnvEnvName(appId, envName, (error, data, response) => {
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
 **envName** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteSelfApplicationsAppIdInstances

> deleteSelfApplicationsAppIdInstances(appId)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let appId = "appId_example"; // String | 
apiInstance.deleteSelfApplicationsAppIdInstances(appId, (error, data, response) => {
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

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteSelfApplicationsAppIdTagsTag

> deleteSelfApplicationsAppIdTagsTag(appId, tag)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let appId = "appId_example"; // String | 
let tag = "tag_example"; // String | 
apiInstance.deleteSelfApplicationsAppIdTagsTag(appId, tag, (error, data, response) => {
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
 **tag** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteSelfApplicationsAppIdVhostsDomain

> deleteSelfApplicationsAppIdVhostsDomain(appId, domain)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let appId = "appId_example"; // String | 
let domain = "domain_example"; // String | 
apiInstance.deleteSelfApplicationsAppIdVhostsDomain(appId, domain, (error, data, response) => {
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
 **domain** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteSelfApplicationsAppIdVhostsFavourite

> deleteSelfApplicationsAppIdVhostsFavourite(appId)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let appId = "appId_example"; // String | 
apiInstance.deleteSelfApplicationsAppIdVhostsFavourite(appId, (error, data, response) => {
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

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteSelfConsumersKey

> deleteSelfConsumersKey(key)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let key = "key_example"; // String | 
apiInstance.deleteSelfConsumersKey(key, (error, data, response) => {
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
 **key** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteSelfEmailsEmail

> deleteSelfEmailsEmail(email)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let email = "email_example"; // String | 
apiInstance.deleteSelfEmailsEmail(email, (error, data, response) => {
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
 **email** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteSelfKeysKey

> deleteSelfKeysKey(key)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let key = "key_example"; // String | 
apiInstance.deleteSelfKeysKey(key, (error, data, response) => {
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
 **key** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteSelfPaymentsBillingsBid

> deleteSelfPaymentsBillingsBid(bid)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let bid = "bid_example"; // String | 
apiInstance.deleteSelfPaymentsBillingsBid(bid, (error, data, response) => {
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
 **bid** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteSelfPaymentsMethodsMId

> deleteSelfPaymentsMethodsMId(mId)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let mId = "mId_example"; // String | 
apiInstance.deleteSelfPaymentsMethodsMId(mId, (error, data, response) => {
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

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteSelfPaymentsRecurring

> deleteSelfPaymentsRecurring()



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
apiInstance.deleteSelfPaymentsRecurring((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteSelfTokens

> deleteSelfTokens()



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
apiInstance.deleteSelfTokens((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteSelfTokensToken

> deleteSelfTokensToken(token)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let token = "token_example"; // String | 
apiInstance.deleteSelfTokensToken(token, (error, data, response) => {
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
 **token** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## eventsEventSocketGet

> eventsEventSocketGet()



Retrieve events as they come through a websocket connection. To have authorization, you have to send a &#x60;{ \&quot;message_type\&quot;: \&quot;oauth\&quot;, \&quot;authorization\&quot;: \&quot;oauth authorization string\&quot; }&#x60; message

### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
apiInstance.eventsEventSocketGet((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getConfigProvider

> Object getConfigProvider(configurationProviderId, opts)

Get Addon provider configuration

### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let configurationProviderId = "configurationProviderId_example"; // String | Automatically added
let opts = {
  'body': "body_example" // String | 
};
apiInstance.getConfigProvider(configurationProviderId, opts, (error, data, response) => {
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
 **configurationProviderId** | **String**| Automatically added | 
 **body** | **String**|  | [optional] 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getConfigProviderEnv

> [Object] getConfigProviderEnv(configurationProviderId, opts)

Get provider&#39;s addon environment

### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let configurationProviderId = "configurationProviderId_example"; // String | Automatically added
let opts = {
  'body': "body_example" // String | 
};
apiInstance.getConfigProviderEnv(configurationProviderId, opts, (error, data, response) => {
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
 **configurationProviderId** | **String**| Automatically added | 
 **body** | **String**|  | [optional] 

### Return type

**[Object]**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getGithub

> TransactionId getGithub()



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
apiInstance.getGithub((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**TransactionId**](TransactionId.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getGithubApplications

> [Application] getGithubApplications()



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
apiInstance.getGithubApplications((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**[Application]**](Application.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getGithubCallback

> getGithubCallback(opts)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let opts = {
  'code': "code_example", // String | 
  'state': "state_example", // String | 
  'error': "error_example", // String | 
  'errorDescription': "errorDescription_example", // String | 
  'errorUri': "errorUri_example", // String | 
  'cookie': "cookie_example" // String | 
};
apiInstance.getGithubCallback(opts, (error, data, response) => {
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
 **code** | **String**|  | [optional] 
 **state** | **String**|  | [optional] 
 **error** | **String**|  | [optional] 
 **errorDescription** | **String**|  | [optional] 
 **errorUri** | **String**|  | [optional] 
 **cookie** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getGithubEmails

> [String] getGithubEmails()



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
apiInstance.getGithubEmails((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

**[String]**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## getGithubKeys

> [Key] getGithubKeys()



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
apiInstance.getGithubKeys((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**[Key]**](Key.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getGithubLink

> getGithubLink(opts)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let opts = {
  'transactionId': "transactionId_example", // String | From GET /github
  'redirectUrl': "redirectUrl_example" // String | 
};
apiInstance.getGithubLink(opts, (error, data, response) => {
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
 **transactionId** | **String**| From GET /github | [optional] 
 **redirectUrl** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getGithubLogin

> getGithubLogin(opts)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let opts = {
  'redirectUrl': "redirectUrl_example", // String | 
  'fromAuthorize': "fromAuthorize_example" // String | 
};
apiInstance.getGithubLogin(opts, (error, data, response) => {
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
 **redirectUrl** | **String**|  | [optional] 
 **fromAuthorize** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getGithubSignup

> getGithubSignup(opts)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let opts = {
  'redirectUrl': "redirectUrl_example", // String | 
  'fromAuthorize': "fromAuthorize_example" // String | 
};
apiInstance.getGithubSignup(opts, (error, data, response) => {
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
 **redirectUrl** | **String**|  | [optional] 
 **fromAuthorize** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getGithubUsername

> String getGithubUsername()



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
apiInstance.getGithubUsername((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## getMatomo

> Object getMatomo(matomoId, opts)

Get Matomo addon

### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let matomoId = "matomoId_example"; // String | Automatically added
let opts = {
  'body': "body_example" // String | 
};
apiInstance.getMatomo(matomoId, opts, (error, data, response) => {
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
 **matomoId** | **String**| Automatically added | 
 **body** | **String**|  | [optional] 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## getMatomoKTokenValidation

> Object getMatomoKTokenValidation(opts)

Validate a keycloak token

### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let opts = {
  'keycloakToken': "keycloakToken_example", // String | Environment variable injected on the app with 'KEYCLOAK_TOKEN' name
  'body': "body_example" // String | 
};
apiInstance.getMatomoKTokenValidation(opts, (error, data, response) => {
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
 **keycloakToken** | **String**| Environment variable injected on the app with &#39;KEYCLOAK_TOKEN&#39; name | [optional] 
 **body** | **String**|  | [optional] 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## getNetworkGroup

> Object getNetworkGroup(ownerId, networkGroupId, opts)

Get Network Group

Gets details of a Network Group.

### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let ownerId = "ownerId_example"; // String | Automatically added
let networkGroupId = "networkGroupId_example"; // String | Automatically added
let opts = {
  'body': null // Object | 
};
apiInstance.getNetworkGroup(ownerId, networkGroupId, opts, (error, data, response) => {
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


## getNetworkGroupMember

> Schema1 getNetworkGroupMember(ownerId, networkGroupId, memberId, opts)

Get member

Gets details of a Network Group member.

### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let ownerId = "ownerId_example"; // String | Automatically added
let networkGroupId = "networkGroupId_example"; // String | Automatically added
let memberId = "memberId_example"; // String | Automatically added
let opts = {
  'body': null // Object | 
};
apiInstance.getNetworkGroupMember(ownerId, networkGroupId, memberId, opts, (error, data, response) => {
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


## getNetworkGroupPeer

> Object getNetworkGroupPeer(ownerId, networkGroupId, peerId, opts)

Get peer

Gets details of a Network Group peer.

### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let ownerId = "ownerId_example"; // String | Automatically added
let networkGroupId = "networkGroupId_example"; // String | Automatically added
let peerId = "peerId_example"; // String | Automatically added
let opts = {
  'body': null // Object | 
};
apiInstance.getNetworkGroupPeer(ownerId, networkGroupId, peerId, opts, (error, data, response) => {
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


## getNetworkGroupStream

> Object getNetworkGroupStream(ownerId, networkGroupId, opts)

Network Group SSE

Retrieves the current Network Group details as a Server Sent Event.

### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let ownerId = "ownerId_example"; // String | Automatically added
let networkGroupId = "networkGroupId_example"; // String | Automatically added
let opts = {
  'body': null // Object | 
};
apiInstance.getNetworkGroupStream(ownerId, networkGroupId, opts, (error, data, response) => {
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


## getNetworkGroupWireGuardConfiguration

> Object getNetworkGroupWireGuardConfiguration(ownerId, networkGroupId, peerId, opts)

Get WireGuard® configuration

Gets the current WireGuard® tunnel configuration file for a Network Group peer.

### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let ownerId = "ownerId_example"; // String | Automatically added
let networkGroupId = "networkGroupId_example"; // String | Automatically added
let peerId = "peerId_example"; // String | Automatically added
let opts = {
  'body': null // Object | 
};
apiInstance.getNetworkGroupWireGuardConfiguration(ownerId, networkGroupId, peerId, opts, (error, data, response) => {
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


## getNetworkGroupWireGuardConfigurationStream

> Object getNetworkGroupWireGuardConfigurationStream(ownerId, networkGroupId, peerId, opts)

Get WireGuard® configuration

Gets the current WireGuard® tunnel configuration file for a Network Group peer as a Server Sent Event.

### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let ownerId = "ownerId_example"; // String | Automatically added
let networkGroupId = "networkGroupId_example"; // String | Automatically added
let peerId = "peerId_example"; // String | Automatically added
let opts = {
  'body': null // Object | 
};
apiInstance.getNetworkGroupWireGuardConfigurationStream(ownerId, networkGroupId, peerId, opts, (error, data, response) => {
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


## getNewsfeedEngineering

> getNewsfeedEngineering()



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
apiInstance.getNewsfeedEngineering((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getNewsfeedsBlog

> getNewsfeedsBlog()



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
apiInstance.getNewsfeedsBlog((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getOauthAuthorize

> getOauthAuthorize(opts)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let opts = {
  'oauthToken': "oauthToken_example", // String | 
  'cookie': "cookie_example" // String | 
};
apiInstance.getOauthAuthorize(opts, (error, data, response) => {
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
 **oauthToken** | **String**|  | [optional] 
 **cookie** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getOauthRights

> Rights getOauthRights()



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
apiInstance.getOauthRights((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**Rights**](Rights.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getOrganisations

> [Organisation] getOrganisations(opts)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let opts = {
  'user': "user_example" // String | 
};
apiInstance.getOrganisations(opts, (error, data, response) => {
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


## getOrganisationsId

> Organisation getOrganisationsId(id)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let id = "id_example"; // String | 
apiInstance.getOrganisationsId(id, (error, data, response) => {
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


## getOrganisationsIdAddonproviders

> [Provider] getOrganisationsIdAddonproviders(id)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let id = "id_example"; // String | 
apiInstance.getOrganisationsIdAddonproviders(id, (error, data, response) => {
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


## getOrganisationsIdAddonprovidersProviderId

> Provider getOrganisationsIdAddonprovidersProviderId(id, providerId)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let id = "id_example"; // String | 
let providerId = "providerId_example"; // String | 
apiInstance.getOrganisationsIdAddonprovidersProviderId(id, providerId, (error, data, response) => {
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


## getOrganisationsIdAddonprovidersProviderIdFeatures

> [Feature] getOrganisationsIdAddonprovidersProviderIdFeatures(id, providerId)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let id = "id_example"; // String | 
let providerId = "providerId_example"; // String | 
apiInstance.getOrganisationsIdAddonprovidersProviderIdFeatures(id, providerId, (error, data, response) => {
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


## getOrganisationsIdAddonprovidersProviderIdPlans

> [Plan] getOrganisationsIdAddonprovidersProviderIdPlans(id, providerId)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let id = "id_example"; // String | 
let providerId = "providerId_example"; // String | 
apiInstance.getOrganisationsIdAddonprovidersProviderIdPlans(id, providerId, (error, data, response) => {
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


## getOrganisationsIdAddonprovidersProviderIdPlansPlanId

> Plan getOrganisationsIdAddonprovidersProviderIdPlansPlanId(id, providerId, planId)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let id = "id_example"; // String | 
let providerId = "providerId_example"; // String | 
let planId = "planId_example"; // String | 
apiInstance.getOrganisationsIdAddonprovidersProviderIdPlansPlanId(id, providerId, planId, (error, data, response) => {
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


## getOrganisationsIdAddonprovidersProviderIdTags

> [String] getOrganisationsIdAddonprovidersProviderIdTags(id, providerId)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let id = "id_example"; // String | 
let providerId = "providerId_example"; // String | 
apiInstance.getOrganisationsIdAddonprovidersProviderIdTags(id, providerId, (error, data, response) => {
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


## getOrganisationsIdAddons

> [Addon] getOrganisationsIdAddons(id)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let id = "id_example"; // String | 
apiInstance.getOrganisationsIdAddons(id, (error, data, response) => {
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


## getOrganisationsIdAddonsAddonId

> Addon getOrganisationsIdAddonsAddonId(id, addonId)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let id = "id_example"; // String | 
let addonId = "addonId_example"; // String | 
apiInstance.getOrganisationsIdAddonsAddonId(id, addonId, (error, data, response) => {
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


## getOrganisationsIdAddonsAddonIdApplications

> [Application] getOrganisationsIdAddonsAddonIdApplications(id, addonId)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let id = "id_example"; // String | 
let addonId = "addonId_example"; // String | 
apiInstance.getOrganisationsIdAddonsAddonIdApplications(id, addonId, (error, data, response) => {
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


## getOrganisationsIdAddonsAddonIdEnv

> [ListEnv] getOrganisationsIdAddonsAddonIdEnv(id, addonId)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let id = "id_example"; // String | 
let addonId = "addonId_example"; // String | 
apiInstance.getOrganisationsIdAddonsAddonIdEnv(id, addonId, (error, data, response) => {
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


## getOrganisationsIdAddonsAddonIdSso

> AddonProviderSso getOrganisationsIdAddonsAddonIdSso(providerId, id)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let providerId = "providerId_example"; // String | 
let id = "id_example"; // String | 
apiInstance.getOrganisationsIdAddonsAddonIdSso(providerId, id, (error, data, response) => {
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


## getOrganisationsIdAddonsAddonIdTags

> [String] getOrganisationsIdAddonsAddonIdTags(id, addonId)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let id = "id_example"; // String | 
let addonId = "addonId_example"; // String | 
apiInstance.getOrganisationsIdAddonsAddonIdTags(id, addonId, (error, data, response) => {
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


## getOrganisationsIdApplications

> [Application] getOrganisationsIdApplications(id)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let id = "id_example"; // String | 
apiInstance.getOrganisationsIdApplications(id, (error, data, response) => {
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


## getOrganisationsIdApplicationsAppId

> Application getOrganisationsIdApplicationsAppId(id, appId)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let id = "id_example"; // String | 
let appId = "appId_example"; // String | 
apiInstance.getOrganisationsIdApplicationsAppId(id, appId, (error, data, response) => {
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


## getOrganisationsIdApplicationsAppIdAddons

> [Addon] getOrganisationsIdApplicationsAppIdAddons(id, appId)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let id = "id_example"; // String | 
let appId = "appId_example"; // String | 
apiInstance.getOrganisationsIdApplicationsAppIdAddons(id, appId, (error, data, response) => {
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


## getOrganisationsIdApplicationsAppIdAddonsEnv

> [Env] getOrganisationsIdApplicationsAppIdAddonsEnv(id, appId)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let id = "id_example"; // String | 
let appId = "appId_example"; // String | 
apiInstance.getOrganisationsIdApplicationsAppIdAddonsEnv(id, appId, (error, data, response) => {
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


## getOrganisationsIdApplicationsAppIdDependencies

> [Application] getOrganisationsIdApplicationsAppIdDependencies(appId, id)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let appId = "appId_example"; // String | 
let id = "id_example"; // String | 
apiInstance.getOrganisationsIdApplicationsAppIdDependencies(appId, id, (error, data, response) => {
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


## getOrganisationsIdApplicationsAppIdDependents

> [Application] getOrganisationsIdApplicationsAppIdDependents(appId, id)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let appId = "appId_example"; // String | 
let id = "id_example"; // String | 
apiInstance.getOrganisationsIdApplicationsAppIdDependents(appId, id, (error, data, response) => {
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


## getOrganisationsIdApplicationsAppIdDeployments

> [Deployment] getOrganisationsIdApplicationsAppIdDeployments(id, appId, opts)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let id = "id_example"; // String | 
let appId = "appId_example"; // String | 
let opts = {
  'limit': "limit_example", // String | 
  'offset': "offset_example", // String | 
  'action': "action_example" // String | 
};
apiInstance.getOrganisationsIdApplicationsAppIdDeployments(id, appId, opts, (error, data, response) => {
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


## getOrganisationsIdApplicationsAppIdEnv

> [ListEnv] getOrganisationsIdApplicationsAppIdEnv(id, appId)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let id = "id_example"; // String | 
let appId = "appId_example"; // String | 
apiInstance.getOrganisationsIdApplicationsAppIdEnv(id, appId, (error, data, response) => {
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


## getOrganisationsIdApplicationsAppIdInstances

> [AppInstance] getOrganisationsIdApplicationsAppIdInstances(id, appId)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let id = "id_example"; // String | 
let appId = "appId_example"; // String | 
apiInstance.getOrganisationsIdApplicationsAppIdInstances(id, appId, (error, data, response) => {
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


## getOrganisationsIdApplicationsAppIdTags

> [String] getOrganisationsIdApplicationsAppIdTags(id, appId)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let id = "id_example"; // String | 
let appId = "appId_example"; // String | 
apiInstance.getOrganisationsIdApplicationsAppIdTags(id, appId, (error, data, response) => {
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


## getOrganisationsIdApplicationsAppIdVhosts

> [Vhost] getOrganisationsIdApplicationsAppIdVhosts(id, appId)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let id = "id_example"; // String | 
let appId = "appId_example"; // String | 
apiInstance.getOrganisationsIdApplicationsAppIdVhosts(id, appId, (error, data, response) => {
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


## getOrganisationsIdApplicationsAppIdVhostsFavourite

> Vhost getOrganisationsIdApplicationsAppIdVhostsFavourite(id, appId)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let id = "id_example"; // String | 
let appId = "appId_example"; // String | 
apiInstance.getOrganisationsIdApplicationsAppIdVhostsFavourite(id, appId, (error, data, response) => {
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


## getOrganisationsIdConsumers

> [Consumer] getOrganisationsIdConsumers(id)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let id = "id_example"; // String | 
apiInstance.getOrganisationsIdConsumers(id, (error, data, response) => {
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


## getOrganisationsIdConsumersKey

> Consumer getOrganisationsIdConsumersKey(id, key)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let id = "id_example"; // String | 
let key = "key_example"; // String | 
apiInstance.getOrganisationsIdConsumersKey(id, key, (error, data, response) => {
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


## getOrganisationsIdConsumersKeySecret

> Secret getOrganisationsIdConsumersKeySecret(id, key)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let id = "id_example"; // String | 
let key = "key_example"; // String | 
apiInstance.getOrganisationsIdConsumersKeySecret(id, key, (error, data, response) => {
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


## getOrganisationsIdConsumptions

> Conso getOrganisationsIdConsumptions(id, opts)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let id = "id_example"; // String | 
let opts = {
  'appId': "appId_example", // String | 
  'from': "from_example", // String | 
  'to': "to_example" // String | 
};
apiInstance.getOrganisationsIdConsumptions(id, opts, (error, data, response) => {
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


## getOrganisationsIdCredits

> Credits getOrganisationsIdCredits(id)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let id = "id_example"; // String | 
apiInstance.getOrganisationsIdCredits(id, (error, data, response) => {
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


## getOrganisationsIdDeployments

> DeploymentSummary getOrganisationsIdDeployments(id)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let id = "id_example"; // String | 
apiInstance.getOrganisationsIdDeployments(id, (error, data, response) => {
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


## getOrganisationsIdInstances

> Object getOrganisationsIdInstances(id)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let id = "id_example"; // String | 
apiInstance.getOrganisationsIdInstances(id, (error, data, response) => {
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


## getOrganisationsIdMembers

> [Schema1] getOrganisationsIdMembers(id)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let id = "id_example"; // String | 
apiInstance.getOrganisationsIdMembers(id, (error, data, response) => {
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


## getOrganisationsIdPaymentInfo

> getOrganisationsIdPaymentInfo(id)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let id = "id_example"; // String | 
apiInstance.getOrganisationsIdPaymentInfo(id, (error, data, response) => {
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


## getOrganisationsIdPaymentsBillings

> getOrganisationsIdPaymentsBillings(id)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let id = "id_example"; // String | 
apiInstance.getOrganisationsIdPaymentsBillings(id, (error, data, response) => {
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


## getOrganisationsIdPaymentsBillingsBid

> getOrganisationsIdPaymentsBillingsBid(id, bid)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let id = "id_example"; // String | 
let bid = "bid_example"; // String | 
apiInstance.getOrganisationsIdPaymentsBillingsBid(id, bid, (error, data, response) => {
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


## getOrganisationsIdPaymentsBillingsBidPdf

> getOrganisationsIdPaymentsBillingsBidPdf(id, bid, opts)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let id = "id_example"; // String | 
let bid = "bid_example"; // String | 
let opts = {
  'token': "token_example" // String | 
};
apiInstance.getOrganisationsIdPaymentsBillingsBidPdf(id, bid, opts, (error, data, response) => {
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


## getOrganisationsIdPaymentsFullPricePrice

> getOrganisationsIdPaymentsFullPricePrice(id, price)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let id = "id_example"; // String | 
let price = "price_example"; // String | 
apiInstance.getOrganisationsIdPaymentsFullPricePrice(id, price, (error, data, response) => {
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


## getPasswordForgotten

> getPasswordForgotten()



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
apiInstance.getPasswordForgotten((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getPasswordForgottenKey

> getPasswordForgottenKey(key)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let key = "key_example"; // String | 
apiInstance.getPasswordForgottenKey(key, (error, data, response) => {
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
 **key** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getPaymentsCouponsName

> getPaymentsCouponsName(name)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let name = "name_example"; // String | 
apiInstance.getPaymentsCouponsName(name, (error, data, response) => {
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
 **name** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getPaymentsProviders

> [PaymentProvider] getPaymentsProviders()



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
apiInstance.getPaymentsProviders((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**[PaymentProvider]**](PaymentProvider.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPaymentsTokensStripe

> getPaymentsTokensStripe()



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
apiInstance.getPaymentsTokensStripe((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getProductsAddonProviders

> [Provider] getProductsAddonProviders()



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
apiInstance.getProductsAddonProviders((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**[Provider]**](Provider.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getProductsAddonProvidersProviderId

> Provider getProductsAddonProvidersProviderId(providerId)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let providerId = "providerId_example"; // String | 
apiInstance.getProductsAddonProvidersProviderId(providerId, (error, data, response) => {
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

### Return type

[**Provider**](Provider.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getProductsCountries

> Country getProductsCountries()



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
apiInstance.getProductsCountries((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**Country**](Country.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getProductsCountrycodes

> Country getProductsCountrycodes()



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
apiInstance.getProductsCountrycodes((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**Country**](Country.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getProductsInstances

> [Instance] getProductsInstances(opts)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let opts = {
  '_for': "_for_example" // String | 
};
apiInstance.getProductsInstances(opts, (error, data, response) => {
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
 **_for** | **String**|  | [optional] 

### Return type

[**[Instance]**](Instance.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getProductsInstancesTypeVersion

> Instance getProductsInstancesTypeVersion(type, version, opts)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let type = "type_example"; // String | 
let version = "version_example"; // String | 
let opts = {
  '_for': "_for_example", // String | 
  'app': "app_example" // String | 
};
apiInstance.getProductsInstancesTypeVersion(type, version, opts, (error, data, response) => {
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
 **type** | **String**|  | 
 **version** | **String**|  | 
 **_for** | **String**|  | [optional] 
 **app** | **String**|  | [optional] 

### Return type

[**Instance**](Instance.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getProductsPackages

> getProductsPackages(opts)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let opts = {
  'coupon': "coupon_example", // String | 
  'orgaId': "orgaId_example", // String | 
  'currency': "currency_example" // String | 
};
apiInstance.getProductsPackages(opts, (error, data, response) => {
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
 **coupon** | **String**|  | [optional] 
 **orgaId** | **String**|  | [optional] 
 **currency** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getProductsPrices

> getProductsPrices()



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
apiInstance.getProductsPrices((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getProductsZones

> [Zone] getProductsZones()



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
apiInstance.getProductsZones((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**[Zone]**](Zone.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSelf

> User getSelf()



Get information about yourself

### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
apiInstance.getSelf((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**User**](User.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSelfAddons

> [Addon] getSelfAddons()

Addon

Get all the addons

### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
apiInstance.getSelfAddons((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**[Addon]**](Addon.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSelfAddonsAddonId

> Addon getSelfAddonsAddonId(addonId)

Specific addon

Get a specific addon

### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let addonId = "addonId_example"; // String | 
apiInstance.getSelfAddonsAddonId(addonId, (error, data, response) => {
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
 **addonId** | **String**|  | 

### Return type

[**Addon**](Addon.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSelfAddonsAddonIdApplications

> [Application] getSelfAddonsAddonIdApplications(addonId)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let addonId = "addonId_example"; // String | 
apiInstance.getSelfAddonsAddonIdApplications(addonId, (error, data, response) => {
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
 **addonId** | **String**|  | 

### Return type

[**[Application]**](Application.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSelfAddonsAddonIdEnv

> [ListEnv] getSelfAddonsAddonIdEnv(addonId)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let addonId = "addonId_example"; // String | 
apiInstance.getSelfAddonsAddonIdEnv(addonId, (error, data, response) => {
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
 **addonId** | **String**|  | 

### Return type

[**[ListEnv]**](ListEnv.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSelfAddonsAddonIdSso

> Sso getSelfAddonsAddonIdSso(addonId)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let addonId = "addonId_example"; // String | 
apiInstance.getSelfAddonsAddonIdSso(addonId, (error, data, response) => {
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
 **addonId** | **String**|  | 

### Return type

[**Sso**](Sso.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSelfAddonsAddonIdTags

> [String] getSelfAddonsAddonIdTags(addonId)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let addonId = "addonId_example"; // String | 
apiInstance.getSelfAddonsAddonIdTags(addonId, (error, data, response) => {
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
 **addonId** | **String**|  | 

### Return type

**[String]**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## getSelfApplications

> [Application] getSelfApplications()



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
apiInstance.getSelfApplications((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**[Application]**](Application.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSelfApplicationsAppId

> Application getSelfApplicationsAppId(appId)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let appId = "appId_example"; // String | 
apiInstance.getSelfApplicationsAppId(appId, (error, data, response) => {
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

### Return type

[**Application**](Application.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSelfApplicationsAppIdAddons

> [Addon] getSelfApplicationsAppIdAddons(appId)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let appId = "appId_example"; // String | 
apiInstance.getSelfApplicationsAppIdAddons(appId, (error, data, response) => {
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

### Return type

[**[Addon]**](Addon.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSelfApplicationsAppIdAddonsEnv

> [Env] getSelfApplicationsAppIdAddonsEnv(appId)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let appId = "appId_example"; // String | 
apiInstance.getSelfApplicationsAppIdAddonsEnv(appId, (error, data, response) => {
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

### Return type

[**[Env]**](Env.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSelfApplicationsAppIdDependencies

> [Application] getSelfApplicationsAppIdDependencies(appId)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let appId = "appId_example"; // String | 
apiInstance.getSelfApplicationsAppIdDependencies(appId, (error, data, response) => {
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

### Return type

[**[Application]**](Application.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSelfApplicationsAppIdDependenciesDependencyId

> getSelfApplicationsAppIdDependenciesDependencyId(dependencyId, appId, wannabeApplication)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let dependencyId = "dependencyId_example"; // String | 
let appId = "appId_example"; // String | 
let wannabeApplication = new CleverCloudApi.WannabeApplication(); // WannabeApplication | 
apiInstance.getSelfApplicationsAppIdDependenciesDependencyId(dependencyId, appId, wannabeApplication, (error, data, response) => {
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
 **wannabeApplication** | [**WannabeApplication**](WannabeApplication.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## getSelfApplicationsAppIdDependents

> [Application] getSelfApplicationsAppIdDependents(appId)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let appId = "appId_example"; // String | 
apiInstance.getSelfApplicationsAppIdDependents(appId, (error, data, response) => {
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

### Return type

[**[Application]**](Application.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSelfApplicationsAppIdDeployments

> [Deployment] getSelfApplicationsAppIdDeployments(appId, opts)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let appId = "appId_example"; // String | 
let opts = {
  'limit': "limit_example", // String | 
  'offset': "offset_example", // String | 
  'action': "action_example" // String | 
};
apiInstance.getSelfApplicationsAppIdDeployments(appId, opts, (error, data, response) => {
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


## getSelfApplicationsAppIdEnv

> [ListEnv] getSelfApplicationsAppIdEnv(appId)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let appId = "appId_example"; // String | 
apiInstance.getSelfApplicationsAppIdEnv(appId, (error, data, response) => {
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

### Return type

[**[ListEnv]**](ListEnv.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSelfApplicationsAppIdInstances

> [Instance] getSelfApplicationsAppIdInstances(appId)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let appId = "appId_example"; // String | 
apiInstance.getSelfApplicationsAppIdInstances(appId, (error, data, response) => {
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

### Return type

[**[Instance]**](Instance.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSelfApplicationsAppIdTags

> [String] getSelfApplicationsAppIdTags(appId)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let appId = "appId_example"; // String | 
apiInstance.getSelfApplicationsAppIdTags(appId, (error, data, response) => {
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

### Return type

**[String]**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## getSelfApplicationsAppIdVhosts

> [Vhost] getSelfApplicationsAppIdVhosts(appId)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let appId = "appId_example"; // String | 
apiInstance.getSelfApplicationsAppIdVhosts(appId, (error, data, response) => {
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

### Return type

[**[Vhost]**](Vhost.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSelfApplicationsAppIdVhostsFavourite

> Vhost getSelfApplicationsAppIdVhostsFavourite(appId)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let appId = "appId_example"; // String | 
apiInstance.getSelfApplicationsAppIdVhostsFavourite(appId, (error, data, response) => {
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

### Return type

[**Vhost**](Vhost.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSelfConfirmationEmail

> getSelfConfirmationEmail()



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
apiInstance.getSelfConfirmationEmail((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getSelfConsumers

> [Consumer] getSelfConsumers()



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
apiInstance.getSelfConsumers((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**[Consumer]**](Consumer.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSelfConsumersKey

> Consumer getSelfConsumersKey(key)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let key = "key_example"; // String | 
apiInstance.getSelfConsumersKey(key, (error, data, response) => {
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
 **key** | **String**|  | 

### Return type

[**Consumer**](Consumer.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSelfConsumersKeySecret

> Secret getSelfConsumersKeySecret(key)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let key = "key_example"; // String | 
apiInstance.getSelfConsumersKeySecret(key, (error, data, response) => {
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
 **key** | **String**|  | 

### Return type

[**Secret**](Secret.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSelfConsumptions

> Conso getSelfConsumptions(opts)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let opts = {
  'appId': "appId_example", // String | 
  'from': "from_example", // String | 
  'to': "to_example" // String | 
};
apiInstance.getSelfConsumptions(opts, (error, data, response) => {
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


## getSelfCredits

> Credits getSelfCredits()



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
apiInstance.getSelfCredits((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**Credits**](Credits.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSelfEmails

> [String] getSelfEmails()



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
apiInstance.getSelfEmails((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

**[String]**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## getSelfId

> String getSelfId()



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
apiInstance.getSelfId((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## getSelfInstances

> [Instance] getSelfInstances()



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
apiInstance.getSelfInstances((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**[Instance]**](Instance.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSelfKeys

> [Key] getSelfKeys()



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
apiInstance.getSelfKeys((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**[Key]**](Key.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSelfPaymentInfo

> getSelfPaymentInfo()



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
apiInstance.getSelfPaymentInfo((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getSelfPaymentsBillings

> getSelfPaymentsBillings()



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
apiInstance.getSelfPaymentsBillings((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getSelfPaymentsBillingsBid

> getSelfPaymentsBillingsBid(bid)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let bid = "bid_example"; // String | 
apiInstance.getSelfPaymentsBillingsBid(bid, (error, data, response) => {
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
 **bid** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getSelfPaymentsBillingsBidPdf

> getSelfPaymentsBillingsBidPdf(bid, opts)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let bid = "bid_example"; // String | 
let opts = {
  'token': "token_example" // String | 
};
apiInstance.getSelfPaymentsBillingsBidPdf(bid, opts, (error, data, response) => {
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
 **bid** | **String**|  | 
 **token** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getSelfPaymentsFullpricePrice

> getSelfPaymentsFullpricePrice(price)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let price = "price_example"; // String | 
apiInstance.getSelfPaymentsFullpricePrice(price, (error, data, response) => {
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
 **price** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getSelfPaymentsMethods

> getSelfPaymentsMethods()



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
apiInstance.getSelfPaymentsMethods((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getSelfTokens

> [Token] getSelfTokens()



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
apiInstance.getSelfTokens((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**[Token]**](Token.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSelfValidateEmail

> getSelfValidateEmail(opts)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let opts = {
  'validationKey': "validationKey_example" // String | 
};
apiInstance.getSelfValidateEmail(opts, (error, data, response) => {
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
 **validationKey** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getSummary

> Summary getSummary()



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
apiInstance.getSummary((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**Summary**](Summary.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getUsersId

> User getUsersId(id)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let id = "id_example"; // String | 
apiInstance.getUsersId(id, (error, data, response) => {
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

[**User**](User.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getUsersIdApplications

> [Application] getUsersIdApplications(id)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let id = "id_example"; // String | 
apiInstance.getUsersIdApplications(id, (error, data, response) => {
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


## getUsersUserIdGitInfo

> getUsersUserIdGitInfo(userId)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let userId = "userId_example"; // String | 
apiInstance.getUsersUserIdGitInfo(userId, (error, data, response) => {
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
 **userId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getVendorApps

> [Application] getVendorApps(opts)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let opts = {
  'offset': 56 // Number | 
};
apiInstance.getVendorApps(opts, (error, data, response) => {
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
 **offset** | **Number**|  | [optional] 

### Return type

[**[Application]**](Application.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getVendorAppsAddonId

> getVendorAppsAddonId(addonId)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let addonId = "addonId_example"; // String | 
apiInstance.getVendorAppsAddonId(addonId, (error, data, response) => {
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
 **addonId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## listNetworkGroupMembers

> [Schema1] listNetworkGroupMembers(ownerId, networkGroupId, opts)

List members

Lists members in a Network Group.

### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let ownerId = "ownerId_example"; // String | Automatically added
let networkGroupId = "networkGroupId_example"; // String | Automatically added
let opts = {
  'body': null // Object | 
};
apiInstance.listNetworkGroupMembers(ownerId, networkGroupId, opts, (error, data, response) => {
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


## listNetworkGroupPeers

> [Object] listNetworkGroupPeers(ownerId, networkGroupId, opts)

List peers

Lists peers in a Network Group.

### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let ownerId = "ownerId_example"; // String | Automatically added
let networkGroupId = "networkGroupId_example"; // String | Automatically added
let opts = {
  'body': null // Object | 
};
apiInstance.listNetworkGroupPeers(ownerId, networkGroupId, opts, (error, data, response) => {
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


## listNetworkGroups

> [Object] listNetworkGroups(ownerId, opts)

List Network Groups

Lists Network Groups from an owner.

### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let ownerId = "ownerId_example"; // String | Automatically added
let opts = {
  'body': null // Object | 
};
apiInstance.listNetworkGroups(ownerId, opts, (error, data, response) => {
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


## logsAppIdDrainsGet

> logsAppIdDrainsGet(appId)



Fetch the logs drains for a given application

### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let appId = "appId_example"; // String | Automatically added
apiInstance.logsAppIdDrainsGet(appId, (error, data, response) => {
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
 **appId** | **String**| Automatically added | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## logsAppIdDrainsIdOrUrlDelete

> logsAppIdDrainsIdOrUrlDelete(appId)



Delete the logs drain by id or url for a given application

### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let appId = "appId_example"; // String | Automatically added
apiInstance.logsAppIdDrainsIdOrUrlDelete(appId, (error, data, response) => {
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
 **appId** | **String**| Automatically added | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## logsAppIdDrainsIdOrUrlGet

> logsAppIdDrainsIdOrUrlGet(appId)



Fetch the logs drain by id or url for a given application

### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let appId = "appId_example"; // String | Automatically added
apiInstance.logsAppIdDrainsIdOrUrlGet(appId, (error, data, response) => {
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
 **appId** | **String**| Automatically added | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## logsAppIdDrainsPost

> logsAppIdDrainsPost(appId)



Add a log drain for a given application

### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let appId = "appId_example"; // String | Automatically added
apiInstance.logsAppIdDrainsPost(appId, (error, data, response) => {
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
 **appId** | **String**| Automatically added | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## logsAppIdGet

> logsAppIdGet(appId, opts)



Fetch the logs for a given application

### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let appId = "appId_example"; // String | Application Id
let opts = {
  'limit': 56, // Number | Number of lines to return
  'order': "'desc'", // String | Logs order
  'after': new Date("2013-10-20T19:20:30+01:00"), // Date | Lowest bound for logs date, ISO 8601
  'before': new Date("2013-10-20T19:20:30+01:00"), // Date | Highest bounds for logs date, ISO 8601
  'filter': "filter_example", // String | A pattern to filter with
  'deploymentId': "deploymentId_example" // String | Only fetch logs emitted by this deployment
};
apiInstance.logsAppIdGet(appId, opts, (error, data, response) => {
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
 **appId** | **String**| Application Id | 
 **limit** | **Number**| Number of lines to return | [optional] 
 **order** | **String**| Logs order | [optional] [default to &#39;desc&#39;]
 **after** | **Date**| Lowest bound for logs date, ISO 8601 | [optional] 
 **before** | **Date**| Highest bounds for logs date, ISO 8601 | [optional] 
 **filter** | **String**| A pattern to filter with | [optional] 
 **deploymentId** | **String**| Only fetch logs emitted by this deployment | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## logsAppIdSseGet

> logsAppIdSseGet(appId)



Retrieve logs as they come through a sse connection. To have authorization, you have to add &#x60;authorization&#x3D;oAuthAuthorizationString&#x60; as query param.

### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let appId = "appId_example"; // String | Automatically added
apiInstance.logsAppIdSseGet(appId, (error, data, response) => {
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
 **appId** | **String**| Automatically added | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## logsDrainsDrainIdPut

> logsDrainsDrainIdPut(drainId)



Fetch all the logs drains (ccadmin dedicated route)

### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let drainId = "drainId_example"; // String | Automatically added
apiInstance.logsDrainsDrainIdPut(drainId, (error, data, response) => {
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
 **drainId** | **String**| Automatically added | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## logsDrainsGet

> logsDrainsGet()



Fetch all the logs drains (ccadmin dedicated route)

### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
apiInstance.logsDrainsGet((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## logsLogsChunkedAppIdGet

> logsLogsChunkedAppIdGet(appId, opts)



Retrieve logs as they come through a chunked, never-ending response

### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let appId = "appId_example"; // String | Application Id
let opts = {
  'download': true // Boolean | Tell the user-agent to download the body as a file
};
apiInstance.logsLogsChunkedAppIdGet(appId, opts, (error, data, response) => {
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
 **appId** | **String**| Application Id | 
 **download** | **Boolean**| Tell the user-agent to download the body as a file | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## logsLogsSocketAppIdGet

> logsLogsSocketAppIdGet(appId, opts)



Retrieve logs as they come through a websocket connection. To have authorization, you have to send a &#x60;{ \&quot;message_type\&quot;: \&quot;oauth\&quot;, \&quot;authorization\&quot;: \&quot;oauth authorization string\&quot; }&#x60; message

### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let appId = "appId_example"; // String | Application Id
let opts = {
  'since': new Date("2013-10-20T19:20:30+01:00"), // Date | Only fetch logs newer than this (ISO-8601 formatted) date
  'filter': "filter_example", // String | A pattern to filter with
  'deploymentId': "deploymentId_example" // String | Only fetch logs emitted by this deployment
};
apiInstance.logsLogsSocketAppIdGet(appId, opts, (error, data, response) => {
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
 **appId** | **String**| Application Id | 
 **since** | **Date**| Only fetch logs newer than this (ISO-8601 formatted) date | [optional] 
 **filter** | **String**| A pattern to filter with | [optional] 
 **deploymentId** | **String**| Only fetch logs emitted by this deployment | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## logsSocketAppIdGet

> logsSocketAppIdGet(appId)



WebSocket to get logs for :appID. Optional queryString arg bind_to_es&#x3D;true to bind WS on log storage and not real time AMQP broker

### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let appId = "appId_example"; // String | Automatically added
apiInstance.logsSocketAppIdGet(appId, (error, data, response) => {
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
 **appId** | **String**| Automatically added | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## notificationsEmailhooksOwnerIdGet

> notificationsEmailhooksOwnerIdGet(ownerId)



list created e-mail hooks

### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let ownerId = "ownerId_example"; // String | Automatically added
apiInstance.notificationsEmailhooksOwnerIdGet(ownerId, (error, data, response) => {
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

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## notificationsEmailhooksOwnerIdIdDelete

> notificationsEmailhooksOwnerIdIdDelete(ownerId)



delete an e-mail hook

### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let ownerId = "ownerId_example"; // String | Automatically added
apiInstance.notificationsEmailhooksOwnerIdIdDelete(ownerId, (error, data, response) => {
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

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## notificationsEmailhooksOwnerIdIdPut

> notificationsEmailhooksOwnerIdIdPut(ownerId)



edit an e-mail hook

### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let ownerId = "ownerId_example"; // String | Automatically added
apiInstance.notificationsEmailhooksOwnerIdIdPut(ownerId, (error, data, response) => {
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

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## notificationsEmailhooksOwnerIdPost

> notificationsEmailhooksOwnerIdPost(ownerId)



create a hook for e-mail notifications

### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let ownerId = "ownerId_example"; // String | Automatically added
apiInstance.notificationsEmailhooksOwnerIdPost(ownerId, (error, data, response) => {
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

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## notificationsInfoEventsGet

> notificationsInfoEventsGet()



list available events

### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
apiInstance.notificationsInfoEventsGet((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## notificationsInfoWebhookformatsGet

> notificationsInfoWebhookformatsGet()



list available webhook formats

### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
apiInstance.notificationsInfoWebhookformatsGet((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## notificationsWebhooksOwnerIdGet

> notificationsWebhooksOwnerIdGet(ownerId)



list created hooks

### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let ownerId = "ownerId_example"; // String | Automatically added
apiInstance.notificationsWebhooksOwnerIdGet(ownerId, (error, data, response) => {
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

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## notificationsWebhooksOwnerIdIdDelete

> notificationsWebhooksOwnerIdIdDelete(ownerId)



delete a hook

### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let ownerId = "ownerId_example"; // String | Automatically added
apiInstance.notificationsWebhooksOwnerIdIdDelete(ownerId, (error, data, response) => {
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

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## notificationsWebhooksOwnerIdIdPut

> notificationsWebhooksOwnerIdIdPut(ownerId)



edit a hook

### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let ownerId = "ownerId_example"; // String | Automatically added
apiInstance.notificationsWebhooksOwnerIdIdPut(ownerId, (error, data, response) => {
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

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## notificationsWebhooksOwnerIdPost

> notificationsWebhooksOwnerIdPost(ownerId)



create a hook for notifications

### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let ownerId = "ownerId_example"; // String | Automatically added
apiInstance.notificationsWebhooksOwnerIdPost(ownerId, (error, data, response) => {
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

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## oauthAccessTokenQueryPost

> oauthAccessTokenQueryPost(opts)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let opts = {
  'oauthConsumerKey': "oauthConsumerKey_example", // String | 
  'oauthToken': "oauthToken_example", // String | 
  'oauthSignatureMethod': "oauthSignatureMethod_example", // String | 
  'oauthSignature': "oauthSignature_example", // String | 
  'oauthTimestamp': "oauthTimestamp_example", // String | 
  'oauthNonce': "oauthNonce_example", // String | 
  'oauthVersion': "oauthVersion_example", // String | 
  'oauthVerifier': "oauthVerifier_example", // String | 
  'oauthCallback': "oauthCallback_example", // String | 
  'oauthTokenSecret': "oauthTokenSecret_example", // String | 
  'oauthCallbackConfirmed': "oauthCallbackConfirmed_example" // String | 
};
apiInstance.oauthAccessTokenQueryPost(opts, (error, data, response) => {
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
 **oauthConsumerKey** | **String**|  | [optional] 
 **oauthToken** | **String**|  | [optional] 
 **oauthSignatureMethod** | **String**|  | [optional] 
 **oauthSignature** | **String**|  | [optional] 
 **oauthTimestamp** | **String**|  | [optional] 
 **oauthNonce** | **String**|  | [optional] 
 **oauthVersion** | **String**|  | [optional] 
 **oauthVerifier** | **String**|  | [optional] 
 **oauthCallback** | **String**|  | [optional] 
 **oauthTokenSecret** | **String**|  | [optional] 
 **oauthCallbackConfirmed** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## oauthRequestTokenQueryPost

> oauthRequestTokenQueryPost(opts)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let opts = {
  'oauthConsumerKey': "oauthConsumerKey_example", // String | 
  'oauthToken': "oauthToken_example", // String | 
  'oauthSignatureMethod': "oauthSignatureMethod_example", // String | 
  'oauthSignature': "oauthSignature_example", // String | 
  'oauthTimestamp': "oauthTimestamp_example", // String | 
  'oauthNonce': "oauthNonce_example", // String | 
  'oauthVersion': "oauthVersion_example", // String | 
  'oauthVerifier': "oauthVerifier_example", // String | 
  'oauthCallback': "oauthCallback_example", // String | 
  'oauthTokenSecret': "oauthTokenSecret_example", // String | 
  'oauthCallbackConfirmed': "oauthCallbackConfirmed_example" // String | 
};
apiInstance.oauthRequestTokenQueryPost(opts, (error, data, response) => {
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
 **oauthConsumerKey** | **String**|  | [optional] 
 **oauthToken** | **String**|  | [optional] 
 **oauthSignatureMethod** | **String**|  | [optional] 
 **oauthSignature** | **String**|  | [optional] 
 **oauthTimestamp** | **String**|  | [optional] 
 **oauthNonce** | **String**|  | [optional] 
 **oauthVersion** | **String**|  | [optional] 
 **oauthVerifier** | **String**|  | [optional] 
 **oauthCallback** | **String**|  | [optional] 
 **oauthTokenSecret** | **String**|  | [optional] 
 **oauthCallbackConfirmed** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## openapiGet

> openapiGet()



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
apiInstance.openapiGet((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## openapiTypeGet

> openapiTypeGet(type)

Get the swagger for this API as {type}

Get the swagger for this API as {type}. Type can be either \&quot;yml\&quot; or \&quot;json\&quot;.

### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let type = "type_example"; // String | 
apiInstance.openapiTypeGet(type, (error, data, response) => {
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
 **type** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## organisationsIdAddonprovidersProviderIdDelete

> organisationsIdAddonprovidersProviderIdDelete(id, providerId)

Remove an add-on provider

Remove a given add-on provider. providerId must be owned by organisation {id}.

### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let id = "id_example"; // String | 
let providerId = "providerId_example"; // String | 
apiInstance.organisationsIdAddonprovidersProviderIdDelete(id, providerId, (error, data, response) => {
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


## organisationsIdAddonsAddonIdInstancesGet

> [SupernovaInstanceView] organisationsIdAddonsAddonIdInstancesGet(id, addonId, opts)

List instances for this add-on.

### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let id = "id_example"; // String | 
let addonId = "addonId_example"; // String | 
let opts = {
  'deploymentId': "deploymentId_example", // String | 
  'withDeleted': "withDeleted_example" // String | 
};
apiInstance.organisationsIdAddonsAddonIdInstancesGet(id, addonId, opts, (error, data, response) => {
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


## organisationsIdAddonsAddonIdInstancesInstanceIdGet

> SupernovaInstanceView organisationsIdAddonsAddonIdInstancesInstanceIdGet(instanceId, id, addonId)

Get a specific instance for {addonId}

### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let instanceId = "instanceId_example"; // String | 
let id = "id_example"; // String | 
let addonId = "addonId_example"; // String | 
apiInstance.organisationsIdAddonsAddonIdInstancesInstanceIdGet(instanceId, id, addonId, (error, data, response) => {
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


## organisationsIdAddonsAddonIdMigrationsGet

> [AddonMigration] organisationsIdAddonsAddonIdMigrationsGet(id, addonId)

Get past migrations from add-on.

### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let id = "id_example"; // String | 
let addonId = "addonId_example"; // String | 
apiInstance.organisationsIdAddonsAddonIdMigrationsGet(id, addonId, (error, data, response) => {
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


## organisationsIdAddonsAddonIdMigrationsMigrationIdGet

> AddonMigration organisationsIdAddonsAddonIdMigrationsMigrationIdGet(migrationId, id, addonId)

Get a given migration

### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let migrationId = "migrationId_example"; // String | 
let id = "id_example"; // String | 
let addonId = "addonId_example"; // String | 
apiInstance.organisationsIdAddonsAddonIdMigrationsMigrationIdGet(migrationId, id, addonId, (error, data, response) => {
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


## organisationsIdAddonsAddonIdMigrationsPost

> Object organisationsIdAddonsAddonIdMigrationsPost(id, addonId, organisationsIdAddonsAddonIdMigrationsPostRequest)

Start a new add-on migration

### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let id = "id_example"; // String | 
let addonId = "addonId_example"; // String | 
let organisationsIdAddonsAddonIdMigrationsPostRequest = new CleverCloudApi.OrganisationsIdAddonsAddonIdMigrationsPostRequest(); // OrganisationsIdAddonsAddonIdMigrationsPostRequest | 
apiInstance.organisationsIdAddonsAddonIdMigrationsPost(id, addonId, organisationsIdAddonsAddonIdMigrationsPostRequest, (error, data, response) => {
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


## organisationsIdAddonsAddonIdSsoGet

> Sso organisationsIdAddonsAddonIdSsoGet(id, addonId)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let id = "id_example"; // String | 
let addonId = "addonId_example"; // String | 
apiInstance.organisationsIdAddonsAddonIdSsoGet(id, addonId, (error, data, response) => {
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


## organisationsIdAddonsPreordersPost

> organisationsIdAddonsPreordersPost(id, wannabeAddon)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let id = "id_example"; // String | 
let wannabeAddon = new CleverCloudApi.WannabeAddon(); // WannabeAddon | 
apiInstance.organisationsIdAddonsPreordersPost(id, wannabeAddon, (error, data, response) => {
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


## organisationsIdApplicationsAppIdBranchPut

> organisationsIdApplicationsAppIdBranchPut(appId, id)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let appId = "appId_example"; // String | 
let id = "id_example"; // String | 
apiInstance.organisationsIdApplicationsAppIdBranchPut(appId, id, (error, data, response) => {
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


## organisationsIdApplicationsAppIdBranchesGet

> organisationsIdApplicationsAppIdBranchesGet(appId, id)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let appId = "appId_example"; // String | 
let id = "id_example"; // String | 
apiInstance.organisationsIdApplicationsAppIdBranchesGet(appId, id, (error, data, response) => {
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


## organisationsIdApplicationsAppIdBuildflavorPut

> organisationsIdApplicationsAppIdBuildflavorPut(appId, id)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let appId = "appId_example"; // String | 
let id = "id_example"; // String | 
apiInstance.organisationsIdApplicationsAppIdBuildflavorPut(appId, id, (error, data, response) => {
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


## organisationsIdApplicationsAppIdDependenciesEnvGet

> [LinkedAppEnv] organisationsIdApplicationsAppIdDependenciesEnvGet(appId, id)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let appId = "appId_example"; // String | 
let id = "id_example"; // String | 
apiInstance.organisationsIdApplicationsAppIdDependenciesEnvGet(appId, id, (error, data, response) => {
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


## organisationsIdApplicationsAppIdDeploymentsDeploymentIdGet

> organisationsIdApplicationsAppIdDeploymentsDeploymentIdGet(appId, deploymentId, id)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let appId = "appId_example"; // String | 
let deploymentId = "deploymentId_example"; // String | 
let id = "id_example"; // String | 
apiInstance.organisationsIdApplicationsAppIdDeploymentsDeploymentIdGet(appId, deploymentId, id, (error, data, response) => {
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


## organisationsIdApplicationsAppIdExposedEnvGet

> organisationsIdApplicationsAppIdExposedEnvGet(appId, id)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let appId = "appId_example"; // String | 
let id = "id_example"; // String | 
apiInstance.organisationsIdApplicationsAppIdExposedEnvGet(appId, id, (error, data, response) => {
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


## organisationsIdApplicationsAppIdExposedEnvPut

> organisationsIdApplicationsAppIdExposedEnvPut(appId, id)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let appId = "appId_example"; // String | 
let id = "id_example"; // String | 
apiInstance.organisationsIdApplicationsAppIdExposedEnvPut(appId, id, (error, data, response) => {
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


## organisationsIdApplicationsAppIdInstancesInstanceIdGet

> organisationsIdApplicationsAppIdInstancesInstanceIdGet(instanceId, appId, id)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let instanceId = "instanceId_example"; // String | 
let appId = "appId_example"; // String | 
let id = "id_example"; // String | 
apiInstance.organisationsIdApplicationsAppIdInstancesInstanceIdGet(instanceId, appId, id, (error, data, response) => {
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


## organisationsIdPaymentsBillingsUnpaidGet

> organisationsIdPaymentsBillingsUnpaidGet(id)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let id = "id_example"; // String | 
apiInstance.organisationsIdPaymentsBillingsUnpaidGet(id, (error, data, response) => {
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


## organisationsIdPaymentsMethodsDefaultGet

> organisationsIdPaymentsMethodsDefaultGet(id)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let id = "id_example"; // String | 
apiInstance.organisationsIdPaymentsMethodsDefaultGet(id, (error, data, response) => {
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


## organisationsIdPaymentsMethodsDefaultPut

> organisationsIdPaymentsMethodsDefaultPut(id, paymentData)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let id = "id_example"; // String | 
let paymentData = new CleverCloudApi.PaymentData(); // PaymentData | 
apiInstance.organisationsIdPaymentsMethodsDefaultPut(id, paymentData, (error, data, response) => {
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


## organisationsIdPaymentsMethodsGet

> organisationsIdPaymentsMethodsGet(id)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let id = "id_example"; // String | 
apiInstance.organisationsIdPaymentsMethodsGet(id, (error, data, response) => {
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


## organisationsIdPaymentsMethodsMIdDelete

> organisationsIdPaymentsMethodsMIdDelete(mId, id)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let mId = "mId_example"; // String | 
let id = "id_example"; // String | 
apiInstance.organisationsIdPaymentsMethodsMIdDelete(mId, id, (error, data, response) => {
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


## organisationsIdPaymentsMethodsPost

> organisationsIdPaymentsMethodsPost(id, body)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let id = "id_example"; // String | 
let body = new CleverCloudApi.Body(); // Body | 
apiInstance.organisationsIdPaymentsMethodsPost(id, body, (error, data, response) => {
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


## organisationsIdPaymentsMonthlyinvoiceGet

> organisationsIdPaymentsMonthlyinvoiceGet(id)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let id = "id_example"; // String | 
apiInstance.organisationsIdPaymentsMonthlyinvoiceGet(id, (error, data, response) => {
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


## organisationsIdPaymentsMonthlyinvoiceMaxcreditPut

> organisationsIdPaymentsMonthlyinvoiceMaxcreditPut(id)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let id = "id_example"; // String | 
apiInstance.organisationsIdPaymentsMonthlyinvoiceMaxcreditPut(id, (error, data, response) => {
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


## organisationsIdPaymentsRecurringGet

> organisationsIdPaymentsRecurringGet(id)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let id = "id_example"; // String | 
apiInstance.organisationsIdPaymentsRecurringGet(id, (error, data, response) => {
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


## paymentsAssetsPayButtonTokenButtonPngGet

> paymentsAssetsPayButtonTokenButtonPngGet(token)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let token = "token_example"; // String | 
apiInstance.paymentsAssetsPayButtonTokenButtonPngGet(token, (error, data, response) => {
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
 **token** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## paymentsBidEndStripePost

> paymentsBidEndStripePost(bid)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let bid = "bid_example"; // String | 
apiInstance.paymentsBidEndStripePost(bid, (error, data, response) => {
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
 **bid** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## postAuthorize

> postAuthorize()



Handled by our API.

### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
apiInstance.postAuthorize((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## postGithubRedeploy

> postGithubRedeploy(opts)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let opts = {
  'userAgent': "userAgent_example", // String | 
  'xGithubEvent': "xGithubEvent_example", // String | 
  'xHubSignature': "xHubSignature_example" // String | 
};
apiInstance.postGithubRedeploy(opts, (error, data, response) => {
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
 **userAgent** | **String**|  | [optional] 
 **xGithubEvent** | **String**|  | [optional] 
 **xHubSignature** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## postGithubSignup

> postGithubSignup(opts)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let opts = {
  'transactionId': "transactionId_example", // String | 
  'name': "name_example", // String | 
  'otherId': "otherId_example", // String | 
  'otherEmail': "otherEmail_example", // String | 
  'password': "password_example", // String | 
  'autoLink': "autoLink_example", // String | 
  'terms': "terms_example" // String | 
};
apiInstance.postGithubSignup(opts, (error, data, response) => {
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
 **transactionId** | **String**|  | [optional] 
 **name** | **String**|  | [optional] 
 **otherId** | **String**|  | [optional] 
 **otherEmail** | **String**|  | [optional] 
 **password** | **String**|  | [optional] 
 **autoLink** | **String**|  | [optional] 
 **terms** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## postOauthAccessToken

> postOauthAccessToken(opts)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let opts = {
  'oauthConsumerKey': "oauthConsumerKey_example", // String | 
  'oauthToken': "oauthToken_example", // String | 
  'oauthSignatureMethod': "oauthSignatureMethod_example", // String | 
  'oauthSignature': "oauthSignature_example", // String | 
  'oauthTimestamp': "oauthTimestamp_example", // String | 
  'oauthNonce': "oauthNonce_example", // String | 
  'oauthVersion': "oauthVersion_example", // String | 
  'oauthVerifier': "oauthVerifier_example", // String | 
  'oauthCallback': "oauthCallback_example", // String | 
  'oauthTokenSecret': "oauthTokenSecret_example", // String | 
  'oauthCallbackConfirmed': "oauthCallbackConfirmed_example" // String | 
};
apiInstance.postOauthAccessToken(opts, (error, data, response) => {
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
 **oauthConsumerKey** | **String**|  | [optional] 
 **oauthToken** | **String**|  | [optional] 
 **oauthSignatureMethod** | **String**|  | [optional] 
 **oauthSignature** | **String**|  | [optional] 
 **oauthTimestamp** | **String**|  | [optional] 
 **oauthNonce** | **String**|  | [optional] 
 **oauthVersion** | **String**|  | [optional] 
 **oauthVerifier** | **String**|  | [optional] 
 **oauthCallback** | **String**|  | [optional] 
 **oauthTokenSecret** | **String**|  | [optional] 
 **oauthCallbackConfirmed** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## postOauthAuthorize

> postOauthAuthorize(opts)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let opts = {
  'almighty': "almighty_example", // String | 
  'accessOrganisations': "accessOrganisations_example", // String | 
  'manageOrganisations': "manageOrganisations_example", // String | 
  'manageOrganisationsServices': "manageOrganisationsServices_example", // String | 
  'manageOrganisationsApplications': "manageOrganisationsApplications_example", // String | 
  'manageOrganisationsMembers': "manageOrganisationsMembers_example", // String | 
  'accessOrganisationsBills': "accessOrganisationsBills_example", // String | 
  'accessOrganisationsCreditCount': "accessOrganisationsCreditCount_example", // String | 
  'accessOrganisationsConsumptionStatistics': "accessOrganisationsConsumptionStatistics_example", // String | 
  'accessPersonalInformation': "accessPersonalInformation_example", // String | 
  'managePersonalInformation': "managePersonalInformation_example", // String | 
  'manageSshKeys': "manageSshKeys_example", // String | 
  'manageServices': "manageServices_example", // String | 
  'manageApplications': "manageApplications_example", // String | 
  'accessBills': "accessBills_example", // String | 
  'accessCreditCount': "accessCreditCount_example", // String | 
  'accessConsumptionStatistics': "accessConsumptionStatistics_example", // String | 
  'cookie': "cookie_example" // String | 
};
apiInstance.postOauthAuthorize(opts, (error, data, response) => {
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
 **almighty** | **String**|  | [optional] 
 **accessOrganisations** | **String**|  | [optional] 
 **manageOrganisations** | **String**|  | [optional] 
 **manageOrganisationsServices** | **String**|  | [optional] 
 **manageOrganisationsApplications** | **String**|  | [optional] 
 **manageOrganisationsMembers** | **String**|  | [optional] 
 **accessOrganisationsBills** | **String**|  | [optional] 
 **accessOrganisationsCreditCount** | **String**|  | [optional] 
 **accessOrganisationsConsumptionStatistics** | **String**|  | [optional] 
 **accessPersonalInformation** | **String**|  | [optional] 
 **managePersonalInformation** | **String**|  | [optional] 
 **manageSshKeys** | **String**|  | [optional] 
 **manageServices** | **String**|  | [optional] 
 **manageApplications** | **String**|  | [optional] 
 **accessBills** | **String**|  | [optional] 
 **accessCreditCount** | **String**|  | [optional] 
 **accessConsumptionStatistics** | **String**|  | [optional] 
 **cookie** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## postOauthRequestToken

> postOauthRequestToken(opts)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let opts = {
  'oauthConsumerKey': "oauthConsumerKey_example", // String | 
  'oauthToken': "oauthToken_example", // String | 
  'oauthSignatureMethod': "oauthSignatureMethod_example", // String | 
  'oauthSignature': "oauthSignature_example", // String | 
  'oauthTimestamp': "oauthTimestamp_example", // String | 
  'oauthNonce': "oauthNonce_example", // String | 
  'oauthVersion': "oauthVersion_example", // String | 
  'oauthVerifier': "oauthVerifier_example", // String | 
  'oauthCallback': "oauthCallback_example", // String | 
  'oauthTokenSecret': "oauthTokenSecret_example", // String | 
  'oauthCallbackConfirmed': "oauthCallbackConfirmed_example" // String | 
};
apiInstance.postOauthRequestToken(opts, (error, data, response) => {
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
 **oauthConsumerKey** | **String**|  | [optional] 
 **oauthToken** | **String**|  | [optional] 
 **oauthSignatureMethod** | **String**|  | [optional] 
 **oauthSignature** | **String**|  | [optional] 
 **oauthTimestamp** | **String**|  | [optional] 
 **oauthNonce** | **String**|  | [optional] 
 **oauthVersion** | **String**|  | [optional] 
 **oauthVerifier** | **String**|  | [optional] 
 **oauthCallback** | **String**|  | [optional] 
 **oauthTokenSecret** | **String**|  | [optional] 
 **oauthCallbackConfirmed** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## postOrganisations

> Organisation postOrganisations(wannabeOrganisation)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let wannabeOrganisation = new CleverCloudApi.WannabeOrganisation(); // WannabeOrganisation | 
apiInstance.postOrganisations(wannabeOrganisation, (error, data, response) => {
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


## postOrganisationsIdAddonproviders

> Provider postOrganisationsIdAddonproviders(id, wannabeAddonProvider)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let id = "id_example"; // String | 
let wannabeAddonProvider = new CleverCloudApi.WannabeAddonProvider(); // WannabeAddonProvider | 
apiInstance.postOrganisationsIdAddonproviders(id, wannabeAddonProvider, (error, data, response) => {
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


## postOrganisationsIdAddonprovidersProviderIdFeatures

> Feature postOrganisationsIdAddonprovidersProviderIdFeatures(id, providerId, wannabeFeature)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let id = "id_example"; // String | 
let providerId = "providerId_example"; // String | 
let wannabeFeature = new CleverCloudApi.WannabeFeature(); // WannabeFeature | 
apiInstance.postOrganisationsIdAddonprovidersProviderIdFeatures(id, providerId, wannabeFeature, (error, data, response) => {
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


## postOrganisationsIdAddonprovidersProviderIdPlans

> Plan postOrganisationsIdAddonprovidersProviderIdPlans(id, providerId, wannabePlan)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let id = "id_example"; // String | 
let providerId = "providerId_example"; // String | 
let wannabePlan = new CleverCloudApi.WannabePlan(); // WannabePlan | 
apiInstance.postOrganisationsIdAddonprovidersProviderIdPlans(id, providerId, wannabePlan, (error, data, response) => {
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


## postOrganisationsIdAddonprovidersProviderIdTesters

> postOrganisationsIdAddonprovidersProviderIdTesters(id, providerId)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let id = "id_example"; // String | 
let providerId = "providerId_example"; // String | 
apiInstance.postOrganisationsIdAddonprovidersProviderIdTesters(id, providerId, (error, data, response) => {
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


## postOrganisationsIdAddons

> Addon postOrganisationsIdAddons(id, wannabeAddon)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let id = "id_example"; // String | 
let wannabeAddon = new CleverCloudApi.WannabeAddon(); // WannabeAddon | 
apiInstance.postOrganisationsIdAddons(id, wannabeAddon, (error, data, response) => {
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


## postOrganisationsIdApplications

> Application postOrganisationsIdApplications(id, wannabeApplication)



Creates an application. If you want to create a Github app, you need to replace the oauthApp field with what you will find here: https://github.com/CleverCloud/doc.clever-cloud.com/issues/179

### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let id = "id_example"; // String | 
let wannabeApplication = new CleverCloudApi.WannabeApplication(); // WannabeApplication | 
apiInstance.postOrganisationsIdApplications(id, wannabeApplication, (error, data, response) => {
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


## postOrganisationsIdApplicationsAppIdAddons

> postOrganisationsIdApplicationsAppIdAddons(id, appId, body)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let id = "id_example"; // String | 
let appId = "appId_example"; // String | 
let body = new CleverCloudApi.Body(); // Body | 
apiInstance.postOrganisationsIdApplicationsAppIdAddons(id, appId, body, (error, data, response) => {
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


## postOrganisationsIdApplicationsAppIdInstances

> postOrganisationsIdApplicationsAppIdInstances(id, appId, opts)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let id = "id_example"; // String | 
let appId = "appId_example"; // String | 
let opts = {
  'commit': "commit_example" // String | 
};
apiInstance.postOrganisationsIdApplicationsAppIdInstances(id, appId, opts, (error, data, response) => {
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


## postOrganisationsIdConsumers

> postOrganisationsIdConsumers(id, wannabeConsumer)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let id = "id_example"; // String | 
let wannabeConsumer = new CleverCloudApi.WannabeConsumer(); // WannabeConsumer | 
apiInstance.postOrganisationsIdConsumers(id, wannabeConsumer, (error, data, response) => {
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


## postOrganisationsIdMembers

> postOrganisationsIdMembers(id, body, opts)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let id = "id_example"; // String | 
let body = new CleverCloudApi.Schema2(); // Schema2 | 
let opts = {
  'invitationKey': "invitationKey_example" // String | 
};
apiInstance.postOrganisationsIdMembers(id, body, opts, (error, data, response) => {
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


## postOrganisationsIdPaymentsBillings

> postOrganisationsIdPaymentsBillings(id)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let id = "id_example"; // String | 
apiInstance.postOrganisationsIdPaymentsBillings(id, (error, data, response) => {
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


## postPasswordForgotten

> postPasswordForgotten(opts)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let opts = {
  'login': "login_example", // String | 
  'dropTokens': "dropTokens_example", // String | 
  'testerPass': "testerPass_example" // String | 
};
apiInstance.postPasswordForgotten(opts, (error, data, response) => {
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
 **login** | **String**|  | [optional] 
 **dropTokens** | **String**|  | [optional] 
 **testerPass** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## postPasswordForgottenKey

> postPasswordForgottenKey(key, opts)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let key = "key_example"; // String | 
let opts = {
  'pass': "pass_example", // String | 
  'pass2': "pass2_example" // String | 
};
apiInstance.postPasswordForgottenKey(key, opts, (error, data, response) => {
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
 **key** | **String**|  | 
 **pass** | **String**|  | [optional] 
 **pass2** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## postSelfAddons

> postSelfAddons(wannabeAddon)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let wannabeAddon = new CleverCloudApi.WannabeAddon(); // WannabeAddon | 
apiInstance.postSelfAddons(wannabeAddon, (error, data, response) => {
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
 **wannabeAddon** | [**WannabeAddon**](WannabeAddon.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## postSelfApplications

> postSelfApplications(wannabeApplication)



Creates an application. If you want to create a Github app, you need to replace the oauthApp field with what you will find here: https://github.com/CleverCloud/doc.clever-cloud.com/issues/179

### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let wannabeApplication = new CleverCloudApi.WannabeApplication(); // WannabeApplication | 
apiInstance.postSelfApplications(wannabeApplication, (error, data, response) => {
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
 **wannabeApplication** | [**WannabeApplication**](WannabeApplication.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## postSelfApplicationsAppIdAddons

> postSelfApplicationsAppIdAddons(appId, body)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let appId = "appId_example"; // String | 
let body = new CleverCloudApi.Body(); // Body | 
apiInstance.postSelfApplicationsAppIdAddons(appId, body, (error, data, response) => {
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
 **body** | [**Body**](Body.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## postSelfApplicationsAppIdInstances

> postSelfApplicationsAppIdInstances(appId, opts)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let appId = "appId_example"; // String | 
let opts = {
  'commit': "commit_example" // String | 
};
apiInstance.postSelfApplicationsAppIdInstances(appId, opts, (error, data, response) => {
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
 **commit** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## postSelfConsumers

> postSelfConsumers(wannabeConsumer)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let wannabeConsumer = new CleverCloudApi.WannabeConsumer(); // WannabeConsumer | 
apiInstance.postSelfConsumers(wannabeConsumer, (error, data, response) => {
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
 **wannabeConsumer** | [**WannabeConsumer**](WannabeConsumer.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## postSelfPaymentsBillings

> postSelfPaymentsBillings()



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
apiInstance.postSelfPaymentsBillings((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## postSelfPaymentsMethods

> postSelfPaymentsMethods()



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
apiInstance.postSelfPaymentsMethods((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## postUsers

> postUsers(wannabeUser, opts)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let wannabeUser = new CleverCloudApi.WannabeUser(); // WannabeUser | 
let opts = {
  'invitationKey': "invitationKey_example", // String | 
  'addonBetaInvitationKey': "addonBetaInvitationKey_example", // String | 
  'email': "email_example", // String | 
  'pass': "pass_example", // String | 
  'urlNext': "urlNext_example", // String | 
  'terms': "terms_example" // String | 
};
apiInstance.postUsers(wannabeUser, opts, (error, data, response) => {
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
 **wannabeUser** | [**WannabeUser**](WannabeUser.md)|  | 
 **invitationKey** | **String**|  | [optional] 
 **addonBetaInvitationKey** | **String**|  | [optional] 
 **email** | **String**|  | [optional] 
 **pass** | **String**|  | [optional] 
 **urlNext** | **String**|  | [optional] 
 **terms** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## postVendorBillingOwnerId

> postVendorBillingOwnerId(addonId, wannabeAddonBilling)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let addonId = "addonId_example"; // String | 
let wannabeAddonBilling = new CleverCloudApi.WannabeAddonBilling(); // WannabeAddonBilling | 
apiInstance.postVendorBillingOwnerId(addonId, wannabeAddonBilling, (error, data, response) => {
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
 **addonId** | **String**|  | 
 **wannabeAddonBilling** | [**WannabeAddonBilling**](WannabeAddonBilling.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## productsAddonprovidersProviderIdVersionsGet

> productsAddonprovidersProviderIdVersionsGet(providerId)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let providerId = "providerId_example"; // String | 
apiInstance.productsAddonprovidersProviderIdVersionsGet(providerId, (error, data, response) => {
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
 **providerId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## productsMfaKindsGet

> productsMfaKindsGet()



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
apiInstance.productsMfaKindsGet((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## putOrganisationsId

> Organisation putOrganisationsId(id, wannabeOrganisation)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let id = "id_example"; // String | 
let wannabeOrganisation = new CleverCloudApi.WannabeOrganisation(); // WannabeOrganisation | 
apiInstance.putOrganisationsId(id, wannabeOrganisation, (error, data, response) => {
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


## putOrganisationsIdAddonprovidersProviderId

> Provider putOrganisationsIdAddonprovidersProviderId(id, providerId, wannabeAddonProvider)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let id = "id_example"; // String | 
let providerId = "providerId_example"; // String | 
let wannabeAddonProvider = new CleverCloudApi.WannabeAddonProvider(); // WannabeAddonProvider | 
apiInstance.putOrganisationsIdAddonprovidersProviderId(id, providerId, wannabeAddonProvider, (error, data, response) => {
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


## putOrganisationsIdAddonprovidersProviderIdPlansPlanId

> Plan putOrganisationsIdAddonprovidersProviderIdPlansPlanId(id, providerId, planId, wannabePlan)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let id = "id_example"; // String | 
let providerId = "providerId_example"; // String | 
let planId = "planId_example"; // String | 
let wannabePlan = new CleverCloudApi.WannabePlan(); // WannabePlan | 
apiInstance.putOrganisationsIdAddonprovidersProviderIdPlansPlanId(id, providerId, planId, wannabePlan, (error, data, response) => {
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


## putOrganisationsIdAddonprovidersProviderIdPlansPlanIdFeaturesFeatureName

> putOrganisationsIdAddonprovidersProviderIdPlansPlanIdFeaturesFeatureName(id, featureName, providerId, planId, wannabePlanFeature)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let id = "id_example"; // String | 
let featureName = "featureName_example"; // String | 
let providerId = "providerId_example"; // String | 
let planId = "planId_example"; // String | 
let wannabePlanFeature = new CleverCloudApi.WannabePlanFeature(); // WannabePlanFeature | 
apiInstance.putOrganisationsIdAddonprovidersProviderIdPlansPlanIdFeaturesFeatureName(id, featureName, providerId, planId, wannabePlanFeature, (error, data, response) => {
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


## putOrganisationsIdAddonsAddonId

> Addon putOrganisationsIdAddonsAddonId(id, addonId, wannabeAddon)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let id = "id_example"; // String | 
let addonId = "addonId_example"; // String | 
let wannabeAddon = new CleverCloudApi.WannabeAddon(); // WannabeAddon | 
apiInstance.putOrganisationsIdAddonsAddonId(id, addonId, wannabeAddon, (error, data, response) => {
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


## putOrganisationsIdAddonsAddonIdTagsTag

> putOrganisationsIdAddonsAddonIdTagsTag(id, tag, addonId, body)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let id = "id_example"; // String | 
let tag = "tag_example"; // String | 
let addonId = "addonId_example"; // String | 
let body = new CleverCloudApi.Body(); // Body | 
apiInstance.putOrganisationsIdAddonsAddonIdTagsTag(id, tag, addonId, body, (error, data, response) => {
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


## putOrganisationsIdApplicationsAppId

> Application putOrganisationsIdApplicationsAppId(id, appId, wannabeApplication)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let id = "id_example"; // String | 
let appId = "appId_example"; // String | 
let wannabeApplication = new CleverCloudApi.WannabeApplication(); // WannabeApplication | 
apiInstance.putOrganisationsIdApplicationsAppId(id, appId, wannabeApplication, (error, data, response) => {
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


## putOrganisationsIdApplicationsAppIdDependenciesDependencyId

> putOrganisationsIdApplicationsAppIdDependenciesDependencyId(dependencyId, appId, id, body)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let dependencyId = "dependencyId_example"; // String | 
let appId = "appId_example"; // String | 
let id = "id_example"; // String | 
let body = new CleverCloudApi.Body(); // Body | 
apiInstance.putOrganisationsIdApplicationsAppIdDependenciesDependencyId(dependencyId, appId, id, body, (error, data, response) => {
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


## putOrganisationsIdApplicationsAppIdEnv

> ListEnv putOrganisationsIdApplicationsAppIdEnv(id, appId, wannabeEnv)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let id = "id_example"; // String | 
let appId = "appId_example"; // String | 
let wannabeEnv = new CleverCloudApi.WannabeEnv(); // WannabeEnv | 
apiInstance.putOrganisationsIdApplicationsAppIdEnv(id, appId, wannabeEnv, (error, data, response) => {
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


## putOrganisationsIdApplicationsAppIdEnvEnvName

> ListEnv putOrganisationsIdApplicationsAppIdEnvEnvName(id, appId, envName, wannabeEnv)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let id = "id_example"; // String | 
let appId = "appId_example"; // String | 
let envName = "envName_example"; // String | 
let wannabeEnv = new CleverCloudApi.WannabeEnv(); // WannabeEnv | 
apiInstance.putOrganisationsIdApplicationsAppIdEnvEnvName(id, appId, envName, wannabeEnv, (error, data, response) => {
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


## putOrganisationsIdApplicationsAppIdTagsTag

> putOrganisationsIdApplicationsAppIdTagsTag(id, appId, tag, body)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let id = "id_example"; // String | 
let appId = "appId_example"; // String | 
let tag = "tag_example"; // String | 
let body = new CleverCloudApi.Body(); // Body | 
apiInstance.putOrganisationsIdApplicationsAppIdTagsTag(id, appId, tag, body, (error, data, response) => {
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


## putOrganisationsIdApplicationsAppIdVhostsDomain

> putOrganisationsIdApplicationsAppIdVhostsDomain(id, appId, domain, vhost)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let id = "id_example"; // String | 
let appId = "appId_example"; // String | 
let domain = "domain_example"; // String | 
let vhost = new CleverCloudApi.Vhost(); // Vhost | 
apiInstance.putOrganisationsIdApplicationsAppIdVhostsDomain(id, appId, domain, vhost, (error, data, response) => {
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


## putOrganisationsIdApplicationsAppIdVhostsFavourite

> putOrganisationsIdApplicationsAppIdVhostsFavourite(id, appId, vhost)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let id = "id_example"; // String | 
let appId = "appId_example"; // String | 
let vhost = new CleverCloudApi.Vhost(); // Vhost | 
apiInstance.putOrganisationsIdApplicationsAppIdVhostsFavourite(id, appId, vhost, (error, data, response) => {
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


## putOrganisationsIdAvatar

> putOrganisationsIdAvatar(id)



If you want to upload an image from your computer, send the image in the body of the request without anything else.

### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let id = "id_example"; // String | 
apiInstance.putOrganisationsIdAvatar(id, (error, data, response) => {
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


## putOrganisationsIdConsumersKey

> putOrganisationsIdConsumersKey(id, key, wannabeConsumer)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let id = "id_example"; // String | 
let key = "key_example"; // String | 
let wannabeConsumer = new CleverCloudApi.WannabeConsumer(); // WannabeConsumer | 
apiInstance.putOrganisationsIdConsumersKey(id, key, wannabeConsumer, (error, data, response) => {
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


## putOrganisationsIdMembersUserId

> putOrganisationsIdMembersUserId(id, userId, body)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let id = "id_example"; // String | 
let userId = "userId_example"; // String | 
let body = new CleverCloudApi.Schema2(); // Schema2 | 
apiInstance.putOrganisationsIdMembersUserId(id, userId, body, (error, data, response) => {
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


## putOrganisationsIdPaymentsBillingsBid

> putOrganisationsIdPaymentsBillingsBid(id, bid)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let id = "id_example"; // String | 
let bid = "bid_example"; // String | 
apiInstance.putOrganisationsIdPaymentsBillingsBid(id, bid, (error, data, response) => {
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


## putSelf

> putSelf(wannabeUser)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let wannabeUser = new CleverCloudApi.WannabeUser(); // WannabeUser | 
apiInstance.putSelf(wannabeUser, (error, data, response) => {
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
 **wannabeUser** | [**WannabeUser**](WannabeUser.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## putSelfAddonsAddonId

> putSelfAddonsAddonId(addonId, wannabeAddon)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let addonId = "addonId_example"; // String | 
let wannabeAddon = new CleverCloudApi.WannabeAddon(); // WannabeAddon | 
apiInstance.putSelfAddonsAddonId(addonId, wannabeAddon, (error, data, response) => {
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
 **addonId** | **String**|  | 
 **wannabeAddon** | [**WannabeAddon**](WannabeAddon.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## putSelfAddonsAddonIdPlan

> putSelfAddonsAddonIdPlan(addonId, wannabePlan)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let addonId = "addonId_example"; // String | 
let wannabePlan = new CleverCloudApi.WannabePlan(); // WannabePlan | 
apiInstance.putSelfAddonsAddonIdPlan(addonId, wannabePlan, (error, data, response) => {
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
 **addonId** | **String**|  | 
 **wannabePlan** | [**WannabePlan**](WannabePlan.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## putSelfAddonsAddonIdTagsTag

> putSelfAddonsAddonIdTagsTag(tag, addonId, body)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let tag = "tag_example"; // String | 
let addonId = "addonId_example"; // String | 
let body = new CleverCloudApi.Body(); // Body | 
apiInstance.putSelfAddonsAddonIdTagsTag(tag, addonId, body, (error, data, response) => {
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


## putSelfApplicationsAppId

> putSelfApplicationsAppId(appId, wannabeApplication)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let appId = "appId_example"; // String | 
let wannabeApplication = new CleverCloudApi.WannabeApplication(); // WannabeApplication | 
apiInstance.putSelfApplicationsAppId(appId, wannabeApplication, (error, data, response) => {
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
 **wannabeApplication** | [**WannabeApplication**](WannabeApplication.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## putSelfApplicationsAppIdEnv

> putSelfApplicationsAppIdEnv(appId, wannabeEnv)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let appId = "appId_example"; // String | 
let wannabeEnv = new CleverCloudApi.WannabeEnv(); // WannabeEnv | 
apiInstance.putSelfApplicationsAppIdEnv(appId, wannabeEnv, (error, data, response) => {
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
 **wannabeEnv** | [**WannabeEnv**](WannabeEnv.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## putSelfApplicationsAppIdEnvEnvName

> putSelfApplicationsAppIdEnvEnvName(appId, envName, wannabeEnv)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let appId = "appId_example"; // String | 
let envName = "envName_example"; // String | 
let wannabeEnv = new CleverCloudApi.WannabeEnv(); // WannabeEnv | 
apiInstance.putSelfApplicationsAppIdEnvEnvName(appId, envName, wannabeEnv, (error, data, response) => {
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
 **envName** | **String**|  | 
 **wannabeEnv** | [**WannabeEnv**](WannabeEnv.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## putSelfApplicationsAppIdTagsTag

> putSelfApplicationsAppIdTagsTag(appId, tag, body)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let appId = "appId_example"; // String | 
let tag = "tag_example"; // String | 
let body = new CleverCloudApi.Body(); // Body | 
apiInstance.putSelfApplicationsAppIdTagsTag(appId, tag, body, (error, data, response) => {
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
 **tag** | **String**|  | 
 **body** | [**Body**](Body.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## putSelfApplicationsAppIdVhostsDomain

> putSelfApplicationsAppIdVhostsDomain(appId, domain, vhost)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let appId = "appId_example"; // String | 
let domain = "domain_example"; // String | 
let vhost = new CleverCloudApi.Vhost(); // Vhost | 
apiInstance.putSelfApplicationsAppIdVhostsDomain(appId, domain, vhost, (error, data, response) => {
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
 **domain** | **String**|  | 
 **vhost** | [**Vhost**](Vhost.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## putSelfApplicationsAppIdVhostsFavourite

> putSelfApplicationsAppIdVhostsFavourite(appId, vhost)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let appId = "appId_example"; // String | 
let vhost = new CleverCloudApi.Vhost(); // Vhost | 
apiInstance.putSelfApplicationsAppIdVhostsFavourite(appId, vhost, (error, data, response) => {
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
 **vhost** | [**Vhost**](Vhost.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## putSelfAvatar

> putSelfAvatar(avatar)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let avatar = new CleverCloudApi.Avatar(); // Avatar | 
apiInstance.putSelfAvatar(avatar, (error, data, response) => {
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
 **avatar** | [**Avatar**](Avatar.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## putSelfChangePassword

> ChangePassword putSelfChangePassword()



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
apiInstance.putSelfChangePassword((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**ChangePassword**](ChangePassword.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## putSelfConsumersKey

> putSelfConsumersKey(key, wannabeConsumer)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let key = "key_example"; // String | 
let wannabeConsumer = new CleverCloudApi.WannabeConsumer(); // WannabeConsumer | 
apiInstance.putSelfConsumersKey(key, wannabeConsumer, (error, data, response) => {
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
 **key** | **String**|  | 
 **wannabeConsumer** | [**WannabeConsumer**](WannabeConsumer.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## putSelfEmailsEmail

> putSelfEmailsEmail(email, body)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let email = "email_example"; // String | 
let body = new CleverCloudApi.Body(); // Body | 
apiInstance.putSelfEmailsEmail(email, body, (error, data, response) => {
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
 **email** | **String**|  | 
 **body** | [**Body**](Body.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## putSelfKeysKey

> putSelfKeysKey(key, body)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let key = "key_example"; // String | 
let body = new CleverCloudApi.Body(); // Body | 
apiInstance.putSelfKeysKey(key, body, (error, data, response) => {
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
 **key** | **String**|  | 
 **body** | [**Body**](Body.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## putSelfPaymentsBillingsBid

> putSelfPaymentsBillingsBid(bid)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let bid = "bid_example"; // String | 
apiInstance.putSelfPaymentsBillingsBid(bid, (error, data, response) => {
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
 **bid** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## putVendorAppsAddonId

> putVendorAppsAddonId(addonId)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let addonId = "addonId_example"; // String | 
apiInstance.putVendorAppsAddonId(addonId, (error, data, response) => {
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
 **addonId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## selfAddonsPreordersPost

> selfAddonsPreordersPost(wannabeAddon)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let wannabeAddon = new CleverCloudApi.WannabeAddon(); // WannabeAddon | 
apiInstance.selfAddonsPreordersPost(wannabeAddon, (error, data, response) => {
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
 **wannabeAddon** | [**WannabeAddon**](WannabeAddon.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## selfApplicationsAppIdBranchPut

> selfApplicationsAppIdBranchPut(appId)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let appId = "appId_example"; // String | 
apiInstance.selfApplicationsAppIdBranchPut(appId, (error, data, response) => {
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

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## selfApplicationsAppIdBranchesGet

> selfApplicationsAppIdBranchesGet(appId)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let appId = "appId_example"; // String | 
apiInstance.selfApplicationsAppIdBranchesGet(appId, (error, data, response) => {
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

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## selfApplicationsAppIdBuildflavorPut

> selfApplicationsAppIdBuildflavorPut(appId)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let appId = "appId_example"; // String | 
apiInstance.selfApplicationsAppIdBuildflavorPut(appId, (error, data, response) => {
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

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## selfApplicationsAppIdDependenciesEnvGet

> [LinkedAppEnv] selfApplicationsAppIdDependenciesEnvGet(appId)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let appId = "appId_example"; // String | 
apiInstance.selfApplicationsAppIdDependenciesEnvGet(appId, (error, data, response) => {
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

### Return type

[**[LinkedAppEnv]**](LinkedAppEnv.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## selfApplicationsAppIdDeploymentsDeploymentIdGet

> selfApplicationsAppIdDeploymentsDeploymentIdGet(appId, deploymentId)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let appId = "appId_example"; // String | 
let deploymentId = "deploymentId_example"; // String | 
apiInstance.selfApplicationsAppIdDeploymentsDeploymentIdGet(appId, deploymentId, (error, data, response) => {
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

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## selfApplicationsAppIdExposedEnvGet

> selfApplicationsAppIdExposedEnvGet(appId)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let appId = "appId_example"; // String | 
apiInstance.selfApplicationsAppIdExposedEnvGet(appId, (error, data, response) => {
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

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## selfApplicationsAppIdExposedEnvPut

> selfApplicationsAppIdExposedEnvPut(appId)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let appId = "appId_example"; // String | 
apiInstance.selfApplicationsAppIdExposedEnvPut(appId, (error, data, response) => {
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

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## selfApplicationsAppIdInstancesInstanceIdGet

> selfApplicationsAppIdInstancesInstanceIdGet(instanceId, appId)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let instanceId = "instanceId_example"; // String | 
let appId = "appId_example"; // String | 
apiInstance.selfApplicationsAppIdInstancesInstanceIdGet(instanceId, appId, (error, data, response) => {
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

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## selfCliTokensGet

> selfCliTokensGet(opts)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let opts = {
  'cliToken': "cliToken_example" // String | 
};
apiInstance.selfCliTokensGet(opts, (error, data, response) => {
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
 **cliToken** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## selfMfaKindBackupcodesGet

> selfMfaKindBackupcodesGet(kind)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let kind = "kind_example"; // String | 
apiInstance.selfMfaKindBackupcodesGet(kind, (error, data, response) => {
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
 **kind** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## selfMfaKindConfirmationPost

> selfMfaKindConfirmationPost(kind)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let kind = "kind_example"; // String | 
apiInstance.selfMfaKindConfirmationPost(kind, (error, data, response) => {
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
 **kind** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## selfMfaKindDelete

> selfMfaKindDelete(kind)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let kind = "kind_example"; // String | 
apiInstance.selfMfaKindDelete(kind, (error, data, response) => {
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
 **kind** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## selfMfaKindPost

> selfMfaKindPost(kind)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let kind = "kind_example"; // String | 
apiInstance.selfMfaKindPost(kind, (error, data, response) => {
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
 **kind** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## selfMfaKindPut

> selfMfaKindPut(kind)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let kind = "kind_example"; // String | 
apiInstance.selfMfaKindPut(kind, (error, data, response) => {
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
 **kind** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## selfPaymentsMethodsDefaultGet

> selfPaymentsMethodsDefaultGet()



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
apiInstance.selfPaymentsMethodsDefaultGet((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## selfPaymentsMethodsDefaultPut

> selfPaymentsMethodsDefaultPut()



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
apiInstance.selfPaymentsMethodsDefaultPut((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## selfPaymentsMonthlyinvoiceGet

> selfPaymentsMonthlyinvoiceGet()



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
apiInstance.selfPaymentsMonthlyinvoiceGet((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## selfPaymentsMonthlyinvoiceMaxcreditPut

> selfPaymentsMonthlyinvoiceMaxcreditPut()



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
apiInstance.selfPaymentsMonthlyinvoiceMaxcreditPut((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## selfPaymentsRecurringGet

> selfPaymentsRecurringGet()



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
apiInstance.selfPaymentsRecurringGet((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## selfPaymentsTokensStripeGet

> selfPaymentsTokensStripeGet()



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
apiInstance.selfPaymentsTokensStripeGet((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## updateConfigProviderEnv

> [Object] updateConfigProviderEnv(configurationProviderId, requestBody)

Update provider&#39;s addon environment

### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let configurationProviderId = "configurationProviderId_example"; // String | Automatically added
let requestBody = [null]; // [Object] | 
apiInstance.updateConfigProviderEnv(configurationProviderId, requestBody, (error, data, response) => {
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
 **configurationProviderId** | **String**| Automatically added | 
 **requestBody** | [**[Object]**](Object.md)|  | 

### Return type

**[Object]**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## v3LogsAppIdDrainsGet

> v3LogsAppIdDrainsGet(appId)



Fetch the logs drains for a given application

### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let appId = "appId_example"; // String | Automatically added
apiInstance.v3LogsAppIdDrainsGet(appId, (error, data, response) => {
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
 **appId** | **String**| Automatically added | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## v3LogsAppIdDrainsIdOrUrlDelete

> v3LogsAppIdDrainsIdOrUrlDelete(appId)



Delete the logs drain by id or url for a given application

### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let appId = "appId_example"; // String | Automatically added
apiInstance.v3LogsAppIdDrainsIdOrUrlDelete(appId, (error, data, response) => {
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
 **appId** | **String**| Automatically added | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## v3LogsAppIdDrainsIdOrUrlGet

> v3LogsAppIdDrainsIdOrUrlGet(appId)



Fetch the logs drain by id or url for a given application

### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let appId = "appId_example"; // String | Automatically added
apiInstance.v3LogsAppIdDrainsIdOrUrlGet(appId, (error, data, response) => {
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
 **appId** | **String**| Automatically added | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## v3LogsAppIdDrainsPost

> v3LogsAppIdDrainsPost(appId)



Add a log drain for a given application

### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let appId = "appId_example"; // String | Automatically added
apiInstance.v3LogsAppIdDrainsPost(appId, (error, data, response) => {
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
 **appId** | **String**| Automatically added | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## v3LogsAppIdGet

> v3LogsAppIdGet(appId)



Fetch the logs for a given application

### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let appId = "appId_example"; // String | Automatically added
apiInstance.v3LogsAppIdGet(appId, (error, data, response) => {
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
 **appId** | **String**| Automatically added | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## v3LogsAppIdLogsChunkedGet

> v3LogsAppIdLogsChunkedGet(appId)



Retrieve logs as they come through a chunked, never-ending response

### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let appId = "appId_example"; // String | Automatically added
apiInstance.v3LogsAppIdLogsChunkedGet(appId, (error, data, response) => {
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
 **appId** | **String**| Automatically added | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## v3LogsAppIdLogsSocketGet

> v3LogsAppIdLogsSocketGet(appId)



Retrieve logs as they come through a websocket connection. To have authorization, you have to send a &#x60;{ \&quot;message_type\&quot;: \&quot;oauth\&quot;, \&quot;authorization\&quot;: \&quot;oauth authorization string\&quot; }&#x60; message

### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let appId = "appId_example"; // String | Automatically added
apiInstance.v3LogsAppIdLogsSocketGet(appId, (error, data, response) => {
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
 **appId** | **String**| Automatically added | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## vendorAddonsPost

> vendorAddonsPost()



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
apiInstance.vendorAddonsPost((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## vendorAppsAddonIdLogscollectorGet

> vendorAppsAddonIdLogscollectorGet(addonId)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let addonId = "addonId_example"; // String | 
apiInstance.vendorAppsAddonIdLogscollectorGet(addonId, (error, data, response) => {
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
 **addonId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## vendorAppsAddonIdMigrationCallbackPut

> vendorAppsAddonIdMigrationCallbackPut(addonId, opts)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.AllApi();
let addonId = "addonId_example"; // String | 
let opts = {
  'planId': "planId_example", // String | 
  'region': "region_example" // String | 
};
apiInstance.vendorAppsAddonIdMigrationCallbackPut(addonId, opts, (error, data, response) => {
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
 **addonId** | **String**|  | 
 **planId** | **String**|  | [optional] 
 **region** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

