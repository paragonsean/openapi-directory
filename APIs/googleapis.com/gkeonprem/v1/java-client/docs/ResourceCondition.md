

# ResourceCondition

ResourceCondition provides a standard mechanism for higher-level status reporting from controller.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**lastTransitionTime** | **String** | Last time the condition transit from one status to another. |  [optional] |
|**message** | **String** | Human-readable message indicating details about last transition. |  [optional] |
|**reason** | **String** | Machine-readable message indicating details about last transition. |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | state of the condition. |  [optional] |
|**type** | **String** | Type of the condition. (e.g., ClusterRunning, NodePoolRunning or ServerSidePreflightReady) |  [optional] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| TRUE | &quot;STATE_TRUE&quot; |
| FALSE | &quot;STATE_FALSE&quot; |
| UNKNOWN | &quot;STATE_UNKNOWN&quot; |



