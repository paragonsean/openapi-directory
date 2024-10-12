

# GoogleCloudRunV2TrafficTargetStatus

Represents the observed state of a single `TrafficTarget` entry.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**percent** | **Integer** | Specifies percent of the traffic to this Revision. |  [optional] |
|**revision** | **String** | Revision to which this traffic is sent. |  [optional] |
|**tag** | **String** | Indicates the string used in the URI to exclusively reference this target. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | The allocation type for this traffic target. |  [optional] |
|**uri** | **String** | Displays the target URI. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;TRAFFIC_TARGET_ALLOCATION_TYPE_UNSPECIFIED&quot; |
| LATEST | &quot;TRAFFIC_TARGET_ALLOCATION_TYPE_LATEST&quot; |
| REVISION | &quot;TRAFFIC_TARGET_ALLOCATION_TYPE_REVISION&quot; |



