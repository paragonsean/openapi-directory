

# ExpressRouteLinkMacSecConfig

ExpressRouteLink Mac Security Configuration.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cakSecretIdentifier** | **String** | Keyvault Secret Identifier URL containing Mac security CAK key. |  [optional] |
|**cipher** | [**CipherEnum**](#CipherEnum) | Mac security cipher. |  [optional] |
|**cknSecretIdentifier** | **String** | Keyvault Secret Identifier URL containing Mac security CKN key. |  [optional] |



## Enum: CipherEnum

| Name | Value |
|---- | -----|
| _128 | &quot;gcm-aes-128&quot; |
| _256 | &quot;gcm-aes-256&quot; |



