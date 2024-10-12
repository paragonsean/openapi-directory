# AllApi

All URIs are relative to *https://api.clever-cloud.com/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**applicationAppIdEnvironmentGet**](AllApi.md#applicationAppIdEnvironmentGet) | **GET** /application/{appId}/environment |  |
| [**applicationAppIdEnvironmentPut**](AllApi.md#applicationAppIdEnvironmentPut) | **PUT** /application/{appId}/environment |  |
| [**createMatomo**](AllApi.md#createMatomo) | **POST** /v2/providers/addon-matomo/resources | Create Matomo addon |
| [**createNetworkGroup**](AllApi.md#createNetworkGroup) | **POST** /v4/networkgroups/organisations/{ownerId}/networkgroups | Create Network Group |
| [**createNetworkGroupExternalPeer**](AllApi.md#createNetworkGroupExternalPeer) | **POST** /v4/networkgroups/organisations/{ownerId}/networkgroups/{networkGroupId}/external-peers | Add external peer |
| [**createNetworkGroupMember**](AllApi.md#createNetworkGroupMember) | **POST** /v4/networkgroups/organisations/{ownerId}/networkgroups/{networkGroupId}/members | Add member |
| [**deleteGithubLink**](AllApi.md#deleteGithubLink) | **DELETE** /github/link |  |
| [**deleteMatomo**](AllApi.md#deleteMatomo) | **DELETE** /v2/providers/addon-matomo/resources/{matomoId} | Delete Matomo addon |
| [**deleteNetworkGroup**](AllApi.md#deleteNetworkGroup) | **DELETE** /v4/networkgroups/organisations/{ownerId}/networkgroups/{networkGroupId} | Delete Network Group |
| [**deleteNetworkGroupExternalPeer**](AllApi.md#deleteNetworkGroupExternalPeer) | **DELETE** /v4/networkgroups/organisations/{ownerId}/networkgroups/{networkGroupId}/external-peers/{peerId} | Remove external peer |
| [**deleteNetworkGroupMember**](AllApi.md#deleteNetworkGroupMember) | **DELETE** /v4/networkgroups/organisations/{ownerId}/networkgroups/{networkGroupId}/members/{memberId} | Remove member |
| [**deleteNetworkGroupPeer**](AllApi.md#deleteNetworkGroupPeer) | **DELETE** /v4/networkgroups/organisations/{ownerId}/networkgroups/{networkGroupId}/peers/{peerId} | Remove peer |
| [**deleteOrganisationsId**](AllApi.md#deleteOrganisationsId) | **DELETE** /organisations/{id} |  |
| [**deleteOrganisationsIdAddonprovidersProviderIdFeaturesFeatureId**](AllApi.md#deleteOrganisationsIdAddonprovidersProviderIdFeaturesFeatureId) | **DELETE** /organisations/{id}/addonproviders/{providerId}/features/{featureId} |  |
| [**deleteOrganisationsIdAddonprovidersProviderIdPlansPlanId**](AllApi.md#deleteOrganisationsIdAddonprovidersProviderIdPlansPlanId) | **DELETE** /organisations/{id}/addonproviders/{providerId}/plans/{planId} |  |
| [**deleteOrganisationsIdAddonprovidersProviderIdPlansPlanIdFeaturesFeatureName**](AllApi.md#deleteOrganisationsIdAddonprovidersProviderIdPlansPlanIdFeaturesFeatureName) | **DELETE** /organisations/{id}/addonproviders/{providerId}/plans/{planId}/features/{featureName} |  |
| [**deleteOrganisationsIdAddonsAddonId**](AllApi.md#deleteOrganisationsIdAddonsAddonId) | **DELETE** /organisations/{id}/addons/{addonId} |  |
| [**deleteOrganisationsIdAddonsAddonIdTagsTag**](AllApi.md#deleteOrganisationsIdAddonsAddonIdTagsTag) | **DELETE** /organisations/{id}/addons/{addonId}/tags/{tag} |  |
| [**deleteOrganisationsIdApplicationsAppId**](AllApi.md#deleteOrganisationsIdApplicationsAppId) | **DELETE** /organisations/{id}/applications/{appId} |  |
| [**deleteOrganisationsIdApplicationsAppIdAddonsAddonId**](AllApi.md#deleteOrganisationsIdApplicationsAppIdAddonsAddonId) | **DELETE** /organisations/{id}/applications/{appId}/addons/{addonId} |  |
| [**deleteOrganisationsIdApplicationsAppIdDependenciesDependencyId**](AllApi.md#deleteOrganisationsIdApplicationsAppIdDependenciesDependencyId) | **DELETE** /organisations/{id}/applications/{appId}/dependencies/{dependencyId} |  |
| [**deleteOrganisationsIdApplicationsAppIdDeploymentsDeploymentIdInstances**](AllApi.md#deleteOrganisationsIdApplicationsAppIdDeploymentsDeploymentIdInstances) | **DELETE** /organisations/{id}/applications/{appId}/deployments/{deploymentId}/instances |  |
| [**deleteOrganisationsIdApplicationsAppIdEnvEnvName**](AllApi.md#deleteOrganisationsIdApplicationsAppIdEnvEnvName) | **DELETE** /organisations/{id}/applications/{appId}/env/{envName} |  |
| [**deleteOrganisationsIdApplicationsAppIdInstances**](AllApi.md#deleteOrganisationsIdApplicationsAppIdInstances) | **DELETE** /organisations/{id}/applications/{appId}/instances |  |
| [**deleteOrganisationsIdApplicationsAppIdTagsTag**](AllApi.md#deleteOrganisationsIdApplicationsAppIdTagsTag) | **DELETE** /organisations/{id}/applications/{appId}/tags/{tag} |  |
| [**deleteOrganisationsIdApplicationsAppIdVhostsDomain**](AllApi.md#deleteOrganisationsIdApplicationsAppIdVhostsDomain) | **DELETE** /organisations/{id}/applications/{appId}/vhosts/{domain} |  |
| [**deleteOrganisationsIdApplicationsAppIdVhostsFavourite**](AllApi.md#deleteOrganisationsIdApplicationsAppIdVhostsFavourite) | **DELETE** /organisations/{id}/applications/{appId}/vhosts/favourite |  |
| [**deleteOrganisationsIdConsumersKey**](AllApi.md#deleteOrganisationsIdConsumersKey) | **DELETE** /organisations/{id}/consumers/{key} |  |
| [**deleteOrganisationsIdMembersUserId**](AllApi.md#deleteOrganisationsIdMembersUserId) | **DELETE** /organisations/{id}/members/{userId} |  |
| [**deleteOrganisationsIdPaymentsBillingsBid**](AllApi.md#deleteOrganisationsIdPaymentsBillingsBid) | **DELETE** /organisations/{id}/payments/billings/{bid} |  |
| [**deleteOrganisationsIdPaymentsRecurring**](AllApi.md#deleteOrganisationsIdPaymentsRecurring) | **DELETE** /organisations/{id}/payments/recurring |  |
| [**deleteSelf**](AllApi.md#deleteSelf) | **DELETE** /self |  |
| [**deleteSelfAddonsAddonId**](AllApi.md#deleteSelfAddonsAddonId) | **DELETE** /self/addons/{addonId} |  |
| [**deleteSelfAddonsAddonIdTagsTag**](AllApi.md#deleteSelfAddonsAddonIdTagsTag) | **DELETE** /self/addons/{addonId}/tags/{tag} |  |
| [**deleteSelfApplicationsAppId**](AllApi.md#deleteSelfApplicationsAppId) | **DELETE** /self/applications/{appId} |  |
| [**deleteSelfApplicationsAppIdAddonsAddonId**](AllApi.md#deleteSelfApplicationsAppIdAddonsAddonId) | **DELETE** /self/applications/{appId}/addons/{addonId} |  |
| [**deleteSelfApplicationsAppIdDependenciesDependencyId**](AllApi.md#deleteSelfApplicationsAppIdDependenciesDependencyId) | **DELETE** /self/applications/{appId}/dependencies/{dependencyId} |  |
| [**deleteSelfApplicationsAppIdDeploymentsDeploymentIdInstances**](AllApi.md#deleteSelfApplicationsAppIdDeploymentsDeploymentIdInstances) | **DELETE** /self/applications/{appId}/deployments/{deploymentId}/instances |  |
| [**deleteSelfApplicationsAppIdEnvEnvName**](AllApi.md#deleteSelfApplicationsAppIdEnvEnvName) | **DELETE** /self/applications/{appId}/env/{envName} |  |
| [**deleteSelfApplicationsAppIdInstances**](AllApi.md#deleteSelfApplicationsAppIdInstances) | **DELETE** /self/applications/{appId}/instances |  |
| [**deleteSelfApplicationsAppIdTagsTag**](AllApi.md#deleteSelfApplicationsAppIdTagsTag) | **DELETE** /self/applications/{appId}/tags/{tag} |  |
| [**deleteSelfApplicationsAppIdVhostsDomain**](AllApi.md#deleteSelfApplicationsAppIdVhostsDomain) | **DELETE** /self/applications/{appId}/vhosts/{domain} |  |
| [**deleteSelfApplicationsAppIdVhostsFavourite**](AllApi.md#deleteSelfApplicationsAppIdVhostsFavourite) | **DELETE** /self/applications/{appId}/vhosts/favourite |  |
| [**deleteSelfConsumersKey**](AllApi.md#deleteSelfConsumersKey) | **DELETE** /self/consumers/{key} |  |
| [**deleteSelfEmailsEmail**](AllApi.md#deleteSelfEmailsEmail) | **DELETE** /self/emails/{email} |  |
| [**deleteSelfKeysKey**](AllApi.md#deleteSelfKeysKey) | **DELETE** /self/keys/{key} |  |
| [**deleteSelfPaymentsBillingsBid**](AllApi.md#deleteSelfPaymentsBillingsBid) | **DELETE** /self/payments/billings/{bid} |  |
| [**deleteSelfPaymentsMethodsMId**](AllApi.md#deleteSelfPaymentsMethodsMId) | **DELETE** /self/payments/methods/{mId} |  |
| [**deleteSelfPaymentsRecurring**](AllApi.md#deleteSelfPaymentsRecurring) | **DELETE** /self/payments/recurring |  |
| [**deleteSelfTokens**](AllApi.md#deleteSelfTokens) | **DELETE** /self/tokens |  |
| [**deleteSelfTokensToken**](AllApi.md#deleteSelfTokensToken) | **DELETE** /self/tokens/{token} |  |
| [**eventsEventSocketGet**](AllApi.md#eventsEventSocketGet) | **GET** /events/event-socket |  |
| [**getConfigProvider**](AllApi.md#getConfigProvider) | **GET** /v4/addon-providers/config-provider/addons/{configurationProviderId} | Get Addon provider configuration |
| [**getConfigProviderEnv**](AllApi.md#getConfigProviderEnv) | **GET** /v4/addon-providers/config-provider/addons/{configurationProviderId}/env | Get provider&#39;s addon environment |
| [**getGithub**](AllApi.md#getGithub) | **GET** /github |  |
| [**getGithubApplications**](AllApi.md#getGithubApplications) | **GET** /github/applications |  |
| [**getGithubCallback**](AllApi.md#getGithubCallback) | **GET** /github/callback |  |
| [**getGithubEmails**](AllApi.md#getGithubEmails) | **GET** /github/emails |  |
| [**getGithubKeys**](AllApi.md#getGithubKeys) | **GET** /github/keys |  |
| [**getGithubLink**](AllApi.md#getGithubLink) | **GET** /github/link |  |
| [**getGithubLogin**](AllApi.md#getGithubLogin) | **GET** /github/login |  |
| [**getGithubSignup**](AllApi.md#getGithubSignup) | **GET** /github/signup |  |
| [**getGithubUsername**](AllApi.md#getGithubUsername) | **GET** /github/username |  |
| [**getMatomo**](AllApi.md#getMatomo) | **GET** /v4/addon-providers/addon-matomo/addons/{matomoId} | Get Matomo addon |
| [**getMatomoKTokenValidation**](AllApi.md#getMatomoKTokenValidation) | **GET** /v4/addon-providers/addon-matomo/token/validate | Validate a keycloak token |
| [**getNetworkGroup**](AllApi.md#getNetworkGroup) | **GET** /v4/networkgroups/organisations/{ownerId}/networkgroups/{networkGroupId} | Get Network Group |
| [**getNetworkGroupMember**](AllApi.md#getNetworkGroupMember) | **GET** /v4/networkgroups/organisations/{ownerId}/networkgroups/{networkGroupId}/members/{memberId} | Get member |
| [**getNetworkGroupPeer**](AllApi.md#getNetworkGroupPeer) | **GET** /v4/networkgroups/organisations/{ownerId}/networkgroups/{networkGroupId}/peers/{peerId} | Get peer |
| [**getNetworkGroupStream**](AllApi.md#getNetworkGroupStream) | **GET** /v4/networkgroups/organisations/{ownerId}/networkgroups/{networkGroupId}/stream | Network Group SSE |
| [**getNetworkGroupWireGuardConfiguration**](AllApi.md#getNetworkGroupWireGuardConfiguration) | **GET** /v4/networkgroups/organisations/{ownerId}/networkgroups/{networkGroupId}/peers/{peerId}/wireguard/configuration | Get WireGuard® configuration |
| [**getNetworkGroupWireGuardConfigurationStream**](AllApi.md#getNetworkGroupWireGuardConfigurationStream) | **GET** /v4/networkgroups/organisations/{ownerId}/networkgroups/{networkGroupId}/peers/{peerId}/wireguard/configuration/stream | Get WireGuard® configuration |
| [**getNewsfeedEngineering**](AllApi.md#getNewsfeedEngineering) | **GET** /newsfeeds/engineering |  |
| [**getNewsfeedsBlog**](AllApi.md#getNewsfeedsBlog) | **GET** /newsfeeds/blog |  |
| [**getOauthAuthorize**](AllApi.md#getOauthAuthorize) | **GET** /oauth/authorize |  |
| [**getOauthRights**](AllApi.md#getOauthRights) | **GET** /oauth/rights |  |
| [**getOrganisations**](AllApi.md#getOrganisations) | **GET** /organisations |  |
| [**getOrganisationsId**](AllApi.md#getOrganisationsId) | **GET** /organisations/{id} |  |
| [**getOrganisationsIdAddonproviders**](AllApi.md#getOrganisationsIdAddonproviders) | **GET** /organisations/{id}/addonproviders |  |
| [**getOrganisationsIdAddonprovidersProviderId**](AllApi.md#getOrganisationsIdAddonprovidersProviderId) | **GET** /organisations/{id}/addonproviders/{providerId} |  |
| [**getOrganisationsIdAddonprovidersProviderIdFeatures**](AllApi.md#getOrganisationsIdAddonprovidersProviderIdFeatures) | **GET** /organisations/{id}/addonproviders/{providerId}/features |  |
| [**getOrganisationsIdAddonprovidersProviderIdPlans**](AllApi.md#getOrganisationsIdAddonprovidersProviderIdPlans) | **GET** /organisations/{id}/addonproviders/{providerId}/plans |  |
| [**getOrganisationsIdAddonprovidersProviderIdPlansPlanId**](AllApi.md#getOrganisationsIdAddonprovidersProviderIdPlansPlanId) | **GET** /organisations/{id}/addonproviders/{providerId}/plans/{planId} |  |
| [**getOrganisationsIdAddonprovidersProviderIdTags**](AllApi.md#getOrganisationsIdAddonprovidersProviderIdTags) | **GET** /organisations/{id}/addonproviders/{providerId}/tags |  |
| [**getOrganisationsIdAddons**](AllApi.md#getOrganisationsIdAddons) | **GET** /organisations/{id}/addons |  |
| [**getOrganisationsIdAddonsAddonId**](AllApi.md#getOrganisationsIdAddonsAddonId) | **GET** /organisations/{id}/addons/{addonId} |  |
| [**getOrganisationsIdAddonsAddonIdApplications**](AllApi.md#getOrganisationsIdAddonsAddonIdApplications) | **GET** /organisations/{id}/addons/{addonId}/applications |  |
| [**getOrganisationsIdAddonsAddonIdEnv**](AllApi.md#getOrganisationsIdAddonsAddonIdEnv) | **GET** /organisations/{id}/addons/{addonId}/env |  |
| [**getOrganisationsIdAddonsAddonIdSso**](AllApi.md#getOrganisationsIdAddonsAddonIdSso) | **GET** /organisations/{id}/addonproviders/{providerId}/sso |  |
| [**getOrganisationsIdAddonsAddonIdTags**](AllApi.md#getOrganisationsIdAddonsAddonIdTags) | **GET** /organisations/{id}/addons/{addonId}/tags |  |
| [**getOrganisationsIdApplications**](AllApi.md#getOrganisationsIdApplications) | **GET** /organisations/{id}/applications |  |
| [**getOrganisationsIdApplicationsAppId**](AllApi.md#getOrganisationsIdApplicationsAppId) | **GET** /organisations/{id}/applications/{appId} |  |
| [**getOrganisationsIdApplicationsAppIdAddons**](AllApi.md#getOrganisationsIdApplicationsAppIdAddons) | **GET** /organisations/{id}/applications/{appId}/addons |  |
| [**getOrganisationsIdApplicationsAppIdAddonsEnv**](AllApi.md#getOrganisationsIdApplicationsAppIdAddonsEnv) | **GET** /organisations/{id}/applications/{appId}/addons/env |  |
| [**getOrganisationsIdApplicationsAppIdDependencies**](AllApi.md#getOrganisationsIdApplicationsAppIdDependencies) | **GET** /organisations/{id}/applications/{appId}/dependencies |  |
| [**getOrganisationsIdApplicationsAppIdDependents**](AllApi.md#getOrganisationsIdApplicationsAppIdDependents) | **GET** /organisations/{id}/applications/{appId}/dependents |  |
| [**getOrganisationsIdApplicationsAppIdDeployments**](AllApi.md#getOrganisationsIdApplicationsAppIdDeployments) | **GET** /organisations/{id}/applications/{appId}/deployments |  |
| [**getOrganisationsIdApplicationsAppIdEnv**](AllApi.md#getOrganisationsIdApplicationsAppIdEnv) | **GET** /organisations/{id}/applications/{appId}/env |  |
| [**getOrganisationsIdApplicationsAppIdInstances**](AllApi.md#getOrganisationsIdApplicationsAppIdInstances) | **GET** /organisations/{id}/applications/{appId}/instances |  |
| [**getOrganisationsIdApplicationsAppIdTags**](AllApi.md#getOrganisationsIdApplicationsAppIdTags) | **GET** /organisations/{id}/applications/{appId}/tags |  |
| [**getOrganisationsIdApplicationsAppIdVhosts**](AllApi.md#getOrganisationsIdApplicationsAppIdVhosts) | **GET** /organisations/{id}/applications/{appId}/vhosts |  |
| [**getOrganisationsIdApplicationsAppIdVhostsFavourite**](AllApi.md#getOrganisationsIdApplicationsAppIdVhostsFavourite) | **GET** /organisations/{id}/applications/{appId}/vhosts/favourite |  |
| [**getOrganisationsIdConsumers**](AllApi.md#getOrganisationsIdConsumers) | **GET** /organisations/{id}/consumers |  |
| [**getOrganisationsIdConsumersKey**](AllApi.md#getOrganisationsIdConsumersKey) | **GET** /organisations/{id}/consumers/{key} |  |
| [**getOrganisationsIdConsumersKeySecret**](AllApi.md#getOrganisationsIdConsumersKeySecret) | **GET** /organisations/{id}/consumers/{key}/secret |  |
| [**getOrganisationsIdConsumptions**](AllApi.md#getOrganisationsIdConsumptions) | **GET** /organisations/{id}/consumptions |  |
| [**getOrganisationsIdCredits**](AllApi.md#getOrganisationsIdCredits) | **GET** /organisations/{id}/credits |  |
| [**getOrganisationsIdDeployments**](AllApi.md#getOrganisationsIdDeployments) | **GET** /organisations/{id}/deployments |  |
| [**getOrganisationsIdInstances**](AllApi.md#getOrganisationsIdInstances) | **GET** /organisations/{id}/instances |  |
| [**getOrganisationsIdMembers**](AllApi.md#getOrganisationsIdMembers) | **GET** /organisations/{id}/members |  |
| [**getOrganisationsIdPaymentInfo**](AllApi.md#getOrganisationsIdPaymentInfo) | **GET** /organisations/{id}/payment-info |  |
| [**getOrganisationsIdPaymentsBillings**](AllApi.md#getOrganisationsIdPaymentsBillings) | **GET** /organisations/{id}/payments/billings |  |
| [**getOrganisationsIdPaymentsBillingsBid**](AllApi.md#getOrganisationsIdPaymentsBillingsBid) | **GET** /organisations/{id}/payments/billings/{bid} |  |
| [**getOrganisationsIdPaymentsBillingsBidPdf**](AllApi.md#getOrganisationsIdPaymentsBillingsBidPdf) | **GET** /organisations/{id}/payments/billings/{bid}.pdf |  |
| [**getOrganisationsIdPaymentsFullPricePrice**](AllApi.md#getOrganisationsIdPaymentsFullPricePrice) | **GET** /organisations/{id}/payments/fullprice/{price} |  |
| [**getPasswordForgotten**](AllApi.md#getPasswordForgotten) | **GET** /password_forgotten |  |
| [**getPasswordForgottenKey**](AllApi.md#getPasswordForgottenKey) | **GET** /password_forgotten/{key} |  |
| [**getPaymentsCouponsName**](AllApi.md#getPaymentsCouponsName) | **GET** /payments/coupons/{name} |  |
| [**getPaymentsProviders**](AllApi.md#getPaymentsProviders) | **GET** /payments/providers |  |
| [**getPaymentsTokensStripe**](AllApi.md#getPaymentsTokensStripe) | **GET** /payments/tokens/stripe |  |
| [**getProductsAddonProviders**](AllApi.md#getProductsAddonProviders) | **GET** /products/addonproviders |  |
| [**getProductsAddonProvidersProviderId**](AllApi.md#getProductsAddonProvidersProviderId) | **GET** /products/addonproviders/{provider_id} |  |
| [**getProductsCountries**](AllApi.md#getProductsCountries) | **GET** /products/countries |  |
| [**getProductsCountrycodes**](AllApi.md#getProductsCountrycodes) | **GET** /products/countrycodes |  |
| [**getProductsInstances**](AllApi.md#getProductsInstances) | **GET** /products/instances |  |
| [**getProductsInstancesTypeVersion**](AllApi.md#getProductsInstancesTypeVersion) | **GET** /products/instances/{type}-{version} |  |
| [**getProductsPackages**](AllApi.md#getProductsPackages) | **GET** /products/packages |  |
| [**getProductsPrices**](AllApi.md#getProductsPrices) | **GET** /products/prices |  |
| [**getProductsZones**](AllApi.md#getProductsZones) | **GET** /products/zones |  |
| [**getSelf**](AllApi.md#getSelf) | **GET** /self |  |
| [**getSelfAddons**](AllApi.md#getSelfAddons) | **GET** /self/addons | Addon |
| [**getSelfAddonsAddonId**](AllApi.md#getSelfAddonsAddonId) | **GET** /self/addons/{addonId} | Specific addon |
| [**getSelfAddonsAddonIdApplications**](AllApi.md#getSelfAddonsAddonIdApplications) | **GET** /self/addons/{addonId}/applications |  |
| [**getSelfAddonsAddonIdEnv**](AllApi.md#getSelfAddonsAddonIdEnv) | **GET** /self/addons/{addonId}/env |  |
| [**getSelfAddonsAddonIdSso**](AllApi.md#getSelfAddonsAddonIdSso) | **GET** /self/addons/{addonId}/sso |  |
| [**getSelfAddonsAddonIdTags**](AllApi.md#getSelfAddonsAddonIdTags) | **GET** /self/addons/{addonId}/tags |  |
| [**getSelfApplications**](AllApi.md#getSelfApplications) | **GET** /self/applications |  |
| [**getSelfApplicationsAppId**](AllApi.md#getSelfApplicationsAppId) | **GET** /self/applications/{appId} |  |
| [**getSelfApplicationsAppIdAddons**](AllApi.md#getSelfApplicationsAppIdAddons) | **GET** /self/applications/{appId}/addons |  |
| [**getSelfApplicationsAppIdAddonsEnv**](AllApi.md#getSelfApplicationsAppIdAddonsEnv) | **GET** /self/applications/{appId}/addons/env |  |
| [**getSelfApplicationsAppIdDependencies**](AllApi.md#getSelfApplicationsAppIdDependencies) | **GET** /self/applications/{appId}/dependencies |  |
| [**getSelfApplicationsAppIdDependenciesDependencyId**](AllApi.md#getSelfApplicationsAppIdDependenciesDependencyId) | **PUT** /self/applications/{appId}/dependencies/{dependencyId} |  |
| [**getSelfApplicationsAppIdDependents**](AllApi.md#getSelfApplicationsAppIdDependents) | **GET** /self/applications/{appId}/dependents |  |
| [**getSelfApplicationsAppIdDeployments**](AllApi.md#getSelfApplicationsAppIdDeployments) | **GET** /self/applications/{appId}/deployments |  |
| [**getSelfApplicationsAppIdEnv**](AllApi.md#getSelfApplicationsAppIdEnv) | **GET** /self/applications/{appId}/env |  |
| [**getSelfApplicationsAppIdInstances**](AllApi.md#getSelfApplicationsAppIdInstances) | **GET** /self/applications/{appId}/instances |  |
| [**getSelfApplicationsAppIdTags**](AllApi.md#getSelfApplicationsAppIdTags) | **GET** /self/applications/{appId}/tags |  |
| [**getSelfApplicationsAppIdVhosts**](AllApi.md#getSelfApplicationsAppIdVhosts) | **GET** /self/applications/{appId}/vhosts |  |
| [**getSelfApplicationsAppIdVhostsFavourite**](AllApi.md#getSelfApplicationsAppIdVhostsFavourite) | **GET** /self/applications/{appId}/vhosts/favourite |  |
| [**getSelfConfirmationEmail**](AllApi.md#getSelfConfirmationEmail) | **GET** /self/confirmation_email |  |
| [**getSelfConsumers**](AllApi.md#getSelfConsumers) | **GET** /self/consumers |  |
| [**getSelfConsumersKey**](AllApi.md#getSelfConsumersKey) | **GET** /self/consumers/{key} |  |
| [**getSelfConsumersKeySecret**](AllApi.md#getSelfConsumersKeySecret) | **GET** /self/consumers/{key}/secret |  |
| [**getSelfConsumptions**](AllApi.md#getSelfConsumptions) | **GET** /self/consumptions |  |
| [**getSelfCredits**](AllApi.md#getSelfCredits) | **GET** /self/credits |  |
| [**getSelfEmails**](AllApi.md#getSelfEmails) | **GET** /self/emails |  |
| [**getSelfId**](AllApi.md#getSelfId) | **GET** /self/id |  |
| [**getSelfInstances**](AllApi.md#getSelfInstances) | **GET** /self/instances |  |
| [**getSelfKeys**](AllApi.md#getSelfKeys) | **GET** /self/keys |  |
| [**getSelfPaymentInfo**](AllApi.md#getSelfPaymentInfo) | **GET** /self/payment-info |  |
| [**getSelfPaymentsBillings**](AllApi.md#getSelfPaymentsBillings) | **GET** /self/payments/billings |  |
| [**getSelfPaymentsBillingsBid**](AllApi.md#getSelfPaymentsBillingsBid) | **GET** /self/payments/billings/{bid} |  |
| [**getSelfPaymentsBillingsBidPdf**](AllApi.md#getSelfPaymentsBillingsBidPdf) | **GET** /self/payments/billings/{bid}.pdf |  |
| [**getSelfPaymentsFullpricePrice**](AllApi.md#getSelfPaymentsFullpricePrice) | **GET** /self/payments/fullprice/{price} |  |
| [**getSelfPaymentsMethods**](AllApi.md#getSelfPaymentsMethods) | **GET** /self/payments/methods |  |
| [**getSelfTokens**](AllApi.md#getSelfTokens) | **GET** /self/tokens |  |
| [**getSelfValidateEmail**](AllApi.md#getSelfValidateEmail) | **GET** /self/validate_email |  |
| [**getSummary**](AllApi.md#getSummary) | **GET** /summary |  |
| [**getUsersId**](AllApi.md#getUsersId) | **GET** /users/{id} |  |
| [**getUsersIdApplications**](AllApi.md#getUsersIdApplications) | **GET** /users/{id}/applications |  |
| [**getUsersUserIdGitInfo**](AllApi.md#getUsersUserIdGitInfo) | **GET** /users/{userId}/git-info |  |
| [**getVendorApps**](AllApi.md#getVendorApps) | **GET** /vendor/apps |  |
| [**getVendorAppsAddonId**](AllApi.md#getVendorAppsAddonId) | **GET** /vendor/apps/{addonId} |  |
| [**listNetworkGroupMembers**](AllApi.md#listNetworkGroupMembers) | **GET** /v4/networkgroups/organisations/{ownerId}/networkgroups/{networkGroupId}/members | List members |
| [**listNetworkGroupPeers**](AllApi.md#listNetworkGroupPeers) | **GET** /v4/networkgroups/organisations/{ownerId}/networkgroups/{networkGroupId}/peers | List peers |
| [**listNetworkGroups**](AllApi.md#listNetworkGroups) | **GET** /v4/networkgroups/organisations/{ownerId}/networkgroups | List Network Groups |
| [**logsAppIdDrainsGet**](AllApi.md#logsAppIdDrainsGet) | **GET** /logs/{appId}/drains |  |
| [**logsAppIdDrainsIdOrUrlDelete**](AllApi.md#logsAppIdDrainsIdOrUrlDelete) | **DELETE** /logs/{appId}/drains/:idOrUrl |  |
| [**logsAppIdDrainsIdOrUrlGet**](AllApi.md#logsAppIdDrainsIdOrUrlGet) | **GET** /logs/{appId}/drains/:idOrUrl |  |
| [**logsAppIdDrainsPost**](AllApi.md#logsAppIdDrainsPost) | **POST** /logs/{appId}/drains |  |
| [**logsAppIdGet**](AllApi.md#logsAppIdGet) | **GET** /logs/{appId} |  |
| [**logsAppIdSseGet**](AllApi.md#logsAppIdSseGet) | **GET** /logs/{appId}/sse |  |
| [**logsDrainsDrainIdPut**](AllApi.md#logsDrainsDrainIdPut) | **PUT** /logs/drains/{drainId} |  |
| [**logsDrainsGet**](AllApi.md#logsDrainsGet) | **GET** /logs/drains |  |
| [**logsLogsChunkedAppIdGet**](AllApi.md#logsLogsChunkedAppIdGet) | **GET** /logs/logs-chunked/{appId} |  |
| [**logsLogsSocketAppIdGet**](AllApi.md#logsLogsSocketAppIdGet) | **GET** /logs/logs-socket/{appId} |  |
| [**logsSocketAppIdGet**](AllApi.md#logsSocketAppIdGet) | **GET** /logs-socket/{appId} |  |
| [**notificationsEmailhooksOwnerIdGet**](AllApi.md#notificationsEmailhooksOwnerIdGet) | **GET** /notifications/emailhooks/{ownerId} |  |
| [**notificationsEmailhooksOwnerIdIdDelete**](AllApi.md#notificationsEmailhooksOwnerIdIdDelete) | **DELETE** /notifications/emailhooks/{ownerId}/:id |  |
| [**notificationsEmailhooksOwnerIdIdPut**](AllApi.md#notificationsEmailhooksOwnerIdIdPut) | **PUT** /notifications/emailhooks/{ownerId}/:id |  |
| [**notificationsEmailhooksOwnerIdPost**](AllApi.md#notificationsEmailhooksOwnerIdPost) | **POST** /notifications/emailhooks/{ownerId} |  |
| [**notificationsInfoEventsGet**](AllApi.md#notificationsInfoEventsGet) | **GET** /notifications/info/events |  |
| [**notificationsInfoWebhookformatsGet**](AllApi.md#notificationsInfoWebhookformatsGet) | **GET** /notifications/info/webhookformats |  |
| [**notificationsWebhooksOwnerIdGet**](AllApi.md#notificationsWebhooksOwnerIdGet) | **GET** /notifications/webhooks/{ownerId} |  |
| [**notificationsWebhooksOwnerIdIdDelete**](AllApi.md#notificationsWebhooksOwnerIdIdDelete) | **DELETE** /notifications/webhooks/{ownerId}/:id |  |
| [**notificationsWebhooksOwnerIdIdPut**](AllApi.md#notificationsWebhooksOwnerIdIdPut) | **PUT** /notifications/webhooks/{ownerId}/:id |  |
| [**notificationsWebhooksOwnerIdPost**](AllApi.md#notificationsWebhooksOwnerIdPost) | **POST** /notifications/webhooks/{ownerId} |  |
| [**oauthAccessTokenQueryPost**](AllApi.md#oauthAccessTokenQueryPost) | **POST** /oauth/access_token_query |  |
| [**oauthRequestTokenQueryPost**](AllApi.md#oauthRequestTokenQueryPost) | **POST** /oauth/request_token_query |  |
| [**openapiGet**](AllApi.md#openapiGet) | **GET** //openapi |  |
| [**openapiTypeGet**](AllApi.md#openapiTypeGet) | **GET** /openapi.{type} | Get the swagger for this API as {type} |
| [**organisationsIdAddonprovidersProviderIdDelete**](AllApi.md#organisationsIdAddonprovidersProviderIdDelete) | **DELETE** /organisations/{id}/addonproviders/{providerId} | Remove an add-on provider |
| [**organisationsIdAddonsAddonIdInstancesGet**](AllApi.md#organisationsIdAddonsAddonIdInstancesGet) | **GET** /organisations/{id}/addons/{addonId}/instances | List instances for this add-on. |
| [**organisationsIdAddonsAddonIdInstancesInstanceIdGet**](AllApi.md#organisationsIdAddonsAddonIdInstancesInstanceIdGet) | **GET** /organisations/{id}/addons/{addonId}/instances/{instanceId} | Get a specific instance for {addonId} |
| [**organisationsIdAddonsAddonIdMigrationsGet**](AllApi.md#organisationsIdAddonsAddonIdMigrationsGet) | **GET** /organisations/{id}/addons/{addonId}/migrations | Get past migrations from add-on. |
| [**organisationsIdAddonsAddonIdMigrationsMigrationIdGet**](AllApi.md#organisationsIdAddonsAddonIdMigrationsMigrationIdGet) | **GET** /organisations/{id}/addons/{addonId}/migrations/{migrationId} | Get a given migration |
| [**organisationsIdAddonsAddonIdMigrationsPost**](AllApi.md#organisationsIdAddonsAddonIdMigrationsPost) | **POST** /organisations/{id}/addons/{addonId}/migrations | Start a new add-on migration |
| [**organisationsIdAddonsAddonIdSsoGet**](AllApi.md#organisationsIdAddonsAddonIdSsoGet) | **GET** /organisations/{id}/addons/{addonId}/sso |  |
| [**organisationsIdAddonsPreordersPost**](AllApi.md#organisationsIdAddonsPreordersPost) | **POST** /organisations/{id}/addons/preorders |  |
| [**organisationsIdApplicationsAppIdBranchPut**](AllApi.md#organisationsIdApplicationsAppIdBranchPut) | **PUT** /organisations/{id}/applications/{appId}/branch |  |
| [**organisationsIdApplicationsAppIdBranchesGet**](AllApi.md#organisationsIdApplicationsAppIdBranchesGet) | **GET** /organisations/{id}/applications/{appId}/branches |  |
| [**organisationsIdApplicationsAppIdBuildflavorPut**](AllApi.md#organisationsIdApplicationsAppIdBuildflavorPut) | **PUT** /organisations/{id}/applications/{appId}/buildflavor |  |
| [**organisationsIdApplicationsAppIdDependenciesEnvGet**](AllApi.md#organisationsIdApplicationsAppIdDependenciesEnvGet) | **GET** /organisations/{id}/applications/{appId}/dependencies/env |  |
| [**organisationsIdApplicationsAppIdDeploymentsDeploymentIdGet**](AllApi.md#organisationsIdApplicationsAppIdDeploymentsDeploymentIdGet) | **GET** /organisations/{id}/applications/{appId}/deployments/{deploymentId} |  |
| [**organisationsIdApplicationsAppIdExposedEnvGet**](AllApi.md#organisationsIdApplicationsAppIdExposedEnvGet) | **GET** /organisations/{id}/applications/{appId}/exposed_env |  |
| [**organisationsIdApplicationsAppIdExposedEnvPut**](AllApi.md#organisationsIdApplicationsAppIdExposedEnvPut) | **PUT** /organisations/{id}/applications/{appId}/exposed_env |  |
| [**organisationsIdApplicationsAppIdInstancesInstanceIdGet**](AllApi.md#organisationsIdApplicationsAppIdInstancesInstanceIdGet) | **GET** /organisations/{id}/applications/{appId}/instances/{instanceId} |  |
| [**organisationsIdPaymentsBillingsUnpaidGet**](AllApi.md#organisationsIdPaymentsBillingsUnpaidGet) | **GET** /organisations/{id}/payments/billings/unpaid |  |
| [**organisationsIdPaymentsMethodsDefaultGet**](AllApi.md#organisationsIdPaymentsMethodsDefaultGet) | **GET** /organisations/{id}/payments/methods/default |  |
| [**organisationsIdPaymentsMethodsDefaultPut**](AllApi.md#organisationsIdPaymentsMethodsDefaultPut) | **PUT** /organisations/{id}/payments/methods/default |  |
| [**organisationsIdPaymentsMethodsGet**](AllApi.md#organisationsIdPaymentsMethodsGet) | **GET** /organisations/{id}/payments/methods |  |
| [**organisationsIdPaymentsMethodsMIdDelete**](AllApi.md#organisationsIdPaymentsMethodsMIdDelete) | **DELETE** /organisations/{id}/payments/methods/{mId} |  |
| [**organisationsIdPaymentsMethodsPost**](AllApi.md#organisationsIdPaymentsMethodsPost) | **POST** /organisations/{id}/payments/methods |  |
| [**organisationsIdPaymentsMonthlyinvoiceGet**](AllApi.md#organisationsIdPaymentsMonthlyinvoiceGet) | **GET** /organisations/{id}/payments/monthlyinvoice |  |
| [**organisationsIdPaymentsMonthlyinvoiceMaxcreditPut**](AllApi.md#organisationsIdPaymentsMonthlyinvoiceMaxcreditPut) | **PUT** /organisations/{id}/payments/monthlyinvoice/maxcredit |  |
| [**organisationsIdPaymentsRecurringGet**](AllApi.md#organisationsIdPaymentsRecurringGet) | **GET** /organisations/{id}/payments/recurring |  |
| [**paymentsAssetsPayButtonTokenButtonPngGet**](AllApi.md#paymentsAssetsPayButtonTokenButtonPngGet) | **GET** /payments/assets/pay_button/{token}/button.png |  |
| [**paymentsBidEndStripePost**](AllApi.md#paymentsBidEndStripePost) | **POST** /payments/{bid}/end/stripe |  |
| [**postAuthorize**](AllApi.md#postAuthorize) | **POST** /authorize |  |
| [**postGithubRedeploy**](AllApi.md#postGithubRedeploy) | **POST** /github/redeploy |  |
| [**postGithubSignup**](AllApi.md#postGithubSignup) | **POST** /github/signup |  |
| [**postOauthAccessToken**](AllApi.md#postOauthAccessToken) | **POST** /oauth/access_token |  |
| [**postOauthAuthorize**](AllApi.md#postOauthAuthorize) | **POST** /oauth/authorize |  |
| [**postOauthRequestToken**](AllApi.md#postOauthRequestToken) | **POST** /oauth/request_token |  |
| [**postOrganisations**](AllApi.md#postOrganisations) | **POST** /organisations |  |
| [**postOrganisationsIdAddonproviders**](AllApi.md#postOrganisationsIdAddonproviders) | **POST** /organisations/{id}/addonproviders |  |
| [**postOrganisationsIdAddonprovidersProviderIdFeatures**](AllApi.md#postOrganisationsIdAddonprovidersProviderIdFeatures) | **POST** /organisations/{id}/addonproviders/{providerId}/features |  |
| [**postOrganisationsIdAddonprovidersProviderIdPlans**](AllApi.md#postOrganisationsIdAddonprovidersProviderIdPlans) | **POST** /organisations/{id}/addonproviders/{providerId}/plans |  |
| [**postOrganisationsIdAddonprovidersProviderIdTesters**](AllApi.md#postOrganisationsIdAddonprovidersProviderIdTesters) | **POST** /organisations/{id}/addonproviders/{providerId}/testers |  |
| [**postOrganisationsIdAddons**](AllApi.md#postOrganisationsIdAddons) | **POST** /organisations/{id}/addons |  |
| [**postOrganisationsIdApplications**](AllApi.md#postOrganisationsIdApplications) | **POST** /organisations/{id}/applications |  |
| [**postOrganisationsIdApplicationsAppIdAddons**](AllApi.md#postOrganisationsIdApplicationsAppIdAddons) | **POST** /organisations/{id}/applications/{appId}/addons |  |
| [**postOrganisationsIdApplicationsAppIdInstances**](AllApi.md#postOrganisationsIdApplicationsAppIdInstances) | **POST** /organisations/{id}/applications/{appId}/instances |  |
| [**postOrganisationsIdConsumers**](AllApi.md#postOrganisationsIdConsumers) | **POST** /organisations/{id}/consumers |  |
| [**postOrganisationsIdMembers**](AllApi.md#postOrganisationsIdMembers) | **POST** /organisations/{id}/members |  |
| [**postOrganisationsIdPaymentsBillings**](AllApi.md#postOrganisationsIdPaymentsBillings) | **POST** /organisations/{id}/payments/billings |  |
| [**postPasswordForgotten**](AllApi.md#postPasswordForgotten) | **POST** /password_forgotten |  |
| [**postPasswordForgottenKey**](AllApi.md#postPasswordForgottenKey) | **POST** /password_forgotten/{key} |  |
| [**postSelfAddons**](AllApi.md#postSelfAddons) | **POST** /self/addons |  |
| [**postSelfApplications**](AllApi.md#postSelfApplications) | **POST** /self/applications |  |
| [**postSelfApplicationsAppIdAddons**](AllApi.md#postSelfApplicationsAppIdAddons) | **POST** /self/applications/{appId}/addons |  |
| [**postSelfApplicationsAppIdInstances**](AllApi.md#postSelfApplicationsAppIdInstances) | **POST** /self/applications/{appId}/instances |  |
| [**postSelfConsumers**](AllApi.md#postSelfConsumers) | **POST** /self/consumers |  |
| [**postSelfPaymentsBillings**](AllApi.md#postSelfPaymentsBillings) | **POST** /self/payments/billings |  |
| [**postSelfPaymentsMethods**](AllApi.md#postSelfPaymentsMethods) | **POST** /self/payments/methods |  |
| [**postUsers**](AllApi.md#postUsers) | **POST** /users |  |
| [**postVendorBillingOwnerId**](AllApi.md#postVendorBillingOwnerId) | **POST** /vendor/apps/{addonId}/consumptions |  |
| [**productsAddonprovidersProviderIdVersionsGet**](AllApi.md#productsAddonprovidersProviderIdVersionsGet) | **GET** /products/addonproviders/{provider_id}/versions |  |
| [**productsMfaKindsGet**](AllApi.md#productsMfaKindsGet) | **GET** /products/mfa_kinds |  |
| [**putOrganisationsId**](AllApi.md#putOrganisationsId) | **PUT** /organisations/{id} |  |
| [**putOrganisationsIdAddonprovidersProviderId**](AllApi.md#putOrganisationsIdAddonprovidersProviderId) | **PUT** /organisations/{id}/addonproviders/{providerId} |  |
| [**putOrganisationsIdAddonprovidersProviderIdPlansPlanId**](AllApi.md#putOrganisationsIdAddonprovidersProviderIdPlansPlanId) | **PUT** /organisations/{id}/addonproviders/{providerId}/plans/{planId} |  |
| [**putOrganisationsIdAddonprovidersProviderIdPlansPlanIdFeaturesFeatureName**](AllApi.md#putOrganisationsIdAddonprovidersProviderIdPlansPlanIdFeaturesFeatureName) | **PUT** /organisations/{id}/addonproviders/{providerId}/plans/{planId}/features/{featureName} |  |
| [**putOrganisationsIdAddonsAddonId**](AllApi.md#putOrganisationsIdAddonsAddonId) | **PUT** /organisations/{id}/addons/{addonId} |  |
| [**putOrganisationsIdAddonsAddonIdTagsTag**](AllApi.md#putOrganisationsIdAddonsAddonIdTagsTag) | **PUT** /organisations/{id}/addons/{addonId}/tags/{tag} |  |
| [**putOrganisationsIdApplicationsAppId**](AllApi.md#putOrganisationsIdApplicationsAppId) | **PUT** /organisations/{id}/applications/{appId} |  |
| [**putOrganisationsIdApplicationsAppIdDependenciesDependencyId**](AllApi.md#putOrganisationsIdApplicationsAppIdDependenciesDependencyId) | **PUT** /organisations/{id}/applications/{appId}/dependencies/{dependencyId} |  |
| [**putOrganisationsIdApplicationsAppIdEnv**](AllApi.md#putOrganisationsIdApplicationsAppIdEnv) | **PUT** /organisations/{id}/applications/{appId}/env |  |
| [**putOrganisationsIdApplicationsAppIdEnvEnvName**](AllApi.md#putOrganisationsIdApplicationsAppIdEnvEnvName) | **PUT** /organisations/{id}/applications/{appId}/env/{envName} |  |
| [**putOrganisationsIdApplicationsAppIdTagsTag**](AllApi.md#putOrganisationsIdApplicationsAppIdTagsTag) | **PUT** /organisations/{id}/applications/{appId}/tags/{tag} |  |
| [**putOrganisationsIdApplicationsAppIdVhostsDomain**](AllApi.md#putOrganisationsIdApplicationsAppIdVhostsDomain) | **PUT** /organisations/{id}/applications/{appId}/vhosts/{domain} |  |
| [**putOrganisationsIdApplicationsAppIdVhostsFavourite**](AllApi.md#putOrganisationsIdApplicationsAppIdVhostsFavourite) | **PUT** /organisations/{id}/applications/{appId}/vhosts/favourite |  |
| [**putOrganisationsIdAvatar**](AllApi.md#putOrganisationsIdAvatar) | **PUT** /organisations/{id}/avatar |  |
| [**putOrganisationsIdConsumersKey**](AllApi.md#putOrganisationsIdConsumersKey) | **PUT** /organisations/{id}/consumers/{key} |  |
| [**putOrganisationsIdMembersUserId**](AllApi.md#putOrganisationsIdMembersUserId) | **PUT** /organisations/{id}/members/{userId} |  |
| [**putOrganisationsIdPaymentsBillingsBid**](AllApi.md#putOrganisationsIdPaymentsBillingsBid) | **PUT** /organisations/{id}/payments/billings/{bid} |  |
| [**putSelf**](AllApi.md#putSelf) | **PUT** /self |  |
| [**putSelfAddonsAddonId**](AllApi.md#putSelfAddonsAddonId) | **PUT** /self/addons/{addonId} |  |
| [**putSelfAddonsAddonIdPlan**](AllApi.md#putSelfAddonsAddonIdPlan) | **PUT** /self/addons/{addonId}/plan |  |
| [**putSelfAddonsAddonIdTagsTag**](AllApi.md#putSelfAddonsAddonIdTagsTag) | **PUT** /self/addons/{addonId}/tags/{tag} |  |
| [**putSelfApplicationsAppId**](AllApi.md#putSelfApplicationsAppId) | **PUT** /self/applications/{appId} |  |
| [**putSelfApplicationsAppIdEnv**](AllApi.md#putSelfApplicationsAppIdEnv) | **PUT** /self/applications/{appId}/env |  |
| [**putSelfApplicationsAppIdEnvEnvName**](AllApi.md#putSelfApplicationsAppIdEnvEnvName) | **PUT** /self/applications/{appId}/env/{envName} |  |
| [**putSelfApplicationsAppIdTagsTag**](AllApi.md#putSelfApplicationsAppIdTagsTag) | **PUT** /self/applications/{appId}/tags/{tag} |  |
| [**putSelfApplicationsAppIdVhostsDomain**](AllApi.md#putSelfApplicationsAppIdVhostsDomain) | **PUT** /self/applications/{appId}/vhosts/{domain} |  |
| [**putSelfApplicationsAppIdVhostsFavourite**](AllApi.md#putSelfApplicationsAppIdVhostsFavourite) | **PUT** /self/applications/{appId}/vhosts/favourite |  |
| [**putSelfAvatar**](AllApi.md#putSelfAvatar) | **PUT** /self/avatar |  |
| [**putSelfChangePassword**](AllApi.md#putSelfChangePassword) | **PUT** /self/change_password |  |
| [**putSelfConsumersKey**](AllApi.md#putSelfConsumersKey) | **PUT** /self/consumers/{key} |  |
| [**putSelfEmailsEmail**](AllApi.md#putSelfEmailsEmail) | **PUT** /self/emails/{email} |  |
| [**putSelfKeysKey**](AllApi.md#putSelfKeysKey) | **PUT** /self/keys/{key} |  |
| [**putSelfPaymentsBillingsBid**](AllApi.md#putSelfPaymentsBillingsBid) | **PUT** /self/payments/billings/{bid} |  |
| [**putVendorAppsAddonId**](AllApi.md#putVendorAppsAddonId) | **PUT** /vendor/apps/{addonId} |  |
| [**selfAddonsPreordersPost**](AllApi.md#selfAddonsPreordersPost) | **POST** /self/addons/preorders |  |
| [**selfApplicationsAppIdBranchPut**](AllApi.md#selfApplicationsAppIdBranchPut) | **PUT** /self/applications/{appId}/branch |  |
| [**selfApplicationsAppIdBranchesGet**](AllApi.md#selfApplicationsAppIdBranchesGet) | **GET** /self/applications/{appId}/branches |  |
| [**selfApplicationsAppIdBuildflavorPut**](AllApi.md#selfApplicationsAppIdBuildflavorPut) | **PUT** /self/applications/{appId}/buildflavor |  |
| [**selfApplicationsAppIdDependenciesEnvGet**](AllApi.md#selfApplicationsAppIdDependenciesEnvGet) | **GET** /self/applications/{appId}/dependencies/env |  |
| [**selfApplicationsAppIdDeploymentsDeploymentIdGet**](AllApi.md#selfApplicationsAppIdDeploymentsDeploymentIdGet) | **GET** /self/applications/{appId}/deployments/{deploymentId} |  |
| [**selfApplicationsAppIdExposedEnvGet**](AllApi.md#selfApplicationsAppIdExposedEnvGet) | **GET** /self/applications/{appId}/exposed_env |  |
| [**selfApplicationsAppIdExposedEnvPut**](AllApi.md#selfApplicationsAppIdExposedEnvPut) | **PUT** /self/applications/{appId}/exposed_env |  |
| [**selfApplicationsAppIdInstancesInstanceIdGet**](AllApi.md#selfApplicationsAppIdInstancesInstanceIdGet) | **GET** /self/applications/{appId}/instances/{instanceId} |  |
| [**selfCliTokensGet**](AllApi.md#selfCliTokensGet) | **GET** /self/cli_tokens |  |
| [**selfMfaKindBackupcodesGet**](AllApi.md#selfMfaKindBackupcodesGet) | **GET** /self/mfa/{kind}/backupcodes |  |
| [**selfMfaKindConfirmationPost**](AllApi.md#selfMfaKindConfirmationPost) | **POST** /self/mfa/{kind}/confirmation |  |
| [**selfMfaKindDelete**](AllApi.md#selfMfaKindDelete) | **DELETE** /self/mfa/{kind} |  |
| [**selfMfaKindPost**](AllApi.md#selfMfaKindPost) | **POST** /self/mfa/{kind} |  |
| [**selfMfaKindPut**](AllApi.md#selfMfaKindPut) | **PUT** /self/mfa/{kind} |  |
| [**selfPaymentsMethodsDefaultGet**](AllApi.md#selfPaymentsMethodsDefaultGet) | **GET** /self/payments/methods/default |  |
| [**selfPaymentsMethodsDefaultPut**](AllApi.md#selfPaymentsMethodsDefaultPut) | **PUT** /self/payments/methods/default |  |
| [**selfPaymentsMonthlyinvoiceGet**](AllApi.md#selfPaymentsMonthlyinvoiceGet) | **GET** /self/payments/monthlyinvoice |  |
| [**selfPaymentsMonthlyinvoiceMaxcreditPut**](AllApi.md#selfPaymentsMonthlyinvoiceMaxcreditPut) | **PUT** /self/payments/monthlyinvoice/maxcredit |  |
| [**selfPaymentsRecurringGet**](AllApi.md#selfPaymentsRecurringGet) | **GET** /self/payments/recurring |  |
| [**selfPaymentsTokensStripeGet**](AllApi.md#selfPaymentsTokensStripeGet) | **GET** /self/payments/tokens/stripe |  |
| [**updateConfigProviderEnv**](AllApi.md#updateConfigProviderEnv) | **PUT** /v4/addon-providers/config-provider/addons/{configurationProviderId}/env | Update provider&#39;s addon environment |
| [**v3LogsAppIdDrainsGet**](AllApi.md#v3LogsAppIdDrainsGet) | **GET** /v3/logs/{appId}/drains |  |
| [**v3LogsAppIdDrainsIdOrUrlDelete**](AllApi.md#v3LogsAppIdDrainsIdOrUrlDelete) | **DELETE** /v3/logs/{appId}/drains/:idOrUrl |  |
| [**v3LogsAppIdDrainsIdOrUrlGet**](AllApi.md#v3LogsAppIdDrainsIdOrUrlGet) | **GET** /v3/logs/{appId}/drains/:idOrUrl |  |
| [**v3LogsAppIdDrainsPost**](AllApi.md#v3LogsAppIdDrainsPost) | **POST** /v3/logs/{appId}/drains |  |
| [**v3LogsAppIdGet**](AllApi.md#v3LogsAppIdGet) | **GET** /v3/logs/{appId} |  |
| [**v3LogsAppIdLogsChunkedGet**](AllApi.md#v3LogsAppIdLogsChunkedGet) | **GET** /v3/logs/{appId}/logs-chunked |  |
| [**v3LogsAppIdLogsSocketGet**](AllApi.md#v3LogsAppIdLogsSocketGet) | **GET** /v3/logs/{appId}/logs-socket |  |
| [**vendorAddonsPost**](AllApi.md#vendorAddonsPost) | **POST** /vendor//addons |  |
| [**vendorAppsAddonIdLogscollectorGet**](AllApi.md#vendorAppsAddonIdLogscollectorGet) | **GET** /vendor//apps/{addonId}/logscollector |  |
| [**vendorAppsAddonIdMigrationCallbackPut**](AllApi.md#vendorAppsAddonIdMigrationCallbackPut) | **PUT** /vendor/apps/{addonId}/migration_callback |  |


<a id="applicationAppIdEnvironmentGet"></a>
# **applicationAppIdEnvironmentGet**
> applicationAppIdEnvironmentGet(appId, token)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String appId = "appId_example"; // String | 
    String token = "token_example"; // String | 
    try {
      apiInstance.applicationAppIdEnvironmentGet(appId, token);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#applicationAppIdEnvironmentGet");
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
| **200** | Status 200 |  -  |

<a id="applicationAppIdEnvironmentPut"></a>
# **applicationAppIdEnvironmentPut**
> applicationAppIdEnvironmentPut(appId, token)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String appId = "appId_example"; // String | 
    String token = "token_example"; // String | 
    try {
      apiInstance.applicationAppIdEnvironmentPut(appId, token);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#applicationAppIdEnvironmentPut");
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
| **200** | Status 200 |  -  |

<a id="createMatomo"></a>
# **createMatomo**
> Object createMatomo(body)

Create Matomo addon

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    Object body = null; // Object | 
    try {
      Object result = apiInstance.createMatomo(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#createMatomo");
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
| **body** | **Object**|  | [optional] |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | default response |  -  |

<a id="createNetworkGroup"></a>
# **createNetworkGroup**
> Object createNetworkGroup(ownerId, body)

Create Network Group

Creates a Network Group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String ownerId = "ownerId_example"; // String | Automatically added
    Object body = null; // Object | 
    try {
      Object result = apiInstance.createNetworkGroup(ownerId, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#createNetworkGroup");
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

<a id="createNetworkGroupExternalPeer"></a>
# **createNetworkGroupExternalPeer**
> Object createNetworkGroupExternalPeer(ownerId, networkGroupId, body)

Add external peer

Adds an external peer to a Network Group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String ownerId = "ownerId_example"; // String | Automatically added
    String networkGroupId = "networkGroupId_example"; // String | Automatically added
    Object body = null; // Object | 
    try {
      Object result = apiInstance.createNetworkGroupExternalPeer(ownerId, networkGroupId, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#createNetworkGroupExternalPeer");
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

<a id="createNetworkGroupMember"></a>
# **createNetworkGroupMember**
> createNetworkGroupMember(ownerId, networkGroupId, schema2)

Add member

Adds a member to a Network Group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String ownerId = "ownerId_example"; // String | Automatically added
    String networkGroupId = "networkGroupId_example"; // String | Automatically added
    Schema2 schema2 = new Schema2(); // Schema2 | 
    try {
      apiInstance.createNetworkGroupMember(ownerId, networkGroupId, schema2);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#createNetworkGroupMember");
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

<a id="deleteGithubLink"></a>
# **deleteGithubLink**
> deleteGithubLink()



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    try {
      apiInstance.deleteGithubLink();
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#deleteGithubLink");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
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

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | unlinkGithub |  -  |

<a id="deleteMatomo"></a>
# **deleteMatomo**
> Object deleteMatomo(matomoId, body)

Delete Matomo addon

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String matomoId = "matomoId_example"; // String | Automatically added
    String body = "body_example"; // String | 
    try {
      Object result = apiInstance.deleteMatomo(matomoId, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#deleteMatomo");
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
| **matomoId** | **String**| Automatically added | |
| **body** | **String**|  | [optional] |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | default response |  -  |

<a id="deleteNetworkGroup"></a>
# **deleteNetworkGroup**
> deleteNetworkGroup(ownerId, networkGroupId, body)

Delete Network Group

Deletes a Network Group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String ownerId = "ownerId_example"; // String | Automatically added
    String networkGroupId = "networkGroupId_example"; // String | Automatically added
    Object body = null; // Object | 
    try {
      apiInstance.deleteNetworkGroup(ownerId, networkGroupId, body);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#deleteNetworkGroup");
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

<a id="deleteNetworkGroupExternalPeer"></a>
# **deleteNetworkGroupExternalPeer**
> deleteNetworkGroupExternalPeer(ownerId, networkGroupId, peerId, body)

Remove external peer

Removes an external peer from a Network Group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String ownerId = "ownerId_example"; // String | Automatically added
    String networkGroupId = "networkGroupId_example"; // String | Automatically added
    String peerId = "peerId_example"; // String | Automatically added
    Object body = null; // Object | 
    try {
      apiInstance.deleteNetworkGroupExternalPeer(ownerId, networkGroupId, peerId, body);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#deleteNetworkGroupExternalPeer");
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

<a id="deleteNetworkGroupMember"></a>
# **deleteNetworkGroupMember**
> deleteNetworkGroupMember(ownerId, networkGroupId, memberId, body)

Remove member

Removes a member from a Network Group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String ownerId = "ownerId_example"; // String | Automatically added
    String networkGroupId = "networkGroupId_example"; // String | Automatically added
    String memberId = "memberId_example"; // String | Automatically added
    Object body = null; // Object | 
    try {
      apiInstance.deleteNetworkGroupMember(ownerId, networkGroupId, memberId, body);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#deleteNetworkGroupMember");
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

<a id="deleteNetworkGroupPeer"></a>
# **deleteNetworkGroupPeer**
> deleteNetworkGroupPeer(ownerId, networkGroupId, peerId, body)

Remove peer

Removes a peer from a Network Group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String ownerId = "ownerId_example"; // String | Automatically added
    String networkGroupId = "networkGroupId_example"; // String | Automatically added
    String peerId = "peerId_example"; // String | Automatically added
    Object body = null; // Object | 
    try {
      apiInstance.deleteNetworkGroupPeer(ownerId, networkGroupId, peerId, body);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#deleteNetworkGroupPeer");
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

<a id="deleteOrganisationsId"></a>
# **deleteOrganisationsId**
> deleteOrganisationsId(id)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String id = "id_example"; // String | 
    try {
      apiInstance.deleteOrganisationsId(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#deleteOrganisationsId");
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

<a id="deleteOrganisationsIdAddonprovidersProviderIdFeaturesFeatureId"></a>
# **deleteOrganisationsIdAddonprovidersProviderIdFeaturesFeatureId**
> deleteOrganisationsIdAddonprovidersProviderIdFeaturesFeatureId(id, featureId, providerId)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String id = "id_example"; // String | 
    String featureId = "featureId_example"; // String | 
    String providerId = "providerId_example"; // String | 
    try {
      apiInstance.deleteOrganisationsIdAddonprovidersProviderIdFeaturesFeatureId(id, featureId, providerId);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#deleteOrganisationsIdAddonprovidersProviderIdFeaturesFeatureId");
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

<a id="deleteOrganisationsIdAddonprovidersProviderIdPlansPlanId"></a>
# **deleteOrganisationsIdAddonprovidersProviderIdPlansPlanId**
> deleteOrganisationsIdAddonprovidersProviderIdPlansPlanId(id, providerId, planId)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String id = "id_example"; // String | 
    String providerId = "providerId_example"; // String | 
    String planId = "planId_example"; // String | 
    try {
      apiInstance.deleteOrganisationsIdAddonprovidersProviderIdPlansPlanId(id, providerId, planId);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#deleteOrganisationsIdAddonprovidersProviderIdPlansPlanId");
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

<a id="deleteOrganisationsIdAddonprovidersProviderIdPlansPlanIdFeaturesFeatureName"></a>
# **deleteOrganisationsIdAddonprovidersProviderIdPlansPlanIdFeaturesFeatureName**
> deleteOrganisationsIdAddonprovidersProviderIdPlansPlanIdFeaturesFeatureName(id, featureName, providerId, planId)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String id = "id_example"; // String | 
    String featureName = "featureName_example"; // String | 
    String providerId = "providerId_example"; // String | 
    String planId = "planId_example"; // String | 
    try {
      apiInstance.deleteOrganisationsIdAddonprovidersProviderIdPlansPlanIdFeaturesFeatureName(id, featureName, providerId, planId);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#deleteOrganisationsIdAddonprovidersProviderIdPlansPlanIdFeaturesFeatureName");
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

<a id="deleteOrganisationsIdAddonsAddonId"></a>
# **deleteOrganisationsIdAddonsAddonId**
> deleteOrganisationsIdAddonsAddonId(id, addonId)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String id = "id_example"; // String | 
    String addonId = "addonId_example"; // String | 
    try {
      apiInstance.deleteOrganisationsIdAddonsAddonId(id, addonId);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#deleteOrganisationsIdAddonsAddonId");
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

<a id="deleteOrganisationsIdAddonsAddonIdTagsTag"></a>
# **deleteOrganisationsIdAddonsAddonIdTagsTag**
> deleteOrganisationsIdAddonsAddonIdTagsTag(id, tag, addonId)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String id = "id_example"; // String | 
    String tag = "tag_example"; // String | 
    String addonId = "addonId_example"; // String | 
    try {
      apiInstance.deleteOrganisationsIdAddonsAddonIdTagsTag(id, tag, addonId);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#deleteOrganisationsIdAddonsAddonIdTagsTag");
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

<a id="deleteOrganisationsIdApplicationsAppId"></a>
# **deleteOrganisationsIdApplicationsAppId**
> deleteOrganisationsIdApplicationsAppId(id, appId)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String id = "id_example"; // String | 
    String appId = "appId_example"; // String | 
    try {
      apiInstance.deleteOrganisationsIdApplicationsAppId(id, appId);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#deleteOrganisationsIdApplicationsAppId");
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

<a id="deleteOrganisationsIdApplicationsAppIdAddonsAddonId"></a>
# **deleteOrganisationsIdApplicationsAppIdAddonsAddonId**
> deleteOrganisationsIdApplicationsAppIdAddonsAddonId(id, appId, addonId)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String id = "id_example"; // String | 
    String appId = "appId_example"; // String | 
    String addonId = "addonId_example"; // String | 
    try {
      apiInstance.deleteOrganisationsIdApplicationsAppIdAddonsAddonId(id, appId, addonId);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#deleteOrganisationsIdApplicationsAppIdAddonsAddonId");
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

<a id="deleteOrganisationsIdApplicationsAppIdDependenciesDependencyId"></a>
# **deleteOrganisationsIdApplicationsAppIdDependenciesDependencyId**
> deleteOrganisationsIdApplicationsAppIdDependenciesDependencyId(dependencyId, appId, id)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String dependencyId = "dependencyId_example"; // String | 
    String appId = "appId_example"; // String | 
    String id = "id_example"; // String | 
    try {
      apiInstance.deleteOrganisationsIdApplicationsAppIdDependenciesDependencyId(dependencyId, appId, id);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#deleteOrganisationsIdApplicationsAppIdDependenciesDependencyId");
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

<a id="deleteOrganisationsIdApplicationsAppIdDeploymentsDeploymentIdInstances"></a>
# **deleteOrganisationsIdApplicationsAppIdDeploymentsDeploymentIdInstances**
> deleteOrganisationsIdApplicationsAppIdDeploymentsDeploymentIdInstances(id, appId, deploymentId)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String id = "id_example"; // String | 
    String appId = "appId_example"; // String | 
    String deploymentId = "deploymentId_example"; // String | 
    try {
      apiInstance.deleteOrganisationsIdApplicationsAppIdDeploymentsDeploymentIdInstances(id, appId, deploymentId);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#deleteOrganisationsIdApplicationsAppIdDeploymentsDeploymentIdInstances");
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

<a id="deleteOrganisationsIdApplicationsAppIdEnvEnvName"></a>
# **deleteOrganisationsIdApplicationsAppIdEnvEnvName**
> deleteOrganisationsIdApplicationsAppIdEnvEnvName(id, appId, envName)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String id = "id_example"; // String | 
    String appId = "appId_example"; // String | 
    String envName = "envName_example"; // String | 
    try {
      apiInstance.deleteOrganisationsIdApplicationsAppIdEnvEnvName(id, appId, envName);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#deleteOrganisationsIdApplicationsAppIdEnvEnvName");
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

<a id="deleteOrganisationsIdApplicationsAppIdInstances"></a>
# **deleteOrganisationsIdApplicationsAppIdInstances**
> deleteOrganisationsIdApplicationsAppIdInstances(id, appId)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String id = "id_example"; // String | 
    String appId = "appId_example"; // String | 
    try {
      apiInstance.deleteOrganisationsIdApplicationsAppIdInstances(id, appId);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#deleteOrganisationsIdApplicationsAppIdInstances");
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

<a id="deleteOrganisationsIdApplicationsAppIdTagsTag"></a>
# **deleteOrganisationsIdApplicationsAppIdTagsTag**
> deleteOrganisationsIdApplicationsAppIdTagsTag(id, appId, tag)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String id = "id_example"; // String | 
    String appId = "appId_example"; // String | 
    String tag = "tag_example"; // String | 
    try {
      apiInstance.deleteOrganisationsIdApplicationsAppIdTagsTag(id, appId, tag);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#deleteOrganisationsIdApplicationsAppIdTagsTag");
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

<a id="deleteOrganisationsIdApplicationsAppIdVhostsDomain"></a>
# **deleteOrganisationsIdApplicationsAppIdVhostsDomain**
> deleteOrganisationsIdApplicationsAppIdVhostsDomain(id, appId, domain)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String id = "id_example"; // String | 
    String appId = "appId_example"; // String | 
    String domain = "domain_example"; // String | 
    try {
      apiInstance.deleteOrganisationsIdApplicationsAppIdVhostsDomain(id, appId, domain);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#deleteOrganisationsIdApplicationsAppIdVhostsDomain");
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

<a id="deleteOrganisationsIdApplicationsAppIdVhostsFavourite"></a>
# **deleteOrganisationsIdApplicationsAppIdVhostsFavourite**
> deleteOrganisationsIdApplicationsAppIdVhostsFavourite(id, appId)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String id = "id_example"; // String | 
    String appId = "appId_example"; // String | 
    try {
      apiInstance.deleteOrganisationsIdApplicationsAppIdVhostsFavourite(id, appId);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#deleteOrganisationsIdApplicationsAppIdVhostsFavourite");
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

<a id="deleteOrganisationsIdConsumersKey"></a>
# **deleteOrganisationsIdConsumersKey**
> deleteOrganisationsIdConsumersKey(id, key)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String id = "id_example"; // String | 
    String key = "key_example"; // String | 
    try {
      apiInstance.deleteOrganisationsIdConsumersKey(id, key);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#deleteOrganisationsIdConsumersKey");
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

<a id="deleteOrganisationsIdMembersUserId"></a>
# **deleteOrganisationsIdMembersUserId**
> deleteOrganisationsIdMembersUserId(id, userId)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String id = "id_example"; // String | 
    String userId = "userId_example"; // String | 
    try {
      apiInstance.deleteOrganisationsIdMembersUserId(id, userId);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#deleteOrganisationsIdMembersUserId");
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

<a id="deleteOrganisationsIdPaymentsBillingsBid"></a>
# **deleteOrganisationsIdPaymentsBillingsBid**
> deleteOrganisationsIdPaymentsBillingsBid(id, bid)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String id = "id_example"; // String | 
    String bid = "bid_example"; // String | 
    try {
      apiInstance.deleteOrganisationsIdPaymentsBillingsBid(id, bid);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#deleteOrganisationsIdPaymentsBillingsBid");
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

<a id="deleteOrganisationsIdPaymentsRecurring"></a>
# **deleteOrganisationsIdPaymentsRecurring**
> deleteOrganisationsIdPaymentsRecurring(id)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String id = "id_example"; // String | 
    try {
      apiInstance.deleteOrganisationsIdPaymentsRecurring(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#deleteOrganisationsIdPaymentsRecurring");
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

<a id="deleteSelf"></a>
# **deleteSelf**
> deleteSelf()



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    try {
      apiInstance.deleteSelf();
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#deleteSelf");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
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

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | deleteUser |  -  |

<a id="deleteSelfAddonsAddonId"></a>
# **deleteSelfAddonsAddonId**
> deleteSelfAddonsAddonId(addonId)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String addonId = "addonId_example"; // String | 
    try {
      apiInstance.deleteSelfAddonsAddonId(addonId);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#deleteSelfAddonsAddonId");
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

<a id="deleteSelfAddonsAddonIdTagsTag"></a>
# **deleteSelfAddonsAddonIdTagsTag**
> deleteSelfAddonsAddonIdTagsTag(tag, addonId)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String tag = "tag_example"; // String | 
    String addonId = "addonId_example"; // String | 
    try {
      apiInstance.deleteSelfAddonsAddonIdTagsTag(tag, addonId);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#deleteSelfAddonsAddonIdTagsTag");
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

<a id="deleteSelfApplicationsAppId"></a>
# **deleteSelfApplicationsAppId**
> deleteSelfApplicationsAppId(appId)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String appId = "appId_example"; // String | 
    try {
      apiInstance.deleteSelfApplicationsAppId(appId);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#deleteSelfApplicationsAppId");
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

<a id="deleteSelfApplicationsAppIdAddonsAddonId"></a>
# **deleteSelfApplicationsAppIdAddonsAddonId**
> deleteSelfApplicationsAppIdAddonsAddonId(appId, addonId)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String appId = "appId_example"; // String | 
    String addonId = "addonId_example"; // String | 
    try {
      apiInstance.deleteSelfApplicationsAppIdAddonsAddonId(appId, addonId);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#deleteSelfApplicationsAppIdAddonsAddonId");
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

<a id="deleteSelfApplicationsAppIdDependenciesDependencyId"></a>
# **deleteSelfApplicationsAppIdDependenciesDependencyId**
> deleteSelfApplicationsAppIdDependenciesDependencyId(dependencyId, appId)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String dependencyId = "dependencyId_example"; // String | 
    String appId = "appId_example"; // String | 
    try {
      apiInstance.deleteSelfApplicationsAppIdDependenciesDependencyId(dependencyId, appId);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#deleteSelfApplicationsAppIdDependenciesDependencyId");
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

<a id="deleteSelfApplicationsAppIdDeploymentsDeploymentIdInstances"></a>
# **deleteSelfApplicationsAppIdDeploymentsDeploymentIdInstances**
> deleteSelfApplicationsAppIdDeploymentsDeploymentIdInstances(appId, deploymentId)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String appId = "appId_example"; // String | 
    String deploymentId = "deploymentId_example"; // String | 
    try {
      apiInstance.deleteSelfApplicationsAppIdDeploymentsDeploymentIdInstances(appId, deploymentId);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#deleteSelfApplicationsAppIdDeploymentsDeploymentIdInstances");
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
| **200** | cancelDeploy |  -  |

<a id="deleteSelfApplicationsAppIdEnvEnvName"></a>
# **deleteSelfApplicationsAppIdEnvEnvName**
> deleteSelfApplicationsAppIdEnvEnvName(appId, envName)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String appId = "appId_example"; // String | 
    String envName = "envName_example"; // String | 
    try {
      apiInstance.deleteSelfApplicationsAppIdEnvEnvName(appId, envName);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#deleteSelfApplicationsAppIdEnvEnvName");
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

<a id="deleteSelfApplicationsAppIdInstances"></a>
# **deleteSelfApplicationsAppIdInstances**
> deleteSelfApplicationsAppIdInstances(appId)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String appId = "appId_example"; // String | 
    try {
      apiInstance.deleteSelfApplicationsAppIdInstances(appId);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#deleteSelfApplicationsAppIdInstances");
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

<a id="deleteSelfApplicationsAppIdTagsTag"></a>
# **deleteSelfApplicationsAppIdTagsTag**
> deleteSelfApplicationsAppIdTagsTag(appId, tag)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String appId = "appId_example"; // String | 
    String tag = "tag_example"; // String | 
    try {
      apiInstance.deleteSelfApplicationsAppIdTagsTag(appId, tag);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#deleteSelfApplicationsAppIdTagsTag");
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

<a id="deleteSelfApplicationsAppIdVhostsDomain"></a>
# **deleteSelfApplicationsAppIdVhostsDomain**
> deleteSelfApplicationsAppIdVhostsDomain(appId, domain)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String appId = "appId_example"; // String | 
    String domain = "domain_example"; // String | 
    try {
      apiInstance.deleteSelfApplicationsAppIdVhostsDomain(appId, domain);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#deleteSelfApplicationsAppIdVhostsDomain");
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

<a id="deleteSelfApplicationsAppIdVhostsFavourite"></a>
# **deleteSelfApplicationsAppIdVhostsFavourite**
> deleteSelfApplicationsAppIdVhostsFavourite(appId)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String appId = "appId_example"; // String | 
    try {
      apiInstance.deleteSelfApplicationsAppIdVhostsFavourite(appId);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#deleteSelfApplicationsAppIdVhostsFavourite");
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

<a id="deleteSelfConsumersKey"></a>
# **deleteSelfConsumersKey**
> deleteSelfConsumersKey(key)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String key = "key_example"; // String | 
    try {
      apiInstance.deleteSelfConsumersKey(key);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#deleteSelfConsumersKey");
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

<a id="deleteSelfEmailsEmail"></a>
# **deleteSelfEmailsEmail**
> deleteSelfEmailsEmail(email)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String email = "email_example"; // String | 
    try {
      apiInstance.deleteSelfEmailsEmail(email);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#deleteSelfEmailsEmail");
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
| **email** | **String**|  | |

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
| **200** | removeEmailAddress |  -  |

<a id="deleteSelfKeysKey"></a>
# **deleteSelfKeysKey**
> deleteSelfKeysKey(key)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String key = "key_example"; // String | 
    try {
      apiInstance.deleteSelfKeysKey(key);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#deleteSelfKeysKey");
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
| **200** | removeSshKey |  -  |

<a id="deleteSelfPaymentsBillingsBid"></a>
# **deleteSelfPaymentsBillingsBid**
> deleteSelfPaymentsBillingsBid(bid)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String bid = "bid_example"; // String | 
    try {
      apiInstance.deleteSelfPaymentsBillingsBid(bid);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#deleteSelfPaymentsBillingsBid");
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

<a id="deleteSelfPaymentsMethodsMId"></a>
# **deleteSelfPaymentsMethodsMId**
> deleteSelfPaymentsMethodsMId(mId)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String mId = "mId_example"; // String | 
    try {
      apiInstance.deleteSelfPaymentsMethodsMId(mId);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#deleteSelfPaymentsMethodsMId");
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
| **200** | deleteUserCard |  -  |

<a id="deleteSelfPaymentsRecurring"></a>
# **deleteSelfPaymentsRecurring**
> deleteSelfPaymentsRecurring()



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    try {
      apiInstance.deleteSelfPaymentsRecurring();
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#deleteSelfPaymentsRecurring");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
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

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | deleteRecurrentPayment |  -  |

<a id="deleteSelfTokens"></a>
# **deleteSelfTokens**
> deleteSelfTokens()



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    try {
      apiInstance.deleteSelfTokens();
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#deleteSelfTokens");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
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

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | revokeAllTokens |  -  |

<a id="deleteSelfTokensToken"></a>
# **deleteSelfTokensToken**
> deleteSelfTokensToken(token)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String token = "token_example"; // String | 
    try {
      apiInstance.deleteSelfTokensToken(token);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#deleteSelfTokensToken");
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
| **token** | **String**|  | |

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
| **200** | revokeToken |  -  |

<a id="eventsEventSocketGet"></a>
# **eventsEventSocketGet**
> eventsEventSocketGet()



Retrieve events as they come through a websocket connection. To have authorization, you have to send a &#x60;{ \&quot;message_type\&quot;: \&quot;oauth\&quot;, \&quot;authorization\&quot;: \&quot;oauth authorization string\&quot; }&#x60; message

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    try {
      apiInstance.eventsEventSocketGet();
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#eventsEventSocketGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
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

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | &lt;No description&gt; |  -  |

<a id="getConfigProvider"></a>
# **getConfigProvider**
> Object getConfigProvider(configurationProviderId, body)

Get Addon provider configuration

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String configurationProviderId = "configurationProviderId_example"; // String | Automatically added
    String body = "body_example"; // String | 
    try {
      Object result = apiInstance.getConfigProvider(configurationProviderId, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#getConfigProvider");
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
| **configurationProviderId** | **String**| Automatically added | |
| **body** | **String**|  | [optional] |

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
| **200** | requested config provider object |  -  |
| **401** |  |  -  |

<a id="getConfigProviderEnv"></a>
# **getConfigProviderEnv**
> List&lt;Object&gt; getConfigProviderEnv(configurationProviderId, body)

Get provider&#39;s addon environment

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String configurationProviderId = "configurationProviderId_example"; // String | Automatically added
    String body = "body_example"; // String | 
    try {
      List<Object> result = apiInstance.getConfigProviderEnv(configurationProviderId, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#getConfigProviderEnv");
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
| **configurationProviderId** | **String**| Automatically added | |
| **body** | **String**|  | [optional] |

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
| **200** | config provider environment variables |  -  |
| **401** |  |  -  |

<a id="getGithub"></a>
# **getGithub**
> TransactionId getGithub()



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    try {
      TransactionId result = apiInstance.getGithub();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#getGithub");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
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

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | startGithub |  -  |

<a id="getGithubApplications"></a>
# **getGithubApplications**
> List&lt;Application&gt; getGithubApplications()



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    try {
      List<Application> result = apiInstance.getGithubApplications();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#getGithubApplications");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

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
| **200** | getGithubApplications |  -  |

<a id="getGithubCallback"></a>
# **getGithubCallback**
> getGithubCallback(code, state, error, errorDescription, errorUri, cookie)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String code = "code_example"; // String | 
    String state = "state_example"; // String | 
    String error = "error_example"; // String | 
    String errorDescription = "errorDescription_example"; // String | 
    String errorUri = "errorUri_example"; // String | 
    String cookie = "cookie_example"; // String | 
    try {
      apiInstance.getGithubCallback(code, state, error, errorDescription, errorUri, cookie);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#getGithubCallback");
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
| **code** | **String**|  | [optional] |
| **state** | **String**|  | [optional] |
| **error** | **String**|  | [optional] |
| **errorDescription** | **String**|  | [optional] |
| **errorUri** | **String**|  | [optional] |
| **cookie** | **String**|  | [optional] |

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
| **200** | githubCallback |  -  |

<a id="getGithubEmails"></a>
# **getGithubEmails**
> List&lt;String&gt; getGithubEmails()



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    try {
      List<String> result = apiInstance.getGithubEmails();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#getGithubEmails");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

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
| **200** | getGithubEmails |  -  |

<a id="getGithubKeys"></a>
# **getGithubKeys**
> List&lt;Key&gt; getGithubKeys()



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    try {
      List<Key> result = apiInstance.getGithubKeys();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#getGithubKeys");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**List&lt;Key&gt;**](Key.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | getGithubKeys |  -  |

<a id="getGithubLink"></a>
# **getGithubLink**
> getGithubLink(transactionId, redirectUrl)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String transactionId = "transactionId_example"; // String | From GET /github
    String redirectUrl = "redirectUrl_example"; // String | 
    try {
      apiInstance.getGithubLink(transactionId, redirectUrl);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#getGithubLink");
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
| **transactionId** | **String**| From GET /github | [optional] |
| **redirectUrl** | **String**|  | [optional] |

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
| **200** | linkGithub |  -  |

<a id="getGithubLogin"></a>
# **getGithubLogin**
> getGithubLogin(redirectUrl, fromAuthorize)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String redirectUrl = "redirectUrl_example"; // String | 
    String fromAuthorize = "fromAuthorize_example"; // String | 
    try {
      apiInstance.getGithubLogin(redirectUrl, fromAuthorize);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#getGithubLogin");
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
| **redirectUrl** | **String**|  | [optional] |
| **fromAuthorize** | **String**|  | [optional] |

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
| **200** | githubLogin |  -  |

<a id="getGithubSignup"></a>
# **getGithubSignup**
> getGithubSignup(redirectUrl, fromAuthorize)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String redirectUrl = "redirectUrl_example"; // String | 
    String fromAuthorize = "fromAuthorize_example"; // String | 
    try {
      apiInstance.getGithubSignup(redirectUrl, fromAuthorize);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#getGithubSignup");
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
| **redirectUrl** | **String**|  | [optional] |
| **fromAuthorize** | **String**|  | [optional] |

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
| **200** | githubSignup |  -  |

<a id="getGithubUsername"></a>
# **getGithubUsername**
> String getGithubUsername()



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    try {
      String result = apiInstance.getGithubUsername();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#getGithubUsername");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
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

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | getGithubUsername |  -  |

<a id="getMatomo"></a>
# **getMatomo**
> Object getMatomo(matomoId, body)

Get Matomo addon

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String matomoId = "matomoId_example"; // String | Automatically added
    String body = "body_example"; // String | 
    try {
      Object result = apiInstance.getMatomo(matomoId, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#getMatomo");
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
| **matomoId** | **String**| Automatically added | |
| **body** | **String**|  | [optional] |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | default response |  -  |

<a id="getMatomoKTokenValidation"></a>
# **getMatomoKTokenValidation**
> Object getMatomoKTokenValidation(keycloakToken, body)

Validate a keycloak token

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String keycloakToken = "keycloakToken_example"; // String | Environment variable injected on the app with 'KEYCLOAK_TOKEN' name
    String body = "body_example"; // String | 
    try {
      Object result = apiInstance.getMatomoKTokenValidation(keycloakToken, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#getMatomoKTokenValidation");
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
| **keycloakToken** | **String**| Environment variable injected on the app with &#39;KEYCLOAK_TOKEN&#39; name | [optional] |
| **body** | **String**|  | [optional] |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | default response |  -  |

<a id="getNetworkGroup"></a>
# **getNetworkGroup**
> Object getNetworkGroup(ownerId, networkGroupId, body)

Get Network Group

Gets details of a Network Group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String ownerId = "ownerId_example"; // String | Automatically added
    String networkGroupId = "networkGroupId_example"; // String | Automatically added
    Object body = null; // Object | 
    try {
      Object result = apiInstance.getNetworkGroup(ownerId, networkGroupId, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#getNetworkGroup");
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

<a id="getNetworkGroupMember"></a>
# **getNetworkGroupMember**
> Schema1 getNetworkGroupMember(ownerId, networkGroupId, memberId, body)

Get member

Gets details of a Network Group member.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String ownerId = "ownerId_example"; // String | Automatically added
    String networkGroupId = "networkGroupId_example"; // String | Automatically added
    String memberId = "memberId_example"; // String | Automatically added
    Object body = null; // Object | 
    try {
      Schema1 result = apiInstance.getNetworkGroupMember(ownerId, networkGroupId, memberId, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#getNetworkGroupMember");
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

<a id="getNetworkGroupPeer"></a>
# **getNetworkGroupPeer**
> Object getNetworkGroupPeer(ownerId, networkGroupId, peerId, body)

Get peer

Gets details of a Network Group peer.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String ownerId = "ownerId_example"; // String | Automatically added
    String networkGroupId = "networkGroupId_example"; // String | Automatically added
    String peerId = "peerId_example"; // String | Automatically added
    Object body = null; // Object | 
    try {
      Object result = apiInstance.getNetworkGroupPeer(ownerId, networkGroupId, peerId, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#getNetworkGroupPeer");
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

<a id="getNetworkGroupStream"></a>
# **getNetworkGroupStream**
> Object getNetworkGroupStream(ownerId, networkGroupId, body)

Network Group SSE

Retrieves the current Network Group details as a Server Sent Event.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String ownerId = "ownerId_example"; // String | Automatically added
    String networkGroupId = "networkGroupId_example"; // String | Automatically added
    Object body = null; // Object | 
    try {
      Object result = apiInstance.getNetworkGroupStream(ownerId, networkGroupId, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#getNetworkGroupStream");
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

<a id="getNetworkGroupWireGuardConfiguration"></a>
# **getNetworkGroupWireGuardConfiguration**
> Object getNetworkGroupWireGuardConfiguration(ownerId, networkGroupId, peerId, body)

Get WireGuard® configuration

Gets the current WireGuard® tunnel configuration file for a Network Group peer.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String ownerId = "ownerId_example"; // String | Automatically added
    String networkGroupId = "networkGroupId_example"; // String | Automatically added
    String peerId = "peerId_example"; // String | Automatically added
    Object body = null; // Object | 
    try {
      Object result = apiInstance.getNetworkGroupWireGuardConfiguration(ownerId, networkGroupId, peerId, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#getNetworkGroupWireGuardConfiguration");
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

<a id="getNetworkGroupWireGuardConfigurationStream"></a>
# **getNetworkGroupWireGuardConfigurationStream**
> Object getNetworkGroupWireGuardConfigurationStream(ownerId, networkGroupId, peerId, body)

Get WireGuard® configuration

Gets the current WireGuard® tunnel configuration file for a Network Group peer as a Server Sent Event.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String ownerId = "ownerId_example"; // String | Automatically added
    String networkGroupId = "networkGroupId_example"; // String | Automatically added
    String peerId = "peerId_example"; // String | Automatically added
    Object body = null; // Object | 
    try {
      Object result = apiInstance.getNetworkGroupWireGuardConfigurationStream(ownerId, networkGroupId, peerId, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#getNetworkGroupWireGuardConfigurationStream");
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

<a id="getNewsfeedEngineering"></a>
# **getNewsfeedEngineering**
> getNewsfeedEngineering()



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    try {
      apiInstance.getNewsfeedEngineering();
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#getNewsfeedEngineering");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
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

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | getEngineeringFeed |  -  |

<a id="getNewsfeedsBlog"></a>
# **getNewsfeedsBlog**
> getNewsfeedsBlog()



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    try {
      apiInstance.getNewsfeedsBlog();
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#getNewsfeedsBlog");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
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

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | getBlogFeed |  -  |

<a id="getOauthAuthorize"></a>
# **getOauthAuthorize**
> getOauthAuthorize(oauthToken, cookie)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String oauthToken = "oauthToken_example"; // String | 
    String cookie = "cookie_example"; // String | 
    try {
      apiInstance.getOauthAuthorize(oauthToken, cookie);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#getOauthAuthorize");
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
| **oauthToken** | **String**|  | [optional] |
| **cookie** | **String**|  | [optional] |

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
| **200** | authorizeForm |  -  |

<a id="getOauthRights"></a>
# **getOauthRights**
> Rights getOauthRights()



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    try {
      Rights result = apiInstance.getOauthRights();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#getOauthRights");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
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

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | getAvailableRights |  -  |

<a id="getOrganisations"></a>
# **getOrganisations**
> List&lt;Organisation&gt; getOrganisations(user)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String user = "user_example"; // String | 
    try {
      List<Organisation> result = apiInstance.getOrganisations(user);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#getOrganisations");
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

<a id="getOrganisationsId"></a>
# **getOrganisationsId**
> Organisation getOrganisationsId(id)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String id = "id_example"; // String | 
    try {
      Organisation result = apiInstance.getOrganisationsId(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#getOrganisationsId");
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

<a id="getOrganisationsIdAddonproviders"></a>
# **getOrganisationsIdAddonproviders**
> List&lt;Provider&gt; getOrganisationsIdAddonproviders(id)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String id = "id_example"; // String | 
    try {
      List<Provider> result = apiInstance.getOrganisationsIdAddonproviders(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#getOrganisationsIdAddonproviders");
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

<a id="getOrganisationsIdAddonprovidersProviderId"></a>
# **getOrganisationsIdAddonprovidersProviderId**
> Provider getOrganisationsIdAddonprovidersProviderId(id, providerId)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String id = "id_example"; // String | 
    String providerId = "providerId_example"; // String | 
    try {
      Provider result = apiInstance.getOrganisationsIdAddonprovidersProviderId(id, providerId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#getOrganisationsIdAddonprovidersProviderId");
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

<a id="getOrganisationsIdAddonprovidersProviderIdFeatures"></a>
# **getOrganisationsIdAddonprovidersProviderIdFeatures**
> List&lt;Feature&gt; getOrganisationsIdAddonprovidersProviderIdFeatures(id, providerId)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String id = "id_example"; // String | 
    String providerId = "providerId_example"; // String | 
    try {
      List<Feature> result = apiInstance.getOrganisationsIdAddonprovidersProviderIdFeatures(id, providerId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#getOrganisationsIdAddonprovidersProviderIdFeatures");
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

<a id="getOrganisationsIdAddonprovidersProviderIdPlans"></a>
# **getOrganisationsIdAddonprovidersProviderIdPlans**
> List&lt;Plan&gt; getOrganisationsIdAddonprovidersProviderIdPlans(id, providerId)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String id = "id_example"; // String | 
    String providerId = "providerId_example"; // String | 
    try {
      List<Plan> result = apiInstance.getOrganisationsIdAddonprovidersProviderIdPlans(id, providerId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#getOrganisationsIdAddonprovidersProviderIdPlans");
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

<a id="getOrganisationsIdAddonprovidersProviderIdPlansPlanId"></a>
# **getOrganisationsIdAddonprovidersProviderIdPlansPlanId**
> Plan getOrganisationsIdAddonprovidersProviderIdPlansPlanId(id, providerId, planId)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String id = "id_example"; // String | 
    String providerId = "providerId_example"; // String | 
    String planId = "planId_example"; // String | 
    try {
      Plan result = apiInstance.getOrganisationsIdAddonprovidersProviderIdPlansPlanId(id, providerId, planId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#getOrganisationsIdAddonprovidersProviderIdPlansPlanId");
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

<a id="getOrganisationsIdAddonprovidersProviderIdTags"></a>
# **getOrganisationsIdAddonprovidersProviderIdTags**
> List&lt;String&gt; getOrganisationsIdAddonprovidersProviderIdTags(id, providerId)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String id = "id_example"; // String | 
    String providerId = "providerId_example"; // String | 
    try {
      List<String> result = apiInstance.getOrganisationsIdAddonprovidersProviderIdTags(id, providerId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#getOrganisationsIdAddonprovidersProviderIdTags");
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

<a id="getOrganisationsIdAddons"></a>
# **getOrganisationsIdAddons**
> List&lt;Addon&gt; getOrganisationsIdAddons(id)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String id = "id_example"; // String | 
    try {
      List<Addon> result = apiInstance.getOrganisationsIdAddons(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#getOrganisationsIdAddons");
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

<a id="getOrganisationsIdAddonsAddonId"></a>
# **getOrganisationsIdAddonsAddonId**
> Addon getOrganisationsIdAddonsAddonId(id, addonId)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String id = "id_example"; // String | 
    String addonId = "addonId_example"; // String | 
    try {
      Addon result = apiInstance.getOrganisationsIdAddonsAddonId(id, addonId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#getOrganisationsIdAddonsAddonId");
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

<a id="getOrganisationsIdAddonsAddonIdApplications"></a>
# **getOrganisationsIdAddonsAddonIdApplications**
> List&lt;Application&gt; getOrganisationsIdAddonsAddonIdApplications(id, addonId)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String id = "id_example"; // String | 
    String addonId = "addonId_example"; // String | 
    try {
      List<Application> result = apiInstance.getOrganisationsIdAddonsAddonIdApplications(id, addonId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#getOrganisationsIdAddonsAddonIdApplications");
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

<a id="getOrganisationsIdAddonsAddonIdEnv"></a>
# **getOrganisationsIdAddonsAddonIdEnv**
> List&lt;ListEnv&gt; getOrganisationsIdAddonsAddonIdEnv(id, addonId)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String id = "id_example"; // String | 
    String addonId = "addonId_example"; // String | 
    try {
      List<ListEnv> result = apiInstance.getOrganisationsIdAddonsAddonIdEnv(id, addonId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#getOrganisationsIdAddonsAddonIdEnv");
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

<a id="getOrganisationsIdAddonsAddonIdSso"></a>
# **getOrganisationsIdAddonsAddonIdSso**
> AddonProviderSso getOrganisationsIdAddonsAddonIdSso(providerId, id)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String providerId = "providerId_example"; // String | 
    String id = "id_example"; // String | 
    try {
      AddonProviderSso result = apiInstance.getOrganisationsIdAddonsAddonIdSso(providerId, id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#getOrganisationsIdAddonsAddonIdSso");
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

<a id="getOrganisationsIdAddonsAddonIdTags"></a>
# **getOrganisationsIdAddonsAddonIdTags**
> List&lt;String&gt; getOrganisationsIdAddonsAddonIdTags(id, addonId)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String id = "id_example"; // String | 
    String addonId = "addonId_example"; // String | 
    try {
      List<String> result = apiInstance.getOrganisationsIdAddonsAddonIdTags(id, addonId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#getOrganisationsIdAddonsAddonIdTags");
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

<a id="getOrganisationsIdApplications"></a>
# **getOrganisationsIdApplications**
> List&lt;Application&gt; getOrganisationsIdApplications(id)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String id = "id_example"; // String | 
    try {
      List<Application> result = apiInstance.getOrganisationsIdApplications(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#getOrganisationsIdApplications");
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

<a id="getOrganisationsIdApplicationsAppId"></a>
# **getOrganisationsIdApplicationsAppId**
> Application getOrganisationsIdApplicationsAppId(id, appId)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String id = "id_example"; // String | 
    String appId = "appId_example"; // String | 
    try {
      Application result = apiInstance.getOrganisationsIdApplicationsAppId(id, appId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#getOrganisationsIdApplicationsAppId");
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

<a id="getOrganisationsIdApplicationsAppIdAddons"></a>
# **getOrganisationsIdApplicationsAppIdAddons**
> List&lt;Addon&gt; getOrganisationsIdApplicationsAppIdAddons(id, appId)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String id = "id_example"; // String | 
    String appId = "appId_example"; // String | 
    try {
      List<Addon> result = apiInstance.getOrganisationsIdApplicationsAppIdAddons(id, appId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#getOrganisationsIdApplicationsAppIdAddons");
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

<a id="getOrganisationsIdApplicationsAppIdAddonsEnv"></a>
# **getOrganisationsIdApplicationsAppIdAddonsEnv**
> List&lt;Env&gt; getOrganisationsIdApplicationsAppIdAddonsEnv(id, appId)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String id = "id_example"; // String | 
    String appId = "appId_example"; // String | 
    try {
      List<Env> result = apiInstance.getOrganisationsIdApplicationsAppIdAddonsEnv(id, appId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#getOrganisationsIdApplicationsAppIdAddonsEnv");
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

<a id="getOrganisationsIdApplicationsAppIdDependencies"></a>
# **getOrganisationsIdApplicationsAppIdDependencies**
> List&lt;Application&gt; getOrganisationsIdApplicationsAppIdDependencies(appId, id)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String appId = "appId_example"; // String | 
    String id = "id_example"; // String | 
    try {
      List<Application> result = apiInstance.getOrganisationsIdApplicationsAppIdDependencies(appId, id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#getOrganisationsIdApplicationsAppIdDependencies");
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

<a id="getOrganisationsIdApplicationsAppIdDependents"></a>
# **getOrganisationsIdApplicationsAppIdDependents**
> List&lt;Application&gt; getOrganisationsIdApplicationsAppIdDependents(appId, id)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String appId = "appId_example"; // String | 
    String id = "id_example"; // String | 
    try {
      List<Application> result = apiInstance.getOrganisationsIdApplicationsAppIdDependents(appId, id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#getOrganisationsIdApplicationsAppIdDependents");
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

<a id="getOrganisationsIdApplicationsAppIdDeployments"></a>
# **getOrganisationsIdApplicationsAppIdDeployments**
> List&lt;Deployment&gt; getOrganisationsIdApplicationsAppIdDeployments(id, appId, limit, offset, action)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String id = "id_example"; // String | 
    String appId = "appId_example"; // String | 
    String limit = "limit_example"; // String | 
    String offset = "offset_example"; // String | 
    String action = "action_example"; // String | 
    try {
      List<Deployment> result = apiInstance.getOrganisationsIdApplicationsAppIdDeployments(id, appId, limit, offset, action);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#getOrganisationsIdApplicationsAppIdDeployments");
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

<a id="getOrganisationsIdApplicationsAppIdEnv"></a>
# **getOrganisationsIdApplicationsAppIdEnv**
> List&lt;ListEnv&gt; getOrganisationsIdApplicationsAppIdEnv(id, appId)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String id = "id_example"; // String | 
    String appId = "appId_example"; // String | 
    try {
      List<ListEnv> result = apiInstance.getOrganisationsIdApplicationsAppIdEnv(id, appId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#getOrganisationsIdApplicationsAppIdEnv");
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

<a id="getOrganisationsIdApplicationsAppIdInstances"></a>
# **getOrganisationsIdApplicationsAppIdInstances**
> List&lt;AppInstance&gt; getOrganisationsIdApplicationsAppIdInstances(id, appId)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String id = "id_example"; // String | 
    String appId = "appId_example"; // String | 
    try {
      List<AppInstance> result = apiInstance.getOrganisationsIdApplicationsAppIdInstances(id, appId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#getOrganisationsIdApplicationsAppIdInstances");
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

<a id="getOrganisationsIdApplicationsAppIdTags"></a>
# **getOrganisationsIdApplicationsAppIdTags**
> List&lt;String&gt; getOrganisationsIdApplicationsAppIdTags(id, appId)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String id = "id_example"; // String | 
    String appId = "appId_example"; // String | 
    try {
      List<String> result = apiInstance.getOrganisationsIdApplicationsAppIdTags(id, appId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#getOrganisationsIdApplicationsAppIdTags");
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

<a id="getOrganisationsIdApplicationsAppIdVhosts"></a>
# **getOrganisationsIdApplicationsAppIdVhosts**
> List&lt;Vhost&gt; getOrganisationsIdApplicationsAppIdVhosts(id, appId)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String id = "id_example"; // String | 
    String appId = "appId_example"; // String | 
    try {
      List<Vhost> result = apiInstance.getOrganisationsIdApplicationsAppIdVhosts(id, appId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#getOrganisationsIdApplicationsAppIdVhosts");
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

<a id="getOrganisationsIdApplicationsAppIdVhostsFavourite"></a>
# **getOrganisationsIdApplicationsAppIdVhostsFavourite**
> Vhost getOrganisationsIdApplicationsAppIdVhostsFavourite(id, appId)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String id = "id_example"; // String | 
    String appId = "appId_example"; // String | 
    try {
      Vhost result = apiInstance.getOrganisationsIdApplicationsAppIdVhostsFavourite(id, appId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#getOrganisationsIdApplicationsAppIdVhostsFavourite");
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

<a id="getOrganisationsIdConsumers"></a>
# **getOrganisationsIdConsumers**
> List&lt;Consumer&gt; getOrganisationsIdConsumers(id)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String id = "id_example"; // String | 
    try {
      List<Consumer> result = apiInstance.getOrganisationsIdConsumers(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#getOrganisationsIdConsumers");
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

<a id="getOrganisationsIdConsumersKey"></a>
# **getOrganisationsIdConsumersKey**
> Consumer getOrganisationsIdConsumersKey(id, key)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String id = "id_example"; // String | 
    String key = "key_example"; // String | 
    try {
      Consumer result = apiInstance.getOrganisationsIdConsumersKey(id, key);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#getOrganisationsIdConsumersKey");
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

<a id="getOrganisationsIdConsumersKeySecret"></a>
# **getOrganisationsIdConsumersKeySecret**
> Secret getOrganisationsIdConsumersKeySecret(id, key)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String id = "id_example"; // String | 
    String key = "key_example"; // String | 
    try {
      Secret result = apiInstance.getOrganisationsIdConsumersKeySecret(id, key);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#getOrganisationsIdConsumersKeySecret");
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

<a id="getOrganisationsIdConsumptions"></a>
# **getOrganisationsIdConsumptions**
> Conso getOrganisationsIdConsumptions(id, appId, from, to)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String id = "id_example"; // String | 
    String appId = "appId_example"; // String | 
    String from = "from_example"; // String | 
    String to = "to_example"; // String | 
    try {
      Conso result = apiInstance.getOrganisationsIdConsumptions(id, appId, from, to);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#getOrganisationsIdConsumptions");
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

<a id="getOrganisationsIdCredits"></a>
# **getOrganisationsIdCredits**
> Credits getOrganisationsIdCredits(id)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String id = "id_example"; // String | 
    try {
      Credits result = apiInstance.getOrganisationsIdCredits(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#getOrganisationsIdCredits");
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

<a id="getOrganisationsIdDeployments"></a>
# **getOrganisationsIdDeployments**
> DeploymentSummary getOrganisationsIdDeployments(id)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String id = "id_example"; // String | 
    try {
      DeploymentSummary result = apiInstance.getOrganisationsIdDeployments(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#getOrganisationsIdDeployments");
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

<a id="getOrganisationsIdInstances"></a>
# **getOrganisationsIdInstances**
> Object getOrganisationsIdInstances(id)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String id = "id_example"; // String | 
    try {
      Object result = apiInstance.getOrganisationsIdInstances(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#getOrganisationsIdInstances");
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

<a id="getOrganisationsIdMembers"></a>
# **getOrganisationsIdMembers**
> List&lt;Schema1&gt; getOrganisationsIdMembers(id)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String id = "id_example"; // String | 
    try {
      List<Schema1> result = apiInstance.getOrganisationsIdMembers(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#getOrganisationsIdMembers");
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

<a id="getOrganisationsIdPaymentInfo"></a>
# **getOrganisationsIdPaymentInfo**
> getOrganisationsIdPaymentInfo(id)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String id = "id_example"; // String | 
    try {
      apiInstance.getOrganisationsIdPaymentInfo(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#getOrganisationsIdPaymentInfo");
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

<a id="getOrganisationsIdPaymentsBillings"></a>
# **getOrganisationsIdPaymentsBillings**
> getOrganisationsIdPaymentsBillings(id)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String id = "id_example"; // String | 
    try {
      apiInstance.getOrganisationsIdPaymentsBillings(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#getOrganisationsIdPaymentsBillings");
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

<a id="getOrganisationsIdPaymentsBillingsBid"></a>
# **getOrganisationsIdPaymentsBillingsBid**
> getOrganisationsIdPaymentsBillingsBid(id, bid)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String id = "id_example"; // String | 
    String bid = "bid_example"; // String | 
    try {
      apiInstance.getOrganisationsIdPaymentsBillingsBid(id, bid);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#getOrganisationsIdPaymentsBillingsBid");
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

<a id="getOrganisationsIdPaymentsBillingsBidPdf"></a>
# **getOrganisationsIdPaymentsBillingsBidPdf**
> getOrganisationsIdPaymentsBillingsBidPdf(id, bid, token)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String id = "id_example"; // String | 
    String bid = "bid_example"; // String | 
    String token = "token_example"; // String | 
    try {
      apiInstance.getOrganisationsIdPaymentsBillingsBidPdf(id, bid, token);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#getOrganisationsIdPaymentsBillingsBidPdf");
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

<a id="getOrganisationsIdPaymentsFullPricePrice"></a>
# **getOrganisationsIdPaymentsFullPricePrice**
> getOrganisationsIdPaymentsFullPricePrice(id, price)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String id = "id_example"; // String | 
    String price = "price_example"; // String | 
    try {
      apiInstance.getOrganisationsIdPaymentsFullPricePrice(id, price);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#getOrganisationsIdPaymentsFullPricePrice");
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

<a id="getPasswordForgotten"></a>
# **getPasswordForgotten**
> getPasswordForgotten()



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    try {
      apiInstance.getPasswordForgotten();
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#getPasswordForgotten");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
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

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | getPasswordForgottenForm |  -  |

<a id="getPasswordForgottenKey"></a>
# **getPasswordForgottenKey**
> getPasswordForgottenKey(key)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String key = "key_example"; // String | 
    try {
      apiInstance.getPasswordForgottenKey(key);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#getPasswordForgottenKey");
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
| **200** | confirmPasswordResetRequest |  -  |

<a id="getPaymentsCouponsName"></a>
# **getPaymentsCouponsName**
> getPaymentsCouponsName(name)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String name = "name_example"; // String | 
    try {
      apiInstance.getPaymentsCouponsName(name);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#getPaymentsCouponsName");
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
| **name** | **String**|  | |

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
| **200** | getCoupon |  -  |

<a id="getPaymentsProviders"></a>
# **getPaymentsProviders**
> List&lt;PaymentProvider&gt; getPaymentsProviders()



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    try {
      List<PaymentProvider> result = apiInstance.getPaymentsProviders();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#getPaymentsProviders");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**List&lt;PaymentProvider&gt;**](PaymentProvider.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | getAvailablePaymentProviders |  -  |

<a id="getPaymentsTokensStripe"></a>
# **getPaymentsTokensStripe**
> getPaymentsTokensStripe()



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    try {
      apiInstance.getPaymentsTokensStripe();
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#getPaymentsTokensStripe");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
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

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | getStripeToken |  -  |

<a id="getProductsAddonProviders"></a>
# **getProductsAddonProviders**
> List&lt;Provider&gt; getProductsAddonProviders()



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    try {
      List<Provider> result = apiInstance.getProductsAddonProviders();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#getProductsAddonProviders");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

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
| **200** | getAddonProviders |  -  |

<a id="getProductsAddonProvidersProviderId"></a>
# **getProductsAddonProvidersProviderId**
> Provider getProductsAddonProvidersProviderId(providerId)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String providerId = "providerId_example"; // String | 
    try {
      Provider result = apiInstance.getProductsAddonProvidersProviderId(providerId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#getProductsAddonProvidersProviderId");
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
| **200** | getAddonProvider |  -  |

<a id="getProductsCountries"></a>
# **getProductsCountries**
> Country getProductsCountries()



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    try {
      Country result = apiInstance.getProductsCountries();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#getProductsCountries");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
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

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | getCountries |  -  |

<a id="getProductsCountrycodes"></a>
# **getProductsCountrycodes**
> Country getProductsCountrycodes()



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    try {
      Country result = apiInstance.getProductsCountrycodes();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#getProductsCountrycodes");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
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

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | getCountryCodes |  -  |

<a id="getProductsInstances"></a>
# **getProductsInstances**
> List&lt;Instance&gt; getProductsInstances(_for)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String _for = "_for_example"; // String | 
    try {
      List<Instance> result = apiInstance.getProductsInstances(_for);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#getProductsInstances");
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
| **_for** | **String**|  | [optional] |

### Return type

[**List&lt;Instance&gt;**](Instance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | getAvailableInstances |  -  |

<a id="getProductsInstancesTypeVersion"></a>
# **getProductsInstancesTypeVersion**
> Instance getProductsInstancesTypeVersion(type, version, _for, app)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String type = "type_example"; // String | 
    String version = "version_example"; // String | 
    String _for = "_for_example"; // String | 
    String app = "app_example"; // String | 
    try {
      Instance result = apiInstance.getProductsInstancesTypeVersion(type, version, _for, app);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#getProductsInstancesTypeVersion");
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
| **type** | **String**|  | |
| **version** | **String**|  | |
| **_for** | **String**|  | [optional] |
| **app** | **String**|  | [optional] |

### Return type

[**Instance**](Instance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | getAvailableInstance |  -  |

<a id="getProductsPackages"></a>
# **getProductsPackages**
> getProductsPackages(coupon, orgaId, currency)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String coupon = "coupon_example"; // String | 
    String orgaId = "orgaId_example"; // String | 
    String currency = "currency_example"; // String | 
    try {
      apiInstance.getProductsPackages(coupon, orgaId, currency);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#getProductsPackages");
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
| **coupon** | **String**|  | [optional] |
| **orgaId** | **String**|  | [optional] |
| **currency** | **String**|  | [optional] |

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
| **200** | getAvailablePackages |  -  |

<a id="getProductsPrices"></a>
# **getProductsPrices**
> getProductsPrices()



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    try {
      apiInstance.getProductsPrices();
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#getProductsPrices");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
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

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | getExchangeRates |  -  |

<a id="getProductsZones"></a>
# **getProductsZones**
> List&lt;Zone&gt; getProductsZones()



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    try {
      List<Zone> result = apiInstance.getProductsZones();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#getProductsZones");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**List&lt;Zone&gt;**](Zone.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | getZones |  -  |

<a id="getSelf"></a>
# **getSelf**
> User getSelf()



Get information about yourself

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    try {
      User result = apiInstance.getSelf();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#getSelf");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
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

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | getUser |  -  |

<a id="getSelfAddons"></a>
# **getSelfAddons**
> List&lt;Addon&gt; getSelfAddons()

Addon

Get all the addons

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    try {
      List<Addon> result = apiInstance.getSelfAddons();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#getSelfAddons");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

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

<a id="getSelfAddonsAddonId"></a>
# **getSelfAddonsAddonId**
> Addon getSelfAddonsAddonId(addonId)

Specific addon

Get a specific addon

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String addonId = "addonId_example"; // String | 
    try {
      Addon result = apiInstance.getSelfAddonsAddonId(addonId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#getSelfAddonsAddonId");
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

<a id="getSelfAddonsAddonIdApplications"></a>
# **getSelfAddonsAddonIdApplications**
> List&lt;Application&gt; getSelfAddonsAddonIdApplications(addonId)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String addonId = "addonId_example"; // String | 
    try {
      List<Application> result = apiInstance.getSelfAddonsAddonIdApplications(addonId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#getSelfAddonsAddonIdApplications");
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

<a id="getSelfAddonsAddonIdEnv"></a>
# **getSelfAddonsAddonIdEnv**
> List&lt;ListEnv&gt; getSelfAddonsAddonIdEnv(addonId)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String addonId = "addonId_example"; // String | 
    try {
      List<ListEnv> result = apiInstance.getSelfAddonsAddonIdEnv(addonId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#getSelfAddonsAddonIdEnv");
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

<a id="getSelfAddonsAddonIdSso"></a>
# **getSelfAddonsAddonIdSso**
> Sso getSelfAddonsAddonIdSso(addonId)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String addonId = "addonId_example"; // String | 
    try {
      Sso result = apiInstance.getSelfAddonsAddonIdSso(addonId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#getSelfAddonsAddonIdSso");
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

<a id="getSelfAddonsAddonIdTags"></a>
# **getSelfAddonsAddonIdTags**
> List&lt;String&gt; getSelfAddonsAddonIdTags(addonId)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String addonId = "addonId_example"; // String | 
    try {
      List<String> result = apiInstance.getSelfAddonsAddonIdTags(addonId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#getSelfAddonsAddonIdTags");
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

<a id="getSelfApplications"></a>
# **getSelfApplications**
> List&lt;Application&gt; getSelfApplications()



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    try {
      List<Application> result = apiInstance.getSelfApplications();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#getSelfApplications");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

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
| **200** | getApplications |  -  |

<a id="getSelfApplicationsAppId"></a>
# **getSelfApplicationsAppId**
> Application getSelfApplicationsAppId(appId)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String appId = "appId_example"; // String | 
    try {
      Application result = apiInstance.getSelfApplicationsAppId(appId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#getSelfApplicationsAppId");
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

<a id="getSelfApplicationsAppIdAddons"></a>
# **getSelfApplicationsAppIdAddons**
> List&lt;Addon&gt; getSelfApplicationsAppIdAddons(appId)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String appId = "appId_example"; // String | 
    try {
      List<Addon> result = apiInstance.getSelfApplicationsAppIdAddons(appId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#getSelfApplicationsAppIdAddons");
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

<a id="getSelfApplicationsAppIdAddonsEnv"></a>
# **getSelfApplicationsAppIdAddonsEnv**
> List&lt;Env&gt; getSelfApplicationsAppIdAddonsEnv(appId)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String appId = "appId_example"; // String | 
    try {
      List<Env> result = apiInstance.getSelfApplicationsAppIdAddonsEnv(appId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#getSelfApplicationsAppIdAddonsEnv");
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

<a id="getSelfApplicationsAppIdDependencies"></a>
# **getSelfApplicationsAppIdDependencies**
> List&lt;Application&gt; getSelfApplicationsAppIdDependencies(appId)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String appId = "appId_example"; // String | 
    try {
      List<Application> result = apiInstance.getSelfApplicationsAppIdDependencies(appId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#getSelfApplicationsAppIdDependencies");
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

<a id="getSelfApplicationsAppIdDependenciesDependencyId"></a>
# **getSelfApplicationsAppIdDependenciesDependencyId**
> getSelfApplicationsAppIdDependenciesDependencyId(dependencyId, appId, wannabeApplication)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String dependencyId = "dependencyId_example"; // String | 
    String appId = "appId_example"; // String | 
    WannabeApplication wannabeApplication = new WannabeApplication(); // WannabeApplication | 
    try {
      apiInstance.getSelfApplicationsAppIdDependenciesDependencyId(dependencyId, appId, wannabeApplication);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#getSelfApplicationsAppIdDependenciesDependencyId");
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
| **wannabeApplication** | [**WannabeApplication**](WannabeApplication.md)|  | |

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

<a id="getSelfApplicationsAppIdDependents"></a>
# **getSelfApplicationsAppIdDependents**
> List&lt;Application&gt; getSelfApplicationsAppIdDependents(appId)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String appId = "appId_example"; // String | 
    try {
      List<Application> result = apiInstance.getSelfApplicationsAppIdDependents(appId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#getSelfApplicationsAppIdDependents");
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

<a id="getSelfApplicationsAppIdDeployments"></a>
# **getSelfApplicationsAppIdDeployments**
> List&lt;Deployment&gt; getSelfApplicationsAppIdDeployments(appId, limit, offset, action)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String appId = "appId_example"; // String | 
    String limit = "limit_example"; // String | 
    String offset = "offset_example"; // String | 
    String action = "action_example"; // String | 
    try {
      List<Deployment> result = apiInstance.getSelfApplicationsAppIdDeployments(appId, limit, offset, action);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#getSelfApplicationsAppIdDeployments");
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
| **200** | getApplicationDeployments |  -  |

<a id="getSelfApplicationsAppIdEnv"></a>
# **getSelfApplicationsAppIdEnv**
> List&lt;ListEnv&gt; getSelfApplicationsAppIdEnv(appId)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String appId = "appId_example"; // String | 
    try {
      List<ListEnv> result = apiInstance.getSelfApplicationsAppIdEnv(appId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#getSelfApplicationsAppIdEnv");
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
| **200** | editApplicationEnv |  -  |

<a id="getSelfApplicationsAppIdInstances"></a>
# **getSelfApplicationsAppIdInstances**
> List&lt;Instance&gt; getSelfApplicationsAppIdInstances(appId)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String appId = "appId_example"; // String | 
    try {
      List<Instance> result = apiInstance.getSelfApplicationsAppIdInstances(appId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#getSelfApplicationsAppIdInstances");
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

### Return type

[**List&lt;Instance&gt;**](Instance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | getApplicationInstances |  -  |

<a id="getSelfApplicationsAppIdTags"></a>
# **getSelfApplicationsAppIdTags**
> List&lt;String&gt; getSelfApplicationsAppIdTags(appId)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String appId = "appId_example"; // String | 
    try {
      List<String> result = apiInstance.getSelfApplicationsAppIdTags(appId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#getSelfApplicationsAppIdTags");
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

<a id="getSelfApplicationsAppIdVhosts"></a>
# **getSelfApplicationsAppIdVhosts**
> List&lt;Vhost&gt; getSelfApplicationsAppIdVhosts(appId)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String appId = "appId_example"; // String | 
    try {
      List<Vhost> result = apiInstance.getSelfApplicationsAppIdVhosts(appId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#getSelfApplicationsAppIdVhosts");
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

<a id="getSelfApplicationsAppIdVhostsFavourite"></a>
# **getSelfApplicationsAppIdVhostsFavourite**
> Vhost getSelfApplicationsAppIdVhostsFavourite(appId)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String appId = "appId_example"; // String | 
    try {
      Vhost result = apiInstance.getSelfApplicationsAppIdVhostsFavourite(appId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#getSelfApplicationsAppIdVhostsFavourite");
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

<a id="getSelfConfirmationEmail"></a>
# **getSelfConfirmationEmail**
> getSelfConfirmationEmail()



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    try {
      apiInstance.getSelfConfirmationEmail();
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#getSelfConfirmationEmail");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
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

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | getConfirmationEmail |  -  |

<a id="getSelfConsumers"></a>
# **getSelfConsumers**
> List&lt;Consumer&gt; getSelfConsumers()



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    try {
      List<Consumer> result = apiInstance.getSelfConsumers();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#getSelfConsumers");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

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

<a id="getSelfConsumersKey"></a>
# **getSelfConsumersKey**
> Consumer getSelfConsumersKey(key)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String key = "key_example"; // String | 
    try {
      Consumer result = apiInstance.getSelfConsumersKey(key);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#getSelfConsumersKey");
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

<a id="getSelfConsumersKeySecret"></a>
# **getSelfConsumersKeySecret**
> Secret getSelfConsumersKeySecret(key)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String key = "key_example"; // String | 
    try {
      Secret result = apiInstance.getSelfConsumersKeySecret(key);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#getSelfConsumersKeySecret");
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

<a id="getSelfConsumptions"></a>
# **getSelfConsumptions**
> Conso getSelfConsumptions(appId, from, to)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String appId = "appId_example"; // String | 
    String from = "from_example"; // String | 
    String to = "to_example"; // String | 
    try {
      Conso result = apiInstance.getSelfConsumptions(appId, from, to);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#getSelfConsumptions");
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
| **200** | getConsumptions |  -  |

<a id="getSelfCredits"></a>
# **getSelfCredits**
> Credits getSelfCredits()



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    try {
      Credits result = apiInstance.getSelfCredits();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#getSelfCredits");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
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

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | getAmount |  -  |

<a id="getSelfEmails"></a>
# **getSelfEmails**
> List&lt;String&gt; getSelfEmails()



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    try {
      List<String> result = apiInstance.getSelfEmails();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#getSelfEmails");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

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
| **200** | getEmailAddresses |  -  |

<a id="getSelfId"></a>
# **getSelfId**
> String getSelfId()



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    try {
      String result = apiInstance.getSelfId();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#getSelfId");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
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

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | getId |  -  |

<a id="getSelfInstances"></a>
# **getSelfInstances**
> List&lt;Instance&gt; getSelfInstances()



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    try {
      List<Instance> result = apiInstance.getSelfInstances();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#getSelfInstances");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**List&lt;Instance&gt;**](Instance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | getInstancesForAllApps |  -  |

<a id="getSelfKeys"></a>
# **getSelfKeys**
> List&lt;Key&gt; getSelfKeys()



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    try {
      List<Key> result = apiInstance.getSelfKeys();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#getSelfKeys");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**List&lt;Key&gt;**](Key.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | getSshKeys |  -  |

<a id="getSelfPaymentInfo"></a>
# **getSelfPaymentInfo**
> getSelfPaymentInfo()



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    try {
      apiInstance.getSelfPaymentInfo();
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#getSelfPaymentInfo");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
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

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | getPaymentInfo |  -  |

<a id="getSelfPaymentsBillings"></a>
# **getSelfPaymentsBillings**
> getSelfPaymentsBillings()



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    try {
      apiInstance.getSelfPaymentsBillings();
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#getSelfPaymentsBillings");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
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

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | getInvoices |  -  |

<a id="getSelfPaymentsBillingsBid"></a>
# **getSelfPaymentsBillingsBid**
> getSelfPaymentsBillingsBid(bid)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String bid = "bid_example"; // String | 
    try {
      apiInstance.getSelfPaymentsBillingsBid(bid);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#getSelfPaymentsBillingsBid");
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

<a id="getSelfPaymentsBillingsBidPdf"></a>
# **getSelfPaymentsBillingsBidPdf**
> getSelfPaymentsBillingsBidPdf(bid, token)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String bid = "bid_example"; // String | 
    String token = "token_example"; // String | 
    try {
      apiInstance.getSelfPaymentsBillingsBidPdf(bid, token);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#getSelfPaymentsBillingsBidPdf");
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

<a id="getSelfPaymentsFullpricePrice"></a>
# **getSelfPaymentsFullpricePrice**
> getSelfPaymentsFullpricePrice(price)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String price = "price_example"; // String | 
    try {
      apiInstance.getSelfPaymentsFullpricePrice(price);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#getSelfPaymentsFullpricePrice");
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

<a id="getSelfPaymentsMethods"></a>
# **getSelfPaymentsMethods**
> getSelfPaymentsMethods()



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    try {
      apiInstance.getSelfPaymentsMethods();
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#getSelfPaymentsMethods");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
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

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | getUserPaymentMethods |  -  |

<a id="getSelfTokens"></a>
# **getSelfTokens**
> List&lt;Token&gt; getSelfTokens()



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    try {
      List<Token> result = apiInstance.getSelfTokens();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#getSelfTokens");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**List&lt;Token&gt;**](Token.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | getSelfTokens |  -  |

<a id="getSelfValidateEmail"></a>
# **getSelfValidateEmail**
> getSelfValidateEmail(validationKey)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String validationKey = "validationKey_example"; // String | 
    try {
      apiInstance.getSelfValidateEmail(validationKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#getSelfValidateEmail");
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
| **validationKey** | **String**|  | [optional] |

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
| **200** | validateEmail |  -  |

<a id="getSummary"></a>
# **getSummary**
> Summary getSummary()



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    try {
      Summary result = apiInstance.getSummary();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#getSummary");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
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

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | getSummary |  -  |

<a id="getUsersId"></a>
# **getUsersId**
> User getUsersId(id)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String id = "id_example"; // String | 
    try {
      User result = apiInstance.getUsersId(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#getUsersId");
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

[**User**](User.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | getUser |  -  |

<a id="getUsersIdApplications"></a>
# **getUsersIdApplications**
> List&lt;Application&gt; getUsersIdApplications(id)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String id = "id_example"; // String | 
    try {
      List<Application> result = apiInstance.getUsersIdApplications(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#getUsersIdApplications");
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
| **200** | getApplications |  -  |

<a id="getUsersUserIdGitInfo"></a>
# **getUsersUserIdGitInfo**
> getUsersUserIdGitInfo(userId)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String userId = "userId_example"; // String | 
    try {
      apiInstance.getUsersUserIdGitInfo(userId);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#getUsersUserIdGitInfo");
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
| **200** | getGitInfo |  -  |

<a id="getVendorApps"></a>
# **getVendorApps**
> List&lt;Application&gt; getVendorApps(offset)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    Integer offset = 56; // Integer | 
    try {
      List<Application> result = apiInstance.getVendorApps(offset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#getVendorApps");
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
| **offset** | **Integer**|  | [optional] |

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
| **200** | listApps |  -  |

<a id="getVendorAppsAddonId"></a>
# **getVendorAppsAddonId**
> getVendorAppsAddonId(addonId)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String addonId = "addonId_example"; // String | 
    try {
      apiInstance.getVendorAppsAddonId(addonId);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#getVendorAppsAddonId");
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
| **200** | getApplicationInfo |  -  |

<a id="listNetworkGroupMembers"></a>
# **listNetworkGroupMembers**
> List&lt;Schema1&gt; listNetworkGroupMembers(ownerId, networkGroupId, body)

List members

Lists members in a Network Group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String ownerId = "ownerId_example"; // String | Automatically added
    String networkGroupId = "networkGroupId_example"; // String | Automatically added
    Object body = null; // Object | 
    try {
      List<Schema1> result = apiInstance.listNetworkGroupMembers(ownerId, networkGroupId, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#listNetworkGroupMembers");
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

<a id="listNetworkGroupPeers"></a>
# **listNetworkGroupPeers**
> List&lt;Object&gt; listNetworkGroupPeers(ownerId, networkGroupId, body)

List peers

Lists peers in a Network Group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String ownerId = "ownerId_example"; // String | Automatically added
    String networkGroupId = "networkGroupId_example"; // String | Automatically added
    Object body = null; // Object | 
    try {
      List<Object> result = apiInstance.listNetworkGroupPeers(ownerId, networkGroupId, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#listNetworkGroupPeers");
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

<a id="listNetworkGroups"></a>
# **listNetworkGroups**
> List&lt;Object&gt; listNetworkGroups(ownerId, body)

List Network Groups

Lists Network Groups from an owner.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String ownerId = "ownerId_example"; // String | Automatically added
    Object body = null; // Object | 
    try {
      List<Object> result = apiInstance.listNetworkGroups(ownerId, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#listNetworkGroups");
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

<a id="logsAppIdDrainsGet"></a>
# **logsAppIdDrainsGet**
> logsAppIdDrainsGet(appId)



Fetch the logs drains for a given application

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String appId = "appId_example"; // String | Automatically added
    try {
      apiInstance.logsAppIdDrainsGet(appId);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#logsAppIdDrainsGet");
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
| **appId** | **String**| Automatically added | |

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
| **0** | &lt;No description&gt; |  -  |

<a id="logsAppIdDrainsIdOrUrlDelete"></a>
# **logsAppIdDrainsIdOrUrlDelete**
> logsAppIdDrainsIdOrUrlDelete(appId)



Delete the logs drain by id or url for a given application

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String appId = "appId_example"; // String | Automatically added
    try {
      apiInstance.logsAppIdDrainsIdOrUrlDelete(appId);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#logsAppIdDrainsIdOrUrlDelete");
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
| **appId** | **String**| Automatically added | |

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
| **0** | &lt;No description&gt; |  -  |

<a id="logsAppIdDrainsIdOrUrlGet"></a>
# **logsAppIdDrainsIdOrUrlGet**
> logsAppIdDrainsIdOrUrlGet(appId)



Fetch the logs drain by id or url for a given application

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String appId = "appId_example"; // String | Automatically added
    try {
      apiInstance.logsAppIdDrainsIdOrUrlGet(appId);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#logsAppIdDrainsIdOrUrlGet");
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
| **appId** | **String**| Automatically added | |

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
| **0** | &lt;No description&gt; |  -  |

<a id="logsAppIdDrainsPost"></a>
# **logsAppIdDrainsPost**
> logsAppIdDrainsPost(appId)



Add a log drain for a given application

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String appId = "appId_example"; // String | Automatically added
    try {
      apiInstance.logsAppIdDrainsPost(appId);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#logsAppIdDrainsPost");
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
| **appId** | **String**| Automatically added | |

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
| **0** | &lt;No description&gt; |  -  |

<a id="logsAppIdGet"></a>
# **logsAppIdGet**
> logsAppIdGet(appId, limit, order, after, before, filter, deploymentId)



Fetch the logs for a given application

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String appId = "appId_example"; // String | Application Id
    Integer limit = 56; // Integer | Number of lines to return
    String order = "asc"; // String | Logs order
    OffsetDateTime after = OffsetDateTime.now(); // OffsetDateTime | Lowest bound for logs date, ISO 8601
    OffsetDateTime before = OffsetDateTime.now(); // OffsetDateTime | Highest bounds for logs date, ISO 8601
    String filter = "filter_example"; // String | A pattern to filter with
    String deploymentId = "deploymentId_example"; // String | Only fetch logs emitted by this deployment
    try {
      apiInstance.logsAppIdGet(appId, limit, order, after, before, filter, deploymentId);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#logsAppIdGet");
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
| **appId** | **String**| Application Id | |
| **limit** | **Integer**| Number of lines to return | [optional] |
| **order** | **String**| Logs order | [optional] [default to desc] [enum: asc, desc] |
| **after** | **OffsetDateTime**| Lowest bound for logs date, ISO 8601 | [optional] |
| **before** | **OffsetDateTime**| Highest bounds for logs date, ISO 8601 | [optional] |
| **filter** | **String**| A pattern to filter with | [optional] |
| **deploymentId** | **String**| Only fetch logs emitted by this deployment | [optional] |

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
| **0** | &lt;No description&gt; |  -  |

<a id="logsAppIdSseGet"></a>
# **logsAppIdSseGet**
> logsAppIdSseGet(appId)



Retrieve logs as they come through a sse connection. To have authorization, you have to add &#x60;authorization&#x3D;oAuthAuthorizationString&#x60; as query param.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String appId = "appId_example"; // String | Automatically added
    try {
      apiInstance.logsAppIdSseGet(appId);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#logsAppIdSseGet");
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
| **appId** | **String**| Automatically added | |

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
| **0** | &lt;No description&gt; |  -  |

<a id="logsDrainsDrainIdPut"></a>
# **logsDrainsDrainIdPut**
> logsDrainsDrainIdPut(drainId)



Fetch all the logs drains (ccadmin dedicated route)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String drainId = "drainId_example"; // String | Automatically added
    try {
      apiInstance.logsDrainsDrainIdPut(drainId);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#logsDrainsDrainIdPut");
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
| **drainId** | **String**| Automatically added | |

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
| **0** | &lt;No description&gt; |  -  |

<a id="logsDrainsGet"></a>
# **logsDrainsGet**
> logsDrainsGet()



Fetch all the logs drains (ccadmin dedicated route)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    try {
      apiInstance.logsDrainsGet();
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#logsDrainsGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
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

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | &lt;No description&gt; |  -  |

<a id="logsLogsChunkedAppIdGet"></a>
# **logsLogsChunkedAppIdGet**
> logsLogsChunkedAppIdGet(appId, download)



Retrieve logs as they come through a chunked, never-ending response

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String appId = "appId_example"; // String | Application Id
    Boolean download = true; // Boolean | Tell the user-agent to download the body as a file
    try {
      apiInstance.logsLogsChunkedAppIdGet(appId, download);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#logsLogsChunkedAppIdGet");
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
| **appId** | **String**| Application Id | |
| **download** | **Boolean**| Tell the user-agent to download the body as a file | [optional] |

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
| **0** | &lt;No description&gt; |  -  |

<a id="logsLogsSocketAppIdGet"></a>
# **logsLogsSocketAppIdGet**
> logsLogsSocketAppIdGet(appId, since, filter, deploymentId)



Retrieve logs as they come through a websocket connection. To have authorization, you have to send a &#x60;{ \&quot;message_type\&quot;: \&quot;oauth\&quot;, \&quot;authorization\&quot;: \&quot;oauth authorization string\&quot; }&#x60; message

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String appId = "appId_example"; // String | Application Id
    OffsetDateTime since = OffsetDateTime.now(); // OffsetDateTime | Only fetch logs newer than this (ISO-8601 formatted) date
    String filter = "filter_example"; // String | A pattern to filter with
    String deploymentId = "deploymentId_example"; // String | Only fetch logs emitted by this deployment
    try {
      apiInstance.logsLogsSocketAppIdGet(appId, since, filter, deploymentId);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#logsLogsSocketAppIdGet");
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
| **appId** | **String**| Application Id | |
| **since** | **OffsetDateTime**| Only fetch logs newer than this (ISO-8601 formatted) date | [optional] |
| **filter** | **String**| A pattern to filter with | [optional] |
| **deploymentId** | **String**| Only fetch logs emitted by this deployment | [optional] |

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
| **0** | &lt;No description&gt; |  -  |

<a id="logsSocketAppIdGet"></a>
# **logsSocketAppIdGet**
> logsSocketAppIdGet(appId)



WebSocket to get logs for :appID. Optional queryString arg bind_to_es&#x3D;true to bind WS on log storage and not real time AMQP broker

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String appId = "appId_example"; // String | Automatically added
    try {
      apiInstance.logsSocketAppIdGet(appId);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#logsSocketAppIdGet");
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
| **appId** | **String**| Automatically added | |

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
| **0** | &lt;No description&gt; |  -  |

<a id="notificationsEmailhooksOwnerIdGet"></a>
# **notificationsEmailhooksOwnerIdGet**
> notificationsEmailhooksOwnerIdGet(ownerId)



list created e-mail hooks

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String ownerId = "ownerId_example"; // String | Automatically added
    try {
      apiInstance.notificationsEmailhooksOwnerIdGet(ownerId);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#notificationsEmailhooksOwnerIdGet");
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
| **0** | &lt;No description&gt; |  -  |

<a id="notificationsEmailhooksOwnerIdIdDelete"></a>
# **notificationsEmailhooksOwnerIdIdDelete**
> notificationsEmailhooksOwnerIdIdDelete(ownerId)



delete an e-mail hook

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String ownerId = "ownerId_example"; // String | Automatically added
    try {
      apiInstance.notificationsEmailhooksOwnerIdIdDelete(ownerId);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#notificationsEmailhooksOwnerIdIdDelete");
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
| **0** | &lt;No description&gt; |  -  |

<a id="notificationsEmailhooksOwnerIdIdPut"></a>
# **notificationsEmailhooksOwnerIdIdPut**
> notificationsEmailhooksOwnerIdIdPut(ownerId)



edit an e-mail hook

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String ownerId = "ownerId_example"; // String | Automatically added
    try {
      apiInstance.notificationsEmailhooksOwnerIdIdPut(ownerId);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#notificationsEmailhooksOwnerIdIdPut");
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
| **0** | &lt;No description&gt; |  -  |

<a id="notificationsEmailhooksOwnerIdPost"></a>
# **notificationsEmailhooksOwnerIdPost**
> notificationsEmailhooksOwnerIdPost(ownerId)



create a hook for e-mail notifications

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String ownerId = "ownerId_example"; // String | Automatically added
    try {
      apiInstance.notificationsEmailhooksOwnerIdPost(ownerId);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#notificationsEmailhooksOwnerIdPost");
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
| **0** | &lt;No description&gt; |  -  |

<a id="notificationsInfoEventsGet"></a>
# **notificationsInfoEventsGet**
> notificationsInfoEventsGet()



list available events

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    try {
      apiInstance.notificationsInfoEventsGet();
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#notificationsInfoEventsGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
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

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | &lt;No description&gt; |  -  |

<a id="notificationsInfoWebhookformatsGet"></a>
# **notificationsInfoWebhookformatsGet**
> notificationsInfoWebhookformatsGet()



list available webhook formats

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    try {
      apiInstance.notificationsInfoWebhookformatsGet();
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#notificationsInfoWebhookformatsGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
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

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | &lt;No description&gt; |  -  |

<a id="notificationsWebhooksOwnerIdGet"></a>
# **notificationsWebhooksOwnerIdGet**
> notificationsWebhooksOwnerIdGet(ownerId)



list created hooks

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String ownerId = "ownerId_example"; // String | Automatically added
    try {
      apiInstance.notificationsWebhooksOwnerIdGet(ownerId);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#notificationsWebhooksOwnerIdGet");
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
| **0** | &lt;No description&gt; |  -  |

<a id="notificationsWebhooksOwnerIdIdDelete"></a>
# **notificationsWebhooksOwnerIdIdDelete**
> notificationsWebhooksOwnerIdIdDelete(ownerId)



delete a hook

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String ownerId = "ownerId_example"; // String | Automatically added
    try {
      apiInstance.notificationsWebhooksOwnerIdIdDelete(ownerId);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#notificationsWebhooksOwnerIdIdDelete");
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
| **0** | &lt;No description&gt; |  -  |

<a id="notificationsWebhooksOwnerIdIdPut"></a>
# **notificationsWebhooksOwnerIdIdPut**
> notificationsWebhooksOwnerIdIdPut(ownerId)



edit a hook

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String ownerId = "ownerId_example"; // String | Automatically added
    try {
      apiInstance.notificationsWebhooksOwnerIdIdPut(ownerId);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#notificationsWebhooksOwnerIdIdPut");
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
| **0** | &lt;No description&gt; |  -  |

<a id="notificationsWebhooksOwnerIdPost"></a>
# **notificationsWebhooksOwnerIdPost**
> notificationsWebhooksOwnerIdPost(ownerId)



create a hook for notifications

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String ownerId = "ownerId_example"; // String | Automatically added
    try {
      apiInstance.notificationsWebhooksOwnerIdPost(ownerId);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#notificationsWebhooksOwnerIdPost");
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
| **0** | &lt;No description&gt; |  -  |

<a id="oauthAccessTokenQueryPost"></a>
# **oauthAccessTokenQueryPost**
> oauthAccessTokenQueryPost(oauthConsumerKey, oauthToken, oauthSignatureMethod, oauthSignature, oauthTimestamp, oauthNonce, oauthVersion, oauthVerifier, oauthCallback, oauthTokenSecret, oauthCallbackConfirmed)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String oauthConsumerKey = "oauthConsumerKey_example"; // String | 
    String oauthToken = "oauthToken_example"; // String | 
    String oauthSignatureMethod = "oauthSignatureMethod_example"; // String | 
    String oauthSignature = "oauthSignature_example"; // String | 
    String oauthTimestamp = "oauthTimestamp_example"; // String | 
    String oauthNonce = "oauthNonce_example"; // String | 
    String oauthVersion = "oauthVersion_example"; // String | 
    String oauthVerifier = "oauthVerifier_example"; // String | 
    String oauthCallback = "oauthCallback_example"; // String | 
    String oauthTokenSecret = "oauthTokenSecret_example"; // String | 
    String oauthCallbackConfirmed = "oauthCallbackConfirmed_example"; // String | 
    try {
      apiInstance.oauthAccessTokenQueryPost(oauthConsumerKey, oauthToken, oauthSignatureMethod, oauthSignature, oauthTimestamp, oauthNonce, oauthVersion, oauthVerifier, oauthCallback, oauthTokenSecret, oauthCallbackConfirmed);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#oauthAccessTokenQueryPost");
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
| **oauthConsumerKey** | **String**|  | [optional] |
| **oauthToken** | **String**|  | [optional] |
| **oauthSignatureMethod** | **String**|  | [optional] |
| **oauthSignature** | **String**|  | [optional] |
| **oauthTimestamp** | **String**|  | [optional] |
| **oauthNonce** | **String**|  | [optional] |
| **oauthVersion** | **String**|  | [optional] |
| **oauthVerifier** | **String**|  | [optional] |
| **oauthCallback** | **String**|  | [optional] |
| **oauthTokenSecret** | **String**|  | [optional] |
| **oauthCallbackConfirmed** | **String**|  | [optional] |

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

<a id="oauthRequestTokenQueryPost"></a>
# **oauthRequestTokenQueryPost**
> oauthRequestTokenQueryPost(oauthConsumerKey, oauthToken, oauthSignatureMethod, oauthSignature, oauthTimestamp, oauthNonce, oauthVersion, oauthVerifier, oauthCallback, oauthTokenSecret, oauthCallbackConfirmed)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String oauthConsumerKey = "oauthConsumerKey_example"; // String | 
    String oauthToken = "oauthToken_example"; // String | 
    String oauthSignatureMethod = "oauthSignatureMethod_example"; // String | 
    String oauthSignature = "oauthSignature_example"; // String | 
    String oauthTimestamp = "oauthTimestamp_example"; // String | 
    String oauthNonce = "oauthNonce_example"; // String | 
    String oauthVersion = "oauthVersion_example"; // String | 
    String oauthVerifier = "oauthVerifier_example"; // String | 
    String oauthCallback = "oauthCallback_example"; // String | 
    String oauthTokenSecret = "oauthTokenSecret_example"; // String | 
    String oauthCallbackConfirmed = "oauthCallbackConfirmed_example"; // String | 
    try {
      apiInstance.oauthRequestTokenQueryPost(oauthConsumerKey, oauthToken, oauthSignatureMethod, oauthSignature, oauthTimestamp, oauthNonce, oauthVersion, oauthVerifier, oauthCallback, oauthTokenSecret, oauthCallbackConfirmed);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#oauthRequestTokenQueryPost");
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
| **oauthConsumerKey** | **String**|  | [optional] |
| **oauthToken** | **String**|  | [optional] |
| **oauthSignatureMethod** | **String**|  | [optional] |
| **oauthSignature** | **String**|  | [optional] |
| **oauthTimestamp** | **String**|  | [optional] |
| **oauthNonce** | **String**|  | [optional] |
| **oauthVersion** | **String**|  | [optional] |
| **oauthVerifier** | **String**|  | [optional] |
| **oauthCallback** | **String**|  | [optional] |
| **oauthTokenSecret** | **String**|  | [optional] |
| **oauthCallbackConfirmed** | **String**|  | [optional] |

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

<a id="openapiGet"></a>
# **openapiGet**
> openapiGet()



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    try {
      apiInstance.openapiGet();
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#openapiGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
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

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The swagger documenting this API in yaml format. |  -  |

<a id="openapiTypeGet"></a>
# **openapiTypeGet**
> openapiTypeGet(type)

Get the swagger for this API as {type}

Get the swagger for this API as {type}. Type can be either \&quot;yml\&quot; or \&quot;json\&quot;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String type = "type_example"; // String | 
    try {
      apiInstance.openapiTypeGet(type);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#openapiTypeGet");
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
| **type** | **String**|  | |

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
| **200** | This API swagger documentation in {type} format. |  -  |

<a id="organisationsIdAddonprovidersProviderIdDelete"></a>
# **organisationsIdAddonprovidersProviderIdDelete**
> organisationsIdAddonprovidersProviderIdDelete(id, providerId)

Remove an add-on provider

Remove a given add-on provider. providerId must be owned by organisation {id}.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String id = "id_example"; // String | 
    String providerId = "providerId_example"; // String | 
    try {
      apiInstance.organisationsIdAddonprovidersProviderIdDelete(id, providerId);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#organisationsIdAddonprovidersProviderIdDelete");
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

<a id="organisationsIdAddonsAddonIdInstancesGet"></a>
# **organisationsIdAddonsAddonIdInstancesGet**
> List&lt;SupernovaInstanceView&gt; organisationsIdAddonsAddonIdInstancesGet(id, addonId, deploymentId, withDeleted)

List instances for this add-on.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String id = "id_example"; // String | 
    String addonId = "addonId_example"; // String | 
    String deploymentId = "deploymentId_example"; // String | 
    String withDeleted = "withDeleted_example"; // String | 
    try {
      List<SupernovaInstanceView> result = apiInstance.organisationsIdAddonsAddonIdInstancesGet(id, addonId, deploymentId, withDeleted);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#organisationsIdAddonsAddonIdInstancesGet");
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

<a id="organisationsIdAddonsAddonIdInstancesInstanceIdGet"></a>
# **organisationsIdAddonsAddonIdInstancesInstanceIdGet**
> SupernovaInstanceView organisationsIdAddonsAddonIdInstancesInstanceIdGet(instanceId, id, addonId)

Get a specific instance for {addonId}

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String instanceId = "instanceId_example"; // String | 
    String id = "id_example"; // String | 
    String addonId = "addonId_example"; // String | 
    try {
      SupernovaInstanceView result = apiInstance.organisationsIdAddonsAddonIdInstancesInstanceIdGet(instanceId, id, addonId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#organisationsIdAddonsAddonIdInstancesInstanceIdGet");
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

<a id="organisationsIdAddonsAddonIdMigrationsGet"></a>
# **organisationsIdAddonsAddonIdMigrationsGet**
> List&lt;AddonMigration&gt; organisationsIdAddonsAddonIdMigrationsGet(id, addonId)

Get past migrations from add-on.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String id = "id_example"; // String | 
    String addonId = "addonId_example"; // String | 
    try {
      List<AddonMigration> result = apiInstance.organisationsIdAddonsAddonIdMigrationsGet(id, addonId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#organisationsIdAddonsAddonIdMigrationsGet");
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

<a id="organisationsIdAddonsAddonIdMigrationsMigrationIdGet"></a>
# **organisationsIdAddonsAddonIdMigrationsMigrationIdGet**
> AddonMigration organisationsIdAddonsAddonIdMigrationsMigrationIdGet(migrationId, id, addonId)

Get a given migration

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String migrationId = "migrationId_example"; // String | 
    String id = "id_example"; // String | 
    String addonId = "addonId_example"; // String | 
    try {
      AddonMigration result = apiInstance.organisationsIdAddonsAddonIdMigrationsMigrationIdGet(migrationId, id, addonId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#organisationsIdAddonsAddonIdMigrationsMigrationIdGet");
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

<a id="organisationsIdAddonsAddonIdMigrationsPost"></a>
# **organisationsIdAddonsAddonIdMigrationsPost**
> Object organisationsIdAddonsAddonIdMigrationsPost(id, addonId, organisationsIdAddonsAddonIdMigrationsPostRequest)

Start a new add-on migration

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String id = "id_example"; // String | 
    String addonId = "addonId_example"; // String | 
    OrganisationsIdAddonsAddonIdMigrationsPostRequest organisationsIdAddonsAddonIdMigrationsPostRequest = new OrganisationsIdAddonsAddonIdMigrationsPostRequest(); // OrganisationsIdAddonsAddonIdMigrationsPostRequest | 
    try {
      Object result = apiInstance.organisationsIdAddonsAddonIdMigrationsPost(id, addonId, organisationsIdAddonsAddonIdMigrationsPostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#organisationsIdAddonsAddonIdMigrationsPost");
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

<a id="organisationsIdAddonsAddonIdSsoGet"></a>
# **organisationsIdAddonsAddonIdSsoGet**
> Sso organisationsIdAddonsAddonIdSsoGet(id, addonId)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String id = "id_example"; // String | 
    String addonId = "addonId_example"; // String | 
    try {
      Sso result = apiInstance.organisationsIdAddonsAddonIdSsoGet(id, addonId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#organisationsIdAddonsAddonIdSsoGet");
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

<a id="organisationsIdAddonsPreordersPost"></a>
# **organisationsIdAddonsPreordersPost**
> organisationsIdAddonsPreordersPost(id, wannabeAddon)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String id = "id_example"; // String | 
    WannabeAddon wannabeAddon = new WannabeAddon(); // WannabeAddon | 
    try {
      apiInstance.organisationsIdAddonsPreordersPost(id, wannabeAddon);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#organisationsIdAddonsPreordersPost");
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

<a id="organisationsIdApplicationsAppIdBranchPut"></a>
# **organisationsIdApplicationsAppIdBranchPut**
> organisationsIdApplicationsAppIdBranchPut(appId, id)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String appId = "appId_example"; // String | 
    String id = "id_example"; // String | 
    try {
      apiInstance.organisationsIdApplicationsAppIdBranchPut(appId, id);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#organisationsIdApplicationsAppIdBranchPut");
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

<a id="organisationsIdApplicationsAppIdBranchesGet"></a>
# **organisationsIdApplicationsAppIdBranchesGet**
> organisationsIdApplicationsAppIdBranchesGet(appId, id)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String appId = "appId_example"; // String | 
    String id = "id_example"; // String | 
    try {
      apiInstance.organisationsIdApplicationsAppIdBranchesGet(appId, id);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#organisationsIdApplicationsAppIdBranchesGet");
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

<a id="organisationsIdApplicationsAppIdBuildflavorPut"></a>
# **organisationsIdApplicationsAppIdBuildflavorPut**
> organisationsIdApplicationsAppIdBuildflavorPut(appId, id)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String appId = "appId_example"; // String | 
    String id = "id_example"; // String | 
    try {
      apiInstance.organisationsIdApplicationsAppIdBuildflavorPut(appId, id);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#organisationsIdApplicationsAppIdBuildflavorPut");
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

<a id="organisationsIdApplicationsAppIdDependenciesEnvGet"></a>
# **organisationsIdApplicationsAppIdDependenciesEnvGet**
> List&lt;LinkedAppEnv&gt; organisationsIdApplicationsAppIdDependenciesEnvGet(appId, id)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String appId = "appId_example"; // String | 
    String id = "id_example"; // String | 
    try {
      List<LinkedAppEnv> result = apiInstance.organisationsIdApplicationsAppIdDependenciesEnvGet(appId, id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#organisationsIdApplicationsAppIdDependenciesEnvGet");
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

<a id="organisationsIdApplicationsAppIdDeploymentsDeploymentIdGet"></a>
# **organisationsIdApplicationsAppIdDeploymentsDeploymentIdGet**
> organisationsIdApplicationsAppIdDeploymentsDeploymentIdGet(appId, deploymentId, id)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String appId = "appId_example"; // String | 
    String deploymentId = "deploymentId_example"; // String | 
    String id = "id_example"; // String | 
    try {
      apiInstance.organisationsIdApplicationsAppIdDeploymentsDeploymentIdGet(appId, deploymentId, id);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#organisationsIdApplicationsAppIdDeploymentsDeploymentIdGet");
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

<a id="organisationsIdApplicationsAppIdExposedEnvGet"></a>
# **organisationsIdApplicationsAppIdExposedEnvGet**
> organisationsIdApplicationsAppIdExposedEnvGet(appId, id)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String appId = "appId_example"; // String | 
    String id = "id_example"; // String | 
    try {
      apiInstance.organisationsIdApplicationsAppIdExposedEnvGet(appId, id);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#organisationsIdApplicationsAppIdExposedEnvGet");
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

<a id="organisationsIdApplicationsAppIdExposedEnvPut"></a>
# **organisationsIdApplicationsAppIdExposedEnvPut**
> organisationsIdApplicationsAppIdExposedEnvPut(appId, id)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String appId = "appId_example"; // String | 
    String id = "id_example"; // String | 
    try {
      apiInstance.organisationsIdApplicationsAppIdExposedEnvPut(appId, id);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#organisationsIdApplicationsAppIdExposedEnvPut");
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

<a id="organisationsIdApplicationsAppIdInstancesInstanceIdGet"></a>
# **organisationsIdApplicationsAppIdInstancesInstanceIdGet**
> organisationsIdApplicationsAppIdInstancesInstanceIdGet(instanceId, appId, id)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String instanceId = "instanceId_example"; // String | 
    String appId = "appId_example"; // String | 
    String id = "id_example"; // String | 
    try {
      apiInstance.organisationsIdApplicationsAppIdInstancesInstanceIdGet(instanceId, appId, id);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#organisationsIdApplicationsAppIdInstancesInstanceIdGet");
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

<a id="organisationsIdPaymentsBillingsUnpaidGet"></a>
# **organisationsIdPaymentsBillingsUnpaidGet**
> organisationsIdPaymentsBillingsUnpaidGet(id)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String id = "id_example"; // String | 
    try {
      apiInstance.organisationsIdPaymentsBillingsUnpaidGet(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#organisationsIdPaymentsBillingsUnpaidGet");
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

<a id="organisationsIdPaymentsMethodsDefaultGet"></a>
# **organisationsIdPaymentsMethodsDefaultGet**
> organisationsIdPaymentsMethodsDefaultGet(id)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String id = "id_example"; // String | 
    try {
      apiInstance.organisationsIdPaymentsMethodsDefaultGet(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#organisationsIdPaymentsMethodsDefaultGet");
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

<a id="organisationsIdPaymentsMethodsDefaultPut"></a>
# **organisationsIdPaymentsMethodsDefaultPut**
> organisationsIdPaymentsMethodsDefaultPut(id, paymentData)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String id = "id_example"; // String | 
    PaymentData paymentData = new PaymentData(); // PaymentData | 
    try {
      apiInstance.organisationsIdPaymentsMethodsDefaultPut(id, paymentData);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#organisationsIdPaymentsMethodsDefaultPut");
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

<a id="organisationsIdPaymentsMethodsGet"></a>
# **organisationsIdPaymentsMethodsGet**
> organisationsIdPaymentsMethodsGet(id)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String id = "id_example"; // String | 
    try {
      apiInstance.organisationsIdPaymentsMethodsGet(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#organisationsIdPaymentsMethodsGet");
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

<a id="organisationsIdPaymentsMethodsMIdDelete"></a>
# **organisationsIdPaymentsMethodsMIdDelete**
> organisationsIdPaymentsMethodsMIdDelete(mId, id)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String mId = "mId_example"; // String | 
    String id = "id_example"; // String | 
    try {
      apiInstance.organisationsIdPaymentsMethodsMIdDelete(mId, id);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#organisationsIdPaymentsMethodsMIdDelete");
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

<a id="organisationsIdPaymentsMethodsPost"></a>
# **organisationsIdPaymentsMethodsPost**
> organisationsIdPaymentsMethodsPost(id, body)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String id = "id_example"; // String | 
    Body body = new Body(); // Body | 
    try {
      apiInstance.organisationsIdPaymentsMethodsPost(id, body);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#organisationsIdPaymentsMethodsPost");
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

<a id="organisationsIdPaymentsMonthlyinvoiceGet"></a>
# **organisationsIdPaymentsMonthlyinvoiceGet**
> organisationsIdPaymentsMonthlyinvoiceGet(id)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String id = "id_example"; // String | 
    try {
      apiInstance.organisationsIdPaymentsMonthlyinvoiceGet(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#organisationsIdPaymentsMonthlyinvoiceGet");
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

<a id="organisationsIdPaymentsMonthlyinvoiceMaxcreditPut"></a>
# **organisationsIdPaymentsMonthlyinvoiceMaxcreditPut**
> organisationsIdPaymentsMonthlyinvoiceMaxcreditPut(id)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String id = "id_example"; // String | 
    try {
      apiInstance.organisationsIdPaymentsMonthlyinvoiceMaxcreditPut(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#organisationsIdPaymentsMonthlyinvoiceMaxcreditPut");
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

<a id="organisationsIdPaymentsRecurringGet"></a>
# **organisationsIdPaymentsRecurringGet**
> organisationsIdPaymentsRecurringGet(id)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String id = "id_example"; // String | 
    try {
      apiInstance.organisationsIdPaymentsRecurringGet(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#organisationsIdPaymentsRecurringGet");
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

<a id="paymentsAssetsPayButtonTokenButtonPngGet"></a>
# **paymentsAssetsPayButtonTokenButtonPngGet**
> paymentsAssetsPayButtonTokenButtonPngGet(token)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String token = "token_example"; // String | 
    try {
      apiInstance.paymentsAssetsPayButtonTokenButtonPngGet(token);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#paymentsAssetsPayButtonTokenButtonPngGet");
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
| **token** | **String**|  | |

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

<a id="paymentsBidEndStripePost"></a>
# **paymentsBidEndStripePost**
> paymentsBidEndStripePost(bid)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String bid = "bid_example"; // String | 
    try {
      apiInstance.paymentsBidEndStripePost(bid);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#paymentsBidEndStripePost");
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
| **200** | endPaymentWithStripe |  -  |

<a id="postAuthorize"></a>
# **postAuthorize**
> postAuthorize()



Handled by our API.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    try {
      apiInstance.postAuthorize();
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#postAuthorize");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
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

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | authorize |  -  |

<a id="postGithubRedeploy"></a>
# **postGithubRedeploy**
> postGithubRedeploy(userAgent, xGithubEvent, xHubSignature)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String userAgent = "userAgent_example"; // String | 
    String xGithubEvent = "xGithubEvent_example"; // String | 
    String xHubSignature = "xHubSignature_example"; // String | 
    try {
      apiInstance.postGithubRedeploy(userAgent, xGithubEvent, xHubSignature);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#postGithubRedeploy");
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
| **userAgent** | **String**|  | [optional] |
| **xGithubEvent** | **String**|  | [optional] |
| **xHubSignature** | **String**|  | [optional] |

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
| **200** | redeployApp |  -  |

<a id="postGithubSignup"></a>
# **postGithubSignup**
> postGithubSignup(transactionId, name, otherId, otherEmail, password, autoLink, terms)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String transactionId = "transactionId_example"; // String | 
    String name = "name_example"; // String | 
    String otherId = "otherId_example"; // String | 
    String otherEmail = "otherEmail_example"; // String | 
    String password = "password_example"; // String | 
    String autoLink = "autoLink_example"; // String | 
    String terms = "terms_example"; // String | 
    try {
      apiInstance.postGithubSignup(transactionId, name, otherId, otherEmail, password, autoLink, terms);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#postGithubSignup");
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
| **transactionId** | **String**|  | [optional] |
| **name** | **String**|  | [optional] |
| **otherId** | **String**|  | [optional] |
| **otherEmail** | **String**|  | [optional] |
| **password** | **String**|  | [optional] |
| **autoLink** | **String**|  | [optional] |
| **terms** | **String**|  | [optional] |

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
| **200** | finsihGithubSignup |  -  |

<a id="postOauthAccessToken"></a>
# **postOauthAccessToken**
> postOauthAccessToken(oauthConsumerKey, oauthToken, oauthSignatureMethod, oauthSignature, oauthTimestamp, oauthNonce, oauthVersion, oauthVerifier, oauthCallback, oauthTokenSecret, oauthCallbackConfirmed)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String oauthConsumerKey = "oauthConsumerKey_example"; // String | 
    String oauthToken = "oauthToken_example"; // String | 
    String oauthSignatureMethod = "oauthSignatureMethod_example"; // String | 
    String oauthSignature = "oauthSignature_example"; // String | 
    String oauthTimestamp = "oauthTimestamp_example"; // String | 
    String oauthNonce = "oauthNonce_example"; // String | 
    String oauthVersion = "oauthVersion_example"; // String | 
    String oauthVerifier = "oauthVerifier_example"; // String | 
    String oauthCallback = "oauthCallback_example"; // String | 
    String oauthTokenSecret = "oauthTokenSecret_example"; // String | 
    String oauthCallbackConfirmed = "oauthCallbackConfirmed_example"; // String | 
    try {
      apiInstance.postOauthAccessToken(oauthConsumerKey, oauthToken, oauthSignatureMethod, oauthSignature, oauthTimestamp, oauthNonce, oauthVersion, oauthVerifier, oauthCallback, oauthTokenSecret, oauthCallbackConfirmed);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#postOauthAccessToken");
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
| **oauthConsumerKey** | **String**|  | [optional] |
| **oauthToken** | **String**|  | [optional] |
| **oauthSignatureMethod** | **String**|  | [optional] |
| **oauthSignature** | **String**|  | [optional] |
| **oauthTimestamp** | **String**|  | [optional] |
| **oauthNonce** | **String**|  | [optional] |
| **oauthVersion** | **String**|  | [optional] |
| **oauthVerifier** | **String**|  | [optional] |
| **oauthCallback** | **String**|  | [optional] |
| **oauthTokenSecret** | **String**|  | [optional] |
| **oauthCallbackConfirmed** | **String**|  | [optional] |

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
| **200** | postAccessTokenRequest |  -  |

<a id="postOauthAuthorize"></a>
# **postOauthAuthorize**
> postOauthAuthorize(almighty, accessOrganisations, manageOrganisations, manageOrganisationsServices, manageOrganisationsApplications, manageOrganisationsMembers, accessOrganisationsBills, accessOrganisationsCreditCount, accessOrganisationsConsumptionStatistics, accessPersonalInformation, managePersonalInformation, manageSshKeys, manageServices, manageApplications, accessBills, accessCreditCount, accessConsumptionStatistics, cookie)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String almighty = "almighty_example"; // String | 
    String accessOrganisations = "accessOrganisations_example"; // String | 
    String manageOrganisations = "manageOrganisations_example"; // String | 
    String manageOrganisationsServices = "manageOrganisationsServices_example"; // String | 
    String manageOrganisationsApplications = "manageOrganisationsApplications_example"; // String | 
    String manageOrganisationsMembers = "manageOrganisationsMembers_example"; // String | 
    String accessOrganisationsBills = "accessOrganisationsBills_example"; // String | 
    String accessOrganisationsCreditCount = "accessOrganisationsCreditCount_example"; // String | 
    String accessOrganisationsConsumptionStatistics = "accessOrganisationsConsumptionStatistics_example"; // String | 
    String accessPersonalInformation = "accessPersonalInformation_example"; // String | 
    String managePersonalInformation = "managePersonalInformation_example"; // String | 
    String manageSshKeys = "manageSshKeys_example"; // String | 
    String manageServices = "manageServices_example"; // String | 
    String manageApplications = "manageApplications_example"; // String | 
    String accessBills = "accessBills_example"; // String | 
    String accessCreditCount = "accessCreditCount_example"; // String | 
    String accessConsumptionStatistics = "accessConsumptionStatistics_example"; // String | 
    String cookie = "cookie_example"; // String | 
    try {
      apiInstance.postOauthAuthorize(almighty, accessOrganisations, manageOrganisations, manageOrganisationsServices, manageOrganisationsApplications, manageOrganisationsMembers, accessOrganisationsBills, accessOrganisationsCreditCount, accessOrganisationsConsumptionStatistics, accessPersonalInformation, managePersonalInformation, manageSshKeys, manageServices, manageApplications, accessBills, accessCreditCount, accessConsumptionStatistics, cookie);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#postOauthAuthorize");
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
| **almighty** | **String**|  | [optional] |
| **accessOrganisations** | **String**|  | [optional] |
| **manageOrganisations** | **String**|  | [optional] |
| **manageOrganisationsServices** | **String**|  | [optional] |
| **manageOrganisationsApplications** | **String**|  | [optional] |
| **manageOrganisationsMembers** | **String**|  | [optional] |
| **accessOrganisationsBills** | **String**|  | [optional] |
| **accessOrganisationsCreditCount** | **String**|  | [optional] |
| **accessOrganisationsConsumptionStatistics** | **String**|  | [optional] |
| **accessPersonalInformation** | **String**|  | [optional] |
| **managePersonalInformation** | **String**|  | [optional] |
| **manageSshKeys** | **String**|  | [optional] |
| **manageServices** | **String**|  | [optional] |
| **manageApplications** | **String**|  | [optional] |
| **accessBills** | **String**|  | [optional] |
| **accessCreditCount** | **String**|  | [optional] |
| **accessConsumptionStatistics** | **String**|  | [optional] |
| **cookie** | **String**|  | [optional] |

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
| **200** | authorizeToken |  -  |

<a id="postOauthRequestToken"></a>
# **postOauthRequestToken**
> postOauthRequestToken(oauthConsumerKey, oauthToken, oauthSignatureMethod, oauthSignature, oauthTimestamp, oauthNonce, oauthVersion, oauthVerifier, oauthCallback, oauthTokenSecret, oauthCallbackConfirmed)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String oauthConsumerKey = "oauthConsumerKey_example"; // String | 
    String oauthToken = "oauthToken_example"; // String | 
    String oauthSignatureMethod = "oauthSignatureMethod_example"; // String | 
    String oauthSignature = "oauthSignature_example"; // String | 
    String oauthTimestamp = "oauthTimestamp_example"; // String | 
    String oauthNonce = "oauthNonce_example"; // String | 
    String oauthVersion = "oauthVersion_example"; // String | 
    String oauthVerifier = "oauthVerifier_example"; // String | 
    String oauthCallback = "oauthCallback_example"; // String | 
    String oauthTokenSecret = "oauthTokenSecret_example"; // String | 
    String oauthCallbackConfirmed = "oauthCallbackConfirmed_example"; // String | 
    try {
      apiInstance.postOauthRequestToken(oauthConsumerKey, oauthToken, oauthSignatureMethod, oauthSignature, oauthTimestamp, oauthNonce, oauthVersion, oauthVerifier, oauthCallback, oauthTokenSecret, oauthCallbackConfirmed);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#postOauthRequestToken");
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
| **oauthConsumerKey** | **String**|  | [optional] |
| **oauthToken** | **String**|  | [optional] |
| **oauthSignatureMethod** | **String**|  | [optional] |
| **oauthSignature** | **String**|  | [optional] |
| **oauthTimestamp** | **String**|  | [optional] |
| **oauthNonce** | **String**|  | [optional] |
| **oauthVersion** | **String**|  | [optional] |
| **oauthVerifier** | **String**|  | [optional] |
| **oauthCallback** | **String**|  | [optional] |
| **oauthTokenSecret** | **String**|  | [optional] |
| **oauthCallbackConfirmed** | **String**|  | [optional] |

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
| **200** | postReqTokenRequest |  -  |

<a id="postOrganisations"></a>
# **postOrganisations**
> Organisation postOrganisations(wannabeOrganisation)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    WannabeOrganisation wannabeOrganisation = new WannabeOrganisation(); // WannabeOrganisation | 
    try {
      Organisation result = apiInstance.postOrganisations(wannabeOrganisation);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#postOrganisations");
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

<a id="postOrganisationsIdAddonproviders"></a>
# **postOrganisationsIdAddonproviders**
> Provider postOrganisationsIdAddonproviders(id, wannabeAddonProvider)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String id = "id_example"; // String | 
    WannabeAddonProvider wannabeAddonProvider = new WannabeAddonProvider(); // WannabeAddonProvider | 
    try {
      Provider result = apiInstance.postOrganisationsIdAddonproviders(id, wannabeAddonProvider);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#postOrganisationsIdAddonproviders");
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

<a id="postOrganisationsIdAddonprovidersProviderIdFeatures"></a>
# **postOrganisationsIdAddonprovidersProviderIdFeatures**
> Feature postOrganisationsIdAddonprovidersProviderIdFeatures(id, providerId, wannabeFeature)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String id = "id_example"; // String | 
    String providerId = "providerId_example"; // String | 
    WannabeFeature wannabeFeature = new WannabeFeature(); // WannabeFeature | 
    try {
      Feature result = apiInstance.postOrganisationsIdAddonprovidersProviderIdFeatures(id, providerId, wannabeFeature);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#postOrganisationsIdAddonprovidersProviderIdFeatures");
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

<a id="postOrganisationsIdAddonprovidersProviderIdPlans"></a>
# **postOrganisationsIdAddonprovidersProviderIdPlans**
> Plan postOrganisationsIdAddonprovidersProviderIdPlans(id, providerId, wannabePlan)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String id = "id_example"; // String | 
    String providerId = "providerId_example"; // String | 
    WannabePlan wannabePlan = new WannabePlan(); // WannabePlan | 
    try {
      Plan result = apiInstance.postOrganisationsIdAddonprovidersProviderIdPlans(id, providerId, wannabePlan);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#postOrganisationsIdAddonprovidersProviderIdPlans");
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

<a id="postOrganisationsIdAddonprovidersProviderIdTesters"></a>
# **postOrganisationsIdAddonprovidersProviderIdTesters**
> postOrganisationsIdAddonprovidersProviderIdTesters(id, providerId)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String id = "id_example"; // String | 
    String providerId = "providerId_example"; // String | 
    try {
      apiInstance.postOrganisationsIdAddonprovidersProviderIdTesters(id, providerId);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#postOrganisationsIdAddonprovidersProviderIdTesters");
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

<a id="postOrganisationsIdAddons"></a>
# **postOrganisationsIdAddons**
> Addon postOrganisationsIdAddons(id, wannabeAddon)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String id = "id_example"; // String | 
    WannabeAddon wannabeAddon = new WannabeAddon(); // WannabeAddon | 
    try {
      Addon result = apiInstance.postOrganisationsIdAddons(id, wannabeAddon);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#postOrganisationsIdAddons");
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

<a id="postOrganisationsIdApplications"></a>
# **postOrganisationsIdApplications**
> Application postOrganisationsIdApplications(id, wannabeApplication)



Creates an application. If you want to create a Github app, you need to replace the oauthApp field with what you will find here: https://github.com/CleverCloud/doc.clever-cloud.com/issues/179

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String id = "id_example"; // String | 
    WannabeApplication wannabeApplication = new WannabeApplication(); // WannabeApplication | 
    try {
      Application result = apiInstance.postOrganisationsIdApplications(id, wannabeApplication);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#postOrganisationsIdApplications");
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

<a id="postOrganisationsIdApplicationsAppIdAddons"></a>
# **postOrganisationsIdApplicationsAppIdAddons**
> postOrganisationsIdApplicationsAppIdAddons(id, appId, body)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String id = "id_example"; // String | 
    String appId = "appId_example"; // String | 
    Body body = new Body(); // Body | 
    try {
      apiInstance.postOrganisationsIdApplicationsAppIdAddons(id, appId, body);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#postOrganisationsIdApplicationsAppIdAddons");
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

<a id="postOrganisationsIdApplicationsAppIdInstances"></a>
# **postOrganisationsIdApplicationsAppIdInstances**
> postOrganisationsIdApplicationsAppIdInstances(id, appId, commit)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String id = "id_example"; // String | 
    String appId = "appId_example"; // String | 
    String commit = "commit_example"; // String | 
    try {
      apiInstance.postOrganisationsIdApplicationsAppIdInstances(id, appId, commit);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#postOrganisationsIdApplicationsAppIdInstances");
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

<a id="postOrganisationsIdConsumers"></a>
# **postOrganisationsIdConsumers**
> postOrganisationsIdConsumers(id, wannabeConsumer)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String id = "id_example"; // String | 
    WannabeConsumer wannabeConsumer = new WannabeConsumer(); // WannabeConsumer | 
    try {
      apiInstance.postOrganisationsIdConsumers(id, wannabeConsumer);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#postOrganisationsIdConsumers");
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

<a id="postOrganisationsIdMembers"></a>
# **postOrganisationsIdMembers**
> postOrganisationsIdMembers(id, body, invitationKey)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String id = "id_example"; // String | 
    Schema2 body = new Schema2(); // Schema2 | 
    String invitationKey = "invitationKey_example"; // String | 
    try {
      apiInstance.postOrganisationsIdMembers(id, body, invitationKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#postOrganisationsIdMembers");
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

<a id="postOrganisationsIdPaymentsBillings"></a>
# **postOrganisationsIdPaymentsBillings**
> postOrganisationsIdPaymentsBillings(id)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String id = "id_example"; // String | 
    try {
      apiInstance.postOrganisationsIdPaymentsBillings(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#postOrganisationsIdPaymentsBillings");
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

<a id="postPasswordForgotten"></a>
# **postPasswordForgotten**
> postPasswordForgotten(login, dropTokens, testerPass)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String login = "login_example"; // String | 
    String dropTokens = "dropTokens_example"; // String | 
    String testerPass = "testerPass_example"; // String | 
    try {
      apiInstance.postPasswordForgotten(login, dropTokens, testerPass);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#postPasswordForgotten");
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
| **login** | **String**|  | [optional] |
| **dropTokens** | **String**|  | [optional] |
| **testerPass** | **String**|  | [optional] |

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
| **200** | askForPasswordResetViaForm |  -  |

<a id="postPasswordForgottenKey"></a>
# **postPasswordForgottenKey**
> postPasswordForgottenKey(key, pass, pass2)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String key = "key_example"; // String | 
    String pass = "pass_example"; // String | 
    String pass2 = "pass2_example"; // String | 
    try {
      apiInstance.postPasswordForgottenKey(key, pass, pass2);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#postPasswordForgottenKey");
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
| **key** | **String**|  | |
| **pass** | **String**|  | [optional] |
| **pass2** | **String**|  | [optional] |

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
| **200** | resetPasswordForgotten |  -  |

<a id="postSelfAddons"></a>
# **postSelfAddons**
> postSelfAddons(wannabeAddon)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    WannabeAddon wannabeAddon = new WannabeAddon(); // WannabeAddon | 
    try {
      apiInstance.postSelfAddons(wannabeAddon);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#postSelfAddons");
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
| **200** | provisionAddon |  -  |

<a id="postSelfApplications"></a>
# **postSelfApplications**
> postSelfApplications(wannabeApplication)



Creates an application. If you want to create a Github app, you need to replace the oauthApp field with what you will find here: https://github.com/CleverCloud/doc.clever-cloud.com/issues/179

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    WannabeApplication wannabeApplication = new WannabeApplication(); // WannabeApplication | 
    try {
      apiInstance.postSelfApplications(wannabeApplication);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#postSelfApplications");
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
| **wannabeApplication** | [**WannabeApplication**](WannabeApplication.md)|  | |

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
| **200** | addApplication |  -  |

<a id="postSelfApplicationsAppIdAddons"></a>
# **postSelfApplicationsAppIdAddons**
> postSelfApplicationsAppIdAddons(appId, body)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String appId = "appId_example"; // String | 
    Body body = new Body(); // Body | 
    try {
      apiInstance.postSelfApplicationsAppIdAddons(appId, body);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#postSelfApplicationsAppIdAddons");
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

<a id="postSelfApplicationsAppIdInstances"></a>
# **postSelfApplicationsAppIdInstances**
> postSelfApplicationsAppIdInstances(appId, commit)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String appId = "appId_example"; // String | 
    String commit = "commit_example"; // String | 
    try {
      apiInstance.postSelfApplicationsAppIdInstances(appId, commit);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#postSelfApplicationsAppIdInstances");
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

<a id="postSelfConsumers"></a>
# **postSelfConsumers**
> postSelfConsumers(wannabeConsumer)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    WannabeConsumer wannabeConsumer = new WannabeConsumer(); // WannabeConsumer | 
    try {
      apiInstance.postSelfConsumers(wannabeConsumer);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#postSelfConsumers");
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

<a id="postSelfPaymentsBillings"></a>
# **postSelfPaymentsBillings**
> postSelfPaymentsBillings()



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    try {
      apiInstance.postSelfPaymentsBillings();
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#postSelfPaymentsBillings");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
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

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | buyDrops |  -  |

<a id="postSelfPaymentsMethods"></a>
# **postSelfPaymentsMethods**
> postSelfPaymentsMethods()



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    try {
      apiInstance.postSelfPaymentsMethods();
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#postSelfPaymentsMethods");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
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

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | addUserMethod |  -  |

<a id="postUsers"></a>
# **postUsers**
> postUsers(wannabeUser, invitationKey, addonBetaInvitationKey, email, pass, urlNext, terms)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    WannabeUser wannabeUser = new WannabeUser(); // WannabeUser | 
    String invitationKey = "invitationKey_example"; // String | 
    String addonBetaInvitationKey = "addonBetaInvitationKey_example"; // String | 
    String email = "email_example"; // String | 
    String pass = "pass_example"; // String | 
    String urlNext = "urlNext_example"; // String | 
    String terms = "terms_example"; // String | 
    try {
      apiInstance.postUsers(wannabeUser, invitationKey, addonBetaInvitationKey, email, pass, urlNext, terms);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#postUsers");
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
| **wannabeUser** | [**WannabeUser**](WannabeUser.md)|  | |
| **invitationKey** | **String**|  | [optional] |
| **addonBetaInvitationKey** | **String**|  | [optional] |
| **email** | **String**|  | [optional] |
| **pass** | **String**|  | [optional] |
| **urlNext** | **String**|  | [optional] |
| **terms** | **String**|  | [optional] |

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
| **200** | createUser createUserFromForm |  -  |

<a id="postVendorBillingOwnerId"></a>
# **postVendorBillingOwnerId**
> postVendorBillingOwnerId(addonId, wannabeAddonBilling)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String addonId = "addonId_example"; // String | 
    WannabeAddonBilling wannabeAddonBilling = new WannabeAddonBilling(); // WannabeAddonBilling | 
    try {
      apiInstance.postVendorBillingOwnerId(addonId, wannabeAddonBilling);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#postVendorBillingOwnerId");
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
| **addonId** | **String**|  | |
| **wannabeAddonBilling** | [**WannabeAddonBilling**](WannabeAddonBilling.md)|  | |

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

<a id="productsAddonprovidersProviderIdVersionsGet"></a>
# **productsAddonprovidersProviderIdVersionsGet**
> productsAddonprovidersProviderIdVersionsGet(providerId)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String providerId = "providerId_example"; // String | 
    try {
      apiInstance.productsAddonprovidersProviderIdVersionsGet(providerId);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#productsAddonprovidersProviderIdVersionsGet");
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

<a id="productsMfaKindsGet"></a>
# **productsMfaKindsGet**
> productsMfaKindsGet()



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    try {
      apiInstance.productsMfaKindsGet();
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#productsMfaKindsGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
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

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Status 200 |  -  |

<a id="putOrganisationsId"></a>
# **putOrganisationsId**
> Organisation putOrganisationsId(id, wannabeOrganisation)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String id = "id_example"; // String | 
    WannabeOrganisation wannabeOrganisation = new WannabeOrganisation(); // WannabeOrganisation | 
    try {
      Organisation result = apiInstance.putOrganisationsId(id, wannabeOrganisation);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#putOrganisationsId");
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

<a id="putOrganisationsIdAddonprovidersProviderId"></a>
# **putOrganisationsIdAddonprovidersProviderId**
> Provider putOrganisationsIdAddonprovidersProviderId(id, providerId, wannabeAddonProvider)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String id = "id_example"; // String | 
    String providerId = "providerId_example"; // String | 
    WannabeAddonProvider wannabeAddonProvider = new WannabeAddonProvider(); // WannabeAddonProvider | 
    try {
      Provider result = apiInstance.putOrganisationsIdAddonprovidersProviderId(id, providerId, wannabeAddonProvider);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#putOrganisationsIdAddonprovidersProviderId");
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

<a id="putOrganisationsIdAddonprovidersProviderIdPlansPlanId"></a>
# **putOrganisationsIdAddonprovidersProviderIdPlansPlanId**
> Plan putOrganisationsIdAddonprovidersProviderIdPlansPlanId(id, providerId, planId, wannabePlan)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String id = "id_example"; // String | 
    String providerId = "providerId_example"; // String | 
    String planId = "planId_example"; // String | 
    WannabePlan wannabePlan = new WannabePlan(); // WannabePlan | 
    try {
      Plan result = apiInstance.putOrganisationsIdAddonprovidersProviderIdPlansPlanId(id, providerId, planId, wannabePlan);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#putOrganisationsIdAddonprovidersProviderIdPlansPlanId");
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

<a id="putOrganisationsIdAddonprovidersProviderIdPlansPlanIdFeaturesFeatureName"></a>
# **putOrganisationsIdAddonprovidersProviderIdPlansPlanIdFeaturesFeatureName**
> putOrganisationsIdAddonprovidersProviderIdPlansPlanIdFeaturesFeatureName(id, featureName, providerId, planId, wannabePlanFeature)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String id = "id_example"; // String | 
    String featureName = "featureName_example"; // String | 
    String providerId = "providerId_example"; // String | 
    String planId = "planId_example"; // String | 
    WannabePlanFeature wannabePlanFeature = new WannabePlanFeature(); // WannabePlanFeature | 
    try {
      apiInstance.putOrganisationsIdAddonprovidersProviderIdPlansPlanIdFeaturesFeatureName(id, featureName, providerId, planId, wannabePlanFeature);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#putOrganisationsIdAddonprovidersProviderIdPlansPlanIdFeaturesFeatureName");
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

<a id="putOrganisationsIdAddonsAddonId"></a>
# **putOrganisationsIdAddonsAddonId**
> Addon putOrganisationsIdAddonsAddonId(id, addonId, wannabeAddon)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String id = "id_example"; // String | 
    String addonId = "addonId_example"; // String | 
    WannabeAddon wannabeAddon = new WannabeAddon(); // WannabeAddon | 
    try {
      Addon result = apiInstance.putOrganisationsIdAddonsAddonId(id, addonId, wannabeAddon);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#putOrganisationsIdAddonsAddonId");
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

<a id="putOrganisationsIdAddonsAddonIdTagsTag"></a>
# **putOrganisationsIdAddonsAddonIdTagsTag**
> putOrganisationsIdAddonsAddonIdTagsTag(id, tag, addonId, body)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String id = "id_example"; // String | 
    String tag = "tag_example"; // String | 
    String addonId = "addonId_example"; // String | 
    Body body = new Body(); // Body | 
    try {
      apiInstance.putOrganisationsIdAddonsAddonIdTagsTag(id, tag, addonId, body);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#putOrganisationsIdAddonsAddonIdTagsTag");
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

<a id="putOrganisationsIdApplicationsAppId"></a>
# **putOrganisationsIdApplicationsAppId**
> Application putOrganisationsIdApplicationsAppId(id, appId, wannabeApplication)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String id = "id_example"; // String | 
    String appId = "appId_example"; // String | 
    WannabeApplication wannabeApplication = new WannabeApplication(); // WannabeApplication | 
    try {
      Application result = apiInstance.putOrganisationsIdApplicationsAppId(id, appId, wannabeApplication);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#putOrganisationsIdApplicationsAppId");
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

<a id="putOrganisationsIdApplicationsAppIdDependenciesDependencyId"></a>
# **putOrganisationsIdApplicationsAppIdDependenciesDependencyId**
> putOrganisationsIdApplicationsAppIdDependenciesDependencyId(dependencyId, appId, id, body)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String dependencyId = "dependencyId_example"; // String | 
    String appId = "appId_example"; // String | 
    String id = "id_example"; // String | 
    Body body = new Body(); // Body | 
    try {
      apiInstance.putOrganisationsIdApplicationsAppIdDependenciesDependencyId(dependencyId, appId, id, body);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#putOrganisationsIdApplicationsAppIdDependenciesDependencyId");
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

<a id="putOrganisationsIdApplicationsAppIdEnv"></a>
# **putOrganisationsIdApplicationsAppIdEnv**
> ListEnv putOrganisationsIdApplicationsAppIdEnv(id, appId, wannabeEnv)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String id = "id_example"; // String | 
    String appId = "appId_example"; // String | 
    WannabeEnv wannabeEnv = new WannabeEnv(); // WannabeEnv | 
    try {
      ListEnv result = apiInstance.putOrganisationsIdApplicationsAppIdEnv(id, appId, wannabeEnv);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#putOrganisationsIdApplicationsAppIdEnv");
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

<a id="putOrganisationsIdApplicationsAppIdEnvEnvName"></a>
# **putOrganisationsIdApplicationsAppIdEnvEnvName**
> ListEnv putOrganisationsIdApplicationsAppIdEnvEnvName(id, appId, envName, wannabeEnv)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String id = "id_example"; // String | 
    String appId = "appId_example"; // String | 
    String envName = "envName_example"; // String | 
    WannabeEnv wannabeEnv = new WannabeEnv(); // WannabeEnv | 
    try {
      ListEnv result = apiInstance.putOrganisationsIdApplicationsAppIdEnvEnvName(id, appId, envName, wannabeEnv);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#putOrganisationsIdApplicationsAppIdEnvEnvName");
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

<a id="putOrganisationsIdApplicationsAppIdTagsTag"></a>
# **putOrganisationsIdApplicationsAppIdTagsTag**
> putOrganisationsIdApplicationsAppIdTagsTag(id, appId, tag, body)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String id = "id_example"; // String | 
    String appId = "appId_example"; // String | 
    String tag = "tag_example"; // String | 
    Body body = new Body(); // Body | 
    try {
      apiInstance.putOrganisationsIdApplicationsAppIdTagsTag(id, appId, tag, body);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#putOrganisationsIdApplicationsAppIdTagsTag");
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

<a id="putOrganisationsIdApplicationsAppIdVhostsDomain"></a>
# **putOrganisationsIdApplicationsAppIdVhostsDomain**
> putOrganisationsIdApplicationsAppIdVhostsDomain(id, appId, domain, vhost)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String id = "id_example"; // String | 
    String appId = "appId_example"; // String | 
    String domain = "domain_example"; // String | 
    Vhost vhost = new Vhost(); // Vhost | 
    try {
      apiInstance.putOrganisationsIdApplicationsAppIdVhostsDomain(id, appId, domain, vhost);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#putOrganisationsIdApplicationsAppIdVhostsDomain");
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

<a id="putOrganisationsIdApplicationsAppIdVhostsFavourite"></a>
# **putOrganisationsIdApplicationsAppIdVhostsFavourite**
> putOrganisationsIdApplicationsAppIdVhostsFavourite(id, appId, vhost)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String id = "id_example"; // String | 
    String appId = "appId_example"; // String | 
    Vhost vhost = new Vhost(); // Vhost | 
    try {
      apiInstance.putOrganisationsIdApplicationsAppIdVhostsFavourite(id, appId, vhost);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#putOrganisationsIdApplicationsAppIdVhostsFavourite");
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

<a id="putOrganisationsIdAvatar"></a>
# **putOrganisationsIdAvatar**
> putOrganisationsIdAvatar(id)



If you want to upload an image from your computer, send the image in the body of the request without anything else.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String id = "id_example"; // String | 
    try {
      apiInstance.putOrganisationsIdAvatar(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#putOrganisationsIdAvatar");
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

<a id="putOrganisationsIdConsumersKey"></a>
# **putOrganisationsIdConsumersKey**
> putOrganisationsIdConsumersKey(id, key, wannabeConsumer)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String id = "id_example"; // String | 
    String key = "key_example"; // String | 
    WannabeConsumer wannabeConsumer = new WannabeConsumer(); // WannabeConsumer | 
    try {
      apiInstance.putOrganisationsIdConsumersKey(id, key, wannabeConsumer);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#putOrganisationsIdConsumersKey");
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

<a id="putOrganisationsIdMembersUserId"></a>
# **putOrganisationsIdMembersUserId**
> putOrganisationsIdMembersUserId(id, userId, body)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String id = "id_example"; // String | 
    String userId = "userId_example"; // String | 
    Schema2 body = new Schema2(); // Schema2 | 
    try {
      apiInstance.putOrganisationsIdMembersUserId(id, userId, body);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#putOrganisationsIdMembersUserId");
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

<a id="putOrganisationsIdPaymentsBillingsBid"></a>
# **putOrganisationsIdPaymentsBillingsBid**
> putOrganisationsIdPaymentsBillingsBid(id, bid)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String id = "id_example"; // String | 
    String bid = "bid_example"; // String | 
    try {
      apiInstance.putOrganisationsIdPaymentsBillingsBid(id, bid);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#putOrganisationsIdPaymentsBillingsBid");
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

<a id="putSelf"></a>
# **putSelf**
> putSelf(wannabeUser)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    WannabeUser wannabeUser = new WannabeUser(); // WannabeUser | 
    try {
      apiInstance.putSelf(wannabeUser);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#putSelf");
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
| **wannabeUser** | [**WannabeUser**](WannabeUser.md)|  | |

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
| **200** | editUser |  -  |

<a id="putSelfAddonsAddonId"></a>
# **putSelfAddonsAddonId**
> putSelfAddonsAddonId(addonId, wannabeAddon)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String addonId = "addonId_example"; // String | 
    WannabeAddon wannabeAddon = new WannabeAddon(); // WannabeAddon | 
    try {
      apiInstance.putSelfAddonsAddonId(addonId, wannabeAddon);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#putSelfAddonsAddonId");
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
| **addonId** | **String**|  | |
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
| **200** | Update addon informations |  -  |

<a id="putSelfAddonsAddonIdPlan"></a>
# **putSelfAddonsAddonIdPlan**
> putSelfAddonsAddonIdPlan(addonId, wannabePlan)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String addonId = "addonId_example"; // String | 
    WannabePlan wannabePlan = new WannabePlan(); // WannabePlan | 
    try {
      apiInstance.putSelfAddonsAddonIdPlan(addonId, wannabePlan);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#putSelfAddonsAddonIdPlan");
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
| **addonId** | **String**|  | |
| **wannabePlan** | [**WannabePlan**](WannabePlan.md)|  | |

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
| **200** | Update plan of an add-on. |  -  |

<a id="putSelfAddonsAddonIdTagsTag"></a>
# **putSelfAddonsAddonIdTagsTag**
> putSelfAddonsAddonIdTagsTag(tag, addonId, body)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String tag = "tag_example"; // String | 
    String addonId = "addonId_example"; // String | 
    Body body = new Body(); // Body | 
    try {
      apiInstance.putSelfAddonsAddonIdTagsTag(tag, addonId, body);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#putSelfAddonsAddonIdTagsTag");
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

<a id="putSelfApplicationsAppId"></a>
# **putSelfApplicationsAppId**
> putSelfApplicationsAppId(appId, wannabeApplication)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String appId = "appId_example"; // String | 
    WannabeApplication wannabeApplication = new WannabeApplication(); // WannabeApplication | 
    try {
      apiInstance.putSelfApplicationsAppId(appId, wannabeApplication);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#putSelfApplicationsAppId");
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
| **wannabeApplication** | [**WannabeApplication**](WannabeApplication.md)|  | |

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
| **200** | editApplication |  -  |

<a id="putSelfApplicationsAppIdEnv"></a>
# **putSelfApplicationsAppIdEnv**
> putSelfApplicationsAppIdEnv(appId, wannabeEnv)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String appId = "appId_example"; // String | 
    WannabeEnv wannabeEnv = new WannabeEnv(); // WannabeEnv | 
    try {
      apiInstance.putSelfApplicationsAppIdEnv(appId, wannabeEnv);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#putSelfApplicationsAppIdEnv");
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
| **wannabeEnv** | [**WannabeEnv**](WannabeEnv.md)|  | |

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
| **200** | editApplicationEnvironment |  -  |

<a id="putSelfApplicationsAppIdEnvEnvName"></a>
# **putSelfApplicationsAppIdEnvEnvName**
> putSelfApplicationsAppIdEnvEnvName(appId, envName, wannabeEnv)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String appId = "appId_example"; // String | 
    String envName = "envName_example"; // String | 
    WannabeEnv wannabeEnv = new WannabeEnv(); // WannabeEnv | 
    try {
      apiInstance.putSelfApplicationsAppIdEnvEnvName(appId, envName, wannabeEnv);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#putSelfApplicationsAppIdEnvEnvName");
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
| **envName** | **String**|  | |
| **wannabeEnv** | [**WannabeEnv**](WannabeEnv.md)|  | |

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
| **200** | editApplicationEnv |  -  |

<a id="putSelfApplicationsAppIdTagsTag"></a>
# **putSelfApplicationsAppIdTagsTag**
> putSelfApplicationsAppIdTagsTag(appId, tag, body)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String appId = "appId_example"; // String | 
    String tag = "tag_example"; // String | 
    Body body = new Body(); // Body | 
    try {
      apiInstance.putSelfApplicationsAppIdTagsTag(appId, tag, body);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#putSelfApplicationsAppIdTagsTag");
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

<a id="putSelfApplicationsAppIdVhostsDomain"></a>
# **putSelfApplicationsAppIdVhostsDomain**
> putSelfApplicationsAppIdVhostsDomain(appId, domain, vhost)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String appId = "appId_example"; // String | 
    String domain = "domain_example"; // String | 
    Vhost vhost = new Vhost(); // Vhost | 
    try {
      apiInstance.putSelfApplicationsAppIdVhostsDomain(appId, domain, vhost);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#putSelfApplicationsAppIdVhostsDomain");
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

<a id="putSelfApplicationsAppIdVhostsFavourite"></a>
# **putSelfApplicationsAppIdVhostsFavourite**
> putSelfApplicationsAppIdVhostsFavourite(appId, vhost)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String appId = "appId_example"; // String | 
    Vhost vhost = new Vhost(); // Vhost | 
    try {
      apiInstance.putSelfApplicationsAppIdVhostsFavourite(appId, vhost);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#putSelfApplicationsAppIdVhostsFavourite");
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

<a id="putSelfAvatar"></a>
# **putSelfAvatar**
> putSelfAvatar(avatar)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    Avatar avatar = new Avatar(); // Avatar | 
    try {
      apiInstance.putSelfAvatar(avatar);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#putSelfAvatar");
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
| **avatar** | [**Avatar**](Avatar.md)|  | |

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
| **200** | setUserAvatar setUserAvatarFromSource |  -  |

<a id="putSelfChangePassword"></a>
# **putSelfChangePassword**
> ChangePassword putSelfChangePassword()



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    try {
      ChangePassword result = apiInstance.putSelfChangePassword();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#putSelfChangePassword");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
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

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | changeUserPassword |  -  |

<a id="putSelfConsumersKey"></a>
# **putSelfConsumersKey**
> putSelfConsumersKey(key, wannabeConsumer)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String key = "key_example"; // String | 
    WannabeConsumer wannabeConsumer = new WannabeConsumer(); // WannabeConsumer | 
    try {
      apiInstance.putSelfConsumersKey(key, wannabeConsumer);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#putSelfConsumersKey");
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
| **200** | PUT same consumer data as in POST. |  -  |

<a id="putSelfEmailsEmail"></a>
# **putSelfEmailsEmail**
> putSelfEmailsEmail(email, body)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String email = "email_example"; // String | 
    Body body = new Body(); // Body | 
    try {
      apiInstance.putSelfEmailsEmail(email, body);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#putSelfEmailsEmail");
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
| **email** | **String**|  | |
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
| **200** | addEmailAddress |  -  |

<a id="putSelfKeysKey"></a>
# **putSelfKeysKey**
> putSelfKeysKey(key, body)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String key = "key_example"; // String | 
    Body body = new Body(); // Body | 
    try {
      apiInstance.putSelfKeysKey(key, body);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#putSelfKeysKey");
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
| **key** | **String**|  | |
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
| **200** | addSshKey |  -  |

<a id="putSelfPaymentsBillingsBid"></a>
# **putSelfPaymentsBillingsBid**
> putSelfPaymentsBillingsBid(bid)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String bid = "bid_example"; // String | 
    try {
      apiInstance.putSelfPaymentsBillingsBid(bid);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#putSelfPaymentsBillingsBid");
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

<a id="putVendorAppsAddonId"></a>
# **putVendorAppsAddonId**
> putVendorAppsAddonId(addonId)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String addonId = "addonId_example"; // String | 
    try {
      apiInstance.putVendorAppsAddonId(addonId);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#putVendorAppsAddonId");
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
| **200** | editApplicationConfiguration |  -  |

<a id="selfAddonsPreordersPost"></a>
# **selfAddonsPreordersPost**
> selfAddonsPreordersPost(wannabeAddon)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    WannabeAddon wannabeAddon = new WannabeAddon(); // WannabeAddon | 
    try {
      apiInstance.selfAddonsPreordersPost(wannabeAddon);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#selfAddonsPreordersPost");
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

<a id="selfApplicationsAppIdBranchPut"></a>
# **selfApplicationsAppIdBranchPut**
> selfApplicationsAppIdBranchPut(appId)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String appId = "appId_example"; // String | 
    try {
      apiInstance.selfApplicationsAppIdBranchPut(appId);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#selfApplicationsAppIdBranchPut");
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

<a id="selfApplicationsAppIdBranchesGet"></a>
# **selfApplicationsAppIdBranchesGet**
> selfApplicationsAppIdBranchesGet(appId)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String appId = "appId_example"; // String | 
    try {
      apiInstance.selfApplicationsAppIdBranchesGet(appId);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#selfApplicationsAppIdBranchesGet");
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

<a id="selfApplicationsAppIdBuildflavorPut"></a>
# **selfApplicationsAppIdBuildflavorPut**
> selfApplicationsAppIdBuildflavorPut(appId)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String appId = "appId_example"; // String | 
    try {
      apiInstance.selfApplicationsAppIdBuildflavorPut(appId);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#selfApplicationsAppIdBuildflavorPut");
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

<a id="selfApplicationsAppIdDependenciesEnvGet"></a>
# **selfApplicationsAppIdDependenciesEnvGet**
> List&lt;LinkedAppEnv&gt; selfApplicationsAppIdDependenciesEnvGet(appId)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String appId = "appId_example"; // String | 
    try {
      List<LinkedAppEnv> result = apiInstance.selfApplicationsAppIdDependenciesEnvGet(appId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#selfApplicationsAppIdDependenciesEnvGet");
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

<a id="selfApplicationsAppIdDeploymentsDeploymentIdGet"></a>
# **selfApplicationsAppIdDeploymentsDeploymentIdGet**
> selfApplicationsAppIdDeploymentsDeploymentIdGet(appId, deploymentId)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String appId = "appId_example"; // String | 
    String deploymentId = "deploymentId_example"; // String | 
    try {
      apiInstance.selfApplicationsAppIdDeploymentsDeploymentIdGet(appId, deploymentId);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#selfApplicationsAppIdDeploymentsDeploymentIdGet");
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

<a id="selfApplicationsAppIdExposedEnvGet"></a>
# **selfApplicationsAppIdExposedEnvGet**
> selfApplicationsAppIdExposedEnvGet(appId)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String appId = "appId_example"; // String | 
    try {
      apiInstance.selfApplicationsAppIdExposedEnvGet(appId);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#selfApplicationsAppIdExposedEnvGet");
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

<a id="selfApplicationsAppIdExposedEnvPut"></a>
# **selfApplicationsAppIdExposedEnvPut**
> selfApplicationsAppIdExposedEnvPut(appId)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String appId = "appId_example"; // String | 
    try {
      apiInstance.selfApplicationsAppIdExposedEnvPut(appId);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#selfApplicationsAppIdExposedEnvPut");
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

<a id="selfApplicationsAppIdInstancesInstanceIdGet"></a>
# **selfApplicationsAppIdInstancesInstanceIdGet**
> selfApplicationsAppIdInstancesInstanceIdGet(instanceId, appId)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String instanceId = "instanceId_example"; // String | 
    String appId = "appId_example"; // String | 
    try {
      apiInstance.selfApplicationsAppIdInstancesInstanceIdGet(instanceId, appId);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#selfApplicationsAppIdInstancesInstanceIdGet");
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

<a id="selfCliTokensGet"></a>
# **selfCliTokensGet**
> selfCliTokensGet(cliToken)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String cliToken = "cliToken_example"; // String | 
    try {
      apiInstance.selfCliTokensGet(cliToken);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#selfCliTokensGet");
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
| **cliToken** | **String**|  | [optional] |

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

<a id="selfMfaKindBackupcodesGet"></a>
# **selfMfaKindBackupcodesGet**
> selfMfaKindBackupcodesGet(kind)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String kind = "kind_example"; // String | 
    try {
      apiInstance.selfMfaKindBackupcodesGet(kind);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#selfMfaKindBackupcodesGet");
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
| **kind** | **String**|  | |

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

<a id="selfMfaKindConfirmationPost"></a>
# **selfMfaKindConfirmationPost**
> selfMfaKindConfirmationPost(kind)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String kind = "kind_example"; // String | 
    try {
      apiInstance.selfMfaKindConfirmationPost(kind);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#selfMfaKindConfirmationPost");
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
| **kind** | **String**|  | |

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

<a id="selfMfaKindDelete"></a>
# **selfMfaKindDelete**
> selfMfaKindDelete(kind)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String kind = "kind_example"; // String | 
    try {
      apiInstance.selfMfaKindDelete(kind);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#selfMfaKindDelete");
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
| **kind** | **String**|  | |

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

<a id="selfMfaKindPost"></a>
# **selfMfaKindPost**
> selfMfaKindPost(kind)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String kind = "kind_example"; // String | 
    try {
      apiInstance.selfMfaKindPost(kind);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#selfMfaKindPost");
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
| **kind** | **String**|  | |

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

<a id="selfMfaKindPut"></a>
# **selfMfaKindPut**
> selfMfaKindPut(kind)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String kind = "kind_example"; // String | 
    try {
      apiInstance.selfMfaKindPut(kind);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#selfMfaKindPut");
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
| **kind** | **String**|  | |

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

<a id="selfPaymentsMethodsDefaultGet"></a>
# **selfPaymentsMethodsDefaultGet**
> selfPaymentsMethodsDefaultGet()



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    try {
      apiInstance.selfPaymentsMethodsDefaultGet();
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#selfPaymentsMethodsDefaultGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
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

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Status 200 |  -  |

<a id="selfPaymentsMethodsDefaultPut"></a>
# **selfPaymentsMethodsDefaultPut**
> selfPaymentsMethodsDefaultPut()



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    try {
      apiInstance.selfPaymentsMethodsDefaultPut();
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#selfPaymentsMethodsDefaultPut");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
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

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Status 200 |  -  |

<a id="selfPaymentsMonthlyinvoiceGet"></a>
# **selfPaymentsMonthlyinvoiceGet**
> selfPaymentsMonthlyinvoiceGet()



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    try {
      apiInstance.selfPaymentsMonthlyinvoiceGet();
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#selfPaymentsMonthlyinvoiceGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
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

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Status 200 |  -  |

<a id="selfPaymentsMonthlyinvoiceMaxcreditPut"></a>
# **selfPaymentsMonthlyinvoiceMaxcreditPut**
> selfPaymentsMonthlyinvoiceMaxcreditPut()



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    try {
      apiInstance.selfPaymentsMonthlyinvoiceMaxcreditPut();
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#selfPaymentsMonthlyinvoiceMaxcreditPut");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
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

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Status 200 |  -  |

<a id="selfPaymentsRecurringGet"></a>
# **selfPaymentsRecurringGet**
> selfPaymentsRecurringGet()



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    try {
      apiInstance.selfPaymentsRecurringGet();
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#selfPaymentsRecurringGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
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

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Status 200 |  -  |

<a id="selfPaymentsTokensStripeGet"></a>
# **selfPaymentsTokensStripeGet**
> selfPaymentsTokensStripeGet()



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    try {
      apiInstance.selfPaymentsTokensStripeGet();
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#selfPaymentsTokensStripeGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
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

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Status 200 |  -  |

<a id="updateConfigProviderEnv"></a>
# **updateConfigProviderEnv**
> List&lt;Object&gt; updateConfigProviderEnv(configurationProviderId, requestBody)

Update provider&#39;s addon environment

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String configurationProviderId = "configurationProviderId_example"; // String | Automatically added
    List<Object> requestBody = null; // List<Object> | 
    try {
      List<Object> result = apiInstance.updateConfigProviderEnv(configurationProviderId, requestBody);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#updateConfigProviderEnv");
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
| **configurationProviderId** | **String**| Automatically added | |
| **requestBody** | [**List&lt;Object&gt;**](Object.md)|  | |

### Return type

**List&lt;Object&gt;**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | updated config providers environment variables |  -  |
| **401** |  |  -  |

<a id="v3LogsAppIdDrainsGet"></a>
# **v3LogsAppIdDrainsGet**
> v3LogsAppIdDrainsGet(appId)



Fetch the logs drains for a given application

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String appId = "appId_example"; // String | Automatically added
    try {
      apiInstance.v3LogsAppIdDrainsGet(appId);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#v3LogsAppIdDrainsGet");
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
| **appId** | **String**| Automatically added | |

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
| **0** | &lt;No description&gt; |  -  |

<a id="v3LogsAppIdDrainsIdOrUrlDelete"></a>
# **v3LogsAppIdDrainsIdOrUrlDelete**
> v3LogsAppIdDrainsIdOrUrlDelete(appId)



Delete the logs drain by id or url for a given application

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String appId = "appId_example"; // String | Automatically added
    try {
      apiInstance.v3LogsAppIdDrainsIdOrUrlDelete(appId);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#v3LogsAppIdDrainsIdOrUrlDelete");
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
| **appId** | **String**| Automatically added | |

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
| **0** | &lt;No description&gt; |  -  |

<a id="v3LogsAppIdDrainsIdOrUrlGet"></a>
# **v3LogsAppIdDrainsIdOrUrlGet**
> v3LogsAppIdDrainsIdOrUrlGet(appId)



Fetch the logs drain by id or url for a given application

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String appId = "appId_example"; // String | Automatically added
    try {
      apiInstance.v3LogsAppIdDrainsIdOrUrlGet(appId);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#v3LogsAppIdDrainsIdOrUrlGet");
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
| **appId** | **String**| Automatically added | |

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
| **0** | &lt;No description&gt; |  -  |

<a id="v3LogsAppIdDrainsPost"></a>
# **v3LogsAppIdDrainsPost**
> v3LogsAppIdDrainsPost(appId)



Add a log drain for a given application

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String appId = "appId_example"; // String | Automatically added
    try {
      apiInstance.v3LogsAppIdDrainsPost(appId);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#v3LogsAppIdDrainsPost");
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
| **appId** | **String**| Automatically added | |

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
| **0** | &lt;No description&gt; |  -  |

<a id="v3LogsAppIdGet"></a>
# **v3LogsAppIdGet**
> v3LogsAppIdGet(appId)



Fetch the logs for a given application

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String appId = "appId_example"; // String | Automatically added
    try {
      apiInstance.v3LogsAppIdGet(appId);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#v3LogsAppIdGet");
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
| **appId** | **String**| Automatically added | |

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
| **0** | &lt;No description&gt; |  -  |

<a id="v3LogsAppIdLogsChunkedGet"></a>
# **v3LogsAppIdLogsChunkedGet**
> v3LogsAppIdLogsChunkedGet(appId)



Retrieve logs as they come through a chunked, never-ending response

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String appId = "appId_example"; // String | Automatically added
    try {
      apiInstance.v3LogsAppIdLogsChunkedGet(appId);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#v3LogsAppIdLogsChunkedGet");
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
| **appId** | **String**| Automatically added | |

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
| **0** | &lt;No description&gt; |  -  |

<a id="v3LogsAppIdLogsSocketGet"></a>
# **v3LogsAppIdLogsSocketGet**
> v3LogsAppIdLogsSocketGet(appId)



Retrieve logs as they come through a websocket connection. To have authorization, you have to send a &#x60;{ \&quot;message_type\&quot;: \&quot;oauth\&quot;, \&quot;authorization\&quot;: \&quot;oauth authorization string\&quot; }&#x60; message

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String appId = "appId_example"; // String | Automatically added
    try {
      apiInstance.v3LogsAppIdLogsSocketGet(appId);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#v3LogsAppIdLogsSocketGet");
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
| **appId** | **String**| Automatically added | |

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
| **0** | &lt;No description&gt; |  -  |

<a id="vendorAddonsPost"></a>
# **vendorAddonsPost**
> vendorAddonsPost()



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    try {
      apiInstance.vendorAddonsPost();
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#vendorAddonsPost");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
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

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Status 200 |  -  |

<a id="vendorAppsAddonIdLogscollectorGet"></a>
# **vendorAppsAddonIdLogscollectorGet**
> vendorAppsAddonIdLogscollectorGet(addonId)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String addonId = "addonId_example"; // String | 
    try {
      apiInstance.vendorAppsAddonIdLogscollectorGet(addonId);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#vendorAppsAddonIdLogscollectorGet");
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
| **200** | Status 200 |  -  |

<a id="vendorAppsAddonIdMigrationCallbackPut"></a>
# **vendorAppsAddonIdMigrationCallbackPut**
> vendorAppsAddonIdMigrationCallbackPut(addonId, planId, region)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AllApi apiInstance = new AllApi(defaultClient);
    String addonId = "addonId_example"; // String | 
    String planId = "planId_example"; // String | 
    String region = "region_example"; // String | 
    try {
      apiInstance.vendorAppsAddonIdMigrationCallbackPut(addonId, planId, region);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#vendorAppsAddonIdMigrationCallbackPut");
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
| **addonId** | **String**|  | |
| **planId** | **String**|  | [optional] |
| **region** | **String**|  | [optional] |

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

