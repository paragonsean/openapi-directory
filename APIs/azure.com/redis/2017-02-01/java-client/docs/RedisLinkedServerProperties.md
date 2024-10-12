

# RedisLinkedServerProperties

Properties of a linked server to be returned in get/put response

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**provisioningState** | **String** | Terminal state of the link between primary and secondary redis cache. |  [optional] [readonly] |
|**linkedRedisCacheId** | **String** | Fully qualified resourceId of the linked redis cache. |  |
|**linkedRedisCacheLocation** | **String** | Location of the linked redis cache. |  |
|**serverRole** | [**ServerRoleEnum**](#ServerRoleEnum) | Role of the linked server. |  |



## Enum: ServerRoleEnum

| Name | Value |
|---- | -----|
| PRIMARY | &quot;Primary&quot; |
| SECONDARY | &quot;Secondary&quot; |



