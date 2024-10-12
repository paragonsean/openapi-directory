

# GoogleCloudIdentitytoolkitAdminV2MultiFactorAuthConfig

Options related to MultiFactor Authentication for the project.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**enabledProviders** | [**List&lt;EnabledProvidersEnum&gt;**](#List&lt;EnabledProvidersEnum&gt;) | A list of usable second factors for this project. |  [optional] |
|**providerConfigs** | [**List&lt;GoogleCloudIdentitytoolkitAdminV2ProviderConfig&gt;**](GoogleCloudIdentitytoolkitAdminV2ProviderConfig.md) | A list of usable second factors for this project along with their configurations. This field does not support phone based MFA, for that use the &#39;enabled_providers&#39; field. |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | Whether MultiFactor Authentication has been enabled for this project. |  [optional] |



## Enum: List&lt;EnabledProvidersEnum&gt;

| Name | Value |
|---- | -----|
| PROVIDER_UNSPECIFIED | &quot;PROVIDER_UNSPECIFIED&quot; |
| PHONE_SMS | &quot;PHONE_SMS&quot; |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| DISABLED | &quot;DISABLED&quot; |
| ENABLED | &quot;ENABLED&quot; |
| MANDATORY | &quot;MANDATORY&quot; |



