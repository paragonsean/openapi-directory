# WebAppsApiClient.ApiKVReference

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**details** | **String** |  | [optional] 
**identityType** | **String** |  | [optional] 
**location** | **String** |  | [optional] 
**reference** | **String** |  | [optional] 
**secretName** | **String** |  | [optional] 
**secretVersion** | **String** |  | [optional] 
**source** | **String** |  | [optional] 
**status** | **String** |  | [optional] 
**vaultName** | **String** |  | [optional] 



## Enum: IdentityTypeEnum


* `None` (value: `"None"`)

* `SystemAssigned` (value: `"SystemAssigned"`)

* `UserAssigned` (value: `"UserAssigned"`)





## Enum: LocationEnum


* `ApplicationSetting` (value: `"ApplicationSetting"`)





## Enum: SourceEnum


* `KeyVault` (value: `"KeyVault"`)





## Enum: StatusEnum


* `Initialized` (value: `"Initialized"`)

* `Resolved` (value: `"Resolved"`)

* `InvalidSyntax` (value: `"InvalidSyntax"`)

* `MSINotEnabled` (value: `"MSINotEnabled"`)

* `VaultNotFound` (value: `"VaultNotFound"`)

* `SecretNotFound` (value: `"SecretNotFound"`)

* `SecretVersionNotFound` (value: `"SecretVersionNotFound"`)

* `AccessToKeyVaultDenied` (value: `"AccessToKeyVaultDenied"`)

* `OtherReasons` (value: `"OtherReasons"`)




