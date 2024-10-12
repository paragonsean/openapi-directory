

# AvailabilityRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**closest** | [**ClosestEnum**](#ClosestEnum) | The direction to find the closest snapshot to the requested timestamp |  [optional] |
|**tag** | **String** | A user-supplied tag, used for collation |  [optional] |
|**timestamp** | **String** | Timestamp requested in ISO 8601 format. The following formats are acceptable: - YYYY - YYYY-MM - YYYY-MM-DD - YYYY-MM-DDTHH:mm:SSz - YYYY-MM-DD:HH:mm+00:00  |  [optional] |
|**url** | **String** | The URL requested |  |



## Enum: ClosestEnum

| Name | Value |
|---- | -----|
| EITHER | &quot;either&quot; |
| AFTER | &quot;after&quot; |
| BEFORE | &quot;before&quot; |



