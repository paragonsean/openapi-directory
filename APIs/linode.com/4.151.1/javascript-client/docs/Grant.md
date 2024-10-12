# LinodeApi.Grant

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **Number** | The ID of the entity this grant applies to.  | [optional] 
**label** | **String** | The current label of the entity this grant applies to, for display purposes.  | [optional] [readonly] 
**permissions** | **String** | The level of access this User has to this entity.  If null, this User has no access.  | [optional] 



## Enum: PermissionsEnum


* `only` (value: `"read_only"`)

* `write` (value: `"read_write"`)




