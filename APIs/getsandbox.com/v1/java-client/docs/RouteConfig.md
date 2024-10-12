

# RouteConfig


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**errorStrategy** | [**ErrorStrategyEnum**](#ErrorStrategyEnum) |  |  [optional] |
|**latencyMs** | **Integer** |  |  [optional] |
|**latencyMultiplier** | **Integer** |  |  [optional] |
|**latencyType** | [**LatencyTypeEnum**](#LatencyTypeEnum) |  |  [optional] |
|**method** | **String** |  |  [optional] |
|**path** | **String** |  |  [optional] |



## Enum: ErrorStrategyEnum

| Name | Value |
|---- | -----|
| NONE | &quot;NONE&quot; |
| TIMEOUT | &quot;TIMEOUT&quot; |
| SERVICE_DOWN | &quot;SERVICE_DOWN&quot; |



## Enum: LatencyTypeEnum

| Name | Value |
|---- | -----|
| NONE | &quot;NONE&quot; |
| CONSTANT | &quot;CONSTANT&quot; |
| LINEAR | &quot;LINEAR&quot; |



