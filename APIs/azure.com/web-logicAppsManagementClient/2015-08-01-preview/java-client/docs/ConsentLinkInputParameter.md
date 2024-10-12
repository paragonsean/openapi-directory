

# ConsentLinkInputParameter



## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**objectId** | **String** | AAD OID (user or group) if the principal type is ActiveDirectory.              MSA PUID if the principal type is MicrosoftAccount. |  [optional] |
|**parameterName** | **String** | Name of the parameter in the connection provider&#39;s oauthSettings |  [optional] |
|**principalType** | [**PrincipalTypeEnum**](#PrincipalTypeEnum) | Principal type |  [optional] |
|**redirectUrl** | **String** | Name of the parameter in the connection provider&#39;s oauthSettings |  [optional] |
|**tenantId** | **String** | Tenant Id |  [optional] |



## Enum: PrincipalTypeEnum

| Name | Value |
|---- | -----|
| ACTIVE_DIRECTORY | &quot;ActiveDirectory&quot; |
| CONNECTION | &quot;Connection&quot; |
| MICROSOFT_ACCOUNT | &quot;MicrosoftAccount&quot; |



