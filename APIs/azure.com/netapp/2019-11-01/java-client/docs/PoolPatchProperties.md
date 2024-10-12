

# PoolPatchProperties

Patchable pool properties

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**serviceLevel** | [**ServiceLevelEnum**](#ServiceLevelEnum) | The service level of the file system |  [optional] |
|**size** | **Long** | Provisioned size of the pool (in bytes). Allowed values are in 4TiB chunks (value must be multiply of 4398046511104). |  [optional] |



## Enum: ServiceLevelEnum

| Name | Value |
|---- | -----|
| STANDARD | &quot;Standard&quot; |
| PREMIUM | &quot;Premium&quot; |
| ULTRA | &quot;Ultra&quot; |



