

# CreateInstanceRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**clientToken** | **String** | The idempotency token. |  [optional] |
|**identityManagementType** | [**IdentityManagementTypeEnum**](#IdentityManagementTypeEnum) | The type of identity management for your Amazon Connect users. |  |
|**instanceAlias** | **String** | The name for your instance. |  [optional] |
|**directoryId** | **String** | The identifier for the directory. |  [optional] |
|**inboundCallsEnabled** | **Boolean** | Your contact center handles incoming contacts. |  |
|**outboundCallsEnabled** | **Boolean** | Your contact center allows outbound calls. |  |



## Enum: IdentityManagementTypeEnum

| Name | Value |
|---- | -----|
| SAML | &quot;SAML&quot; |
| CONNECT_MANAGED | &quot;CONNECT_MANAGED&quot; |
| EXISTING_DIRECTORY | &quot;EXISTING_DIRECTORY&quot; |



