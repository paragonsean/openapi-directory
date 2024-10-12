

# GoogleCloudIdentitytoolkitAdminV2ProviderConfig

ProviderConfig describes the supported MFA providers along with their configurations.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**state** | [**StateEnum**](#StateEnum) | Describes the state of the MultiFactor Authentication type. |  [optional] |
|**totpProviderConfig** | [**GoogleCloudIdentitytoolkitAdminV2TotpMfaProviderConfig**](GoogleCloudIdentitytoolkitAdminV2TotpMfaProviderConfig.md) |  |  [optional] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| MFA_STATE_UNSPECIFIED | &quot;MFA_STATE_UNSPECIFIED&quot; |
| DISABLED | &quot;DISABLED&quot; |
| ENABLED | &quot;ENABLED&quot; |
| MANDATORY | &quot;MANDATORY&quot; |



