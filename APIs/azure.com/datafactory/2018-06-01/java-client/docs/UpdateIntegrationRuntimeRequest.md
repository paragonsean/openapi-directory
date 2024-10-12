

# UpdateIntegrationRuntimeRequest

Update integration runtime request.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**autoUpdate** | [**AutoUpdateEnum**](#AutoUpdateEnum) | The state of integration runtime auto update. |  [optional] |
|**updateDelayOffset** | **String** | The time offset (in hours) in the day, e.g., PT03H is 3 hours. The integration runtime auto update will happen on that time. |  [optional] |



## Enum: AutoUpdateEnum

| Name | Value |
|---- | -----|
| ON | &quot;On&quot; |
| OFF | &quot;Off&quot; |



