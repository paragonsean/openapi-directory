

# Source

Source represents an object from which asset information is streamed to Migration Center.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createTime** | **String** | Output only. The timestamp when the source was created. |  [optional] [readonly] |
|**description** | **String** | Free-text description. |  [optional] |
|**displayName** | **String** | User-friendly display name. |  [optional] |
|**errorFrameCount** | **Integer** | Output only. The number of frames that were reported by the source and contained errors. |  [optional] [readonly] |
|**isManaged** | **Boolean** | If &#x60;true&#x60;, the source is managed by other service(s). |  [optional] |
|**name** | **String** | Output only. The full name of the source. |  [optional] [readonly] |
|**pendingFrameCount** | **Integer** | Output only. Number of frames that are still being processed. |  [optional] [readonly] |
|**priority** | **Integer** | The information confidence of the source. The higher the value, the higher the confidence. |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | Output only. The state of the source. |  [optional] [readonly] |
|**type** | [**TypeEnum**](#TypeEnum) | Data source type. |  [optional] |
|**updateTime** | **String** | Output only. The timestamp when the source was last updated. |  [optional] [readonly] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| ACTIVE | &quot;ACTIVE&quot; |
| DELETING | &quot;DELETING&quot; |
| INVALID | &quot;INVALID&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;SOURCE_TYPE_UNKNOWN&quot; |
| UPLOAD | &quot;SOURCE_TYPE_UPLOAD&quot; |
| GUEST_OS_SCAN | &quot;SOURCE_TYPE_GUEST_OS_SCAN&quot; |
| INVENTORY_SCAN | &quot;SOURCE_TYPE_INVENTORY_SCAN&quot; |
| CUSTOM | &quot;SOURCE_TYPE_CUSTOM&quot; |



