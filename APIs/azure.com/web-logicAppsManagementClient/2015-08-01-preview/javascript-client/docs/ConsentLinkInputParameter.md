# LogicAppsManagementClient.ConsentLinkInputParameter

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**objectId** | **String** | AAD OID (user or group) if the principal type is ActiveDirectory.              MSA PUID if the principal type is MicrosoftAccount. | [optional] 
**parameterName** | **String** | Name of the parameter in the connection provider&#39;s oauthSettings | [optional] 
**principalType** | **String** | Principal type | [optional] 
**redirectUrl** | **String** | Name of the parameter in the connection provider&#39;s oauthSettings | [optional] 
**tenantId** | **String** | Tenant Id | [optional] 



## Enum: PrincipalTypeEnum


* `ActiveDirectory` (value: `"ActiveDirectory"`)

* `Connection` (value: `"Connection"`)

* `MicrosoftAccount` (value: `"MicrosoftAccount"`)




