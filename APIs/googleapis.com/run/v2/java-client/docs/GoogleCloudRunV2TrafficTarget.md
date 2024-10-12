

# GoogleCloudRunV2TrafficTarget

Holds a single traffic routing entry for the Service. Allocations can be done to a specific Revision name, or pointing to the latest Ready Revision.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**percent** | **Integer** | Specifies percent of the traffic to this Revision. This defaults to zero if unspecified. |  [optional] |
|**revision** | **String** | Revision to which to send this portion of traffic, if traffic allocation is by revision. |  [optional] |
|**tag** | **String** | Indicates a string to be part of the URI to exclusively reference this target. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | The allocation type for this traffic target. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;TRAFFIC_TARGET_ALLOCATION_TYPE_UNSPECIFIED&quot; |
| LATEST | &quot;TRAFFIC_TARGET_ALLOCATION_TYPE_LATEST&quot; |
| REVISION | &quot;TRAFFIC_TARGET_ALLOCATION_TYPE_REVISION&quot; |



