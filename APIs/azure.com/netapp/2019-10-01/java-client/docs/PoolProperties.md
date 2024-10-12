

# PoolProperties

Pool properties

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**poolId** | **String** | UUID v4 used to identify the Pool |  [optional] [readonly] |
|**provisioningState** | **String** | Azure lifecycle management |  [optional] [readonly] |
|**serviceLevel** | [**ServiceLevelEnum**](#ServiceLevelEnum) | The service level of the file system |  |
|**size** | **Long** | Provisioned size of the pool (in bytes). Allowed values are in 4TiB chunks (value must be multiply of 4398046511104). |  |



## Enum: ServiceLevelEnum

| Name | Value |
|---- | -----|
| STANDARD | &quot;Standard&quot; |
| PREMIUM | &quot;Premium&quot; |
| ULTRA | &quot;Ultra&quot; |



