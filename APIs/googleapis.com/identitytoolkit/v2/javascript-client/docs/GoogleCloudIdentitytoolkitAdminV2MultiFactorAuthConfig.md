# IdentityToolkitApi.GoogleCloudIdentitytoolkitAdminV2MultiFactorAuthConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabledProviders** | **[String]** | A list of usable second factors for this project. | [optional] 
**providerConfigs** | [**[GoogleCloudIdentitytoolkitAdminV2ProviderConfig]**](GoogleCloudIdentitytoolkitAdminV2ProviderConfig.md) | A list of usable second factors for this project along with their configurations. This field does not support phone based MFA, for that use the &#39;enabled_providers&#39; field. | [optional] 
**state** | **String** | Whether MultiFactor Authentication has been enabled for this project. | [optional] 



## Enum: [EnabledProvidersEnum]


* `PROVIDER_UNSPECIFIED` (value: `"PROVIDER_UNSPECIFIED"`)

* `PHONE_SMS` (value: `"PHONE_SMS"`)





## Enum: StateEnum


* `STATE_UNSPECIFIED` (value: `"STATE_UNSPECIFIED"`)

* `DISABLED` (value: `"DISABLED"`)

* `ENABLED` (value: `"ENABLED"`)

* `MANDATORY` (value: `"MANDATORY"`)




