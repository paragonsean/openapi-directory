

# EncryptionIdentity


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**principalId** | **UUID** | The principal identifier associated with the encryption. |  [optional] [readonly] |
|**tenantId** | **UUID** | The tenant identifier associated with the encryption. |  [optional] [readonly] |
|**type** | [**TypeEnum**](#TypeEnum) | The type of encryption being used. Currently the only supported type is &#39;SystemAssigned&#39;. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| SYSTEM_ASSIGNED | &quot;SystemAssigned&quot; |



