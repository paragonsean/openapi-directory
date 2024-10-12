

# ApiKVReference

Description of site key vault references.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**details** | **String** |  |  [optional] |
|**identityType** | [**IdentityTypeEnum**](#IdentityTypeEnum) |  |  [optional] |
|**location** | [**LocationEnum**](#LocationEnum) |  |  [optional] |
|**reference** | **String** |  |  [optional] |
|**secretName** | **String** |  |  [optional] |
|**secretVersion** | **String** |  |  [optional] |
|**source** | [**SourceEnum**](#SourceEnum) |  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) |  |  [optional] |
|**vaultName** | **String** |  |  [optional] |



## Enum: IdentityTypeEnum

| Name | Value |
|---- | -----|
| NONE | &quot;None&quot; |
| SYSTEM_ASSIGNED | &quot;SystemAssigned&quot; |
| USER_ASSIGNED | &quot;UserAssigned&quot; |



## Enum: LocationEnum

| Name | Value |
|---- | -----|
| APPLICATION_SETTING | &quot;ApplicationSetting&quot; |



## Enum: SourceEnum

| Name | Value |
|---- | -----|
| KEY_VAULT | &quot;KeyVault&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| INITIALIZED | &quot;Initialized&quot; |
| RESOLVED | &quot;Resolved&quot; |
| INVALID_SYNTAX | &quot;InvalidSyntax&quot; |
| MSI_NOT_ENABLED | &quot;MSINotEnabled&quot; |
| VAULT_NOT_FOUND | &quot;VaultNotFound&quot; |
| SECRET_NOT_FOUND | &quot;SecretNotFound&quot; |
| SECRET_VERSION_NOT_FOUND | &quot;SecretVersionNotFound&quot; |
| ACCESS_TO_KEY_VAULT_DENIED | &quot;AccessToKeyVaultDenied&quot; |
| OTHER_REASONS | &quot;OtherReasons&quot; |



