

# Grant

Represents the level of access a restricted User has to a specific resource on the Account. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **Integer** | The ID of the entity this grant applies to.  |  [optional] |
|**label** | **String** | The current label of the entity this grant applies to, for display purposes.  |  [optional] [readonly] |
|**permissions** | [**PermissionsEnum**](#PermissionsEnum) | The level of access this User has to this entity.  If null, this User has no access.  |  [optional] |



## Enum: PermissionsEnum

| Name | Value |
|---- | -----|
| ONLY | &quot;read_only&quot; |
| WRITE | &quot;read_write&quot; |



