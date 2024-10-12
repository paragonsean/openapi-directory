

# RedisLinkedServerCreateProperties

Create properties for a linked server

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**linkedRedisCacheId** | **String** | Fully qualified resourceId of the linked redis cache. |  |
|**linkedRedisCacheLocation** | **String** | Location of the linked redis cache. |  |
|**serverRole** | [**ServerRoleEnum**](#ServerRoleEnum) | Role of the linked server. |  |



## Enum: ServerRoleEnum

| Name | Value |
|---- | -----|
| PRIMARY | &quot;Primary&quot; |
| SECONDARY | &quot;Secondary&quot; |



