

# Instance

An Instance represents the instance resources of the Registry. Currently, only one instance is allowed for each project.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**build** | [**Build**](Build.md) |  |  [optional] |
|**config** | [**Config**](Config.md) |  |  [optional] |
|**createTime** | **String** | Output only. Creation timestamp. |  [optional] [readonly] |
|**name** | **String** | Format: &#x60;projects/_*_/locations/_*_/instance&#x60;. Currently only &#x60;locations/global&#x60; is supported. |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | Output only. The current state of the Instance. |  [optional] [readonly] |
|**stateMessage** | **String** | Output only. Extra information of Instance.State if the state is &#x60;FAILED&#x60;. |  [optional] [readonly] |
|**updateTime** | **String** | Output only. Last update timestamp. |  [optional] [readonly] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| INACTIVE | &quot;INACTIVE&quot; |
| CREATING | &quot;CREATING&quot; |
| ACTIVE | &quot;ACTIVE&quot; |
| UPDATING | &quot;UPDATING&quot; |
| DELETING | &quot;DELETING&quot; |
| FAILED | &quot;FAILED&quot; |



