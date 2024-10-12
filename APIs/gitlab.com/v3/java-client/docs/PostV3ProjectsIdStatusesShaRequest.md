

# PostV3ProjectsIdStatusesShaRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**state** | [**StateEnum**](#StateEnum) | The state of the status |  |
|**ref** | **String** | The ref |  [optional] |
|**targetUrl** | **String** | The target URL to associate with this status |  [optional] |
|**description** | **String** | A short description of the status |  [optional] |
|**name** | **String** | A string label to differentiate this status from the status of other systems. Default: \&quot;default\&quot; |  [optional] |
|**context** | **String** | A string label to differentiate this status from the status of other systems. Default: \&quot;default\&quot; |  [optional] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| PENDING | &quot;pending&quot; |
| RUNNING | &quot;running&quot; |
| SUCCESS | &quot;success&quot; |
| FAILED | &quot;failed&quot; |
| CANCELED | &quot;canceled&quot; |



