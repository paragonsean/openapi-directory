

# CreateDedicatedIpPoolRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**poolName** | **String** | The name of a dedicated IP pool. |  |
|**tags** | [**List&lt;Tag&gt;**](Tag.md) | An object that defines the tags (keys and values) that you want to associate with the pool. |  [optional] |
|**scalingMode** | [**ScalingModeEnum**](#ScalingModeEnum) | The type of scaling mode. |  [optional] |



## Enum: ScalingModeEnum

| Name | Value |
|---- | -----|
| STANDARD | &quot;STANDARD&quot; |
| MANAGED | &quot;MANAGED&quot; |



