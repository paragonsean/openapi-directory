

# RecoveryServicesProviderProperties

Recovery services provider properties.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**allowedScenarios** | **List&lt;String&gt;** | The scenarios allowed on this provider. |  [optional] |
|**authenticationIdentityDetails** | [**IdentityProviderDetails**](IdentityProviderDetails.md) |  |  [optional] |
|**connectionStatus** | **String** | A value indicating whether DRA is responsive. |  [optional] |
|**draIdentifier** | **String** | The DRA Id. |  [optional] |
|**fabricFriendlyName** | **String** | The fabric friendly name. |  [optional] |
|**fabricType** | **String** | Type of the site. |  [optional] |
|**friendlyName** | **String** | Friendly name of the DRA. |  [optional] |
|**healthErrorDetails** | [**List&lt;HealthError&gt;**](HealthError.md) | The recovery services provider health error details. |  [optional] |
|**lastHeartBeat** | **OffsetDateTime** | Time when last heartbeat was sent by the DRA. |  [optional] |
|**protectedItemCount** | **Integer** | Number of protected VMs currently managed by the DRA. |  [optional] |
|**providerVersion** | **String** | The provider version. |  [optional] |
|**providerVersionDetails** | [**VersionDetails**](VersionDetails.md) |  |  [optional] |
|**providerVersionExpiryDate** | **OffsetDateTime** | Expiry date of the version. |  [optional] |
|**providerVersionState** | **String** | DRA version status. |  [optional] |
|**resourceAccessIdentityDetails** | [**IdentityProviderDetails**](IdentityProviderDetails.md) |  |  [optional] |
|**serverVersion** | **String** | The fabric provider. |  [optional] |



